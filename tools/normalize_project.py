import os
import re
from pathlib import Path


RE_WIDGET_BAD_THEME = re.compile(r'href="\.\./\.\./\.\./\.\./shared/styles/widget-theme\.css"')
RE_WIDGET_THEME_OK = 'href="../../../shared/styles/widget-theme.css"'

RE_WIDGET_BAD_STATIC = re.compile(r'(?<=["\'])\.\./\.\./\.\./\.\./static/')
RE_WIDGET_STATIC_OK = "../../../static/"

RE_BAD_STATIC_SCRIPT = re.compile(
    r'^\s*<script\s+src="\.\./\.\./static/js/(ui|notes-widget|pomodoro|progress-tracker|glossary-loader)\.js"\s*></script>\s*$',
    re.IGNORECASE | re.MULTILINE,
)


def normalize_widget_html(html: str) -> str:
    html2 = RE_WIDGET_BAD_THEME.sub(RE_WIDGET_THEME_OK, html)
    html2 = RE_WIDGET_BAD_STATIC.sub(RE_WIDGET_STATIC_OK, html2)
    html2 = RE_BAD_STATIC_SCRIPT.sub("", html2)
    # Clean up any large blank runs introduced by removals
    html2 = re.sub(r"\n{3,}", "\n\n", html2)
    return html2


def normalize_lecture_index(html: str) -> str:
    out = html

    # 1) Ensure skip link right after <body>
    if '<a href="#main" class="skip-link">' not in out:
        out = out.replace(
            "<body>",
            '<body>\n  <a href="#main" class="skip-link">Skip to content</a>',
            1,
        )

    # 2) Ensure sticky header class
    out = re.sub(
        r'<header\s+class="site-header(?![^"]*\bsticky\b)([^"]*)"',
        r'<header class="site-header sticky\1"',
        out,
        flags=re.IGNORECASE,
    )

    # 3) Add role="banner" to site header (if missing)
    out = re.sub(
        r'<header\s+class="site-header([^"]*)"(?![^>]*\brole=)',
        r'<header class="site-header\1" role="banner"',
        out,
        flags=re.IGNORECASE,
    )

    # 4) Normalize header container to include header-inner
    out = re.sub(
        r'(<header\s+class="site-header[^"]*"[^>]*>\s*)<div\s+class="container"(?![^"]*\bheader-inner\b)',
        r'\1<div class="container header-inner"',
        out,
        flags=re.IGNORECASE,
    )

    # 5) Add nav semantics for the lecture navigation
    out = re.sub(
        r'<nav\s+class="nav"(?![^>]*\brole=)',
        r'<nav class="nav" role="navigation" aria-label="Lecture Navigation"',
        out,
        flags=re.IGNORECASE,
    )

    # 6) Add id+role to the lecture main content area
    out = re.sub(
        r'<main\s+class="lecture-content"(?![^>]*\bid=)',
        r'<main id="main" class="lecture-content" role="main"',
        out,
        flags=re.IGNORECASE,
    )

    return out


def write_if_changed(path: Path, new_text: str) -> bool:
    old = path.read_text(encoding="utf-8")
    if old == new_text:
        return False
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    os.chdir(root)

    changed = 0

    # Widgets
    for p in root.glob("topics/*/widgets/*.html"):
        txt = p.read_text(encoding="utf-8")
        new = normalize_widget_html(txt)
        if write_if_changed(p, new):
            changed += 1

    # Lecture pages
    for p in root.glob("topics/*/index.html"):
        txt = p.read_text(encoding="utf-8")
        new = normalize_lecture_index(txt)
        if write_if_changed(p, new):
            changed += 1

    print(f"normalize_project: updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


