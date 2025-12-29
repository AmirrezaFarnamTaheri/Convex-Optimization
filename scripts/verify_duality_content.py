from playwright.sync_api import sync_playwright, Page, expect

def verify_duality_page(page: Page):
    # Navigate to the file directly
    page.goto("file:///app/topics/09-duality/index.html")

    # Wait for the main content to load
    page.wait_for_selector(".lecture-content")

    # Wait for mathjax to render (if any, although here it is handled by katex script which might take a moment)
    page.wait_for_timeout(2000) # Give it 2 seconds to be safe

    # Locate P9.12 heading specifically
    p12 = page.locator("h3:has-text('P9.12 — Chebyshev Approximation vs Least Squares')")
    p12.scroll_into_view_if_needed()

    # Take screenshot
    page.screenshot(path="/home/jules/verification/duality_problems_12_13.png", full_page=False)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_duality_page(page)
        finally:
            browser.close()
