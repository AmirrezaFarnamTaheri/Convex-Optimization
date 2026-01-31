## Convex Optimization — Interactive Lecture Notes

This repository is a self-contained, **static** website for interactive convex optimization lecture notes and widgets.
It includes:
- Lecture pages under `topics/*/index.html`
- Interactive widgets under `topics/*/widgets/`
- Shared UI and theming under `static/`

### Disclaimer
These notes are **not official course materials** and may contain mistakes or omissions.
They are provided as a study aid.

---

## Course structure (high-level)

### Part I: Mathematical Foundations
* **Lecture 00: Linear Algebra Basics**
  * **Core Concepts**: Notation, Subspaces, and the Four Fundamental Spaces.
  * **Algebraic Invariants**: Determinant, Trace, and Eigenvalues (including spectral mapping).
  * **Geometry**: Inner Products, Norms, Angles, and Orthogonality.
  * **Matrices**: Positive Semidefinite (PSD) Matrices and their properties.
  * **Optimization Tools**: Projections onto Subspaces/Affine Sets and the Method of Least Squares.

* **Lecture 01: Linear Algebra Advanced**
  * **Factorizations**: The QR Decomposition and its applications.
  * **Spectral Theory**: The Singular Value Decomposition (SVD) and its geometric interpretation.
  * **Inversion**: The Moore-Penrose Pseudoinverse and Condition Number analysis.

### Part II: Introduction to Optimization
* **Lecture 02: Introduction to Convex Optimization**
  * **Definitions**: Formal definition of optimization problems and convexity.
  * **The Fundamental Theorem**: Proof that local optima are global in convex problems.
  * **Problem Families**: The hierarchy of convex problems (LP $\subset$ QP $\subset$ SOCP $\subset$ SDP).
  * **Modeling**: The "Loss + Regularizer" paradigm and Standard Form transformations.
  * **DCP**: Introduction to Disciplined Convex Programming rules.

### Part III: Convex Sets
* **Lecture 03: Convex Sets & Geometry**
  * **Basics**: Affine and Convex sets, hulls, and combinations.
  * **Canonical Sets**: Hyperplanes, Halfspaces, Polyhedra, and Norm Balls.
  * **Operations**: Intersection, Affine functions, Perspective functions, and Linear-Fractional transformations.
  * **Topology**: Interior, Closure, Relative Interior, and Boundary definitions.

* **Lecture 04: Cones & Separation Theorems**
  * **Theorems**: Separating and Supporting Hyperplane theorems.
  * **Conic Geometry**: Proper cones, Generalized Inequalities, and Dual Cones.
  * **Applications**: Theorems of Alternatives (Farkas' Lemma).

### Part IV: Convex Functions
* **Lecture 05: Convex Functions Basics**
  * **Definitions**: Convexity, Concavity, and Strict/Strong convexity.
  * **Characterizations**: Epigraphs, First-Order (Gradient), and Second-Order (Hessian) conditions.
  * **Operations**: Pointwise maximum, composition rules, and minimization.
  * **Examples**: Verification of convexity for common functions.

* **Lecture 06: Convex Functions Advanced**
  * **Conjugacy**: The Fenchel Conjugate and its geometric interpretation.
  * **Quasiconvexity**: Definitions, sublevel sets, and properties.
  * **Log-Concavity**: Log-concave and Log-convex functions, integration properties.

### Part V: Standard Problems & Duality
* **Lecture 07: Standard Convex Problems**
  * **Linear Programming (LP)**: Diet problem, Transportation, Chebyshev center.
  * **Quadratic Programming (QP)**: Portfolio optimization, LASSO, Support Vector Machines.
  * **Reformulations**: Converting piecewise linear and norm minimization problems to standard forms.

* **Lecture 08: Conic Optimization**
  * **SOCP**: Second-Order Cone Programming and Robust Least Squares.
  * **SDP**: Semidefinite Programming, Matrix Norm Minimization, and MAX-CUT relaxation.
  * **Quasiconvex Optimization**: Bisection methods for fractional programming.

* **Lecture 09: Duality Theory**
  * **The Lagrangian**: Primal and Dual variables, the Dual Function.
  * **The Dual Problem**: Weak and Strong Duality, Slater's Condition.
  * **Optimality**: KKT Conditions (Stationarity, Primal/Dual Feasibility, Complementary Slackness).
  * **Sensitivity**: Interpretation of dual variables as shadow prices.
  * **Generalized Inequalities**: Duality for conic problems (SOCP/SDP).

### Part VI: Applications & Algorithms
* **Lecture 10: Approximation & Fitting**
  * **Approximation**: Least Squares, weighted least squares, and matrix approximation.
  * **Regularization**: Ridge regression, LASSO (L1), and Elastic Net for preventing overfitting.
  * **Robustness**: Robust regression using Huber loss and L1-norm minimization.
  * **Applications**: Total variation denoising and basis pursuit for sparse signal recovery.

* **Lecture 11: Statistical Estimation & ML**
  * **Estimation**: Maximum Likelihood Estimation (MLE) and MAP estimation.
  * **Classification**: Logistic regression, Support Vector Machines (SVM), and margin maximization.
  * **Hypothesis Testing**: Neyman-Pearson lemma and minimax tests.
  * **Experiment Design**: Optimal experiment design (A-optimal, D-optimal, E-optimal).

* **Lecture 12: Geometric Problems**
  * **Centers**: Chebyshev center (largest inscribed ball) and Analytic center.
  * **Ellipsoids**: Minimum Volume Enclosing Ellipsoid (MVEE) and Maximum Volume Inscribed Ellipsoid.
  * **Classification**: Linear discrimination and separating hyperplanes.
  * **Placement**: Fermat-Weber problem and facility location.

* **Lecture 13: Unconstrained Minimization**
  * **Gradient Descent**: Algorithm, step size selection (backtracking, exact), and convergence analysis.
  * **Newton's Method**: Second-order information, quadratic convergence, and affine invariance.
  * **Quasi-Newton**: BFGS and L-BFGS methods for approximating the Hessian.
  * **Conditioning**: The impact of condition number on convergence rates.

* **Lecture 14: Equality-Constrained Minimization**
  * **KKT Systems**: Solving KKT systems via block elimination.
  * **Newton Methods**: Equality-constrained Newton's method with feasible start.
  * **Infeasible Start**: Newton's method with infeasible start (primal-dual updates).
  * **Elimination**: Reducing equality-constrained problems to unconstrained ones via null-space bases.

* **Lecture 15: Interior-Point Methods**
  * **Barrier Method**: Log-barrier functions, the Central Path, and the barrier parameter $t$.
  * **Algorithm**: Outer loop (centering step) vs. Inner loop (Newton step).
  * **Complexity**: Polynomial-time complexity ($O(\sqrt{m})$ iterations).
  * **Conic Extension**: Extension to generalized inequalities (SOCP, SDP barriers).

---

## Run locally

Browsers block module imports and some fetch calls when opening pages via `file://`.
Run a local server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Quality checks

Run the local reference checker (lectures + widgets):

```bash
python verify_site.py
```

## License / attribution

These notes are provided for personal study. Third‑party materials remain the property of their respective owners.
