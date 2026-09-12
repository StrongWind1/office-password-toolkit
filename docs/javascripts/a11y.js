/* Make scrollable code blocks keyboard-focusable (WCAG scrollable-region-focusable).
   Applied unconditionally because overflow can change with viewport width. */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".md-typeset pre > code").forEach(function (code) {
    code.setAttribute("tabindex", "0");
    code.setAttribute("role", "region");
    code.setAttribute("aria-label", "Code block");
  });
});
