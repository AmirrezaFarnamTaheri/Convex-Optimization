
from playwright.sync_api import sync_playwright
import os

def verify_duality_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Use absolute path based on pwd result /app
        filepath = os.path.abspath("topics/09-duality/index.html")
        page.goto(f"file://{filepath}")

        # Take a screenshot of the whole page (or a long scroll)
        # Since it is a lecture note, full page screenshot is useful
        page.screenshot(path="verification/duality_full.png", full_page=True)

        # Also take specific screenshots of new sections to verify rendering
        # 1. Learning Objectives
        page.locator("section.section-card").first.screenshot(path="verification/duality_learning_objectives.png")

        # 2. Motivating Example (in Section 2)
        # Find the example box
        example = page.locator(".example").filter(has_text="Motivating Example").first
        if example.count() > 0:
            example.screenshot(path="verification/duality_motivating_example.png")

        # 3. KKT Water Filling (in Section 5)
        water_filling = page.locator(".example").filter(has_text="Water-Filling").first
        if water_filling.count() > 0:
            water_filling.screenshot(path="verification/duality_water_filling.png")

        # 4. Canonical Duals Problem Pack
        canonicals = page.locator("#section-10")
        if canonicals.count() > 0:
            canonicals.screenshot(path="verification/duality_canonicals.png")

        browser.close()

if __name__ == "__main__":
    verify_duality_page()
