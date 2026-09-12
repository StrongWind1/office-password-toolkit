# SPDX-License-Identifier: Apache-2.0
"""Jet User-Level Security (ULS) password, workgroup identity, and PID decode.

Jet ULS stores per-user passwords in the ``MSysAccounts`` table of workgroup
information files (``.mdw``). The password field is a binary blob containing
8-byte 3DES-encrypted blocks. Unused blocks are filled with the workgroup key
constant ``6952AD67F3D5E1E6``.

Three independent 3DES ciphers protect different parts of the workgroup file:

* **User passwords** -- key ``kjhggautnitremvk`` (16 bytes), DECODE class.
  Jet 4 (.mdw 2000+) stores 5 blocks (40 bytes, UTF-16LE).
  Jet 3 (.mdw 95/97) stores 2 blocks (16 bytes, single-byte cp1252).
* **Workgroup identity** (WID, owner name, organisation) -- key
  ``rkatpvjgjshcsabn`` (16 bytes), 12 blocks (96 bytes) in the Admins SID
  blob, decoded to three null-terminated ASCII strings.
* **Personal ID (PID)** -- NOT 3DES; a custom obfuscation with positional XOR
  (constant ``0x7FA52EBD``), bit rotation, byte-split, and stride extraction.

All three were reverse-engineered from ``msjet40.dll`` and independently
confirmed against thewd-hub/source ``aspwsupport.cpp`` (v1.01, (C)thewd).
"""

from __future__ import annotations

from dataclasses import dataclass

from Crypto.Cipher import DES3

# --- 3DES keys ---------------------------------------------------------------

_PASSWORD_KEY: bytes = b"kjhggaut" + b"nitremvk"
_WORKGROUP_IDENTITY_KEY: bytes = b"rkatpvjg" + b"jshcsabn"

WORKGROUP_KEY: bytes = bytes.fromhex("6952ad67f3d5e1e6")

_BLOCK_SIZE: int = 8
_JET4_FIELD_SIZE: int = 40
_JET3_FIELD_SIZE: int = 16
_WORKGROUP_BLOCKS: int = 12
_UTF16LE_CHAR_SIZE: int = 2
_PID_MAGIC: int = 0x7FA52EBD
_PID_MARKER_FF: int = 0xFF
_PID_DEFAULT_BASE: int = 4

# --- MDW file layout constants -----------------------------------------------

_MDW_SIGNATURE: bytes = b"Jet System DB"
_MDW_SIGNATURE_OFFSET: int = 0x04
_MDW_RC4_KEY: bytes = b"\xc7\xda\x39\x6b"
_MDW_RC4_REGION_START: int = 0x18
_MDW_RC4_REGION_LEN: int = 90
_MDW_ENCODING_KEY_OFFSET: int = 0x3E
_MDW_ENCODING_KEY_SIZE: int = 4
_JET4_ACCOUNT_SECTION_OFFSET: int = 0x15000
_JET3_ACCOUNT_SECTION_OFFSET: int = 0xE000
_ACCOUNT_SECTION_SIZE: int = 0x1500
_RC4_STATE_SIZE: int = 256
_CRC_CHECK: bytes = b"\x01\x01"
_OFFSET_MASK: int = 0x3FFF
_MAX_ACCOUNTS: int = 1024
_ACCOUNT_HEADER_THRESHOLD: int = 0x0F

# Jet version string at 0x9C: "4.0" = Jet 4 (Access 2000+).
_JET_VERSION_OFFSET: int = 0x9C
_JET4_VERSION_STRING: bytes = b"4.0"

# Account section header offsets.
_JET4_FIRST_OFFSET: int = 0x0C
_JET3_FIRST_OFFSET: int = 0x08

_BUILTIN_USERS: frozenset[str] = frozenset({"admin", "engine", "creator", "guest"})
_BUILTIN_GROUPS: frozenset[str] = frozenset({"admins", "users", "guests"})


# --- Password decode/encode -------------------------------------------------


