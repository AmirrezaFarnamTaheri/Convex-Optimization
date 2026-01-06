from playwright.sync_api import sync_playwright

def verify_css_override():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport
        page = browser.new_page(viewport={"width": 390, "height": 844})

        # Load page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")
        page.wait_for_timeout(1000)

        # Initial check
        display_initial = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        print(f"Initial display: {display_initial}")

        # JS toggle simulation
        page.evaluate("document.documentElement.style.setProperty(\"--header-display\", \"none\")")
        page.wait_for_timeout(500)

        display_after = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        print(f"Display after toggle: {display_after}")

        if display_after == "none":
            print("SUCCESS: Header hidden.")
        else:
            print("FAILURE: Header still visible.")
            # Debug: Check if any media query is overriding
            # We can print all styles applied to header
            pass

        browser.close()

if __name__ == "__main__":
    verify_css_override()
