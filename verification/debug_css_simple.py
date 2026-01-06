from playwright.sync_api import sync_playwright

def check_css_var():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844})

        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")

        # Manually set the variable to none
        page.evaluate("document.documentElement.style.setProperty(\"--header-display\", \"none\")")

        # Get the computed display of site-header
        display = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")

        print(f"Header Display: {display}")

        # Also check if any media query is applying display:flex
        # We can't easily check "which rule wins" in playwright without complex JS, but the computed style is the source of truth.

        browser.close()

if __name__ == "__main__":
    check_css_var()
