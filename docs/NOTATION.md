# NOTATION.md — Course-Wide Symbol Standard

Normative for all lectures, widgets, problems, and solutions. Conventions
follow Boyd & Vandenberghe (*Convex Optimization*) unless noted. A lecture may
not deviate even when a cited source does — add a conversion remark instead
(`docs/PEDAGOGY.md` §6).

---

## 1. Spaces, Sets, and Linear Algebra

| Symbol | Definition | Plain English |
| :--- | :--- | :--- |
| $\mathbb{R}^n$, $\mathbb{R}^{m\times n}$ | real $n$-vectors / $m\times n$ matrices | vectors are **columns** |
| $\mathbb{R}_+$, $\mathbb{R}_{++}$ | $\{x \ge 0\}$, $\{x > 0\}$ | nonnegative / positive reals |
| $\mathbb{S}^n$, $\mathbb{S}^n_+$, $\mathbb{S}^n_{++}$ | symmetric / PSD / PD $n\times n$ matrices | the matrix habitats of the course |
| $A^\top$, $A^{-1}$, $A^\dagger$ | transpose, inverse, Moore–Penrose pseudoinverse | $A^\dagger$ via SVD (L01) |
| $\mathcal{R}(A)$, $\mathcal{N}(A)$ | range (column space), null space | two of the four fundamental subspaces (L00) |
| $\operatorname{rank} A$, $\operatorname{tr} A$, $\det A$ | rank, trace, determinant | |
| $\lambda_i(A)$, $\sigma_i(A)$ | eigenvalues, singular values, **sorted descending**: $\lambda_1 \ge \cdots \ge \lambda_n$ | $\lambda_{\max}, \lambda_{\min}$ for extremes |
| $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ | condition number | the conditioning thread's protagonist |
| $\langle x, y\rangle = x^\top y$ | Euclidean inner product; on matrices $\langle X, Y\rangle = \operatorname{tr}(X^\top Y)$ | |
| $\|x\|$, $\|x\|_1$, $\|x\|_\infty$, $\|x\|_p$ | **unsubscripted $\|\cdot\|$ means $\ell_2$** | subscript everything else |
| $\|A\|_2$, $\|A\|_F$, $\|A\|_*$ | spectral, Frobenius, nuclear norm | $\|A\|_2 = \sigma_{\max}(A)$ |
| $I$, $\mathbf 1$, $e_i$ | identity, all-ones vector, $i$-th standard basis vector | |
| $A \succeq 0$, $A \succ 0$ | PSD / PD (for $A \in \mathbb{S}^n$) | also the partial order $A \succeq B \iff A - B \succeq 0$ |

## 2. Convex Sets and Geometry

| Symbol | Definition | Notes |
| :--- | :--- | :--- |
| $\operatorname{\mathbf{aff}} C$, $\operatorname{\mathbf{conv}} C$, $\operatorname{\mathbf{cone}} C$ | affine / convex / conic hull | |
| $\operatorname{\mathbf{int}} C$, $\operatorname{\mathbf{relint}} C$, $\operatorname{\mathbf{cl}} C$, $\operatorname{\mathbf{bd}} C$ | interior, relative interior, closure, boundary | rel-int is the Slater-relevant one (L03 §5) |
| $\mathcal{B}(x_c, r)$ | Euclidean ball, center $x_c$, radius $r$ | |
| $\mathcal{E} = \{x_c + Au : \|u\| \le 1\}$ | ellipsoid | alternative form $\{x : (x - x_c)^\top P^{-1}(x-x_c) \le 1\}$, $P \succ 0$ |
| $\mathcal{P} = \{x : Ax \preceq b\}$ | polyhedron | $\preceq$ componentwise here |
| $\mathcal{Q}^n = \{(x,t) : \|x\| \le t\}$ | second-order (Lorentz/ice-cream) cone | self-dual |
| $K$, $K^*$ | proper cone, dual cone $K^* = \{y : \langle x,y\rangle \ge 0 \ \forall x \in K\}$ | |
| $x \preceq_K y$ | generalized inequality: $y - x \in K$ | plain $\preceq$ = componentwise ($K = \mathbb{R}^n_+$); on $\mathbb{S}^n$, $\succeq$ = PSD order |
| $P_C(x)$ | projection of $x$ onto closed convex $C$ | |
| $\operatorname{dist}(x, C)$ | $\inf_{y \in C}\|x - y\|$ | |
| $I_C(x)$ | indicator: $0$ on $C$, $+\infty$ off | the bridge from constraints to objectives (L15 §1) |

