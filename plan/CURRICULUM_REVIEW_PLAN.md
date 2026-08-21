# Master Curriculum Review & Architectural Compendium: The Ultimate 17-Dimensional Convex Optimization Blueprint

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute an exhaustive, grounded, multi-dimensional, deep audit and systematic refinement of all 16 lecture modules, mathematical proofs, algorithm implementations, D3/Three.js interactive widgets, Pyodide live in-browser solvers, and visual assets across the entire Convex Optimization curriculum.

**Architecture:** An all-encompassing 17-Dimensional Matrix Review Framework synthesizing automated AST static analysis, formal mathematical proof compendiums, numerical precision profiling, multi-engine solver benchmarks (NumPy/SciPy/CVXPY/OSQP/Clarabel/JAX), landmark real-world optimization applications (SVM, Portfolio, LASSO, MAX-CUT, MPC), Socratic misconception traps with 3-tier autograding, 300 DPI vector graphic generation, and D3.js/Three.js/Pyodide interactive simulation laboratories.

**Tech Stack:** Python 3.11+, HTML5/ES6, D3.js (v7), Three.js (r134+), Pyodide, KaTeX, CVXPY, SciPy, NumPy, Matplotlib, pytest, ruff.

---

## 0. The Execution Quality Standard: The 7 Pillars of Perfectionist Academic Rigor

> **CORE OPERATIONAL DIRECTIVE:** Every review, derivation, code modification, interactive widget, and pedagogical explanation must strictly adhere to the **7 Pillars of Perfectionist Academic Rigor**:

