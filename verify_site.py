import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable, List, Tuple


HREF_SRC_RE = re.compile(r"""\b(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)


def is_external(url: str) -> bool:
    u = url.strip().lower()
    return (
        u.startswith("http://")
        or u.startswith("https://")
        or u.startswith("//")
        or u.startswith("mailto:")
        or u.startswith("tel:")
        or u.startswith("javascript:")
        or u.startswith("data:")
    )


def strip_fragment(url: str) -> str:
    # file.html#section -> file.html
    return url.split("#", 1)[0]


def strip_query(url: str) -> str:
    # file.html?mode=foo -> file.html
    return url.split("?", 1)[0]


def iter_html_paths(root: str) -> List[str]:
    pages: List[str] = []

    # Root pages
    for name in ["index.html", "syllabus.html"]:
        p = os.path.join(root, name)
        if os.path.exists(p):
            pages.append(p)

    # Lecture pages (topics/*/index.html)
    topics_dir = os.path.join(root, "topics")
    if os.path.isdir(topics_dir):
        for topic in sorted(os.listdir(topics_dir)):
            topic_index = os.path.join(topics_dir, topic, "index.html")
            if os.path.exists(topic_index):
                pages.append(topic_index)

    # Widget pages (topics/*/widgets/*.html)
    if os.path.isdir(topics_dir):
        for topic in sorted(os.listdir(topics_dir)):
            widgets_dir = os.path.join(topics_dir, topic, "widgets")
            if not os.path.isdir(widgets_dir):
                continue
            for name in sorted(os.listdir(widgets_dir)):
                if name.lower().endswith(".html"):
                    pages.append(os.path.join(widgets_dir, name))

    # Legacy pages we still ship (e.g., redirects)
    legacy = os.path.join(root, "topics", "09-duality", "index_latest.html")
    if os.path.exists(legacy):
        pages.append(legacy)

    return pages


def extract_local_refs(html_path: str) -> List[str]:
    with open(html_path, "r", encoding="utf-8") as f:
        text = f.read()

    refs: List[str] = []
    for raw in HREF_SRC_RE.findall(text):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        if is_external(raw):
            continue
        raw = strip_query(strip_fragment(raw))
        if not raw:
            continue
        refs.append(raw)
    return refs


@dataclass(frozen=True)
class MissingRef:
    page: str
    ref: str
    resolved_path: str


def check_page(html_path: str) -> Tuple[int, List[MissingRef]]:
    missing: List[MissingRef] = []
    base_dir = os.path.dirname(html_path)

    refs = extract_local_refs(html_path)
    for ref in refs:
        # Absolute paths within repo are not expected; treat as relative to repo root
        if ref.startswith("/"):
            resolved = os.path.normpath(os.path.join(os.path.dirname(base_dir), ref.lstrip("/")))
        else:
            resolved = os.path.normpath(os.path.join(base_dir, ref))

        # If it's a directory link, allow index.html as a fallback.
        if os.path.isdir(resolved):
            resolved = os.path.join(resolved, "index.html")

        if not os.path.exists(resolved):
            missing.append(
                MissingRef(
                    page=os.path.relpath(html_path, os.getcwd()),
                    ref=ref,
                    resolved_path=os.path.relpath(resolved, os.getcwd()),
                )
            )

    return len(refs), missing


def main() -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    pages = iter_html_paths(root)
    if not pages:
        print("No pages found to verify.")
        return 1

    total_refs = 0
    all_missing: List[MissingRef] = []

    for p in pages:
        count, missing = check_page(p)
        total_refs += count
        all_missing.extend(missing)

    if all_missing:
        print("Missing local references detected:\n")
        for m in all_missing:
            print(f"- page: {m.page}")
            print(f"  ref:  {m.ref}")
            print(f"  ->   {m.resolved_path}")
        print(f"\nSummary: {len(all_missing)} missing refs across {len(pages)} pages (checked {total_refs} local refs).")
        return 2

    print(f"OK: {len(pages)} pages verified (checked {total_refs} local refs). No missing local refs found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