def decode_password(field: bytes, *, jet3: bool = False) -> str:
    """Decode an ``MSysAccounts.Password`` field to the original password."""
    field_size = _JET3_FIELD_SIZE if jet3 else _JET4_FIELD_SIZE
    if len(field) < field_size:
        field = field.ljust(field_size, b"\x00")

    cipher = DES3.new(_PASSWORD_KEY, DES3.MODE_ECB)
    plaintext = bytearray()

    for offset in range(0, field_size, _BLOCK_SIZE):
        block = field[offset : offset + _BLOCK_SIZE]
        if block == WORKGROUP_KEY:
            break
        plaintext.extend(cipher.decrypt(block))

    if jet3:
        return bytes(plaintext).rstrip(b"\x00").decode("cp1252", errors="replace")

    while len(plaintext) >= _UTF16LE_CHAR_SIZE and plaintext[-1] == 0 and plaintext[-2] == 0:
        plaintext = plaintext[:-_UTF16LE_CHAR_SIZE]
    if not plaintext:
        return ""
    return bytes(plaintext).decode("utf-16-le", errors="replace")


def encode_password(password: str, *, jet3: bool = False) -> bytes:
    """Encode a plaintext password to the ``MSysAccounts.Password`` field."""
    field_size = _JET3_FIELD_SIZE if jet3 else _JET4_FIELD_SIZE
    pw_bytes = password.encode("cp1252" if jet3 else "utf-16-le")
    if len(pw_bytes) > field_size:
        pw_bytes = pw_bytes[:field_size]

    cipher = DES3.new(_PASSWORD_KEY, DES3.MODE_ECB)
    result = bytearray()

    for offset in range(0, field_size, _BLOCK_SIZE):
        block = pw_bytes[offset : offset + _BLOCK_SIZE] if offset < len(pw_bytes) else b""
        if not block or block == b"\x00" * _BLOCK_SIZE:
            result.extend(WORKGROUP_KEY)
        else:
            block = block.ljust(_BLOCK_SIZE, b"\x00")
            result.extend(cipher.encrypt(block))

    return bytes(result)


def is_blank(field: bytes) -> bool:
    """Return True if the password field represents a blank (empty) password."""
    return field[:_BLOCK_SIZE] == WORKGROUP_KEY


# --- Workgroup identity decode -----------------------------------------------


@dataclass(frozen=True)
class WorkgroupIdentity:
    """Decoded workgroup owner information from the Admins group SID."""

    workgroup_id: str
    owner_name: str
    organisation: str


def _decode_workgroup_payload(payload: bytes) -> WorkgroupIdentity | None:
    """3DES-decrypt a raw 96-byte workgroup identity payload."""
    payload_size = _WORKGROUP_BLOCKS * _BLOCK_SIZE
    if len(payload) < payload_size:
        return None

    data = bytearray(payload[:payload_size])
    cipher = DES3.new(_WORKGROUP_IDENTITY_KEY, DES3.MODE_ECB)

    for i in range(_WORKGROUP_BLOCKS):
        offset = i * _BLOCK_SIZE
        data[offset : offset + _BLOCK_SIZE] = cipher.decrypt(bytes(data[offset : offset + _BLOCK_SIZE]))

    def _extract(buf: bytes, start: int, max_len: int) -> str:
        end = buf.find(b"\x00", start, start + max_len)
        return bytes(buf[start : end if end >= 0 else start + max_len]).decode("ascii", errors="replace")

    return WorkgroupIdentity(
        workgroup_id=_extract(data, 0, 0x15),
        owner_name=_extract(data, 0x15, 0x28),
        organisation=_extract(data, 0x15 + 0x28, 0x28),
    )


def decode_workgroup_identity(sid_blob: bytes, *, jet3: bool = False) -> WorkgroupIdentity | None:
    """Decode the Admins group SID to recover the workgroup WID, name, and organisation."""
    skip = 1 if jet3 else _UTF16LE_CHAR_SIZE
    payload_size = _WORKGROUP_BLOCKS * _BLOCK_SIZE
    if len(sid_blob) < skip + payload_size:
        return None
    return _decode_workgroup_payload(sid_blob[skip : skip + payload_size])


# --- PID recovery ------------------------------------------------------------


