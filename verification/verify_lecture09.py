import os
from playwright.sync_api import sync_playwright

def verify_lecture09():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "topics/09-duality/index.html")
        url = f"file://{file_path}"

        print(f"Navigating to {url}")
        page.goto(url)

        # Take screenshot of the new sections
        # Problem 8
        # We target the h3, then go up to the parent div.problem
        # locator("xpath=..") selects the parent

        # Taking full page screenshot to be safe as well
        page.screenshot(path="verification/full_page.png", full_page=True)

        try:
            p8 = page.locator("div.problem").filter(has_text="Problem 8: Sum of Largest Elements (The Deep Dive)")
            if p8.count() > 0:
                p8.first.screenshot(path="verification/problem8.png")
                print("Problem 8 screenshot taken.")
            else:
                print("Problem 8 not found.")

            p9 = page.locator("div.problem").filter(has_text="Problem 9: Markowitz Portfolio with Diversification")
            if p9.count() > 0:
                p9.first.screenshot(path="verification/problem9.png")
                print("Problem 9 screenshot taken.")
            else:
                print("Problem 9 not found.")
        except Exception as e:
            print(f"Error taking element screenshots: {e}")

        browser.close()

if __name__ == "__main__":
    verify_lecture09()
