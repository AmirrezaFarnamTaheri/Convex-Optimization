from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Create an absolute path to the file
        file_path = os.path.abspath("topics/13-unconstrained-minimization/index.html")
        page.goto(f"file://{file_path}")

        # Wait for content to load - specifically check for the main content
        page.wait_for_selector('main')
        page.wait_for_selector('h1')

        # Take a full page screenshot
        os.makedirs("verification", exist_ok=True)
        screenshot_path = "verification/verification_fixed.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
