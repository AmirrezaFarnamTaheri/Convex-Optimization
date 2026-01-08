from playwright.sync_api import sync_playwright
import os

def verify_lecture_13():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        file_url = f"file://{cwd}/topics/13-unconstrained-minimization/index.html"

        print(f"Navigating to {file_url}")
        page.goto(file_url)

        content = page.content()

        # Verify card-grid exists
        if "card-grid" in content:
            print("SUCCESS: Found 'card-grid' class in HTML")
        else:
            print("FAILURE: Did not find 'card-grid' class")

        # Verify images are loaded
        images = page.locator("img")
        count = images.count()
        print(f"Found {count} images.")

        # Screenshot the grid area
        grid = page.locator(".card-grid").first
        if grid.count() > 0:
            grid.screenshot(path="verification/13-lecture-grid.png")
            print("Screenshot of grid saved.")
        else:
            print("WARNING: Could not find .card-grid for screenshot")

        browser.close()

if __name__ == "__main__":
    verify_lecture_13()
