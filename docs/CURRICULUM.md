# COURSE BLUEPRINT: Convex Optimization — Interactive Lecture Notes

> **Target Audience:** Advanced undergraduates / graduate students and ML–controls–signal-processing engineers comfortable with multivariable calculus and basic linear algebra, plus Python familiarity for the interactive labs.
> **Course Goal (terminal capability):** Given a real engineering or ML problem, the student can (1) recognize or *reformulate* it as a convex problem, (2) classify it within the LP ⊂ QP ⊂ SOCP ⊂ SDP hierarchy, (3) derive its dual and KKT conditions and extract sensitivity information, and (4) select, implement, and diagnose an appropriate algorithm (gradient / Newton / interior-point) with an understanding of its convergence behavior.
> **Format:** 16 self-paced interactive lectures (~90 min each) with in-browser widgets; roughly a one-semester load at 1–2 lectures/week.

This blueprint is the **single source of truth** for course structure. Lecture pages
under `topics/` implement it; changes to scope, objectives, or ordering must be
reflected here in the same commit (see `CLAUDE.md`).

**Companion documents** (the curriculum-architecture suite):

| Document | Contents |
| :--- | :--- |
| `docs/PEDAGOGY.md` | Teaching protocol: invariants, concept pipeline, cognitive-load rules, callout taxonomy |
| `docs/NOTATION.md` | Course-wide symbol standard and code↔math naming map |
| `docs/ASSESSMENT.md` | Problem-bank architecture, tier definitions, rubrics, solved exemplars, index schema |
| `docs/WIDGETS.md` | Widget inventory, interaction-design standard, prioritized build backlog |
| `docs/REFERENCES.md` | Canonical bibliography, per-lecture [BV] chapter mapping, citation rules |

---

## 0. Design Philosophy

Five commitments shape every lecture (expanded in `docs/PEDAGOGY.md`):

1. **Geometry before algebra.** Every algebraic object gets a picture first: the
   dual cone before the dual problem, the epigraph before the conjugate, the
   central path before the complexity bound.
2. **One spine, many bodies.** The course has a single narrative spine —
   *sets → functions → problems → duality → algorithms* — and every application
   lecture (L10–L12) is explicitly a body of examples hanging off that spine.
3. **Duality is the payoff, not an appendix.** L04 (separation), L06 (conjugates),
   and L09 (Lagrange duality) are one continuous argument, deliberately spread
   across three parts so the machinery is rehearsed before it is composed.
4. **Algorithms are consequences of analysis.** Convergence behavior is always
   tied back to conditioning (L01) and strong convexity (L06); no algorithm is
   presented as a recipe.
5. **Interaction where intuition is hardest.** Widget effort concentrates where
   static pictures fail: high-dimensional geometry, limiting behavior, and
   trajectory dynamics (see `docs/WIDGETS.md` §3 for the priority function).

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
                                         │                       │ (conjugates, subgradients,
                          PART V         ▼                       ▼  strong convexity)
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

### 1.1 Annotated critical-path edges

A student skipping one of these edges hits a specific, predictable wall:

| Edge | What breaks without it |
| :--- | :--- |
| L00 §7 (PSD) → L05 §7 | The Hessian test $\nabla^2 f \succeq 0$ is unreadable without PSD fluency |
| L00 §5,8 (projections) → L14 | Null-space elimination and projected steps *are* projection theory |
| L01 (SVD, $\kappa$) → L13 | The conditioning–convergence story ($\kappa = \sigma_{\max}/\sigma_{\min}$ controls the GD rate) has no foundation |
| L02 §3 (local=global) → everything | The entire course's *raison d'être* |
| L03 §3 (operations) → L05 §4–5 | Function convexity calculus mirrors set operations; learned twice = learned once |
| L04 §2–3 (dual cones, separation) → L09 §4, §8 | Strong duality proofs and conic duality both stand on separation |
| L05 §6 (first-order condition) → L09 §5 | KKT stationarity is the first-order condition plus multipliers |
| L06 §1 (subgradients) → L09, L13 | Optimality for nondifferentiable objectives (LASSO!) needs $\partial f$ |
| L06 §2 (strong convexity/smoothness) → L13 | Convergence rates are stated in terms of $m, L$ |
| L06 §3 (conjugates) → L09 §3, §7 | Dual functions of separable problems are computed via $f^*$ |
| L07 §1 (epigraph trick) → L08, L10 | Norm and max objectives enter conic form through epigraph variables |
| L09 §5 (KKT) → L14 §1, L15 §3 | KKT systems are what Newton solves; the central path is perturbed KKT |
| L13 (Newton) → L14 → L15 | One Newton machine, three settings: unconstrained → equality-constrained → barrier inner loop |

### 1.2 Cross-cutting threads

Three ideas recur so often they deserve explicit tracking. Each lecture that
advances a thread should name it (a one-line "Thread" callout suffices):

- **Duality thread:** L04 dual cones → L06 conjugates → L09 Lagrange/conic duality
  → L14 dual variables in KKT systems → L15 duality gap $m/t$ as stopping criterion.
- **Conditioning thread:** L01 $\kappa(A)$ → L13 GD zig-zag on ill-conditioned
  quadratics → L14 KKT-system conditioning → L15 central-path numerical behavior
  as $t \to \infty$.
- **Reformulation thread:** L02 standard-form rewrites → L07 epigraph trick →
  L08 conic embeddings → L10–L12 modeling patterns → capstone step 1.

---

## 2. Learner Personas & Tracks

### 2.1 Personas (used for the dual-perspective audit, `CLAUDE.md` §2.6)

| Persona | Background | Goal | Predictable friction points |
| :--- | :--- | :--- | :--- |
| **The ML Engineer** | Strong Python, patchy proofs | Understand *why* LASSO/SVM/logistic work; read optimization papers | Proof-heavy L04/L06; tolerance for $\sup/\inf$ manipulations |
| **The Graduate Theorist** | Strong math, little code | Master duality and complexity results rigorously | Under-values widgets/labs; may skip modeling practice they actually need |
| **The Exam Reviser** | Took a course before | Rebuild fluency fast for quals/interviews | Needs cheat sheets, traps, and problems — not narrative |

### 2.2 Tracks through the same material

| Track | Path | Depth contract |
| :--- | :--- | :--- |
| **Full (default)** | L00 → L15 in order + capstone | All sections incl. appendix proofs |
| **Practitioner** | L02 → L03(§1–3) → L05 → L07 → L08 → L09(§1–6) → L10 → L11 → L13 → L15(§1–4) | Proof appendices optional; every widget and lab mandatory |
| **Theory-first** | L00 → L06 in order → L09 (incl. all appendices) → L13 → L15, dipping into L07/L08 for examples | All proofs; labs optional but recommended |
| **Rapid revision** | Cheat-sheet sections of L02, L05, L09, L13, L15 + `docs/ASSESSMENT.md` mastery checklists + hard-tier problems | Timed problem solving only |