```
                       THE 7 PILLARS OF PERFECTIONIST RIGOR
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ 1. 📐 RIGOROUS       │ Formal mathematical theorem-proof chains with zero   │
   │                      │ missing algebraic intermediate steps. No hand-waving.│
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 2. 💎 PERFECTIONIST  │ Absolute zero tolerance for placeholders, stubs,     │
   │                      │ `TODO` markers, ellipses (`...`), or incomplete code.│
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 3. 🧱 CONCRETE       │ Exact executable Python/JS functions, explicit type  │
   │                      │ signatures, verified numerical tolerances (tol<=1e-8)│
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 4. 🛡️ SOLID          │ Defensively guarded against ill-conditioning (kappa  │
   │                      │ <= 1e8), singular Hessians, step-size line divergence│
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 5. 🌊 DEEP           │ Unpacks multi-step structural mechanisms, dual cone  │
   │                      │ geometry, KKT saddle points, and self-concordance.    │
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 6. 🔍 DETAILED       │ Granular step-by-step algorithms, memory strides,    │
   │                      │ line search bounds, and complete parameter domains.  │
   ├──────────────────────┼──────────────────────────────────────────────────────┤
   │ 7. ⚓ GROUNDED        │ Anchored in Boyd-Vandenberghe, Nesterov, Rockafellar, │
   │                      │ and real industrial applications (MPC, LASSO, SVM).  │
   └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. The 17 Analytical Dimensions (The Complete Optimization Matrix)

Every lecture topic, code block, mathematical proof, exercise, and visual asset is evaluated across **17 orthogonal analytical lenses**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 THE 17-DIMENSIONAL CONVEX OPTIMIZATION MATRIX                                    │
├──────────────────────────────────────┬───────────────────────────────────────────────────────────────────────────┤
│ 1. Mathematical Rigor & Proofs       │ Formal theorem statements, lemma chains, boundary regularity, parameter   │
│                                      │ domains, step-by-step derivations, no missing algebraic intermediate steps│
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 2. Computational Soundness           │ Matrix conditioning $\kappa(A)$, floating-point precision, numerical      │
│                                      │ stability, asymptotic complexity $O(N)$, cancellation error prevention    │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 3. Code Standards & Architecture     │ Strict PEP 8/257/484 typing, production docstrings, DRY, modular design,  │
│                                      │ defensive assertion guards, zero dead code, zero placeholder stubs       │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 4. Pedagogical Flow & Scaffolding    │ 4-Stage Arc (Intuition $\to$ Math $\to$ Code $\to$ Engineering Insight),  │
│                                      │ cognitive load balance, active learning hooks, concept discovery          │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 5. Visual & LaTeX Precision          │ 300 DPI vector figures, academic color tokens, KaTeX math text in labels, │
│                                      │ pure Python/D3 DAG flowcharts, Three.js 3D epigraph manifolds            │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 6. Empirical & Applied Integrity     │ Real-world benchmarks (Markowitz, SVM, LASSO, Total Variation, MAX-CUT), │
│                                      │ lookahead-free pipelines, automated fallback solvers                      │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 7. Exercises & Problem Sets          │ 3-Tier Difficulty (Warmup $\to$ Application $\to$ Challenge), self-testing│
│                                      │ assertion blocks, complete analytical & computational reference solutions │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 8. Epistemological Grounding         │ Historical context, foundational citations (Boyd, Nesterov, Rockafellar,  │
│                                      │ Nemirovski, Dantzig, Karush-Kuhn-Tucker), paradigm evolutions             │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 9. Anti-Slop & Human Voice           │ Elimination of generic LLM throat-clearing, peer-level academic tone,    │
│                                      │ crisp authoritative explanations, zero condescending or passive padding  │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 10. Robustness & Error Defense       │ Graceful failure handling, non-invertibility warnings, singular Hessian   │
│                                      │ guards, backtracking line search safeguards                              │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 11. Reproducibility & Environment    │ Fixed random seeds (`np.random.default_rng(42)`), Python 3.11+ / Pyodide, │
│                                      │ zero unpinned external C-dependencies                                     │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 12. Cross-Linking & Navigation       │ Interactive sidebar navigation, relative link validity (`verify_site.py`),│
│                                      │ anchor linking between primal theory, dual math, and interactive widgets  │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 13. Modernity & State-of-the-Art     │ Modern 2026 optimization tools: ADMM, Proximal Algorithms, Clarabel,     │
│                                      │ JAX automatic differentiation, Conformal Optimization, Semidefinite Relax │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 14. Algorithmic Vectorization        │ Vectorized NumPy broadcasting over explicit loops, block elimination for  │
│                                      │ KKT systems, sparse matrix representations (`scipy.sparse.csc_matrix`)    │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 15. Geometric & Duality Intuition    │ Explicit geometric interpretations of supporting hyperplanes, epigraphs,  │
│                                      │ dual cones, subgradients, and Lagrange multiplier shadow prices           │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 16. Interactive 3D & D3/Pyodide Lab  │ Real-time D3 hyperplane dragging, Three.js 3D epigraph rendering,         │
│                                      │ in-browser Pyodide CVXPY solver execution with live iteration logs        │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ 17. Frontend Design & Hallmark De-Slop│ Strict `DESIGN.md` token system (OKLCH 60-30-10), 8-state component       │
│                                      │ matrix, typography purity (no italic headers), 320px mobile-tested layout │
└──────────────────────────────────────┴───────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Granular Lecture-by-Lecture Audit Specifications (All 16 Lectures)

| # | Lecture Directory | Primary Theoretical & Geometric Focus | Mandatory Code, Proof & Interactive Deliverables |
| :-: | :--- | :--- | :--- |
| **00** | `topics/00-linear-algebra-basics` | Four fundamental subspaces, SVD geometry, PSD matrices, least squares | Orthogonal projection proofs, Gram-Schmidt algebra, D3 fundamental subspaces visualizer, least squares normal equations $A^T A x = A^T b$. |
| **01** | `topics/01-linear-algebra-advanced` | QR factorization, SVD spectral decomposition, Moore-Penrose pseudoinverse | Eckart-Young-Mirsky low-rank theorem proof, condition number $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ bounds, 3D ellipse transformation interactive widget. |
| **02** | `topics/02-introduction` | Formal convex problem definition, local vs global optimality, DCP rules | Formal proof that local optima are global in convex optimization; hierarchy LP $\subset$ QP $\subset$ SOCP $\subset$ SDP; Pyodide CVXPY DCP validation. |
| **03** | `topics/03-convex-sets-geometry` | Hyperplanes, halfspaces, polyhedra, norm balls, perspective functions | Proof of convexity preservation under affine and perspective mappings; D3 convex hull & Minkowski sum interactive manipulator. |
| **04** | `topics/04-convex-sets-cones` | Proper cones, generalized inequalities, dual cones, Farkas' lemma | Separating & Supporting Hyperplane Theorem proofs; dual cone calculus ($K^*$ for Lorentz and PSD cones); Theorems of Alternatives. |
| **05** | `topics/05-convex-functions-basics` | Epigraphs, 1st-order gradient condition, 2nd-order Hessian PSD condition | Proof of 1st-order characterization $f(y) \ge f(x) + \nabla f(x)^T(y-x)$; 2nd-order $\nabla^2 f(x) \succeq 0$; Three.js 3D epigraph visualization. |
| **06** | `topics/06-convex-functions-advanced` | Fenchel conjugate, quasiconvexity, log-concavity, sublevel sets | Fenchel-Moreau biconjugate theorem $f^{**} = f$; Legendre transform derivations for entropy, quadratic, and exponential functions; D3 conjugate slider. |
| **07** | `topics/07-convex-problems-standard` | Linear Programming (LP), Quadratic Programming (QP), QCQP | Simplex vs Interior-point geometry; converting piecewise linear and $L_1$/$L_\infty$ norm problems into LP standard form; Portfolio mean-variance QP. |
| **08** | `topics/08-convex-problems-conic` | Second-Order Cone Programming (SOCP), Semidefinite Programming (SDP) | Robust least squares as SOCP; Schur complement theorem proof; MAX-CUT Goemans-Williamson 0.878 SDP relaxation; Matrix completion SDP. |
| **09** | `topics/09-duality` | Lagrangian duality, weak/strong duality, Slater's condition, KKT | Proof of Strong Duality under Slater's constraint qualification; complete KKT derivation; shadow price sensitivity $\lambda_i^* = -\frac{\partial p^*}{\partial u_i}$; D3 dual bound widget. |
| **10** | `topics/10-approximation-fitting` | Least squares, LASSO ($L_1$), Ridge ($L_2$), Huber loss, Total Variation | Soft-thresholding closed-form coordinate descent derivation; Huber robust regression; 1D/2D Total Variation signal denoising via Pyodide. |
| **11** | `topics/11-statistical-estimation` | Maximum Likelihood (MLE), MAP estimation, SVM margin maximization | Logistic regression log-concavity proof; Hard & Soft-margin SVM dual derivations; A/D/E-optimal experiment design SDPs. |
| **12** | `topics/12-geometric-problems` | Chebyshev center, Minimum Volume Enclosing Ellipsoid (MVEE/Löwner-John) | Löwner-John ellipsoid SDP derivation; analytic center cutting-plane geometry; Fermat-Weber spatial facility location. |
| **13** | `topics/13-unconstrained-minimization` | Gradient descent, Backtracking line search, Newton's method, BFGS | Proof of quadratic convergence for Newton's method $\|x_{k+1} - x^*\| \le \frac{L}{2 m^2} \|x_k - x^*\|^2$; Armijo condition; L-BFGS two-loop recursion. |
| **14** | `topics/14-equality-constrained-minimization` | KKT systems, block elimination, feasible vs infeasible start Newton | Block elimination Schur complement solver; primal-dual Newton step derivations; null-space basis reduction. |
| **15** | `topics/15-interior-point-methods` | Log-barrier functions, Central Path, Newton centering step, complexity | Proof of self-concordance for $-\sum \ln(-f_i(x))$; polynomial iteration bound $O(\sqrt{m} \ln(m/(\epsilon t_0)))$; primal-dual interior-point path following. |

---

## 3. The 35 Core Mathematical Proofs to Audit & Formalize

Every proof must follow strict **Assumption $\to$ Lemma Chain $\to$ Main Theorem $\to$ Step-by-Step Derivation $\to$ Geometric/Economic Interpretation** formatting:

1. **Fundamental Theorem of Convex Optimization**: Proof that any local minimum of a convex function over a convex set is a global minimum, and the solution set is convex.
2. **Strict Convexity & Uniqueness**: Proof that strictly convex objective functions have at most one global minimizer.
3. **First-Order Convexity Condition**: Proof that a differentiable function $f$ is convex if and only if $\text{dom } f$ is convex and $f(y) \ge f(x) + \nabla f(x)^T(y-x), \forall x, y \in \text{dom } f$.
4. **Second-Order Convexity Condition**: Proof that a twice-differentiable function $f$ is convex if and only if $\nabla^2 f(x) \succeq 0, \forall x \in \text{dom } f$.
5. **Epigraph Convexity Equivalence**: Proof that a function $f$ is convex if and only if its epigraph $\text{epi } f = \{(x, t) \mid x \in \text{dom } f, f(x) \le t\}$ is a convex set.
6. **Strict Separating Hyperplane Theorem**: Proof that for two disjoint non-empty convex sets $C$ and $D$ where $C$ is compact and $D$ is closed, there exists a hyperplane that strictly separates them.
7. **Supporting Hyperplane Theorem**: Proof that for any non-empty convex set $C$ and any boundary point $x_0 \in \text{bd } C$, there exists a non-zero vector $a$ such that $a^T x \le a^T x_0, \forall x \in C$.
8. **Farkas' Lemma (Theorem of Alternatives)**: Proof that exactly one of the systems $\{A x \le 0, c^T x > 0\}$ or $\{A^T y = c, y \ge 0\}$ has a solution.
9. **Dual Cone Properties**: Proof that for any cone $K$, its dual $K^* = \{y \mid x^T y \ge 0, \forall x \in K\}$ is always closed and convex, and $K^{**} = \text{cl}(\text{conv}(K))$.
10. **Lorentz (Second-Order) Self-Duality**: Proof that the Second-Order Cone $\mathcal{K}_{\text{SOC}} = \{(x, t) \mid \|x\|_2 \le t\}$ is self-dual ($\mathcal{K}_{\text{SOC}}^* = \mathcal{K}_{\text{SOC}}$).
11. **Positive Semidefinite Cone Self-Duality**: Proof that the PSD matrix cone $\mathbb{S}_+^n$ is self-dual under the Frobenius trace inner product $\langle X, Y \rangle = \text{tr}(X Y)$.
12. **Fenchel-Young Inequality**: Proof that for any function $f$ and its conjugate $f^*(y) = \sup_x (y^T x - f(x))$, $f(x) + f^*(y) \ge x^T y$, with equality if and only if $y \in \partial f(x)$.
13. **Fenchel-Moreau Biconjugation Theorem**: Proof that $f^{**} = f$ if and only if $f$ is proper, convex, and lower semicontinuous.
14. **Schur Complement Convexity & PSD Lemma**: Proof that $M = \begin{pmatrix} A & B \\ B^T & C \end{pmatrix} \succ 0 \iff A \succ 0 \text{ and } C - B^T A^{-1} B \succ 0$.
15. **Weak Duality Theorem**: Proof that for any optimization problem, $d^* \le p^*$, and the duality gap satisfies $p^* - d^* \ge 0$.
16. **Slater's Condition & Strong Duality**: Formal proof that strict feasibility ($f_i(x) < 0$ for all non-affine constraints) implies zero duality gap ($p^* = d^*$) and dual attainment.
17. **Karush-Kuhn-Tucker (KKT) Necessary & Sufficient Conditions**: Proof that under strong duality, $(x^*, \lambda^*, \nu^*)$ are optimal if and only if they satisfy Stationarity, Primal Feasibility, Dual Feasibility, and Complementary Slackness.
18. **Saddle-Point Equivalence Theorem**: Proof that $(x^*, \lambda^*, \nu^*)$ is a saddle point of the Lagrangian $L(x, \lambda, \nu)$ if and only if $x^*$ is primal optimal, $(\lambda^*, \nu^*)$ is dual optimal, and strong duality holds.
19. **Dual Sensitivity & Shadow Price Interpretation**: Analytical proof that $\lambda_i^* = -\frac{\partial p^*(u, v)}{\partial u_i}$ where $p^*(u, v)$ is the perturbed optimal value function.
20. **Minimax Theorem (von Neumann)**: Proof of $\min_{x \in X} \max_{y \in Y} x^T A y = \max_{y \in Y} \min_{x \in X} x^T A y$ for probability simplexes $X, Y$.
21. **Lasso Soft-Thresholding Closed-Form Solution**: Derivation of $\arg\min_x \frac{1}{2}(x - y)^2 + \lambda |x| = \text{sign}(y) \max(0, |y| - \lambda)$.
22. **Goemans-Williamson MAX-CUT SDP Approximation Bound**: Formal proof that the SDP relaxation achieves an approximation ratio $\alpha \ge \frac{2}{\pi} \min_{0 \le \theta \le \pi} \frac{\theta}{1 - \cos\theta} \approx 0.87856$.
23. **Chebyshev Center Convex Formulation**: Proof that finding the largest inscribed Euclidean ball in a polyhedron $\{x \mid a_i^T x \le b_i\}$ is an exact Linear Program.
24. **Löwner-John Ellipsoid Existence & Uniqueness**: Proof of the unique minimum volume enclosing ellipsoid for any compact set with non-empty interior.
25. **Gradient Descent Convergence Rate on Strongly Convex Functions**: Proof of linear convergence $\|x_k - x^*\|_2 \le c^k \|x_0 - x^*\|_2$ with contraction factor $c = 1 - \frac{m}{M}$.
26. **Backtracking Line Search Termination & Armijo Bounds**: Proof that the backtracking line search terminates in a finite number of steps with step size $t \ge \min(1, \frac{2 \beta (1-\alpha)}{M})$.
27. **Newton's Method Affine Invariance**: Proof that the Newton step $\Delta x_{\text{nt}} = -(\nabla^2 f(x))^{-1} \nabla f(x)$ is invariant under any non-singular affine coordinate change $x = T y$.
28. **Newton's Method Quadratic Convergence**: Proof that in the quadratic convergence phase, $\frac{L}{2 m^2} \|\nabla f(x_{k+1})\|_2 \le \left(\frac{L}{2 m^2} \|\nabla f(x_k)\|_2\right)^2$.
29. **Self-Concordance & Hessian Metric Invariance**: Proof that self-concordant functions satisfy $|f'''(x)| \le 2 f''(x)^{3/2}$ and exhibit parameter-free polynomial convergence under Newton's method.
30. **Logarithmic Barrier Central Path Convergence**: Proof that the central path solution $x^*(t)$ satisfies $f_0(x^*(t)) - p^* \le \frac{m}{t}$, yielding an exact $\epsilon$-suboptimality for $t = m/\epsilon$.
31. **Primal-Dual Newton Step Block Elimination Algebra**: Complete algebraic derivation of the reduced KKT system via Schur complement reduction.
32. **Subgradient Method Convergence Rate**: Proof that the subgradient method with constant step size satisfies $f_{\text{best}}^{(k)} - f^* \le \frac{R^2 + G^2 \sum \alpha_i^2}{2 \sum \alpha_i} = O(1/\sqrt{k})$.
33. **Proximal Gradient Method (ISTA) $O(1/k)$ Convergence**: Proof of $O(1/k)$ objective error rate for composite optimization $f(x) + g(x)$ where $\nabla f$ is Lipschitz.
34. **Nesterov Accelerated Gradient Method (FISTA) $O(1/k^2)$ Bound**: Proof of optimal $O(1/k^2)$ first-order convergence via momentum extrapolation.
35. **Alternating Direction Method of Multipliers (ADMM) Global Convergence**: Proof of residual convergence $r^k \to 0$, objective convergence $f(x^k) + g(z^k) \to p^*$, and dual variable convergence under convex separable structures.

---

## 4. Multi-Engine Computational Tournament

Every core optimization algorithm is benchmarked across **6 industry-standard backends**:

```
                       MULTI-ENGINE OPTIMIZATION TOURNAMENT
   ┌───────────────────────┬───────────────────────────────────────────────────────────┐
   │ Solver / Backend      │ Application Scope & Target Benchmark                      │
   ├───────────────────────┼───────────────────────────────────────────────────────────┤
   │ 1. NumPy / SciPy      │ Native baseline routines (`scipy.optimize.minimize`)      │
   │ 2. CVXPY (Python)     │ Disciplined Convex Programming (DCP) modeling & parsing   │
   │ 3. OSQP / Clarabel    │ High-performance C-accelerated QP and Conic solvers       │
   │ 4. MOSEK (Conic/SDP)  │ Commercial gold-standard interior-point conic solver      │
   │ 5. JAX Opt / Autodiff │ GPU-accelerated gradient descent & unconstrained Newton   │
   │ 6. Pyodide (Browser)  │ Client-side WASM execution in the interactive web portal  │
   └───────────────────────┴───────────────────────────────────────────────────────────┘
