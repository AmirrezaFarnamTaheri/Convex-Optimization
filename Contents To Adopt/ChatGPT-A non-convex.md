# A non-convex

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:05:20  
**Updated:** 12/28/2025 12:40:32  
**Exported:** 12/29/2025 0:12:02  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505f1e-1d00-8332-98d4-7f433b165742](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505f1e-1d00-8332-98d4-7f433b165742)  

## Response:
You’re looking at the classic **trust-region subproblem**:

$$
\begin{aligned} \min_{x\in\mathbb R^n}\quad & f(x):=x^T A x + 2 b^T x\\ \text{s.t.}\quad & x^T x \le 1, \end{aligned} \tag{P}
$$

with  $A\in\mathbb S^n$  symmetric and (in the screenshot) ** $A\nsucceq 0$ **, so the objective can curve downward in some directions → the problem is **nonconvex**.

Yet (plot twist) its Lagrange dual has **zero duality gap**: the dual optimum equals the primal optimum. Let’s unpack every line of what you see.

* * *

1) What this problem “is”, geometrically
----------------------------------------

*   The constraint  $x^T x \le 1$  is  $\|x\|_2\le 1$ : the **unit ball**.
*   The objective  $x^T A x + 2b^T x$  is a quadratic surface.
    *   If  $A\succeq 0$ , it’s convex (bowl-shaped).
    *   If  $A\nsucceq 0$ , it’s indefinite: it has at least one “downhill” direction.

So globally minimizing an indefinite quadratic is usually scary (NP-hard if unconstrained by general constraints). The miracle here is: **a single Euclidean ball constraint makes the dual exact**.

* * *

2) Primal → Lagrangian (where the  $\lambda$  comes from)
---------------------------------------------------------

The constraint is

$$
x^T x - 1 \le 0.
$$

For an inequality constraint  $g(x)\le 0$ , the Lagrangian uses a multiplier  $\lambda\ge 0$  and adds  $\lambda g(x)$ :

$$
L(x,\lambda)=x^T A x + 2b^T x + \lambda(x^T x-1).
$$

Group terms:

$$
L(x,\lambda)=x^T(A+\lambda I)x + 2b^T x - \lambda.
$$

Define

$$
H(\lambda):=A+\lambda I.
$$

So

$$
L(x,\lambda)=x^T H(\lambda)x+2b^T x-\lambda.
$$

* * *

3) Dual function  $g(\lambda)=\inf_x L(x,\lambda)$ : why those conditions appear
--------------------------------------------------------------------------------

By definition,

$$
g(\lambda):=\inf_{x\in\mathbb R^n} L(x,\lambda).
$$

So for a fixed  $\lambda$ , we are minimizing (over unconstrained  $x$ ) the quadratic

$$
\phi_\lambda(x)=x^T Hx+2b^T x-\lambda.
$$

The  $-\lambda$  doesn’t affect where the minimizer is; it just shifts the value.

### 3.1 When is the infimum finite (not  $-\infty$ )?

There are exactly two failure modes.

#### Failure mode A:  $H(\lambda)$  has a negative curvature direction

If  $H$  is not positive semidefinite, there exists  $d\neq 0$  with  $d^T H d<0$ .  
Then along  $x=td$ ,

$$
\phi_\lambda(td)=t^2(d^THd)+2t(b^Td)-\lambda \to -\infty \quad \text{as }|t|\to\infty
$$

because the  $t^2$  term dominates and is negative.

So we must have

$$
H(\lambda)=A+\lambda I \succeq 0.
$$

#### Failure mode B:  $H(\lambda)\succeq 0$  but is singular and the linear term “pushes” in a null direction

If  $H\succeq 0$  but has a nonzero nullspace, take  $d\in\mathrm{Null}(H)$  (so  $Hd=0$ ).  
Then

$$
\phi_\lambda(x+td)= (x+td)^TH(x+td)+2b^T(x+td)-\lambda = x^THx +2b^Tx -\lambda + 2t\,b^Td
$$

because all terms involving  $H$  and  $d$  vanish.

If  $b^Td\neq 0$ , you can choose  $t\to \pm\infty$  to drive  $\phi_\lambda\to -\infty$ .

So for finiteness we need:

$$
b^T d=0 \quad \forall d\in \mathrm{Null}(H).
$$

That condition is equivalent to

$$
b \in \mathrm{Range}(H).
$$

Why? For symmetric  $H$ ,  $\mathrm{Range}(H) = \mathrm{Null}(H)^\perp$ . Saying “ $b$  is orthogonal to the nullspace” is exactly saying “ $b$  lies in the range”.

So **finite dual function** requires both:

$$
A+\lambda I\succeq 0,\qquad b\in \mathcal R(A+\lambda I).
$$

That matches the screenshot.

* * *

4) Actually computing  $\inf_x L(x,\lambda)$ : where the pseudoinverse comes from
---------------------------------------------------------------------------------

Assume the conditions hold. Then the quadratic is convex (maybe flat in some directions), so it attains a minimum.

Differentiate w.r.t.  $x$ :

$$
\nabla_x \phi_\lambda(x)=2Hx+2b.
$$

Stationary points satisfy

$$
Hx + b = 0. \tag{*}
$$
*   If  $H$  is invertible:  $x^*(\lambda)=-H^{-1}b$ .
*   If  $H$  is singular: equation  $(*)$  has a solution **iff**  $b\in \mathcal R(H)$ , which we already required. The minimum-norm solution is  $x^*=-H^\dagger b$ , where  $H^\dagger$  is the **Moore–Penrose pseudoinverse**.

Now plug the minimizer value into the quadratic. A clean identity (true for PSD  $H$  with  $b\in\mathcal R(H)$ ) is:

$$
\inf_x \{x^T Hx + 2b^Tx\} = -\,b^T H^\dagger b.
$$

Therefore:

$$
g(\lambda)= -\,b^T(A+\lambda I)^\dagger b \;-\;\lambda,
$$

when  $A+\lambda I\succeq 0$  and  $b\in\mathcal R(A+\lambda I)$ ; otherwise  $g(\lambda)=-\infty$ .

That is exactly what the text states.

* * *

5) The dual problem (and why it’s convex / easy)
------------------------------------------------

The Lagrange dual is:

$$
\begin{aligned} \max_{\lambda\ge 0}\quad & g(\lambda)\\ \text{s.t.}\quad & A+\lambda I\succeq 0,\;\; b\in\mathcal R(A+\lambda I). \end{aligned} \tag{D}
$$

In the screenshot they write “ $\lambda\in\mathbb R$ ” but in this nonconvex setting they also assume  $A\nsucceq 0$ , which forces  $\lambda\ge -\lambda_{\min}(A)>0$  anyway (so it ends up nonnegative automatically at feasibility). The “correct” inequality-multiplier rule is  $\lambda\ge 0$ ; feasibility via PSD already implies it here.

Why is it “convex optimization” even though it’s a maximization? Because it’s maximizing a **concave** function of  $\lambda$  over a convex set. And it’s only **one scalar variable**.

* * *

6) Turning the dual into the eigenvalue formula in the screenshot
-----------------------------------------------------------------

Let  $A$  have spectral decomposition:

$$
A = Q\Lambda Q^T,\qquad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n),
$$

with orthonormal eigenvectors  $q_i$  (columns of  $Q$ ).

Write  $b$  in that basis:

$$
b = \sum_{i=1}^n \beta_i q_i,\qquad \beta_i:=q_i^T b.
$$

Then

$$
A+\lambda I = Q(\Lambda+\lambda I)Q^T,
$$

so its eigenvalues are  $\lambda_i+\lambda$ .

### PSD constraint

$$
A+\lambda I\succeq 0 \iff \lambda_i+\lambda\ge 0\ \forall i \iff \lambda\ge -\lambda_{\min}(A).
$$

### Range condition  $b\in\mathcal R(A+\lambda I)$ 

If  $\lambda_i+\lambda=0$  for some  $i$ , that direction is in the nullspace. Then we must have  $\beta_i=0$  for all such  $i$ . The text encodes this with the convention

$$
\frac{\beta_i^2}{\lambda_i+\lambda}=0 \quad \text{when } \beta_i=0 \text{ and } \lambda_i+\lambda=0
$$

(i.e., treat  $0/0$  as  $0$  here).

### Pseudoinverse in eigenbasis

$$
(A+\lambda I)^\dagger = Q(\Lambda+\lambda I)^\dagger Q^T,
$$

where  $(\Lambda+\lambda I)^\dagger$  has diagonal entries

$$
\frac{1}{\lambda_i+\lambda}\ \text{if }\lambda_i+\lambda>0,\quad 0\ \text{if }\lambda_i+\lambda=0.
$$

So

$$
b^T(A+\lambda I)^\dagger b = \sum_{i=1}^n \frac{\beta_i^2}{\lambda_i+\lambda}
$$

with that same convention.

Therefore the dual becomes the 1D problem:

$$
\begin{aligned} \max_{\lambda\ge -\lambda_{\min}(A)}\quad & -\sum_{i=1}^n \frac{(q_i^T b)^2}{\lambda_i+\lambda} \;-\;\lambda, \end{aligned}
$$

which matches the screenshot.

This is extremely nice computationally: a scalar concave maximization.

* * *

7) How the dual “finds” the primal optimizer (KKT conditions)
-------------------------------------------------------------

At optimality (under Slater, which holds because  $x=0$  satisfies  $x^Tx<1$ ), you get KKT conditions that are not just necessary but (in this special problem) essentially sufficient:

1.  **Stationarity**
    
$$
(A+\lambda^* I)x^* + b = 0.
$$
2.  **Primal feasibility**
    
$$
\|x^*\|_2^2\le 1.
$$
3.  **Dual feasibility**
    
$$
\lambda^*\ge 0,\quad A+\lambda^* I\succeq 0.
$$
4.  **Complementary slackness**
    
$$
\lambda^*(\|x^*\|_2^2-1)=0.
$$

Interpretation:

*   If the unconstrained minimizer fits inside the ball, constraint is inactive →  $\lambda^*=0$ .
*   In the nonconvex case  $A\nsucceq 0$ , the solution typically lies on the boundary  $\|x^*\|=1$  with  $\lambda^*>0$ , and  $\lambda^*$  “shifts”  $A$  until  $A+\lambda^*I\succeq 0$ .

* * *

8) The “miracle”: why strong duality holds even though the primal is nonconvex
------------------------------------------------------------------------------

General convex duality says: convex + Slater ⇒ strong duality.  
Here the primal is **not convex**, so that theorem doesn’t apply.

What applies instead is a special fact about QCQPs with **one quadratic inequality constraint** (often packaged as the **S-lemma / S-procedure** result). Roughly:

*   With one quadratic constraint and Slater (strict feasibility), the condition
    $$
    x^T A x + 2b^T x \ge \gamma \quad \text{for all }\|x\|^2\le 1
    $$
    can be certified by a single scalar  $\lambda\ge 0$  such that a certain lifted matrix is PSD.
*   That certificate structure is exactly what the dual is optimizing over.
*   Hence the best certificate bound equals the true optimum → **zero duality gap**.

So this is one of those rare nonconvex problems where the dual is not just a bound; it is **exact**.

* * *

9) One extra layer: solving the 1D dual in practice (the root condition)
------------------------------------------------------------------------

Let

$$
\psi(\lambda):=-\sum_{i=1}^n \frac{\beta_i^2}{\lambda_i+\lambda}-\lambda.
$$

For feasible  $\lambda>-\lambda_{\min}(A)$ , differentiate:

$$
\psi'(\lambda)=\sum_{i=1}^n \frac{\beta_i^2}{(\lambda_i+\lambda)^2}-1.
$$

At an interior maximizer  $\lambda^*$ ,

$$
\sum_{i=1}^n \frac{\beta_i^2}{(\lambda_i+\lambda^*)^2}=1.
$$

That equation is tightly connected to  $\|x^*\|=1$ , because  $x^*=-(A+\lambda^*I)^{-1}b$  (when invertible), and in the eigenbasis

$$
\|x^*\|^2=\sum_{i=1}^n \frac{\beta_i^2}{(\lambda_i+\lambda^*)^2}.
$$

So the dual optimality condition is literally enforcing the trust-region boundary.

* * *

If you want the next step, the natural continuation is: “Given  $\lambda^*$ , construct  $x^*$ ” including the singular case  $A+\lambda^*I\succeq 0$  but not invertible, and show explicitly (by algebra) that  $f(x^*) = g(\lambda^*)$ . That last identity is the cleanest way to _see_ strong duality here without invoking the S-lemma by name.

## Response:
Great — we're going to unpack the **nonconvex quadratic problem with strong duality** example from the book (Equation (5.32)–(5.33)), step by step, with a complete zero-to-hero roadmap. This is a foundational example for understanding **trust-region problems**, **nonconvex QCQPs**, and why they can still have **zero duality gap** and **strong duality**, despite the primal being nonconvex.

* * *

🧭 Roadmap for Fully Understanding This Problem
-----------------------------------------------

Each step will be delivered in a **self-contained deep walkthrough**, and we’ll go section by section until the entire image and duality phenomenon are internalized.

* * *

### ✅ PHASE 0 — Problem Setup and High-Level Intuition

> What is this optimization problem really about?

| Step | Goal |
| --- | --- |
| 0.1 | Define and interpret the primal problem: Equation (5.32) |
| 0.2 | Explain why it is nonconvex (even though quadratic) |
| 0.3 | Intuition: Why does this show up in real problems? (trust region, local approximation, etc.) |
| 0.4 | Geometry of constraint: the unit ball (ellipsoid) |

* * *

### ✅ PHASE 1 — Deriving the Dual

> How do we construct the Lagrangian and get to the dual problem?

| Step | Goal |
| --- | --- |
| 1.1 | Write and unpack the Lagrangian  $L(x, \lambda)$  |
| 1.2 | Explain the domain of λ (why λ ≥ 0) |
| 1.3 | Define the dual function  $g(\lambda)$ : inf over x |
| 1.4 | When is the dual function finite? Domain conditions |
| 1.5 | Derive the expression for  $g(\lambda)$  (pseudoinverse form) |
| 1.6 | Explain meaning of range constraint  $b \in \mathcal{R}(A + \lambda I)$  |

* * *

### ✅ PHASE 2 — Dual Problem as Convex Optimization

> Why is the dual convex, even though the primal is not?

| Step | Goal |
| --- | --- |
| 2.1 | Express the dual problem (maximize g(λ) subject to λ ≥ 0) |
| 2.2 | Convexity of dual: properties of supremum of affine functions |
| 2.3 | Rewrite dual in eigenbasis of A |
| 2.4 | Explain orthogonal diagonalization and pseudoinverse in spectral terms |
| 2.5 | Interpret dual as convex function in λ |

* * *

### ✅ PHASE 3 — Strong Duality and No Duality Gap

> Why do we get exact recovery (no gap) even though the primal is nonconvex?

| Step | Goal |
| --- | --- |
| 3.1 | Slater’s condition for dual |
| 3.2 | What does strong duality mean in this setting? |
| 3.3 | Why is optimal value of primal = optimal value of dual here? |
| 3.4 | Geometric intuition: ellipse inside ball + dual hyperplane |
| 3.5 | Generalization: any QCQP with one quadratic inequality (S-Lemma) |

* * *

### ✅ PHASE 4 — Bonus Topics (Optional Deep Dives)

| Step | Goal |
| --- | --- |
| 4.1 | Trust-region subproblem as special case of QCQP |
| 4.2 | Duality via S-lemma (proof sketch) |
| 4.3 | Eigenvalue interpretation of solution |
| 4.4 | Compare with nonconvex problems that **do** have duality gaps |
| 4.5 | Applications in robust optimization, control, machine learning |

* * *

⏱️ Ready to Begin?
------------------

We’ll start with **Phase 0**, and deliver step **0.1** now: define and fully unpack the primal problem.

Shall I begin with that?

2/2

## Response:
Perfect — let’s now rigorously walk through **0.1** and **0.2**, unpacking every detail of the problem setup and why it is **nonconvex**, despite appearances. This is the foundation on which the duality and solution analysis will build, so we’ll go slowly and thoroughly.

* * *

✅ Step 0.1 — Define and Interpret the Primal Problem
====================================================

We are given the following optimization problem:

$$
\begin{aligned} \text{minimize}_{x \in \mathbb{R}^n} \quad & f(x) := x^T A x + 2b^T x \\ \text{subject to} \quad & x^T x \leq 1 \end{aligned} \tag{P}
$$

Let’s unpack every piece:

* * *

### 🔹 Objective function:  $f(x) = x^T A x + 2b^T x$ 

This is a **quadratic function** in  $x \in \mathbb{R}^n$ , with:

*    $A \in \mathbb{S}^n$ : a real symmetric matrix, i.e.,  $A = A^T$ 
*    $b \in \mathbb{R}^n$ : a vector

So:

*   The term  $x^T A x$  is the **quadratic form**.
*   The term  $2b^T x$  is a **linear term**.
*   The total objective is **quadratic in  $x$ **.

Note: The scalar factor 2 on  $b^T x$  is a convention — it simplifies derivatives later. It's common in trust-region problems because the gradient becomes  $\nabla f(x) = 2Ax + 2b$ .

* * *

### 🔹 Constraint:  $x^T x \leq 1$ 

This is a **norm constraint**. In more familiar notation:

$$
\|x\|_2^2 \leq 1 \quad \iff \quad x \in \mathbb{B}^n := \{x \in \mathbb{R}^n : \|x\|_2 \leq 1\}
$$

So we're minimizing a quadratic function **over the unit ball** in  $\mathbb{R}^n$ .