Site implication: the syllabus page should eventually surface these tracks
(roadmap item R6).

---

## 3. Content Status Audit (2026-07)

Ground truth from inspecting every `topics/*/index.html` (size is a proxy for
depth; section structure is the real signal):

| Lecture | Size | Structure | Status |
| :--- | ---: | :--- | :--- |
| L00 Linear Algebra Basics | 215 KB | 11 numbered sections + proofs appendix + exercises + cheat sheet | **Developed** |
| L01 Linear Algebra Advanced | 75 KB | 8 sections + appendix + exercises | **Developed** |
| L02 Introduction | 121 KB | 12 sections + exercises | **Developed** |
| L03 Convex Sets & Geometry | 141 KB | 8 sections + appendix + exercises | **Developed** |
| L04 Cones & Separation | 82 KB | 5 sections + appendix + exercises | **Developed** |
| L05 Convex Functions Basics | 196 KB | 10 sections + appendix + exercises | **Developed** |
| L06 Convex Functions Advanced | 139 KB | 7 sections (subgradients, strong convexity, conjugates, quasi/log-convexity) + appendix | **Developed** |
| L07 Standard Problems | 131 KB | 9 sections (incl. LFP + **GP**) + appendix | **Developed** |
| L08 Conic Problems | 114 KB | 8 sections (incl. **exponential cone**) + appendix | **Developed** |
| L09 Duality | 134 KB | 12 sections + 9 dedicated HTML widgets + appendix | **Developed (flagship)** |
| L10 Approximation & Fitting | 27 KB | Generic "Key Concepts / Widgets / Examples" shell | **THIN — needs build-out** |
| L11 Statistical Estimation | 21 KB | Generic shell | **THIN — needs build-out** |
| L12 Geometric Problems | 22 KB | Generic shell | **THIN — needs build-out** |
| L13 Unconstrained Minimization | 86 KB | Key concepts + solved exercises + convergence-proof appendix | **Partial** |
| L14 Equality-Constrained | 19 KB | Generic shell | **THIN — needs build-out** |
| L15 Interior-Point Methods | 18 KB | 8 concept subsections + 3 widgets + 5 problems, all compact | **THIN — needs build-out** |

Data-layer audit: `data/problems-index.json` holds only **15 problems** keyed to
**obsolete slugs** (`02-convex-sets` → today's L03; the lone
`03-convex-functions` entry is Fenchel/biconjugate material → today's **L06** —
per-problem repair map in `docs/ASSESSMENT.md` §5). `data/glossary.json` has 84
terms but is **missing at least 11 load-bearing ones**: subgradient,
subdifferential, strong convexity, smoothness, barrier, central path, Newton
decrement, self-concordance, Huber, soft thresholding, proximal.
`data/diagrams-index.json` has 39 entries. Infrastructure notes:
`static/js/widgets-loader.js` is an **empty stub** no page uses (widgets mount
via inline ES-module scripts; L09 uses iframes — mechanics in
`docs/WIDGETS.md` §1), and the L09 iframe widgets hardcode a dark palette that
ignores the site theme switcher.

> **Note:** The per-lecture specs in §4 are written to the *target* state. For
> THIN lectures they are the build-out specification, not a description of
> current content.

---

## 4. Module Specifications

Bloom levels: **R**emember, **U**nderstand, **Ap**ply, **An**alyze, **E**valuate, **C**reate.
Widget names refer to real files under `topics/NN-*/widgets/` (inventory in `docs/WIDGETS.md`).

---

### PART I — Mathematical Foundations

#### L00 · Linear Algebra Basics (`topics/00-linear-algebra-basics`) — Developed

- **Role in spine:** Supplies the geometric vocabulary (subspaces, projections,
  PSD order) that Parts III–VI consume constantly.
- **Core questions:** What geometric structure does a matrix impose on space?
  When does $Ax=b$ have a solution — and what is the *best* answer when it doesn't?
  What does $A \succeq 0$ buy us?
- **Concept inventory:** fields/vector spaces → subspaces & four fundamental
  subspaces → determinant/trace/eigenvalues (incl. spectral mapping) → inner
  products, norms, angles → orthogonality & projections → matrix calculus
  (gradients of $a^\top x$, $x^\top A x$) → PSD matrices (definitions,
  eigenvalue/minor tests, square roots) → projections onto subspaces/affine
  sets → least squares.
- **Learning objectives:**
  1. (U) Relate the four fundamental subspaces to solvability of $Ax=b$.
  2. (Ap) Test PSD-ness three ways: eigenvalues, principal minors, quadratic form.
  3. (Ap) Compute orthogonal projections onto subspaces and affine sets.
  4. (Ap) Differentiate quadratic and linear forms ($\nabla x^\top A x = (A{+}A^\top)x$).
  5. (An) Derive the normal equations $A^\top A \hat x = A^\top b$ and interpret residual orthogonality.
- **Key derivations (must remain complete):** projection matrix $P = A(A^\top A)^{-1}A^\top$;
  spectral theorem statement + proof sketch in appendix; least-squares optimality.
- **Misconceptions & traps:**
  - "PSD means all entries $\ge 0$" → counterexample $\begin{psmallmatrix}1&-1\\-1&2\end{psmallmatrix}$ vs $\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}$.
  - "Eigenvalues exist and are real for every matrix" → symmetric hypothesis matters.
  - Confusing $\nabla f$ layout conventions (numerator vs denominator) — the course fixes one (see `docs/NOTATION.md` §5).
- **Widgets:** `la_batch1.html`, `la_batch2.html`, `hessian-landscape-visualizer.js`, `norm-geometry-visualizer.js`.
- **Assessment targets:** 8 problems (3 easy / 3 medium / 2 hard) per `docs/ASSESSMENT.md` §3.
- **Mastery checklist:** □ state all four subspaces of a given small $A$ □ verify PSD by two different tests □ derive normal equations unaided □ compute a projection onto an affine set.

#### L01 · Linear Algebra Advanced (`topics/01-linear-algebra-advanced`) — Developed

- **Role in spine:** Factorization fluency and the conditioning thread's origin.
- **Core questions:** How do QR and SVD expose the geometry of a linear map?
  When should I distrust a numerically computed solution?
