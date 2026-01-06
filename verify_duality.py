from playwright.sync_api import sync_playwright

def verify_duality_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Navigate to the local server
        page.goto("http://localhost:8000/topics/09-duality/index.html")

        # Take a full page screenshot to verify the presence of new problems
        page.screenshot(path="/home/jules/verification/duality_page.png", full_page=True)

        # Also scroll to the specific new problems to ensure they rendered correctly
        # We can locate them by text

        # Check for Problem 5.3
        p53 = page.get_by_text("P9.16 — Conjugate-based dual of least-squares (Problem 5.3)")
        if p53.is_visible():
            print("Problem 5.3 found.")
        else:
            print("Problem 5.3 NOT found.")

        # Check for Problem 5.4
        p54 = page.get_by_text("P9.17 — Quadratic inequality via duality (Problem 5.4)")
        if p54.is_visible():
            print("Problem 5.4 found.")
        else:
            print("Problem 5.4 NOT found.")

        # Check for renamed Problem 8
        p8 = page.get_by_text("Problem 8: Sum of Largest Elements (The Deep Dive) (Problem 5.19)")
        if p8.is_visible():
            print("Problem 8 found.")
        else:
             print("Problem 8 NOT found.")

        browser.close()

if __name__ == "__main__":
    verify_duality_page()