* * *

### 🔹 What kind of problem is this?

This is a **quadratically constrained quadratic program (QCQP)**:

*   **Objective**: quadratic
*   **Constraint**: quadratic (here, convex)

In short:

*   **Minimize a quadratic** over the **unit Euclidean ball**.

* * *

### 🔹 Names for this problem

This specific structure is known as the **trust-region subproblem**:

*   Arises in numerical optimization, when approximating a complicated function locally via quadratic models (like Newton's method).
*   The idea: minimize a second-order Taylor approximation (which gives the quadratic form) **within a trust region**, i.e., a small ball around the current point.

* * *

### 🔹 Example context

Suppose you're optimizing a complicated nonlinear function  $f_{\text{true}}(x)$ , but it's hard to minimize directly. Around some point  $x_0$ , you form a **second-order Taylor approximation**:

$$
f_{\text{true}}(x_0 + d) \approx f(x_0) + \nabla f^T d + \frac{1}{2} d^T H d
$$

This is quadratic in  $d$ . But to ensure the approximation is valid (locally accurate), you only trust it **within a small ball**, say  $\|d\| \leq \delta$ . So you end up solving something of the form:

$$
\min_{\|d\| \leq \delta} \quad d^T H d + 2 \nabla f^T d
$$

Which is exactly our primal problem with appropriate scaling.

* * *

✅ Step 0.2 — Why is This Problem Nonconvex?
-------------------------------------------

Let’s now rigorously analyze the convexity of the objective and constraint.

* * *

### 🔹 Constraint is convex

$$
x^T x \leq 1 \quad \iff \quad \|x\|_2^2 \leq 1
$$
*   This is a convex constraint because the unit ball  $\mathbb{B}^n$  is a convex set.
*   The function  $x \mapsto \|x\|_2^2$  is convex.
*   The inequality  $\|x\|_2^2 \leq 1$  defines a **sublevel set** of a convex function — hence, convex.

✅ **Constraint set is convex**.

* * *

### 🔹 Objective: is it convex?

$$
f(x) = x^T A x + 2b^T x
$$

We must ask: is this function **convex in  $x$ **?

> A function  $f: \mathbb{R}^n \to \mathbb{R}$  is convex if and only if its **Hessian** is positive semidefinite (PSD) everywhere.

* * *

#### 🔸 What is the Hessian of this function?

Let’s compute:

*   The gradient:
    $$
    \nabla f(x) = 2A x + 2b
    $$
*   The Hessian:
    $$
    \nabla^2 f(x) = 2A
    $$

So the convexity of  $f(x)$  depends on whether  $A \succeq 0$  (positive semidefinite).

* * *

#### 🔸 Case analysis

*   If  $A \succeq 0$ , then  $f(x)$  is convex.
*   If  $A \prec 0$ , then  $f(x)$  is concave.
*   If  $A$  has **both positive and negative eigenvalues**, then  $f(x)$  is **neither convex nor concave**.

In our problem:

> **The assumption is:  $A \not\succeq 0$ **.

So  $A$  is **not** positive semidefinite — it has **some negative eigenvalues**.

🔻 Therefore:

*    $f(x)$  is **nonconvex**.
*   The **overall optimization problem is nonconvex** because the objective is nonconvex (even though the constraint set is convex).

* * *

### 🔹 Why does this matter?

This is critical because **nonconvex problems may not have strong duality**, and may have a **duality gap**:

*   The dual optimal value can **underestimate** the primal optimal value.
*   But surprisingly, this particular problem **does have strong duality**, despite nonconvexity — a rare and beautiful exception.

We’ll rigorously prove this in upcoming steps.

* * *

✅ Summary of 0.1–0.2
--------------------

| Concept | Explanation |
| --- | --- |
| **Primal problem** | Minimize a general quadratic function  $x^T A x + 2b^T x$  over the unit ball |
| **Constraint set** |  $\|x\|_2 \leq 1$ , convex |
| **Objective function** | Nonconvex (since  $A \not\succeq 0$ ) |
| **Type** | Quadratically constrained quadratic program (QCQP) |
| **Convexity?** | ❌ Not convex |
| **Why important?** | Despite being nonconvex, this problem will have strong duality and no duality gap — a striking result |

* * *

✅ Ready for **Step 0.3**? It will walk through **why this model shows up in practice**, especially in trust-region methods, and give you more geometric and optimization-theoretic context. Let me know and I’ll proceed.

## Response:
Excellent. Let’s now cover:

*   **0.3** — The **motivation and context** for this problem (why it arises naturally in optimization)
*   **0.4** — The **geometry of the constraint**, i.e. the unit ball  $x^T x \leq 1$ 

Both will deepen our intuition for the nonconvex problem and prepare us to appreciate the duality result that follows.

* * *

✅ Step 0.3 — Why Does This Problem Arise? (Trust Region Motivation)
===================================================================

### 🔹 This problem is a standard form of the **trust-region subproblem**.

It arises when you try to minimize a complicated function using **local approximations**, but limit the step size because the approximation may not be valid far from your current point.

Let’s reconstruct the logic step by step.

* * *

### 🚩 Context: Local Minimization of a Nonlinear Function

Suppose you are minimizing a general nonlinear function  $f_{\text{true}}(x)$ , which may be:

*   nonconvex,
*   expensive to evaluate,
*   or not explicitly available (e.g., via black-box simulation, gradient estimates, etc.).

You might not be able to directly minimize it. So instead, you **build a local quadratic model** of the function around your current iterate  $x_0$ .

* * *

### 🔸 Second-Order Taylor Approximation

Let’s say you're currently at  $x_0$ , and define the displacement  $d := x - x_0$ . The **second-order Taylor approximation** of  $f_{\text{true}}$  around  $x_0$  is:

$$
f_{\text{true}}(x_0 + d) \approx f_{\text{true}}(x_0) + \nabla f_{\text{true}}(x_0)^T d + \frac{1}{2} d^T \nabla^2 f_{\text{true}}(x_0) d
$$

You then want to **minimize this quadratic approximation** with respect to  $d$ , **but only trust it locally**, i.e. for small  $\|d\|$ .

* * *

### 🔸 Define the Trust Region

To restrict to a neighborhood around  $x_0$ , we constrain  $d$  to lie inside a ball:

$$
\|d\|_2 \leq \delta
$$

This gives us the **trust region subproblem**:

$$
\begin{aligned} \text{minimize}_{d \in \mathbb{R}^n} \quad & \frac{1}{2} d^T H d + g^T d \\ \text{subject to} \quad & \|d\|_2 \leq \delta \end{aligned}
$$

where:

*    $H = \nabla^2 f_{\text{true}}(x_0)$ : the Hessian
*    $g = \nabla f_{\text{true}}(x_0)$ : the gradient

This is _exactly_ the same form as our earlier problem, just with different notation.

* * *

### 🔸 Recovering Our Problem Form

Rescale  $d \to x$ , and set  $\delta = 1$  (without loss of generality; we can scale later). The problem becomes:

$$
\begin{aligned} \text{minimize}_x \quad & x^T A x + 2 b^T x \\ \text{subject to} \quad & x^T x \leq 1 \end{aligned}
$$

Where:

*    $A = H$ 
*    $b = g$ 

🧠 This is the **canonical trust-region subproblem**, widely used in:

*   Quasi-Newton methods (e.g. BFGS)
*   Sequential Quadratic Programming (SQP)
*   Nonlinear least-squares solvers
*   Interior-point methods (for inner approximation steps)

* * *

### 🔸 What makes this problem subtle?

*   If  $A = H \succeq 0$ , the quadratic is convex — easy.
*   But often,  $A$  is **indefinite** (e.g., Hessian has both positive and negative eigenvalues).
    *   Then the objective is **nonconvex**.
    *   But the constraint set (unit ball) is convex.

This is what makes it hard — and also **interesting**.

* * *

📌 Summary of 0.3
-----------------

| Concept | Explanation |
| --- | --- |
| **Where this problem comes from** | It's the local quadratic approximation of a nonlinear function |
| **Trust region idea** | Approximation is only valid within a neighborhood (ball constraint) |
| **Why ball constraint?** | Controls step size so Taylor expansion remains accurate |
| **Objective** | Comes from gradient and Hessian of  $f_{\text{true}}$  |
| **Why relevant?** | It appears in almost every serious nonlinear optimization algorithm |
| **Key challenge** | If  $A$  is indefinite, the problem is nonconvex — yet solvable! |

* * *

✅ Step 0.4 — Geometry of the Constraint: The Unit Ball
======================================================

The constraint in our problem is:

$$
x^T x \leq 1 \quad \iff \quad \|x\|_2 \leq 1
$$

Let’s unpack this geometrically and algebraically.

* * *

### 🔸 The Set:  $\mathbb{B}^n = \{ x \in \mathbb{R}^n : \|x\|_2 \leq 1 \}$ 

This is called the **unit Euclidean ball** in  $\mathbb{R}^n$ .

#### Geometric Description:

*   **Center**: the origin (0)
*   **Radius**: 1
*   **Boundary**: the **unit sphere**  $\|x\| = 1$ 
*   **Interior**: all points  $\|x\| < 1$ 

#### Examples:

*   In  $\mathbb{R}^2$ : it’s a filled-in **disk**
*   In  $\mathbb{R}^3$ : a **solid ball**
*   In  $\mathbb{R}^n$ : a generalization of this to n dimensions

* * *

### 🔸 Properties of the Unit Ball

| Property | Explanation |
| --- | --- |
| **Convex** | Every point on the line segment between two points in the ball lies inside the ball |
| **Closed** | Contains its boundary |
| **Bounded** | All points are at most distance 1 from the origin |
| **Strictly convex** | Boundary has no flat parts (no line segments on boundary) |
| **Smooth boundary** | The boundary  $\|x\| = 1$  is smooth (differentiable everywhere) |

* * *

### 🔸 Why is this a good constraint?

*   It’s **simple** and **geometrically clean**
*   Leads to **strong duality** under specific conditions
*   Trust-region algorithms prefer balls over boxes because they are **isotropic**: no direction is preferred

* * *

### 🔸 Constraint Set and Optimization

Let’s define:

$$
\mathcal{F} := \{ x \in \mathbb{R}^n : x^T x \leq 1 \}
$$

This is the **feasible set**.

We’re minimizing a (possibly nonconvex) quadratic function over this **compact, convex, closed** set.

🧠 Even though the feasible set is nice, the objective can behave badly — it can:

*   have multiple local minima,
*   be unbounded below outside the ball,
*   have saddle points.

But the constraint keeps us within a bounded, convex region.

* * *

### 🔸 Visualization in  $\mathbb{R}^2$ 

Let’s suppose we are in  $\mathbb{R}^2$ . Then:

*    $x = [x_1, x_2]^T$ 
*   The constraint  $x_1^2 + x_2^2 \leq 1$  is a **filled-in circle**
*   Objective might be:
    *   A tilted paraboloid (if convex),
    *   A saddle (if indefinite A),
    *   A “valley” along one direction and “hill” along another

The optimizer lies **somewhere inside this disk**, possibly on the **boundary**.

* * *

📌 Summary of 0.4
-----------------

| Concept | Explanation |
| --- | --- |
| **Constraint set** | Unit Euclidean ball in  $\mathbb{R}^n$ , i.e.,  $\|x\| \leq 1$  |
| **Convex?** | ✅ Yes |
| **Geometry** | Closed, bounded, strictly convex |
| **Why used?** | Common trust-region shape, leads to strong duality |
| **Feasible set** | Compact (bounded and closed), so minimum exists (Weierstrass theorem) |
| **Key point** | Even though the objective is nonconvex, constraint is very well-behaved |

* * *

✅ Up next: **Step 1.1–1.2**, where we define and unpack the **Lagrangian** of the problem, and explain why we introduce a **Lagrange multiplier  $\lambda$ ** and constrain  $\lambda \geq 0$ .

Shall I proceed?

## Response:
Excellent — we now move into **Phase 1: Constructing the Dual**.

We’ll cover:

*   **Step 1.1**: Write and fully unpack the **Lagrangian** of the primal problem
*   **Step 1.2**: Explain **why the Lagrange multiplier is constrained** to  $\lambda \geq 0$ 

We’re beginning the **machinery of duality**: the Lagrangian, dual function, and finally the dual problem itself.

* * *

✅ Step 1.1 — Constructing and Unpacking the Lagrangian
======================================================

### 🔹 Recap of the Primal Problem

$$
\begin{aligned} \min_{x \in \mathbb{R}^n} \quad & f(x) := x^T A x + 2b^T x \\ \text{s.t.} \quad & x^T x \leq 1 \end{aligned} \tag{P}
$$

We want to construct its **Lagrangian**  $L(x, \lambda)$ .

* * *

### 🔸 General form of a Lagrangian

For a problem of the form:

$$
\min_x \quad f_0(x) \quad \text{s.t. } f_i(x) \leq 0,
$$

the **Lagrangian** is:

$$
L(x, \lambda) := f_0(x) + \sum_{i=1}^m \lambda_i f_i(x), \quad \lambda_i \geq 0
$$

In our case, there is **only one inequality constraint**:

$$
f_1(x) := x^T x - 1 \leq 0
$$

Hence, we introduce a **single Lagrange multiplier  $\lambda \geq 0$ ** and write:

$$
L(x, \lambda) = f(x) + \lambda (x^T x - 1)
$$

Substitute  $f(x) = x^T A x + 2b^T x$ :

$$
L(x, \lambda) = x^T A x + 2b^T x + \lambda(x^T x - 1)
$$

* * *

### 🔸 Clean up and group terms

Let’s collect like terms:

$$
L(x, \lambda) = x^T A x + \lambda x^T x + 2b^T x - \lambda
$$

Group the quadratic terms:

$$
= x^T (A + \lambda I) x + 2b^T x - \lambda
$$

✅ **This is the Lagrangian**:

$$
\boxed{ L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda }
$$

Let’s dissect each term:

*    $x^T (A + \lambda I) x$ : combined quadratic form
*    $2b^T x$ : linear term
*    $-\lambda$ : constant penalty for violating the constraint

* * *

### 🔸 Interpretation

Think of this Lagrangian as a **penalized objective**:

*   You're still minimizing  $f(x)$ 
*   But if the constraint is violated (i.e.,  $x^T x > 1$ ), the term  $\lambda(x^T x - 1)$  penalizes the objective
*   The dual variable  $\lambda$  controls how harsh this penalty is

* * *

✅ Step 1.2 — Why Is  $\lambda \geq 0$  Required?
------------------------------------------------

This is crucial. Let’s understand why the **Lagrange multiplier must be nonnegative**.

* * *

### 🔸 Basic KKT Rule: Sign of Multipliers for Inequality Constraints

Whenever you have a constraint:

$$
f_i(x) \leq 0
$$

the associated Lagrange multiplier  $\lambda_i$  **must satisfy**:

$$
\lambda_i \geq 0
$$

This is a **fundamental rule in convex optimization and duality theory**, coming from the **Karush-Kuhn-Tucker (KKT)** conditions.

Why?

Because if we allowed  $\lambda_i < 0$ , then:

*   The term  $\lambda_i f_i(x)$  could **reward** constraint violation
*   It would **lower** the Lagrangian when  $f_i(x) > 0$ 
*   This goes against the meaning of a “penalty term” for infeasibility

🧠 In short:  
→ To penalize violation of  $x^T x \leq 1$ , we need  $\lambda \geq 0$ .

* * *

### 🔸 Geometric Meaning

Think of  $\lambda$  as the **slope of the supporting hyperplane** to the feasible region. If you let it go negative, the “supporting” plane becomes **non-supporting** — it cuts inside the feasible set.

That breaks all geometric and duality theorems.

* * *

### 🔸 Summary: Why  $\lambda \geq 0$ 

| Reason | Explanation |
| --- | --- |
| Mathematical | From KKT theory: multipliers for inequality constraints must be ≥ 0 |
| Geometric | Prevents hyperplanes from cutting into feasible region |
| Optimization meaning | Ensures constraint violations are penalized, not rewarded |
| Dual function | Will only be **valid** and **bounded below** if  $\lambda \geq 0$  |

* * *

✅ Summary of Steps 1.1–1.2
--------------------------

| Concept | Explanation |
| --- | --- |
| **Lagrangian** |  $L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda$  |
| **What it does** | Combines objective and constraint via a penalty term |
| **Why  $\lambda \geq 0$ ** | Ensures constraint is treated properly (no reward for violation) |
| **Next Step** | Define the **dual function**: minimize  $L(x, \lambda)$  over  $x$  |

* * *

Up next:

*   **Step 1.3–1.4**: Compute the **dual function**  $g(\lambda) = \inf_x L(x, \lambda)$ , and determine **when it's finite**.
*   We’ll go through the algebra **carefully**, derive the closed-form, and start seeing how duality emerges.

Shall I proceed?

## Response:
Excellent — now we enter the **heart of the duality construction**.

We will now:

*   **1.3**: Define and compute the **dual function**  $g(\lambda) := \inf_x L(x, \lambda)$ 
*   **1.4**: Analyze **when this function is finite**, i.e., when the infimum is not  $-\infty$ 

This is where the dual gets its shape — the **convex function** of  $\lambda$ , which we will **maximize** in the dual problem later.

* * *

✅ Step 1.3 — Define and Compute the Dual Function
=================================================

* * *

### 🔹 Recap: Lagrangian

We already derived:

$$
L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda
$$

We now define the **dual function**:

$$
g(\lambda) := \inf_{x \in \mathbb{R}^n} L(x, \lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T (A + \lambda I) x + 2b^T x - \lambda \right)
$$

This is a **function of  $\lambda$  only**.

* * *

### 🔹 Let’s define:

Let’s define:

*    $Q := A + \lambda I$ 
*   So we want to compute:
    
$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T Q x + 2b^T x - \lambda \right)
$$

