# Convex Optimization Course: Comprehensive Audit and Improvement Roadmap (Lectures 00-09)

## 1. Executive Summary
This document provides a granular, lecture-by-lecture audit of the first ten modules of the Convex Optimization course. It benchmarks the current content against standard academic rigor (Boyd & Vandenberghe, Rockafellar, Strang) and specific user requirements.

**Overall Status:** The course content is mathematically robust and covers the required advanced topics (SVD, Conjugates, Duality). However, significant structural refactoring is needed to improve pedagogical flow, eliminate redundancies, and standardize notation.

**Key Action Items:**
1.  **Global Notation Update:** Switch all vector variables from italic $x$ to bold $\mathbf{x}$.
2.  **Structural Reordering:** Move "Separation Theorems" from L04 to L03; move "Strong Convexity" from L05 to L06.
3.  **Content Additions:** Add "Subgradients" to L06 and "Exponential Cone" to L08.

---

## 2. Global Cross-Cutting Issues
*   **Vector Notation:** Current HTML files use `$x$` (italic). **Requirement:** Switch to `\mathbf{x}` (bold) to distinguish vectors from scalars.
*   **Terminology:** Standardize "Positive Semidefinite" vs "PSD". (Recommendation: Use "PSD" as abbreviation after first definition).
*   **Navigation:** Ensure forward/backward links in headers are updated after content moves.

---

## 3. Detailed Lecture Audits

### Lecture 00: Linear Algebra Basics
*   **Current Content:**
    *   Sec 1: Mathematical Atoms (Vectors, Matrices, Calculus).
    *   Sec 2: Subspaces, Rank-Nullity.
    *   Sec 3: Invariants (Trace, Det, Eigenvalues).
    *   Sec 4: Inner Products, Norms.
    *   Sec 5: Orthogonality, QR.
    *   Sec 6: PSD Matrices (Schur Complement).
    *   Sec 7: Projections.
    *   Sec 8: Least Squares.
*   **Flow Analysis:**
    *   *Current:* Atoms $\to$ Subspaces $\to$ Invariants $\to$ Norms $\to$ Orthogonality $\to$ PSD $\to$ Projections $\to$ LS.
    *   *Critique:* "Algebraic Invariants" (Sec 3) appears before "Norms" (Sec 4). User flow prefers: ... $\to$ eigenvalues $\to$ PSD $\to$ projections. The current flow is acceptable but could be tightened. "Matrix Calculus" (Sec 1.6) is advanced and might overwhelm beginners early on.
*   **Exercises:**
    *   P0.1 Independence; P0.2 Rank-Nullity; P0.3 Trace/Det; P0.4 Norms; P0.5 LS Derivation; P0.6 Matrix Calc; P0.7 Hessian; P0.8 PSD Test; P0.9 Schur; P0.10-11 Projections; P0.12 Orthogonal Complements; P0.13-14 Norm proofs; P0.15 Isometries; P0.16 Loewner; P0.17 Weighted IP; P0.18 Projectors; P0.19 PSD Cone; P0.20 Quad Min.
    *   *Assessment:* Comprehensive. P0.5 (LS) appears before P0.6 (Matrix Calc) which is slightly out of order if P0.5 requires calculus.
*   **Action Plan:**
    1.  **Reorder:** Move "Matrix Calculus" (1.6) to an appendix or later section (before LS).
    2.  **Refine:** Ensure "Algebraic Invariants" (Sec 3) focuses on *geometry* (volume, stretch) rather than just formulas.
    3.  **Notation:** Apply $\mathbf{x}$ global change.

### Lecture 01: Linear Algebra Advanced
*   **Current Content:**
    *   Sec 1: Bases, Coordinates, Change of Basis.
    *   Sec 2: Linear Maps, Rank-Nullity (Recap).
    *   Sec 3: Eigenvalues, Rayleigh Quotient.
    *   Sec 4: Induced Norms ($\ell_1, \ell_\infty, \ell_2$).
    *   Sec 5: QR Decomposition.
    *   Sec 6: SVD (Geometry, Existence, Low-rank).
    *   Sec 7: Pseudoinverse, Condition Number.
*   **Flow Analysis:**
    *   *Redundancy:* Section 2 ("Linear Maps and Rank-Nullity") overlaps with L00 Section 2.
    *   *Strengths:* Section 6 (SVD) has excellent geometric intuition (Rotate-Stretch-Rotate).
*   **Exercises:**
    *   P1.1 Dual of $\ell_p$ (Advanced); P1.2 Frobenius CS; P1.3 SVD Hand Calc; P1.6 Normal vs QR; P1.7-1.9 Projectors; P1.10 Condition Number; P1.11 Rank-1 Pseudo; P1.12-1.13 Operator Norms; P1.14 Orthogonal Group.
    *   *Assessment:* Strong set. P1.1 relies on Hölder's inequality (check if defined in L00).
*   **Action Plan:**
    1.  **Prune:** Compress Section 2 (Rank-Nullity) into a brief "Advanced View" to reduce overlap with L00.
    2.  **Verify:** Ensure Hölder's inequality is defined in L00 (Sec 4) or L01 (Sec 4) before P1.1.

