from playwright.sync_api import sync_playwright
import os

def check_lecture_04():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath('topics/04-convex-sets-cones/index.html')
        page.goto(f'file://{file_path}')

        # Take a screenshot of the top of the page
        page.screenshot(path='verification/04-lecture-top.png')

        # Scroll down to see figure numbering around Figure 26 (previously Figure 5)
        # Figure 26 is roughly in Section 1.1 "The Big Three Cones"
        # We search for the text "Figure 26" to confirm it exists
        try:
            fig26 = page.get_by_text("Figure 26")
            fig26.scroll_into_view_if_needed()
            page.screenshot(path='verification/04-lecture-fig26.png')
            print("Found Figure 26")
        except:
            print("Figure 26 not found")

        # Scroll further to check for style removal on images
        # We can look for the "Cone Zoo" which is Figure 28 (was Figure 7)
        try:
            fig28 = page.get_by_text("Figure 28")
            fig28.scroll_into_view_if_needed()
            page.screenshot(path='verification/04-lecture-fig28.png')
            print("Found Figure 28")
        except:
            print("Figure 28 not found")

        browser.close()

if __name__ == "__main__":
    os.makedirs('verification', exist_ok=True)
    check_lecture_04()