* * *

### 🧠 Strategy:

This is a **quadratic function in  $x$ **. To minimize it, we use the **standard formula** for minimizing unconstrained quadratic functions:

Let  $Q \in \mathbb{S}^n$ ,  $b \in \mathbb{R}^n$ . The unconstrained minimum of:

$$
f(x) = x^T Q x + 2b^T x
$$

is:

*   **If  $Q \succ 0$ ** (positive definite):  
    The minimum occurs at  $x^\star = -Q^{-1} b$ 
*   **If  $Q \succeq 0$ ** (positive semidefinite), but not invertible:  
    The minimum occurs **if**  $b \in \mathcal{R}(Q)$ , and the minimum is attained at any:
    $$
    x^\star \in -Q^\dagger b + \ker(Q)
    $$
    where  $Q^\dagger$  is the **Moore–Penrose pseudoinverse**.
*   **If  $Q \not\succeq 0$ **: the quadratic is **unbounded below** — infimum is  $-\infty$ 

We’ll carefully derive all of these next.

* * *

🧮 Detailed Derivation of  $g(\lambda)$ 
----------------------------------------

Recall:

$$
g(\lambda) = \inf_x \left( x^T Q x + 2b^T x - \lambda \right)
$$

We are minimizing the function:

$$
f(x) := x^T Q x + 2b^T x
$$

Let’s try to complete the square in  $x$ .

* * *

### 🔸 Step 1: Complete the Square

We write:

$$
x^T Q x + 2b^T x = (x + Q^{-1}b)^T Q (x + Q^{-1} b) - b^T Q^{-1} b
$$

✅ This is only valid **if  $Q$  is invertible**, i.e.,  $Q \succ 0$ .

So in that case:

$$
g(\lambda) = \inf_x \left( (x + Q^{-1}b)^T Q (x + Q^{-1} b) - b^T Q^{-1} b - \lambda \right)
$$

But the first term is always ≥ 0, minimized at 0. So:

$$
g(\lambda) = - b^T Q^{-1} b - \lambda \quad \text{if } Q = A + \lambda I \succ 0
$$

That gives the closed-form for  $g(\lambda)$ .

* * *

### 🔸 What if  $Q \succeq 0$ , but **singular**?

Then we can’t use the inverse — but we can still minimize using the **pseudoinverse**.

Suppose:

*    $Q \succeq 0$ 
*   Let’s suppose  $b \in \mathcal{R}(Q)$  (i.e., range of  $Q$ )

Then:

*   There exists  $x^\star \in \mathbb{R}^n$  such that:
    $$
    Q x^\star = -b
    $$
*   So:
    $$
    x^\star = - Q^\dagger b + z, \quad \text{for any } z \in \ker(Q)
    $$
*   And the minimum is still finite and given by:
    $$
    g(\lambda) = - b^T Q^\dagger b - \lambda
    $$

But if  $b \notin \mathcal{R}(Q)$ , then:

*   The minimization has **no solution** (no  $x$  satisfies the first-order condition),
*   And the quadratic form goes to  $-\infty$  in some direction (since  $Q$  is singular),
*   So  $g(\lambda) = -\infty$ 

* * *

✅ Step 1.4 — When is  $g(\lambda)$  Finite?
===========================================

Let’s now **characterize the domain of the dual function**  $g(\lambda)$ :

We know:

$$
g(\lambda) = \begin{cases} - b^T (A + \lambda I)^{-1} b - \lambda & \text{if } A + \lambda I \succ 0 \\ - b^T (A + \lambda I)^\dagger b - \lambda & \text{if } A + \lambda I \succeq 0 \text{ and } b \in \mathcal{R}(A + \lambda I) \\ -\infty & \text{otherwise} \end{cases}
$$

So the dual function is **finite** only when:

### ✅ Condition:

$$
A + \lambda I \succeq 0 \quad \text{and} \quad b \in \mathcal{R}(A + \lambda I)
$$

Let’s break this into parts.

* * *

### 🔹 Condition 1:  $A + \lambda I \succeq 0$ 

*    $A$  may have **negative eigenvalues**.
*   Adding  $\lambda I$  **shifts all eigenvalues up** by  $\lambda$ 
*   So to ensure  $A + \lambda I \succeq 0$ , we must take  $\lambda \geq -\lambda_{\min}(A)$ 

🧠 Think of  $\lambda$  as "neutralizing" the nonconvexity of  $A$ 

* * *

### 🔹 Condition 2:  $b \in \mathcal{R}(A + \lambda I)$ 

Why is this needed?

Because in order to solve:

$$
\nabla_x L(x, \lambda) = 2(A + \lambda I)x + 2b = 0
$$

We need to be able to **solve the equation**:

$$
(A + \lambda I) x = -b
$$

This equation only has a solution if  $b \in \mathcal{R}(A + \lambda I)$ 

If not, then  $x \mapsto L(x, \lambda) \to -\infty$  in directions where  $Qx + b \to 0$ , but  $x$  goes to infinity

* * *

📌 Final Form of Dual Function
------------------------------

$$
\boxed{ g(\lambda) = \begin{cases} - b^T (A + \lambda I)^{-1} b - \lambda & \text{if } A + \lambda I \succ 0 \\ - b^T (A + \lambda I)^\dagger b - \lambda & \text{if } A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \\ -\infty & \text{otherwise} \end{cases} }
$$

* * *

### ✅ Domain of the dual function:

$$
\boxed{ \operatorname{dom}(g) = \left\{ \lambda \geq 0 \mid A + \lambda I \succeq 0,\quad b \in \mathcal{R}(A + \lambda I) \right\} }
$$

* * *

### 🧠 Intuition:

*   The **dual function** is always concave (since it's a pointwise infimum over affine functions).
*   But it may take  $-\infty$  values outside its domain.
*   The domain is where the **penalized quadratic** is **bounded below**.

* * *

✅ Summary of Steps 1.3–1.4
--------------------------

| Concept | Explanation |
| --- | --- |
| **Dual function** |  $g(\lambda) = \inf_x L(x, \lambda)$  |
| **Lagrangian** |  $L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda$  |
| **Closed-form** |  $g(\lambda) = -b^T (A + \lambda I)^{-1} b - \lambda$  when  $A + \lambda I \succ 0$  |
| **General form** | Use pseudoinverse if  $A + \lambda I$  is singular and  $b \in \mathcal{R}(A + \lambda I)$  |
| **Otherwise** |  $g(\lambda) = -\infty$  |
| **Domain** |  $\{ \lambda \geq 0 : A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \}$  |

* * *

✅ Next up:  
**1.5–1.6** — we’ll finalize the derivation of the dual expression, and explain in detail **what the range constraint means**, including via eigenbasis analysis.

Would you like to proceed to that?

## Response:
Let’s now give the **deepest possible unpacking** of the **dual function**  $g(\lambda)$ , explaining:

*   Where it comes from (derivation recap),
*   What it means algebraically and geometrically,
*   What happens in edge cases (singular matrices, pseudoinverse),
*   Why it’s concave,
*   And how to interpret it via **eigenvalues**, **directions**, and **penalized descent**.

This is the **central object** of the dual problem — and understanding it in full depth explains why a **nonconvex primal** can yield an **exact convex dual**.

* * *

🚩 GOAL: Understand the dual function
=====================================

We’re given the primal problem:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n} \quad & x^T A x + 2b^T x \\ \text{subject to} \quad & x^T x \leq 1 \end{aligned} \tag{P}
$$

We form the **Lagrangian**:

$$
L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda
$$

And define the **dual function**:

$$
g(\lambda) := \inf_{x \in \mathbb{R}^n} L(x, \lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T (A + \lambda I) x + 2b^T x - \lambda \right)
$$

Our task is to **fully understand** this function: what it looks like, when it’s finite, how to compute it, and how to interpret it.

* * *

✅ 1. Understanding the Structure of  $g(\lambda)$ 
==================================================

Let’s write:

*    $Q := A + \lambda I$ , so the dual function becomes:
    
$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T Q x + 2b^T x - \lambda \right)
$$

This is a **quadratic optimization problem** in  $x$ , unconstrained.

It is of the form:

$$
f(x) = x^T Q x + 2b^T x + c
$$

where:

*    $Q = A + \lambda I \in \mathbb{S}^n$ 
*    $b \in \mathbb{R}^n$ 
*    $c = -\lambda$ 

* * *

🚨 Key Question: Is this function bounded below?
------------------------------------------------

That depends on  $Q$ :

### Case 1:  $Q \succ 0$  (positive definite)

*   The quadratic form  $x^T Q x \to \infty$  as  $\|x\| \to \infty$ 
*   So  $f(x)$  has a unique minimizer

You can complete the square:

$$
x^T Q x + 2b^T x = (x + Q^{-1} b)^T Q (x + Q^{-1} b) - b^T Q^{-1} b
$$

Then:

$$
g(\lambda) = -b^T Q^{-1} b - \lambda
$$

This is finite and differentiable.

* * *

### Case 2:  $Q \succeq 0$  but **singular**

*   Then  $Q$  has **zero eigenvalues**
*   So  $x^T Q x$  is flat along certain directions (i.e., does not grow)
*   Whether  $f(x)$  is bounded below depends on the **linear term**  $2b^T x$ 

Let’s write first-order condition:

$$
\nabla_x L(x, \lambda) = 2Q x + 2b = 0
$$

This has a solution if and only if:

$$
b \in \mathcal{R}(Q)
$$

Then the minimizer is:

$$
x^\star = -Q^\dagger b + z, \quad \text{for any } z \in \ker(Q)
$$

Then the infimum is finite and given by:

$$
g(\lambda) = -b^T Q^\dagger b - \lambda
$$

* * *

### Case 3:  $Q$  **not** PSD

*   Then there exists a direction  $v \in \mathbb{R}^n$  such that  $v^T Q v < 0$ 
*   Then you can drive  $f(x) \to -\infty$  along the ray  $x = \alpha v$ 
*   So the infimum is unbounded below

Hence:

$$
g(\lambda) = -\infty
$$

* * *

✅ 2. Algebraic Summary: Exact Form of  $g(\lambda)$ 
====================================================

$$
\boxed{ g(\lambda) = \begin{cases} - b^T (A + \lambda I)^{-1} b - \lambda & \text{if } A + \lambda I \succ 0 \\ - b^T (A + \lambda I)^\dagger b - \lambda & \text{if } A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \\ -\infty & \text{otherwise} \end{cases} }
$$

Where:

*    $\dagger$  = Moore–Penrose pseudoinverse
*    $\mathcal{R}(\cdot)$  = range (column space)

* * *

✅ 3. Interpretation of the Dual Function
========================================

### 🔹 What is  $g(\lambda)$  doing?

It gives the **best lower bound** on the primal objective we can get by penalizing the constraint  $x^T x \leq 1$  with multiplier  $\lambda \geq 0$ .

That is:

*   We allow ourselves to ignore the constraint, but penalize violations via  $\lambda(x^T x - 1)$ 
*   We then ask: what is the best lower bound we can get by adjusting this penalty?

So  $g(\lambda)$  is a **lower bound** on the optimal value of the primal.

Later, we’ll **maximize**  $g(\lambda)$  over all  $\lambda \geq 0$ .

* * *

### 🔹 What does each term mean?

If  $A + \lambda I \succ 0$ , then:

$$
g(\lambda) = -b^T (A + \lambda I)^{-1} b - \lambda
$$

Let’s dissect:

*    $b^T (A + \lambda I)^{-1} b$ : quadratic form that measures how much **b aligns with the "curved directions"** of  $A + \lambda I$ 
*    $-\lambda$ : constant term coming from the Lagrange penalty
*   Overall: tradeoff between **flattening the quadratic** and **paying more penalty**

* * *

### 🔹 Why is it concave?

For any Lagrangian dual:

> The dual function  $g(\lambda)$  is always **concave**, even if the primal is nonconvex.

Reason:

*   It is a **pointwise infimum** of a family of **affine functions** of  $\lambda$ 
*   Convexity of the epigraph is preserved

So:

*    $g(\lambda)$  is a **concave function on  $\mathbb{R}_+$ **,
*   Possibly taking value  $-\infty$  outside its domain

* * *

✅ 4. Eigenvalue Interpretation
==============================

Let’s now **diagonalize**  $A$  to get spectral intuition.

Let:

$$
A = U \Lambda U^T, \quad \text{where } U \in \mathbb{R}^{n \times n} \text{ orthogonal},\ \Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)
$$

Then:

$$
A + \lambda I = U (\Lambda + \lambda I) U^T
$$

So the eigenvalues of  $A + \lambda I$  are:

$$
\lambda_i^{(A+\lambda I)} = \lambda_i^{(A)} + \lambda
$$

So to ensure  $A + \lambda I \succeq 0$ , we need:

$$
\lambda \geq -\lambda_{\min}(A)
$$

* * *

### 🔹 Diagonalizing the problem

Let  $z = U^T x$ ,  $\tilde{b} = U^T b$ 

Then:

$$
x^T (A + \lambda I) x = z^T (\Lambda + \lambda I) z = \sum_{i=1}^n (\lambda_i + \lambda) z_i^2
$$
 
$$
2b^T x = 2 \tilde{b}^T z = 2 \sum_{i=1}^n \tilde{b}_i z_i
$$

So the minimization becomes **separable**:

$$
g(\lambda) = \sum_{i=1}^n \inf_{z_i \in \mathbb{R}} \left( (\lambda_i + \lambda) z_i^2 + 2 \tilde{b}_i z_i \right) - \lambda
$$

Each term is minimized as:

$$
\inf_{z_i} \left( (\lambda_i + \lambda) z_i^2 + 2 \tilde{b}_i z_i \right) = \begin{cases} - \dfrac{\tilde{b}_i^2}{\lambda_i + \lambda} & \text{if } \lambda_i + \lambda > 0 \\ - \infty & \text{if } \lambda_i + \lambda < 0 \end{cases}
$$

So:

$$
g(\lambda) = - \sum_{i=1}^n \dfrac{\tilde{b}_i^2}{\lambda_i + \lambda} - \lambda
$$

if all denominators are positive.

* * *

✅ 5. Dual Function: Summary
===========================

### 💡 Dual function:

$$
g(\lambda) = \inf_x \left( x^T (A + \lambda I) x + 2b^T x - \lambda \right)
$$

### 🧾 Closed-form:

$$
\boxed{ g(\lambda) = \begin{cases} - b^T (A + \lambda I)^{-1} b - \lambda & \text{if } A + \lambda I \succ 0 \\ - b^T (A + \lambda I)^\dagger b - \lambda & \text{if } A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \\ -\infty & \text{otherwise} \end{cases} }
$$

### 🧠 Interpretation:

| Term | Meaning |
| --- | --- |
|  $A + \lambda I$  | Penalized curvature: dual modifies the primal's curvature |
|  $b^T Q^{-1} b$  | How the gradient “aligns” with directions of curvature |
|  $-\lambda$  | Dual cost of imposing constraint penalty |
| Finite only when |  $A + \lambda I \succeq 0$  and  $b \in \mathcal{R}(A + \lambda I)$  |
| Concave? | ✅ Always concave (even if primal is nonconvex) |
| Domain | A convex ray on  $\lambda \geq 0$ , often starting from  $\lambda = -\lambda_{\min}(A)$  |

* * *

✅ Let me know if you'd like to now proceed to:

*   **1.5** — Spectral form of the dual
*   **1.6** — Meaning and role of the range constraint  $b \in \mathcal{R}(A + \lambda I)$ 

These will finalize the dual and transition us to the **dual problem optimization**.

## Response:
Let’s now **unpack the concept of the dual function** itself — not just for this problem, but **in general**, from **first principles** and with complete rigor.

* * *

📌 WHAT IS THE DUAL FUNCTION?
=============================

The **dual function** is a fundamental object in optimization theory — it arises naturally from the **Lagrangian** and serves as a **tool for obtaining lower bounds** on a constrained minimization problem.

To fully understand it, we’ll walk through:

* * *

✅ Table of Contents
-------------------

1.  **Recap: the primal optimization problem**
2.  **Lagrangian: combining objective + constraints**
3.  **Dual function: definition**
4.  **Interpretation: what does the dual function mean?**
5.  **When is the dual function finite?**
6.  **Concavity of the dual function**
7.  **Role in duality: why it matters**

* * *

✅ 1. The Primal Optimization Problem
====================================

We start with a general form of an optimization problem:

$$
\begin{aligned} \text{minimize}_{x \in \mathbb{R}^n} \quad & f_0(x) \\ \text{subject to} \quad & f_i(x) \leq 0 \quad \text{for } i = 1, \dots, m \\ & h_j(x) = 0 \quad \text{for } j = 1, \dots, p \end{aligned} \tag{P}
$$

Where:

*    $f_0(x)$ : objective function (we want to minimize this)
*    $f_i(x)$ : inequality constraint functions
*    $h_j(x)$ : equality constraint functions

Let the **feasible set** be:

$$
\mathcal{F} := \left\{ x \in \mathbb{R}^n \mid f_i(x) \leq 0,\ h_j(x) = 0 \right\}
$$

The **primal optimal value** is:

$$
p^\star := \inf_{x \in \mathcal{F}} f_0(x)
$$

We are trying to find the best (smallest) value of the objective that satisfies all the constraints.

* * *

✅ 2. The Lagrangian
===================