```

- **Condition Number Bounds**: Enforce $\kappa(\nabla^2 f(x)) \le 10^8$; automatically apply diagonal or incomplete Cholesky preconditioning for large sparse KKT systems.
- **DCP Verification Test Suite**: Automated unit tests checking positive semi-definiteness of user Hessians and verifying DCP curvature rules (convex $\times$ positive constant, composition monotonicity).

---

## 5. Landmark Applied Optimization Case Studies

1. **Markowitz Mean-Variance Portfolio Selection with Cardinality & Sector Bounds**:
   - Formulation as QP/SOCP; tracking error bounds; frontier generation with transaction costs.
2. **Support Vector Machines (SVM) & Kernel Margin Maximization**:
   - Primal QP vs Dual QP; kernel trick substitution; support vector extraction via complementary slackness.
3. **Sparse Signal Recovery & Total Variation Denoising**:
   - $L_1$ Basis Pursuit Dequantization; 1D and 2D image total variation regularized reconstruction.
4. **MAX-CUT Semidefinite Relaxation (Goemans-Williamson)**:
   - Random hyperplane rounding; verifying the 0.878 approximation guarantee empirically over 100 random graphs.
5. **Model Predictive Control (MPC) & Real-Time Trajectory Optimization**:
   - Receding horizon optimal control solved as a multi-stage quadratic program with state and input constraints.

---

## 6. Pedagogical Scaffolding, Socratic Traps & 3-Tier Autograding

- **Common Misconceptions & Diagnostic Traps**:
  - Confusing non-convex sets with non-convex functions.
  - Assuming strong duality always holds without checking Slater's condition.
  - Ignoring condition numbers and wondering why gradient descent zig-zags on ill-conditioned quadratics.
  - Misapplying DCP rules (e.g. attempting to minimize $\sqrt{x^2 + 1}$ without reformulating as norm).
- **3-Tier Interactive Problem Sets**:
  - **Tier 1 (Warmup)**: Analytical derivative / dual problem derivation.
  - **Tier 2 (Application)**: Formulating an engineering/data problem in CVXPY and solving with OSQP/Clarabel.
  - **Tier 3 (Challenge / Research Extension)**: Implementing a custom custom primal-dual interior-point solver from scratch and matching commercial convergence logs.
- **In-Browser Pyodide Autograders**: Python assertion blocks in widget cells giving instant diagnostic feedback.

---

## 7. Interactive D3.js, Three.js & Pyodide Laboratory

- **D3.js 2D Geometry**:
  - Interactive hyperplane draggers showing separating vs supporting hyperplanes in real time.
  - Dynamic 2D subgradient bundles at non-differentiable points (e.g. $|x_1| + |x_2|$).
- **Three.js 3D Geometric Manifolds**:
  - 3D epigraph rendering for convex ($x^2 + y^2$), non-convex (saddle/Rosenbrock), and quasiconvex functions.
  - 3D Second-Order (Lorentz) cone and PSD matrix cone slices ($\mathbb{S}_+^2$).
- **Pyodide In-Browser Optimization Console**:
  - Live execution of CVXPY scripts directly inside the browser with zero server roundtrips.

---

## 8. Frontend Design System & Hallmark Anti-Slop Discipline (`DESIGN.md`)

- **Aesthetic Direction**: *Geometric Precision & Rigorous Convex Analysis* in OKLCH.
- **Typography Purity**: Roman display headers (`font-style: normal`). Zero italic emphasis in headings.
- **8-State Interactive Matrix**: Every slider, button, and input in D3/Three.js widgets implements all 8 states (`default`, `hover`, `focus-visible`, `active`, `disabled`, `loading`, `error`, `success`).
- **Responsive Mobile Viewports**: Non-negotiable `overflow-x: clip` tested at 320px, 375px, 414px, 768px.
- **Hallmark Pre-Emit Critique Stamp**: Stamped on every visual layout:
  `/* Hallmark · pre-emit critique: Philosophy:5 Hierarchy:5 Execution:5 Specificity:5 Restraint:5 Variety:5 */`

---

## 9. Comprehensive Module Enrichment, Gap-Filling & Redundancy Consolidation

- **Dual-Action Consolidation**:
  - DRY Code: Centralize shared D3/Three.js setup and KaTeX renderers into `static/js/shared/`.
  - Harmonized Variable Notation: Objective $f_0(x)$, inequality constraints $f_i(x) \le 0$, equality constraints $A x = b$, dual multipliers $\lambda_i \ge 0, \nu_j \in \mathbb{R}$, optimal values $p^*, d^*$.
  - Prerequisite Cross-Linking: Replace repetitive linear algebra recaps with direct links to `topics/00-linear-algebra-basics` and `topics/01-linear-algebra-advanced`.

---

## 10. Multi-Scale Curriculum Enrichment: 8 New Advanced Frontier Lectures

| Module / Topic | New Lecture Proposal | Theoretical & Computational Scope |
| :--- | :--- | :--- |
| **Topic 16** | `topics/16-subgradient-methods` | Subgradients, subdifferential calculus, subgradient method convergence $O(1/\sqrt{k})$, Polyak step size. |
| **Topic 17** | `topics/17-proximal-algorithms-admm` | Proximal operators, Moreau envelope, ISTA/FISTA, ADMM consensus and sharing problems. |
| **Topic 18** | `topics/18-coordinate-and-frank-wolfe` | Block coordinate descent, Frank-Wolfe (conditional gradient) algorithm, projection-free optimization. |
| **Topic 19** | `topics/19-nonconvex-relaxations` | Convex envelopes, rank minimization nuclear norm heuristics, Boolean LP relaxation, PhaseLift. |
| **Topic 20** | `topics/20-conic-duality-advanced` | Copositive programming, Sum-of-Squares (SOS) polynomials, Lasserre/Parrilo moment hierarchies. |
| **Topic 21** | `topics/21-stochastic-and-online-opt` | Stochastic Gradient Descent (SGD), mini-batching, AdaGrad, Adam, Online Convex Optimization (OCO) regret bounds. |
| **Topic 22** | `topics/22-distributed-large-scale-opt` | Dual decomposition, distributed ADMM over communication graphs, gossip algorithms. |
| **Topic 23** | `topics/23-model-predictive-control` | Dynamic systems, quadratic optimal control, state/input constraints, real-time QP solvers (OSQP). |

---

## 11. Deep-Dive Gap Inventory (24 Advanced Topics)

```
                 THE DEEP-DIVE GAP INVENTORY (24 ADVANCED TOPICS)
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ 🏛️ SECTION 1: CONIC GEOMETRY & POLYNOMIAL OPTIMIZATION                      │
   │ 1. Copositive and Completely Positive Cone Geometry & NP-hard Formulations │
   │ 2. Sum-of-Squares (SOS) Polynomials and Positivstellensatz Certificates     │
   │ 3. Lasserre Semidefinite Hierarchy for Polynomial Optimization             │
   │ 4. Polar Cones and Bipolar Theorem ($K^{**} = \text{cl}(\text{conv}(K))$)  │
   │ 5. Generalized Inequalities with Non-Solid and Non-Proper Cones            │
   │ 6. Nuclear Norm & Matrix Completion Exact Recovery Bounds (Candès-Recht)    │
   ├─────────────────────────────────────────────────────────────────────────────┤
   │ ⚡ SECTION 2: FIRST-ORDER & PROXIMAL ALGORITHMIC FRONTIERS                  │
   │ 7. Moreau Envelope and Proximal Operator Regularization Calculus            │
   │ 8. Douglas-Rachford Operator Splitting & Monotone Operator Resolvents       │
   │ 9. Chambolle-Pock Primal-Dual Algorithm for Saddle Point Problems           │
   │ 10. Frank-Wolfe / Conditional Gradient $O(1/k)$ Projection-Free Bounds       │
   │ 11. Nesterov Acceleration Momentum Mechanics & Continuous ODE Limit         │
   │ 12. Mirror Descent & Bregman Divergence Distance Generating Functions      │
   ├─────────────────────────────────────────────────────────────────────────────┤
   │ 🎯 SECTION 3: SECOND-ORDER & INTERIOR-POINT MECHANICS                       │
   │ 13. Self-Concordant Barriers for Conic Programming (Lorentz & PSD Cones)   │
   │ 14. Mehrotra Predictor-Corrector Infeasible Primal-Dual Interior-Point Path│
   │ 15. Quasi-Newton BFGS / DFP Secant Equation & Positive Definiteness Update │
   │ 16. Incomplete Cholesky & Conjugate Gradient Preconditioning for KKT       │
   │ 17. Null-Space vs Range-Space Methods for Large-Scale Equality Constraints │
   │ 18. Homogeneous Self-Dual Embedding for LP/Conic Solvers                    │
   ├─────────────────────────────────────────────────────────────────────────────┤
   │ 📈 SECTION 4: APPLIED HIGH-DIMENSIONAL & DISTRIBUTED OPTIMIZATION           │
   │ 19. Distributed Consensus ADMM over Graph Networks with Packet Loss        │
   │ 20. Online Convex Optimization (OCO) with $O(\sqrt{T})$ Regret Bounds      │
   │ 21. Robust Optimization with Ellipsoidal & Polyhedral Uncertainty Sets     │
   │ 22. Sensor Network Localization via Non-Convex Distance SDP Relaxation     │
   │ 23. Optimal Experiment Design (A-, D-, E-optimality) Matrix Convexity      │
   │ 24. Exact Penalty Functions & Augmented Lagrangian Method of Multipliers   │
   └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 12. Master Implementation & Actionable Task Breakdown

