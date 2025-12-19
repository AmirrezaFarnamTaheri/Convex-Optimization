# Audit Log: Lecture 00 - Linear Algebra Basics

## 1. Content Audit
*   **Definitions:**
    *   Scalars, Vectors, Matrices are defined in Section 1.3.
    *   Subspaces, Rank, Nullspace are defined in Section 2.
    *   Invariants (Trace, Det, Eigenvalues) are in Section 3.
    *   Inner products, Norms in Section 4.
    *   Orthogonality in Section 5.
    *   PSD Matrices in Section 6.
    *   Projections in Section 7.
    *   Least Squares in Section 8.
*   **Accuracy Check:**
    *   Trace/Det/Eigenvalues properties look correct.
    *   Spectral theorem stated correctly for real symmetric matrices.
    *   Rank-Nullity theorem proof looks standard.
    *   Least Squares derivation via calculus and geometry looks correct.
*   **Numbering:**
    *   Sections are numbered 1 to 11.
    *   Subsections 1.1, 1.2, etc. exist.
    *   Exercises are P0.1 to P0.20.

## 2. Completeness and Redundancy
*   **Prerequisites:** Subspaces are defined in Section 2, but used implicitly in 1.5 ("Generated Object" table mentions Subspace). This is fine as 1.5 is an overview.
*   **Redundancy:**
    *   Rank-Nullity is discussed in Section 2.
    *   PSD matrices are discussed in Section 6.
    *   There is a "Forward Connection" box in 6.2 and 6.5 mentioning later lectures.
    *   Is Rank-Nullity defined twice? Only in Section 2.
    *   PSD material seems consolidated in Section 6.

## 3. Pedagogical Flow
*   **Current Flow:** Atoms (Sets/Funcs/Combos) -> Subspaces -> Invariants -> Norms -> Orthogonality -> PSD -> Projections -> LS.
*   **Requested Flow:** Scalars/Vectors -> Matrices -> Operations -> Subspaces -> Eigenvalues -> PSD -> Projections -> LS.
*   **Gap Analysis:**
    *   Section 1.1 "Geometric Atoms" is a bit abstract to start with ("Mixing, Measuring, Pullback").
    *   Section 1.2 "Lines/Segments" jumps into affine/convex combinations before defining vectors/matrices formally (which is 1.3).
    *   **Action:** Swap 1.2 and 1.3? Or merge? The user wants "basic notions precede advanced ones".
    *   The "Atoms" section (1.1) is nice motivation but maybe too meta for "Linear Algebra Basics".
    *   "Operations" (Addition, Multiplication) are mentioned in 1.3 but briefly.
    *   "Matrix Calculus Basics" (1.6) is quite advanced for Section 1. It might belong better after Invariants or Norms, or in a separate section. It relies on inner products (Sec 4) and trace (Sec 3). **Major Issue:** 1.6 uses trace and inner products before they are formally introduced in Sec 3 and 4.
    *   **Proposed Reordering:**
        1.  Scalars, Vectors, Matrices (Old 1.3) + Operations.
        2.  Lines, Segments, Combinations (Old 1.2, 1.5).
        3.  Subspaces (Old 2).
        4.  Invariants (Old 3).
        5.  Inner Products & Norms (Old 4).
        6.  Matrix Calculus (Old 1.6) -> Move to after Norms or near the end? It's used for LS (Sec 8) and PSD (Hessian check). Maybe place it before PSD or just before LS?
        7.  Orthogonality (Old 5).
        8.  Projections (Old 7).
        9.  Least Squares (Old 8).
        10. PSD (Old 6) - *User wants PSD before Projections/LS?* "eigenvalues/eigenvectors -> PSD matrices -> projections and least squares". Yes.
        11. So: Basics -> Subspaces -> Invariants -> Norms -> Matrix Calc? -> Orthogonality -> PSD -> Projections -> LS.
    *   Let's check the user's specific list: "scalars and vectors → matrices → operations (addition, multiplication) → subspaces and dimension → eigenvalues/eigenvectors → PSD matrices → projections and least squares."
    *   Where do Norms/Inner products go? Usually with Orthogonality.
    *   Matrix Calculus is not in the user's list, but is in the content. It is advanced. It fits well before LS (deriving normal equations) or PSD (Hessians).

## 4. Writing Style
*   **Notation:**
    *   Vectors: Currently $x, y$ (italic). User wants **bold** (${\bf x}$).
    *   Matrices: $A, B$ (Capital). Consistent.
    *   Scalars: $\alpha, \beta$ (italic). Consistent.
    *   **Action:** Change all vector variables to `\mathbf{x}`, `\mathbf{y}`, etc. This is a big change in LaTeX.
    *   "Rewrite verbose sentences..." -> Section 1.1 is quite verbose.

## 5. Exercises
*   Current exercises P0.1 - P0.20.
*   Logic:
    *   P0.1 Independence (Computational)
    *   P0.2 Rank-Nullity (Conceptual/Comp)
    *   P0.3 Trace/Det (Proof)
    *   P0.4 Norm Equivalence (Proof)
    *   P0.5 LS from Scratch (Proof/Derivation) -> Depends on Matrix Calc.
    *   P0.6 Matrix Calc Practice.
    *   P0.7 Hessian Cubic.
    *   P0.8 PSD Testing.
    *   P0.9 Schur Complement.
    *   P0.10 Projection Line (Comp).
    *   P0.11 Projection Hyperplane (Comp).
    *   P0.12 Orthogonal Complements (Proof).
    *   P0.13 Frobenius Submult (Proof).
    *   P0.14 Spectral Norm (Proof).
    *   P0.15 Isometries (Proof).
    *   P0.16 Loewner (Proof).
    *   P0.17 Weighted IP (Proof).
    *   P0.18 Projectors (Proof).
    *   P0.19 PSD Cone (Conceptual).
    *   P0.20 General Quad Min (Derivation).
*   **Critique:**
    *   P0.5 (LS) appears before P0.6 (Matrix Calc). Should be swapped or grouped?
    *   P0.10/11 (Projections) are basic but appear late.
    *   **Action:** Reorder exercises to match the new lecture flow.
        *   Basics/Subspaces: P0.1, P0.2, P0.12.
        *   Invariants: P0.3.
        *   Norms/Inner Products: P0.4, P0.13, P0.14, P0.15, P0.17.
        *   Matrix Calc: P0.6, P0.7.
        *   PSD: P0.8, P0.16, P0.19, P0.9.
        *   Projections/Orthogonality: P0.18, P0.10, P0.11.
        *   LS/Opt: P0.5, P0.20.

## 6. Proposed Plan Details
*   **Structure:**
    1.  **Vectors, Matrices, and Linear Combinations** (Merge 1.2, 1.3, 1.5). Define scalars, vectors (bold), matrices, operations. Then combinations.
    2.  **Subspaces and Dimension** (Section 2).
    3.  **Algebraic Invariants** (Section 3).
    4.  **Inner Products, Norms, and Geometry** (Section 4). Include angles.
    5.  **Orthogonality** (Section 5). Gram-Schmidt, QR.
    6.  **Matrix Calculus** (Move 1.6 here). Now we have trace and inner products defined.
    7.  **Positive Semidefinite Matrices** (Section 6).
    8.  **Projections and Least Squares** (Merge 7 and 8, or keep adjacent). The user suggested "projections and least squares" as the end.
*   **Formatting:**
    *   Convert vectors to `\mathbf{v}`.
    *   Ensure proofs are clean lists.