The **Lagrangian** is a scalar function that incorporates all the constraints into the objective using multipliers.

$$
L(x, \lambda, \nu) := f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

Where:

*    $\lambda \in \mathbb{R}^m$ : multipliers for inequality constraints (called **dual variables**)
*    $\nu \in \mathbb{R}^p$ : multipliers for equality constraints

**Domain condition**:

*   For the Lagrangian to be meaningful, we require  $\lambda \geq 0$ , i.e., each  $\lambda_i \geq 0$ .
*   Otherwise, the constraint penalty  $\lambda_i f_i(x)$  might reward violations.

* * *

✅ 3. Definition of the Dual Function
====================================

The **dual function** is the infimum of the Lagrangian over all primal variables  $x$ :

$$
\boxed{ g(\lambda, \nu) := \inf_{x \in \mathbb{R}^n} L(x, \lambda, \nu) }
$$

This is a function of  $(\lambda, \nu)$  — the dual variables — and **not** of  $x$  anymore.

It is defined **for all**  $(\lambda, \nu)$  such that the infimum is well-defined (possibly  $-\infty$ ).

* * *

✅ 4. What Does the Dual Function Mean?
======================================

### 🔹 Interpretation: **Best lower bound**

For **any**  $\lambda \geq 0, \nu \in \mathbb{R}^p$ , and **any feasible point  $x \in \mathcal{F}$ **, we have:

$$
L(x, \lambda, \nu) \leq f_0(x)
$$

because:

*    $f_i(x) \leq 0$ , so  $\lambda_i f_i(x) \leq 0$  (since  $\lambda_i \geq 0$ )
*    $h_j(x) = 0$ , so  $\nu_j h_j(x) = 0$ 

Hence:

$$
L(x, \lambda, \nu) \leq f_0(x) \quad \text{for all feasible } x
$$

Taking infimum over all  $x \in \mathbb{R}^n$ , we get:

$$
\boxed{ g(\lambda, \nu) \leq p^\star }
$$

This means:

> The dual function always gives a **lower bound** on the optimal value of the primal.

* * *

### 🔸 Visual Intuition

*   Think of the dual function as a **penalized version of the objective**.
*   Instead of minimizing  $f_0(x)$  subject to hard constraints, we minimize an **unconstrained Lagrangian**.
*   The constraints are encoded via **soft penalties** controlled by  $\lambda, \nu$ .
*   For each pair  $(\lambda, \nu)$ , we get one lower bound.
*   The goal is to find the **tightest possible** such lower bound.

That’s what leads to the **dual problem**.

* * *

✅ 5. When Is  $g(\lambda, \nu)$  Finite?
========================================

The infimum:

$$
g(\lambda, \nu) = \inf_x \left[ f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right]
$$

may not always be finite. There are three cases:

* * *

### Case 1: Bounded below

If the function inside the infimum has a minimum at some  $x^\star$ , then  $g(\lambda, \nu) \in \mathbb{R}$ 

* * *

### Case 2: Unbounded below

If the Lagrangian goes to  $-\infty$  in some direction (e.g., due to negative curvature), then:

$$
g(\lambda, \nu) = -\infty
$$

* * *

### Case 3: Infeasible or not well-defined

If some part of the Lagrangian is ill-defined (e.g., domain issues), the dual function may be undefined or infinite.

* * *

✅ 6. Why Is the Dual Function Always Concave?
=============================================

Regardless of whether the primal is convex, the dual function  $g(\lambda, \nu)$  is always **concave** in  $(\lambda, \nu)$ .

* * *

### 🔹 Reason:

The dual function is a **pointwise infimum over affine functions** of  $(\lambda, \nu)$ :

$$
g(\lambda, \nu) = \inf_x \left[ f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right]
$$
*   For each  $x$ , the function inside is affine in  $(\lambda, \nu)$ 
*   The infimum over affine functions is concave

🧠 This is a standard convex analysis result:

*   Pointwise infimum of affine functions ⇒ concave function

* * *

### 🔸 Meaning:

*   Even if the primal is **nonconvex**, the dual function is **always concave**
*   So the dual problem (maximize  $g$ ) is a **convex optimization problem**

This is why duality is powerful — it gives you a **convex handle** on potentially nonconvex problems.

* * *

✅ 7. What Happens Next? The Dual Problem
========================================

Once we have the dual function  $g(\lambda, \nu)$ , we define the **dual optimization problem**:

$$
\begin{aligned} \text{maximize}_{\lambda, \nu} \quad & g(\lambda, \nu) \\ \text{subject to} \quad & \lambda \geq 0 \end{aligned} \tag{D}
$$

This is the **Lagrange dual problem** of the original primal problem.

The optimal value of the dual is denoted:

$$
d^\star := \sup_{\lambda \geq 0, \nu} g(\lambda, \nu)
$$

We always have:

$$
d^\star \leq p^\star
$$

This is called **weak duality**.

* * *

✅ When does equality hold?
--------------------------

*   If  $p^\star = d^\star$ , then we say **strong duality** holds.
*   This is guaranteed in many cases:
    *   If the primal is convex and satisfies **Slater’s condition** (strict feasibility),
    *   Or if the problem has special structure (e.g., trust-region QCQP)

* * *

🔄 Analogy: Penalty vs Constraint
=================================

You can think of the dual function as exploring:

> "What happens if instead of strictly enforcing the constraint, I penalize it — and how strong should the penalty be to get the tightest lower bound?"

* * *

✅ Dual Function: Summary Table
==============================

| Feature | Description |
| --- | --- |
| **Definition** |  $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$  |
| **Lagrangian** | Combines objective + constraints via multipliers |
| **Lower bound** |  $g(\lambda, \nu) \leq f_0(x)$  for all feasible  $x$  |
| **Always concave** | Pointwise infimum over affine functions |
| **Finite when** | Lagrangian is bounded below (depends on  $x$ ) |
| **Used in dual problem** |  $\max_{\lambda \geq 0, \nu} g(\lambda, \nu)$  |
| **Dual optimal value** |  $d^\star \leq p^\star$  (equality = strong duality) |

* * *

✅ Final Takeaways
=================

*   The **dual function** is the **best lower bound** you can get on the primal objective by penalizing constraint violation.
*   It is **built from the Lagrangian** by minimizing out the primal variable.
*   It is **concave**, even if the primal is not.
*   Its role is to help you understand and bound the primal problem from below.
*   It becomes a **powerful optimization object** when strong duality holds — especially in convex problems or special cases like trust-region QCQP.

* * *

Would you like to now go back to the **specific trust-region dual function** and interpret it in the context of this general theory? Or proceed to **1.5–1.6**, where we express it in **eigenbasis form** and analyze the **range condition**?

## Response:
Perfect. Let's now go **even deeper, more detailed, and granular**, and treat this as a **complete newcomer walkthrough** to the **dual function**, starting from zero.

* * *

📚 TOTAL UNPACKING: The Dual Function — From First Principles
=============================================================

This is a **foundational object** in optimization theory. You’ll see it in:

*   Convex optimization,
*   Lagrangian duality,
*   Game theory,
*   Machine learning (SVMs, Lasso),
*   Economics (prices = dual variables),
*   Robust optimization, and more.

We’re going to **unpack the dual function from scratch**, explain every term and idea rigorously, and build complete intuition — algebraic, geometric, optimization-theoretic.

* * *

🧭 ROADMAP for This Walkthrough
-------------------------------

| Step | Topic |
| --- | --- |
| 0 | Motivation: What problem are we trying to solve? |
| 1 | The primal problem: constraints and objective |
| 2 | Lagrangian: turning constraints into penalties |
| 3 | Definition of the dual function |
| 4 | Why the dual function always gives a lower bound |
| 5 | Infimum over  $x$ : how to compute the dual function |
| 6 | Examples: linear and quadratic cases |
| 7 | When is the dual function finite? |
| 8 | Concavity: why it’s always concave |
| 9 | What happens next: the dual problem |
| 10 | Why the dual function is a gift — summary and deep insight |

* * *

🔰 STEP 0: Motivation — Why Are We Doing This?
----------------------------------------------

You’re trying to solve a constrained minimization problem:

> Minimize a cost function  $f(x)$ , but only over values  $x$  that obey some **inequality** and/or **equality constraints**.

Examples:

*   **Engineering**: minimize energy subject to system constraints
*   **Machine learning**: minimize loss under regularization
*   **Economics**: maximize utility subject to budget constraints
*   **Control**: minimize error subject to physical limits

These are **constrained optimization** problems. They are hard.

The **dual function** is a way to **analyze and sometimes even solve** such problems — by constructing a new, related function that is **easier**, and gives you a **lower bound** on the solution.

* * *

✅ STEP 1: The Primal Problem
----------------------------

We start with a general constrained problem:

$$
\begin{aligned} \text{minimize}_{x \in \mathbb{R}^n} \quad & f_0(x) \\ \text{subject to} \quad & f_i(x) \leq 0, \quad i=1,\dots,m \\ & h_j(x) = 0, \quad j=1,\dots,p \end{aligned}
$$

Let’s name things:

*    $f_0(x)$ : the **objective** — what you want to minimize.
*    $f_i(x) \leq 0$ : **inequality constraints** (e.g., capacity, budget, norm bounds).
*    $h_j(x) = 0$ : **equality constraints** (e.g., equations of motion, exact matches).

The **feasible set** is all the points  $x$  that satisfy all constraints.

$$
\mathcal{F} := \left\{ x \in \mathbb{R}^n \ \middle|\ f_i(x) \leq 0,\ h_j(x) = 0 \right\}
$$

The **goal**: find the best (smallest) value of  $f_0(x)$  over  $\mathcal{F}$ :

$$
p^\star := \inf_{x \in \mathcal{F}} f_0(x)
$$

This is called the **primal optimal value**.

* * *

✅ STEP 2: The Lagrangian — Turning Constraints Into Penalties
-------------------------------------------------------------

### Problem: Constraints are annoying.

*   They make optimization harder.
*   They create complicated feasible regions.

**Solution**: **Incorporate the constraints into the objective**, using **Lagrange multipliers**.

We define the **Lagrangian function**:

$$
L(x, \lambda, \nu) := f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

Where:

*    $\lambda_i$  are the multipliers for **inequality constraints**
*    $\nu_j$  are the multipliers for **equality constraints**
*   These are **extra variables** — they live in the "dual" world.

🧠 Think of:

*    $\lambda_i$  as how much we are willing to **penalize** violation of constraint  $f_i(x) \leq 0$ 
*    $\nu_j$  as enforcing equality constraints via **soft pressure**

* * *

✅ STEP 3: Definition of the Dual Function
-----------------------------------------

Now we define the **dual function**:

$$
\boxed{ g(\lambda, \nu) := \inf_{x \in \mathbb{R}^n} L(x, \lambda, \nu) }
$$

Let’s explain this slowly.

You fix some values of  $(\lambda, \nu)$  — i.e., you **pick how much to penalize** each constraint.

Then you minimize the resulting **Lagrangian**, which is now **unconstrained** (no more constraints! Just penalized terms).

So for each choice of  $(\lambda, \nu)$ , the dual function gives a **number** — the smallest value you can get when trading off:

*   the original cost  $f_0(x)$ 
*   the penalties for constraint violations

* * *

### What kind of function is this?

*   **Input**:  $(\lambda, \nu)$  ∈  $\mathbb{R}^m_+ \times \mathbb{R}^p$ 
*   **Output**: scalar (possibly  $-\infty$ )

🧠 Think of the dual function as a way to:

*   explore different **"penalized versions"** of your problem,
*   and find how low you can go for each set of penalties.

* * *

✅ STEP 4: Why Is  $g(\lambda, \nu) \leq p^\star$ ?
--------------------------------------------------

Let’s show this fundamental property:

> The dual function always gives a **lower bound** on the optimal value of the primal.

Let  $x \in \mathcal{F}$  be any feasible point. Then:

*    $f_i(x) \leq 0$ , and  $\lambda_i \geq 0$  ⇒  $\lambda_i f_i(x) \leq 0$ 
*    $h_j(x) = 0$  ⇒  $\nu_j h_j(x) = 0$ 

So:

$$
L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \leq f_0(x)
$$

Then:

$$
g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) \leq L(x, \lambda, \nu) \leq f_0(x)
$$

Since this is true for **any feasible  $x$ **, we conclude:

$$
\boxed{g(\lambda, \nu) \leq p^\star}
$$

This is called **weak duality**.

* * *

✅ STEP 5: Infimum Over  $x$  — How Is  $g$  Computed?
-----------------------------------------------------

The expression:

$$
g(\lambda, \nu) = \inf_x \left[ f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \right]
$$

is just an **unconstrained minimization problem** over  $x$ . Depending on the form of the functions:

*   It might be solvable in closed form (e.g., if quadratic)
*   It might be convex, or not
*   It might go to  $-\infty$ 

So:

*   If  $L(x, \lambda, \nu)$  is **bounded below**, the dual function is finite
*   If not, then  $g(\lambda, \nu) = -\infty$ 

* * *

✅ STEP 6: Example — Simple Quadratic Case
-----------------------------------------

Let’s say:

*    $f_0(x) = x^2$ 
*    $f_1(x) = x - 1 \leq 0$ 

Then the primal is:

$$
\min_x x^2 \quad \text{s.t. } x - 1 \leq 0
$$

✅ The optimal is at  $x = 0$ , value  $0$ 

Now compute the Lagrangian:

$$
L(x, \lambda) = x^2 + \lambda(x - 1)
$$

Dual function:

$$
g(\lambda) = \inf_x \left[ x^2 + \lambda x - \lambda \right]
$$

Complete the square:

$$
= \inf_x \left[ \left(x + \frac{\lambda}{2} \right)^2 - \frac{\lambda^2}{4} - \lambda \right] = - \frac{\lambda^2}{4} - \lambda
$$

So:

$$
g(\lambda) = -\frac{\lambda^2}{4} - \lambda, \quad \text{valid for } \lambda \geq 0
$$

This is a concave function.

We then **maximize**  $g(\lambda)$ , which gives us the **dual optimal value** — a lower bound on the primal.

✅ In this case, the dual optimal value is also 0 (attained at  $\lambda = 2$ )

* * *

✅ STEP 7: When Is the Dual Function Finite?
-------------------------------------------

The dual function is finite only if the **infimum over  $x$ ** does **not go to  $-\infty$ **.

This depends on:

*   The structure of the Lagrangian
*   Whether the **quadratic terms** are bounded below
*   Whether the **penalties** grow fast enough to prevent collapse

This is why we impose conditions like:

*    $A + \lambda I \succeq 0$ 
*    $b \in \mathcal{R}(A + \lambda I)$ 

Otherwise,  $L(x, \lambda) \to -\infty$  in some direction.

* * *

✅ STEP 8: Why Is the Dual Function Always Concave?
--------------------------------------------------

Even if the primal is nonconvex, the dual function is always:

$$
\boxed{\text{concave in } (\lambda, \nu)}
$$

Why?

Because  $L(x, \lambda, \nu)$  is **affine** in  $(\lambda, \nu)$  for each  $x$ , and:

> The pointwise infimum of affine functions is concave.

This is a deep fact from convex analysis:

*   Affine + inf = concave
*   Even if each function is **not convex in  $x$ **

So even for **nonconvex primal problems**, the dual function is **always concave**.

* * *

✅ STEP 9: What Happens Next? The Dual Problem
---------------------------------------------

Now we **optimize over  $\lambda, \nu$ **:

$$
\begin{aligned} \text{maximize}_{\lambda \geq 0, \nu} \quad & g(\lambda, \nu) \end{aligned}
$$

This is called the **dual problem**.

Let the **dual optimal value** be  $d^\star$ . Then:

$$
\boxed{d^\star := \sup_{\lambda \geq 0, \nu} g(\lambda, \nu) \leq p^\star}
$$

So the dual gives us the **best possible lower bound** on the primal — via a convex problem.

* * *

✅ STEP 10: Why the Dual Function Is a Gift
------------------------------------------

Let’s pause.

Even when the original problem is **nonconvex**, ugly, or constrained in complex ways:

*   The dual function gives a **family of guaranteed lower bounds**
*   It is always **concave**, always well-behaved
*   It can sometimes recover the exact solution
*   Its structure helps us understand when constraints are **tight** (via KKT)
*   It shows up in **machine learning**, **economics**, **numerical algorithms**, **control**

It is one of the most **profound constructs** in modern optimization theory.

* * *

✅ TL;DR: Dual Function Deep Summary
-----------------------------------

| Concept | What It Means |
| --- | --- |
| **Definition** |  $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$  |
| **Lagrangian** | Adds constraints as penalties |
| **Always ≤ primal** | Lower bound for every  $\lambda \geq 0$  |
| **When finite** | Only if the Lagrangian is bounded below |
| **Concave** | Always concave in  $(\lambda, \nu)$  |
| **Used for** | Constructing dual problem (maximize  $g$ ) |
| **Dual optimal value** |  $d^\star := \sup g(\lambda, \nu) \leq p^\star$  |
| **Equality?** | Strong duality holds under Slater’s condition |
| **Why powerful** | Turns a messy problem into a structured convex one |

* * *

Would you now like to return to our **trust-region example**, and interpret **that specific dual function** using this general framework?

Or continue with the next step: **1.5–1.6**, where we express the dual in **eigenbasis form** and interpret the **range constraint**  $b \in \mathcal{R}(A + \lambda I)$ ?

## Response:
Fantastic question — and the short answer is:

> **No. The dual function is _not_ the same thing as the Lagrangian.**
> 
> But the dual function is _built from_ the Lagrangian — specifically, it is the **infimum** of the Lagrangian over the primal variable  $x$ .

