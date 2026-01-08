from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Check index.html
        file_path_index = os.path.abspath("index.html")
        print(f"Checking {file_path_index}...")
        page.goto(f"file://{file_path_index}")
        page.wait_for_selector('main')
        page.wait_for_selector('h1')
        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/verification_index.png", full_page=True)
        print("Screenshot saved to verification/verification_index.png")

        # Check a topic page
        file_path_topic = os.path.abspath("topics/00-linear-algebra-basics/index.html")
        print(f"Checking {file_path_topic}...")
        page.goto(f"file://{file_path_topic}")
        page.wait_for_selector('main')
        page.wait_for_selector('h1')
        page.screenshot(path="verification/verification_topic.png", full_page=True)
        print("Screenshot saved to verification/verification_topic.png")

        browser.close()

if __name__ == "__main__":
    run()