### Phase 1: Static Quality Verification & Site Health
- [ ] **Task 1.1: Run Local Link & Reference Verification (`verify_site.py`)**
  - Verify all 31 HTML pages, D3 scripts, KaTeX formulas, and assets resolve with zero broken local refs.
- [ ] **Task 1.2: Audit KaTeX LaTeX Formula Rendering**
  - Ensure all math environments use strict `$...$` and `$$...$$` with correct macro definitions.

### Phase 2: Mathematical Proof Formalization (All 35 Theorems)
- [ ] **Task 2.1: Audit & Complete Foundations & Set Proofs** (Theorems 1–11).
- [ ] **Task 2.2: Audit & Complete Duality & KKT Proofs** (Theorems 12–20).
- [ ] **Task 2.3: Audit & Complete Algorithmic Convergence Proofs** (Theorems 21–35).

### Phase 3: Interactive D3, Three.js & Pyodide Widgets
- [ ] **Task 3.1: Upgrade D3.js 2D Geometry Manipulators with Hallmark 8-State Controls**.
- [ ] **Task 3.2: Verify Three.js 3D Epigraph and Cone Visualizers at 60 FPS**.
- [ ] **Task 3.3: Verify Pyodide CVXPY Solvers Execute with Live Step Logs**.

### Phase 4: Applied Case Studies & Autograding Exercises
- [ ] **Task 4.1: Construct 3-Tier Problem Sets for Topics 00 through 15**.
- [ ] **Task 4.2: Build Self-Contained Unit Test Assertions for Solutions**.

### Phase 5: Design System & Mobile Responsiveness
- [ ] **Task 5.1: Verify `DESIGN.md` OKLCH Tokens Across `static/css/`**.
- [ ] **Task 5.2: Verify Mobile Viewports at 320px, 375px, 414px, and 768px**.

---

## 13. Verification Checkpoints & Definition of Done

```
[ ] Checkpoint 1 (Site Health): `python verify_site.py` passes with 0 broken refs across all 31+ pages.
[ ] Checkpoint 2 (Proof Completeness): All 35 core optimization theorems fully stated with step-by-step proofs.
[ ] Checkpoint 3 (Interactive Lab): All D3/Three.js widgets render smoothly; Pyodide CVXPY runs without errors.
[ ] Checkpoint 4 (Design & Anti-Slop): `DESIGN.md` tokens enforced; Hallmark pre-emit score >= 4/5 on all axes.
[ ] Checkpoint 5 (Clean Archive & Git): Clean repository tree pushed to origin/main; valid ZIP archive generated.
```