Let’s unpack this slowly and precisely, to clarify the relationship.

* * *

🔍 Key Difference: Lagrangian vs. Dual Function
-----------------------------------------------

| Concept | Depends on | Purpose | What it is |
| --- | --- | --- | --- |
| **Lagrangian**  $L(x, \lambda, \nu)$  |  $x, \lambda, \nu$  | Combines objective + constraints | A scalar function of both **primal** and **dual** variables |
| **Dual function**  $g(\lambda, \nu)$  |  $\lambda, \nu$  only | Gives lower bounds on the primal | The **infimum** of the Lagrangian over  $x$ :  $\inf_x L(x, \lambda, \nu)$  |

* * *

🧩 More Precisely:
------------------

### 🟦 The **Lagrangian** is:

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$
*   It is a **function of all three**:
    *    $x$ : the **primal variable** (what you're optimizing over)
    *    $\lambda$ : multipliers for inequality constraints
    *    $\nu$ : multipliers for equality constraints

Think of it as the **engine** of the duality theory. It creates a new function whose structure merges objective + constraints.

* * *

### 🟨 The **dual function** is:

$$
g(\lambda, \nu) := \inf_{x \in \mathbb{R}^n} L(x, \lambda, \nu)
$$

So:

*   You **fix** the multipliers  $\lambda, \nu$ ,
*   Then you **minimize** the Lagrangian **over  $x$ **.

✅ This makes  $g(\lambda, \nu)$  a function of the **dual variables only**.

* * *

🔁 Analogy:
-----------

Imagine the Lagrangian as a **machine**:

> Input:  $x$ , and dual weights  $\lambda, \nu$   
> Output: a scalar number = total penalized objective

Now imagine the dual function as what you get when you:

> Keep the dual weights fixed  
> And ask: _what is the smallest possible output this machine can give me as I try all possible  $x$ ?_

That **minimal output** is  $g(\lambda, \nu)$ .

* * *

💡 Intuition
------------

### Lagrangian:

*   A raw, general-purpose object.
*   Not optimized — just combines all data.

### Dual function:

*   The **best achievable value** of the Lagrangian for fixed penalties.
*   Tells us how much we can **lower the cost** while staying within penalized constraints.

* * *

📌 Summary
----------

| Lagrangian | Dual Function |
| --- | --- |
|  $L(x, \lambda, \nu)$  |  $g(\lambda, \nu) := \inf_x L(x, \lambda, \nu)$  |
| Function of  $x, \lambda, \nu$  | Function of  $\lambda, \nu$  only |
| Combines objective + constraints | Lower bound on the constrained problem |
| Appears in KKT conditions | Appears in the dual problem |
| Used to define suboptimality | Used to derive dual problem |
| Not convex/concave in general | Always **concave** (even if primal isn't convex) |

* * *

📣 Bottom Line:
---------------

> The **dual function is not the same as the Lagrangian**, but it is **defined using the Lagrangian**, by minimizing over  $x$ .

So:

*   Lagrangian = raw blueprint (takes  $x$ )
*   Dual function = lowest possible value of that blueprint when optimizing  $x$  (only takes  $\lambda, \nu$ )

Would you like a visual diagram or metaphor to help reinforce this even more clearly?

## Response:
Exactly — your intuition is excellent, and you're circling around a **key conceptual shift** between:

*   the **primal problem**, where we minimize over  $x$  subject to constraints,
*   the **Lagrangian**, which combines constraints into the objective using dual weights (multipliers),
*   and the **dual function**, where we fix the dual weights  $(\lambda, \nu)$ , and **minimize over  $x$  only**, to evaluate the tightest lower bound we can get from those weights.

Let’s now walk through this transition **in deep detail**, from your exact question:

* * *

🔁 “Why do we fix the dual variables and minimize only over  $x$ ?”
===================================================================

🔷 Let's start from the Lagrangian:
-----------------------------------

$$
L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x)
$$
*   This function has **3 types of variables**:
    *    $x$ : primal variable — what we ultimately care about
    *    $\lambda$ : inequality constraint weights (dual variables)
    *    $\nu$ : equality constraint weights (dual variables)

* * *

🧠 Core idea of duality:
------------------------

> Instead of solving the constrained problem directly, try solving a related **unconstrained** problem where you penalize the constraints using  $\lambda, \nu$ .

That’s what the **Lagrangian** does:  
It **softens the constraints** and lets you "pay a price" for violating them.

* * *

🟨 But what’s the dual function?
--------------------------------

Now suppose you **fix** the constraint weights  $\lambda, \nu$ .  
You ask:

> _If I charge myself penalties  $(\lambda, \nu)$  for constraint violations, what’s the **best possible** value I can get for the Lagrangian?_

That is:

$$
g(\lambda, \nu) = \inf_{x} L(x, \lambda, \nu)
$$

✅ So the dual function **minimizes only over  $x$ **.

It **does not** minimize over  $\lambda, \nu$  — those are fixed **inputs** to the function.

Instead, the **dual problem** is:

> Maximize  $g(\lambda, \nu)$  over all feasible dual weights:

$$
\begin{aligned} \text{maximize}_{\lambda \geq 0,\ \nu} \quad & g(\lambda, \nu) \end{aligned}
$$

So the process is:

1.  For each choice of  $\lambda, \nu$ , compute  $g(\lambda, \nu)$  by minimizing over  $x$ 
2.  Then find the best possible such lower bound (i.e., take the **supremum** over  $\lambda, \nu$ )

* * *

📐 Geometric Interpretation
---------------------------

You can visualize this as a two-stage process:

### 🎯 Step 1 (Inner minimization):

Fix  $\lambda, \nu$ . Then:

*   The Lagrangian is a function of  $x$ 
*   You minimize it over all  $x$  (no constraints!)
*   The result is a number: the **lowest penalized cost**

This is  $g(\lambda, \nu)$ 

### 🎯 Step 2 (Outer maximization):

Now vary  $\lambda, \nu$ 

*   Each choice gives a different lower bound
*   You try to find the **tightest lower bound** — i.e., the largest value of  $g(\lambda, \nu)$ 

That’s the dual problem.

* * *

🔁 Compare to Primal Problem
----------------------------

| Primal | Dual |
| --- | --- |
| Minimize  $f_0(x)$  | Maximize  $g(\lambda, \nu)$  |
| Subject to constraints on  $x$  | Subject to  $\lambda \geq 0$  |
| Optimize over  $x$  | Optimize over  $\lambda, \nu$  |
| Hard constraints  $f_i(x) \leq 0$  | Soft penalization inside Lagrangian |

* * *

✅ Summary
---------

> In the **dual function**  $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$ , we are **fixing** the constraint weights  $(\lambda, \nu)$ , and asking:
> 
> “What’s the **minimum** value of the Lagrangian I can get if I were penalized using these weights?”

So:

*   Yes, you are absolutely right.
*   In the **dual function**, we **minimize over  $x$ ** for each fixed  $(\lambda, \nu)$ 
*   Then in the **dual problem**, we **maximize over  $(\lambda, \nu)$ ** to get the tightest lower bound

* * *

Would you like to walk through an **illustrated example** of this two-stage process with explicit values of  $x, \lambda, \nu$ ? Or continue with the trust-region problem’s dual?

## Response:
Perfect — let’s **resume our deep walkthrough of the trust-region problem**, picking up right where we left off: the **Lagrangian** and its properties.

We already previewed these in earlier steps, but now we’ll deliver them again with even more **mathematical depth**, **granularity**, and **newcomer-friendly clarity** — as requested.

* * *

🔁 RECAP: The Primal Problem
============================

We are studying the **trust-region subproblem**, which is a **nonconvex QCQP** (quadratically constrained quadratic program):

$$
\begin{aligned} \min_{x \in \mathbb{R}^n} \quad & f(x) := x^T A x + 2b^T x \\ \text{s.t.} \quad & x^T x \leq 1 \end{aligned} \tag{P}
$$
*    $A \in \mathbb{S}^n$  (i.e., symmetric matrix)
*    $b \in \mathbb{R}^n$ 
*   The constraint  $x^T x \leq 1$  defines the **unit ball**

This is a special case of a **quadratic objective + quadratic constraint**, where the constraint is convex but the objective **might not be**.

* * *

✅ Step 1.1 — Construct the Lagrangian
=====================================

We’re now building the **Lagrangian** function that encodes both:

*   the **objective**  $f(x) = x^T A x + 2b^T x$ 
*   and the **constraint**  $x^T x \leq 1$ 

into a **single unconstrained function**  $L(x, \lambda)$ .

* * *

🔸 Step-by-step construction
----------------------------

We have **one** inequality constraint:

$$
f_1(x) := x^T x - 1 \leq 0
$$

We introduce one **dual variable**  $\lambda \geq 0$  to represent this constraint. (Why nonnegative? We’ll get to that in 1.2.)

So the Lagrangian is:

$$
L(x, \lambda) = f(x) + \lambda \cdot f_1(x) = x^T A x + 2b^T x + \lambda(x^T x - 1)
$$

* * *

🔸 Clean it up algebraically
----------------------------

Group terms:

$$
L(x, \lambda) = x^T A x + \lambda x^T x + 2b^T x - \lambda
$$
 
$$
\boxed{ L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda }
$$

This is the standard quadratic form of the Lagrangian.

* * *

🔸 Each term explained:
-----------------------

| Term | Meaning |
| --- | --- |
|  $x^T A x$  | Original quadratic cost |
|  $2b^T x$  | Linear cost term |
|  $\lambda x^T x$  | Penalization for how much  $x$  stretches beyond the unit ball |
|  $-\lambda$  | Constant offset (from  $-\lambda \cdot 1$ ) |

So this Lagrangian:

*   **modifies the curvature** of the objective via  $A + \lambda I$ 
*   and penalizes constraint violation softly (instead of enforcing  $\|x\| \leq 1$  strictly)

* * *

✅ Step 1.2 — Why Must  $\lambda \geq 0$ ?
=========================================

This is critical: the Lagrange multiplier  $\lambda$  associated with the inequality constraint **must be nonnegative**.

Let’s now unpack why.

* * *

🔸 Reason 1: KKT theory — Constraint penalties must not reward violations
-------------------------------------------------------------------------

We have an inequality constraint:

$$
f_1(x) = x^T x - 1 \leq 0
$$

In general, for **any** inequality constraint  $f_i(x) \leq 0$ , the Lagrange multiplier  $\lambda_i$  must satisfy:

$$
\lambda_i \geq 0
$$

Why?

Because in the Lagrangian:

$$
L(x, \lambda) = f_0(x) + \sum_i \lambda_i f_i(x)
$$

If  $\lambda_i < 0$ , then:

*   **Violating the constraint** (i.e.  $f_i(x) > 0$ ) actually **decreases the cost**
*   This means you are **rewarded** for constraint violation!

That breaks everything — especially duality theory.

* * *

🔸 Reason 2: Geometric meaning — Supporting hyperplanes
-------------------------------------------------------

In duality, the **Lagrange multipliers define a supporting hyperplane** to the feasible region:

*   For inequality constraints, these hyperplanes must support the **epigraph** or **feasible region from below**.
*   This only works if the multipliers are **nonnegative**

Negative multipliers produce **non-supporting hyperplanes** (i.e., they cut into the feasible region), which contradicts the basic geometric guarantees of duality.

* * *

🔸 Reason 3: Optimization logic
-------------------------------

Let’s look at the term:

$$
\lambda (x^T x - 1)
$$

If  $\lambda < 0$ , then minimizing  $L(x, \lambda)$  **encourages** making  $x^T x$  as large as possible — i.e., violating the constraint.

But the whole point of introducing  $\lambda$  is to **penalize** constraint violation.

So the sign must be:

*    $\lambda > 0$ : large norm is penalized
*    $\lambda = 0$ : constraint ignored
*    $\lambda < 0$ : large norm rewarded ⇒ **forbidden**

* * *

✅ Summary of 1.1–1.2
====================

| Concept | Explanation |
| --- | --- |
| **Lagrangian** |  $L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda$  |
| **Why we construct it** | Turns the constrained problem into an unconstrained function of  $x$ , parameterized by  $\lambda$  |
| **Why  $\lambda \geq 0$ ** | Ensures constraint violation is penalized, not rewarded; required by KKT conditions and geometry |
| **Next step** | Define the **dual function**: minimize this Lagrangian over all  $x \in \mathbb{R}^n$  |

* * *

Would you like to now proceed to **1.3–1.4**, where we define the **dual function** from this Lagrangian and derive its **domain of finiteness**? Or revisit any part of 1.1–1.2 in more depth (e.g., symbolic examples, perturbation view)?

## Response:
Excellent. Let’s now **deeply unpack Steps 1.3 and 1.4**:  
We’ll **define**, **compute**, and **analyze** the **dual function**  $g(\lambda)$ , and then **determine when it is finite**, i.e., when it does **not go to  $-\infty$ **.

* * *

🧩 Step 1.3 — Define and Compute the Dual Function  $g(\lambda)$ 
=================================================================

* * *

🔁 Recap from Step 1.1
----------------------

We previously constructed the **Lagrangian**:

$$
L(x, \lambda) = x^T (A + \lambda I) x + 2b^T x - \lambda
$$

We now define the **dual function** as:

$$
\boxed{ g(\lambda) := \inf_{x \in \mathbb{R}^n} L(x, \lambda) }
$$

This is a **function of  $\lambda$  only**. For each fixed  $\lambda \geq 0$ , the dual function gives us the **lowest value** the Lagrangian can take when we vary  $x$  freely.

This means:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T (A + \lambda I) x + 2b^T x - \lambda \right)
$$

Let’s define:

*    $Q := A + \lambda I$ 

Then:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T Q x + 2b^T x - \lambda \right)
$$

This is an **unconstrained quadratic minimization** problem in  $x$ .

* * *

📐 Strategy: Minimize a general quadratic function
--------------------------------------------------

We now minimize:

$$
f(x) = x^T Q x + 2b^T x
$$

This is a standard quadratic form:

*   The **gradient** is:  $\nabla f(x) = 2Qx + 2b$ 
*   Setting  $\nabla f(x) = 0$  gives the **stationary point**:
    $$
    Qx = -b
    $$

The solution and value depend on **whether  $Q$  is invertible** or not.

* * *

🧠 Case 1:  $Q \succ 0$  (positive definite)
--------------------------------------------

If  $Q = A + \lambda I$  is **positive definite**, then:

*   It is **invertible**
*   The minimum is achieved at:
    $$
    x^\star = -Q^{-1} b
    $$

Plug into the objective:

$$
f(x^\star) = ( -Q^{-1} b )^T Q ( -Q^{-1} b ) + 2b^T ( -Q^{-1} b ) = b^T Q^{-1} b - 2 b^T Q^{-1} b = - b^T Q^{-1} b
$$

Therefore:

$$
g(\lambda) = - b^T (A + \lambda I)^{-1} b - \lambda
$$

✅ So if  $A + \lambda I \succ 0$ , the dual function is **finite and closed-form computable**.

* * *

🧠 Case 2:  $Q = A + \lambda I \succeq 0$ , but **singular**
------------------------------------------------------------

This means:

*    $Q$  has **zero eigenvalues**
*   It is **not invertible**
*   But it is **still positive semidefinite**

In this case:

*   The gradient equation  $Qx + b = 0$  **only has a solution** if:
    
$$
\boxed{b \in \mathcal{R}(Q)}
$$

That is,  $b$  must lie in the **column space (range)** of  $Q$ .

If this holds:

*   We can solve for the minimum using the **Moore–Penrose pseudoinverse**:
    $$
    x^\star = -Q^\dagger b
    $$
*   The minimum value becomes:
    $$
    g(\lambda) = - b^T Q^\dagger b - \lambda
    $$

✅ So if  $A + \lambda I \succeq 0$  **and**  $b \in \mathcal{R}(A + \lambda I)$ , then  $g(\lambda)$  is finite.

* * *

🧨 Case 3:  $Q = A + \lambda I$  is **not PSD**
-----------------------------------------------

If  $Q$  has **negative eigenvalues**, then:

*   There exists a direction  $v \in \mathbb{R}^n$  such that:
    $$
    v^T Q v < 0
    $$
*   Along the ray  $x = \alpha v$ , we have:
    $$
    f(x) = \alpha^2 v^T Q v + 2\alpha b^T v
    $$
*   For large  $|\alpha|$ , this goes to  $-\infty$ 

So the Lagrangian is **unbounded below**, and:

$$
g(\lambda) = -\infty
$$

* * *

✅ Step 1.4 — Domain of the Dual Function (When Is It Finite?)
=============================================================

Let’s now summarize the exact conditions under which  $g(\lambda)$  is **finite**.

* * *

### 🔒 Condition 1: Positive semidefiniteness

We need:

$$
A + \lambda I \succeq 0
$$

This ensures that  $x^T Q x \geq 0$  for all  $x$ . Otherwise the infimum goes to  $-\infty$ .

* * *

### 🔒 Condition 2: Linear term solvability

We also need:

$$
b \in \mathcal{R}(A + \lambda I)
$$

Otherwise, the gradient equation  $Qx + b = 0$  has **no solution**, and the function drops to  $-\infty$  along directions of  $\ker(Q)$ .

* * *

🧰 Final Summary: Dual Function  $g(\lambda)$ 
----------------------------------------------

$$
\boxed{ g(\lambda) = \begin{cases} - b^T (A + \lambda I)^{-1} b - \lambda & \text{if } A + \lambda I \succ 0 \\ - b^T (A + \lambda I)^\dagger b - \lambda & \text{if } A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \\ -\infty & \text{otherwise} \end{cases} }
$$