def decode_pid(sid_field: bytes) -> str:
    """Recover the Personal ID (PID) from an account's SID field.

    Algorithm ported from thewd-hub ``aspwsupport.cpp`` ``recoverPID()`` (v1.01).
    """
    pid_length = len(sid_field)
    if pid_length <= _UTF16LE_CHAR_SIZE:
        return ""

    buf = bytearray(sid_field)

    if buf[0] == _PID_MARKER_FF:
        buf = buf[1:]
        pid_length -= 1
        base_value = _PID_DEFAULT_BASE
    else:
        base_value = buf[1]
        buf = buf[_UTF16LE_CHAR_SIZE:]
        pid_length -= _UTF16LE_CHAR_SIZE

    if pid_length <= 0 or base_value > pid_length:
        return ""

    sub_value = pid_length - base_value
    if sub_value == 0:
        return ""

    xor_value = (_PID_MAGIC // sub_value) & 0xFF
    for i in range(pid_length):
        buf[i] ^= (xor_value * i) & 0xFF

    shift_right = (sub_value % 7) + 1
    shift_left = _BLOCK_SIZE - shift_right
    last_value = (buf[pid_length - 1] << shift_left) & 0xFF
    for i in range(pid_length):
        current = buf[i]
        buf[i] = (last_value | (current >> shift_right)) & 0xFF
        last_value = (current << shift_left) & 0xFF

    split1 = pid_length - (pid_length >> 1)
    split2 = pid_length - split1
    reversed_buf = bytearray(pid_length)
    reversed_buf[:split2] = buf[split1 : split1 + split2]
    reversed_buf[split2:] = buf[:split1]

    increment = 1 if base_value <= 1 else sub_value // (base_value - 1)
    recovered = bytearray(base_value)
    idx = 0
    for i in range(base_value):
        recovered[base_value - 1 - i] = reversed_buf[idx]
        idx += 1 + increment

    return bytes(recovered).decode("ascii", errors="replace").rstrip("\x00")


def encode_sid(pid: str, account_name: str) -> bytes:
    """Generate the full SID from a PID and account name.

    The pre-obfuscation buffer scatters reversed PID chars at stride positions
    and fills the gaps with account name chars. The stride is determined by
    ``sub_value // (base_value - 1)`` where sub_value = name_length. Then the
    buffer is obfuscated with split-and-swap, circular bit-shift, and XOR.
    Confirmed byte-identical on 8 real test vectors from lab ``.mdw`` files.
    """
    pid_bytes = pid.encode("ascii")
    name_bytes = account_name.encode("ascii")
    base_value = len(pid_bytes)
    if base_value == 0:
        return b""

    data_length = base_value + len(name_bytes)
    sub_value = len(name_bytes)
    if sub_value <= 0:
        return b""

    increment = 1 if base_value <= 1 else sub_value // (base_value - 1)

    # Scatter reversed PID at stride positions, fill gaps with name chars.
    raw = bytearray(data_length)
    name_idx = 0
    stride_pos = 0
    for i in range(base_value):
        raw[stride_pos] = pid_bytes[base_value - 1 - i]
        for j in range(increment):
            fill_pos = stride_pos + 1 + j
            if fill_pos < data_length and name_idx < len(name_bytes):
                raw[fill_pos] = name_bytes[name_idx]
                name_idx += 1
        stride_pos += 1 + increment
    while name_idx < len(name_bytes) and stride_pos < data_length:
        raw[stride_pos] = name_bytes[name_idx]
        name_idx += 1
        stride_pos += 1

    return _apply_obfuscation(raw, base_value)


def encode_pid(pid: str, total_length: int | None = None) -> bytes:
    """Encode a PID into an obfuscated SID field (without account name).

    For a full SID with account name, use ``encode_sid()`` instead.
    This produces a SID where the name portion is zero-filled.
    """
    pid_bytes = pid.encode("ascii")
    base_value = len(pid_bytes)
    if base_value == 0:
        return b""

    if total_length is None:
        total_length = base_value + (base_value // 2) + 1
    sub_value = total_length - base_value
    if sub_value <= 0:
        total_length = base_value + 1

    raw = bytearray(pid_bytes[::-1] + b"\x00" * (total_length - base_value))
    return _apply_obfuscation(raw, base_value)


def _apply_obfuscation(raw: bytearray, base_value: int) -> bytes:
    """Apply the obfuscation layers to raw SID data."""
    data_length = len(raw)
    sub_value = data_length - base_value
    if sub_value <= 0:
        return b""

    split1 = data_length - (data_length >> 1)
    split2 = data_length - split1
    buf = bytearray(data_length)
    buf[:split1] = raw[split2:]
    buf[split1 : split1 + split2] = raw[:split2]

    shift_right = (sub_value % 7) + 1
    shift_left = _BLOCK_SIZE - shift_right
    last_value = (buf[0] >> shift_left) & 0xFF
    for i in range(data_length - 1, -1, -1):
        current = buf[i]
        buf[i] = ((current << shift_right) | last_value) & 0xFF
        last_value = (current >> shift_left) & 0xFF

    xor_value = (_PID_MAGIC // sub_value) & 0xFF
    for i in range(data_length):
        buf[i] ^= (xor_value * i) & 0xFF

    return bytes([0xFE, base_value]) + bytes(buf)


# --- MDW file parsing --------------------------------------------------------


def _rc4(key: bytes, data: bytes) -> bytes:
    """RC4 encrypt/decrypt."""
    state = list(range(_RC4_STATE_SIZE))
    j = 0
    for i in range(_RC4_STATE_SIZE):
        j = (j + state[i] + key[i % len(key)]) % _RC4_STATE_SIZE
        state[i], state[j] = state[j], state[i]
    out = bytearray(len(data))
    i = j = 0
    for index, byte in enumerate(data):
        i = (i + 1) % _RC4_STATE_SIZE
        j = (j + state[i]) % _RC4_STATE_SIZE
        state[i], state[j] = state[j], state[i]
        out[index] = byte ^ state[(state[i] + state[j]) % _RC4_STATE_SIZE]
    return bytes(out)


@dataclass(frozen=True)
class MdwAccount:
    """A decoded account from a workgroup (.mdw) file."""

    name: str
    password: str
    pid: str
    is_group: bool
    is_builtin: bool


@dataclass(frozen=True)
class MdwFile:
    """Complete decoded workgroup file contents."""

    jet3: bool
    accounts: list[MdwAccount]
    workgroup: WorkgroupIdentity | None


def is_mdw(data: bytes) -> bool:
    """Return True if ``data`` starts with the Jet workgroup signature."""
    end = _MDW_SIGNATURE_OFFSET + len(_MDW_SIGNATURE)
    return len(data) >= end and data[_MDW_SIGNATURE_OFFSET:end] == _MDW_SIGNATURE


def _is_jet4(data: bytes) -> bool:
    """Return True if the MDW is Jet 4 (Access 2000+), False for Jet 3."""
    end = _JET_VERSION_OFFSET + len(_JET4_VERSION_STRING)
    return len(data) >= end and data[_JET_VERSION_OFFSET:end] == _JET4_VERSION_STRING


def _decode_name(data: bytes, *, jet4: bool) -> str:
    """Decode an account name from the decrypted section."""
    enc = "utf-16-le" if jet4 else "cp1252"
    return bytes(data).decode(enc, errors="replace").rstrip("\x00")


def _decrypt_account_section(data: bytes, *, is_jet4: bool) -> bytearray | None:
    """Decrypt the MDW account section using header-derived RC4 key."""
    base_offset = _JET4_ACCOUNT_SECTION_OFFSET if is_jet4 else _JET3_ACCOUNT_SECTION_OFFSET
    if len(data) < base_offset + _ACCOUNT_SECTION_SIZE:
        return None

    header_region = _rc4(_MDW_RC4_KEY, data[_MDW_RC4_REGION_START : _MDW_RC4_REGION_START + _MDW_RC4_REGION_LEN])
    key_start = _MDW_ENCODING_KEY_OFFSET - _MDW_RC4_REGION_START
    xor_key = bytes(header_region[key_start : key_start + _MDW_ENCODING_KEY_SIZE])

    rc4_key = _find_xor_base(data, base_offset, xor_key)
    if rc4_key is None:
        return None

    section = data[base_offset : base_offset + _ACCOUNT_SECTION_SIZE]
    return bytearray(_rc4(rc4_key, section))


def _find_xor_base(data: bytes, base_offset: int, initial_key: bytes) -> bytes | None:
    """Brute-force byte 0 of the RC4 key to find the CRC 0x0101 sentinel."""
    key = bytearray(initial_key)
    for candidate in range(_RC4_STATE_SIZE):
        key[0] = candidate
        decrypted = _rc4(bytes(key), data[base_offset : base_offset + _UTF16LE_CHAR_SIZE])
        if decrypted == _CRC_CHECK:
            return bytes(key)
    return None


def _build_account_offsets(section: bytearray, *, is_jet4: bool) -> tuple[int, list[tuple[int, int]]]:
    """Parse the account offset table from the decrypted section header."""
    file_offset = _JET4_FIRST_OFFSET if is_jet4 else _JET3_FIRST_OFFSET
    first_len = int.from_bytes(section[4:6], "little")
    if is_jet4:
        first_len *= _UTF16LE_CHAR_SIZE
    count = int.from_bytes(section[file_offset : file_offset + _UTF16LE_CHAR_SIZE], "little")
    file_offset += _UTF16LE_CHAR_SIZE

    offsets: list[tuple[int, int]] = []
    if count > 0 and first_len > 0:
        raw = int.from_bytes(section[file_offset : file_offset + _UTF16LE_CHAR_SIZE], "little")
        offsets.append((raw & _OFFSET_MASK, first_len))

    for _ in range(1, min(count, _MAX_ACCOUNTS)):
        prev = int.from_bytes(section[file_offset : file_offset + _UTF16LE_CHAR_SIZE], "little") & _OFFSET_MASK
        file_offset += _UTF16LE_CHAR_SIZE
        if file_offset + _UTF16LE_CHAR_SIZE > len(section):
            break
        if section[file_offset + 1] <= _ACCOUNT_HEADER_THRESHOLD:
            cur = int.from_bytes(section[file_offset : file_offset + _UTF16LE_CHAR_SIZE], "little") & _OFFSET_MASK
            length = (prev - cur - 1) & _OFFSET_MASK
            if cur == 0 or length == 0:
                break
            offsets.append((cur, length))

    return first_len, offsets


def _parse_account(section: bytearray, acc_offset: int, acc_length: int, *, is_jet4: bool) -> MdwAccount:
    """Decode one account entry from the decrypted section."""
    if is_jet4:
        name_length = section[acc_offset + acc_length - 6] - _UTF16LE_CHAR_SIZE
        pw_off = section[acc_offset + acc_length - 8]
        pw_len = _JET4_FIELD_SIZE
        pid_off = section[acc_offset + acc_length - 6]
    else:
        name_length = section[acc_offset + acc_length - 3] - 1
        pw_off = section[acc_offset + acc_length - 4]
        pw_len = _JET3_FIELD_SIZE
        pid_off = section[acc_offset + acc_length - 3]

    pid_length = pw_off - pid_off
    name_skip = _UTF16LE_CHAR_SIZE if is_jet4 else 1
    name_data = section[acc_offset + name_skip : acc_offset + name_skip + name_length]
    acc_name = _decode_name(name_data, jet4=is_jet4)

    is_group = (pw_off + pw_len) > acc_length
    is_builtin = acc_name.lower() in _BUILTIN_USERS or acc_name.lower() in _BUILTIN_GROUPS

    password = ""
    if not is_group:
        pw_data = bytes(section[acc_offset + pw_off : acc_offset + pw_off + pw_len])
        password = decode_password(pw_data, jet3=not is_jet4)

    pid = ""
    if pid_length > _UTF16LE_CHAR_SIZE:
        pid_data = bytes(section[acc_offset + pid_off : acc_offset + pid_off + pid_length])
        pid = decode_pid(pid_data)

    return MdwAccount(name=acc_name, password=password, pid=pid, is_group=is_group, is_builtin=is_builtin)


def parse_mdw(data: bytes) -> MdwFile | None:
    """Parse a complete ``.mdw`` file and decode all accounts.

    Returns ``None`` if the file is not a valid Jet workgroup database.
    Handles both Jet 3 (Access 95/97) and Jet 4 (Access 2000+) formats.
    """
    if not is_mdw(data):
        return None

    jet4 = _is_jet4(data)
    section = _decrypt_account_section(data, is_jet4=jet4)
    if section is None:
        return None

    first_len, account_offsets = _build_account_offsets(section, is_jet4=jet4)

    accounts: list[MdwAccount] = []
    workgroup_identity: WorkgroupIdentity | None = None

    for idx, (acc_offset, acc_length) in enumerate(account_offsets):
        if acc_offset + acc_length > len(section):
            continue

        if idx == 0:
            wg_start = acc_offset + first_len + 1
            wg_skip = _UTF16LE_CHAR_SIZE if jet4 else 1
            wg_payload_start = wg_start + wg_skip
            wg_payload_end = wg_payload_start + _WORKGROUP_BLOCKS * _BLOCK_SIZE
            if wg_payload_end <= len(section):
                workgroup_identity = _decode_workgroup_payload(bytes(section[wg_payload_start:wg_payload_end]))

            name_data = section[acc_offset : acc_offset + first_len]
            name_skip = _UTF16LE_CHAR_SIZE if jet4 else 1
            acc_name = _decode_name(name_data[name_skip:], jet4=jet4)
            accounts.append(MdwAccount(name=acc_name, password="", pid="", is_group=False, is_builtin=True))
            continue

        accounts.append(_parse_account(section, acc_offset, acc_length, is_jet4=jet4))

    return MdwFile(jet3=not jet4, accounts=accounts, workgroup=workgroup_identity)
