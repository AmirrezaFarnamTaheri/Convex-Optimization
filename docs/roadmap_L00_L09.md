# Convex Optimization Course: Audit and Improvement Roadmap (Lectures 00-09)

## 1. Executive Summary
This document outlines the current state, identified gaps, and a detailed improvement plan for the first ten lectures (L00-L09) of the Convex Optimization course. The goal is to align the content with standard academic rigor (Boyd & Vandenberghe, Rockafellar, Strang), ensure pedagogical continuity, and fix structural inconsistencies.

The overall status is **good**, with most advanced topics already present. The primary work required involves **reordering sections for better flow**, **filling specific theoretical gaps** (e.g., geometric proofs), and **standardizing notation** (specifically vector boldface).

## 2. Global Cross-Cutting Issues
*   **Vector Notation:** The audit for Lecture 00 noted a requirement for bold vectors ($\mathbf{x}$), but current HTML files largely use italic ($x$). This requires a global search-and-replace (carefully done to avoid changing scalar variables).
*   **Structural Consistency:** L00-L09 generally use the `section-card` class, but L10-L15 (outside this scope but noted in memory) differ. We focus here on L00-L09 consistency.
*   **Navigation:** Forward/backward links in the header need verification after any reordering.

---

## 3. Lecture-by-Lecture Audit

### Lecture 00: Linear Algebra Basics
*   **Current Status:** Covers vectors, matrices, subspaces, rank-nullity, invariants (trace/det), inner products, norms, PSD matrices, projections, and least squares.
*   **Gaps & Discrepancies:**
    *   *Flow:* User wants "Basics → Subspaces → Invariants → Norms → Orthogonality → PSD → Projections → LS".
    *   *Notation:* Vectors are currently italic `$x$`, user wants `\mathbf{x}`.
    *   *Content:* "Matrix Calculus" is present but advanced; might fit better later or be marked optional.
*   **Action Plan:**
    1.  **Reorder Sections:** Move "Algebraic Invariants" (Sec 3) to after Subspaces. Ensure Norms (Sec 4) follow Invariants.
    2.  **Refine Text:** Switch to bold vector notation globally.
    3.  **Exercises:** Re-align exercise order with the new section order.

### Lecture 01: Linear Algebra Advanced
*   **Current Status:** Covers Basis Change, Rank-Nullity (again?), Eigenvalues, Induced Norms, QR, SVD, Pseudoinverse, Condition Number.
    *   *Note:* "Rank-Nullity" appears in the TOC headers of L01, but is also a core part of L00. This looks like redundancy.
*   **Gaps & Discrepancies:**
    *   *Redundancy:* Remove basic definitions of Rank-Nullity if fully covered in L00. Focus L01 on **Linear Maps** and **Change of Basis**.
    *   *Content:* The user wants "Induced operator norm" details (present in L01 Sec 4), "Geometric interpretations" for SVD (present in Sec 6).
    *   *Missing:* Explicit connection of Rayleigh Quotient to optimization bounds (present in Sec 3 but can be strengthened).
*   **Action Plan:**
    1.  **De-duplicate:** Reduce Rank-Nullity in L01 to a brief recap or "Advanced Geometric View".
    2.  **Enhance SVD:** Ensure the "Rotation-Scaling-Rotation" visual is prominent (it is currently in the text).
    3.  **Exercises:** Add manual SVD computation for 2x2 matrix (already in P1.3, good).

### Lecture 02: Introduction to Convex Optimization
*   **Current Status:** Defines convex problems, Local=Global theorem, Taxonomy (LP, QP, etc.), Feasible sets.
*   **Gaps & Discrepancies:**
    *   *Flow:* Generally good.
    *   *Content:* User wants "Three conditions for convexity" clearly stated. User wants "Complexity" discussion (NP-hardness).
*   **Action Plan:**
    1.  **Modeling Tricks:** Expand "Standard Form Transformation" with step-by-step slack variable examples.
    2.  **Comparison Table:** Verify the "Loss+Regularizer" table exists and is accurate.

### Lecture 03: Convex Sets – Geometry
*   **Current Status:** Affine/Convex sets, Hulls, Carathéodory, Sets from Functions (Sublevel, Epigraph).
*   **Gaps & Discrepancies:**
    *   *Separation Theorems:* User instructions for L03 mention "Separation theorems". However, currently they are in **Lecture 04** (Sec 1).
    *   *Flow:* User wants "Geometry of convex sets" leading to "Operations".
*   **Action Plan:**
    1.  **Major Move:** Move "Separating and Supporting Hyperplane Theorems" from **Lecture 04** to **Lecture 03** (or explicitly link them if length is an issue). *Recommendation: Keep in L04 if L03 is too long, but usually Separation belongs with Geometry.* User prompt explicitly asks to "Cross-check statement of separation theorems" in L03 context.
    2.  **Visuals:** Ensure "Convex Combination" widget is highlighted.

