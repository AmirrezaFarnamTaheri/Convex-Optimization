# COURSE BLUEPRINT: Convex Optimization — Interactive Lecture Notes

> **Target Audience:** Advanced undergraduates / graduate students and ML–controls–signal-processing engineers comfortable with multivariable calculus and basic linear algebra, plus Python familiarity for the interactive labs.
> **Course Goal (terminal capability):** Given a real engineering or ML problem, the student can (1) recognize or *reformulate* it as a convex problem, (2) classify it within the LP ⊂ QP ⊂ SOCP ⊂ SDP hierarchy, (3) derive its dual and KKT conditions and extract sensitivity information, and (4) select, implement, and diagnose an appropriate algorithm (gradient / Newton / interior-point) with an understanding of its convergence behavior.
> **Format:** 16 self-paced interactive lectures (~90 min each) with in-browser widgets and Pyodide code labs; roughly a one-semester load at 1–2 lectures/week.

This blueprint is the **single source of truth** for course structure. Lecture pages
under `topics/` implement it; changes to scope, objectives, or ordering must be
reflected here in the same commit (see `CLAUDE.md` §3.5).

---

## 1. Prerequisite Tree & Learning Graph

```text
 External prerequisites            PART I — Foundations
 ┌──────────────────────┐
 │ Multivariable calc   │──┐
 │ Basic linear algebra │──┼──► [L00 LinAlg Basics] ──► [L01 LinAlg Advanced]
 │ Python basics        │──┘            │                       │
 └──────────────────────┘              ▼                       │
                          PART II      [L02 Intro to Convex Opt]◄┘
                                         │
                          PART III       ▼
                                       [L03 Convex Sets] ──► [L04 Cones & Separation]
                                         │                       │
                          PART IV        ▼                       │
                                       [L05 Convex Fn Basics] ──► [L06 Convex Fn Advanced]
                                         │                       │ (conjugates)
                          PART V         ▼                       ▼
                                       [L07 Standard Problems] ─► [L08 Conic (SOCP/SDP)]
                                         │                       │
                                         └────────► [L09 Duality & KKT] ◄─────┐
                                                        │             (L04: separation
                          PART VI                       │              powers strong
                                                        ▼              duality proofs)
                        ┌───────────────┬───────────────┬───────────────┐
                        ▼               ▼               ▼               │
                  [L10 Approx     [L11 Statistical [L12 Geometric       │
                   & Fitting]      Estimation/ML]   Problems]           │
                        │               │               │               │
                        └───────┬───────┴───────────────┘               │
                                ▼                                       │
                  [L13 Unconstrained Min] ──► [L14 Equality-Constrained]│
                                                        │               │
                                                        ▼               │
                                          [L15 Interior-Point Methods] ◄┘
                                                        │
                                                        ▼
                                              [Capstone Project]
```

**Critical-path edges** (a student skipping these will hit a wall):
L02 → L05 (convexity definitions), L04 → L09 (separating hyperplanes underlie strong
duality), L06 → L09 (conjugates appear in dual derivations), L09 → L15 (the central
path is a perturbed-KKT trajectory), L13 → L14 → L15 (Newton machinery builds up).

---

## 2. Module Breakdown

Bloom levels used below: **R**emember, **U**nderstand, **Ap**ply, **An**alyze, **E**valuate, **C**reate.

### PART I — Mathematical Foundations

#### L00 · Linear Algebra Basics (`topics/00-linear-algebra-basics`)
- **Core questions:** What geometric structure does a matrix impose on space? When does $Ax = b$ have a solution, and what is the *best* answer when it doesn't?
- **Learning objectives:**
  1. (U) Relate the four fundamental subspaces to solvability of linear systems.
  2. (Ap) Test positive semidefiniteness via eigenvalues, principal minors, and quadratic forms.
  3. (Ap) Compute orthogonal projections onto subspaces and affine sets.
  4. (An) Derive and interpret the least-squares normal equations $A^\top A \hat x = A^\top b$.
- **Labs/widgets:** eigen/quadratic-form explorer, projection visualizer, PSD cone probe (3 widgets).
- **Assessment:** verify PSD-ness of given matrices; derive a projection formula; least-squares fit with residual-orthogonality check.

#### L01 · Linear Algebra Advanced (`topics/01-linear-algebra-advanced`)
- **Core questions:** How do factorizations (QR, SVD) expose the geometry of a linear map? What does conditioning mean for numerical trust?
- **Learning objectives:**
  1. (U) Interpret SVD as rotate–scale–rotate and read off rank/range/null space.
  2. (Ap) Solve least squares stably via QR; construct the pseudoinverse from SVD.
  3. (An) Predict solution sensitivity from the condition number $\kappa(A) = \sigma_{\max}/\sigma_{\min}$.
- **Labs/widgets:** SVD geometry widget, conditioning explorer (2 widgets).
- **Assessment:** hand-compute a small SVD; compare normal-equations vs. QR accuracy on an ill-conditioned system.

### PART II — Introduction to Optimization

