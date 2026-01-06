from playwright.sync_api import sync_playwright

def verify_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport (iPhone 12/13/14 size)
        page = browser.new_page(viewport={"width": 390, "height": 844})

        # Load the page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")
        page.wait_for_selector(".control-dock")

        # Verify header is initially visible
        header = page.locator(".site-header")
        assert header.is_visible(), "Header should be visible by default on mobile"
        page.screenshot(path="verification/mobile_header_visible.png")

        # Open Settings
        # On mobile, dock might be crowded, but let click it
        page.click("button[aria-label=\"Page Settings\"]")
        page.wait_for_selector(".settings-panel", state="visible")

        # Toggle Header OFF
        # The checkbox id is toggle-header
        page.click("#toggle-header")

        # Verify header is hidden
        # Wait a moment for CSS update if needed (though it should be instant via var update)
        page.wait_for_timeout(200)

        # Check visibility
        # Note: display: none elements are not "visible" in Playwright
        assert not header.is_visible(), "Header should be hidden after toggling off on mobile"
        page.screenshot(path="verification/mobile_header_hidden.png")

        print("Mobile verification passed!")
        browser.close()

if __name__ == "__main__":
    verify_mobile()
