# SPDX-License-Identifier: Apache-2.0
"""Microsoft Project password decode (Props-based XOR+permutation).

MPP files store password data in a binary Props stream within the OLE directory.
The root-level Props stream (``Props9``/``Props12``/``Props14``) is always plaintext
and contains the password flag, encryption code, and password data block. The
password itself is XOR-masked with ``0xFF - encryption_code`` and scattered across
16 fixed offsets in a 64-byte block (the PASSWORD_MASK permutation).

This is NOT real encryption -- the XOR key is embedded in the same file. Recovery
is instantaneous (DECODE class). The algorithm is ported from MPXJ's
``MPPUtility.decodePassword()`` and ``Props.java`` (LGPL-2.1).

No published [MS-*] spec exists for this format.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    import olefile

logger = logging.getLogger(__name__)

# --- Props key constants (MPXJ PropsKey enum) ---

PROPS_KEY_PASSWORD_FLAG: Final = 0x35400000
PROPS_KEY_PASSWORD_DATA: Final = 0x35400004
PROPS_KEY_WRITE_PASSWORD_DATA: Final = 0x35400005
PROPS_KEY_ENCRYPTION_CODE: Final = 0x35400007

# --- Props stream names per MPP version ---

_PROPS_STREAMS: Final[dict[str, str]] = {
    "   19": "Props9",
    "   112": "Props12",
    "   114": "Props14",
}

# --- Password decode constants (MPXJ MPPUtility) ---

_PASSWORD_BLOCK_SIZE: Final = 64
_PASSWORD_MASK: Final = (60, 30, 48, 2, 6, 14, 8, 22, 44, 12, 38, 10, 62, 16, 34, 24)
_PROPS_HEADER_SIZE: Final = 16
_PROPS_ITEM_PREFIX_SIZE: Final = 12


def parse_props(data: bytes) -> dict[int, bytes]:
    """Parse a Props9/Props12/Props14 binary stream into key-value pairs.

    Layout (MPXJ Props.java): 16-byte header, LE u16 item count at offset 12.
    Each item: LE i32 size, LE i32 key, LE i32 attrib (ignored), then `size`
    bytes of value data with 1-byte alignment padding when size is odd.
    """
    if len(data) < _PROPS_HEADER_SIZE:
        return {}
    header_count = int.from_bytes(data[12:14], "little")
    result: dict[int, bytes] = {}
    offset = _PROPS_HEADER_SIZE
    for _ in range(header_count):
        if offset + _PROPS_ITEM_PREFIX_SIZE > len(data):
            break
        item_size = int.from_bytes(data[offset : offset + 4], "little", signed=True)
        item_key = int.from_bytes(data[offset + 4 : offset + 8], "little", signed=True)
        offset += _PROPS_ITEM_PREFIX_SIZE
        if item_size < 1 or offset + item_size > len(data):
            break
        result[item_key & 0xFFFFFFFF] = data[offset : offset + item_size]
        offset += item_size
        if item_size % 2 != 0:
            offset += 1
    logger.debug("props: %d items parsed from %d bytes", len(result), len(data))
    return result


def locate_props_stream(ole: olefile.OleFileIO, mpp_dir: str) -> bytes | None:
    """Read the root-level Props stream for the given MPP version directory."""
    stream_name = _PROPS_STREAMS.get(mpp_dir)
    if stream_name is None:
        return None
    try:
        if not ole.exists(stream_name):
            logger.debug("props stream %s not found", stream_name)
            return None
        return bytes(ole.openstream(stream_name).read())
    except (OSError, ValueError, KeyError):
        return None


def password_flag(props: dict[int, bytes]) -> int:
    """Read the PASSWORD_FLAG byte: bit 0 = open password, bit 1 = write reservation."""
    raw = props.get(PROPS_KEY_PASSWORD_FLAG)
    if raw is None or len(raw) < 1:
        return 0
    return raw[0]


def has_open_password(props: dict[int, bytes]) -> bool:
    """Whether bit 0 of PASSWORD_FLAG is set (open password present)."""
    return bool(password_flag(props) & 0x01)


def has_write_reservation(props: dict[int, bytes]) -> bool:
    """Whether bit 1 of PASSWORD_FLAG is set (write-reservation password present)."""
    return bool(password_flag(props) & 0x02)


def _decode_password_block(props: dict[int, bytes], props_key: int) -> str | None:
    """Shared XOR+permutation decode for both open and write-reservation passwords."""
    block_raw = props.get(props_key)
    if block_raw is None or len(block_raw) < _PASSWORD_BLOCK_SIZE:
        return None
    code_raw = props.get(PROPS_KEY_ENCRYPTION_CODE)
    code = code_raw[0] if code_raw and len(code_raw) >= 1 else 0
    mask = (0xFF - code) & 0xFF if code != 0 else 0
    block = bytearray(block_raw[:_PASSWORD_BLOCK_SIZE])
    for i in range(_PASSWORD_BLOCK_SIZE):
        block[i] ^= mask
    chars: list[str] = []
    for offset in _PASSWORD_MASK:
        ch = block[offset]
        if ch == 0x00:
            break
        chars.append(chr(ch))
    password = "".join(chars)
    return password or None


def decode_mpp9_password(props: dict[int, bytes]) -> str | None:
    """Recover the MPP9 open password from the Props data (DECODE, not crack).

    Algorithm (MPXJ MPPUtility.decodePassword): read the ENCRYPTION_CODE byte,
    compute ``mask = 0xFF - code``, XOR-decode the 64-byte password block, then
    read single-byte characters at the 16 PASSWORD_MASK offsets until a null byte.
    Returns None if the password data is absent or too short.
    """
    if not has_open_password(props):
        return None
    result = _decode_password_block(props, PROPS_KEY_PASSWORD_DATA)
    if result is not None:
        logger.debug("mpp9 decode: recovered %d-char password", len(result))
    return result


def decode_mpp9_write_password(props: dict[int, bytes]) -> str | None:
    """Recover the MPP9 write-reservation password (same XOR+permutation at a different key)."""
    if not has_write_reservation(props):
        return None
    return _decode_password_block(props, PROPS_KEY_WRITE_PASSWORD_DATA)


def detect_mpp_version(ole: olefile.OleFileIO) -> str | None:
    """Return the MPP version directory name if this OLE file is a Project file."""
    try:
        top_streams = {entry[0] for entry in ole.listdir() if entry}
    except (OSError, ValueError):
        return None
    for mpp_dir in _PROPS_STREAMS:
        if mpp_dir in top_streams:
            return mpp_dir
    return None