#### L02 · Introduction to Convex Optimization (`topics/02-introduction`)
- **Core questions:** Why does convexity make optimization tractable? What is the problem-class hierarchy, and where does my problem live?
- **Learning objectives:**
  1. (R/U) State the standard-form problem and the definition of a convex problem.
  2. (An) Prove that local optima are global for convex problems.
  3. (U) Place LP ⊂ QP ⊂ SOCP ⊂ SDP in the hierarchy with examples.
  4. (Ap) Express ML problems in the "loss + regularizer" paradigm; apply basic DCP rules.
- **Assessment:** classify given problems into the hierarchy; DCP-verify expressions; standard-form conversions.

### PART III — Convex Sets

#### L03 · Convex Sets & Geometry (`topics/03-convex-sets-geometry`)
- **Learning objectives:**
  1. (R/U) Define affine/convex sets, hulls, and combinations; recognize canonical sets (hyperplanes, halfspaces, polyhedra, norm balls).
  2. (Ap) Prove convexity via convexity-preserving operations (intersection, affine images, perspective, linear-fractional).
  3. (U) Distinguish interior vs. relative interior and why the distinction matters for low-dimensional sets.
- **Assessment:** convexity proofs from definitions vs. from operations; identify rel-int of given sets.

#### L04 · Cones & Separation Theorems (`topics/04-convex-sets-cones`)
- **Core questions:** Why can disjoint convex sets always be separated by a hyperplane, and why is that *the* structural theorem of the course?
- **Learning objectives:**
  1. (An) Prove the separating and supporting hyperplane theorems.
  2. (U) Work with proper cones, generalized inequalities $\preceq_K$, and dual cones $K^*$.
  3. (Ap) Apply Farkas' lemma to certify infeasibility of linear systems.
- **Assessment:** compute dual cones; use a theorem of alternatives to certify infeasibility.

### PART IV — Convex Functions

#### L05 · Convex Functions Basics (`topics/05-convex-functions-basics`)
- **Learning objectives:**
  1. (R/U) State the definitions of convex/strictly/strongly convex functions and the epigraph characterization.
  2. (Ap) Verify convexity via first-order ($f(y) \ge f(x) + \nabla f(x)^\top (y-x)$) and second-order ($\nabla^2 f \succeq 0$) conditions.
  3. (Ap) Build convex functions with the calculus of operations (pointwise max, composition rules, partial minimization).
- **Assessment:** convexity verification portfolio (log-sum-exp, quadratic-over-linear, max eigenvalue, …), each by the cheapest sufficient rule.

#### L06 · Convex Functions Advanced (`topics/06-convex-functions-advanced`)
- **Core questions:** What is the conjugate $f^*(y) = \sup_x (y^\top x - f(x))$ *geometrically*, and why does it keep reappearing in duality?
- **Learning objectives:**
  1. (U/An) Compute and geometrically interpret Fenchel conjugates of standard functions.
  2. (U) Characterize quasiconvexity via sublevel sets; contrast with convexity.
  3. (U) Recognize log-concave/log-convex functions and their closure properties.
- **Assessment:** conjugate computations; classify functions as convex / quasiconvex / log-concave.

### PART V — Standard Problems & Duality

#### L07 · Standard Convex Problems (`topics/07-convex-problems-standard`)
- **Learning objectives:**
  1. (Ap) Model resource-allocation, portfolio, LASSO, and SVM problems as LP/QP.
  2. (C) Reformulate piecewise-linear and norm-minimization objectives into standard form via epigraph variables.
- **Assessment:** modeling exercises graded on correctness of the reformulation *and* recovery of the original solution.

#### L08 · Conic Optimization (`topics/08-convex-problems-conic`)
- **Learning objectives:**
  1. (Ap) Cast robust least squares as SOCP; matrix-norm minimization and MAX-CUT relaxation as SDP.
  2. (Ap) Solve quasiconvex problems (e.g., fractional programs) by bisection on the sublevel-set feasibility problem.
- **Assessment:** SOCP/SDP modeling set; implement bisection for a linear-fractional program.

#### L09 · Duality Theory (`topics/09-duality`) — **keystone lecture**
- **Core questions:** Where do lower bounds on $p^\star$ come from? When is the bound tight? What do the multipliers *mean*?
- **Learning objectives:**
  1. (Ap) Construct the Lagrangian and dual function for any problem; prove weak duality.
  2. (An) State and apply Slater's condition; explain a strong-duality proof via separating hyperplanes.
  3. (An) Derive KKT conditions and solve small problems analytically with them.
  4. (E) Interpret dual variables as shadow prices / sensitivities of the perturbed problem.
  5. (Ap) Derive duals of LP, QP, SOCP, SDP.
- **Labs/widgets:** 9 widgets (primal–dual 1-D, KKT force balance, conjugate explorer, Slater-failure demo, dual cones, value-function support, …) — the course's richest interactive suite, deliberately.
- **Assessment:** full dual derivations; a KKT case-analysis problem; a sensitivity-interpretation problem.

### PART VI — Applications & Algorithms