* * *

🧭 Domain of  $g(\lambda)$ 
---------------------------

The domain is:

$$
\operatorname{dom}(g) = \left\{ \lambda \geq 0 \ \middle|\ A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \right\}
$$

This domain is:

*   Convex (intersection of PSD cone + affine space)
*   A **closed ray** from some  $\lambda_0$  upward

Usually, the smallest feasible  $\lambda$  is:

$$
\lambda_0 = - \lambda_{\min}(A)
$$

Assuming  $A$  has negative eigenvalues.

* * *

💡 Geometric Intuition
----------------------

You can think of  $\lambda$  as the **amount of curvature** you’re adding to make  $A + \lambda I$  positive semidefinite.

*   The dual function only makes sense if the Lagrangian is **bounded below**
*   That happens **only if  $\lambda$  flattens the objective enough**

* * *

✅ Summary of Steps 1.3–1.4
--------------------------

| Concept | Meaning |
| --- | --- |
| **Dual function** |  $g(\lambda) = \inf_x L(x, \lambda)$  |
| **Computed as** | Quadratic minimization over  $x \in \mathbb{R}^n$  |
| **Closed-form** |  $-b^T Q^{-1} b - \lambda$ , or pseudoinverse |
| **Domain** | All  $\lambda \geq 0$  s.t.  $A + \lambda I \succeq 0$  and  $b \in \mathcal{R}(A + \lambda I)$  |
| **Unbounded below** | If  $A + \lambda I \not\succeq 0$ , or  $b \notin \mathcal{R}(A + \lambda I)$  |

* * *

Would you like to now proceed to **Step 1.5–1.6**, where we:

*   **Diagonalize** the problem using the eigenbasis of  $A$ ,
*   And interpret the **range condition**  $b \in \mathcal{R}(A + \lambda I)$ ?

## Response:
Good. These two cases are the ones that really explain why the dual function has a **restricted domain**. Let’s slow way down and do them properly, from first principles, with geometry, linear algebra, and limits all lined up.

We are minimizing, for fixed  $\lambda$ ,

$$
L(x,\lambda)=x^{T}Qx+2b^{T}x-\lambda,\qquad Q=A+\lambda I.
$$

The constant  $-\lambda$  does nothing to the minimization over  $x$ , so the real object is

$$
\phi(x)=x^{T}Qx+2b^{T}x.
$$

Everything depends on the matrix  $Q$ .

* * *

Case 2 —  $Q\succeq0$  but **singular**
---------------------------------------

This is the subtle one.

### Step 1. What does “PSD but singular” mean?

 $Q\succeq0$  means

$$
x^TQx\ge 0\quad\text{for all }x.
$$

Singular means

$$
\ker(Q)\neq\{0\}.
$$

So there exist nonzero vectors  $z$  with

$$
Qz=0.
$$

Geometrically:

*   In directions orthogonal to  $\ker(Q)$ , the quadratic grows.
*   Along directions in  $\ker(Q)$ , the quadratic is **flat**:  
     $z^TQz=0$ .

So  $\phi(x)$  looks like a bowl in some directions and a **flat valley** in others.

* * *

### Step 2. Split space into two parts

Every vector  $x$  can be written uniquely as

$$
x = x_r + x_n,
$$

where

*    $x_r\in\mathcal R(Q)$  (range, curved directions),
*    $x_n\in\ker(Q)$  (flat directions).

These two subspaces are orthogonal.

Now compute the objective:

$$
\phi(x)=x^TQx+2b^Tx.
$$

Since  $Qx_n=0$ , we get

$$
x^TQx = x_r^TQx_r.
$$

And

$$
2b^Tx = 2b^Tx_r + 2b^Tx_n.
$$

So

$$
\phi(x)=x_r^TQx_r + 2b^Tx_r + 2b^Tx_n.
$$

The last term is dangerous: it is **linear** in the flat directions.

* * *

### Step 3. What happens in flat directions?

Take any  $z\in\ker(Q)$ . Consider moving along the ray

$$
x(t)=x_r + t z.
$$

Then

$$
\phi(x(t))=x_r^TQx_r + 2b^Tx_r + 2t\,b^Tz.
$$

This is an affine function of  $t$ .

Now two possibilities:

#### If  $b^T z\neq 0$ 

Then by choosing  $t\to\pm\infty$  with the correct sign,

$$
2t\,b^Tz \to -\infty.
$$

So

$$
\phi(x(t))\to -\infty.
$$

That means

$$
g(\lambda)=\inf_x L(x,\lambda)=-\infty.
$$

The Lagrangian is unbounded below.

* * *

#### If  $b^T z=0$  for all  $z\in\ker(Q)$ 

Then the flat directions contribute **nothing**:

$$
2b^Tx_n=0.
$$

So  $\phi(x)$  depends only on  $x_r$ . No direction can drive it to  $-\infty$ .

This condition is exactly

$$
b \perp \ker(Q) \quad\Longleftrightarrow\quad b\in \mathcal R(Q).
$$

Only then does a minimum exist.

* * *

### Step 4. What is the minimum when it exists?

On  $\mathcal R(Q)$ ,  $Q$  is invertible. So we solve

$$
Qx_r = -b.
$$

The minimum-norm solution is

$$
x_r=-Q^\dagger b,
$$

and any  $x_n\in\ker(Q)$  can be added without changing the value.

The minimal value is

$$
\phi_{\min} = -\,b^T Q^\dagger b,
$$

so

$$
g(\lambda)=-b^TQ^\dagger b-\lambda.
$$

That’s Case 2.

* * *

Case 3 —  $Q$  is **not** PSD
-----------------------------

Now suppose  $Q$  has a negative eigenvalue.

That means:  
there exists some vector  $v\neq0$  such that

$$
v^TQv<0.
$$

Look at the ray  $x=t v$ . Then

$$
\phi(tv)=t^2 v^TQv + 2t\,b^Tv.
$$

The leading term is

$$
t^2 v^TQv,
$$

which is negative and grows like  $-|t|^2$ .

So as  $|t|\to\infty$ ,

$$
\phi(tv)\to -\infty,
$$

no matter what  $b$  is doing.

Therefore

$$
g(\lambda)=-\infty.
$$

The Lagrangian is violently unstable in directions of negative curvature.

* * *

Final picture
-------------

For fixed  $\lambda$ , the dual function exists only if the Lagrangian is **stable** as a function of  $x$ :

|  $Q=A+\lambda I$  | Behavior |
| --- | --- |
| Has negative eigenvalue | Downward parabola →  $g(\lambda)=-\infty$  |
| PSD but singular,  $b\notin\mathcal R(Q)$  | Flat + tilt →  $g(\lambda)=-\infty$  |
| PSD and  $b\in\mathcal R(Q)$  | Stable → finite  $g(\lambda)$  |

This is why the dual function has the exact domain

$$
A+\lambda I\succeq0,\qquad b\in\mathcal R(A+\lambda I).
$$

Outside this set, the Lagrangian collapses to  $-\infty$ , so those  $\lambda$ ’s are useless for the dual.

That’s the real geometry behind Cases 2 and 3.

## Response:
Perfect — we’ll now do an **ultra-deep, step-by-step walkthrough** of:

*   🔸 **Step 1.3 Case 2**: What happens when  $Q = A + \lambda I \succeq 0$  but is **singular**, i.e. not invertible.
*   🔸 **Step 1.3 Case 3**: When  $Q = A + \lambda I$  is **not** positive semidefinite — i.e. has negative eigenvalues.

Then, we’ll move on to:

*   🔸 **Step 1.4**: Fully unpacking when the dual function  $g(\lambda) = \inf_x L(x, \lambda)$  is finite in all three cases.

* * *

🎯 GOAL: Understand exactly what happens to the dual function  $g(\lambda)$  in each case of definiteness of  $A + \lambda I$ , and what it means geometrically, analytically, and algebraically.
=================================================================================================================================================================================================

* * *

✅ 1.3, Case 2:  $A + \lambda I \succeq 0$ , but **not** invertible
==================================================================

* * *

🔹 What does this mean?
-----------------------

You are in the case where:

*    $A + \lambda I$  is **positive semidefinite**, so:
    $$
    x^T (A + \lambda I) x \geq 0 \quad \text{for all } x
    $$
*   But it's **not positive definite**:  
    There exists a nonzero  $v \in \mathbb{R}^n$  such that:
    $$
    v^T (A + \lambda I) v = 0
    $$
    ⇒  $v \in \ker(A + \lambda I)$ 

So:

*   The matrix is **singular** — i.e., it has **at least one eigenvalue equal to 0**
*   It has a **nontrivial nullspace**: some directions  $x$  where the quadratic form is flat (zero curvature)

* * *

🔸 What happens to minimization?
--------------------------------

We are minimizing:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left[ x^T Q x + 2b^T x - \lambda \right] \quad \text{with } Q := A + \lambda I
$$

This is a quadratic function — but since  $Q$  is singular:

*   Some directions  $x$  will have **zero curvature** (flat directions).
*   So  $x^T Q x = 0$  along  $x \in \ker(Q)$ 

The key question is:

> Does the linear term  $2b^T x$  "push" us along those flat directions, making the function go to  $-\infty$ ?

Let’s make this rigorous.

* * *

🔸 First-order optimality: when is minimum attained?
----------------------------------------------------

The **stationary point** condition is:

$$
\nabla_x L(x, \lambda) = 2Qx + 2b = 0 \quad \iff \quad Qx = -b
$$

This linear equation has a solution **if and only if**:

$$
\boxed{ b \in \mathcal{R}(Q) }
$$

This is basic linear algebra:

*   A linear system  $Qx = -b$  is solvable iff  $-b$  lies in the **column space** of  $Q$ 
*   Equivalently,  $b \in \mathcal{R}(Q)$ 

* * *

🔸 Two subcases
---------------

### Case 2a:  $b \in \mathcal{R}(Q)$ 

Then:

*   The optimality condition has a solution
*   We can compute:
    $$
    x^\star = -Q^\dagger b
    $$
    where  $Q^\dagger$  is the **Moore–Penrose pseudoinverse**

Then the optimal value is:

$$
g(\lambda) = x^{\star T} Q x^\star + 2b^T x^\star - \lambda
$$

Let’s compute step-by-step:

*    $Q x^\star = -b$ 
*   So  $x^{\star T} Q x^\star = x^{\star T} (-b) = -x^{\star T} b$ 
*   And  $b^T x^\star = x^{\star T} b$ 

So:

$$
g(\lambda) = - x^{\star T} b + 2(- x^{\star T} b) - \lambda = - b^T x^\star - \lambda
$$

We can write:

$$
\boxed{ g(\lambda) = - b^T Q^\dagger b - \lambda }
$$

✅ The dual function is **finite**, even though  $Q$  is singular.

* * *

### Case 2b:  $b \notin \mathcal{R}(Q)$ 

Then:

*   The equation  $Qx = -b$  has **no solution**
*   So  $\nabla L(x, \lambda) = 0$  has **no stationary point**
*   What happens to  $L(x, \lambda)$  in this case?

It goes to ** $-\infty$ **.

Why?

Let’s pick any  $v \in \ker(Q)$ . Then:

*    $Qv = 0$ 
*   So  $v^T Q v = 0$ 

Now, consider a path  $x_\alpha = z + \alpha v$ , where  $z \in \mathbb{R}^n$  is any fixed vector.

Then:

$$
L(x_\alpha, \lambda) = (z + \alpha v)^T Q (z + \alpha v) + 2b^T (z + \alpha v) - \lambda = z^T Q z + 2b^T z + 2\alpha b^T v - \lambda
$$

Notice:

*    $Qv = 0$ , so no quadratic growth in  $\alpha$ 
*   But  $b^T v \ne 0$  (since  $b \notin \mathcal{R}(Q)$ )

Then:

$$
L(x_\alpha, \lambda) \to -\infty \quad \text{as } \alpha \to \pm \infty \ \text{(depending on sign of } b^T v)
$$

So:

$$
\boxed{ g(\lambda) = -\infty }
$$

Even though  $Q \succeq 0$ , the **linear term** dominates along flat directions.

* * *

✅ 1.3, Case 3:  $A + \lambda I \not\succeq 0$  — Not Positive Semidefinite
==========================================================================

Now we’re in the worst-case scenario:

*    $Q = A + \lambda I$  has **negative eigenvalues**

So there exists some direction  $v \in \mathbb{R}^n$  such that:

$$
v^T Q v < 0
$$

This implies:

*   The quadratic form is **not bounded below**
*   The function can be made arbitrarily negative

Let’s construct such a direction explicitly.

* * *

🔸 Consider the direction  $x_\alpha = \alpha v$ 
-------------------------------------------------

Let’s evaluate the Lagrangian:

$$
L(x_\alpha, \lambda) = \alpha^2 v^T Q v + 2\alpha b^T v - \lambda
$$
*    $v^T Q v < 0$ 
*   So for large enough  $\alpha$ , the quadratic term dominates

Then:

$$
L(x_\alpha, \lambda) \to -\infty \quad \text{as } |\alpha| \to \infty
$$

So:

$$
\boxed{ g(\lambda) = -\infty }
$$

The dual function is **undefined (minus infinity)** when  $Q$  is not PSD.

This is expected: **dual function only makes sense if Lagrangian is bounded below**.

* * *

✅ Step 1.4 — When Is  $g(\lambda)$  Finite?
===========================================

Let’s now gather all 3 cases together and explain the **domain of the dual function**.

* * *

🔲 Case 1:  $A + \lambda I \succ 0$ 
------------------------------------

Then:

*   Lagrangian is strictly convex
*   Has a unique minimizer:
    $$
    x^\star = - (A + \lambda I)^{-1} b
    $$
*   Dual function is:
    $$
    g(\lambda) = - b^T (A + \lambda I)^{-1} b - \lambda
    $$
*   **Always finite** for  $\lambda > -\lambda_{\min}(A)$ 

✅ **Included in domain**

* * *

🔲 Case 2:  $A + \lambda I \succeq 0$ , singular
------------------------------------------------

*   **If**  $b \in \mathcal{R}(A + \lambda I)$ :  
    Use pseudoinverse to compute solution:
    $$
    g(\lambda) = - b^T (A + \lambda I)^\dagger b - \lambda
    $$
    ✅ **Included in domain**
*   **If not**: Lagrangian unbounded below ⇒
    $$
    g(\lambda) = -\infty
    $$
    ❌ **Excluded from domain**

* * *

🔲 Case 3:  $A + \lambda I \not\succeq 0$ 
------------------------------------------

*   Some direction makes  $x^T Q x \to -\infty$ 
*   No hope of boundedness
*   So:
    
$$
g(\lambda) = -\infty
$$

❌ **Excluded from domain**

* * *

✅ Final Characterization of the Domain
--------------------------------------

$$
\boxed{ \operatorname{dom}(g) = \left\{ \lambda \geq 0 \ \middle|\ A + \lambda I \succeq 0,\quad b \in \mathcal{R}(A + \lambda I) \right\} }
$$

This is the set of  $\lambda$  for which:

*   The penalized quadratic is convex enough
*   The linear term  $b$  doesn't push you into an unbounded direction

* * *

Would you like to now proceed to **1.5–1.6**, where we rewrite the dual function in the **eigenbasis** of  $A$ , and **explicitly interpret the range condition**  $b \in \mathcal{R}(A + \lambda I)$  in spectral terms?

## Response:
Perfect — let’s now **deeply unpack and fully explain Step 1.4**, going beyond the summary given so far.

We’ll rigorously analyze:

*   **When is the dual function  $g(\lambda)$  finite?**
*   **Why does it go to  $-\infty$  in other cases?**
*   **What exactly is happening geometrically and algebraically?**
*   **What does the domain of the dual function really mean?**

This step is crucial because it tells us **where the dual function is valid**, and **why we cannot just plug in any λ** when forming the dual problem.

* * *

🔁 Quick Recall of What the Dual Function Is
============================================

We’ve derived the **Lagrangian**:

$$
L(x, \lambda) = x^T (A + \lambda I)x + 2b^T x - \lambda
$$

Then the **dual function** is:

$$
\boxed{g(\lambda) = \inf_{x \in \mathbb{R}^n} L(x, \lambda)} = \inf_x \left[ x^T (A + \lambda I) x + 2b^T x - \lambda \right]
$$

The matrix  $Q := A + \lambda I$  determines the shape of this quadratic function in  $x$ , and affects:

*   Whether the function is **bounded below**
*   Whether a **minimum exists**
*   Whether we can compute the minimum in **closed form**

So now we ask:

* * *

✅ When is  $g(\lambda)$  finite?
================================

To answer this, we analyze the quadratic function:

$$
f(x) = x^T Q x + 2b^T x - \lambda \quad \text{with } Q := A + \lambda I
$$

We must examine the **behavior of  $f(x)$ ** as  $x \to \infty$ . The key factor is:

*   Does the quadratic form  $x^T Q x$  grow fast enough to **overcome** the linear term  $2b^T x$ ?
*   If it does, the function is **bounded below**
*   If not, it **dives to  $-\infty$ ** ⇒ no meaningful dual function

Let’s now **go case by case**, carefully.

* * *

⚠️ CASE 1:  $Q = A + \lambda I \succ 0$  (positive definite)
------------------------------------------------------------

This means:

*   All eigenvalues of  $Q$  are **strictly positive**
*   For all  $x \ne 0$ , we have:
    $$
    x^T Q x > 0
    $$
*   In fact:  $x^T Q x \geq \sigma_{\min} \|x\|^2$ , for some  $\sigma_{\min} > 0$ 

