# Lagrange duality walkthrough

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/27/2025 23:59:05  
**Updated:** 12/28/2025 2:03:55  
**Exported:** 12/28/2025 16:14:01  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/6950415e-1a90-8328-a43a-b76a01c547e8](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/6950415e-1a90-8328-a43a-b76a01c547e8)  

## Response:
Thought for 48s

Let’s unpack the page as if you’ve never seen Lagrange duality before, but we still want to end up exactly at (5.32) → (5.33) and understand why “strong duality” can hold even though the primal problem is nonconvex.

I’ll follow the text’s flow, but I’ll also fill in every missing step and “why” behind each move.

* * *

0) The primal problem and what makes it weird
---------------------------------------------

The problem is (their equation 5.32):

$$
\begin{aligned} \text{minimize}_{x\in\mathbb R^n}\quad & x^T A x + 2 b^T x\\ \text{subject to}\quad & x^T x \le 1, \end{aligned} \tag{5.32}
$$

where:

*    $x\in\mathbb R^n$  is the decision variable.
*    $A\in\mathbb S^n$  means  $A$  is a real symmetric  $n\times n$  matrix.
*    $b\in\mathbb R^n$ .
*   The constraint  $x^T x\le 1$  is “ $x$  lies in the unit ball” (Euclidean norm constraint):  $\|x\|_2^2\le 1$ .

### Why can this be nonconvex?

A quadratic function  $x^T A x + 2 b^T x$  is convex **iff**  $A\succeq 0$  (positive semidefinite).  
But here they explicitly allow  $A\not\succeq 0$  (it might be indefinite, with negative eigenvalues). Then the objective is not convex, so (5.32) is a **nonconvex** optimization problem.

This problem is famous: it’s the (classical) **trust-region subproblem**. In numerical optimization, it shows up when you approximate a complicated function by a quadratic near a point and restrict to a ball where the approximation is trusted.

* * *

1) Lagrange multipliers from first principles
---------------------------------------------

### 1.1 Turning the constraint into a penalty with a multiplier

The constraint is:

$$
x^T x \le 1 \quad\Longleftrightarrow\quad x^T x - 1 \le 0.
$$

The Lagrangian method says: introduce a scalar multiplier  $\lambda\ge 0$  and form

$$
L(x,\lambda)= \underbrace{x^T A x +2 b^T x}_{\text{objective}} \;+\; \lambda\underbrace{(x^T x -1)}_{\text{constraint function}}.
$$

That is exactly what the page writes:

$$
L(x,\lambda)=x^T A x +2 b^T x +\lambda(x^T x-1).
$$

Now regroup terms:

*    $x^T A x + \lambda x^T x = x^T(A+\lambda I)x$  because  $x^T(\lambda I)x=\lambda x^T x$ .
*   The remaining terms are  $2 b^T x - \lambda$ .

So

$$
L(x,\lambda)=x^T(A+\lambda I)x +2 b^T x - \lambda.
$$

This is the key simplification: for a fixed  $\lambda$ , the Lagrangian becomes a quadratic function of  $x$  with “Hessian”  $2(A+\lambda I)$ .

* * *

2) The dual function  $g(\lambda)$ : “best lower bound” idea
------------------------------------------------------------

### 2.1 What the dual function is, conceptually

For any  $\lambda\ge 0$ , the Lagrangian gives a **lower bound** on the constrained optimum.

Why? If  $x$  is feasible, then  $x^T x-1\le 0$ , and since  $\lambda\ge 0$ ,

$$
\lambda(x^T x-1)\le 0.
$$

So for feasible  $x$ ,

$$
L(x,\lambda) = (x^T A x +2 b^T x) + \lambda(x^T x-1) \le x^T A x +2 b^T x.
$$

So: for feasible  $x$ ,  $L(x,\lambda)$  never exceeds the objective value.  
Now if we take the **infimum over all  $x$ ** (even infeasible ones), we get the best possible lower bound produced by that  $\lambda$ :

$$
g(\lambda):=\inf_{x\in\mathbb R^n} L(x,\lambda).
$$

That is the dual function.

*    $g(\lambda)$  is always a lower bound on the primal optimal value  $p^\star$ .
*   The dual problem will maximize this lower bound over  $\lambda\ge 0$ .

So the dual is:

$$
\max_{\lambda\ge 0} g(\lambda).
$$

Everything now reduces to: compute  $g(\lambda)$  explicitly.

* * *

3) Computing  $\inf_x L(x,\lambda)$ : minimizing a quadratic
------------------------------------------------------------

Fix  $\lambda$ . Define

$$
M(\lambda):=A+\lambda I.
$$

Then

$$
L(x,\lambda)=x^T M(\lambda) x +2 b^T x - \lambda.
$$

So the  $\inf_x$  is the infimum of a quadratic form plus a linear term.

### 3.1 When is the infimum finite vs.  $-\infty$ ?

This is _the_ crucial case split.

*   If  $M(\lambda)$  has a direction of negative curvature, i.e.  $M(\lambda)$  is not PSD, then you can push  $x$  off to infinity along a direction that drives  $x^T M x\to -\infty$ , and the linear term can’t stop it. Then  $\inf_x L(x,\lambda)=-\infty$ .

So one necessary condition for a finite infimum is:

$$
M(\lambda)=A+\lambda I \succeq 0.
$$
*   Even if  $M(\lambda)\succeq 0$ , it might be singular (has a nontrivial nullspace). Then the quadratic term is “flat” along directions  $v$  with  $Mv=0$ . Along such a direction,
    $$
    L(x+tv,\lambda)=L(x,\lambda)+2t\,b^T v
    $$
    because  $(x+tv)^T M (x+tv)=x^T M x$  when  $Mv=0$  (all cross and  $t^2$  terms vanish).  
    If there exists  $v\in\ker(M)$  with  $b^T v\neq 0$ , you can choose  $t\to \pm\infty$  to drive the linear part to  $-\infty$ . So you still get  $-\infty$ .

So for finite infimum when  $M\succeq 0$ , you also need:

$$
b \perp \ker(M) \quad\Longleftrightarrow\quad b\in \mathcal R(M),
$$

where  $\mathcal R(M)$  means the range/column space of  $M$ . (For symmetric  $M$ ,  $\mathcal R(M)=\ker(M)^\perp$ .)

This explains the condition in the page:

*   finite only if  $A+\lambda I\succeq 0$  and  $b\in\mathcal R(A+\lambda I)$ 
*   otherwise  $-\infty$ .

### 3.2 The value of the infimum when it’s finite

Assume now:

$$
M\succeq 0,\qquad b\in\mathcal R(M).
$$

If  $M$  were invertible (positive definite), you’d “complete the square”:

$$
x^T M x +2b^T x = (x+M^{-1}b)^T M (x+M^{-1}b) - b^T M^{-1} b,
$$

so the minimum over  $x$  is  $-b^T M^{-1} b$ , achieved at  $x^\star=-M^{-1}b$ .

When  $M$  is singular PSD, the same idea works but you must replace the inverse by the **Moore–Penrose pseudoinverse**  $M^\dagger$ . Under  $b\in\mathcal R(M)$ , the minimizing set is  $x=-M^\dagger b + v$  for any  $v\in\ker(M)$ , and the minimum value is still

$$
\inf_x (x^T M x +2b^T x)= - b^T M^\dagger b.
$$

Therefore:

$$
g(\lambda)= - b^T (A+\lambda I)^\dagger b - \lambda \quad\text{if } A+\lambda I\succeq 0,\ b\in\mathcal R(A+\lambda I),
$$

and  $-\infty$  otherwise.

That is exactly what the page states.

* * *

4) The dual problem (their 5.33)
--------------------------------

Now maximize  $g(\lambda)$  over  $\lambda\ge 0$ :

$$
\begin{aligned} \text{maximize}\quad & - b^T (A+\lambda I)^\dagger b - \lambda\\ \text{subject to}\quad & A+\lambda I\succeq 0,\\ & b\in\mathcal R(A+\lambda I),\\ & \lambda\ge 0. \end{aligned} \tag{5.33}
$$

A few comments that matter:

1.  Even though the primal is nonconvex, the dual is always a **concave maximization** problem in  $\lambda$ , because  $g(\lambda)$  as a dual function is concave by construction (infimum of affine functions of  $\lambda$ ). Here  $\lambda$  is just one real variable, so it’s actually a 1D concave maximization, i.e., “nice”.
2.  The PSD constraint  $A+\lambda I\succeq 0$  is equivalent to a simple scalar inequality on  $\lambda$ :  
    If  $\lambda_{\min}(A)$  is the smallest eigenvalue of  $A$ , then
    
$$
A+\lambda I\succeq 0 \iff \lambda \ge -\lambda_{\min}(A).
$$

(Proof: eigenvalues shift by  $\lambda$ .)

So the “matrix constraint” is secretly just a lower bound on  $\lambda$ .

* * *

5) Eigen-decomposition form: why the dual becomes explicit
----------------------------------------------------------

The page then says you can rewrite the dual using eigenvalues/eigenvectors.

Let  $A$  have orthonormal eigen-decomposition:

$$
A = Q \,\mathrm{diag}(\lambda_1,\dots,\lambda_n)\,Q^T,
$$

where:

*    $Q=[q_1\ \cdots\ q_n]$  is orthogonal,  $Q^TQ=I$ ,
*    $A q_i=\lambda_i q_i$ .

Now express  $b$  in this eigenbasis:

$$
b = \sum_{i=1}^n \beta_i q_i \quad\Longleftrightarrow\quad \beta = Q^T b,
$$

where  $\beta_i=q_i^T b$ . (The page writes something like  $q_i$  for the eigenvectors and uses  $(q_i^T b)^2$  as coefficients.)

Then

$$
A+\lambda I = Q\,\mathrm{diag}(\lambda_1+\lambda,\dots,\lambda_n+\lambda)\,Q^T.
$$

### 5.1 Pseudoinverse in diagonal form

For a diagonal matrix  $D=\mathrm{diag}(d_i)$ , the pseudoinverse is  $\mathrm{diag}(d_i^\dagger)$  where  $d_i^\dagger=1/d_i$  if  $d_i\neq 0$ , and  $0$  if  $d_i=0$ .

So:

$$
(A+\lambda I)^\dagger = Q\,\mathrm{diag}\Big(\frac{1}{\lambda_i+\lambda}\ \text{if }\lambda_i+\lambda\neq 0;\ 0\ \text{if }=0\Big)\,Q^T.
$$

Now compute the quadratic form:

$$
b^T(A+\lambda I)^\dagger b = \beta^T \mathrm{diag}(\cdots)\beta = \sum_{i:\lambda_i+\lambda\neq 0} \frac{\beta_i^2}{\lambda_i+\lambda}.
$$

### 5.2 The “range condition”  $b\in\mathcal R(A+\lambda I)$  in eigen-coordinates

For symmetric matrices,  $\mathcal R(A+\lambda I)=\ker(A+\lambda I)^\perp$ .

*    $\ker(A+\lambda I)$  consists of eigenvectors with eigenvalue  $\lambda_i+\lambda=0$ , i.e.  $\lambda=-\lambda_i$ .
*   Being orthogonal to that kernel means: if  $\lambda_i+\lambda=0$ , then  $\beta_i=q_i^T b$  must be  $0$ .

So the condition “ $b\in\mathcal R(A+\lambda I)$ ” becomes:

$$
\text{If }\lambda_i+\lambda=0,\ \text{then }\beta_i=0.
$$

This is why the page uses the convention:

*   interpret  $\frac{(q_i^T b)^2}{\lambda_i+\lambda}$  as  $0$  if numerator  $=0$  and denominator  $=0$ ,
*   and as  $+\infty$  if numerator  $\neq 0$  while denominator  $=0$ ,  
    so that the formula automatically encodes the range condition.

### 5.3 Final eigenvalue form of the dual

So the dual objective:

$$
- b^T(A+\lambda I)^\dagger b -\lambda = -\sum_{i=1}^n \frac{(q_i^T b)^2}{\lambda_i+\lambda} - \lambda
$$

(with the conventions above).

And the PSD constraint is  $\lambda \ge -\lambda_{\min}(A)$ . Also we already have  $\lambda\ge 0$  from the inequality constraint multiplier.

So you end up with a clean 1D problem:

$$
\begin{aligned} \text{maximize}_{\lambda}\quad & -\sum_{i=1}^n \frac{(q_i^T b)^2}{\lambda_i+\lambda} - \lambda\\ \text{subject to}\quad & \lambda \ge \max\{0,\,-\lambda_{\min}(A)\}. \end{aligned}
$$

This is what the page is communicating.

* * *

6) Why this dual is convex (even though the primal isn’t)
---------------------------------------------------------

Two separate facts:

1.  **Dual functions are always concave.**  
    Because  $g(\lambda)=\inf_x L(x,\lambda)$  and  $L$  is affine in  $\lambda$ . Infimum of affine functions is concave.
2.  Here it’s 1D, and the feasible set for  $\lambda$  is an interval  $[\max\{0,-\lambda_{\min}(A)\},\infty)$ . Maximizing a concave function over an interval is a convex optimization problem (equivalently, minimizing a convex function  $-g$ ).

So the dual is “nice”.

* * *

7) The punchline: strong duality with a nonconvex primal (why no duality gap)
-----------------------------------------------------------------------------

Normally:

*   convex + Slater ⇒ strong duality.
*   nonconvex ⇒ often a positive duality gap.

Yet for this trust-region problem, the page says the gap is **zero**: primal optimum = dual optimum.

What’s going on?

### 7.1 The “hidden convexity” phenomenon

Even though  $x^T A x$  may be nonconvex, the presence of a **single quadratic constraint**  $\|x\|_2^2\le 1$  is special. There is a deep result (often connected to the **S-lemma / S-procedure**) that says: for “one quadratic inequality,” the Lagrangian dual can be exact under a mild regularity condition (a Slater-like interior-feasibility condition).

Here Slater’s condition is trivial to satisfy as long as the ball isn’t empty: pick  $x=0$  and you get  $0<1$ . So Slater holds.

That’s why they say: strong duality holds for “quadratic objective + one quadratic inequality,” provided Slater holds (they reference an appendix theorem).

### 7.2 What strong duality means here, concretely

Let:

*    $p^\star$  be the optimal value of the primal.
*    $d^\star$  be the optimal value of the dual.

Always we have weak duality:  $d^\star\le p^\star$ .  
Strong duality means:  $d^\star = p^\star$ .

So the dual problem (which is convex / 1D) gives you the exact global optimum of the nonconvex primal.

That’s extremely useful computationally: you can solve the nonconvex trust-region subproblem globally via the dual/KKT conditions.

* * *

8) Extra: how the dual solution gives you the primal solution (the “mechanics”)
-------------------------------------------------------------------------------

Once you find an optimal  $\lambda^\star$  solving the dual, the KKT stationarity condition says:

$$
\nabla_x L(x,\lambda^\star)=0 \quad\Rightarrow\quad 2(A+\lambda^\star I)x +2b =0 \quad\Rightarrow\quad (A+\lambda^\star I)x = -b.
$$

So a candidate primal optimizer is:

*   If  $A+\lambda^\star I$  is invertible:  $x^\star = -(A+\lambda^\star I)^{-1} b$ .
*   If singular:  $x^\star = -(A+\lambda^\star I)^\dagger b + v$  where  $v\in\ker(A+\lambda^\star I)$  is chosen to satisfy the norm constraint (and complementarity).

Complementary slackness adds:

$$
\lambda^\star(\|x^\star\|_2^2-1)=0.
$$

So:

*   if  $\lambda^\star>0$ , then  $\|x^\star\|_2=1$  (active boundary).
*   if  $\lambda^\star=0$ , then the unconstrained minimizer (if it exists) already lies inside the ball.

This is the operational route people use in numerical methods.

* * *

9) Summary of the page in one tight chain (now that every step is clear)
------------------------------------------------------------------------

*   Start with nonconvex trust-region primal (5.32).
*   Form Lagrangian with multiplier  $\lambda\ge 0$ :
    $$
    L(x,\lambda)=x^T(A+\lambda I)x+2b^T x-\lambda.
    $$
*   Dual function is  $g(\lambda)=\inf_x L(x,\lambda)$ .
*   This infimum is finite iff  $A+\lambda I\succeq 0$  and  $b\in\mathcal R(A+\lambda I)$ , and then
    $$
    g(\lambda)=-b^T(A+\lambda I)^\dagger b-\lambda.
    $$
*   Dual problem is maximize  $g(\lambda)$  over  $\lambda\ge 0$  with those feasibility conditions (their 5.33).
*   Using eigen-decomposition, the objective becomes an explicit sum:
    $$
    -\sum_i \frac{(q_i^Tb)^2}{\lambda_i+\lambda} - \lambda,
    $$
    with conventions to handle zero denominators.
*   Despite primal nonconvexity, this special “one quadratic constraint” case has **zero duality gap** under Slater, so the convex dual solves the global nonconvex primal.

* * *

If you want to go even more “hands-on,” the next natural step is to derive (carefully) that eigen-sum objective is concave in  $\lambda$  on the feasible interval, and then show how to solve for  $\lambda^\star$  via a monotone equation involving  $\|x(\lambda)\|_2$ . That turns the whole trust-region problem into basically a 1D root-finding problem with guarantees.

## Response:
Alright. We’ll do this “from bedrock,” not from “people usually know.” I’ll rebuild the whole story: primal problem → Lagrangian → dual function → dual problem → weak vs strong duality → why this special nonconvex quadratic still has zero duality gap. And I’ll explain every formula transformation, every condition ( $A+\lambda I\succeq 0$ ,  $b\in\mathcal R(\cdot)$ , pseudoinverse), and the eigen-expansion.

I’ll keep symbols consistent with the page.

* * *

1) Primal problem: what it _is_ at the definition level
-------------------------------------------------------

### 1.1 What is an optimization problem, abstractly?

An optimization problem is:

*   a variable  $x$  you can choose (a vector in  $\mathbb R^n$ ),
*   an objective function  $f(x)$  you want to minimize (or maximize),
*   constraints that restrict which  $x$  are allowed (“feasible”).

A standard “primal” problem looks like:

$$
\begin{aligned} \minimize_x \quad & f(x) \\ \text{subject to}\quad & g_i(x)\le 0,\ \ i=1,\dots,m \\ & h_j(x)=0,\ \ j=1,\dots,p . \end{aligned}
$$
*   Any  $x$  satisfying all constraints is **feasible**.
*   The set of all feasible points is the **feasible set**.
*   The optimal objective value is usually denoted  $p^\star$  (for “primal star”).

### 1.2 Your specific primal (trust region subproblem)

The page’s primal is:

$$
\begin{aligned} \minimize_{x\in\mathbb R^n}\quad & f(x):=x^T A x + 2b^T x\\ \text{subject to}\quad & x^T x \le 1. \end{aligned} \tag{P}
$$

Let’s parse each piece:

*    $x\in\mathbb R^n$ : decision vector.
*    $A\in\mathbb S^n$ : symmetric matrix, so  $A^T=A$ . Symmetry matters because  $x^T A x$  is a real scalar and eigen-decomposition works nicely.
*    $b\in\mathbb R^n$ .
*   Constraint  $x^T x\le 1$  means  $\|x\|_2^2\le 1$ , i.e.  $\|x\|_2\le 1$ : the closed Euclidean unit ball.

This is called “trust region” because you restrict  $x$  to a ball.

### 1.3 Why it can be nonconvex

A function is convex if its Hessian (second derivative matrix) is PSD (for quadratics).

*    $x^T A x$  is convex iff  $A\succeq 0$ .
*   If  $A$  has a negative eigenvalue,  $x^T A x$  curves downward in that direction → nonconvex.

So if  $A\not\succeq 0$ , the primal is **nonconvex**.

The constraint set  $\{x:\|x\|\le 1\}$  is convex, but the objective may not be.

* * *

2) Lagrangian: why it’s built and what it means
-----------------------------------------------

### 2.1 General idea: “turn constraints into penalties”

Suppose you have one inequality constraint  $g(x)\le 0$ . A common trick is to form:

$$
f(x) + \lambda g(x)
$$

where  $\lambda\ge 0$  is a multiplier.

Why  $\lambda\ge 0$ ? Because for feasible  $x$ ,  $g(x)\le 0$ . If  $\lambda\ge 0$ , then  $\lambda g(x)\le 0$ , so adding it can only decrease the value—this is what will create lower bounds (more on that soon).

### 2.2 Apply to our constraint

Our constraint is:

$$
x^T x \le 1 \quad \Longleftrightarrow \quad g(x):=x^T x - 1 \le 0.
$$

Define the **Lagrangian**:

$$
L(x,\lambda):= f(x)+\lambda g(x) = x^T A x +2b^T x + \lambda(x^T x - 1)
$$

with the multiplier constraint  $\lambda\ge 0$ .

Now simplify algebraically:

*    $x^T A x + \lambda x^T x = x^T (A+\lambda I)x$  because  $x^T(\lambda I)x = \lambda x^T x$ .
*   Constant term:  $-\lambda$ .

So:

$$
L(x,\lambda)=x^T(A+\lambda I)x +2b^T x - \lambda. \tag{L}
$$

That is exactly what the page writes.

* * *

3) Dual function: definition + why it gives lower bounds
--------------------------------------------------------

### 3.1 Key definition

The **dual function** is:

$$
g(\lambda):=\inf_{x\in\mathbb R^n} L(x,\lambda). \tag{dual function}
$$

Important: this infimum is over _all_  $x$ , not only feasible ones.

### 3.2 Why  $g(\lambda)$  is a lower bound (weak duality mechanism)

Let  $x$  be feasible:  $x^T x -1 \le 0$ . With  $\lambda\ge 0$ :

$$
\lambda(x^T x -1) \le 0.
$$

So for feasible  $x$ ,

$$
L(x,\lambda)= f(x)+\lambda(x^T x-1) \le f(x).
$$

Now take infimum over all  $x$ :

$$
g(\lambda)=\inf_x L(x,\lambda)\le L(x,\lambda)\le f(x) \quad \text{for every feasible } x.
$$

Since the primal optimum  $p^\star$  is the infimum of  $f(x)$  over feasible  $x$ , we get:

$$
g(\lambda)\le p^\star \quad \text{for all }\lambda\ge 0. \tag{lower bound}
$$

This is the core reason duality is useful: each  $\lambda\ge 0$  gives a computable lower bound.

* * *

4) Dual problem: definition + meaning
-------------------------------------

### 4.1 Dual problem definition

Since every  $g(\lambda)$  is a lower bound on  $p^\star$ , you want the **best** (largest) lower bound:

$$
d^\star := \sup_{\lambda\ge 0} g(\lambda).
$$

So the **dual problem** is:

$$
\maximize_{\lambda\ge 0}\ g(\lambda). \tag{D}
$$
*    $d^\star$  is the optimal dual value.
*   Always  $d^\star \le p^\star$  (this is **weak duality**, next).

### 4.2 Weak duality (formal statement)

**Weak duality:** For any primal feasible  $x$  and dual feasible  $\lambda$ ,

$$
g(\lambda)\le f(x).
$$

So maximizing the left side still cannot exceed minimizing the right side:

$$
d^\star \le p^\star.
$$

This always holds—convex or not.

### 4.3 Duality gap and strong duality

*   **Duality gap**:  $p^\star - d^\star \ge 0$ .
*   **Strong duality**:  $p^\star = d^\star$  (gap  $=0$ ).

In convex optimization, strong duality is often guaranteed by Slater’s condition. In nonconvex problems, strong duality can fail badly.

The “weird miracle” on this page is: even though the primal is nonconvex (if  $A$  indefinite), strong duality still holds for this particular structure.

But we can’t claim that until we compute  $g(\lambda)$  exactly.

* * *

5) Computing  $g(\lambda)=\inf_x L(x,\lambda)$ : the real work
--------------------------------------------------------------

We must minimize over  $x$  the function:

$$
L(x,\lambda)= x^T M x +2b^T x -\lambda, \quad \text{where } M:=A+\lambda I.
$$

The  $-\lambda$  is constant w.r.t.  $x$ , so:

$$
g(\lambda)= \left(\inf_x \; x^T M x +2b^T x\right) -\lambda.
$$

So focus on:

$$
\phi(\lambda):=\inf_x \left( x^T M x +2b^T x \right).
$$

This is a (possibly nonconvex) quadratic in  $x$  depending on  $M$ .

### 5.1 Case split: when is the infimum finite?

#### Case A:  $M$  has a negative direction → infimum is  $-\infty$ 

Suppose  $M$  is not PSD. Then there exists some vector  $v\neq 0$  with

$$
v^T M v <0.
$$

Now consider  $x=t v$  and send  $t\to \infty$ .

Compute:

$$
x^T M x +2b^T x = (tv)^T M (tv) +2b^T (tv) = t^2 (v^T M v) +2t(b^T v).
$$

As  $t\to\infty$ , the dominant term is  $t^2(v^T M v)$ , which goes to  $-\infty$  because  $v^T M v<0$ . So the whole expression goes to  $-\infty$ .

Therefore:

$$
\inf_x (x^T M x +2b^T x) = -\infty \quad \text{if } M \not\succeq 0.
$$

So to even have a meaningful dual value, we need:

$$
A+\lambda I \succeq 0. \tag{PSD condition}
$$

#### Case B:  $M\succeq 0$  but singular: need a second condition

Even if  $M\succeq 0$ , it can be singular, meaning there exists  $v\neq 0$  such that  $Mv=0$ . That  $v$  lies in the **nullspace**  $\ker(M)$ .

Along such  $v$ , the quadratic term is flat:

$$
(tv)^T M (tv)=t^2 v^T M v =0, \quad \text{since }Mv=0 \Rightarrow v^T M v=0.
$$

Now evaluate  $x=x_0+tv$ :

$$
(x_0+tv)^T M (x_0+tv) = x_0^T M x_0 \quad \text{(cross terms vanish because }Mv=0),
$$

so the only part that changes with  $t$  is the linear term:

$$
2b^T(x_0+tv)=2b^T x_0 +2t(b^T v).
$$

If  $b^T v\neq 0$ , then by choosing  $t\to -\infty$  or  $+\infty$  with the right sign, you push the expression to  $-\infty$ .

So to avoid  $-\infty$ , we need:

$$
b^T v =0 \quad \text{for all } v\in\ker(M). \tag{range condition in dot-product form}
$$

For symmetric matrices,  $\mathcal R(M)=\ker(M)^\perp$ . So the condition “ $b$  orthogonal to every vector in  $\ker(M)$ ” is exactly:

$$
b\in \mathcal R(M). \tag{range condition}
$$

That is the second condition you see on the page.

So the dual function is finite only if:

1.   $A+\lambda I\succeq 0$ 
2.   $b\in\mathcal R(A+\lambda I)$ 

Otherwise  $g(\lambda)=-\infty$ .

This is not random “technicality”—it’s literally preventing unbounded descent along flat directions.

* * *

6) When finite: compute the minimum value using completing the square
---------------------------------------------------------------------

Assume  $M\succeq 0$  and  $b\in\mathcal R(M)$ . We compute:

$$
\inf_x \; x^T M x +2b^T x.
$$

### 6.1 Warm-up: if  $M\succ 0$  (invertible)

If  $M$  is positive definite, standard calculus gives the minimizer.

Take gradient w.r.t.  $x$ :

*   Gradient of  $x^T M x$  is  $2Mx$  (since  $M$  symmetric).
*   Gradient of  $2b^T x$  is  $2b$ .

Set to zero:

$$
2Mx +2b =0 \quad\Rightarrow\quad Mx = -b.
$$

So:

$$
x^\star = -M^{-1} b.
$$

Plug back in to get minimum value (complete square):

$$
x^T M x +2b^T x = (x+M^{-1}b)^T M (x+M^{-1}b) - b^T M^{-1} b.
$$

The first term is  $\ge 0$  and achieves 0 at  $x=-M^{-1}b$ . So the infimum is:

$$
- b^T M^{-1} b.
$$

### 6.2 General case:  $M\succeq 0$  possibly singular → pseudoinverse

If  $M$  is singular,  $M^{-1}$  doesn’t exist. The correct replacement is the **Moore–Penrose pseudoinverse**  $M^\dagger$ .

Facts you need (and what they mean):

*    $M^\dagger$  acts like the inverse on the range space, and acts like 0 on the nullspace.
*   If  $b\in\mathcal R(M)$ , then the equation  $Mx=-b$  is solvable.
*   One particular solution with minimum norm is  $x_0=-M^\dagger b$ .
*   All solutions are  $x_0+v$  with  $v\in\ker(M)$ .

When the range condition holds, the same completion-of-square result becomes:

$$
\inf_x \left(x^T M x +2b^T x\right)= -b^T M^\dagger b.
$$

So:

$$
g(\lambda)= -b^T (A+\lambda I)^\dagger b -\lambda
$$

under the two feasibility conditions; otherwise  $-\infty$ . Exactly the page.

* * *

7) The dual problem (explicit form)
-----------------------------------

Now we can write the dual problem:

$$
\begin{aligned} \maximize_{\lambda\in\mathbb R}\quad & -b^T(A+\lambda I)^\dagger b -\lambda\\ \text{subject to}\quad & \lambda\ge 0,\\ & A+\lambda I\succeq 0,\\ & b\in\mathcal R(A+\lambda I). \end{aligned} \tag{D explicit}
$$

This is their (5.33).

Important subtle point: the “dual feasible set” is not “all  $\lambda\ge 0$ .” It’s those  $\lambda\ge 0$  that also make  $A+\lambda I\succeq 0$  and satisfy the range condition. For other  $\lambda$ ,  $g(\lambda)=-\infty$ , so they’re irrelevant (they would never maximize).

* * *

8) Why the constraint  $A+\lambda I\succeq 0$  is simple in 1D
--------------------------------------------------------------

Right now it looks like a matrix inequality. But eigenvalues make it scalar.

Let  $\lambda_{\min}(A)$  be the smallest eigenvalue of  $A$ . Then eigenvalues of  $A+\lambda I$  are  $\lambda_i(A)+\lambda$ . So:

$$
A+\lambda I\succeq 0 \iff \lambda_i(A)+\lambda \ge 0\ \forall i \iff \lambda \ge -\lambda_{\min}(A).
$$

So dual feasibility forces:

$$
\lambda \ge \max\{0,\,-\lambda_{\min}(A)\}.
$$

That’s why the dual is really just a scalar maximization over an interval.

* * *

9) Eigen-decomposition rewrite: why the dual objective becomes a sum
--------------------------------------------------------------------

Now we compute  $b^T(A+\lambda I)^\dagger b$  in eigen-coordinates.

Let  $A = Q\Lambda Q^T$  with:

*    $Q=[q_1,\dots,q_n]$  orthonormal eigenvectors,
*    $\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$  eigenvalues.

Then:

$$
A+\lambda I = Q(\Lambda+\lambda I)Q^T
$$

where  $\Lambda+\lambda I=\mathrm{diag}(\lambda_1+\lambda,\dots,\lambda_n+\lambda)$ .

