# Audit Log: Lecture 03 - Convex Sets: Geometry

## 1. Content Audit
*   **File:** `topics/03-convex-sets-geometry/index.html`
*   **Status:** Complete / **Action Required**
*   **Scope:** Affine/Convex Sets, Hulls, Canonical Sets (Hyperplanes, Halfspaces, Norm Balls, Polyhedra, PSD Cone), Operations (Intersection, Affine, Perspective, Minkowski), Topology.
*   **Verification of Definitions:**
    *   **Affine/Convex Sets (Sec 1):** Defined correctly via combinations.
    *   **Convex Hull (Sec 1.3):** Defined. Carathéodory's Theorem stated and proved.
    *   **Canonical Sets (Sec 2):** Hyperplanes, Halfspaces, Norm Balls, Polyhedra, PSD Cone all defined correctly.
    *   **Operations (Sec 3):** Intersection, Affine Maps, Perspective, Linear-Fractional, Minkowski Sum all covered with proofs.
    *   **Topology (Sec 4):** Closure, Interior, Relative Interior defined.
*   **Mathematical Accuracy:**
    *   Carathéodory's proof (Sec 1.3) is correct.
    *   Perspective map proof (Sec 3.3) is rigorous.
    *   Minkowski Sum proof (Sec 3.4) is correct.
    *   PSD Cone convexity proof (Sec 2.4) is correct.
*   **Completeness:**
    *   **Separation Theorems:** Currently missing from this lecture (located in Lecture 04). The roadmap suggests moving them here.
    *   **Voronoi Regions:** Covered in Exercise P3.1.
*   **Redundancy:**
    *   **Voronoi Regions:** Duplicates P2.9. It belongs here.

## 2. Pedagogical Flow
*   **Current Flow:** Definitions -> Canonical Sets -> Operations -> Topology.
*   **Critique:**
    *   The roadmap suggests: Definitions -> Operations -> Canonical Sets.
    *   *Reasoning:* It's often easier to prove canonical sets are convex by construction (operations) rather than definition. E.g., Polyhedron = Intersection (Op) of Halfspaces (Canonical).
    *   However, the current flow works well: introduce the "zoo" of sets, then tools to manipulate them.
*   **Action:**
    *   **Move Separation Theorems** from L04 to here (likely as a new Section 5 or integrated into Topology). Separation is a fundamental geometric property.

## 3. Writing Style & Formatting
*   **Notation:**
    *   Vectors are italic $x$. **Action:** Change to bold `\mathbf{x}`.
    *   Sets are calligraphic or capital. Consistent.
*   **Clarity:**
    *   "Frisbee" intuition for Relative Interior (Sec 4.1) is excellent.

## 4. Exercises Audit
*   **Current List:** P3.1 - P3.21.
*   **Content:**
    *   P3.1 (Voronoi): Good.
    *   P3.4 (Linear-Fractional): Crucial for perspective.
    *   P3.15 (Set Classification): Good drill.
    *   P3.19 (Projection): Key for separation proof.
    *   P3.20 (Preimages): Advanced.
*   **Action Plan:**
    *   Ensure P3.19 connects to the Separation Theorem if moved here.

## 5. Implementation Checklist
*   [ ] **Move** Separation Theorems (L04 Sec 1) to L03 (New Section 5).
*   [ ] **Notation:** Global replace `$x$` -> `$\mathbf{x}$`.
*   [ ] **Reorder:** Consider swapping Operations and Canonical Sets if strictly following roadmap, but current flow is defensible.
*   [ ] **De-duplicate:** Confirm P2.9 removal (handled in L02 audit).

---

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
*   [ ] **Extract** Section 1 (Separation) and Exercises P4.1, P4.7, P4.8. Move to L03.
*   [ ] **Notation:** Global replace `$x$` -> `$\mathbf{x}$`.
*   [ ] **Expand** Cone Operations section in L04 to fill the gap.