### Lecture 04: Convex Sets – Cones
*   **Current Status:** Separation Theorems (currently here), Cones, Dual Cones, Generalized Inequalities.
*   **Gaps & Discrepancies:**
    *   *Focus:* If Separation moves to L03, L04 becomes purely about **Cones and Generalized Inequalities**.
    *   *Content:* User wants "Cone operations (direct sum, product)".
*   **Action Plan:**
    1.  **Refocus:** Dedicate L04 to Cones, Dual Cones, and Generalized Inequalities.
    2.  **Additions:** Explicitly cover "Cone Programming" basics here to prep for L08.

### Lecture 05: Convex Functions – Basics
*   **Current Status:** Definition, Jensen's, Integral Characterization, Strict/Strong Convexity.
*   **Gaps & Discrepancies:**
    *   *Strong Convexity:* User prompt puts "Smoothness and Strong Convexity" in **Lecture 06**. Currently, "Strong Convexity" is in L05 (Sec 1.5).
    *   *Operations:* User wants "Operations that preserve convexity" (max, sum, composition).
*   **Action Plan:**
    1.  **Reorder:** Move "Strict and Strong Convexity" to L06 to match user request (or keep basic definition in L05 and advanced analysis in L06).
    2.  **Add:** Ensure "Operations preserving convexity" section is robust (Pointwise max, composition rules).

### Lecture 06: Convex Functions – Advanced
*   **Current Status:** Conjugates, "Why f* is convex", Examples (Log-Det, etc.).
*   **Gaps & Discrepancies:**
    *   *Missing Topics:* User asks for "Subgradients/Subdifferentials" in L06. Current headers don't explicitly show "Subgradients".
    *   *Smoothness/Strong Convexity:* As noted, user wants this here.
    *   *Duality:* User mentions "Fenchel Duality". Current L06 covers "Conjugates" but Fenchel Duality is often in L09. User Plan puts it in L06.
*   **Action Plan:**
    1.  **Add Content:** Add section on **Subgradients and Subdifferentials**.
    2.  **Move/Add:** Move Strong Convexity/Smoothness analysis here.
    3.  **Expand:** Explicitly cover Fenchel's Inequality and Duality Theorem here.

### Lecture 07: Convex Problems – Standard Forms
*   **Current Status:** Standard Form, LP, Diet Problem, Chebyshev Center.
*   **Gaps & Discrepancies:**
    *   *Scope:* Headers show LP. Need to ensure QP, QCQP are covered here or in L08? User plan says "L07: LP, QP, SOCP, SDP details". Current headers only show LP.
    *   *Missing:* QP, SOCP, SDP sections seem missing from L07 headers (L08 covers Conic, which usually includes SOCP/SDP).
*   **Action Plan:**
    1.  **Restructure:** If L08 is "Conic", L07 should cover **LP and QP** thoroughly.
    2.  **Clarify:** Define the boundary between L07 (Standard/QP) and L08 (Conic/SOCP/SDP). Standard academic flow: LP/QP/QCQP in "Standard", SOCP/SDP in "Conic".

### Lecture 08: Convex Problems – Conic Forms
*   **Current Status:** SOCP, Robust LP, SDP.
*   **Gaps & Discrepancies:**
    *   *Alignment:* Matches user request for Conic forms well.
    *   *Content:* User wants "Exponential cone programs".
*   **Action Plan:**
    1.  **Add:** Section on **Exponential Cone** and examples (Entropy maximization).

### Lecture 09: Duality
*   **Current Status:** Conjugates/Support Functions (Recap?), Lagrangian, Dual Function, Examples.
*   **Gaps & Discrepancies:**
    *   *Content:* "Strong Duality and KKT" headers are missing from the top-level list I saw (grep might have missed them if nested deep).
    *   *Flow:* Matches standard progression.
*   **Action Plan:**
    1.  **Check:** Verify Slater's Condition and KKT are present (crucial).
    2.  **Link:** Connect back to "Perturbation/Sensitivity" (User request).

---

## 4. Implementation Roadmap (Prioritized)

### Phase 1: Structural & Notation (High Priority)
1.  **Vector Notation:** Global find-and-replace to change vector variables ($x$) to bold ($\mathbf{x}$) in all `topics/` HTML files.
2.  **Link Verification:** Run a script to check all `href` targets between lectures.

### Phase 2: Content Reordering (Medium Priority)
1.  **L00:** Reorder to: Basics $\to$ Subspaces $\to$ Invariants $\to$ Norms $\to$ Orthogonality $\to$ PSD $\to$ LS.
2.  **L03/L04:** Decide on "Separation Theorems" location. Move to L03 to match user plan.
3.  **L05/L06:** Move "Strong Convexity" to L06. Add "Subgradients" to L06.

### Phase 3: Gap Filling (Low Priority / Detail)
1.  **L02:** Add "Modeling Tricks" (slack vars).
2.  **L07:** Ensure QP is covered (if not in L08).
3.  **L08:** Add Exponential Cone examples.

## 5. Conclusion
The course material is high-quality but requires "polishing" to match the specific pedagogical flow requested. The most significant structural change is the potential shift of Separation Theorems (L04$\to$L03) and Strong Convexity (L05$\to$L06).