The pseudoinverse is:

$$
(A+\lambda I)^\dagger = Q(\Lambda+\lambda I)^\dagger Q^T,
$$

and  $(\Lambda+\lambda I)^\dagger$  is diagonal with entries:

$$
(\lambda_i+\lambda)^\dagger= \begin{cases} \frac{1}{\lambda_i+\lambda}, & \lambda_i+\lambda\neq 0\\ 0, & \lambda_i+\lambda=0. \end{cases}
$$

Write  $b$  in that basis:  $b=\sum_i \beta_i q_i$  with  $\beta_i=q_i^T b$ .

Then:

$$
b^T(A+\lambda I)^\dagger b = \sum_{i:\lambda_i+\lambda\neq 0} \frac{\beta_i^2}{\lambda_i+\lambda}.
$$

So the dual objective is:

$$
-\sum_{i=1}^n \frac{(q_i^T b)^2}{\lambda_i+\lambda} -\lambda,
$$

with the “convention” the page mentions:

*   If  $\lambda_i+\lambda=0$  and  $q_i^T b=0$ , treat the fraction as 0.
*   If  $\lambda_i+\lambda=0$  but  $q_i^T b\neq 0$ , the dual value becomes  $-\infty$  (since the range condition fails), which they encode by treating it as  $+\infty$  inside the sum.

This is not cosmetic: it’s exactly encoding  $b\in\mathcal R(A+\lambda I)$ .

* * *

10) Weak duality vs strong duality: crystal-clear meanings here
---------------------------------------------------------------

### 10.1 Weak duality here

For any  $\lambda$  feasible in the dual:

$$
g(\lambda)\le p^\star.
$$

So the dual optimal value  $d^\star$  satisfies:

$$
d^\star \le p^\star.
$$

That is always true.

### 10.2 Strong duality here (the surprising claim)

Strong duality means:

$$
d^\star = p^\star.
$$

So solving the dual (a convex 1D problem) gives the exact global minimum of the primal, even though the primal is nonconvex.

This is the “rare occasion” claim on the page.

* * *

11) Why strong duality holds _in this special nonconvex case_ (the real intuition)
----------------------------------------------------------------------------------

I’ll give you the core mechanism without pretending we already proved the S-lemma.

### 11.1 What usually breaks in nonconvex duality

In nonconvex problems, the Lagrangian relaxation can be too loose: the dual lower bound may sit strictly below the primal optimum, leaving a positive gap. That gap is because the constraint relaxation can’t “carve out” the exact feasible set tightly enough using a single multiplier.

### 11.2 What is special about “one quadratic constraint”

Here the feasible set is a single quadratic inequality (a ball/ellipsoid), and the objective is quadratic. The interaction of two quadratic forms has a strong algebraic structure: essentially, “checking nonnegativity of one quadratic form over the set defined by another” can be reduced to a single multiplier condition. That’s the heart of the S-lemma / trust-region exactness phenomenon.

Concretely, at optimum you can find a  $\lambda^\star$  such that:

*    $A+\lambda^\star I\succeq 0$  (so the Lagrangian becomes convex in  $x$ ),
*   the minimizer of the Lagrangian in  $x$  actually lands on/inside the ball in exactly the right way,
*   complementary slackness ties the constraint activity to  $\lambda^\star$ .

This creates a “perfectly tight” lower bound.

### 11.3 Slater condition here (why the regularity holds)

Slater for inequality constraints means: there exists a strictly feasible point  $x$  with  $x^T x < 1$ . Here  $x=0$  works:

$$
0^T0 =0 < 1.
$$

So the interior exists. That’s the regularity condition needed by the theorem the page cites.

* * *

12) KKT conditions here: how dual optimum connects to primal optimum
--------------------------------------------------------------------

Even though the primal is nonconvex, for this structure the KKT conditions still describe the global optimum when strong duality holds.

KKT conditions for our single constraint problem:

1.  Primal feasibility:  $\|x^\star\|^2 \le 1$ .
2.  Dual feasibility:  $\lambda^\star\ge 0$ .
3.  Stationarity:  $\nabla_x L(x^\star,\lambda^\star)=0$ .
4.  Complementary slackness:  $\lambda^\star(\|x^\star\|^2-1)=0$ .

Let’s unpack stationarity:

$$
L(x,\lambda)=x^T(A+\lambda I)x+2b^T x-\lambda.
$$

Gradient w.r.t.  $x$ :

*    $\nabla_x (x^T(A+\lambda I)x)=2(A+\lambda I)x$ .
*    $\nabla_x(2b^T x)=2b$ .

So stationarity:

$$
2(A+\lambda^\star I)x^\star +2b =0 \quad\Longleftrightarrow\quad (A+\lambda^\star I)x^\star = -b. \tag{stationarity eq}
$$

This is the same equation we got when minimizing the Lagrangian.

Complementary slackness gives two regimes:

*   If  $\lambda^\star>0$ , then  $\|x^\star\|^2=1$  (optimum on boundary).
*   If  $\lambda^\star=0$ , then constraint may be slack, and  $x^\star$  is an unconstrained minimizer that happens to satisfy  $\|x^\star\|\le 1$ .

This is the practical way the dual solution yields the primal solution.

* * *

13) What you should take away as “zero-to-hero” mental model
------------------------------------------------------------

1.  The primal problem is “minimize a quadratic over a ball.” Nonconvexity can come from  $A$  having negative eigenvalues.
2.  The Lagrangian adds  $\lambda(\|x\|^2-1)$ . For  $\lambda\ge 0$ , it never increases the objective on feasible points, so it can produce lower bounds.
3.  The dual function  $g(\lambda)$  is the best lower bound you can get from that  $\lambda$ , by minimizing over all  $x$ .
4.  Computing  $g(\lambda)$  requires understanding when a quadratic has a finite minimum:
    *   If  $A+\lambda I$  isn’t PSD, the quadratic goes to  $-\infty$ .
    *   If it’s PSD but singular, you must avoid linear drift along the nullspace:  $b$  must be in the range.
    *   When finite, the minimum is  $-b^T(A+\lambda I)^\dagger b$ .
5.  The dual problem is a 1D concave maximization (therefore “convex optimization” in the standard sense).
6.  The miracle: for this structure (quadratic objective + one quadratic inequality + Slater), the dual lower bound is tight → strong duality.

* * *

If you want the next step in maximal rigor, the natural continuation is: prove the “finite iff PSD + range” claim in full detail using spectral decomposition; then derive the pseudoinverse completion-of-square formula explicitly; then state and prove (or at least derive) the exactness theorem (S-lemma flavor) specialized to the trust-region subproblem. That’s the point where the “rare occasion strong duality holds for nonconvex” becomes a theorem you can reproduce, not just a claim.

## Response:
Cool—let’s go slower, more “newcomer-proof,” and make every single step feel inevitable. I’m going to treat this like building a small machine: define the parts, show what each part does, then show how the whole machine outputs (5.33) from (5.32). Along the way I’ll explain the “strange” conditions (PSD, range, pseudoinverse), and why “maximize  $g(\lambda)$ ” is the right thing.

* * *

1) Start at absolute basics: what are primal, dual, optimal value?
------------------------------------------------------------------

### 1.1 “Primal problem” is just the original problem you care about

The primal here is:

$$
\begin{aligned} \min_{x\in\mathbb R^n} \quad & f(x):=x^T A x + 2b^T x\\ \text{s.t.}\quad & x^T x \le 1. \end{aligned} \tag{P}
$$
*   Think of  $f(x)$  as “cost”.
*   Constraint  $x^T x\le 1$  means you can’t choose  $x$  too large: it must live inside the unit ball.

### 1.2 Feasible set and optimal value

Define the feasible set:

$$
\mathcal F := \{x\in\mathbb R^n : x^T x \le 1\}.
$$

Then the primal optimal value is:

$$
p^\star := \inf_{x\in \mathcal F} f(x).
$$

Why “inf” not “min”? In general problems the minimum might not be attained. Here (closed ball + continuous function) it actually is attained, but “inf” is the clean definition.

### 1.3 Why this primal can be nonconvex

A quadratic form  $x^T A x$  curves according to eigenvalues of  $A$ :

*   If  $A\succeq 0$  (no negative eigenvalues), then  $x^T A x$  is bowl-shaped → convex.
*   If  $A$  has a negative eigenvalue, then in that eigen-direction it bends downward → not convex.

So (P) can be nonconvex even though the feasible set is convex.

* * *

2) Why introduce a Lagrangian at all?
-------------------------------------

This is the main conceptual leap, so we do it carefully.

### 2.1 Goal: produce _lower bounds_ on  $p^\star$ 

If you can compute some number  $L$  such that  $L\le p^\star$ , that’s a certified lower bound on the best possible cost.

If you can make this bound as large as possible, you get the tightest possible lower bound. That’s the dual.

So duality is basically: “manufacture lower bounds in a systematic way.”

### 2.2 The trick: add the constraint with a nonnegative weight

Rewrite the constraint as:

$$
g(x):=x^T x - 1 \le 0.
$$

Now pick a scalar  $\lambda\ge 0$ . Consider:

$$
f(x)+\lambda g(x) = f(x)+\lambda(x^T x-1).
$$

Key observation (super important):

*   If  $x$  is feasible, then  $g(x)\le 0$ .
*   Multiply by  $\lambda\ge 0$ :  $\lambda g(x)\le 0$ .
*   Therefore, for feasible  $x$ ,
    
$$
f(x)+\lambda g(x) \le f(x).
$$

So this new expression is always **at most** the true objective on feasible points. That is exactly how lower bounds appear.

* * *

3) Define the Lagrangian precisely and simplify it
--------------------------------------------------

### 3.1 Definition

The **Lagrangian** is

$$
L(x,\lambda) := f(x) + \lambda g(x) = x^T A x +2b^T x + \lambda(x^T x-1), \qquad \lambda\ge 0.
$$

### 3.2 Simplify algebraically

Group the quadratic terms:

*    $x^T A x + \lambda x^T x = x^T (A+\lambda I)x$ .

So:

$$
L(x,\lambda)=x^T(A+\lambda I)x +2b^T x - \lambda. \tag{L}
$$

This is crucial because for a fixed  $\lambda$ ,  $L(\cdot,\lambda)$  is a plain quadratic function of  $x$ .

* * *

4) Dual function  $g(\lambda)$ : definition and meaning
-------------------------------------------------------

### 4.1 Definition

The **dual function** is:

$$
g(\lambda):=\inf_{x\in\mathbb R^n} L(x,\lambda). \tag{dual function}
$$

Note: inf over _all_  $x$ , not just feasible  $x$ .

### 4.2 Why does this give a lower bound on  $p^\star$ ?

Take any feasible  $x\in\mathcal F$ . We already argued:

$$
L(x,\lambda)\le f(x).
$$

Now since  $g(\lambda)$  is the infimum of  $L(x,\lambda)$  over all  $x$ ,

$$
g(\lambda)\le L(x,\lambda)\le f(x) \quad \text{for every feasible }x.
$$

Take infimum over feasible  $x$ :

$$
g(\lambda)\le p^\star.
$$

So: **every**  $\lambda\ge 0$  produces a valid lower bound  $g(\lambda)$ .

This is weak duality in its most basic form.

* * *

5) Dual problem: “best lower bound” = maximize  $g(\lambda)$ 
-------------------------------------------------------------

### 5.1 Definition

Since  $g(\lambda)\le p^\star$  always, the “best bound” is the largest one:

$$
d^\star := \sup_{\lambda\ge 0} g(\lambda).
$$

The **dual problem** is:

$$
\max_{\lambda\ge 0} g(\lambda). \tag{D}
$$

### 5.2 Weak vs strong duality

*   Weak duality:  $d^\star\le p^\star$  always.
*   Strong duality:  $d^\star=p^\star$  (gap 0).

Nonconvex problems often violate strong duality. The page is about a case where it still holds.

But we still need to compute  $g(\lambda)$ .

* * *

6) Compute  $g(\lambda)=\inf_x L(x,\lambda)$  in complete detail
----------------------------------------------------------------

We need to minimize in  $x$ :

$$
L(x,\lambda)=x^T(A+\lambda I)x +2b^T x -\lambda.
$$

The  $-\lambda$  doesn’t depend on  $x$ , so:

$$
g(\lambda)=\left(\inf_x \big[x^T M x +2b^T x\big]\right)-\lambda, \quad M:=A+\lambda I.
$$

So focus on:

$$
\inf_x \big[x^T M x +2b^T x\big]. \tag{*}
$$

This is a quadratic function of  $x$ . The shape depends entirely on the matrix  $M$ .

* * *

### 6.1 First critical question: can the infimum be  $-\infty$ ?

Yes—if the quadratic opens downward in some direction.

#### If  $M$  is not PSD, then inf is  $-\infty$ 

“ $M\succeq 0$ ” means:

$$
x^T M x \ge 0 \quad \forall x.
$$

If this fails, then there exists some  $v\neq 0$  with  $v^T M v <0$ .

Take  $x=t v$ . Then:

$$
x^T M x +2b^T x = t^2(v^T M v) +2t(b^T v).
$$

As  $t\to\infty$ , the  $t^2(v^T M v)$  dominates and goes to  $-\infty$ . So the infimum is  $-\infty$ .

Conclusion:

$$
\inf_x (\cdots) = -\infty\quad \text{if } M \not\succeq 0.
$$

So for dual function to be finite, we must have:

$$
A+\lambda I \succeq 0. \tag{condition 1}
$$

* * *

### 6.2 Second critical question: what if  $M\succeq 0$  but singular?

This is subtler and is exactly where the “range condition” comes from.

If  $M\succeq 0$  but singular, it has a nonzero nullspace:

$$
\ker(M):=\{v: Mv=0\}\neq\{0\}.
$$

Pick  $v\in\ker(M)$ ,  $v\neq 0$ .  
Then:

$$
(tv)^T M (tv)= t^2 v^T M v =0.
$$

So along the line  $x=x_0+tv$ , the quadratic part doesn’t grow at all. Only the linear term changes:

$$
2b^T(x_0+tv)=2b^T x_0 +2t(b^T v).
$$
*   If  $b^T v \neq 0$ , then by choosing  $t\to -\infty$  (or  $+\infty$ ) you make this go to  $-\infty$ .

So to prevent  $-\infty$ , we need:

$$
b^T v =0 \quad \forall v\in\ker(M). \tag{condition 2a}
$$

For symmetric  $M$ , there is a standard linear algebra fact:

$$
\mathcal R(M) = \ker(M)^\perp.
$$

So “ $b$  is orthogonal to  $\ker(M)$ ” is equivalent to:

$$
b\in\mathcal R(M). \tag{condition 2}
$$

This is exactly the page’s condition  $b\in\mathcal R(A+\lambda I)$ .

So finiteness requires both conditions:

1.   $A+\lambda I\succeq 0$ 
2.   $b\in \mathcal R(A+\lambda I)$ 

Otherwise  $g(\lambda)=-\infty$ .

* * *

7) Now compute the finite value: completing the square with pseudoinverse
-------------------------------------------------------------------------

Assume  $M\succeq 0$  and  $b\in\mathcal R(M)$ .

### 7.1 Minimizer from first-order optimality (stationarity)

Take derivative w.r.t.  $x$ :

*    $\nabla_x (x^T M x)=2Mx$  (since  $M$  symmetric),
*    $\nabla_x (2b^T x)=2b$ .

Set to zero:

$$
2Mx + 2b =0 \quad\Rightarrow\quad Mx=-b. \tag{stationarity}
$$
*   If  $M$  invertible:  $x^\star=-M^{-1}b$ .
*   If  $M$  singular: solutions exist iff  $b\in\mathcal R(M)$  (exactly our condition). Then the “canonical” solution is  $x^\star=-M^\dagger b$ .