## 3. Convex Functions

| Symbol | Definition | Notes |
| :--- | :--- | :--- |
| $\operatorname{\mathbf{dom}} f$ | $\{x : f(x) < \infty\}$ | extended-value convention: $f : \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ |
| $\operatorname{\mathbf{epi}} f$ | $\{(x,t) : f(x) \le t\}$ | function convex $\iff$ epigraph convex |
| $S_\alpha = \{x : f(x) \le \alpha\}$ | $\alpha$-sublevel set | quasiconvexity's home |
| $\nabla f(x)$ | gradient, a **column vector** | see §5 layout convention |
| $\nabla^2 f(x)$ | Hessian, in $\mathbb{S}^n$ where twice differentiable | |
| $\partial f(x)$ | subdifferential: $\{g : f(y) \ge f(x) + g^\top(y - x)\ \forall y\}$ | a set; elements are subgradients (L06 §1) |
| $m$, $L$ | strong-convexity and smoothness constants: $mI \preceq \nabla^2 f \preceq LI$ | $\kappa = L/m$ (function condition number, L13) |
| $f^*(y) = \sup_x\,(y^\top x - f(x))$ | Fenchel conjugate | Fenchel–Young: $f(x) + f^*(y) \ge x^\top y$ |
| $\operatorname{lse}(x) = \log \sum_i e^{x_i}$ | log-sum-exp | the smooth max |

## 4. Optimization Problems and Duality (sign conventions — normative)

**The standard form** (all lectures write problems this way or convert first):

$$
\begin{array}{ll}
\text{minimize}   & f_0(x) \\
\text{subject to} & f_i(x) \le 0, \quad i = 1,\dots,m \\
                  & h_j(x) = 0, \quad j = 1,\dots,p
\end{array}
$$

| Symbol | Definition | Notes |
| :--- | :--- | :--- |
| $x \in \mathbb{R}^n$ | decision variable | $n$ = variable dimension |
| $f_0$ | objective | **minimization is the default**; maximization problems are negated on arrival |
| $f_i \le 0$, $h_j = 0$ | inequality / equality constraints | $m$ inequalities, $p$ equalities — reserved letters |
| $\mathcal{D} = \bigcap_i \operatorname{dom} f_i \cap \bigcap_j \operatorname{dom} h_j$ | problem domain | feasibility lives inside it |
| $p^\star$, $d^\star$ | primal / dual optimal values | weak duality: $d^\star \le p^\star$; gap $= p^\star - d^\star \ge 0$ |
| $x^\star$, $(\lambda^\star, \nu^\star)$ | primal / dual optimizers | stars mark optimality, never conjugation |
| $\lambda \in \mathbb{R}^m_+$ | inequality multipliers, $\lambda \succeq 0$ **always** | one per $f_i$ |
| $\nu \in \mathbb{R}^p$ | equality multipliers, sign-free | one per $h_j$ |
| $L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x)$ | Lagrangian | **plus** signs, with $f_i \le 0$ and $\lambda \ge 0$ |
| $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$ | dual function | concave always; $= -\infty$ allowed |
| $\lambda_i^\star f_i(x^\star) = 0$ | complementary slackness | at least one factor vanishes |
| $p^\star(u, v)$ | perturbed optimal value ($f_i \le u_i$, $h_j = v_j$) | shadow prices: $\lambda_i^\star = -\partial p^\star/\partial u_i$ (when differentiable) |
| $t > 0$, $\phi(x) = -\sum_i \log(-f_i(x))$ | barrier parameter, log barrier | central path $x^\star(t)$; gap $= m/t$ (L15 §3) |
| $\mu > 1$ | barrier-parameter growth factor per outer iteration | |

**KKT conditions** (referenced constantly; the reference form):

$$
f_i(x^\star) \le 0,\quad h_j(x^\star) = 0,\quad \lambda^\star \succeq 0,\quad
\lambda_i^\star f_i(x^\star) = 0,\quad
\nabla f_0(x^\star) + \textstyle\sum_i \lambda_i^\star \nabla f_i(x^\star) + \sum_j \nu_j^\star \nabla h_j(x^\star) = 0
$$

## 5. Calculus Layout Convention