- **Concept inventory:** determinant/trace as invariants → eigenvalues & dynamics
  → induced matrix norms → QR (Gram–Schmidt & Householder view) → SVD
  (existence, geometry, low-rank approximation / Eckart–Young) → pseudoinverse
  → condition number.
- **Learning objectives:**
  1. (U) Interpret SVD as rotate–scale–rotate; read rank/range/null space off it.
  2. (Ap) Solve least squares via QR; build $A^\dagger$ from the SVD.
  3. (Ap) Use Eckart–Young to justify truncated-SVD approximation.
  4. (An) Predict solution sensitivity from $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ and connect to induced norms.
- **Misconceptions & traps:**
  - "Normal equations are fine" → $\kappa(A^\top A) = \kappa(A)^2$; QR exists for a reason.
  - "Eigen-decomposition ≈ SVD" → only for symmetric PSD; SVD always exists, eigendecomposition doesn't.
- **Widgets:** `la_batch2.html`, `la_batch3.html`.
- **Assessment targets:** 6 problems (2/3/1). Include one numerical experiment (ill-conditioned Vandermonde fit, QR vs normal equations).
- **Mastery checklist:** □ hand-compute a 2×2 SVD □ state Eckart–Young □ explain why $\kappa$ squared hurts □ pick QR vs SVD vs Cholesky for three scenarios.

---

### PART II — Introduction

#### L02 · Introduction to Convex Optimization (`topics/02-introduction`) — Developed

- **Role in spine:** The thesis statement of the course; every later lecture is
  a footnote to §3 (local = global).
- **Core questions:** Why is convexity *the* boundary between easy and hard
  optimization? Where does my problem live in the hierarchy? How do
  practitioners actually write problems down?
- **Concept inventory:** optimization problem anatomy → convex problem definition
  → local=global theorem → hierarchy LP ⊂ QP ⊂ QCQP ⊂ SOCP ⊂ SDP → loss +
  regularizer paradigm → standard-form transformations → DCP ruleset (first
  encounter) → convexity-verification checklist → end-to-end workflow.
- **Learning objectives:**
  1. (R/U) State standard form and what makes a problem convex (convex $f_0, f_i$; affine $h_j$).
  2. (An) Prove local=global; identify exactly where convexity enters the proof.
  3. (U) Place LP/QP/SOCP/SDP with one canonical example each and strict-inclusion witnesses.
  4. (Ap) Express ridge/LASSO/SVM in loss+regularizer form; run the DCP checklist on given expressions.
- **Misconceptions & traps:**
  - "Convex = has a minimum" → $e^{-x}$ is convex with no minimizer; existence ≠ convexity.
  - "Maximizing a convex function is convex" → it's concave maximization that is; convex *maximization* is NP-hard in general.
  - "DCP rejection = nonconvex" → DCP-invalid merely means *not certified*; rewriting may fix it.
- **Widgets:** `convex-combination.js`, `optimization-landscape.js`, `problem-flowchart.js`, `convergence-comparison.js`.
- **Assessment targets:** 8 problems (3/3/2), heavy on classification-into-hierarchy and rewrite drills.
- **Mastery checklist:** □ reproduce local=global proof □ classify 5 fresh problems □ rewrite an $\ell_1$ objective in standard form □ explain one DCP false-negative.

---

### PART III — Convex Sets

#### L03 · Convex Sets & Geometry (`topics/03-convex-sets-geometry`) — Developed

- **Core questions:** Which sets are convex, how do I *prove* it cheaply, and
  which operations let me build complicated convex sets from simple ones?
- **Concept inventory:** affine/convex/conic combinations & hulls → canonical
  sets (hyperplanes, halfspaces, balls, ellipsoids, polyhedra, simplexes, norm
  balls, PSD cone) → convexity-preserving operations (intersection, affine
  image/preimage, perspective, linear-fractional) → separation preview →
  topology (closure, interior, **relative interior**, boundary).
- **Learning objectives:**
  1. (R/U) Define and distinguish affine/convex/conic hulls; compute them for small examples.
  2. (Ap) Prove convexity two ways: from the definition, and by exhibiting the set as an operation-image of canonical sets.
  3. (U) Explain why relative interior (not interior) is the right notion for low-dimensional sets — and foreshadow Slater.
  4. (An) Prove the PSD cone is convex and closed.
- **Misconceptions & traps:**
  - "Union of convex sets is convex" → two points, one in each.
  - "Open convex sets have no supporting hyperplanes at boundary" confusion — boundary structure preview needs care.
  - Treating $\operatorname{int} C = \emptyset$ as pathology instead of the *normal* situation for constraint sets in $\mathbb{R}^n$.
- **Widgets:** `convex-geometry-lab.js`, `polyhedron-visualizer.js`, `ellipsoid-explorer.js`.
- **Assessment targets:** current index has 14 problems under stale slug `02-convex-sets` — re-key and rebalance to 8 (3/3/2).
- **Mastery checklist:** □ compute hulls of a 4-point set □ two-method convexity proof □ rel-int of a segment in $\mathbb{R}^3$ □ perspective-function image argument.

#### L04 · Cones & Separation Theorems (`topics/04-convex-sets-cones`) — Developed

- **Role in spine:** The structural engine of duality. Everything in L09 §4/§8
  discharges into this lecture's theorems.
- **Core questions:** Why can disjoint convex sets be separated by a hyperplane?
  What is a *dual cone* and why does $\preceq_K$ generalize $\le$ correctly?
- **Concept inventory:** cones, proper cones → generalized inequalities
  $\preceq_K$ and their arithmetic → dual cones $K^*$ (with the four canonical
  self-dual examples: $\mathbb{R}^n_+$, $\mathcal{Q}^n$, $\mathbb{S}^n_+$, and
  $\{0\}^* = \mathbb{R}^n$) → separating hyperplane theorem (with proof via
  closest-point) → supporting hyperplane theorem → theorems of alternatives /
  Farkas' lemma.
- **Learning objectives:**
  1. (U) Verify properness of a cone; order vectors/matrices with $\preceq_K$.
  2. (Ap) Compute dual cones of polyhedral and norm cones; prove self-duality of $\mathbb{S}^n_+$.
  3. (An) Prove the separating hyperplane theorem for a point and a closed convex set.
  4. (Ap) Use Farkas to certify infeasibility of $Ax \le b$ systems, and explain the certificate as a dual object.
- **Misconceptions & traps:**
  - "Any two disjoint convex sets are *strictly* separated" → open/closed and compactness hypotheses matter (classic counterexample: hyperbola epigraph vs. axis).
  - "Dual cone = orthogonal complement" → only for subspaces; the inequality vs. equality distinction is the whole point.
  - Farkas as magic → it is separation applied to a cone and a point.