### 7.2 Value at the minimum

The minimum value of  $x^T M x +2b^T x$  is:

$$
- b^T M^\dagger b.
$$

So:

$$
g(\lambda)= -b^T(A+\lambda I)^\dagger b - \lambda
$$

under the conditions; otherwise  $-\infty$ .

That matches the page precisely.

* * *

8) The dual problem (5.33) is now fully derived
-----------------------------------------------

$$
\begin{aligned} \maximize_{\lambda}\quad & -b^T(A+\lambda I)^\dagger b - \lambda\\ \text{s.t.}\quad & \lambda\ge 0,\\ & A+\lambda I\succeq 0,\\ & b\in \mathcal R(A+\lambda I). \end{aligned} \tag{5.33}
$$

You now know where every piece came from:

*   objective came from minimizing Lagrangian over  $x$ ,
*   PSD/range came from avoiding  $-\infty$ ,
*    $\lambda\ge 0$  came from inequality multiplier sign.

* * *

9) Eigenvalue form: unpacking the “sum” formula
-----------------------------------------------

Let  $A$  have eigenpairs  $(\lambda_i,q_i)$  with orthonormal  $q_i$ .

Write:

$$
b = \sum_{i=1}^n \beta_i q_i,\quad \beta_i:=q_i^T b.
$$

Then:

$$
A+\lambda I \text{ has eigenvalues } \lambda_i+\lambda \text{ with same eigenvectors }q_i.
$$

So:

$$
(A+\lambda I)^\dagger \text{ has eigenvalues } \begin{cases} \frac{1}{\lambda_i+\lambda} & \lambda_i+\lambda\neq 0\\ 0 & \lambda_i+\lambda=0. \end{cases}
$$

Therefore:

$$
b^T(A+\lambda I)^\dagger b = \sum_{i:\lambda_i+\lambda\neq 0} \frac{\beta_i^2}{\lambda_i+\lambda}.
$$

And the dual objective becomes:

$$
-\sum_i \frac{(q_i^T b)^2}{\lambda_i+\lambda} -\lambda,
$$

with the convention about  $0/0$  and nonzero/0 encoding the range condition.

* * *

10) Strong duality: what it means here, why it’s surprising, and the reason
---------------------------------------------------------------------------

### 10.1 Meaning

Strong duality here means:

$$
p^\star = d^\star.
$$

So the convex 1D dual problem yields the exact minimum of the nonconvex primal.

### 10.2 Why it holds (high-level but correct)

This trust-region subproblem is one of the classic “hidden convexity” cases: quadratic objective + exactly one quadratic inequality constraint. Under a mild interior-feasibility condition (Slater), the Lagrangian dual becomes exact (no gap). The page cites the relevant theorem.

Here Slater holds because  $x=0$  strictly satisfies  $x^Tx<1$ .

* * *

If you want, the next ultra-granular step is: derive (not just cite) the exactness theorem specialized to this case via the S-lemma and show explicitly how solving for  $\lambda^\star$  gives you  $x^\star$  through  $(A+\lambda^\star I)x^\star=-b$  and  $\|x^\star\|\le 1$  with complementary slackness. That’s where this becomes a fully reproducible “algorithmic recipe,” not just theory.

## Response:
Thought for 22s

### Problem 5.3 (one inequality constraint): derive the dual in terms of the conjugate  $f^\*$ , without assuming  $f$  is convex; explain why the dual is convex

We start from the _primal_ problem (as written in the screenshot):

$$
\begin{aligned} \minimize_{x\in\mathbb R^n}\quad & c^T x\\ \text{subject to}\quad & f(x)\le 0, \end{aligned} \qquad c\neq 0. \tag{P}
$$

I’ll build the dual from first principles, and I’ll be explicit about where we do _not_ need convexity of  $f$ .

* * *

1) Definitions we need (no convexity assumptions yet)
-----------------------------------------------------

### 1.1 Lagrangian for one inequality

For an inequality constraint  $f(x)\le 0$ , the Lagrangian is defined as

$$
L(x,\lambda)=c^T x+\lambda f(x), \qquad \lambda\ge 0.
$$

Why  $\lambda\ge 0$ ? Because if  $x$  is feasible, then  $f(x)\le 0$ , so  $\lambda f(x)\le 0$  whenever  $\lambda\ge 0$ . This is what guarantees lower bounds (weak duality).

### 1.2 Dual function  $g(\lambda)$ 

The dual function is

$$
g(\lambda)=\inf_{x\in\mathbb R^n} L(x,\lambda)=\inf_x \big(c^T x+\lambda f(x)\big).
$$

This definition also does **not** require  $f$  to be convex.

### 1.3 Fenchel conjugate  $f^\*$  (defined for any function)

The Fenchel conjugate of  $f:\mathbb R^n\to\mathbb R\cup\{+\infty\}$  is

$$
f^\*(y)=\sup_{x\in\mathbb R^n}\big(y^T x - f(x)\big).
$$

This is defined for any  $f$ , convex or not. A crucial fact: ** $f^\*$  is always convex** (as a supremum of affine functions in  $y$ ). This is one of the keys to why the resulting dual is convex.

* * *

2) Compute  $g(\lambda)$  in terms of  $f^\*$ 
----------------------------------------------

We want:

$$
g(\lambda)=\inf_x \left(c^T x+\lambda f(x)\right).
$$

### 2.1 Deal with the case  $\lambda=0$ 

If  $\lambda=0$ ,

$$
g(0)=\inf_x c^T x.
$$

Since  $c\neq 0$ , the linear function  $c^T x$  is unbounded below (take  $x=-t c$ , then  $c^T x=-t\|c\|^2\to -\infty$ ). So

$$
g(0)=-\infty.
$$

So any optimal dual solution (if it exists) will never choose  $\lambda=0$ . Effectively, we only care about  $\lambda>0$ .

### 2.2 Assume  $\lambda>0$  and rewrite using a “sup”

Start with

$$
g(\lambda)=\inf_x \left(c^T x+\lambda f(x)\right).
$$

Multiply and divide the linear term by  $\lambda$ :

$$
c^T x+\lambda f(x)=\lambda\left(\frac{c^T x}{\lambda}+f(x)\right).
$$

So

$$
g(\lambda)=\lambda\inf_x \left(f(x)+\left(\frac{c}{\lambda}\right)^T x\right).
$$

Now turn an inf into a sup using  $\inf u = -\sup(-u)$ :

$$
\inf_x \left(f(x)+\left(\frac{c}{\lambda}\right)^T x\right) = -\sup_x \left(-f(x)-\left(\frac{c}{\lambda}\right)^T x\right).
$$

So

$$
g(\lambda)= -\lambda\sup_x \left(\left(-\frac{c}{\lambda}\right)^T x - f(x)\right).
$$

But the expression inside the  $\sup$  is exactly the conjugate definition with  $y=-c/\lambda$ :

$$
f^\*\!\left(-\frac{c}{\lambda}\right) = \sup_x\left(\left(-\frac{c}{\lambda}\right)^T x - f(x)\right).
$$

Therefore, for  $\lambda>0$ ,

$$
\boxed{ g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). } \tag{1}
$$

No convexity assumption on  $f$  was used anywhere—only the definition of conjugate.

### 2.3 Domain/feasibility interpretation

If  $f^\*(-c/\lambda)=+\infty$ , then  $g(\lambda)=-\infty$ . So “dual feasibility” effectively includes “ $-c/\lambda\in\mathrm{dom}(f^\*)$ ”.

* * *

3) Write the dual problem explicitly
------------------------------------

The dual problem is always:

$$
\max_{\lambda\ge 0} g(\lambda).
$$

We already know  $g(0)=-\infty$ , so we can restrict to  $\lambda>0$ . Using (1):

$$
\boxed{ \begin{aligned} \maximize_{\lambda>0}\quad & -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). \end{aligned} } \tag{D}
$$

That is the clean “in terms of  $f^\*$ ” answer.

A very common equivalent form flips the sign and turns it into a minimization:

$$
\boxed{ \begin{aligned} \minimize_{\lambda>0}\quad & \lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). \end{aligned} } \tag{D'}
$$

Same problem: maximizing a quantity is equivalent to minimizing its negative.

* * *

4) Why this dual is a convex optimization problem
-------------------------------------------------

This is the part you explicitly asked to justify, especially since we did **not** assume  $f$  is convex.

There are two layers:

1.  **General duality fact**:  $g(\lambda)$  is always concave in  $\lambda$ , so maximizing it is a convex optimization problem (concave maximization over a convex set).
2.  **Specific structural fact in terms of  $f^\*$ **:  $\lambda f^\*(-c/\lambda)$  is the _perspective_ of the convex function  $f^\*$ , hence it is convex in  $\lambda$ . Therefore minimizing it is convex.

I’ll unpack both, because each teaches something different.

* * *

### 4.1 Concavity of the dual function  $g(\lambda)$  (works for any  $f$ )

Fix any  $x$ . The Lagrangian as a function of  $\lambda$  is

$$
L(x,\lambda)=c^T x+\lambda f(x),
$$

which is **affine** in  $\lambda$  (a straight line): slope  $f(x)$ , intercept  $c^T x$ .

Now the dual function is the pointwise infimum over  $x$ :

$$
g(\lambda)=\inf_x L(x,\lambda).
$$

A fundamental convex-analysis fact: **the pointwise infimum of affine functions is concave**. Intuition: take a bunch of straight lines; their “lower envelope” bends downward (concave).

So  $g$  is concave on  $\{\lambda\ge 0\}$ , regardless of whether  $f$  is convex.

Therefore, the dual problem

$$
\max_{\lambda\ge 0} g(\lambda)
$$

is a **convex optimization problem** (maximize concave over convex domain).

That’s already enough.

* * *

### 4.2 Convexity via the “perspective” of  $f^\*$  (more explicit)

Now use the explicit formula:

$$
g(\lambda)= -\lambda f^\*\!\left(-\frac{c}{\lambda}\right),\quad \lambda>0.
$$

Define

$$
\phi(\lambda):=\lambda f^\*\!\left(-\frac{c}{\lambda}\right),\quad \lambda>0.
$$

Then the dual is  $\min_{\lambda>0} \phi(\lambda)$  (same as maximizing  $-\phi(\lambda)$ ).

Key fact: if  $h(y)$  is convex, then its **perspective**  $p(t):=t\,h(z/t)$  (with fixed  $z$ , variable  $t>0$ ) is convex in  $t$ . Here:

*    $h = f^\*$ , which is convex even if  $f$  isn’t.
*    $z = -c$ .
*    $t = \lambda$ .

So  $\phi(\lambda)$  is convex in  $\lambda$ . Therefore  $\min_{\lambda>0}\phi(\lambda)$  is a convex minimization problem.

If you want the “why” of the perspective fact in one sentence: the epigraph of the perspective is a linear image of the epigraph of  $h$ , and linear images preserve convexity.

So the dual is convex _because  $f^\*$  is convex_, and conjugates are convex no matter what.

* * *

5) Final boxed answer
---------------------

**Dual function:**

*    $g(0)=-\infty$  (since  $c\neq 0$ ).
*   For  $\lambda>0$ ,
    
$$
\boxed{g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right).}
$$

**Dual problem:**

$$
\boxed{ \maximize_{\lambda>0}\ -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right) \quad\text{equivalently}\quad \minimize_{\lambda>0}\ \lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). }
$$

**Why convex:**  $f^\*$  is convex for any  $f$ , and  $\lambda f^\*(-c/\lambda)$  is the perspective of  $f^\*$ , hence convex in  $\lambda$ ; equivalently  $g$  is concave as an infimum of affine functions.

* * *

Next message, I’ll do **5.4** (LP dual interpretation via relaxed halfspaces) in the same “from definitions, no skipped steps” style.

## Response:
Thought for 1m 30s

### Problem 5.4 — Interpretation of LP dual via relaxed problems (geometric lower-bound view)

We are given the inequality-form LP:

$$
\begin{aligned} \minimize_{x\in\mathbb R^n}\quad & c^T x\\ \text{subject to}\quad & Ax \le b, \end{aligned} \qquad A\in\mathbb R^{m\times n},\ b\in\mathbb R^m. \tag{P}
$$

Let  $p^\star$  denote its optimal value.

The exercise’s idea is: **build a family of “relaxed” problems that are easier (only one constraint)**, each giving a **lower bound** on  $p^\star$ . Then show that **choosing the best lower bound** across that family is exactly the **dual LP**.

I’ll do this from definitions, step-by-step.

* * *

1) Rewrite the constraints in a way that makes geometry obvious
---------------------------------------------------------------

Let the rows of  $A$  be  $a_1^T,\dots,a_m^T$ . Then

$$
Ax\le b \quad\Longleftrightarrow\quad a_i^T x \le b_i \ \ \text{for } i=1,\dots,m.
$$

So the feasible set is an intersection of halfspaces:

$$
\mathcal F=\bigcap_{i=1}^m \{x: a_i^T x\le b_i\}.
$$

Geometrically: each inequality defines a halfspace; the feasible region is their intersection (a polyhedron).

* * *

2) Build a _relaxed_ problem by combining constraints with nonnegative weights
------------------------------------------------------------------------------

Take any vector of weights  $w\in\mathbb R_+^m$  (meaning  $w_i\ge 0$  for all  $i$ ).

### 2.1 Why nonnegative?

Because if  $Ax\le b$ , then each component satisfies  $(Ax)_i \le b_i$ . If you multiply each inequality by a nonnegative weight and add them up, the inequality direction is preserved.

Form the weighted sum:

$$
w^T(Ax)\le w^T b.
$$

This is a **single** linear inequality.

Define the halfspace

$$
H_w:=\{x\in\mathbb R^n:\ w^T A x \le w^T b\}.
$$

Now observe the key containment:

> If  $x$  is feasible for the original LP ( $Ax\le b$ ), then it is feasible for the relaxed constraint ( $w^T Ax \le w^T b$ ).

So:

$$
\mathcal F \subseteq H_w. \tag{containment}
$$

This is exactly what the screenshot says.

### 2.2 Write  $H_w$  in a simpler “normal vector” form

Note:

$$
w^T A x = (A^T w)^T x.
$$

Let

$$
a(w):=A^T w \in \mathbb R^n,\qquad \beta(w):=b^T w \in \mathbb R.
$$

Then

$$
H_w=\{x:\ a(w)^T x \le \beta(w)\}.
$$

So  $H_w$  is a halfspace whose boundary hyperplane has normal vector  $a(w)=A^T w$ .

Also:

$$
a(w)=A^T w = \sum_{i=1}^m w_i a_i,
$$

so the halfspace normal is a **nonnegative linear combination of the original constraint normals**.

That’s the geometric meaning of “multiply constraints by  $w_i\ge 0$  and add”: you are forming a new “aggregate” halfspace that still contains the feasible region.

* * *

3) Define the relaxed problem and prove it gives a lower bound on  $p^\star$ 
-----------------------------------------------------------------------------

For each  $w\ge 0$ , define the relaxed optimization problem:

$$
\begin{aligned} \tilde p(w):=\ \inf_{x\in\mathbb R^n}\quad & c^T x\\ \text{subject to}\quad & w^T A x \le w^T b. \end{aligned} \tag{R(w)}
$$

This is “minimize the same objective, but over the larger set  $H_w$  instead of  $\mathcal F$ .”

### 3.1 Why  $\tilde p(w)\le p^\star$  (lower bound proof)

