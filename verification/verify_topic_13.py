from playwright.sync_api import sync_playwright

def verify_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Navigate to the local server
        page.goto("http://localhost:8000/topics/13-unconstrained-minimization/index.html")

        # Verify title
        title = page.title()
        print(f"Page title: {title}")

        # Take a full page screenshot to verify content
        page.screenshot(path="verification/topic_13_full.png", full_page=True)

        # Take a screenshot of the new Theory sections (approximate location)
        # Scroll to Strong Convexity
        page.evaluate("window.scrollTo(0, 1000)")
        page.screenshot(path="verification/topic_13_theory.png")

        # Scroll to Examples
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="verification/topic_13_examples.png")

        browser.close()

if __name__ == "__main__":
    verify_page()