✅ This ensures:

*   The function  $f(x) = x^T Q x + 2b^T x$  **grows quadratically**
*   The linear term  $2b^T x$  is dominated for large  $\|x\|$ 
*   So  $f(x) \to +\infty$  as  $\|x\| \to \infty$ 

Hence:

*    $f(x)$  has a **global minimum**
*   The minimum is **unique**, because  $Q \succ 0$ 

### ✅ So in this case:

*   The dual function is finite and computable:
    $$
    g(\lambda) = - b^T (A + \lambda I)^{-1} b - \lambda
    $$
*   This case holds for:
    $$
    \boxed{\lambda > - \lambda_{\min}(A)}
    $$
    where  $\lambda_{\min}(A)$  is the smallest eigenvalue of  $A$ 

* * *

⚠️ CASE 2:  $Q = A + \lambda I \succeq 0$ , but **singular**
------------------------------------------------------------

This means:

*   All eigenvalues of  $Q$  are ≥ 0
*   But **at least one eigenvalue is exactly 0**
*   So:
    *    $Q$  is **positive semidefinite**
    *   But **not invertible**
    *   So there exists a nonzero direction  $v \in \ker(Q)$ , i.e.  $Qv = 0$ 

Let’s now analyze **two subcases**, depending on how the **linear term  $2b^T x$ ** interacts with these flat directions.

* * *

### 🔹 Subcase 2a:  $b \in \mathcal{R}(Q)$ 

This means:

*   The equation  $Qx = -b$  has at least one solution
*   In fact, the set of all solutions is:
    $$
    x^\star = -Q^\dagger b + z, \quad z \in \ker(Q)
    $$

Because  $Qz = 0$ , adding any null vector doesn’t change the value of the quadratic term.

Let’s write out:

$$
f(x) = x^T Q x + 2b^T x - \lambda
$$

Let  $x = x^\star = -Q^\dagger b$ . Then:

*    $Qx = -b$ 
*   So:
    $$
    x^T Q x = b^T Q^\dagger b \quad\text{(standard identity)}
    $$
    $$
    b^T x = - b^T Q^\dagger b
    $$

Then:

$$
f(x^\star) = b^T Q^\dagger b + 2 (- b^T Q^\dagger b) - \lambda = - b^T Q^\dagger b - \lambda
$$

So:

$$
\boxed{ g(\lambda) = - b^T (A + \lambda I)^\dagger b - \lambda }
$$

✅ Dual function is **finite and computable** in this case.

* * *

### 🔹 Subcase 2b:  $b \notin \mathcal{R}(Q)$ 

Now, the equation  $Qx = -b$  has **no solution**.

Then:

*   The gradient  $\nabla_x f(x) = 2Qx + 2b$  can never be zero
*   And even worse, the function has **directions in which it decreases without bound**

Let’s construct such a direction.

Let  $v \in \ker(Q)$ , so:

*    $Qv = 0$ 
*   But  $b^T v \ne 0$  (this must be true since  $b \notin \mathcal{R}(Q)$ )

Now consider:

$$
x_\alpha := \alpha v \quad \Rightarrow \quad f(x_\alpha) = 2\alpha b^T v - \lambda
$$
*   The quadratic term is 0 (since  $Qv = 0$ )
*   The linear term dominates

If  $b^T v < 0$ , then:

*    $f(x_\alpha) \to -\infty$  as  $\alpha \to +\infty$ 

If  $b^T v > 0$ , then:

*    $f(x_\alpha) \to -\infty$  as  $\alpha \to -\infty$ 

💥 So in either case:

$$
\boxed{g(\lambda) = -\infty}
$$

🚫 This λ is **not in the domain of the dual function**.

* * *

⚠️ CASE 3:  $Q = A + \lambda I$  is **not** positive semidefinite
-----------------------------------------------------------------

Then:

*   There exists some direction  $v \in \mathbb{R}^n$  such that  $v^T Q v < 0$ 
*   This means the quadratic form curves **downward** in some direction

Let’s again evaluate  $f(x)$  along  $x_\alpha = \alpha v$ :

$$
f(x_\alpha) = \alpha^2 v^T Q v + 2\alpha b^T v - \lambda
$$

As  $\alpha \to \infty$ :

*   The quadratic term dominates:  $\alpha^2 v^T Q v \to -\infty$ 
*   The linear term can’t stop this

So:

$$
\boxed{g(\lambda) = -\infty}
$$

🚫 Such λ is **not valid** for the dual function — it produces an unbounded Lagrangian.

* * *

✅ Final Summary: When Is the Dual Function Finite?
==================================================

We can now summarize all three cases rigorously.

* * *

### 🟩 **Case 1** — Positive definite

| Condition |  $A + \lambda I \succ 0$  |
| --- | --- |
| Domain? ✅ | Yes |
| Why? | The function is strictly convex ⇒ bounded below and unique minimizer |
| Formula |  $g(\lambda) = - b^T (A + \lambda I)^{-1} b - \lambda$  |

* * *

### 🟨 **Case 2** — Semidefinite but singular

| Condition |  $A + \lambda I \succeq 0$ , but singular |
| --- | --- |
| Subcase a:  $b \in \mathcal{R}(A + \lambda I)$  | ✅ |
| Subcase b:  $b \notin \mathcal{R}(A + \lambda I)$  | ❌ |
| Formula (if finite) |  $g(\lambda) = - b^T (A + \lambda I)^\dagger b - \lambda$  |

* * *

### 🟥 **Case 3** — Not semidefinite

| Condition |  $A + \lambda I \not\succeq 0$  |
| --- | --- |
| Domain? ❌ | Not valid — function unbounded below |
| Why? | Quadratic form curves downward ⇒  $f(x) \to -\infty$  |

* * *

✅ Final Answer: Domain of the Dual Function
-------------------------------------------

$$
\boxed{ \operatorname{dom}(g) = \left\{ \lambda \geq 0 \ \middle|\ A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \right\} }
$$

This is the set of all λ for which:

*   The modified matrix  $A + \lambda I$  has **nonnegative curvature** (no downward directions)
*   And the linear term  $b$  **doesn’t push us into a flat direction** we can’t control

* * *

Would you like to now proceed to Step **1.5–1.6**, where we:

*   Rewrite the dual function using the **eigenbasis** of  $A$ ,
*   Interpret the **range condition**  $b \in \mathcal{R}(A + \lambda I)$  spectrally,
*   And begin preparing the **dual problem** optimization?

## Response:
Perfect — let’s now **cleanly and precisely explain the domains** of the dual function  $g(\lambda)$  in each of the three cases, with **no recap**, and focusing purely on the **exact domain logic**, edge cases, and spectral interpretation.

* * *

🟢 Case 1:  $A + \lambda I \succ 0$  (positive definite)
--------------------------------------------------------

*   All eigenvalues of  $A + \lambda I$  are **strictly positive**:
    $$
    \lambda > -\lambda_{\min}(A)
    $$
*   The matrix is **invertible**, the quadratic form is strictly convex.

### ✅ Domain status:

$$
\lambda \in (-\lambda_{\min}(A), \infty)
$$

This is the **interior** of the domain. For all such  $\lambda$ , the dual function is:

*   Finite,
*   Differentiable,
*   Computable in closed form via inverse.

* * *

🟡 Case 2:  $A + \lambda I \succeq 0$ , but **singular**
--------------------------------------------------------

### Subcase 2a:  $b \in \mathcal{R}(A + \lambda I)$ 

*    $A + \lambda I$  is **positive semidefinite**, with **zero eigenvalues**
*   The function is convex, but not strictly
*   The solution exists via the **pseudoinverse**

### ✅ Domain status:

$$
\lambda = -\lambda_{\min}(A) \quad \text{allowed **iff** } b \in \mathcal{R}(A + \lambda I)
$$

This is the **boundary** of the domain — the smallest valid λ value.

Spectral condition:

*   If  $A = U \Lambda U^T$ , with  $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ 
*   And  $\tilde{b} = U^T b$ , then for λ =  $-\lambda_i$ :
    $$
    \text{We require: } \tilde{b}_i = 0 \quad \text{for all } i \text{ where } \lambda_i + \lambda = 0
    $$

* * *

### Subcase 2b:  $b \notin \mathcal{R}(A + \lambda I)$ 

*   Then there exists a direction in the nullspace of  $A + \lambda I$  along which the linear term pulls downward
*   The function is unbounded below

### ❌ Domain status:

$$
\lambda = -\lambda_{\min}(A) \quad \text{**excluded** if } b \notin \mathcal{R}(A + \lambda I)
$$

* * *

🔴 Case 3:  $A + \lambda I \not\succeq 0$ 
------------------------------------------

*   At least one eigenvalue of  $A + \lambda I$  is **negative**
*   So:
    $$
    \lambda < -\lambda_{\min}(A)
    $$
*   The quadratic form curves downward ⇒ the Lagrangian is unbounded below

### ❌ Domain status:

$$
\lambda < -\lambda_{\min}(A) \quad \text{excluded from domain}
$$

No matter what  $b$  is, the function blows up.

* * *

✅ Final Domain Summary
----------------------

$$
\boxed{ \operatorname{dom}(g) = \left\{ \lambda \geq 0 \ \middle|\ A + \lambda I \succeq 0,\quad b \in \mathcal{R}(A + \lambda I) \right\} }
$$
*   It's a **half-line** starting from  $\lambda = -\lambda_{\min}(A)$ , possibly including that endpoint, **if and only if**  $b \in \mathcal{R}(A + \lambda I)$ .
*   For all larger λ, the dual function is finite and well-defined.

Let me know if you want the **eigen-decomposition form of the domain**, or proceed to 1.5–1.6.

## Response:
Excellent — we’re now moving into **Phase 2**, where we study the **dual problem**:

> How do we **maximize** the dual function  $g(\lambda)$  over valid  $\lambda \geq 0$ ?  
> Why is this a **convex problem**, even though the primal is nonconvex?

This step gives us the **dual problem formulation** — the object whose optimal value will match the primal under strong duality (which we'll later prove holds).

* * *

✅ Step 2.1 — Define the Dual Problem (Maximize the Dual Function)
=================================================================

* * *

We’ve previously constructed the **dual function**:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( x^T (A + \lambda I)x + 2b^T x - \lambda \right)
$$

And we now know:

$$
\operatorname{dom}(g) = \left\{ \lambda \geq 0 : A + \lambda I \succeq 0,\ b \in \mathcal{R}(A + \lambda I) \right\}
$$

* * *

🔷 Define the dual optimization problem:
----------------------------------------

The dual problem is to **maximize  $g(\lambda)$ ** over its domain:

$$
\boxed{ \begin{aligned} \text{maximize}_{\lambda \geq 0} \quad & g(\lambda) \\ \text{subject to} \quad & A + \lambda I \succeq 0 \\ & b \in \mathcal{R}(A + \lambda I) \end{aligned} } \tag{D}
$$

This is a **one-dimensional convex optimization problem**, where:

*   The variable is  $\lambda \in [0, \infty)$ 
*   The dual function is concave in  $\lambda$ 
*   We are **maximizing a concave function**, which is a convex problem

The optimal value of this problem is called the **dual optimal value**, denoted:

$$
\boxed{d^\star := \sup_{\lambda \in \operatorname{dom}(g)} g(\lambda)}
$$

We’ll later show that **strong duality holds**, so  $d^\star = p^\star$ , even though the primal is nonconvex.

* * *

✅ Step 2.2 — Why Is the Dual Problem Convex?
============================================

This is one of the most beautiful aspects of duality:

> Even if the primal problem is nonconvex (which it is here), the **dual problem is always convex**.

* * *

🔷 Why is this true?
--------------------

We are maximizing the dual function:

$$
g(\lambda) = \inf_x L(x, \lambda)
$$

Over some convex domain. And here’s the key:

> The function  $g(\lambda)$  is **concave** — always.

This is true **regardless of whether the primal is convex**.

Let’s unpack why.

* * *

🔸 Proof Sketch: Why  $g(\lambda)$  is concave
----------------------------------------------

Let  $\lambda_1, \lambda_2 \in \operatorname{dom}(g)$ , and  $\theta \in [0, 1]$ . Define:

$$
\lambda_\theta := \theta \lambda_1 + (1 - \theta) \lambda_2
$$

Then:

$$
\begin{aligned} g(\lambda_\theta) &= \inf_x L(x, \lambda_\theta) \\ &= \inf_x \left[ x^T (A + \lambda_\theta I) x + 2b^T x - \lambda_\theta \right] \\ &= \inf_x \left[ \theta L(x, \lambda_1) + (1 - \theta) L(x, \lambda_2) \right] \\ &\geq \theta \inf_x L(x, \lambda_1) + (1 - \theta) \inf_x L(x, \lambda_2) \\ &= \theta g(\lambda_1) + (1 - \theta) g(\lambda_2) \end{aligned}
$$

Thus:

$$
\boxed{g(\lambda) \text{ is concave}}
$$

* * *

🧠 Why is this useful?
----------------------

Because **maximizing a concave function** is a **convex optimization problem**.

Even though the **original (primal) problem is nonconvex**, its dual problem is:

*   One-dimensional,
*   Concave objective,
*   Convex domain.

This means:

*   There are **no local maxima** — any local max is global
*   We can use **line search**, **bisection**, **Newton’s method**, etc. to solve it efficiently

* * *

⚠️ Important Caveat:
--------------------

Maximizing a concave function is only a **convex optimization problem** if:

*   The domain is convex
*   The function is concave
*   The constraints preserve convexity

This holds in our case because:

*    $\lambda \mapsto A + \lambda I \succeq 0$  defines a **convex cone constraint** on λ
*    $\lambda \mapsto b \in \mathcal{R}(A + \lambda I)$  defines a **closed set** — actually a union of open intervals (we’ll make this precise soon)

So the dual problem is **well-posed**, **convex**, and **solvable**.

* * *

✅ Step 2.3 — Rewrite the Dual in Eigenbasis Form
================================================

Now, let’s rewrite the dual function explicitly in terms of the **eigenbasis of  $A$ **.

* * *

🔷 Spectral decomposition:
--------------------------

Let:

$$
A = U \Lambda U^T
$$

where:

*    $U \in \mathbb{R}^{n \times n}$  is an orthogonal matrix of eigenvectors
*    $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$  is a diagonal matrix of eigenvalues

Let:

$$
\tilde{b} := U^T b
$$

Then:

$$
A + \lambda I = U (\Lambda + \lambda I) U^T
$$

And:

$$
(A + \lambda I)^{-1} = U (\Lambda + \lambda I)^{-1} U^T \quad \text{(when invertible)}
$$

So:

$$
b^T (A + \lambda I)^{-1} b = \tilde{b}^T (\Lambda + \lambda I)^{-1} \tilde{b} = \sum_{i=1}^n \frac{\tilde{b}_i^2}{\lambda_i + \lambda}
$$

* * *

🔸 Final Spectral Form of the Dual Function
-------------------------------------------

$$
\boxed{ g(\lambda) = \begin{cases} - \displaystyle\sum_{i=1}^n \frac{\tilde{b}_i^2}{\lambda_i + \lambda} - \lambda & \text{if } \lambda > - \min_i \lambda_i \\ \text{finite iff } \tilde{b}_i = 0 \text{ for all } i \text{ with } \lambda_i + \lambda = 0 & \text{if } \lambda = -\lambda_i \\ -\infty & \text{otherwise} \end{cases} }
$$

* * *

✅ Interpretation:
-----------------

*   Each term  $\frac{\tilde{b}_i^2}{\lambda_i + \lambda}$  represents **how aligned**  $b$  is with the  $i$ \-th eigenvector of  $A$ 
*   The denominator  $\lambda_i + \lambda$  shifts the eigenvalues of  $A$ 
*   As  $\lambda \to -\lambda_i$ , the term **blows up** unless  $\tilde{b}_i = 0$ 

So the dual function is only finite at λ values where:

*   All eigenvalues of  $A + \lambda I$  are ≥ 0
*   And the components of  $b$  in the null eigenspaces are zero

This spectral representation makes the **domain of  $g$ ** and the **structure of the dual problem** completely transparent.

* * *

Would you like to proceed to **Step 2.4**, where we interpret this dual function **geometrically** and use it to understand dual feasibility and convexity even deeper?

## Response:
Excellent recap — you’ve nailed the structure of the derivation so far: construct the **Lagrangian**, compute the **dual function** by minimizing it over  $x$ , handle the **case distinctions** based on the definiteness of  $Q = A + \lambda I$ , and finally get a closed-form (or domain-restricted) expression for  $g(\lambda)$ .

Now to your key question:

* * *

❓ Why are we taking  $\max g(\lambda)$  in the dual problem?
============================================================

This question gets to the **heart of duality theory**.

Let’s unpack it in full detail, rigorously and clearly:

* * *

🔷 1. What is the goal of the dual problem?
-------------------------------------------

The **primal problem** is:

$$
\text{minimize}_{x \in \mathbb{R}^n} \quad f(x) := x^T A x + 2b^T x \quad \text{subject to } x^T x \le 1
$$

Its solution gives us the **primal optimal value**:

$$
\boxed{p^\star := \inf_{x \in \mathbb{R}^n,\ x^T x \le 1} f(x)}
$$

We want to **compute or approximate** this value.

* * *

🔶 2. The Lagrangian gives a lower bound
----------------------------------------

For any  $\lambda \geq 0$ , define the **Lagrangian**:

$$
L(x, \lambda) := f(x) + \lambda(x^T x - 1) = x^T A x + 2b^T x + \lambda(x^T x - 1)
$$

Now for **any  $\lambda \geq 0$ **, the **dual function** is:

$$
g(\lambda) := \inf_{x \in \mathbb{R}^n} L(x, \lambda) = \inf_x \left[ f(x) + \lambda(x^T x - 1) \right]
$$

We can interpret this as a **penalized version** of the primal: if  $x$  violates the constraint  $x^T x \le 1$ , it gets a penalty via  $\lambda$ .

* * *

🔸 Key Fact: **Weak duality**
-----------------------------

For **any**  $x$  feasible (i.e.,  $x^T x \le 1$ ) and any  $\lambda \ge 0$ , we have:

$$
L(x, \lambda) = f(x) + \lambda(x^T x - 1) \le f(x)
$$

So taking  $\inf_x L(x, \lambda) \le \inf_{x \in \mathcal{F}} f(x)$ 

Hence:

$$
\boxed{g(\lambda) \le p^\star \quad \text{for all } \lambda \ge 0}
$$

This is the **weak duality inequality**.

> The dual function gives a **lower bound** on the primal optimal value.

* * *

🟢 3. Therefore, we want the **best possible** lower bound
----------------------------------------------------------

Since  $g(\lambda) \le p^\star$  always, the **tightest** lower bound we can obtain is:

$$
\boxed{ \max_{\lambda \ge 0} g(\lambda) }
$$

This gives the **dual optimal value**  $d^\star$ , which satisfies:

$$
d^\star := \sup_{\lambda \in \operatorname{dom}(g)} g(\lambda) \le p^\star
$$

This is what the **dual problem** computes.

* * *

🔷 4. Strong duality
--------------------

Under suitable conditions (we’ll prove them later), we get:

$$
\boxed{d^\star = p^\star}
$$

That is:

*   The **tightest lower bound** equals the **true optimum**
*   The dual maximization recovers the exact primal value

This is **strong duality**, and it is what justifies solving the **dual problem** instead of the primal.

In this particular problem:

*   The primal is **nonconvex**
*   But the dual is **convex**
*   Yet we still get **strong duality**

This is a deep fact tied to trust-region structure and quadratic forms. We’ll prove strong duality for this trust-region QP shortly.

* * *

🧠 Summary: Why maximize  $g(\lambda)$ ?
----------------------------------------

*    $g(\lambda)$  is a **lower bound** on the primal value for every  $\lambda \ge 0$ 
*    $\max g(\lambda)$  gives the **tightest possible** lower bound
*   Under strong duality, this tight bound is **equal** to the primal value
*   So we define the dual problem as:
    $$
    \boxed{\text{maximize}_{\lambda \ge 0} \ g(\lambda)}
    $$

It gives us:

*   A **convex optimization problem**,
*   Whose solution provides the **exact optimal value**,
*   And in many cases, helps **recover the primal optimizer** too (via KKT conditions)

* * *

Would you like to now proceed to **Step 2.4**, where we analyze the **shape** of  $g(\lambda)$ , its **concavity**, and start solving the dual numerically/symbolically?

## Response:
Yes — that sentence you just wrote is exactly right.  
The dual function is the **best (lowest) value the Lagrangian can achieve for a fixed penalty weight**, so it is a **lower envelope** of the Lagrangian family. Now let’s go cleanly and carefully through **2.1–2.3** again, with that picture in mind.

* * *

**2.1 — What is the dual problem here?**
----------------------------------------

We have already built

$$
g(\lambda)=\inf_x\Big(x^T(A+\lambda I)x+2b^Tx-\lambda\Big),
$$

defined only for those  $\lambda$  where this infimum is finite.

From the previous analysis, this happens exactly when

$$
A+\lambda I\succeq0 \quad\text{and}\quad b\in\mathcal R(A+\lambda I).
$$

For every such  $\lambda$ ,

$$
g(\lambda)\le p^\star,
$$

where  $p^\star$  is the true minimum of the constrained primal problem.

So what does the dual problem do?

It says:

> Among all penalty weights  $\lambda$  that make the Lagrangian stable, pick the one that gives the **largest** lower bound.

That is

$$
\boxed{ \max_{\lambda}\; g(\lambda) \quad\text{s.t.}\quad A+\lambda I\succeq0,\; b\in\mathcal R(A+\lambda I),\; \lambda\ge0. }
$$

This is not arbitrary. It is forced by logic:

• Every  $g(\lambda)$  is a valid lower bound  
• Larger is better  
• The best lower bound is their supremum

That supremum is the **dual optimal value**  $d^\star$ .

* * *

**2.2 — Why is this a convex (well‑behaved) problem?**
------------------------------------------------------

This is one of the deepest facts in optimization:

> Even when the primal problem is nonconvex, the dual function is always concave.

Why?

Because for each fixed  $x$ ,

$$
L(x,\lambda) = x^TAx+2b^Tx+\lambda(x^Tx-1)
$$

is an **affine function of  $\lambda$ ** (linear in  $\lambda$  plus a constant).

The dual function is

$$
g(\lambda)=\inf_x L(x,\lambda),
$$

which is the **pointwise infimum of affine functions of  $\lambda$ **.

A fundamental theorem of convex analysis says:

> The pointwise infimum of affine functions is concave.

So  $g(\lambda)$  is concave on its domain.

That means:

• No local maxima  
• One‑dimensional  
• Any maximizer is global  
• Can be solved by calculus, bisection, Newton, etc.

So even though the primal quadratic is nonconvex, the dual problem is a **nice, convex, one‑variable maximization**.

This is the miracle of the trust‑region problem.

* * *

**2.3 — What does the dual look like in eigen‑coordinates?**
------------------------------------------------------------

Now we diagonalize  $A$ .

Let

$$
A = U\Lambda U^T, \qquad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n), \qquad \tilde b=U^Tb.
$$