Because  $\mathcal F\subseteq H_w$ , you are minimizing over a **bigger** feasible set:

*   Minimizing over a bigger set can only make the optimum **smaller or equal**.

Formally:

$$
\tilde p(w)=\inf_{x\in H_w} c^T x \ \le\ \inf_{x\in \mathcal F} c^T x = p^\star.
$$

So every  $w\ge 0$  gives a valid lower bound  $\tilde p(w)$  on the true optimum.

This is the core “relaxation gives a bound” idea.

* * *

4) Compute  $\tilde p(w)$  explicitly (this is the crucial step)
----------------------------------------------------------------

Now we solve:

$$
\inf\{c^T x : a^T x \le \beta\} \quad\text{where } a=A^T w,\ \beta=b^T w.
$$

This is a 1-constraint linear program. The behavior is very clean:

### 4.1 Fact: a linear objective over a halfspace is usually  $-\infty$ 

A halfspace  $\{x: a^T x\le \beta\}$  extends infinitely in many directions. Unless the objective is aligned in a very specific way, you can often move forever in a direction that keeps you feasible while making  $c^T x\to -\infty$ .

So we must determine exactly when  $\tilde p(w)$  is finite.

* * *

### 4.2 When is  $\tilde p(w)$  bounded below?

Let’s reason from first principles.

We want to know if there exists a direction  $d$  such that:

1.  moving in that direction stays feasible forever, i.e.
    $$
    a^T(x+td)\le \beta\ \ \forall t\ge 0,
    $$
    which is guaranteed if  $a^T d \le 0$ ,
2.  and the objective decreases along that direction:
    $$
    c^T(x+td)=c^T x + t(c^T d)\to -\infty \quad\text{if } c^T d<0.
    $$

So if we can find some  $d$  with

$$
a^T d \le 0 \quad\text{and}\quad c^T d<0,
$$

then  $\tilde p(w)=-\infty$ .

Now, when is it _impossible_ to find such a direction? Exactly when  $c$  is a nonnegative multiple of  $-a$ . More concretely, the only way the halfspace can “control” the objective in every feasible direction is if the objective points exactly opposite the normal.

Let’s make that precise in the simplest (strongest) form used in the book’s dual:

> If  $c \neq -a$ , then  $\tilde p(w)=-\infty$ .  
> If  $c = -a$ , then  $\tilde p(w)= -\beta$ .

Because in our LP dual, we will enforce  $a=A^T w = -c$  exactly.

Let’s prove the two statements carefully.

* * *

### 4.3 Case 1: If  $A^T w \neq -c$ , then  $\tilde p(w)=-\infty$ 

Assume  $a\neq -c$ . Consider two subcases:

#### Subcase 1a:  $a=0$ 

Then the constraint is  $0 \le \beta$ , which is either:

*   infeasible if  $\beta<0$ , or
*   always true if  $\beta\ge 0$ .

If it’s always true, the relaxed feasible set is all  $\mathbb R^n$ , and since  $c\neq 0$ ,  $\inf_x c^T x=-\infty$ .

So  $\tilde p(w)=-\infty$  when  $a=0$  (given  $c\neq 0$ ).

#### Subcase 1b:  $a\neq 0$ 

Because  $a\neq -c$ , there exists some direction  $d$  such that:

*    $a^T d=0$  (move parallel to the boundary hyperplane),
*   but  $c^T d<0$  (objective decreases along that direction).

Why can we find such a  $d$ ?  
The set  $\{d: a^T d=0\}$  is an  $(n-1)$ \-dimensional subspace (all directions orthogonal to  $a$ ). If  $c$  were orthogonal to all such  $d$ , then  $c$  would have to be parallel to  $a$ . But we are assuming  $c$  is not equal to  $-a$  (and if we want the strongest statement, “not parallel in the needed direction”). In particular, unless  $c$  is exactly a scalar multiple of  $a$ , there exists a tangent direction that decreases  $c^T x$ . Pick it and you get  $-\infty$ .

Therefore, generically (and in the LP-dual derivation), if  $A^T w\neq -c$ , the relaxation gives no finite bound:  $\tilde p(w)=-\infty$ .

This matches what happens in the Lagrange dual too: the dual function becomes  $-\infty$  unless a certain coefficient equals zero.

* * *

### 4.4 Case 2: If  $A^T w = -c$ , then  $\tilde p(w)= -b^T w$ 

Now assume the special alignment:

$$
A^T w = -c. \tag{alignment}
$$

Then for any  $x\in H_w$ ,

$$
c^T x = (-A^T w)^T x = -(A^T w)^T x = -w^T A x.
$$

But the constraint  $w^T A x \le w^T b$  says:

$$
w^T A x \le w^T b \quad\Rightarrow\quad -w^T A x \ge -w^T b.
$$

So for all feasible  $x\in H_w$ ,

$$
c^T x \ge -b^T w.
$$

That proves  $-b^T w$  is a lower bound on the relaxed objective value.

Now: can we achieve equality? Yes. Because the halfspace constraint allows equality  $w^T A x = w^T b$ . If  $a=A^T w\neq 0$ , we can choose any  $x$  on the boundary hyperplane  $a^T x=\beta$ . For instance, one explicit construction is:

$$
x_0 := \frac{\beta}{\|a\|_2^2}\,a \quad\Rightarrow\quad a^T x_0 = \frac{\beta}{\|a\|^2} a^T a = \beta.
$$

So  $x_0\in H_w$  with equality. Then:

$$
c^T x_0 = -a^T x_0 = -\beta = -b^T w.
$$

Therefore the infimum equals that bound:

$$
\tilde p(w)= -b^T w \quad\text{when } A^T w=-c.
$$

So we have the explicit formula:

$$
\boxed{ \tilde p(w)= \begin{cases} -b^T w, & \text{if } w\ge 0 \text{ and } A^T w=-c,\\ -\infty, & \text{otherwise.} \end{cases}} \tag{*}
$$

This is the heart of the exercise.

* * *

5) “Best relaxation bound” = the LP dual
----------------------------------------

Now recall: every  $w\ge 0$  gives a lower bound  $\tilde p(w)\le p^\star$ . To get the best bound, we maximize  $\tilde p(w)$  over  $w\ge 0$ .

But using  $(*)$ , the only  $w$  that matter are those with  $A^T w=-c$ . For those,  $\tilde p(w)=-b^T w$ . So the “best bound” problem is:

$$
\boxed{ \begin{aligned} \maximize_{w\in\mathbb R^m}\quad & -b^T w\\ \text{subject to}\quad & A^T w = -c,\\ & w\ge 0. \end{aligned}} \tag{D}
$$

That is exactly the standard Lagrange dual (and LP dual) of the primal inequality-form LP.

So geometrically:

*    $w\ge 0$  chooses a **valid aggregate inequality**  $w^T Ax\le w^T b$  that every feasible  $x$  satisfies.
*   Requiring  $A^T w=-c$  forces the aggregate halfspace to be oriented so that minimizing  $c^T x$  over it is **bounded** and occurs on the boundary.
*   The dual objective  $-b^T w$  is precisely the optimum value of that relaxed one-constraint problem.
*   Maximizing  $-b^T w$  selects the **tightest** such lower bound.

That’s the relaxed-problem interpretation of duality.

* * *

6) Tiny geometric picture (in words, but precise)
-------------------------------------------------

*   The feasible set  $\mathcal F$  is a polyhedron (intersection of halfspaces).
*   Pick  $w\ge 0$ . You “add up” some of the constraints (with nonnegative weights) to get one halfspace  $H_w$  that still contains  $\mathcal F$ .
*   Minimizing over a larger set gives a lower bound.
*   The best lower bound comes from the halfspace whose boundary is “most supportive” to the objective direction—encoded by  $A^T w=-c$ .
*   That “best supportive halfspace” construction is exactly what dual variables are doing.

* * *

Next problem is **5.6 (Chebyshev /  $\ell_\infty$  approximation bounds)**, and I’ll keep the same ultra-granular style.

## Response:
Thought for 1m 48s

### Problem 5.6 — Lower bounds in Chebyshev ( $\ell_\infty$ ) approximation from least-squares

You have the **Chebyshev /  $\ell_\infty$ ** approximation problem

$$
\minimize_x \ \|Ax-b\|_\infty , \tag{C}
$$

with  $A\in\mathbb R^{m\times n}$ ,  $\operatorname{rank}(A)=n$  (full column rank), and  $b\in\mathbb R^m$ .  
Let  $x_{\text{ch}}$  be an optimal solution of (C) (there may be several).

You also have the **least-squares** solution

$$
x_{\text{ls}} =\arg\min_x \|Ax-b\|_2 =(A^TA)^{-1}A^T b \tag{LS}
$$

(the formula uses  $\operatorname{rank}(A)=n\Rightarrow A^TA$  invertible).

Define residuals (these are the objects we compare):

$$
r_{\text{ch}} := b-Ax_{\text{ch}}, \qquad r_{\text{ls}} := b-Ax_{\text{ls}}.
$$

The question: if you use  $x_{\text{ls}}$  instead of  $x_{\text{ch}}$ , how bad can  $\|Ax_{\text{ls}}-b\|_\infty$  be relative to the optimal  $\|Ax_{\text{ch}}-b\|_\infty$ ?

* * *

Part (a) Prove the bound  $\|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\, \|Ax_{\text{ch}}-b\|_\infty$ 
--------------------------------------------------------------------------------------------------

### Step 0: rewrite in residual language

$$
\|Ax_{\text{ls}}-b\|_\infty = \|-(b-Ax_{\text{ls}})\|_\infty=\|r_{\text{ls}}\|_\infty,
$$
 
$$
\|Ax_{\text{ch}}-b\|_\infty = \|r_{\text{ch}}\|_\infty.
$$

So the desired inequality is:

 $$
\boxed{\ \|r_{\text{ls}}\|_\infty \le \sqrt m\, \|r_{\text{ch}}\|_\infty\ }.
$$

### Step 1: use what “least squares” means (optimality in  $\ell_2$ )

By definition,  $x_{\text{ls}}$  minimizes  $\|Ax-b\|_2$ , so its residual has smallest 2-norm among all choices of  $x$ :

$$
\|r_{\text{ls}}\|_2 \le \|b-Ax\|_2 \quad \forall x.
$$

In particular, this holds for  $x=x_{\text{ch}}$ :

 $$
\boxed{\ \|r_{\text{ls}}\|_2 \le \|r_{\text{ch}}\|_2\ }. \tag{1}
$$

This is the only place we use the LS optimality.

### Step 2: relate  $\ell_\infty$  and  $\ell_2$  norms (the given inequalities)

You’re given (equivalently):

$$
\|z\|_\infty \le \|z\|_2 \le \sqrt m\,\|z\|_\infty \qquad \forall z\in\mathbb R^m. \tag{2}
$$

We will use both directions.

Apply the **left inequality**  $\|z\|_\infty \le \|z\|_2$  to  $z=r_{\text{ls}}$ :

 $$
\boxed{\ \|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2\ }. \tag{3}
$$

Apply the **right inequality**  $\|z\|_2 \le \sqrt m\,\|z\|_\infty$  to  $z=r_{\text{ch}}$ :

 $$
\boxed{\ \|r_{\text{ch}}\|_2 \le \sqrt m\,\|r_{\text{ch}}\|_\infty\ }. \tag{4}
$$

### Step 3: chain them together

Start from (3), then use (1), then (4):

$$
\|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \le \|r_{\text{ch}}\|_2 \le \sqrt m\,\|r_{\text{ch}}\|_\infty.
$$

That is exactly

 $$
\boxed{\ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty\ }.
$$

So LS is at worst a factor  $\sqrt m$  suboptimal in  $\ell_\infty$ \-error.

* * *

Part (b) Use the dual (5.104) to get lower bounds, and compare to (a)
---------------------------------------------------------------------

The problem gives (as known dual for  $\ell_\infty$  approximation):

$$
\begin{aligned} \maximize_{\nu\in\mathbb R^m}\quad & b^T \nu\\ \text{subject to}\quad & \|\nu\|_1 \le 1,\\ & A^T \nu = 0. \end{aligned} \tag{D\(_\infty\)}
$$

and states: **any feasible  $\nu$ ** gives a **lower bound**  $b^T\nu$  on the optimal Chebyshev value  $\|Ax_{\text{ch}}-b\|_\infty$ .

I’ll (i) justify that lower bound statement cleanly, (ii) prove  $\hat\nu,\tilde\nu$  are feasible, (iii) compute the bounds, (iv) compare.

* * *

### (b.1) Why feasible  $\nu$  gives a lower bound (weak duality in one line)

A key identity about the  $\ell_\infty$  norm is:

$$
\|u\|_\infty = \max_{\|\nu\|_1\le 1} \nu^T u. \tag{5}
$$

This is the “dual norm” relationship: the dual norm of  $\|\cdot\|_\infty$  is  $\|\cdot\|_1$ .

From (5), for any fixed  $u$  and any  $\nu$  with  $\|\nu\|_1\le 1$ ,

$$
\nu^T u \le \|u\|_\infty. \tag{6}
$$

Now plug  $u = Ax-b$ :

$$
\nu^T(Ax-b) \le \|Ax-b\|_\infty.
$$

If also  $A^T\nu=0$ , then  $\nu^T A x = x^T A^T \nu = 0$ , so

$$
\nu^T(Ax-b) = -\nu^T b.
$$

Thus for any  $x$  and any feasible  $\nu$  (meaning  $\|\nu\|_1\le 1$ ,  $A^T\nu=0$ ):

$$
-\nu^T b \le \|Ax-b\|_\infty \quad\Longleftrightarrow\quad b^T\nu \le \|Ax-b\|_\infty.
$$

Now minimize the right-hand side over  $x$ :

$$
b^T\nu \le \min_x \|Ax-b\|_\infty = \|Ax_{\text{ch}}-b\|_\infty.
$$

So indeed:

 $$
\boxed{\ \text{If } \|\nu\|_1\le 1,\ A^T\nu=0,\ \text{then } b^T\nu \le \|Ax_{\text{ch}}-b\|_\infty.\ } \tag{LB}
$$

That’s the “any feasible  $\nu$  gives a lower bound” statement.

* * *

### (b.2) Show  $\hat\nu$  and  $\tilde\nu$  are feasible

You are told (and must use)  $r_{\text{ls}} = b-Ax_{\text{ls}}\neq 0$ . Define:

$$
\hat\nu := -\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \qquad \tilde\nu := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}.
$$

We must check the two feasibility conditions:

1.   $\|\nu\|_1 \le 1$ 
2.   $A^T\nu = 0$ 

#### Condition 1:  $\ell_1$ \-norm

Because we divided by  $\|r_{\text{ls}}\|_1$ ,

$$
\|\tilde\nu\|_1 =\left\|\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right\|_1 =\frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1} =1,
$$

and similarly  $\|\hat\nu\|_1=1$ . So both satisfy  $\|\nu\|_1\le 1$ .

#### Condition 2:  $A^T\nu=0$  (this uses the normal equations for LS)

Least squares solves:

$$
\min_x \|Ax-b\|_2^2.
$$

Differentiate:

$$
\|Ax-b\|_2^2 = (Ax-b)^T(Ax-b).
$$

Gradient w.r.t.  $x$  is:

$$
\nabla_x \|Ax-b\|_2^2 = 2A^T(Ax-b).
$$

At the minimizer  $x_{\text{ls}}$ ,

$$
2A^T(Ax_{\text{ls}}-b)=0 \quad\Longrightarrow\quad A^T(Ax_{\text{ls}}-b)=0.
$$

But  $Ax_{\text{ls}}-b = -(b-Ax_{\text{ls}})= -r_{\text{ls}}$ . So

