from playwright.sync_api import sync_playwright

def verify_header_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport (iPhone 12/13/14 size)
        page = browser.new_page(viewport={"width": 390, "height": 844})

        # Load the page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")
        page.wait_for_selector(".control-dock")

        # 1. Verify Header Visible initially
        display = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        assert display == "flex", f"Initial display should be flex, got {display}"

        # 2. Toggle Header via JS (simulate the checkbox change event)
        # We need to set the variable directly as the checkbox listener does
        page.evaluate("document.documentElement.style.setProperty(\"--header-display\", \"none\")")

        # 3. Verify Header Hidden
        display_after = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        print(f"Header display style after toggle: {display_after}")

        if display_after == "none":
             print("SUCCESS: Header is hidden")
        else:
             print("FAILURE: Header is still visible")
             exit(1)

        browser.close()

if __name__ == "__main__":
    verify_header_toggle()