### Lecture 02: Introduction to Convex Optimization
*   **Current Content:**
    *   Sec 1: Definition (3 conditions).
    *   Sec 2: Fundamental Theorem (Local=Global).
    *   Sec 3: Complexity & Impact.
    *   Sec 4: Hierarchy (LP, QP, SOCP, SDP).
    *   Sec 5: Loss + Regularizer.
    *   Sec 6: Transformations (Abs, Max, SOCP, Epigraph, Linear-Fractional).
    *   Sec 7: DCP.
    *   Sec 8: Verification.
*   **Flow Analysis:**
    *   *Gap:* "Modeling Tricks" (Sec 6) is present but needs to be very explicit (step-by-step) about slack variables.
    *   *Gap:* Section 3 mentions NP-hardness but lacks concrete examples (e.g., Integer Programming) as requested.
*   **Exercises:**
    *   P2.1 Classify; P2.2 Warehouse (QP); P2.3 L1 Regression (LP); P2.4 Feasible Set Convexity; P2.5 Uniqueness; P2.6 MLE (Logistic); P2.7 Definition Proof; P2.8 Strict vs Strong; P2.9 Voronoi.
    *   *Assessment:* Excellent mix of modeling and theory. P2.9 (Voronoi) duplicates P3.1 in L03.
*   **Action Plan:**
    1.  **Expand:** Add explicit "slack variable" tutorial in Section 6.
    2.  **Add Example:** Add Integer Programming example to Section 3 to illustrate non-convex complexity.
    3.  **De-duplicate:** Remove P2.9 (Voronoi) or cross-reference it.

### Lecture 03: Convex Sets – Geometry
*   **Current Content:**
    *   Sec 1: Affine/Convex Sets, Hulls.
    *   Sec 2: Canonical Sets (Hyperplanes, Balls, Polyhedra, PSD Cone).
    *   Sec 3: Operations (Intersection, Affine, Perspective, Minkowski).
    *   Sec 4: Topology (Closure, Interior).
*   **Flow Analysis:**
    *   *Gap:* **Separation Theorems are missing.** They are currently in L04. User expects them here (Geometry).
    *   *Order:* Current is Definitions $\to$ Canonical $\to$ Operations. User prefers Definitions $\to$ Operations $\to$ Canonical.
*   **Exercises:**
    *   P3.1 Voronoi; P3.2 Midpoint; P3.3 Hull of Union; P3.4 Linear-Fractional; P3.5 Quadratic Sublevel; P3.6 Relative Interior; P3.7-3.21 (Various properties).
    *   *Assessment:* Very comprehensive. P3.19 (Projection) is key for Separation proof.
*   **Action Plan:**
    1.  **Major Move:** Move "Separation Theorems" (L04 Sec 1) to L03 (new Section 5).
    2.  **Reorder:** Move Section 3 (Operations) before Section 2 (Canonical Sets).

### Lecture 04: Convex Sets – Cones
*   **Current Content:**
    *   Sec 1: Separation Theorems (Separating, Supporting, Farkas).
    *   Sec 2: Cones (Proper, Generalized Inequalities, Dual Cones).
*   **Flow Analysis:**
    *   *Orphaned Content:* If Separation (Sec 1) moves to L03, L04 becomes too short.
    *   *Gap:* User wants "Cone Operations" (Direct sum, etc.) and "Cone Programming" basics.
*   **Exercises:**
    *   P4.1 Separation by Projection; P4.2 Dual of Subspace; P4.3 Self-Dual SOC; P4.4 Dual Identities; P4.5 Generalized Inequality; P4.6-4.17 (Advanced Cone properties).
    *   *Assessment:* Strong on theory. P4.1 belongs with Separation (L03).
*   **Action Plan:**
    1.  **Restructure:** Move Sec 1 to L03.
    2.  **Expand:** Rename lecture to "Cones and Generalized Inequalities". Add sections on "Cone Operations" and "Cone Programming" (preview of L08).

### Lecture 05: Convex Functions – Basics
*   **Current Content:**
    *   Sec 1: Definition, Jensen's, Strong/Strict Convexity.
    *   Sec 2: Epigraphs.
    *   Sec 3: First-Order Conditions.
    *   Sec 4: Second-Order Conditions.
    *   Sec 5: Operations.
*   **Flow Analysis:**
    *   *Placement:* "Strong Convexity" is introduced in Sec 1.5 and 4.2. User prefers this topic in **Lecture 06**.
*   **Exercises:**
    *   P5.1 Basic Functions; P5.2 AM-GM; P5.3 Log-Sum-Exp; P5.4 Quad-over-Lin; P5.5 Distance; P5.6 Entropy; P5.7 Strong Convexity; P5.12 Sensitivity (Subgradients).
    *   *Assessment:* Good. P5.12 uses subgradients, but subgradients are not formally defined in text.
*   **Action Plan:**
    1.  **Move:** Move "Strict and Strong Convexity" sections to Lecture 06.
    2.  **Refine:** Ensure Section 5 (Operations) covers "Pointwise Maximum" and "Composition" thoroughly.