$$
A^T(-r_{\text{ls}})=0 \quad\Longrightarrow\quad \boxed{A^T r_{\text{ls}}=0.} \tag{7}
$$

Now

$$
A^T \tilde\nu = A^T \left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{A^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} =0,
$$

and similarly  $A^T\hat\nu=0$ .

So both  $\hat\nu$  and  $\tilde\nu$  are feasible for the dual.

* * *

### (b.3) Compute the two lower bounds  $b^T\hat\nu$  and  $b^T\tilde\nu$ 

We want to compute  $b^T\nu$  for  $\nu=\pm r_{\text{ls}}/\|r_{\text{ls}}\|_1$ .

A clean trick: express  $b$  using the residual:

$$
r_{\text{ls}} = b - A x_{\text{ls}} \quad\Longrightarrow\quad b = A x_{\text{ls}} + r_{\text{ls}}. \tag{8}
$$

Then for any  $\nu$  with  $A^T\nu=0$ ,

$$
b^T\nu = (Ax_{\text{ls}})^T\nu + r_{\text{ls}}^T\nu = x_{\text{ls}}^T(A^T\nu) + r_{\text{ls}}^T\nu = 0 + r_{\text{ls}}^T\nu = r_{\text{ls}}^T\nu. \tag{9}
$$

So we only need  $r_{\text{ls}}^T\nu$ .

For  $\tilde\nu = r_{\text{ls}}/\|r_{\text{ls}}\|_1$ :

$$
b^T\tilde\nu = r_{\text{ls}}^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{r_{\text{ls}}^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} = \boxed{\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.} \tag{10}
$$

For  $\hat\nu = -r_{\text{ls}}/\|r_{\text{ls}}\|_1$ :

$$
b^T\hat\nu = -\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. \tag{11}
$$

So one bound is positive, the other is negative.

* * *

### (b.4) Which bound is better?

The Chebyshev optimal value is a norm, so it is always nonnegative:

$$
\|Ax_{\text{ch}}-b\|_\infty \ge 0.
$$

A **lower bound** that is negative is valid but usually useless (it says “something nonnegative is at least some negative number”—true but not informative).

So:

*    $b^T\hat\nu = -\|r_{\text{ls}}\|_2^2/\|r_{\text{ls}}\|_1 < 0$ : weak.
*    $b^T\tilde\nu = \|r_{\text{ls}}\|_2^2/\|r_{\text{ls}}\|_1 > 0$ : informative.

Therefore ** $\tilde\nu$  gives the better bound**.

By (LB):

$$
\boxed{ \|Ax_{\text{ch}}-b\|_\infty \ \ge\ \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. } \tag{12}
$$

* * *

### (b.5) Compare these dual bounds with the bound from part (a)

Part (a) gave:

$$
\|r_{\text{ls}}\|_\infty \le \sqrt m\,\|r_{\text{ch}}\|_\infty.
$$

Rearrange it into a **lower bound on the optimum**  $\|r_{\text{ch}}\|_\infty$ :

$$
\boxed{ \|r_{\text{ch}}\|_\infty \ge \frac{\|r_{\text{ls}}\|_\infty}{\sqrt m}. } \tag{13}
$$

So we now have two different lower bounds on  $\|r_{\text{ch}}\|_\infty$ :

*   From (a):   $\ \|r_{\text{ch}}\|_\infty \ge \|r_{\text{ls}}\|_\infty/\sqrt m$ .
*   From (b):   $\ \|r_{\text{ch}}\|_\infty \ge \|r_{\text{ls}}\|_2^2/\|r_{\text{ls}}\|_1$ .

Which is larger (better)?

We can compare them using basic norm inequalities:

$$
\|r\|_1 \le \sqrt m\,\|r\|_2 \quad\Rightarrow\quad \frac{\|r\|_2^2}{\|r\|_1} \ge \frac{\|r\|_2^2}{\sqrt m\,\|r\|_2} = \frac{\|r\|_2}{\sqrt m}.
$$

Also  $\|r\|_2 \ge \|r\|_\infty$ . So

$$
\frac{\|r\|_2}{\sqrt m} \ge \frac{\|r\|_\infty}{\sqrt m}.
$$

Combine:

$$
\boxed{ \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \ \ge\ \frac{\|r_{\text{ls}}\|_\infty}{\sqrt m}. } \tag{14}
$$

So the dual lower bound from  $\tilde\nu$  is **always at least as good** as the lower bound you can extract from part (a). Often it is strictly better.

* * *

Final answers (clean)
---------------------

**(a)** Using LS optimality in  $\ell_2$  and norm inequalities:

$$
\boxed{ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty. }
$$

**(b)** The proposed vectors are feasible because  $\|\pm r_{\text{ls}}/\|r_{\text{ls}}\|_1\|_1=1$  and  $A^Tr_{\text{ls}}=0$ . Their dual objective values are:

$$
b^T\tilde\nu=\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1},\qquad b^T\hat\nu=-\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$

So  $\tilde\nu$  is better (positive lower bound), and it dominates the part-(a) implied lower bound:

$$
\boxed{ \|Ax_{\text{ch}}-b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \ \ge\ \frac{\|r_{\text{ls}}\|_\infty}{\sqrt m}. }
$$

* * *

Next in your list is **5.7** (piecewise-linear minimization).

## Response:
Thought for 51s

### Problem 5.7 — Piecewise-linear minimization

We study

$$
\min_{x\in\mathbb R^n}\ \max_{i=1,\dots,m}\ (a_i^T x + b_i), \tag{5.105}
$$

where each  $a_i\in\mathbb R^n$ ,  $b_i\in\mathbb R$ . This is “minimize the worst-case of  $m$  affine functions.”

I’ll solve parts (a)–(d) in order, from first principles, and I’ll be painfully explicit about each transformation.

* * *

0) Two equivalent primal formulations you should keep in your head
------------------------------------------------------------------

### 0.1 Original “max-of-affines” form

Define

$$
s_i(x):=a_i^T x+b_i.
$$

Then the objective is  $\max_i s_i(x)$ .

### 0.2 Epigraph (LP) form: introduce a scalar  $t$ 

A standard trick: replace “minimize a max” by an auxiliary variable  $t$  that upper-bounds all pieces:

$$
\max_i s_i(x)\le t \quad \Longleftrightarrow \quad s_i(x)\le t\ \forall i.
$$

So (5.105) is equivalent to:

$$
\begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & a_i^T x + b_i \le t,\quad i=1,\dots,m. \end{aligned} \tag{P-epi}
$$

This is a linear program (LP) because objective and constraints are linear in  $(x,t)$ .

### 0.3 The exercise’s “ $y$ ” form

The prompt in (a) says: consider the equivalent problem

$$
\begin{aligned} \min_{x\in\mathbb R^n,\ y\in\mathbb R^m}\quad & \max_{i=1,\dots,m} y_i\\ \text{s.t.}\quad & a_i^T x + b_i = y_i,\quad i=1,\dots,m. \end{aligned} \tag{P-y}
$$

This is equivalent because the constraints force  $y_i=s_i(x)$ , so  $\max_i y_i=\max_i s_i(x)$ .

We’ll derive the dual from (P-y) in (a), and from (P-epi) in (b), and show they match.

* * *

(a) Derive a dual problem from the Lagrange dual of (P-y)
---------------------------------------------------------

### Step 1: Write constraints in vector/matrix form (to avoid index clutter)

Let  $A\in\mathbb R^{m\times n}$  be the matrix whose  $i$ \-th row is  $a_i^T$ . Let  $b\in\mathbb R^m$  be the vector with entries  $b_i$ . Then the constraints

$$
a_i^T x + b_i = y_i,\ \forall i
$$

become

$$
Ax+b=y. \tag{C}
$$

So (P-y) is:

$$
\min_{x,y}\ \max_i y_i \quad \text{s.t. } Ax+b=y.
$$

### Step 2: Form the Lagrangian

We have equality constraints  $Ax+b-y=0$ . Introduce Lagrange multipliers  $\nu\in\mathbb R^m$  (one multiplier per equality).

Define the Lagrangian:

$$
L(x,y,\nu)=\max_i y_i + \nu^T(Ax+b-y).
$$

Expand:

$$
L(x,y,\nu)=\max_i y_i + \nu^T Ax + \nu^T b - \nu^T y.
$$

So it separates as:

$$
L(x,y,\nu)=\Big(\nu^T Ax\Big) + \nu^T b + \Big(\max_i y_i - \nu^T y\Big).
$$

### Step 3: Define the dual function  $g(\nu)$ 

By definition:

$$
g(\nu)=\inf_{x,y} L(x,y,\nu).
$$

Because  $x$  and  $y$  appear in separate groups, we can take the inf over them separately:

$$
g(\nu)= \nu^T b \;+\;\inf_x (\nu^T A x)\;+\;\inf_y (\max_i y_i - \nu^T y). \tag{1}
$$

Now compute the two infima carefully.

* * *

### Step 4: Compute  $\inf_x (\nu^T A x)$ 

Note:

$$
\nu^T A x = (A^T \nu)^T x.
$$
*   If  $A^T\nu \neq 0$ , then  $(A^T\nu)^T x$  is a nonzero linear function of  $x$ , hence unbounded below:  $\inf_x (A^T\nu)^T x = -\infty$ .
*   If  $A^T\nu = 0$ , then  $(A^T\nu)^T x = 0$  for all  $x$ , so the inf is  $0$ .

Therefore:

$$
\inf_x \nu^T A x = \begin{cases} 0, & A^T\nu=0,\\ -\infty, & \text{otherwise}. \end{cases} \tag{2}
$$

* * *

### Step 5: Compute  $\inf_y(\max_i y_i - \nu^T y)$ 

This is the key “max conjugate” step. Let

$$
\phi(y)=\max_{i} y_i.
$$

We want  $\inf_y (\phi(y)-\nu^T y)$ .

A standard identity from conjugates is:

$$
\inf_y (\phi(y)-\nu^T y) = -\sup_y (\nu^T y - \phi(y)) = -\phi^\*(\nu),
$$

where  $\phi^\*$  is the Fenchel conjugate.

So we need  $\phi^\*$  for  $\phi(y)=\max_i y_i$ .

#### Claim:  $\phi^\*(\nu)=0$  if  $\nu\in\Delta$ , and  $+\infty$  otherwise, where

$$
\Delta:=\{\nu\in\mathbb R^m:\ \nu\ge 0,\ \mathbf 1^T \nu =1\}
$$

(the probability simplex).

I’ll prove this directly (no “trust me, it’s known”).

**Definition of conjugate:**

$$
\phi^\*(\nu)=\sup_{y\in\mathbb R^m}\left(\nu^T y - \max_i y_i\right).
$$

**(i) If  $\nu\in\Delta$ : show the supremum is  $0$ .**

For any  $y$ , since  $\nu\ge 0$  and sums to 1,

$$
\nu^T y = \sum_i \nu_i y_i \le \sum_i \nu_i \max_j y_j = (\mathbf 1^T \nu)\max_j y_j = \max_j y_j.
$$

So

$$
\nu^T y - \max_i y_i \le 0 \quad \forall y.
$$

Thus the supremum is  $\le 0$ . But we can achieve 0 by taking  $y$  constant:  $y=t\mathbf 1$ . Then  $\nu^T y=t$  and  $\max_i y_i=t$ , so the expression is 0. Hence

$$
\phi^\*(\nu)=0 \quad \text{for }\nu\in\Delta.
$$

**(ii) If  $\nu\notin\Delta$ : show the supremum is  $+\infty$ .**

Two ways to fail being in  $\Delta$ :

*   If some  $\nu_k<0$ : choose  $y$  with  $y_k\to -\infty$  while keeping other components fixed and large enough so  $\max_i y_i$  stays bounded. Then  $\nu^T y$  grows to  $+\infty$  (negative times  $-\infty$ ), while  $\max_i y_i$  doesn’t offset it → supremum  $+\infty$ .
*   If  $\mathbf 1^T\nu \neq 1$ : choose  $y=t\mathbf 1$ . Then
    $$
    \nu^T y - \max_i y_i = t(\mathbf 1^T\nu - 1),
    $$
    which goes to  $+\infty$  as  $t\to+\infty$  if  $\mathbf 1^T\nu>1$ , or as  $t\to-\infty$  if  $\mathbf 1^T\nu<1$ . So again supremum  $+\infty$ .

So indeed:

$$
\phi^\*(\nu)= \begin{cases} 0, & \nu\ge 0,\ \mathbf 1^T\nu=1,\\ +\infty, & \text{otherwise}. \end{cases}
$$

Therefore

$$
\inf_y(\max_i y_i - \nu^T y)= -\phi^\*(\nu)= \begin{cases} 0, & \nu\in\Delta,\\ -\infty, & \text{otherwise}. \end{cases} \tag{3}
$$

* * *

### Step 6: Combine (1),(2),(3) to get  $g(\nu)$ 

From (1):

*   If both conditions hold:
    $$
    A^T\nu=0,\quad \nu\in\Delta,
    $$
    then the two inf terms are 0, so
    $$
    g(\nu)=\nu^T b.
    $$
*   Otherwise  $g(\nu)=-\infty$ .

So the **dual problem** is:

$$
\boxed{ \begin{aligned} \maximize_{\nu\in\mathbb R^m}\quad & b^T\nu\\ \text{subject to}\quad & A^T\nu = 0,\\ & \mathbf 1^T\nu = 1,\\ & \nu \ge 0. \end{aligned}} \tag{D-pwl}
$$

That’s the dual derived from the Lagrangian of (P-y).

Interpretation (important intuition):  $\nu$  is a probability distribution over the pieces; the constraint  $A^T\nu=0$  says the weighted average slope is zero; then  $b^T\nu$  is the weighted average intercept, which becomes a guaranteed lower bound on the best achievable max.

* * *

(b) Formulate (5.105) as an LP and take the LP dual; relate to (a)
------------------------------------------------------------------

### Step 1: LP formulation (epigraph)

We already wrote:

$$
\begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & a_i^T x + b_i \le t,\ i=1,\dots,m. \end{aligned}
$$

In matrix form:

$$
Ax + b \le t\mathbf 1. \tag{4}
$$

### Step 2: Build the Lagrangian (inequalities now!)

Introduce dual variables  $\nu\ge 0$  for the inequalities  $Ax+b-t\mathbf 1\le 0$ .

Lagrangian:

$$
L(x,t,\nu)= t + \nu^T(Ax+b-t\mathbf 1) = t + \nu^T Ax + \nu^T b - t(\mathbf 1^T\nu).
$$

Group terms:

$$
L(x,t,\nu)= \nu^T Ax + \nu^T b + t(1-\mathbf 1^T\nu).
$$

Dual function:

$$
g(\nu)=\inf_{x,t} L(x,t,\nu),\quad \nu\ge 0.
$$
*   Inf over  $x$ :  $\inf_x \nu^T Ax$  is 0 if  $A^T\nu=0$ , else  $-\infty$ .
*   Inf over  $t$ :  $\inf_t t(1-\mathbf 1^T\nu)$  is finite only if the coefficient is 0, i.e.  $1-\mathbf 1^T\nu=0$ . Otherwise you can send  $t\to\pm\infty$  to get  $-\infty$ .

So we require:

$$
A^T\nu=0,\quad \mathbf 1^T\nu=1,\quad \nu\ge 0,
$$

and then  $g(\nu)=\nu^T b$ .

Thus the LP dual is exactly the same as (D-pwl) in part (a). That’s the requested relation.

* * *

(c) Smooth approximation via log-sum-exp; show  $0\le p^\*_{gp}-p^\*_{pwl}\le \log m$ 
--------------------------------------------------------------------------------------