- **Denominator layout with column gradients:** for $f : \mathbb{R}^n \to \mathbb{R}$,
  $\nabla f(x) \in \mathbb{R}^n$ is a column; the Jacobian of
  $F : \mathbb{R}^n \to \mathbb{R}^m$ is $DF(x) \in \mathbb{R}^{m \times n}$
  with rows $\nabla F_i(x)^\top$.
- Standard results, as used everywhere: $\nabla(a^\top x) = a$;
  $\nabla(x^\top A x) = (A + A^\top)x$ (so $2Ax$ for symmetric $A$);
  $\nabla^2(x^\top A x) = A + A^\top$; $\nabla(-\log\det X) = -X^{-1}$ on $\mathbb{S}^n_{++}$.
- First-order Taylor as used in proofs:
  $f(y) \approx f(x) + \nabla f(x)^\top (y - x)$ — the transpose sits on the gradient.

## 6. Algorithm Notation (L13–L15)

| Symbol | Meaning |
| :--- | :--- |
| $x^{(k)}$ | iterate at step $k$ (superscript-parenthesis, never subscript — subscripts are components) |
| $\Delta x$ | step/search direction ($\Delta x_{\text{nt}}$ for the Newton step) |
| $t^{(k)}$ or $s$ | step size from line search (context disambiguates from barrier $t$; within L15, **$s$ is the step size and $t$ the barrier parameter**) |
| $\alpha \in (0, 1/2)$, $\beta \in (0,1)$ | backtracking (Armijo) parameters: accept when $f(x + s\Delta x) \le f(x) + \alpha s \nabla f(x)^\top \Delta x$, else $s \leftarrow \beta s$ |
| $\eta$, $\epsilon$ | convergence thresholds (damped→quadratic phase boundary; stopping tolerance) |
| $\lambda(x)^2 = \Delta x_{\text{nt}}^\top \nabla^2 f(x) \Delta x_{\text{nt}}$ | Newton decrement (squared) — the L15 stopping certificate |
| $r(x, \nu) = (\nabla f(x) + A^\top \nu,\; Ax - b)$ | primal–dual residual (L14 infeasible start) |

## 7. Code ↔ Math Naming Map

Widget and lab code uses these identifiers so code reads as the math
(`docs/PEDAGOGY.md` §1 Station 3):

| Math | Code | Math | Code |
| :--- | :--- | :--- | :--- |
| $x$, $x^\star$ | `x`, `x_star` | $\lambda$, $\nu$ | `lam`, `nu` (never `lambda` — reserved in Python) |
| $f_0$, $\nabla f_0$ | `f0`, `grad_f0` | $\nabla^2 f$ | `hess_f` |
| $p^\star$, $d^\star$ | `p_star`, `d_star` | duality gap | `gap` |
| $A$, $b$, $c$ | `A`, `b`, `c` | $\kappa$ | `kappa` |
| $t$ (barrier), $\mu$ | `t`, `mu` | $s$ (step), $\alpha$, $\beta$ | `s`, `alpha`, `beta` |
| $m$, $L$ (SC/smooth) | `m_sc`, `L_smooth` | $\epsilon$ | `eps` |

Rules: no `foo`/`tmp`/`val`; Greek letters are spelled out (`sigma`, not `s`)
except where this table fixes a shorter form; index variables `i, j, k` match
their mathematical roles ($i$ inequalities, $j$ equalities, $k$ iterations).

## 8. Reserved-Letter Conflicts (disambiguation table)

Letters that mean different things in different lectures — each lecture states
which sense is active if both could appear:

| Letter | Sense A | Sense B | Rule |
| :--- | :--- | :--- | :--- |
| $\lambda$ | dual multiplier (L09+) | eigenvalue $\lambda_i(A)$ (L00–L01) | eigenvalues always carry the matrix argument: $\lambda_i(A)$ |
| $t$ | epigraph auxiliary variable (L07) | barrier parameter (L15) | L15 reserves $t$ for the barrier; epigraph variables become $\tau$ there |
| $m$ | number of inequality constraints | strong-convexity constant | constraint-count sense is default; strong convexity writes "$m$-strongly convex" in words at each use |
| $\mu$ | barrier growth factor (L15) | mean vector (L11) | context-local; never both in one section |
| $P$ | projection matrix (L00) | ellipsoid shape matrix (L03/L12) | ellipsoids always written with their defining set |
