from playwright.sync_api import sync_playwright
import os

def verify_l00_content():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/topics/00-linear-algebra-basics/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Verify "Optimization View" insight block
        insight_locator = page.locator("div.insight:has-text('Optimization View: Norms as Shapes')")
        insight_locator.scroll_into_view_if_needed()
        print("Found Optimization View insight block")

        # Take screenshot of the insight block area
        page.screenshot(path="/home/jules/verification/L00_insight.png", clip={
            "x": 0,
            "y": insight_locator.bounding_box()['y'] - 50,
            "width": 1000,
            "height": 800
        })

        # Verify Exercise P0.21
        exercise_locator = page.locator("h3:has-text('P0.21 — Chebyshev Approximation Bound')")
        exercise_locator.scroll_into_view_if_needed()
        print("Found Exercise P0.21")

        # Take screenshot of the exercise area
        page.screenshot(path="/home/jules/verification/L00_P0.21.png", clip={
            "x": 0,
            "y": exercise_locator.bounding_box()['y'] - 50,
            "width": 1000,
            "height": 600
        })

        browser.close()

if __name__ == "__main__":
    verify_l00_content()