Then

$$
A+\lambda I = U(\Lambda+\lambda I)U^T,
$$

so

$$
(A+\lambda I)^{-1} = U(\Lambda+\lambda I)^{-1}U^T
$$

when invertible, and the pseudoinverse works the same way.

Therefore

$$
b^T(A+\lambda I)^{-1}b = \tilde b^T(\Lambda+\lambda I)^{-1}\tilde b = \sum_{i=1}^n \frac{\tilde b_i^2}{\lambda_i+\lambda}.
$$

So the dual function becomes

$$
\boxed{ g(\lambda) = -\sum_{i=1}^n \frac{\tilde b_i^2}{\lambda_i+\lambda} \;-\; \lambda, }
$$

with the domain restrictions:

•  $\lambda_i+\lambda\ge0$  for all  $i$   
• If  $\lambda_i+\lambda=0$ , then  $\tilde b_i=0$ 

This makes everything visible:

Each eigen‑direction contributes a term

$$
-\frac{\tilde b_i^2}{\lambda_i+\lambda}.
$$

If  $\lambda$  is too small, one denominator goes negative → instability →  $g=-\infty$ .  
If  $\lambda$  hits a zero eigenvalue with nonzero  $\tilde b_i$  → blow‑up →  $g=-\infty$ .  
Otherwise  $g(\lambda)$  is smooth, concave, and one‑dimensional.

* * *

### The big picture

You are tuning a single scalar  $\lambda$  that “pushes” all eigenvalues of  $A$  upward until the quadratic becomes stable.  
The dual function measures how much energy you can extract from each eigen‑direction under that stabilization.  
Maximizing  $g(\lambda)$  chooses the stabilization that gives the tightest possible lower bound — and in this special problem, that lower bound turns out to be exact.

That’s the geometry behind 2.1–2.3.

## Response:
Great — and small but important correction first, stated plainly:

> What holds here is **strong duality**, not strong convexity.  
> The primal problem is **not convex** in general, and certainly not strongly convex.  
> The miracle is that **strong duality holds anyway**.

Now let’s **focus only on why strong duality holds in this problem**, and then **sum it up cleanly**.

* * *

1\. What “strong duality” actually means here
---------------------------------------------

You have:

*   **Primal optimal value**
    $$
    p^\star = \inf_{x:\, x^Tx\le 1} \big(x^TAx+2b^Tx\big)
    $$
*   **Dual optimal value**
    $$
    d^\star = \sup_{\lambda\ge0} g(\lambda)
    $$

**Strong duality** means:

$$
\boxed{p^\star = d^\star}
$$

This is surprising because:

*   The primal objective is **nonconvex** when  $A\nsucceq0$ .
*   In general, nonconvex problems **do not** satisfy strong duality.

So why does it work _here_?

* * *

2\. The core reason (one sentence)
----------------------------------

> Strong duality holds because this is a **quadratic objective with exactly one quadratic constraint**, and that structure forces the Lagrangian relaxation to be **exact**.

Everything else is a consequence of this.

* * *

3\. The geometric mechanism (the real reason)
---------------------------------------------

Let’s strip everything to geometry.

### 3.1 The feasible set is simple and compact

The constraint

$$
x^Tx\le1
$$

defines a **compact, convex, smooth set** (the unit ball).

That gives two crucial properties:

1.  A minimizer **exists**.
2.  The boundary is smooth, so optimal points satisfy **first-order stationarity**.

* * *

### 3.2 At the primal optimum, one constraint controls everything

At the primal minimizer  $x^\star$ , one of two things happens:

1.  **Interior solution**
    $$
    \|x^\star\|<1
    $$
    Then the constraint is inactive, and the unconstrained minimum already lies inside the ball.
2.  **Boundary solution**
    $$
    \|x^\star\|=1
    $$
    Then the constraint is active, and the optimality condition becomes:
    $$
    (A+\lambda^\star I)x^\star + b = 0
    $$
    for some scalar  $\lambda^\star\ge0$ .

That equation is _exactly_ the stationarity condition of the Lagrangian.

There is **only one multiplier** and **only one curvature adjustment**.

* * *

4\. Why the Lagrangian relaxation is tight
------------------------------------------

This is the key step.

When you form the Lagrangian:

$$
L(x,\lambda)=x^TAx+2b^Tx+\lambda(x^Tx-1),
$$

you are doing **one very specific thing**:

> You are adding just enough isotropic curvature ( $\lambda I$ ) to kill the nonconvex directions of  $A$ .

Because:

*   Any negative curvature of  $A$  is in some eigen-direction.
*   Adding  $\lambda I$  shifts _all_ eigenvalues uniformly.
*   Once  $A+\lambda I\succeq0$ , the quadratic becomes stable.

There is **no way** for the primal solution to exploit curvature that the dual cannot see.  
That’s the heart of the exactness.

* * *

5\. Why maximizing  $g(\lambda)$  finds the correct  $\lambda^\star$ 
---------------------------------------------------------------------

Recall:

$$
g(\lambda)=\inf_x L(x,\lambda).
$$

For each  $\lambda$ , this is:

*   The **best lower bound** you can get with that penalty.
*   A concave function of  $\lambda$ .

As you increase  $\lambda$ :

*   You stabilize the quadratic more.
*   But you also pay a linear cost  $-\lambda$ .

The maximizing  $\lambda^\star$  is exactly the one where:

$$
\|x(\lambda^\star)\|=1,
$$

i.e. the trust-region boundary is matched perfectly.

At that point:

*   The Lagrangian minimizer coincides with the primal minimizer.
*   The lower bound becomes **tight**.

Hence:

$$
g(\lambda^\star)=f(x^\star).
$$

That is strong duality.

* * *

6\. Why this fails with more constraints (important insight)
------------------------------------------------------------

If you had:

*   Two quadratic constraints, or
*   A non-ball constraint, or
*   A non-quadratic objective,

then:

*   One scalar  $\lambda$  would **not** be enough to stabilize all bad directions.
*   The dual relaxation would become loose.
*   Strong duality would typically fail.

This exactness is **special**, not generic.

* * *

7\. Final clean summary (the takeaway)
--------------------------------------

Here is the distilled explanation:

> **Strong duality holds because**  
> • the objective is quadratic,  
> • there is exactly one quadratic constraint,  
> • the constraint is a Euclidean ball,  
> • and adding  $\lambda I$  is sufficient to eliminate all nonconvexity.
> 
> As a result, the Lagrangian relaxation captures the primal problem exactly, and maximizing the dual function recovers the true minimum.

That’s the entire story — no handwaving, no convexity assumption, no magic.

## Response:
Perfect. Let’s now rigorously and deeply unpack **why strong duality holds** for this problem — even though the **primal is nonconvex**.

This is **the punchline** of the entire trust-region duality framework.

* * *

🎯 Goal: Why does strong duality hold?
======================================

We want to show that:

$$
\boxed{ \max_{\lambda \ge 0} g(\lambda) = \min_{x^T x \le 1} f(x) }
$$

where:

*    $f(x) = x^T A x + 2b^T x$ 
*    $g(\lambda) = \inf_{x \in \mathbb{R}^n} L(x, \lambda)$ 
*    $L(x, \lambda) = f(x) + \lambda(x^T x - 1)$ 

The primal is **nonconvex** if  $A \not\succeq 0$ , so strong duality **is not automatic**.

But we claim that **strong duality holds anyway** for this problem.

Let’s unpack **why** — from both geometric and analytic viewpoints.

* * *

📦 Step-by-Step Breakdown
=========================

* * *

🔶 Step 1: Trust-region structure = hidden convexity
----------------------------------------------------

The constraint  $x^T x \le 1$  defines a **Euclidean ball**, which is convex.

The objective  $f(x) = x^T A x + 2b^T x$  is a **quadratic** function — possibly nonconvex (if  $A \not\succeq 0$ ).

So the problem:

$$
\min_{x^T x \le 1} x^T A x + 2b^T x
$$

is a **quadratically constrained quadratic program (QCQP)**.

This is **not convex in general**.

BUT — when the **constraint is an ellipsoid or ball**, and the **objective is quadratic**, the problem has a **special structure**:

> The dual problem recovers the exact value of the primal — even though the primal is nonconvex.

This is known as the **trust-region duality theorem**.

* * *

✅ Step 2: The dual function is concave
--------------------------------------

We’ve shown in full detail that:

$$
g(\lambda) := \inf_{x} \left[ x^T (A + \lambda I) x + 2b^T x - \lambda \right]
$$

is:

*   **Concave in  $\lambda$ ** (proved via convex combination + infimum inequality)
*   Well-defined for:
    $$
    \lambda \ge -\lambda_{\min}(A) \quad \text{and} \quad b \in \mathcal{R}(A + \lambda I)
    $$

The dual function is continuous and **smooth** on the open set where  $A + \lambda I \succ 0$ .

So the **dual problem**:

$$
\boxed{ \sup_{\lambda \ge 0} \ g(\lambda) }
$$

is a **convex optimization problem** (maximize concave function over convex domain).

This makes it **solvable** — we can always find a global optimum  $\lambda^\star$ .

* * *

📐 Step 3: Geometry of the Lagrangian matches the primal value
--------------------------------------------------------------

Recall:

$$
g(\lambda) = \inf_x \left[ f(x) + \lambda(x^T x - 1) \right]
$$

Let’s rewrite this as:

$$
g(\lambda) = \inf_x \left\{ f(x) \ \text{penalized by how much it violates the constraint} \ x^T x \le 1 \right\}
$$

As  $\lambda \to \infty$ , this **forces** the solution  $x$  to satisfy  $x^T x \le 1$  tightly.

So, roughly speaking:

*   For small  $\lambda$ , constraint is loose ⇒ unbounded below
*   For moderate  $\lambda$ , feasible region emerges
*   For optimal  $\lambda^\star$ , the penalty balances constraint enforcement with objective value

At that point:

*   The constraint is active or inactive depending on where the optimal  $x$  lies
*   The **penalty exactly enforces** the constraint — no more, no less

So  $\sup_\lambda g(\lambda) = f(x^\star)$ , for some primal feasible  $x^\star$ 

Thus:

$$
\boxed{ \sup_\lambda g(\lambda) = \min_{x^T x \le 1} f(x) }
$$

* * *

🧠 Step 4: Why this only works for trust-region problems
--------------------------------------------------------

The key is that the **unit ball constraint is strongly convex**, and the **objective is quadratic**.

This specific structure lets the dual function “encode” the geometry of the feasible set in a way that matches the true primal optimum.

This would **not** work in general — for example, if:

*   The constraint were nonconvex
*   The objective had discontinuities
*   There were multiple constraints
*   The feasible region had holes

But here, the ball constraint  $x^T x \le 1$  keeps everything well-behaved, and the Lagrangian is expressive enough to capture the correct curvature via the  $\lambda$  parameter.

This is the same phenomenon behind:

*   **Trust-region methods in optimization**
*   **Lagrangian relaxations of QCQPs**
*   **Regularization (ridge regression is dual to constrained least squares)**

* * *

✅ Final Summary: Why Strong Duality Holds
=========================================

| Property | Why it holds |
| --- | --- |
| **Primal is nonconvex** | Yes, if  $A \not\succeq 0$  |
| **Lagrangian function exists** | Always (quadratic) |
| **Dual function  $g(\lambda)$ ** | Concave, closed-form, computable |
| **Dual domain** | Nonempty and convex |
| **Dual optimal value  $d^\star$ ** | Exists |
| **Strong duality** | Holds for trust-region QCQP, by structure theorem |

$$
\boxed{ \min_{x^T x \le 1} x^T A x + 2b^T x = \max_{\lambda \ge 0} \inf_x L(x, \lambda) }
$$

Even though the primal is nonconvex!

* * *

Would you like to now:

*   Analyze **examples** or **graphs** of  $g(\lambda)$ ?
*   Or continue to derive the **primal minimizer** from the dual solution (via KKT conditions)?
*   Or unpack the **trust-region duality theorem** formally?



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)