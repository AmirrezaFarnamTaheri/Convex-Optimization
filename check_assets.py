import os
import re
import glob

def verify_assets():
    html_files = glob.glob("topics/*/index.html")
    errors = []

    print(f"Checking {len(html_files)} HTML files...")

    for html_file in html_files:
        base_dir = os.path.dirname(html_file)
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all img tags and extract src
        # Regex is simple, might miss edge cases but good enough for this structure
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)

        for src in img_srcs:
            # Handle absolute/relative paths
            if src.startswith('http') or src.startswith('//'):
                continue # Skip external links

            # Construct absolute path
            # Assuming src is relative to html_file
            asset_path = os.path.join(base_dir, src)

            # Check existence
            if not os.path.exists(asset_path):
                errors.append(f"Missing asset in {html_file}: {src} (Expected at {asset_path})")
            else:
                pass # print(f"Found: {asset_path}")

    if errors:
        print("\nERRORS FOUND:")
        for e in errors:
            print(e)
        exit(1)
    else:
        print("\nAll local image assets verified successfully.")
        exit(0)

if __name__ == "__main__":
    verify_assets()
