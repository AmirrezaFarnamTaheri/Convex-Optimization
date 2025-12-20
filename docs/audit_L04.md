# Audit Log: Lecture 04 - Convex Sets: Cones and Separation

## 1. Content Audit
*   **File:** `topics/04-convex-sets-cones/index.html`
*   **Status:** Complete / **Action Required**
*   **Scope:** Separation Theorems, Cones, Dual Cones, Generalized Inequalities.
*   **Verification of Definitions:**
    *   **Separation (Sec 1):** Separating/Supporting Hyperplane theorems stated. Farkas' Lemma included.
    *   **Cones (Sec 2):** Cone, Convex Cone, Proper Cone defined.
    *   **Dual Cone (Sec 2.4):** Defined correctly ($y^\top x \ge 0$). Bipolar theorem stated.
    *   **Self-Dual Cones:** $\mathbb{R}^n_+$, PSD, SOC proven self-dual.
*   **Mathematical Accuracy:**
    *   Proofs for Separation (via Projection) and Farkas are standard and correct.
    *   PSD Cone self-duality proof (Sec 2.4) is rigorous.
    *   SOC self-duality proof (Sec 2.4) is rigorous.
*   **Completeness:**
    *   **Cone Operations:** Missing explicit section on operations (sum, intersection, dual of operations). P4.4 covers dual of sum.
    *   **Cone Programming:** Brief mention in 2.3 (Pareto). Could be expanded as a preview of L08.

## 2. Pedagogical Flow
*   **Current Flow:** Separation -> Cones -> Dual Cones.
*   **Issue:**
    *   The roadmap plans to **move Separation to L03**.
    *   This leaves L04 with only Cones.
    *   **Proposal:** Rename L04 to "Cones and Generalized Inequalities". Expand on Cone Calculus (Polar, Dual operations) and Cone Programming basics (what does $Ax \preceq_K b$ mean?).
*   **Action:**
    *   Execute the move of Separation to L03.
    *   Flesh out L04 with more on Cone Operations and properties of Generalized Inequalities (e.g., if $x \preceq y$ and $u \preceq v$, is $x+u \preceq y+v$?).

## 3. Writing Style & Formatting
*   **Notation:**
    *   Vectors are italic $x$. **Action:** Change to bold `\mathbf{x}`.
    *   Cones $K$. Good.

## 4. Exercises Audit
*   **Current List:** P4.1 - P4.17.
*   **Content:**
    *   P4.1 (Separation by Projection): Belongs in L03 if Separation moves.
    *   P4.2 (Dual of Subspace): Good.
    *   P4.3 (SOC Self-Dual): Good.
    *   P4.11 (Dual of Generated Cone): Farkas link.
    *   P4.16 (SOCP Dual): Good preview of L08.
*   **Action Plan:**
    *   **Move** P4.1, P4.7, P4.8 (related to Separation/Support) to L03 exercises.
    *   **Keep** the rest for Cones.

## 5. Implementation Checklist
*   [x] **Extract** Section 1 (Separation) and Exercises P4.1, P4.7, P4.8. Move to L03. ✅ COMPLETED (Section moved, exercises pending)
*   [ ] **Notation:** Global replace `$x$` -> `$\mathbf{x}$`.
*   [ ] **Expand** Cone Operations section in L04 to fill the gap.
