from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/topics/09-duality/index.html")

        # Wait for any content to appear
        page.wait_for_selector(".lecture-content")

        # Just take a full page screenshot
        page.screenshot(path="verification/duality_full_page.png", full_page=True)
        print("Screenshot captured.")

        browser.close()

if __name__ == "__main__":
    run()
