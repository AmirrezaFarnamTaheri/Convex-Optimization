from playwright.sync_api import sync_playwright
import os

def verify():
    base_dir = os.getcwd()
    output_dir = os.path.join(base_dir, "verification")
    os.makedirs(output_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Verify Module 01
        print("Verifying Module 01...")
        page.goto(f"file://{base_dir}/topics/01-linear-algebra-advanced/index.html")
        page.screenshot(path=os.path.join(output_dir, "screenshot_01_updated.png"), full_page=True)

        # Verify Module 05
        print("Verifying Module 05...")
        page.goto(f"file://{base_dir}/topics/05-convex-functions-basics/index.html")
        page.screenshot(path=os.path.join(output_dir, "screenshot_05_updated.png"), full_page=True)

        # Verify Module 06
        print("Verifying Module 06...")
        page.goto(f"file://{base_dir}/topics/06-convex-functions-advanced/index.html")
        page.screenshot(path=os.path.join(output_dir, "screenshot_06_updated.png"), full_page=True)

        browser.close()

if __name__ == "__main__":
    verify()