- **Widgets:** `separating-hyperplane.js`; L09's `soc_dual_cone.html` and `psd_cone_2x2.html` are natural cross-links.
- **Assessment targets:** 7 problems (2/3/2) incl. one alternatives-certificate computation.
- **Mastery checklist:** □ dual cone of $\{x : x_1 \ge |x_2|\}$ □ separation proof skeleton from memory □ Farkas certificate for a given infeasible system □ state where properness is used in $\preceq_K$.

---

### PART IV — Convex Functions

#### L05 · Convex Functions Basics (`topics/05-convex-functions-basics`) — Developed

- **Core questions:** What are the *cheapest sufficient conditions* for
  convexity, and how do I combine known-convex atoms into certified-convex
  expressions?
- **Concept inventory:** definitions (convex/strict/concave, extended values,
  domains) → epigraph characterization → standard atom library (affine, exp,
  powers, log, norms, max, log-sum-exp, quadratic-over-linear, log-det) →
  operations preserving convexity (nonneg. weighted sums, pointwise max/sup,
  composition rules, partial minimization, perspective) → first-order condition
  → second-order condition.
- **Learning objectives:**
  1. (R/U) State definitions with correct domain handling (extended-value convention).
  2. (U) Move fluently between function convexity and epigraph convexity.
  3. (Ap) Verify convexity by the *cheapest* sufficient rule, in the order: atom? → operations? → composition? → Hessian (last resort).
  4. (An) Prove the first-order characterization and explain its geometric meaning (global underestimator).
  5. (Ap) Run the Hessian test with correct PSD reasoning (ties to L00 §7).
- **Misconceptions & traps:**
  - "Composition of convex functions is convex" → needs monotonicity conditions; $e^{-x^2}$ kills the naive rule.
  - Forgetting **domain convexity**: $1/x$ on $x \neq 0$ is not convex; on $x>0$ it is.
  - "Checking the Hessian is always easiest" → log-sum-exp's Hessian vs. its composition certificate.
- **Widgets:** `convex-function-inspector.js`, `hessian-heatmap.js`, `operations-preserving.js`.
- **Assessment targets:** build to 9 (3/4/2) — a "verification portfolio" where each problem forbids the previous problem's technique.
- **Mastery checklist:** □ certify log-sum-exp two ways □ state all composition rules from memory □ produce a counterexample to a false rule □ epigraph⇄function convexity both directions.

#### L06 · Convex Functions Advanced (`topics/06-convex-functions-advanced`) — Developed

- **Role in spine:** The analytic toolkit for both duality (conjugates,
  subgradients) and algorithms (strong convexity, smoothness). *The most
  load-bearing lecture that students underrate.*
- **Core questions:** How do we do calculus when $f$ has kinks? What pair of
  constants controls how fast algorithms converge? What is $f^*$ geometrically?
- **Concept inventory:** subgradients & subdifferentials (existence,
  $\partial|x|$, optimality $0 \in \partial f$) → smoothness ($L$-Lipschitz
  gradient) and strong convexity ($m$), the sandwich
  $\tfrac m2\|y-x\|^2 \le f(y) - f(x) - \nabla f(x)^\top(y-x) \le \tfrac L2\|y-x\|^2$
  → Fenchel conjugate $f^*(y) = \sup_x (y^\top x - f(x))$: geometry (supporting
  lines with slope $y$), Fenchel–Young inequality, biconjugation, key pairs
  (quadratic↔quadratic, $\log\sum e^{x_i} \leftrightarrow$ negative entropy,
  norm↔indicator of dual ball) → quasiconvexity via sublevel sets →
  log-concavity/log-convexity and closure properties.
- **Learning objectives:**
  1. (Ap) Compute subdifferentials of $|x|$, $\|x\|_1$, $\max_i x_i$; use $0 \in \partial f$ to solve the soft-threshold problem.
  2. (U/An) Derive the $m$–$L$ sandwich and preview its algorithmic meaning ($\kappa = L/m$).
  3. (Ap) Compute conjugates of the key pairs; interpret $f^*$ as the "price-taking" transform.
  4. (An) Prove sublevel-set characterization of quasiconvexity; give a quasiconvex-not-convex example ($\sqrt{|x|}$, linear-fractional).
  5. (U) Recognize log-concave densities (Gaussian, exponential, uniform) and why marginalization preserves log-concavity (statement).
- **Misconceptions & traps:**
  - "Subgradient = gradient that sometimes doesn't exist" → $\partial f$ is a *set*; at kinks it has many elements and that multiplicity is the useful part.
  - "$f^{**} = f$ always" → needs closed convex; the biconjugate is the convex envelope otherwise.
  - "Quasiconvex ⊂ convex-ish, so sums are fine" → sums of quasiconvex functions need not be quasiconvex.
- **Widgets (gap):** current widgets are **duplicates of L05's** (`convex-function-inspector.js`, `hessian-heatmap.js`, `operations-preserving.js`). L09's `logsumexp_conjugate_widget.html` belongs conceptually here — build a dedicated conjugate-geometry and subgradient widget (backlog W2, W3 in `docs/WIDGETS.md`).
- **Assessment targets:** 8 problems (2/4/2) incl. one full conjugate table row derived from scratch; the stale-keyed Fenchel/biconjugate problem `03-015` re-keys here (`docs/ASSESSMENT.md` §5).
- **Mastery checklist:** □ $\partial \|x\|_1$ at a point with zeros □ derive soft-thresholding □ conjugate of a quadratic with $A \succ 0$ □ $m$–$L$ sandwich statement + one-line proof sketch.

---

### PART V — Standard Problems & Duality

#### L07 · Standard Convex Problems (`topics/07-convex-problems-standard`) — Developed

- **Core questions:** How do real modeling tasks compile down to LP/QP — and
  what tricks (epigraph, slacks, splitting) make "obviously nonstandard"
  objectives standard?
- **Concept inventory:** standard form & epigraph transformation → general
  reformulation moves (slack variables, variable splitting $x = x^+ - x^-$,
  monotone transforms) → LP (polyhedral language; diet, transportation,
  Chebyshev center) → QP (curvature language; portfolio, LASSO-as-QP, SVM) →
  linear-fractional programming → geometric programming (posynomials, log-log
  convexity) → matrix viewpoint of QPs.
- **Learning objectives:**
  1. (Ap) Execute the epigraph transformation on $\min \max_i(a_i^\top x + b_i)$ and on norm objectives.
  2. (C) Model diet/transportation/Chebyshev-center as LPs from a word statement.
  3. (C) Model portfolio (mean–variance), LASSO, and soft-margin SVM as QPs.
  4. (Ap) Convert a linear-fractional program to an LP (Charnes–Cooper).
  5. (Ap) Convert a GP to convex form via $x_i = e^{y_i}$ + log.
