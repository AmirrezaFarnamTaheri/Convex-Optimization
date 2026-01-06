from playwright.sync_api import sync_playwright

def verify_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport (iPhone 12/13/14 size)
        page = browser.new_page(viewport={"width": 390, "height": 844})

        # Load the page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")
        page.wait_for_selector(".control-dock")

        # Open Settings - Force click to bypass obstruction
        # Sometimes settings-trigger might be covered or not interactive immediately
        page.wait_for_selector("button[aria-label=\"Page Settings\"]", state="visible")
        page.click("button[aria-label=\"Page Settings\"]", force=True)

        page.wait_for_selector(".settings-panel", state="visible")

        # Toggle Header OFF
        # Instead of clicking the input directly (which might be covered by label/span), click the label
        page.click("label[for=\"toggle-header\"]", force=True)

        # Check computed style
        page.wait_for_timeout(500)
        display = page.evaluate("window.getComputedStyle(document.querySelector(\".site-header\")).display")
        print(f"Header display style: {display}")

        if display == "none":
             print("SUCCESS: Header is hidden")
             page.screenshot(path="verification/mobile_header_hidden_success.png")
        else:
             print("FAILURE: Header is still visible")
             page.screenshot(path="verification/mobile_header_failure.png")
             exit(1)

        browser.close()

if __name__ == "__main__":
    verify_mobile()
