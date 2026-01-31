import argparse
import os
from pathlib import Path


def iter_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for p in [root / "index.html", root / "syllabus.html"]:
        if p.exists():
            pages.append(p)

    for p in sorted(root.glob("topics/*/index.html")):
        pages.append(p)

    return pages


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Take Playwright screenshots of the main site pages (useful for visual regression checks)."
    )
    parser.add_argument("--out", default="verification", help="Output directory for screenshots.")
    parser.add_argument("--only", default="", help="Optional substring filter (path must contain it).")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    os.chdir(root)

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:  # noqa: BLE001
        raise SystemExit(
            "Playwright is not installed. Install it with:\n"
            "  pip install playwright\n"
            "  playwright install\n\n"
            f"Original error: {e}"
        )

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    pages = [p for p in iter_pages(root) if (args.only in str(p))] if args.only else iter_pages(root)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for html_path in pages:
            file_url = f"file://{html_path.resolve()}"
            page.goto(file_url)
            page.wait_for_selector("main")
            page.wait_for_selector("h1")

            rel = html_path.relative_to(root).as_posix().replace("/", "__")
            png = out_dir / f"{rel}.png"
            page.screenshot(path=str(png), full_page=True)
            print(f"Wrote {png}")

        browser.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