- **Misconceptions & traps:**
  - "$\ell_1$ objectives need special solvers" → splitting/epigraph gives a plain LP/QP.
  - "The reformulated solution *is* the answer" → must map auxiliary-variable solutions back and argue equivalence (tightness at optimum).
  - GP looks nonconvex and *is* nonconvex in $x$ — convexity lives in the log-transformed variables.
- **Widgets:** `reformulation-tool.js`.
- **Assessment targets:** 8 problems (2/4/2), graded on reformulation correctness *and* solution recovery.
- **Mastery checklist:** □ epigraph-transform three objective types □ Charnes–Cooper from memory □ SVM primal QP from the margin story □ explain when a slack inequality is tight.

#### L08 · Conic Optimization (`topics/08-convex-problems-conic`) — Developed

- **Core questions:** What do the second-order, semidefinite, and exponential
  cones each "buy" as modeling languages, and how do relaxations trade
  exactness for tractability?
- **Concept inventory:** SOCP (norm-cone geometry; robust LS, robust LP with
  ellipsoidal uncertainty) → SDP (LMI language; matrix-norm minimization,
  max-eigenvalue, MAX-CUT relaxation with the $x x^\top \to X \succeq 0,
  \operatorname{rank}=1$-dropped story) → exponential-cone programs
  (relative entropy, logistic modeling) → quasiconvex optimization via
  bisection on feasibility problems → DCP recap tying the hierarchy together.
- **Learning objectives:**
  1. (Ap) Cast robust least squares and hyperbolic constraints ($x^2 \le yz$) as SOC constraints.
  2. (Ap) Write max-eigenvalue and spectral-norm minimization as SDPs via LMIs and the Schur complement.
  3. (An) Derive the MAX-CUT SDP relaxation and state exactly which constraint was dropped.
  4. (Ap) Implement quasiconvex bisection: feasibility subproblem, tolerance, iteration bound $\lceil \log_2((u-l)/\epsilon) \rceil$.
- **Misconceptions & traps:**
  - Schur complement direction errors (which block must be $\succ 0$).
  - "Relaxation optimum = original optimum" → it's a *bound*; rounding gives feasible points, Goemans–Williamson gives the guarantee (statement only).
  - "Quasiconvex ⇒ use gradient descent" → bisection over convex feasibility is the reliable route.
- **Widgets:** `sdp-visualizer.js`, `solver-guide.js`.
- **Assessment targets:** 7 problems (2/3/2) incl. one Schur-complement derivation and one bisection implementation.
- **Mastery checklist:** □ SOC form of $\|Ax+b\|_2 \le c^\top x + d$ conditions □ Schur complement both directions □ MAX-CUT relaxation from scratch □ bisection iteration count.

#### L09 · Duality Theory (`topics/09-duality`) — Developed · **keystone lecture**

- **Role in spine:** Where L04's separation, L06's conjugates, and L05's
  first-order conditions compose into the course's central theorem-cluster.
- **Core questions:** Where do lower bounds on $p^\star$ come from? When are
  they tight? What do multipliers *mean* economically and geometrically?
- **Concept inventory:** geometric foundations (value function, supporting
  lines) → Lagrangian $L(x,\lambda,\nu) = f_0 + \sum \lambda_i f_i + \sum \nu_j h_j$
  → dual function $g(\lambda,\nu) = \inf_x L$ (concave always; conjugate
  connection $g = -f_0^*(\cdot)$ for linearly-constrained forms) → weak duality
  → dual problem & strong duality; Slater's condition (and its rel-int
  refinement, closing the loop to L03 §5) → geometric proof via separating
  hyperplane on the value-function epigraph → KKT conditions (necessity under
  strong duality; sufficiency under convexity) → perturbation/sensitivity,
  shadow prices $\lambda_i^\star = -\partial p^\star/\partial u_i$ → worked
  duals (LP, QP, norm problems, entropy) → conic duality with $K^*$
  (SOCP/SDP duals; complementary slackness on cones).
- **Learning objectives:**
  1. (Ap) Construct $L$ and $g$ for any given problem; prove weak duality in two lines.
  2. (An) State Slater precisely (rel-int version) and exhibit the failure mode when it's violated.
  3. (An) Reproduce the separating-hyperplane proof of strong duality at whiteboard depth.
  4. (Ap) Derive and *use* KKT: case-split on active sets to solve small problems analytically (e.g., water-filling).
  5. (E) Interpret $\lambda^\star$ as shadow prices; predict $\Delta p^\star$ to first order under constraint perturbation.
  6. (Ap) Derive the duals of LP, QP, SOCP, SDP and verify weak duality directly.
- **Misconceptions & traps:**
  - "Strong duality always holds for convex problems" → Slater exists because it doesn't (nonzero duality-gap example in `slater_failure_dual_attainment.html`).
  - "KKT ⇒ optimal" for nonconvex problems → necessity vs. sufficiency direction discipline.
  - Sign-convention chaos ($\lambda \ge 0$ with $f_i \le 0$; maximization flips) — `docs/NOTATION.md` §4 is normative.
  - "Complementary slackness means both can be zero" → it means *at least one* is zero; strict complementarity is extra.
- **Widgets (9 — flagship suite):** `primal_dual_1d.html`, `kkt_vector_balance.html`, `value_function_support.html`, `slater_failure_dual_attainment.html`, `logsumexp_conjugate_widget.html`, `equality_dual_projection_2d.html`, `separation_two_disks.html`, `soc_dual_cone.html`, `psd_cone_2x2.html`.
- **Assessment targets:** 10 problems (3/4/3) — the largest bank; must include one full KKT case-analysis and one sensitivity prediction verified numerically.
- **Mastery checklist:** □ dual of an LP in ≤ 5 minutes □ water-filling via KKT □ state Slater + failure example □ shadow-price prediction matching a perturbed re-solve □ SDP dual with $\mathbb{S}^n_+$ self-duality invoked correctly.

---

### PART VI — Applications & Algorithms

#### L10 · Approximation & Fitting (`topics/10-approximation-fitting`) — **THIN: build-out spec**

- **Role in spine:** First applications lecture; every model here is a
  reformulation-thread exercise with statistical meaning deferred to L11.
- **Core questions:** How do norm choice and regularizer choice encode
  assumptions about noise and about the solution? Why does $\ell_1$ produce
  zeros?
