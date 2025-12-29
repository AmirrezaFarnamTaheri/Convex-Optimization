import os
import re

def verify_images(html_file):
    if not os.path.exists(html_file):
        print(f"Error: {html_file} does not exist.")
        return

    with open(html_file, 'r') as f:
        content = f.read()

    # Find all img src attributes
    img_srcs = re.findall(r'<img[^>]+src="([^">]+)"', content)

    base_dir = os.path.dirname(html_file)

    print(f"Verifying images in {html_file}:")
    for src in img_srcs:
        # Resolve path
        if src.startswith('http'):
            continue # Skip external images

        full_path = os.path.normpath(os.path.join(base_dir, src))

        if os.path.exists(full_path):
            print(f"  [OK] {src}")
        else:
            print(f"  [MISSING] {src} (Checked: {full_path})")

if __name__ == "__main__":
    verify_images('topics/00-linear-algebra-basics/index.html')
    verify_images('topics/01-linear-algebra-advanced/index.html')
    verify_images('topics/09-duality/index.html')
