# Audit Log: Lecture 08 - Convex Problems: Conic Programming

## 1. Content Audit
*   **File:** `topics/08-convex-problems-conic/index.html`
*   **Status:** Complete / **Action Required**
*   **Scope:** SOCP, Robust LP, SDP, Quasiconvex, DCP.
*   **Verification of Definitions:**
    *   **SOCP (Sec 1):** Defined correctly with second-order cone constraints.
    *   **SDP (Sec 3):** Defined with LMI constraints.
    *   **Quasiconvex (Sec 4):** Correctly defined via sublevel sets.
    *   **DCP (Sec 5):** Good introduction to the methodology.
*   **Mathematical Accuracy:**
    *   **Robust LS (Sec 1.4):** Derivation from worst-case perturbation to SOCP is rigorous.
    *   **SDP Examples:** Eigenvalue min and Matrix Norm min correctly converted to LMIs via Schur Complement.
    *   **SOCP $\to$ SDP (Sec 3.5):** Proof of embedding via Schur Complement is correct.
*   **Completeness:**
    *   **Exponential Cone:** **MISSING.** The roadmap explicitly asks for "Exponential Cone Programming" (entropy, log-sum-exp) to be added here.
    *   **Conic Duality:** Briefly mentioned in P8.4 and P8.14, but the main text focuses on the Primal forms. L09 covers duality, but introducing the *primal* exponential cone here is essential for completeness of "Conic Forms".

## 2. Pedagogical Flow
*   **Current Flow:** SOCP -> Robust LP -> SDP -> Quasiconvex -> DCP.
*   **Critique:**
    *   Logical progression from vector norms (SOCP) to matrix norms (SDP).
    *   Quasiconvex optimization is a bit of an outlier here; it fits better with L07 (Standard Forms) or as an algorithm (Bisection), but placing it here is acceptable as an "advanced class".
    *   **Action:** Insert "Exponential Cone Programming" before Quasiconvex Optimization.

## 3. Writing Style & Formatting
*   **Notation:**
    *   Vectors are italic $x$. **Action:** Change to bold `\mathbf{x}`.
    *   Matrices Capital.

## 4. Exercises Audit
*   **Current List:** P8.1 - P8.14.
*   **Content:**
    *   P8.1 (Max Abs Dev): Good reformulation.
    *   P8.4 (SDP Eigenvalue): Key example.
    *   P8.5 (Portfolio): QCQP as SOCP.
    *   P8.10 (Linear-Fractional): Shows LP reduction.
*   **Missing Exercises:**
    *   **Exponential Cone:** Need exercises on entropy maximization or log-sum-exp as exponential cone programs.
*   **Action Plan:**
    *   Add exercises for Exponential Cone.

## 5. Implementation Checklist
*   [ ] **Add Section:** "Exponential Cone Programming". Define $K_{exp}$, give examples (Entropy, Geometric Programming in conic form).
*   [ ] **Notation:** Global replace `$x$` -> `$\mathbf{x}$`.
*   [ ] **Add Exercises:** Exponential Cone formulations.
