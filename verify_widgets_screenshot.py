from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")
        page.wait_for_selector(".control-dock")

        # Verify Buttons Exist
        page.wait_for_selector("#notes-widget-btn")
        page.wait_for_selector("#bookmark-widget-btn")
        page.wait_for_selector("#highlight-widget-btn")

        print("All dock buttons visible.")

        # 1. Test Notes Panel
        page.click("#notes-widget-btn")
        page.wait_for_selector("#notes-panel", state="visible")
        # Check ARIA
        role = page.get_attribute("#notes-panel", "role")
        print(f"Notes Panel Role: {role}")
        page.screenshot(path="verification_notes_panel.png")
        page.click("#notes-widget-btn") # Toggle close

        # 2. Test Bookmarks Panel
        page.click("#bookmark-widget-btn")
        page.wait_for_selector("#bookmarks-panel", state="visible")
        page.screenshot(path="verification_bookmarks_panel.png")
        page.click("#bookmark-widget-btn") # Toggle close

        # 3. Test Highlighter Toggle
        page.click("#highlight-widget-btn")
        # Check active state class
        if "active" in page.get_attribute("#highlight-widget-btn", "class"):
            print("Highlighter button active.")
        else:
            print("Highlighter button NOT active.")

        page.screenshot(path="verification_highlighter_active.png")

        browser.close()

if __name__ == "__main__":
    run()
