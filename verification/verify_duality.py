from playwright.sync_api import sync_playwright

def verify_duality_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        # Note: In this environment, we can access files directly via absolute path
        # Adjust path if necessary (assuming repo root is current working dir)
        import os
        cwd = os.getcwd()
        file_url = f"file://{cwd}/topics/09-duality/index.html"

        print(f"Navigating to {file_url}")
        page.goto(file_url)

        # Take a full page screenshot
        page.screenshot(path="verification/lecture_09_full.png", full_page=True)

        # Take specific screenshots of the widgets and new content

        # 1. Motivating Example
        example = page.locator(".example").first
        if example.count() > 0:
            example.screenshot(path="verification/motivating_example.png")
            print("Captured Motivating Example")

        # 2. Conjugate Function Widget
        # It's in an iframe in Section 1 (Recap) or 3.3
        # I placed it in Section 3.3 (Examples of Dual Functions) -> actually Section 3 in the code logic
        # Let's find all iframes
        frames = page.frames
        print(f"Found {len(frames)} frames (including main)")

        # We can also screenshot the container of the iframes
        # The iframes are inside divs with specific style
        # Let's locate them by src attribute

        # Conjugate Widget
        try:
            widget_conj = page.locator('iframe[src="widgets/conjugate_function.html"]')
            if widget_conj.count() > 0:
                widget_conj.screenshot(path="verification/widget_conjugate.png")
                print("Captured Conjugate Widget")
        except Exception as e:
            print(f"Error capturing Conjugate Widget: {e}")

        # Primal Dual 1D Widget
        try:
            widget_pd = page.locator('iframe[src="widgets/primal_dual_1d.html"]')
            if widget_pd.count() > 0:
                widget_pd.screenshot(path="verification/widget_primal_dual.png")
                print("Captured Primal Dual Widget")
        except Exception as e:
            print(f"Error capturing Primal Dual Widget: {e}")

        # PSD Cone Widget
        try:
            widget_psd = page.locator('iframe[src="widgets/psd_cone_2x2.html"]')
            if widget_psd.count() > 0:
                widget_psd.screenshot(path="verification/widget_psd.png")
                print("Captured PSD Widget")
        except Exception as e:
            print(f"Error capturing PSD Widget: {e}")

        # SOC Cone Widget
        try:
            widget_soc = page.locator('iframe[src="widgets/soc_dual_cone.html"]')
            if widget_soc.count() > 0:
                widget_soc.screenshot(path="verification/widget_soc.png")
                print("Captured SOC Widget")
        except Exception as e:
            print(f"Error capturing SOC Widget: {e}")

        browser.close()

if __name__ == "__main__":
    verify_duality_page()