#### L10 · Approximation & Fitting (`topics/10-approximation-fitting`)
- **Objectives:** (Ap) pose weighted/regularized regression (ridge, LASSO, elastic net); (E) choose robust losses (Huber, $\ell_1$) against outliers; (Ap) formulate total-variation denoising and basis pursuit.
- **Assessment:** regularization-path lab; robust-vs-LS comparison on contaminated data.

#### L11 · Statistical Estimation & ML (`topics/11-statistical-estimation`)
- **Objectives:** (An) derive MLE/MAP as convex problems (when they are); (Ap) formulate logistic regression and max-margin SVM; (U) Neyman–Pearson as an LP; (Ap) A/D/E-optimal experiment design as convex programs.
- **Assessment:** derive convexity of a given likelihood; experiment-design mini-lab.

#### L12 · Geometric Problems (`topics/12-geometric-problems`)
- **Objectives:** (Ap) compute Chebyshev/analytic centers; (Ap) formulate MVEE and maximum-volume inscribed ellipsoids; (Ap) linear discrimination; (Ap) Fermat–Weber facility location.
- **Assessment:** center-computation lab on a random polyhedron; ellipsoid formulation exercise.

#### L13 · Unconstrained Minimization (`topics/13-unconstrained-minimization`)
- **Objectives:** (Ap/An) implement gradient descent with backtracking and prove/observe linear convergence under strong convexity; (An) explain Newton's quadratic convergence and affine invariance; (U) BFGS/L-BFGS as Hessian approximation; (An) connect condition number to convergence rate.
- **Assessment:** implement GD + Newton in the Pyodide lab; reproduce the conditioning-vs-iterations curve.

#### L14 · Equality-Constrained Minimization (`topics/14-equality-constrained-minimization`)
- **Objectives:** (Ap) solve KKT systems by block elimination; (Ap) feasible-start and infeasible-start Newton; (Ap) eliminate constraints via null-space parameterization.
- **Assessment:** derive the KKT system of an equality-constrained QP and solve it two ways (elimination vs. full KKT solve), confirming agreement.

#### L15 · Interior-Point Methods (`topics/15-interior-point-methods`)
- **Core questions:** How does the log barrier turn constraints into smooth unconstrained problems, and why does the central path lead to the optimum in $O(\sqrt{m})$ Newton-ish iterations?
- **Objectives:** (U) central path as perturbed KKT ($\lambda_i f_i = -1/t$); (Ap) implement the barrier method (outer centering loop / inner Newton loop); (An) state the polynomial complexity result; (U) barrier extensions to SOCP/SDP.
- **Assessment:** barrier-method implementation on a small LP; plot duality gap $m/t$ vs. outer iterations.

---

## 3. Capstone Project Specification

> **Deliverable:** An end-to-end *"model → dualize → solve → diagnose"* case study, submitted as a self-contained notebook/widget page in the style of the course.

The student picks one realistic problem (e.g., robust portfolio construction, TV
image denoising, optimal experiment design, or min-fuel control) and must:

1. **Model** it as a convex problem; prove convexity via the function calculus (L05–L06); place it in the hierarchy (L02, L07–L08).
2. **Dualize** it: derive the dual and KKT conditions; interpret at least one dual variable in domain terms (L09).
3. **Solve** it two ways: a general-purpose formulation *and* a hand-rolled first-order or barrier method (L13–L15), verifying both reach the same optimum and that the duality gap is ~0.
4. **Diagnose:** study sensitivity to one data perturbation and reconcile the observed change in $p^\star$ with the dual-variable prediction.

**Evaluation matrix:**

| Criterion | Weight | What "excellent" looks like |
| :--- | :--- | :--- |
| Correct convex model & proof | 25% | Convexity argued by the cheapest sufficient rule, standard form stated precisely |
| Dual & KKT derivation | 25% | Every step explicit; multipliers interpreted in domain language |
| Working solver + verification | 30% | Two independent solution paths agree; gap and residuals reported with assertions |
| Sensitivity analysis | 10% | Empirical $\Delta p^\star$ matches the shadow-price prediction to first order |
| Presentation quality | 10% | Meets all `CLAUDE.md` invariants (self-contained, scannable, zero handwaving) |

---

## 4. Maintenance Roadmap (known gaps)

| Gap | Detail | Priority |
| :--- | :--- | :--- |
| Widget-coverage imbalance | L09 has 9 widgets; most lectures have 1. Algorithm lectures (L13–L15) benefit most from step-through visualizations (GD trajectory on ill-conditioned quadratics; central-path animation). | High |
| Problems index coverage | `data/problems-index.json` should index a tiered (easy/intermediate/hard) set **with full solutions** for every lecture, not only early ones. | High |
| Capstone scaffold | Add a `topics/capstone/` template page implementing §3's structure with a worked mini-example. | Medium |
| Cross-lecture notation table | Promote the glossary (`data/glossary.json`) to include a symbol table ($f_0$, $f_i$, $\lambda$, $\nu$, $K^*$, $p^\star$, $d^\star$, …) surfaced on every page. | Medium |

Any PR that closes a roadmap item should update this table.
