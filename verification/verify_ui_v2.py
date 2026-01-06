from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")
        page.wait_for_selector(".control-dock")

        # 1. Settings Panel Verification
        page.click("button[aria-label=\"Page Settings\"]")
        page.wait_for_selector(".settings-panel", state="visible")
        page.screenshot(path="verification/settings_panel.png")

        # Close settings (force click to bypass obstructions)
        page.click("#close-settings", force=True)

        # 2. Content Verification
        # Locate the specific proof boxes we modified
        # Preimage Convexity Proof
        page.evaluate("window.scrollTo(0, 0)")
        preimage_proof = page.get_by_text("Proof: Preimage Convexity").first
        if preimage_proof.is_visible():
             preimage_proof.scroll_into_view_if_needed()
             page.screenshot(path="verification/proof_preimage.png")

        # Gradient Derivation Proof
        gradient_proof = page.get_by_text("Derivation: Gradient of Quadratic Form (Detailed)").first
        if gradient_proof.is_visible():
             gradient_proof.scroll_into_view_if_needed()
             page.screenshot(path="verification/proof_gradient.png")

        browser.close()

if __name__ == "__main__":
    verify_frontend()