### Lecture 06: Convex Functions – Advanced
*   **Current Content:**
    *   Sec 1: Conjugates (Definition, Fenchel Inequality, Examples).
    *   Sec 2: Quasiconvexity.
    *   Sec 3: Log-Concavity.
*   **Flow Analysis:**
    *   *Missing:* **Subgradients** are missing as a main section.
    *   *Missing:* **Strong Convexity** (moved from L05).
    *   *Gap:* Fenchel Duality theorem is typically here (currently just inequality).
*   **Exercises:**
    *   P6.1 Conjugate of Norm; P6.2 Quasiconvexity; P6.3 Softmax; P6.7 Fenchel.
    *   *Assessment:* Needs exercises on Subgradients.
*   **Action Plan:**
    1.  **Add Section:** "1. Subgradients and Subdifferentials".
    2.  **Add Section:** "2. Smoothness and Strong Convexity" (from L05).
    3.  **Enhance:** Expand Conjugates section to include full Fenchel Duality theorem.

### Lecture 07: Convex Problems – Standard Forms
*   **Current Content:**
    *   Sec 1: Standard Form.
    *   Sec 2: LP (Diet, Chebyshev, etc.).
    *   Sec 3: QP (LS, Mean-Variance, Robust LS).
    *   Sec 4: Linear-Fractional (Charnes-Cooper).
    *   Sec 5: Geometric Programming.
    *   Sec 6: Patterns.
    *   Sec 7: Matrix View.
    *   Sec 8: Reformulation.
*   **Flow Analysis:**
    *   *Status:* Excellent. QP coverage (Sec 3) is very detailed.
    *   *Clarification:* Ensure the distinction between "Standard Forms" (L07) and "Conic Forms" (L08) is clear (L07 focuses on scalar inequalities, L08 on cone memberships).
*   **Exercises:**
    *   P7.1 Diet; P7.3 PSD Block; P7.7 LASSO; P7.8 SVM; P7.9 Robust LS.
    *   *Assessment:* Excellent coverage of modeling.
*   **Action Plan:**
    1.  **Refine:** Ensure QP section explicitly walks through the "Portfolio Optimization" derivation.

### Lecture 08: Convex Problems – Conic Forms
*   **Current Content:**
    *   Sec 1: SOCP (Lorentz Cone, Robust LS).
    *   Sec 2: Robust LP.
    *   Sec 3: SDP (PSD Cone, Hierarchy).
    *   Sec 4: Quasiconvex Opt.
    *   Sec 5: DCP.
*   **Flow Analysis:**
    *   *Missing:* **Exponential Cone** programming is missing.
    *   *Balance:* Section 3 (SDP) is brief on examples compared to SOCP.
*   **Exercises:**
    *   P8.1 Max Abs Dev; P8.3 SOCP Reformulation; P8.4 SDP Eigenvalue.
    *   *Assessment:* Good, but needs Exponential Cone exercises.
*   **Action Plan:**
    1.  **Add Section:** "Exponential Cone Programming" (Entropy max, Log-Sum-Exp).
    2.  **Expand:** Add more SDP examples (e.g., Max Cut relaxation).

### Lecture 09: Duality
*   **Current Content:**
    *   Sec 1: Conjugates/Support Recap.
    *   Sec 2: Lagrangian.
    *   Sec 3: Dual Function.
    *   Sec 4: Dual Problem (Weak/Strong, Slater).
    *   Sec 5: KKT.
    *   Sec 6: Sensitivity.
    *   Sec 7: Examples.
*   **Flow Analysis:**
    *   *Status:* Complete and robust.
*   **Exercises:**
    *   P9.1 Dual QP; P9.3 Sensitivity; P9.4 Dual LP; P9.5 Farkas; P9.6 KKT.
    *   *Assessment:* Solid.
*   **Action Plan:**
    1.  **Link:** Ensure Sensitivity Analysis (Sec 6) connects back to "Shadow Prices" interpretation.

---

## 4. Implementation Roadmap

### Phase 1: Structural Hygiene (Immediate)
1.  **Notation:** Run script to replace `$x$` with `$\mathbf{x}$` (and similar for $y, z, u, v, w$) in all `topics/` HTML files.
2.  **Move Separation:** Extract L04 Sec 1 and insert into L03 (as Sec 5 or integrated). Update indices/links.
3.  **Move Strong Convexity:** Extract L05 Sec 1.5/4.2 and insert into L06.

### Phase 2: Content Injection (High Value)
1.  **L06 Update:** Write new section on **Subgradients**.
2.  **L08 Update:** Write new section on **Exponential Cone**.
3.  **L02 Update:** Add explicit "Slack Variable" walkthrough in Section 6.

### Phase 3: Refinement (Polish)
1.  **L00 Reorder:** Swap Invariants and Norms.
2.  **L03 Reorder:** Swap Operations and Canonical Sets.
3.  **De-duplication:** Remove P2.9/P3.1 duplication. Consolidate Rank-Nullity in L01.
