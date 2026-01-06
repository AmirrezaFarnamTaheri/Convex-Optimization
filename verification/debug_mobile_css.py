from playwright.sync_api import sync_playwright

def check_computed_style():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844})

        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")

        # Check initial style
        style = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        var_val = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue(\"--header-display\")")

        print(f"Initial Computed Display: {style}")
        print(f"Initial Variable Value: {var_val}")

        # Toggle via JS
        page.evaluate("document.documentElement.style.setProperty(\"--header-display\", \"none\")")

        # Check again
        style_after = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        var_val_after = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue(\"--header-display\")")

        print(f"After Toggle Computed Display: {style_after}")
        print(f"After Toggle Variable Value: {var_val_after}")

        browser.close()

if __name__ == "__main__":
    check_computed_style()