- **Target structure (bring to the L03–L09 standard):** numbered sections —
  (1) norm approximation $\min \|Ax - b\|$ and the penalty-shape story
  ($\ell_2$ vs $\ell_1$ vs $\ell_\infty$ residual distributions);
  (2) least-squares variants (weighted, regularized; Tikhonov closed form);
  (3) regularization paths — ridge vs LASSO, and the geometric ball-meets-level-set
  sparsity picture plus the soft-thresholding connection (L06 §1);
  (4) robust fitting — Huber loss derivation, $\ell_1$ regression as LP;
  (5) signal recovery — total-variation denoising, basis pursuit;
  (6) matrix problems — matrix completion / nuclear-norm as the rank analogue of $\ell_1$;
  (7) cheat sheet; (8) exercises; appendix (Huber-as-infimal-convolution derivation).
- **Learning objectives:**
  1. (Ap) Formulate weighted/regularized LS with closed-form solutions where they exist.
  2. (An) Explain LASSO sparsity twice: geometry (corners) and subgradient stationarity.
  3. (E) Choose a loss (LS / Huber / $\ell_1$) from a residual-distribution description; justify.
  4. (Ap) Formulate TV denoising and basis pursuit; identify each as QP/SOCP/LP.
- **Misconceptions & traps:** "ridge induces sparsity too (just weaker)" → it shrinks but a.s. never zeroes; "Huber is ad hoc" → it is the Moreau/infimal-convolution smoothing of $|\cdot|$; "TV denoising blurs edges" → staircasing is the actual artifact, edges survive.
- **Widgets (already present, wire into new sections):** `least-squares-regularization.js`, `regularization-theory.js`, `robust-regression.js`, `sparse-recovery.js`, `matrix-completion.js`.
- **Assessment targets:** 8 problems (3/3/2) incl. a regularization-path lab and an outlier-contamination comparison.
- **Mastery checklist:** □ ridge closed form □ LASSO sparsity two ways □ Huber threshold meaning □ TV-denoising formulation with correct difference operator.

#### L11 · Statistical Estimation & ML (`topics/11-statistical-estimation`) — **THIN: build-out spec**

- **Core questions:** When is maximum likelihood a convex problem? What do the
  classifiers of ML look like through the convex-optimization lens?
- **Target structure:** (1) MLE — when $-\log p_\theta$ is convex (exponential
  families; Gaussian → LS, Laplace → $\ell_1$); (2) MAP = MLE + regularizer
  (priors ↔ penalties dictionary); (3) logistic regression — model, convex NLL
  derivation, separable-data non-attainment pathology; (4) SVM — margin
  geometry → hinge-loss QP, duality preview of support vectors; (5) hypothesis
  testing — Neyman–Pearson as an LP over randomized tests, minimax tests;
  (6) optimal experiment design — A/D/E-optimality as convex (SDP/log-det)
  problems, with the relaxation-of-integer-allocations framing; (7) cheat
  sheet; (8) exercises; appendix (NLL Hessian PSD proof for logistic).
- **Learning objectives:**
  1. (An) Derive convexity of the logistic NLL (Hessian = $X^\top D X \succeq 0$).
  2. (U) Translate priors↔regularizers (Gaussian↔ridge, Laplace↔LASSO) with the MAP derivation.
  3. (Ap) Formulate soft-margin SVM and identify support vectors via complementary slackness (L09 payoff).
  4. (Ap) Pose Neyman–Pearson as an LP and read the likelihood-ratio threshold from LP structure.
  5. (Ap) Formulate D-optimal design as a log-det maximization and interpret the confidence-ellipsoid meaning.
- **Misconceptions & traps:** "MLE is always convex" → mixture models aren't; "logistic regression can't overfit, it's convex" → convex ≠ regularized (separable-data divergence); "support vectors are the misclassified points" → they include margin-touching correct points.
- **Widgets:** `logistic-regression.js`, `svm-margin.js`, `classification-boundary.js`.
- **Assessment targets:** 7 problems (2/3/2).
- **Mastery checklist:** □ logistic Hessian PSD proof □ MAP↔penalty dictionary □ SVM dual + support-vector identification □ D-optimal formulation.

#### L12 · Geometric Problems (`topics/12-geometric-problems`) — **THIN: build-out spec**

- **Core questions:** How far does convex modeling reach into pure geometry —
  centers, ellipsoids, distances, placement?
- **Target structure:** (1) distance problems — projection onto sets, distance
  between polyhedra as QP; (2) Chebyshev center as LP (the
  $\sup_{\|u\|\le 1}$ elimination derivation in full) vs. analytic center
  (log-barrier preview → L15); (3) ellipsoidal approximation — MVEE (Löwner–John,
  log-det objective) and maximum-volume inscribed ellipsoid, with the $n$-factor
  sandwich statement; (4) discrimination — linear separation as feasibility,
  robust separation as max-margin (cross-link L11 SVM); (5) placement —
  Fermat–Weber and facility location as SOCP; (6) cheat sheet; (7) exercises;
  appendix (MVEE optimality conditions).
- **Learning objectives:**
  1. (Ap) Derive the Chebyshev-center LP from the robust-halfspace condition, every step explicit.
  2. (U) Contrast Chebyshev vs. analytic center (which data they depend on; redundancy sensitivity).
  3. (Ap) Formulate MVEE and inscribed-ellipsoid problems with log-det objectives; state the Löwner–John factor.
  4. (Ap) Model Fermat–Weber as SOCP; explain nondifferentiability at data points via L06 subgradients.
- **Misconceptions & traps:** "the two centers are basically the same" → analytic center moves under redundant constraints, Chebyshev doesn't; "log-det is concave so we're minimizing it" → direction discipline; MVEE vs. inscribed duality-of-roles confusion.
- **Widgets:** `chebyshev-center.js`, `mvee-visualizer.js`, `distance-between-sets.js`, `best-fit-shape.js`, `robust-geometry.js`, `rank-minimization.js`.
- **Assessment targets:** 6 problems (2/3/1).
- **Mastery checklist:** □ Chebyshev LP derivation unaided □ MVEE formulation □ center-contrast essay answer □ Weber-point SOCP.

#### L13 · Unconstrained Minimization (`topics/13-unconstrained-minimization`) — Partial

- **Role in spine:** The algorithmic template: descent direction + step size +
  convergence analysis. L14/L15 are this lecture with constraints folded in.
- **Core questions:** Why does gradient descent zig-zag and Newton doesn't?
  What exactly does the condition number cost you? When is quasi-Newton the
  right middle ground?