The smooth objective is:

$$
f_0(x)=\log\left(\sum_{i=1}^m \exp(a_i^T x + b_i)\right), \tag{5.106}
$$

and the “GP-like” unconstrained problem is

$$
p^\*_{gp}:=\min_x f_0(x).
$$

The original optimum is

$$
p^\*_{pwl}:=\min_x \max_i (a_i^T x+b_i).
$$

### Step 1: Prove the pointwise inequality for any vector  $s\in\mathbb R^m$ 

Let  $s_i=a_i^T x+b_i$ . Define  $M:=\max_i s_i$ .

Then:

*   Lower bound:
    $$
    \sum_i e^{s_i} \ge e^{M}\quad\Rightarrow\quad \log\sum_i e^{s_i}\ge \log(e^M)=M.
    $$
*   Upper bound:
    $$
    \sum_i e^{s_i} \le \sum_i e^{M}= m e^M\quad\Rightarrow\quad \log\sum_i e^{s_i}\le \log(m e^M)=M+\log m.
    $$

So for every  $x$ ,

$$
\boxed{ \max_i (a_i^T x+b_i)\ \le\ f_0(x)\ \le\ \max_i (a_i^T x+b_i)+\log m. } \tag{5}
$$

### Step 2: Convert pointwise bounds into optimal-value bounds

Take minimum over  $x$  in (5).

*   From the left inequality  $f_0(x)\ge \max_i s_i(x)$ :
    $$
    \min_x f_0(x)\ \ge\ \min_x \max_i s_i(x) \quad\Rightarrow\quad p^\*_{gp}\ge p^\*_{pwl}.
    $$
*   From the right inequality  $f_0(x)\le \max_i s_i(x)+\log m$ :
    $$
    \min_x f_0(x)\ \le\ \min_x \big(\max_i s_i(x)+\log m\big) =\min_x \max_i s_i(x)+\log m =p^\*_{pwl}+\log m.
    $$

Combine:

$$
\boxed{ 0\ \le\ p^\*_{gp}-p^\*_{pwl}\ \le\ \log m. }
$$

That’s exactly what they ask.

(Extra intuition: log-sum-exp is a smooth “soft max.” The worst-case error of soft-max vs max is at most  $\log m$ , and that carries through to optimal values.)

* * *

(d) Same bounds for parameter  $\gamma>0$ ; what happens as  $\gamma$  increases?
---------------------------------------------------------------------------------

Now consider the “temperature-scaled” softmax objective:

$$
f_\gamma(x)=\frac{1}{\gamma}\log\left(\sum_{i=1}^m \exp(\gamma(a_i^T x+b_i))\right), \quad \gamma>0.
$$

Let

$$
p^\*_\gamma := \min_x f_\gamma(x).
$$

### Step 1: Repeat the same max vs log-sum-exp inequality with scaling

Let again  $s_i=a_i^T x+b_i$  and  $M=\max_i s_i$ . Then:

*   Lower bound:
    $$
    \sum_i e^{\gamma s_i}\ge e^{\gamma M} \Rightarrow f_\gamma(x)=\frac{1}{\gamma}\log\sum_i e^{\gamma s_i}\ge \frac{1}{\gamma}\log(e^{\gamma M})=M.
    $$
*   Upper bound:
    $$
    \sum_i e^{\gamma s_i}\le m e^{\gamma M} \Rightarrow f_\gamma(x)\le \frac{1}{\gamma}\log(m e^{\gamma M})=M+\frac{\log m}{\gamma}.
    $$

So pointwise:

$$
\boxed{ \max_i s_i(x)\ \le\ f_\gamma(x)\ \le\ \max_i s_i(x)+\frac{\log m}{\gamma}. } \tag{6}
$$

### Step 2: Convert to optimal-value bounds

Minimize over  $x$ :

$$
p^\*_{pwl}\ \le\ p^\*_\gamma\ \le\ p^\*_{pwl}+\frac{\log m}{\gamma}.
$$

So:

$$
\boxed{ 0\ \le\ p^\*_\gamma - p^\*_{pwl}\ \le\ \frac{\log m}{\gamma}. }
$$

### Step 3: What happens as  $\gamma$  increases?

As  $\gamma\to\infty$ :

*   The upper bound  $\frac{\log m}{\gamma}\to 0$ .
*   So  $p^\*_\gamma \downarrow p^\*_{pwl}$  (it converges to the true piecewise-linear optimum value).
*   Functionally,  $f_\gamma(x)$  becomes a tighter and tighter approximation of  $\max_i s_i(x)$ .

Practical “optimization feel” (useful intuition):

*   For small  $\gamma$ , the objective is very smooth and “averages” the pieces a lot.
*   For large  $\gamma$ , it behaves almost like the nonsmooth max; gradients become highly concentrated on the currently-largest piece (softmax weights become nearly one-hot), and numerics can become more delicate (overflow in  $\exp(\gamma s)$ , ill-conditioning).

* * *

If you want, next I can also derive the dual of (5.106) (the one they reference as (5.62)) explicitly and show how entropy appears; but for this exercise, the bounds in (c)(d) are already fully proven without needing that dual.

## Response:
Thought for 1m 11s

### Problem 5.9 — Suboptimality of a simple covering ellipsoid (Boyd–Vandenberghe)

We’re in the “minimum-volume ellipsoid centered at the origin that contains points  $a_1,\dots,a_m\in\mathbb R^n$ ” setting.

The primal problem (their (5.14) on p.222) is:

$$
\begin{aligned} \min_{X\in \mathbb S_{++}^n}\quad & f_0(X):=\log\det(X^{-1})\\ \text{s.t.}\quad & a_i^T X a_i \le 1,\quad i=1,\dots,m, \end{aligned} \tag{P}
$$

and we assume  $\{a_i\}$  span  $\mathbb R^n$ .

Define the “simple” candidate

$$
X_{\text{sim}} := \left(\sum_{k=1}^m a_k a_k^T\right)^{-1}. \tag{Xsim}
$$

Let me denote

$$
S := \sum_{k=1}^m a_k a_k^T\in\mathbb S^n.
$$

So  $X_{\text{sim}}=S^{-1}$  and  $X_{\text{sim}}^{-1}=S$ .

* * *

0) Why the objective is “volume” (so we know what we’re bounding)
-----------------------------------------------------------------

The ellipsoid defined by  $X\succ 0$  is

$$
\mathcal E(X):=\{u\in\mathbb R^n : u^T X u \le 1\}.
$$

Let  $Q:=X^{-1}\succ 0$ . Then

$$
u^T X u \le 1 \iff u^T Q^{-1} u \le 1.
$$

Write  $u=Q^{1/2} z$ . Then  $u^TQ^{-1}u=z^Tz$ . So

$$
\mathcal E(X)=\{Q^{1/2} z : \|z\|_2\le 1\}=Q^{1/2}\, \mathbb B_2^n.
$$

Volume scales by determinant under linear maps:

$$
\mathrm{vol}(\mathcal E(X)) = \det(Q^{1/2})\,\mathrm{vol}(\mathbb B_2^n) = \sqrt{\det(Q)}\,\mathrm{vol}(\mathbb B_2^n) = \sqrt{\det(X^{-1})}\,\mathrm{vol}(\mathbb B_2^n).
$$

Taking logs:

$$
\log\mathrm{vol}(\mathcal E(X)) = \underbrace{\log\mathrm{vol}(\mathbb B_2^n)}_{\text{constant}} + \tfrac12\log\det(X^{-1}).
$$

So minimizing  $\log\det(X^{-1})$  is exactly minimizing volume (up to a constant and a monotone transformation). Good.

* * *

(a) Show  $X_{\text{sim}}$  is feasible:  $a_i^T X_{\text{sim}} a_i\le 1$ 
==========================================================================

### Step 1: First, why is  $S$  invertible (so  $X_{\text{sim}}$  makes sense)?

For any  $v\in\mathbb R^n$ ,

$$
v^T S v = v^T\left(\sum_{k=1}^m a_k a_k^T\right) v = \sum_{k=1}^m v^T a_k a_k^T v = \sum_{k=1}^m (a_k^T v)^2 \ge 0.
$$

So  $S\succeq 0$ .

Moreover, because  $\{a_k\}$  span  $\mathbb R^n$ : if  $v\neq 0$ , then not all  $a_k^T v$  can be zero. Hence at least one term  $(a_k^T v)^2>0$ , so the sum is  $>0$ . Therefore

$$
v\neq 0 \ \Rightarrow\ v^T S v>0 \quad \Longrightarrow\quad S\succ 0.
$$

So  $S\in\mathbb S_{++}^n$  and  $S^{-1}$  exists.

### Step 2: Build the PSD block matrix in the hint

Fix an index  $i$ . Consider the  $(n+1)\times(n+1)$  block matrix:

$$
M_i := \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix}.
$$

We show  $M_i\succeq 0$ .

Write  $S$  as  $S = \sum_{k\neq i} a_k a_k^T + a_i a_i^T$ . Then:

$$
M_i = \begin{bmatrix} \sum_{k\neq i} a_k a_k^T & 0\\ 0 & 0 \end{bmatrix} + \begin{bmatrix} a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix}.
$$
*   The first matrix is block-diagonal with PSD block  $\sum_{k\neq i} a_k a_k^T\succeq 0$  and scalar  $0$ , hence PSD.
*   The second matrix is an outer product:
    $$
    \begin{bmatrix} a_i\\ 1 \end{bmatrix} \begin{bmatrix} a_i^T & 1 \end{bmatrix} = \begin{bmatrix} a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix},
    $$
    which is PSD (outer products are PSD).

Sum of PSD matrices is PSD, so  $M_i\succeq 0$ .

### Step 3: Use the Schur complement to extract the inequality we need

Because  $S\succ 0$ , the Schur complement rule says:

$$
\begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix}\succeq 0 \quad \Longleftrightarrow\quad 1 - a_i^T S^{-1} a_i \ge 0.
$$

So:

$$
a_i^T S^{-1} a_i \le 1.
$$

But  $S^{-1}=X_{\text{sim}}$ . Therefore

$$
\boxed{a_i^T X_{\text{sim}} a_i \le 1\quad \forall i.}
$$

So  $X_{\text{sim}}$  is feasible for (P). ✅

* * *

(b) Bound how suboptimal  $X_{\text{sim}}$  can be using a restricted dual
==========================================================================

You’re given the dual (derived in the book) as:

$$
\begin{aligned} \maximize_{\lambda\in\mathbb R^m}\quad & \log\det\!\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big)\;-\;\mathbf 1^T\lambda \;+\; n\\ \text{s.t.}\quad & \lambda\ge 0,\\ & \sum_{i=1}^m \lambda_i a_i a_i^T \succ 0. \end{aligned} \tag{D}
$$

I’ll do three things:

1.  (Quickly but clearly) re-derive why the dual objective has that form (so it doesn’t feel like magic).
2.  Restrict to  $\lambda=t\mathbf 1$ , find optimal  $t$ , compute the dual value.
3.  Convert the objective gap into a **volume ratio** bound  $(m/n)^{n/2}$ .

* * *

(b.0) One-screen re-derivation of the dual objective (to remove black-box feelings)
-----------------------------------------------------------------------------------

Primal:

$$
\min_{X\succ 0}\ \log\det(X^{-1})\quad \text{s.t. } a_i^T X a_i\le 1.
$$

Form Lagrangian with multipliers  $\lambda_i\ge 0$ :

$$
L(X,\lambda) = \log\det(X^{-1}) +\sum_{i=1}^m \lambda_i(a_i^T X a_i -1).
$$

Rewrite pieces:

*    $\log\det(X^{-1})=-\log\det X$ .
*    $\sum_i \lambda_i a_i^T X a_i = \sum_i \lambda_i \mathrm{tr}(a_i^T X a_i)=\mathrm{tr}\!\left(\sum_i \lambda_i a_i a_i^T\right)\!X$ .

Define  $S(\lambda):=\sum_i \lambda_i a_i a_i^T$ . Then

$$
L(X,\lambda)= -\log\det X + \mathrm{tr}(S(\lambda)X) - \mathbf 1^T\lambda.
$$

Dual function is  $g(\lambda)=\inf_{X\succ 0} L(X,\lambda)$ .

Key minimization identity (you can verify by first-order condition):

$$
\inf_{X\succ 0}\left[-\log\det X + \mathrm{tr}(S X)\right] = \begin{cases} \log\det S + n, & S\succ 0,\\ -\infty, & \text{otherwise}. \end{cases}
$$

(Reason: derivative gives  $-X^{-1}+S=0\Rightarrow X=S^{-1}$ ; plug in gives  $-\log\det(S^{-1})+\mathrm{tr}(SS^{-1})=\log\det S+n$ .)

Therefore

$$
g(\lambda)=\log\det(S(\lambda)) - \mathbf 1^T\lambda + n \quad \text{when } \lambda\ge 0,\ S(\lambda)\succ 0.
$$

Maximize  $g(\lambda)$  gives the dual (D). Great.

Also: weak duality gives  $d^\star\le p^\star$ , so any feasible  $\lambda$  yields a **lower bound** on the primal optimum value.

* * *

(b.1) Restrict to  $\lambda=t\mathbf 1$  and optimize  $t$ 
-----------------------------------------------------------

We restrict to:

$$
\lambda_i=t,\quad i=1,\dots,m,\qquad t\ge 0.
$$

Then

$$
S(\lambda)=\sum_{i=1}^m t\,a_i a_i^T = t\sum_{i=1}^m a_i a_i^T = tS.
$$

Feasibility:

*    $t>0\Rightarrow tS\succ 0$  since  $S\succ 0$ .
*    $t=0\Rightarrow tS=0$  not  $\succ 0$ , so not feasible for the dual objective (it would give  $-\infty$ ).

So we maximize over  $t>0$ .

### Compute the restricted dual objective

Dual objective:

$$
\Phi(t)=\log\det(tS) - \mathbf 1^T(t\mathbf 1) + n = \log\det(tS) - mt + n.
$$

Compute  $\log\det(tS)$ :

Since  $\det(tS)=t^n\det(S)$  (scaling a matrix by  $t$  scales determinant by  $t^n$ ),

$$
\log\det(tS)=\log(t^n\det S)=n\log t + \log\det S.
$$

So

$$
\Phi(t)= n\log t + \log\det S - mt + n.
$$

### Optimize over  $t>0$ 

Differentiate:

$$
\Phi'(t)=\frac{n}{t}-m.
$$

Set  $\Phi'(t)=0$ :

$$
\frac{n}{t}-m=0 \quad\Rightarrow\quad t^\star = \frac{n}{m}.
$$

Second derivative  $\Phi''(t)=-\frac{n}{t^2}<0$ , so this is a maximum.

### Value at  $t^\star$ 

$$
\Phi(t^\star) = n\log\left(\frac{n}{m}\right)+\log\det S - m\cdot \frac{n}{m} + n = \log\det S + n\log\left(\frac{n}{m}\right).
$$

So the restricted dual gives the valid lower bound:

$$
\boxed{ p^\star \ \ge\ d^\star\ \ge\ \log\det S + n\log\left(\frac{n}{m}\right) = \log\det S - n\log\left(\frac{m}{n}\right). } \tag{LB}
$$

* * *

(b.2) Compare with the primal value at  $X_{\text{sim}}$ 
---------------------------------------------------------

For  $X_{\text{sim}}=S^{-1}$ ,

$$
f_0(X_{\text{sim}})=\log\det(X_{\text{sim}}^{-1})=\log\det(S).
$$

So:

*   “simple” objective value:  $p_{\text{sim}}:=\log\det S$ .
*   optimal objective value:  $p^\star$ .
*   lower bound from dual restriction:  $p^\star \ge \log\det S - n\log(m/n)$ .

Rearrange to bound the objective gap:

$$
p_{\text{sim}} - p^\star \le \log\det S - \left(\log\det S - n\log(m/n)\right) = n\log(m/n).
$$

So:

$$
\boxed{ 0 \le p_{\text{sim}}-p^\star \le n\log\left(\frac{m}{n}\right). } \tag{gap}
$$

* * *

(b.3) Convert objective gap into **volume ratio** bound  $(m/n)^{n/2}$ 
-----------------------------------------------------------------------

Recall:

$$
\mathrm{vol}(\mathcal E(X)) = \mathrm{vol}(\mathbb B_2^n)\cdot \sqrt{\det(X^{-1})}.
$$

Let  $X^\star$  be primal optimal. Then

$$
\frac{\mathrm{vol}(\mathcal E(X_{\text{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \frac{\sqrt{\det(X_{\text{sim}}^{-1})}}{\sqrt{\det(X^{\star -1})}} = \exp\left(\tfrac12\left[\log\det(X_{\text{sim}}^{-1})-\log\det(X^{\star -1})\right]\right).
$$

But  $\log\det(X_{\text{sim}}^{-1})=p_{\text{sim}}$  and  $\log\det(X^{\star -1})=p^\star$ . So

$$
\frac{\mathrm{vol}(\mathcal E(X_{\text{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \exp\left(\tfrac12(p_{\text{sim}}-p^\star)\right).
$$

Use the gap bound (gap):

$$
p_{\text{sim}}-p^\star \le n\log(m/n) \quad\Rightarrow\quad \exp\left(\tfrac12(p_{\text{sim}}-p^\star)\right) \le \exp\left(\tfrac12 n\log(m/n)\right) = \left(\frac{m}{n}\right)^{n/2}.
$$

Therefore:

$$
\boxed{ \mathrm{vol}\Big(\{u: u^T X_{\text{sim}}^{-1} u \le 1\}\Big) \le \left(\frac{m}{n}\right)^{n/2}\, \mathrm{vol}\Big(\{u: u^T X^{\star -1} u \le 1\}\Big). }
$$

That is exactly the requested factor bound.

* * *

What this result _means_ (quick intuition, but precise)
-------------------------------------------------------

*    $X_{\text{sim}}=(\sum a_i a_i^T)^{-1}$  is a very cheap “moment-type” ellipsoid.
*   It always contains all points (part a).
*   Worst-case, its volume is within a factor  $(m/n)^{n/2}$  of optimal.  
    This factor grows with  $m$  (more points = potentially tighter optimal ellipsoid) and shrinks with  $n$  relative to  $m$ .

* * *

Next in your list after 5.9 is **5.19** or **6.9** (depending on the exact numbering you meant).

## Response:
Thought for 2m 26s

### Problem 5.19 — The sum of the largest  $r$  elements of a vector

You’re given a vector  $x\in\mathbb R^n$ . Let  $x_{[1]}\ge x_{[2]}\ge \cdots \ge x_{[n]}$  be the entries of  $x$  sorted in **nonincreasing** order. Define

$$
f(x)=\sum_{i=1}^r x_{[i]}, \qquad r\in\{1,2,\dots,n\}.
$$

So  $f(x)$  is “sum of the top  $r$  components.”

The constraint of interest is  $f(x)\le \alpha$ . Naively, it’s equivalent to “for every subset  $S\subset\{1,\dots,n\}$  of size  $r$ ,  $\sum_{i\in S}x_i\le \alpha$ ” (combinatorially many inequalities). The goal is to derive a **compact LP representation**.

We solve parts (a)(b)(c).

* * *

(a) Show  $f(x)$  equals the optimal value of an LP
---------------------------------------------------

Claim:

$$
f(x) = \max_{y\in\mathbb R^n}\ \ x^T y \quad\text{s.t.}\quad 0\le y\le 1,\ \ \mathbf 1^T y=r. \tag{P}
$$

Here  $\mathbf 1$  is the all-ones vector.

### Step 1: Understand what the feasible set for  $y$  means

The constraints are:

1.   $0\le y_i\le 1$  for each  $i$ .
2.   $\sum_{i=1}^n y_i = r$ .

So  $y$  is like a “soft selector” that picks **total weight  $r$ ** across coordinates, with at most weight 1 per coordinate.

If  $y$  were forced to be binary ( $y_i\in\{0,1\}$ ), these constraints would mean “pick exactly  $r$  indices.” Here  $y$  is allowed to be fractional, but we’ll show the optimum still occurs at a binary point.

### Step 2: Key LP fact: optimum occurs at an extreme point

This is a standard theorem of linear programming:

*   The feasible set is a polytope (intersection of finitely many linear inequalities/equalities).
*   The objective  $x^Ty$  is linear.
*   Therefore, if the maximum is finite and the feasible set is nonempty, there exists an optimal solution at an **extreme point** (vertex) of the polytope.

So it’s enough to characterize the extreme points of

$$
\mathcal Y:=\{y\in\mathbb R^n:\ 0\le y\le 1,\ \mathbf 1^T y=r\}.
$$

### Step 3: Characterize the extreme points of  $\mathcal Y$ 

**Claim:** The extreme points of  $\mathcal Y$  are exactly the vectors  $y\in\{0,1\}^n$  with  $\mathbf 1^T y=r$  (i.e., indicator vectors of subsets of size  $r$ ).

**Proof (no handwaving).**

Take any feasible  $y\in\mathcal Y$ .

*   If there exist two distinct indices  $i\neq j$  such that  $0<y_i<1$  and  $0<y_j<1$ , then we can “wiggle”  $y$  in opposite directions on coordinates  $i$  and  $j$  while staying feasible:
    Choose a small  $\varepsilon>0$  such that
    $$
    y_i+\varepsilon\le 1,\quad y_i-\varepsilon\ge 0,\quad y_j+\varepsilon\le 1,\quad y_j-\varepsilon\ge 0.
    $$
    (This is possible because both are strictly between 0 and 1.)
    Define two new vectors:
    $$
    y^{+}=y+\varepsilon e_i-\varepsilon e_j,\qquad y^{-}=y-\varepsilon e_i+\varepsilon e_j.
    $$
    Then:
    *    $0\le y^\pm\le 1$  still holds (by construction).
    *    $\mathbf 1^T y^\pm=\mathbf 1^T y +\varepsilon-\varepsilon = r$ , so the equality constraint still holds.
    And clearly  $y^+\neq y^-$ , and
    $$
    y = \frac{1}{2}y^+ + \frac{1}{2}y^-.
    $$
    That expresses  $y$  as a nontrivial convex combination of two distinct feasible points, so ** $y$  is not extreme**.

So: **an extreme point cannot have two fractional components**.

What if an extreme point had exactly one fractional component? Suppose one coordinate is fractional,  $0<y_k<1$ , and all others are 0 or 1. Then  $\mathbf 1^T y$  would be “(an integer) + (a fractional number),” which is fractional—contradiction because  $\mathbf 1^T y=r$  is an integer. Therefore, **no fractional component is possible at an extreme point**.

So every extreme point has all components in  $\{0,1\}$ . And since the sum must be  $r$ , it has exactly  $r$  ones.

That proves the claim.

### Step 4: Reduce the LP to choosing a subset of size  $r$ 

At an extreme point,  $y=\mathbf 1_S$  for some subset  $S\subset\{1,\dots,n\}$  with  $|S|=r$ , where  $(\mathbf 1_S)_i=1$  if  $i\in S$ , else 0.

Then

$$
x^T y = x^T \mathbf 1_S = \sum_{i\in S} x_i.
$$

So the LP optimal value equals

$$
\max_{S:\ |S|=r}\ \sum_{i\in S} x_i. \tag{*}
$$

### Step 5: Show the best subset is “the indices of the  $r$  largest components”

Let the sorted values be  $x_{[1]}\ge\cdots\ge x_{[n]}$ . Consider any subset  $S$  of size  $r$ . If  $S$  ever contains an index  $j$  whose value is not among the top  $r$  values, then there exists some index  $k$  among the top  $r$  that is not in  $S$ . Since  $x_k\ge x_j$ , swapping  $j$  out and  $k$  in cannot decrease the sum; it weakly increases it. Repeating this swapping process yields a subset consisting exactly of the indices of the  $r$  largest entries, and the sum becomes  $\sum_{i=1}^r x_{[i]}$ .

Therefore,

$$
\max_{S:\ |S|=r}\sum_{i\in S}x_i = \sum_{i=1}^r x_{[i]} = f(x).
$$

Combine with (\*) and we have proven:

$$
\boxed{ f(x)=\max\ \{x^T y:\ 0\le y\le 1,\ \mathbf 1^T y=r\}. }
$$

That completes (a).

* * *

(b) Derive the dual, and rewrite  $f(x)\le \alpha$  compactly
-------------------------------------------------------------

The primal LP from (a) is:

$$
\begin{aligned} \maximize_y\quad & x^T y\\ \text{s.t.}\quad & y\le \mathbf 1\\ & \mathbf 1^T y = r\\ & y\ge 0. \end{aligned} \tag{P}
$$

This is in the standard “max” LP form:

*   inequalities  $Ay\le b$ ,
*   equalities  $Cy=d$ ,
*   and  $y\ge 0$ .

Here:

*    $A=I$ ,  $b=\mathbf 1$  (because  $y\le \mathbf 1$ ),
*    $C=\mathbf 1^T$ ,  $d=r$ ,
*   objective coefficient  $c=x$ .

### Step 1: Write the standard dual template (so nothing is mysterious)

For the primal:

$$
\maximize\ c^T y \quad \text{s.t. } Ay\le b,\ Cy=d,\ y\ge 0,
$$

the dual is:

$$
\minimize\ b^T u + d^T t \quad \text{s.t. } A^T u + C^T t \ge c,\ u\ge 0,\ t \text{ free}.
$$
*    $u$  corresponds to inequality constraints  $Ay\le b$  and satisfies  $u\ge 0$ .
*    $t$  corresponds to equality constraints  $Cy=d$  and is free (unconstrained in sign).

### Step 2: Apply to our specific  $A,b,C,d,c$ 

*    $A=I\Rightarrow A^T=I$ .
*    $b=\mathbf 1\Rightarrow b^T u = \mathbf 1^T u$ .
*    $C=\mathbf 1^T\Rightarrow C^T = \mathbf 1$ .
*    $d=r\Rightarrow d^T t = rt$  (since  $t$  is scalar).
*    $c=x$ .

So the dual constraints become:

$$
A^T u + C^T t \ge c \quad\Longleftrightarrow\quad u + t\mathbf 1 \ge x.
$$

And the dual objective is:

$$
\mathbf 1^T u + rt.
$$

Also  $u\ge 0$ , and  $t\in\mathbb R$  is free.

So the dual is:

$$
\boxed{ \begin{aligned} \minimize_{t\in\mathbb R,\ u\in\mathbb R^n}\quad & rt+\mathbf 1^T u\\ \text{s.t.}\quad & t\mathbf 1 + u \ge x,\\ & u\ge 0. \end{aligned}} \tag{D}
$$

This matches the statement in the book.

### Step 3: Why does this equal  $f(x)$ ?

Because (P) and (D) are a primal-dual pair of LPs. Under mild feasibility (here it’s easy to see feasibility holds: e.g.  $y=(r/n)\mathbf 1$  is feasible when  $r\le n$ ), **strong duality holds for LPs**:

$$
\text{optimal value of (P)} = \text{optimal value of (D)}.
$$

From (a), the optimal value of (P) is  $f(x)$ . Therefore the optimal value of (D) is also  $f(x)$ .

So we have the extremely useful identity:

$$
\boxed{ f(x)=\min\{rt+\mathbf 1^T u:\ t\mathbf 1+u\ge x,\ u\ge 0\}. }
$$

### Step 4: Convert the constraint  $f(x)\le \alpha$  into a compact set of linear inequalities

We want:

$$
f(x)\le \alpha.
$$

Using the dual representation:

$$
f(x)=\min_{(t,u)\ \text{feasible}} (rt+\mathbf 1^T u).
$$

A minimum is  $\le \alpha$  **iff** there exists a feasible point achieving value  $\le \alpha$ . So:

$$
f(x)\le \alpha \iff \exists\, t\in\mathbb R,\ u\in\mathbb R^n\ \text{s.t.} \begin{cases} t\mathbf 1+u\ge x,\\ u\ge 0,\\ rt+\mathbf 1^T u \le \alpha. \end{cases}
$$

That is the compact representation.

Notice what happened:

*   the original “combinatorial” description had  $\binom{n}{r}$  inequalities,
*   the compact one has only  $2n+1$  inequalities (componentwise  $t\mathbf 1+u\ge x$  gives  $n$ , plus  $u\ge 0$  gives  $n$ , plus  $rt+\mathbf 1^T u\le \alpha$  gives 1).

This is exactly why this exercise exists.

* * *

(c) Markowitz portfolio with diversification: formulate as a QP
---------------------------------------------------------------

You start from the classic Markowitz-type problem:

$$
\begin{aligned} \minimize_{x\in\mathbb R^n}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min}\\ & \mathbf 1^T x = 1\\ & x\ge 0, \end{aligned} \tag{M}
$$

where:

*    $x$  are portfolio weights (nonnegative, sum to 1),
*    $\bar p$  is the mean-return vector,
*    $\Sigma\succeq 0$  is the covariance matrix.

Now add the diversification constraint:

> no more than  $80\%$  of the budget can be invested in any  $10\%$  of the assets.

If  $n$  is divisible by 10, set  $r=0.1n$ . If not, you choose a rounding convention (typically  $r=\lceil 0.1n\rceil$  or  $r=\lfloor 0.1n\rfloor$ ); the book writes  $[0.1n]$  to mean “the integer closest / a chosen integer count of 10%”.

That constraint is:

$$
\sum_{i=1}^{r} x_{[i]} \le 0.8,
$$

i.e. “sum of largest  $r$  positions is at most  $0.8$ .”

But that is exactly  $f(x)\le 0.8$  with the same  $f$  as above.

Using part (b), we can express it with auxiliary variables  $t\in\mathbb R$ ,  $u\in\mathbb R^n$ :

$$
\exists t,u\ \text{s.t.}\quad t\mathbf 1 + u \ge x,\quad u\ge 0,\quad rt+\mathbf 1^T u \le 0.8.
$$

### Final QP formulation (everything explicit)

Decision variables:  $x\in\mathbb R^n$ ,  $u\in\mathbb R^n$ ,  $t\in\mathbb R$ .

$$
\boxed{ \begin{aligned} \minimize_{x,u,t}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min}\\ & \mathbf 1^T x = 1\\ & x\ge 0\\[2mm] & t\mathbf 1 + u \ge x\\ & u\ge 0\\ & rt+\mathbf 1^T u \le 0.8. \end{aligned}}
$$

This is a **QP** because:

*   objective is quadratic in  $x$ ,
*   all constraints are linear in  $(x,u,t)$ .

And it enforces exactly “top 10% holdings sum to at most 80%” without needing  $\binom{n}{r}$  constraints.

* * *

If you want the “feel” of the auxiliary variables:  $t$  acts like a common “cap level,” and  $u$  is the extra slack needed above that cap to cover each  $x_i$ . The inequality  $rt+\mathbf 1^T u\le 0.8$  limits the total mass of the top  $r$  entries by charging 1 per “above-cap” unit. It’s a classic convexification trick that turns sorting/top- $r$  into linear constraints.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)