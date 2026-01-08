from playwright.sync_api import sync_playwright, Page, expect
import time

def verify_topic_13():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the topic 13 page
        # Assuming the structure is topics/13-unconstrained-minimization/index.html
        # And http-server serves from root
        page.goto("http://localhost:8000/topics/13-unconstrained-minimization/index.html")

        # Wait for KaTeX to render (give it a moment, though it is synchronous in script tag usually)
        time.sleep(2)

        # Scroll down to see the exercises
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

        # Take a full page screenshot
        page.screenshot(path="verification/topic_13_full.png", full_page=True)

        # Take a screenshot of specific sections if needed
        # Theory section
        page.locator("h3:has-text('0. Notation and the \"Model\"')").scroll_into_view_if_needed()
        page.screenshot(path="verification/topic_13_theory.png")

        # Exercises section
        page.locator("h2:has-text('Solved Exercises & Example Problems')").scroll_into_view_if_needed()
        page.screenshot(path="verification/topic_13_exercises.png")

        browser.close()

if __name__ == "__main__":
    verify_topic_13()