- **Concept inventory:** descent framework → step-size rules (exact,
  backtracking/Armijo with parameter meanings) → GD convergence: $O(1/k)$
  convex-smooth, linear rate $\left(\tfrac{\kappa-1}{\kappa+1}\right)^2$-flavored
  under strong convexity (full proof in appendix — present, keep) → steepest
  descent in non-Euclidean norms (why the norm choice is a preconditioner) →
  Newton's method: derivation, quadratic convergence theorem, affine
  invariance, damped vs. pure phases → quasi-Newton BFGS/L-BFGS (secant
  condition, curvature pair intuition) → conditioning thread synthesis.
- **Learning objectives:**
  1. (Ap) Implement GD + backtracking; verify the Armijo condition's role empirically.
  2. (An) Reproduce the strongly-convex linear-rate proof; extract the $\kappa$ dependence.
  3. (An) Prove affine invariance of Newton; explain why it neutralizes conditioning.
  4. (U) Derive the secant condition and explain what BFGS stores vs. L-BFGS.
  5. (E) Choose GD / Newton / L-BFGS for given problem sizes and conditioning; defend the choice.
- **Misconceptions & traps:** "smaller step is always safer" → too small never converges in budget, the rate bound is two-sided in spirit; "Newton always converges" → damped phase exists because it doesn't; "L-BFGS approximates the Hessian" → it approximates the *inverse* action on a vector, storing only pairs.
- **Widgets:** `gradient-descent-visualizer.js`, `gd-vs-newton.js`, `convergence-rate.js`, `norm-steepest.js`.
- **Build-out gap:** promote "Key Concepts" into the numbered-section standard; the solved-exercise set and convergence-proof appendix already meet the bar.
- **Assessment targets:** 8 problems (2/4/2) incl. the conditioning-vs-iterations reproduction lab.
- **Mastery checklist:** □ backtracking pseudocode from memory □ linear-rate proof sketch □ affine-invariance proof □ solver choice for three scenarios.

#### L14 · Equality-Constrained Minimization (`topics/14-equality-constrained-minimization`) — **THIN: build-out spec**

- **Core questions:** How does Newton's method absorb $Ax = b$? Why is the KKT
  system the *object*, and elimination just one way to solve it?
- **Target structure:** (1) problem class & optimality — KKT system
  $\begin{psmallmatrix}\nabla^2 f & A^\top\\ A & 0\end{psmallmatrix}
  \begin{psmallmatrix}\Delta x\\ w\end{psmallmatrix} =
  \begin{psmallmatrix}-\nabla f\\ 0\end{psmallmatrix}$ derived from L09 KKT;
  (2) solving KKT systems — block elimination, Schur complement (L08 payoff),
  when the (1,1) block is singular; (3) elimination method — null-space
  parameterization $x = F z + \hat x$, reduction to unconstrained (L13 payoff);
  (4) feasible-start Newton — the equality-constrained Newton step preserves
  feasibility; (5) infeasible-start Newton — primal-dual residual view, why the
  residual norm decreases; (6) cheat sheet; (7) exercises; appendix
  (convergence statement, nonsingularity conditions).
- **Learning objectives:**
  1. (An) Derive the KKT system for equality-constrained QP from stationarity + primal feasibility.
  2. (Ap) Solve it two ways (block elimination; null-space) and verify agreement.
  3. (U) Explain feasible vs. infeasible start: what invariant each maintains.
  4. (Ap) Implement infeasible-start Newton on a small QP tracking $\|r\|$.
- **Misconceptions & traps:** "eliminate variables by hand first, always" → destroys sparsity; structured KKT solves beat naive elimination; "the KKT matrix is PSD" → it is symmetric *indefinite* (saddle-point) — Cholesky doesn't apply; "infeasible start means the method is broken" → it's a feature with its own convergence theory.
- **Widgets:** `null-space-visualizer.js`, `projected-gd.js`, `feasible-vs-interior.js`.
- **Assessment targets:** 6 problems (2/3/1).
- **Mastery checklist:** □ KKT system from scratch □ two-method agreement check □ saddle-point (not PSD) explanation □ residual-decrease statement.

#### L15 · Interior-Point Methods (`topics/15-interior-point-methods`) — **THIN: build-out spec**

- **Role in spine:** The synthesis finale: barriers (L12 analytic center),
  Newton (L13–L14), duality gap (L09), conic generality (L04/L08).
- **Core questions:** How does $-\sum \log(-f_i(x))$ turn inequalities into
  smoothness? Why does the central path exist, and why does following it cost
  only $O(\sqrt m)$ Newton rounds?
- **Target structure (expand the existing 8 compact subsections):**
  (1) inequality-constrained setting & the indicator-function idea;
  (2) log barrier — derivation as smoothed indicator, gradient/Hessian
  formulas in full; (3) central path — definition via $\min t f_0 + \phi$,
  the perturbed-KKT characterization $\lambda_i f_i = -1/t$, and the
  **duality-gap identity: gap $= m/t$ exactly** (with the dual-feasible-point
  construction written out); (4) barrier method — outer/inner loop pseudocode,
  choice of $\mu$, warm starts; (5) complexity — self-concordance stated
  honestly (definition + why it enables the bound; proof pointered to
  appendix), $O(\sqrt m \log(1/\epsilon))$ result; (6) generalized
  inequalities — barriers for $\mathcal{Q}^n$ and $\mathbb{S}^n_+$
  ($-\log\det$), conic IPMs; (7) primal-dual methods — the practical variant,
  Mehrotra sketched at survey depth; (8) phase I — feasibility via the
  auxiliary problem; (9) cheat sheet; (10) exercises; appendix (central-path
  existence, complexity proof).
- **Learning objectives:**
  1. (Ap) Compute $\nabla\phi$, $\nabla^2\phi$ for the log barrier of a polyhedron.
  2. (An) Derive the gap-$= m/t$ identity including the dual feasible point.
  3. (Ap) Implement the barrier method on a small LP; plot gap vs. Newton iterations and observe the $\mu$ trade-off.
  4. (U) State the self-concordance definition and the role it plays (no hand-waved "it just works").
  5. (U) Write the $\mathbb{S}^n_+$ barrier and explain why $-\log\det$ generalizes $-\sum\log$.
- **Misconceptions & traps:** "large $t$ immediately = accurate, so start huge" → Newton's basin collapses; the path-following schedule *is* the algorithm; "IPMs beat simplex always" → dimension/sparsity/warm-start trade-offs (the `lp-simplex-vs-ip.js` widget's point); "barrier methods are obsolete vs. primal-dual" → same skeleton, different step coupling.
- **Widgets:** `barrier-method-path-tracer.js`, `newton-step-ipm.js`, `lp-simplex-vs-ip.js`.
- **Assessment targets:** current 5 problems (P15.1–P15.5) retained and re-keyed; build to 8 (2/4/2).
- **Mastery checklist:** □ barrier gradient/Hessian □ gap identity derivation □ central-path sketch for a 2-D LP □ $\mu$ trade-off explanation □ $-\log\det$ barrier statement.

