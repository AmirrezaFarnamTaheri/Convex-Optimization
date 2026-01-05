from playwright.sync_api import sync_playwright
import os

def run():
    # Make sure we can access the file locally
    file_path = os.path.abspath("topics/09-duality/index.html")
    file_url = f"file://{file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print(f"Loading {file_url}...")
        page.goto(file_url)

        # Check title
        title = page.title()
        if "Duality" not in title:
            print("ERROR: Title does not match expected.")
            exit(1)

        # Check canonical duals section
        sections = page.query_selector_all("#section-8 .problem")
        print(f"Found {len(sections)} canonical dual problems.")
        if len(sections) < 11:
             print("ERROR: Expected at least 11 canonical dual problems.")
             exit(1)

        # Check exercises section
        exercises = page.query_selector_all("#section-exercises .problem")
        print(f"Found {len(exercises)} exercises.")
        if len(exercises) < 14:
             print("ERROR: Expected at least 14 exercises.")
             exit(1)

        # Check if GIFs loaded (by checking img src existence)
        gifs = page.query_selector_all("img")
        print(f"Found {len(gifs)} images.")
        for gif in gifs:
            src = gif.get_attribute("src")
            if "duality_" in src and ".gif" in src:
                print(f"Found GIF reference: {src}")

        # Screenshot
        page.screenshot(path="duality_verified.png", full_page=True)
        print("Verification complete. Screenshot saved.")
        browser.close()

if __name__ == "__main__":
    run()
