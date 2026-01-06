from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index page (or specific lecture page)
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")

        # Wait for control dock to load (dynamic JS)
        page.wait_for_selector(".control-dock")

        # 1. Open Settings Panel
        page.click("button[aria-label=\"Page Settings\"]")
        page.wait_for_selector(".settings-panel", state="visible")

        # 2. Adjust Layout (Width) - simulate interaction
        # We cannot easily drag range in headless, but we can verify it exists and take a screenshot of the panel

        # 3. Take Screenshot of Settings Panel
        page.screenshot(path="verification/settings_panel.png")

        # 4. Close Settings
        page.click("#close-settings")

        # 5. Expand Content (Lecture 00 modifications)
        # Check proof boxes
        proof_box = page.locator(".proof-box").first
        page.evaluate("window.scrollTo(0, 500)")

        # Take Screenshot of Enhanced Content
        page.screenshot(path="verification/enhanced_content.png")

        browser.close()

if __name__ == "__main__":
    verify_frontend()
