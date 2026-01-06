from playwright.sync_api import sync_playwright

def verify_content_enhancements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Load the page
        page.goto("http://localhost:8000/topics/00-linear-algebra-basics/index.html")

        # 1. Verify "Preimage Convexity" Proof is expanded and detailed
        # Check for specific text that was added
        content = page.content()
        assert "Step 1: Pick two points in the preimage." in content, "Preimage proof step 1 missing"
        assert "Step 3: Apply the affine map." in content, "Preimage proof step 3 missing"

        # 2. Verify "Gradient of Quadratic Form" derivation
        # Scroll to section
        gradient_header = page.get_by_text("Derivation: Gradient of Quadratic Form (Detailed)")
        assert gradient_header.count() > 0, "Gradient derivation header not found"

        # Check steps
        assert "Step 1: Perturb the input." in content, "Gradient derivation step 1 missing"
        assert "Step 3: Identify the linear part (The Differential)." in content, "Gradient derivation step 3 missing"

        # 3. Verify "Orthogonality of Eigenvectors" proof
        assert "Step 3: Evaluate the same product using symmetry." in content, "Orthogonality proof step 3 missing"

        # 4. Verify "Least Squares Optimality" proof
        assert "Hypothesis:</strong> Suppose" in content, "Least Squares proof hypothesis missing"

        print("Content verification passed!")
        browser.close()

if __name__ == "__main__":
    verify_content_enhancements()