---

## 5. Pacing Plans

| Plan | Schedule | Notes |
| :--- | :--- | :--- |
| **14-week semester** | Wk 1: L00–L01 · Wk 2: L02 · Wk 3: L03 · Wk 4: L04 · Wk 5: L05 · Wk 6: L06 · Wk 7: L07 + midterm checkpoint (mastery checklists L02–L06) · Wk 8: L08 · Wk 9–10: L09 (two weeks — keystone) · Wk 11: L10 + L11 · Wk 12: L12 + L13 · Wk 13: L14 + L15 · Wk 14: capstone presentations | Capstone assigned Wk 9, milestone M1 due Wk 11 |
| **6-week intensive** | Practitioner track (§2.2), one part per ~4 days; capstone option B or C only | Proof appendices deferred |
| **Reference mode** | Any order via cheat sheets + glossary; prerequisite edges (§1.1) warn what to backfill | The default for returning visitors |

---

## 6. Capstone Project Specification

> **Deliverable:** An end-to-end *"model → dualize → solve → diagnose"* case study,
> submitted as a self-contained lecture-style page (course shell, widgets/plots,
> full derivations) under a `topics/capstone-*/` directory.

### 6.1 The four steps (all options share them)

1. **Model** — formalize the chosen problem; prove convexity via the cheapest
   sufficient rules (L05–L06); place it in the hierarchy (L02/L07/L08).
2. **Dualize** — derive the dual and KKT conditions; interpret at least one
   dual variable in the problem's own domain language (L09).
3. **Solve** — two independent paths: (a) a reformulation to a standard class,
   and (b) a hand-rolled first-order or barrier method (L13–L15); verify both
   reach the same optimum with duality gap ≈ 0 (report the number).
4. **Diagnose** — perturb one datum; reconcile observed $\Delta p^\star$ with
   the shadow-price prediction to first order (L09 §6).

### 6.2 Project options (fully specified)

| Option | Problem | Model class | Dual payoff | Algorithm leg | Stretch goal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Robust portfolio** | Mean–variance with box + budget constraints and ellipsoidal return-uncertainty | QP → SOCP | Budget multiplier = price of capital; uncertainty multiplier = price of robustness | Projected/proximal gradient on the QP; barrier method on the SOCP | Pareto frontier sweep with warm starts |
| **B. TV image denoising** | $\min \tfrac12\|x - y\|_2^2 + \lambda \operatorname{TV}(x)$ on a 1-D/2-D grid | QP/SOCP | Dual is a box-constrained problem — derive it; dual variables = edge indicators | Chambolle-style dual ascent *or* subgradient method; compare | Staircasing study vs. $\lambda$ |
| **C. Optimal experiment design** | D-optimal allocation over candidate measurements | log-det SDP | Multipliers rank measurement informativeness; complementary slackness prunes | Projected gradient on the simplex; verify with KKT residuals | E-optimal variant, compare designs |
| **D. Min-fuel control** | $\min \sum_t \|u_t\|_1$ s.t. linear dynamics reach target | LP | Costate/adjoint interpretation of equality multipliers | Barrier method with the L15 schedule | Bang-bang structure analysis via LP basis |

### 6.3 Milestones

- **M1 (end of Wk 11):** model + convexity proof + hierarchy placement (steps 1) — written, reviewed against the rubric's first row.
- **M2 (end of Wk 12):** dual + KKT derivation (step 2).
- **M3 (end of Wk 13):** both solvers running with agreement + gap report (step 3).
- **Final (Wk 14):** full page incl. diagnosis (step 4) and presentation.

### 6.4 Evaluation matrix

| Criterion | Weight | "Excellent" looks like |
| :--- | ---: | :--- |
| Correct convex model & proof | 25% | Convexity argued by the cheapest sufficient rule; standard form stated precisely; hierarchy placement justified |
| Dual & KKT derivation | 25% | Every step explicit; multipliers interpreted in domain language; sign conventions per `docs/NOTATION.md` |
| Working solver + verification | 30% | Two independent paths agree to tolerance; duality gap and KKT residuals reported with assertions |
| Sensitivity analysis | 10% | Empirical $\Delta p^\star$ matches shadow-price prediction to first order, with the discrepancy discussed |
| Presentation quality | 10% | Meets all `CLAUDE.md` invariants: self-contained, scannable, zero handwaving |

---

## 7. Maintenance Roadmap (prioritized, audit-driven)

| ID | Item | Detail | Priority |
| :--- | :--- | :--- | :--- |
| R1 | **Build out the five THIN lectures** | L10, L11, L12, L14, L15 to the numbered-section standard per the §4 target structures; L13 promoted from Partial | **Highest** |
| R2 | **Repair `data/problems-index.json`** | Per-problem re-key (14 × `02-convex-sets`→`03-convex-sets-geometry`; `03-015`→`06-convex-functions-advanced`); index L15's in-page P15.1–P15.5; then populate per-lecture banks to the §4 targets (schema in `docs/ASSESSMENT.md` §5) | **Highest** |
| R3 | L06 widget identity | Replace the L05-duplicated widgets with dedicated conjugate-geometry and subgradient widgets (specs W2, W3 in `docs/WIDGETS.md` §6) | High |
| R4 | Algorithm-lecture widgets | Central-path dashboard (W1), conditioning arena (W4), KKT anatomy (W5) per `docs/WIDGETS.md` §6 | High |
| R5 | Glossary completion | Add the 11 missing load-bearing terms (§3 list) with definitions matching `docs/NOTATION.md` | High |
| R6 | Widget infrastructure debt | Resolve `widgets-loader.js` stub, theme-unify L09 iframes, de-duplicate overlapping widgets, add L13 headers (W-R1…W-R5 in `docs/WIDGETS.md` §5) | Medium |
| R7 | Capstone scaffold | `topics/capstone-template/` implementing §6 with a worked mini-example (small QP end-to-end) | Medium |
| R8 | Track surfacing | Syllabus page exposes the §2.2 tracks and the §1.1 edge table as "what to backfill" hints | Medium |
| R9 | Symbol table | Promote `docs/NOTATION.md` §2–4 core table into `data/glossary.json` so it surfaces on every page | Medium |
| R10 | Thread callouts | Add one-line "Thread" callouts (§1.2) at each thread touchpoint | Low |

Any PR that closes a roadmap item must update this table **and** re-verify the
§3 status audit row it changes.
