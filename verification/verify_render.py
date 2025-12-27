from playwright.sync_api import sync_playwright
import os

def check_html_files():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify L00
        page.goto(f"file://{os.getcwd()}/topics/00-linear-algebra-basics/index.html")
        page.screenshot(path="verification/L00_screenshot.png", full_page=True)

        # Verify L05
        page.goto(f"file://{os.getcwd()}/topics/05-convex-functions-basics/index.html")
        page.screenshot(path="verification/L05_screenshot.png", full_page=True)

        # Verify L06
        page.goto(f"file://{os.getcwd()}/topics/06-convex-functions-advanced/index.html")
        page.screenshot(path="verification/L06_screenshot.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    check_html_files()
