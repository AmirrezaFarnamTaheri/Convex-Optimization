# Ellipsoid Volume Minimization

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:12:18  
**Updated:** 12/28/2025 23:35:24  
**Exported:** 12/29/2025 0:11:29  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060c1-0b3c-832f-9173-d85fdee798cb](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060c1-0b3c-832f-9173-d85fdee798cb)  

## Response:
Thought for 54s

We’re in the classic “minimum‐volume ellipsoid that contains some points” problem, with the extra simplification that the ellipsoid is **centered at the origin**.

Let the given points be  $a_1,\dots,a_m\in\mathbb R^n$ , and assume they **span**  $\mathbb R^n$  (so  $m\ge n$ , and they aren’t all stuck in a lower-dimensional subspace).

* * *

0) What ellipsoid are we optimizing over, and why this objective?
-----------------------------------------------------------------

A centered ellipsoid can be written in the quadratic form

$$
\mathcal E(X)=\{x\in\mathbb R^n:\ x^T X x \le 1\}, \qquad X\succ 0.
$$
*    $X\succ 0$  means  $X$  is symmetric positive definite, so  $x^T X x$  is a genuine “squared norm”–like thing.
*   The containment constraint “ $\mathcal E(X)$  contains  $a_i$ ” is exactly
    $$
    a_i^T X a_i \le 1,\quad i=1,\dots,m.
    $$

Volume:  $\mathcal E(X)$  is the image of the unit ball under  $X^{-1/2}$ . So

$$
\mathrm{vol}(\mathcal E(X)) = \mathrm{vol}(B_n)\,\det(X^{-1/2}) = \mathrm{vol}(B_n)\,\frac{1}{\sqrt{\det X}} \propto \sqrt{\det(X^{-1})}.
$$

Taking logs (and ignoring the constant  $\log \mathrm{vol}(B_n)$ ),

$$
\log \mathrm{vol}(\mathcal E(X)) = \text{const} + \frac12\log\det(X^{-1}).
$$

So minimizing  $\log\det(X^{-1})$  is exactly minimizing volume.

The primal problem is:

$$
\begin{aligned} \text{minimize } & f_0(X)=\log\det(X^{-1})\\ \text{subject to } & a_i^T X a_i \le 1,\quad i=1,\dots,m,\\ & X\succ 0. \end{aligned}
$$

* * *

(a) Show  $X_{\text{sim}}=\Big(\sum_{k=1}^m a_k a_k^T\Big)^{-1}$  is feasible
-----------------------------------------------------------------------------

### Step 1: Define the key matrix and show it’s invertible

Let

$$
S := \sum_{k=1}^m a_k a_k^T.
$$

Claim:  $S\succ 0$  (hence invertible), using the spanning assumption.

Take any  $x\neq 0$ . Then

$$
x^T S x = x^T\Big(\sum_{k=1}^m a_k a_k^T\Big)x = \sum_{k=1}^m x^T a_k a_k^T x = \sum_{k=1}^m (a_k^T x)^2.
$$

This is a sum of squares, so it’s  $\ge 0$ . It equals  $0$  iff  $a_k^T x = 0$  for all  $k$ , i.e.,  $x$  is orthogonal to  $\mathrm{span}\{a_k\}$ . But the  $a_k$  span  $\mathbb R^n$ , so the only vector orthogonal to all of them is  $x=0$ . Contradiction. Therefore  $x^T S x>0$  for all  $x\neq 0$ , so  $S\succ 0$ .

Thus  $X_{\text{sim}} = S^{-1}$  is well-defined and  $X_{\text{sim}}\succ 0$ .

### Step 2: What we must prove for feasibility

Feasibility means:

$$
a_i^T X_{\text{sim}} a_i = a_i^T S^{-1} a_i \le 1 \quad \text{for each } i.
$$

### Step 3: Build the hinted block matrix and prove it is PSD

For each fixed  $i$ , consider the  $(n+1)\times(n+1)$  symmetric block matrix

$$
M_i := \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix}.
$$

We want to show  $M_i\succeq 0$  (positive semidefinite).

A clean way: write  $M_i$  as a sum of obvious rank-one PSD matrices.

*   For  $k\neq i$ , define the  $(n+1)$ \-vector  $\tilde a_k:=\begin{bmatrix}a_k\\0\end{bmatrix}$ .  
    Then  $\tilde a_k\tilde a_k^T = \begin{bmatrix}a_k a_k^T & 0\\ 0 & 0\end{bmatrix}\succeq 0$ .
*   Define  $\tilde a_i':=\begin{bmatrix}a_i\\1\end{bmatrix}$ .  
    Then  $\tilde a_i'\tilde a_i'^T=\begin{bmatrix}a_i a_i^T & a_i\\ a_i^T & 1\end{bmatrix}\succeq 0$ .

Now sum them:

$$
\sum_{k\neq i} \tilde a_k\tilde a_k^T \;+\; \tilde a_i'\tilde a_i'^T = \begin{bmatrix} \sum_{k\neq i} a_k a_k^T + a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix} = \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Sum of PSD matrices is PSD, so  $M_i\succeq 0$ . Done.

### Step 4: Apply the Schur complement to extract  $a_i^T S^{-1} a_i \le 1$ 

Schur complement fact (the one being hinted): if  $S\succ 0$ , then

$$
\begin{bmatrix} S & u\\ u^T & \alpha \end{bmatrix}\succeq 0 \quad\Longleftrightarrow\quad \alpha - u^T S^{-1}u \ge 0.
$$

Here  $u=a_i$ ,  $\alpha=1$ . Since  $S\succ 0$  and  $M_i\succeq 0$ , we get

$$
1 - a_i^T S^{-1} a_i \ge 0 \quad\Longrightarrow\quad a_i^T S^{-1} a_i \le 1.
$$

But  $S^{-1}=X_{\text{sim}}$ . Therefore

$$
a_i^T X_{\text{sim}} a_i \le 1 \quad \forall i,
$$

so  $X_{\text{sim}}$  is feasible.

That completes (a).

* * *

(b) Use the dual to bound how suboptimal  $X_{\text{sim}}$  can be, and turn it into a volume ratio
---------------------------------------------------------------------------------------------------

You’re given the dual (we’ll use it as a black box, but we’ll be very explicit about how to use it):

$$
\begin{aligned} \text{maximize } & d(\lambda)=\log\det\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big) - \mathbf 1^T\lambda + n\\ \text{subject to } & \lambda\succeq 0,\\ & \sum_{i=1}^m \lambda_i a_i a_i^T \succ 0. \end{aligned}
$$

Key principle: **weak duality**. For any dual-feasible  $\lambda$ ,

$$
d(\lambda)\ \le\ p^\star,
$$

where  $p^\star$  is the optimal primal value (minimum of  $\log\det(X^{-1})$ ).

Also, for any primal-feasible  $X$ ,

$$
p^\star \ \le\ f_0(X).
$$

So for our specific  $X_{\text{sim}}$ ,

$$
d(\lambda)\ \le\ p^\star\ \le\ f_0(X_{\text{sim}}).
$$

### Step 1: Compute the primal objective at  $X_{\text{sim}}$ 

We have  $X_{\text{sim}} = S^{-1}$ , so  $X_{\text{sim}}^{-1}=S$ . Thus

$$
f_0(X_{\text{sim}})=\log\det(X_{\text{sim}}^{-1})=\log\det(S).
$$

### Step 2: Pick a simple dual-feasible family  $\lambda = t\mathbf 1$ 

Take

$$
\lambda_i = t\quad \text{for all } i,\qquad t>0.
$$

Then

$$
\sum_{i=1}^m \lambda_i a_i a_i^T = \sum_{i=1}^m t\, a_i a_i^T = t S.
$$

Since  $S\succ 0$  from part (a), and  $t>0$ , we have  $tS\succ 0$ . Also  $\lambda\succeq 0$ . So this is dual-feasible.

Now evaluate the dual objective:

$$
d(t\mathbf 1)=\log\det(tS) - \mathbf 1^T(t\mathbf 1) + n = \log\det(tS) - mt + n.
$$

Use the determinant scaling rule: for  $n\times n$  matrix  $S$ ,

$$
\det(tS)=t^n\det(S)\quad\Rightarrow\quad \log\det(tS)=n\log t + \log\det(S).
$$

So

$$
d(t\mathbf 1)=\log\det(S) + n\log t - mt + n.
$$

### Step 3: Maximize this over  $t>0$  (analytic optimum)

Define

$$
\phi(t) := \log\det(S) + n\log t - mt + n.
$$

 $\log\det(S)$  and  $n$  are constants here, so the only nontrivial part is  $n\log t - mt$ .

Differentiate:

$$
\phi'(t)=\frac{n}{t} - m.
$$

Set  $\phi'(t)=0$ :

$$
\frac{n}{t}=m \quad\Rightarrow\quad t^\star=\frac{n}{m}.
$$

Second derivative:

$$
\phi''(t)=-\frac{n}{t^2}<0,
$$

so  $t^\star$  is indeed a maximizer.

Plug  $t^\star=n/m$  into  $\phi(t)$ :

$$
\phi(t^\star)=\log\det(S) + n\log\Big(\frac{n}{m}\Big) - m\cdot\frac{n}{m} + n = \log\det(S) + n\log\Big(\frac{n}{m}\Big) - n + n = \log\det(S) + n\log\Big(\frac{n}{m}\Big).
$$

So we have found a concrete dual feasible point giving the bound

$$
p^\star \ \ge\ d(\lambda^\star)=\log\det(S) + n\log\Big(\frac{n}{m}\Big) = \log\det(S) - n\log\Big(\frac{m}{n}\Big).
$$

### Step 4: Compare with  $f_0(X_{\text{sim}})=\log\det(S)$ 

We already computed:

$$
f_0(X_{\text{sim}})=\log\det(S).
$$

Thus

$$
f_0(X_{\text{sim}}) - p^\star \le \log\det(S) - \Big(\log\det(S) - n\log\Big(\frac{m}{n}\Big)\Big) = n\log\Big(\frac{m}{n}\Big).
$$

This is the “objective gap” bound.

### Step 5: Convert objective gap into a volume ratio

Recall:

$$
\mathrm{vol}(\mathcal E(X))=\mathrm{vol}(B_n)\,\exp\Big(\frac12\log\det(X^{-1})\Big) =\mathrm{vol}(B_n)\,\exp\Big(\frac12 f_0(X)\Big).
$$

So for two ellipsoids  $X_1,X_2$ ,

$$
\frac{\mathrm{vol}(\mathcal E(X_1))}{\mathrm{vol}(\mathcal E(X_2))} = \exp\Big(\frac12(f_0(X_1)-f_0(X_2))\Big),
$$

because  $\mathrm{vol}(B_n)$  cancels.

Let  $X^\star$  be optimal. Then  $f_0(X^\star)=p^\star$ . Therefore

$$
\frac{\mathrm{vol}(\mathcal E(X_{\text{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \exp\Big(\frac12(f_0(X_{\text{sim}})-p^\star)\Big) \le \exp\Big(\frac12 \, n\log\Big(\frac{m}{n}\Big)\Big) = \Big(\frac{m}{n}\Big)^{n/2}.
$$

That’s exactly the desired factor bound.

* * *

What this is secretly saying (intuition, but honest)
----------------------------------------------------

*    $S=\sum a_i a_i^T$  is like an “uncentered scatter/covariance” matrix of the points.
*   Taking  $X_{\text{sim}}=S^{-1}$  makes the ellipsoid adapt to the global spread of the points.
*   The proof shows: even if this is not the true minimum-volume ellipsoid, it’s never catastrophically worse—its volume is within  $(m/n)^{n/2}$ .

This factor depends only on the **number of points  $m$ ** and the **dimension  $n$ **, not on the geometry of the particular  $a_i$ . So it’s a worst-case guarantee.

* * *

## Response:
Excellent — this is one of the most elegant and deep exercises in convex optimization. You're dealing with **covering ellipsoids**, duality, Schur complements, and volume ratios. The goal is to understand how much worse a simple feasible solution is, compared to the true minimum-volume ellipsoid. The exercise asks for a _quantitative performance guarantee_ on a specific candidate ellipsoid.

* * *

### ✅ Problem Context: What is this about?

You are given a set of points  $a_1, \dots, a_m \in \mathbb{R}^n$  and are trying to find the **minimum-volume ellipsoid** centered at the origin that contains them. This is done via a semidefinite program (SDP) involving the **log-det** function.

Then, you are asked to:

1.  Construct a specific simple candidate matrix  $X_{\text{sim}}$ ,
2.  Show it's feasible,
3.  Use the dual problem to **bound how suboptimal** this candidate is,
4.  Show that its volume is at most a small factor worse than the minimum possible.

* * *

### 🧭 Full Roadmap for Exercise 5.9 (Suboptimality of a Simple Covering Ellipsoid)

We’ll do this in **6 stages**.

* * *

#### 🔹**Stage 1 — Problem Setup and Geometry of Covering Ellipsoids**

*   What is a covering ellipsoid?
*   What does the SDP for minimum-volume ellipsoid do?
*   Why is log(det  $X^{-1}$ ) the right objective?
*   What does the constraint  $a_i^T X a_i \le 1$  geometrically mean?

* * *

#### 🔹**Stage 2 — Primal SDP for Minimum-Volume Ellipsoid**

*   Recap the primal problem:
    $$
    \min_{X \in \mathbb{S}_{++}^n} \log \det(X^{-1}) \quad \text{s.t. } a_i^T X a_i \le 1
    $$
*   Why is this convex? What’s the domain?
*   Interpret the constraint geometrically: containment of points in ellipsoid.
*   Volume formula for ellipsoid  $\mathcal{E}(X) = \{ x \mid x^T X x \le 1 \}$  is proportional to  $\frac{1}{\sqrt{\det X}}$ .

* * *

#### 🔹**Stage 3 — The Simple Feasible Solution  $X_{\text{sim}}$ **

*   Define:
    $$
    X_{\text{sim}} := \left( \sum_{k=1}^m a_k a_k^T \right)^{-1}
    $$
*   Goal: show it satisfies  $a_i^T X a_i \le 1$ 
*   Use Schur complements to verify feasibility.

* * *

#### 🔹**Stage 4 — Dual Problem and Suboptimality Bound**

*   Write out dual of the log-det primal SDP:
    $$
    \max_{\lambda \ge 0} \log \det \left( \sum_{i=1}^m \lambda_i a_i a_i^T \right) - \mathbf{1}^T \lambda + n
    $$
*   Explain derivation, dual variables, and feasibility.

* * *

#### 🔹**Stage 5 — Restricting Dual to Simple Form  $\lambda_i = t$ **

*   Restrict dual variables to  $\lambda_i = t$  for all  $i$ 
*   Plug into dual objective
*   Optimize over scalar  $t > 0$ 

* * *

#### 🔹**Stage 6 — Compare Volumes**

*   Use optimal  $t$  to compute dual objective value
*   Compare log-determinants → volume ratio
*   Show the suboptimality factor is bounded by  $(m/n)^{n/2}$ 

* * *

### 🚀 Let’s Begin: Stage 1 — Covering Ellipsoids and Problem Geometry

Let’s now begin **Stage 1** in full detail. Once we complete this, we’ll proceed to Stage 2.

Shall I proceed?

## Response:
Great — let’s now go **zero-to-hero** on **Stage 1: Understanding Covering Ellipsoids and the Problem Geometry**.  
We will explain everything as if you’ve never seen this material before. Buckle up.

* * *

✅ Stage 1: Geometry and Setup — What is a “Covering Ellipsoid”?
---------------------------------------------------------------

### 🔹 1.1 What is an ellipsoid?

Let’s define a **centered ellipsoid** in  $\mathbb{R}^n$ :

> An ellipsoid centered at the origin is a set of the form:
> 
> $$
> \mathcal{E}(X) := \left\{ x \in \mathbb{R}^n \;\middle|\; x^T X x \leq 1 \right\},
> $$
> 
> where  $X \in \mathbb{S}_{++}^n$ , the set of **symmetric positive definite**  $n \times n$  matrices.

This is the generalization of a **sphere**. If  $X = I$ , the ellipsoid is the **unit ball**. If  $X$  has different eigenvalues or is rotated, you get stretched, rotated shapes — still convex, closed, and bounded.

🧠 **Intuition**: The matrix  $X$  determines:

*   the **orientation** of the ellipsoid (via eigenvectors),
*   the **shape/length of axes** (via eigenvalues).

* * *

### 🔹 1.2 The Ellipsoid as a Feasible Set

In convex optimization, we often write feasible sets like:

$$
x^T X x \le 1.
$$

This is exactly the constraint that defines an ellipsoid. So when we say:

> “The point  $x$  is in the ellipsoid,”  
> we mean it satisfies the inequality  $x^T X x \le 1$ .

* * *

### 🔹 1.3 What does it mean to “cover” points?

Now, suppose we are **given points**:

$$
a_1, a_2, \dots, a_m \in \mathbb{R}^n.
$$

We want to find an ellipsoid **centered at the origin** that contains **all of these points**.

So we require:

$$
a_i^T X a_i \le 1, \quad \text{for all } i = 1, \dots, m.
$$

This means that each  $a_i$  lies _inside or on the boundary_ of the ellipsoid defined by  $X$ .

* * *

### 🔹 1.4 The Optimization Problem

We want the **smallest ellipsoid** that covers all the points. But how do we define “smallest”?

Ellipsoids don’t have radius directly — instead, their **volume** is what we minimize.

The volume of  $\mathcal{E}(X) = \{ x \mid x^T X x \le 1 \}$  is:

$$
\text{Vol}(X) \propto \frac{1}{\sqrt{\det X}}.
$$

So to **minimize the volume**, we **maximize**  $\sqrt{\det X}$ , or equivalently, **minimize**  $\log \det X^{-1}$ .

So the **primal problem** is:

$$
\begin{aligned} \min_{X \in \mathbb{S}_{++}^n} \quad & f_0(X) := \log \det (X^{-1}) \\ \text{s.t.} \quad & a_i^T X a_i \le 1, \quad i = 1, \dots, m. \end{aligned}
$$

* * *

### 🔹 1.5 Let’s Interpret Every Piece

| Term | Meaning |
| --- | --- |
|  $X \in \mathbb{S}_{++}^n$  | Ellipsoid matrix (must be symmetric and positive definite — this ensures the shape is well-defined and bounded). |
|  $a_i^T X a_i \le 1$  | Means that  $a_i$  is inside the ellipsoid defined by  $X$ . |
|  $\log \det(X^{-1})$  | Equivalent to  $-\log \det X$ , which measures inverse of volume. Minimizing this finds smallest-volume ellipsoid. |

* * *

### 🔹 1.6 Why is this convex?

*   The function  $\log \det X^{-1}$  is convex over the domain  $X \in \mathbb{S}_{++}^n$ .
*   Each constraint  $a_i^T X a_i \le 1$  is **linear in  $X$ ** because:
    $$
    a_i^T X a_i = \mathrm{Tr}(X a_i a_i^T),
    $$
    and trace is linear in  $X$ . So each constraint is affine.

Therefore, the whole optimization is a **convex program** over the space of positive definite matrices.

* * *

### 🔹 1.7 What the Dual Will Do (Preview)

This problem has a dual — and that dual gives us **lower bounds** on how small the volume _could possibly be_.

We’ll later restrict the dual variables to a simple form and evaluate how close a “simple guess”  $X_{\text{sim}}$  gets to the optimal ellipsoid.

* * *

### ✅ Summary of Stage 1

*   A centered ellipsoid is the set  $\{ x \mid x^T X x \le 1 \}$ .
*   To cover points  $a_1, \dots, a_m$ , we require  $a_i^T X a_i \le 1$ .
*   Volume of the ellipsoid is proportional to  $1/\sqrt{\det X}$ .
*   So minimizing volume = minimizing  $\log \det X^{-1}$ .
*   The problem is convex and has a meaningful dual.
*   We’ll analyze a **simple candidate solution**  $X_{\text{sim}}$  and see how close it gets.

* * *

✅ Shall we now proceed to **Stage 2**: fully unpacking the **primal problem** and writing all its ingredients in depth, including feasibility domain and convexity checks?

## Response:
Excellent question — let’s now rigorously unpack **why minimizing  $\log \det(X^{-1})$ ** is equivalent to **maximizing  $\sqrt{\det X}$ **, and how this connects to **minimizing the volume** of an ellipsoid.

We’ll go step-by-step, building from first principles — **no handwaving**.

* * *

🎯 Goal: Why is minimizing  $\log \det(X^{-1})$  the same as minimizing ellipsoid volume?
-----------------------------------------------------------------------------------------

* * *

🔹 Step 1: Volume of a Centered Ellipsoid
-----------------------------------------

We begin with the ellipsoid:

$$
\mathcal{E}(X) = \left\{ x \in \mathbb{R}^n \mid x^T X x \le 1 \right\},
$$

where  $X \in \mathbb{S}_{++}^n$  is symmetric positive definite.

This is a general ellipsoid centered at the origin.

Now: what's its **volume**?

Let’s relate this to a **change of variables** from the **unit ball**.

* * *

### ✅ The geometric trick (volume under transformation)

Let’s perform the following **linear transformation**:

$$
x = A u, \quad \text{where } A \in \mathbb{R}^{n \times n}, \text{ and } X = A^{-T} A^{-1}.
$$

> This means  $X = (A A^T)^{-1}$  ⇒ so  $A$  is a kind of square root of  $X^{-1}$ , or more precisely:

$$
A = X^{-1/2} \quad \Rightarrow \quad X = A^{-T} A^{-1}.
$$

Let’s compute:

$$
x^T X x = u^T A^T X A u = u^T A^T A^{-T} A^{-1} A u = u^T u.
$$

So we get:

$$
x \in \mathcal{E}(X) \iff u \in \mathcal{B}_n := \{ u \in \mathbb{R}^n \mid \|u\|_2 \le 1 \}.
$$

Thus:

$$
\mathcal{E}(X) = \{ x = A u \mid u \in \mathcal{B}_n \}.
$$

Hence, **the ellipsoid is the image of the unit ball under linear map  $A$ **.

* * *

### 🧮 Volume under linear map

Fact (linear algebra):

> The volume of a transformed body under a linear map  $A$  is:

$$
\mathrm{Vol}(A(S)) = |\det A| \cdot \mathrm{Vol}(S).
$$

Apply this to our ellipsoid:

$$
\mathrm{Vol}(\mathcal{E}(X)) = \mathrm{Vol}(A \mathcal{B}_n) = |\det A| \cdot \mathrm{Vol}(\mathcal{B}_n).
$$

Recall:  $A = X^{-1/2}$ , so:

$$
|\det A| = \det(X^{-1/2}) = (\det X)^{-1/2}.
$$

Thus:

$$
\mathrm{Vol}(\mathcal{E}(X)) = \frac{\mathrm{Vol}(\mathcal{B}_n)}{\sqrt{\det X}}.
$$

This is **the key formula**:

* * *

### ✅ Final volume formula:

$$
\boxed{ \mathrm{Vol}(\mathcal{E}(X)) = \frac{c_n}{\sqrt{\det X}}, } \quad \text{where } c_n := \mathrm{Vol}(\mathcal{B}_n).
$$

This constant  $c_n$  only depends on dimension, not  $X$ .

* * *

🔹 Step 2: What are we trying to minimize?
------------------------------------------

We are trying to find the **smallest volume ellipsoid** covering the given points. Since  $c_n$  is fixed, minimizing volume is equivalent to:

$$
\min_X \frac{1}{\sqrt{\det X}}.
$$

But minimizing  $1/\sqrt{\det X}$  is the same as maximizing  $\sqrt{\det X}$ , or:

$$
\max_X \det X \quad \text{or} \quad \max_X \log \det X.
$$

So minimizing volume is the same as **maximizing  $\log \det X$ **.

* * *

🔹 Step 3: Primal uses  $\log \det X^{-1}$ . Why?
-------------------------------------------------

In the actual problem, we are **minimizing  $\log \det (X^{-1})$ **.

But:

$$
\log \det (X^{-1}) = -\log \det X.
$$

So:

$$
\min_X \log \det (X^{-1}) \quad \Longleftrightarrow \quad \max_X \log \det X.
$$

These are the same optimization, just written differently. Why this way?

Because:

*    $\log \det X^{-1}$  is a **convex** function over  $\mathbb{S}_{++}^n$ ,
*   while  $\log \det X$  is **concave**.

Optimization frameworks like CVX prefer to **minimize convex functions**, not maximize concave ones.

So we flip the sign and turn it into a minimization of a convex function.

* * *

✅ Final Takeaways
-----------------

| Expression | Meaning |
| --- | --- |
|  $\text{Vol}(\mathcal{E}(X)) = \frac{c_n}{\sqrt{\det X}}$  | Volume of ellipsoid |
|  $\min \text{Vol} \Longleftrightarrow \max \sqrt{\det X} \Longleftrightarrow \max \log \det X \Longleftrightarrow \min \log \det X^{-1}$  | All equivalent objectives (monotonic transforms) |

So:

$$
\boxed{ \min_X \log \det (X^{-1}) \quad \text{is exactly minimizing ellipsoid volume}. }
$$

This is why log-determinant minimization is the standard way to find minimum-volume ellipsoids in convex optimization.

* * *

✅ Let me know if you want to move to **Stage 2: Full unpacking of the primal problem setup**, or if you'd like a detour into matrix log-determinant properties.

## Response:
Perfect. You now have exactly the right geometric picture in your head:  
we are choosing a linear map  $X^{-1/2}$  that stretches the unit ball just enough to cover all points, while making that stretched ball as small as possible.

Now let’s do **part (a)** properly, from first principles.

* * *

Part (a)
========

We are given the candidate

$$
X_{\text{sim}} \;=\; \Big(\sum_{k=1}^m a_k a_k^T\Big)^{-1}.
$$

We must prove that it is **feasible**, meaning

$$
a_i^T X_{\text{sim}} a_i \;\le\; 1 \quad \text{for every } i.
$$

This means every point  $a_i$  lies inside the ellipsoid.

* * *

Step 1 — Define the key matrix
==============================

Let

$$
S \;=\; \sum_{k=1}^m a_k a_k^T.
$$

Then

$$
X_{\text{sim}} = S^{-1}.
$$

Before anything else, we must check that this inverse even exists.

* * *

Step 2 — Why is  $S$  invertible?
=================================

We are told the vectors  $a_1,\dots,a_m$  **span**  $\mathbb R^n$ .

That means: for every nonzero vector  $x$ , at least one  $a_k$  satisfies

$$
a_k^T x \neq 0.
$$

Now compute

$$
x^T S x = x^T\Big(\sum_{k=1}^m a_k a_k^T\Big)x = \sum_{k=1}^m x^T a_k a_k^T x = \sum_{k=1}^m (a_k^T x)^2.
$$

This is a sum of squares. It is zero only if every term is zero, i.e.,  
 $a_k^T x=0$  for all  $k$ . But that means  $x$  is orthogonal to the span of the  $a_k$ ’s, which is all of  $\mathbb R^n$ . So  $x=0$ .

Therefore,

$$
x^T S x>0 \quad \text{for all } x\neq 0,
$$

so  $S$  is positive definite and invertible.

Thus  $X_{\text{sim}}=S^{-1}$  is well-defined.

* * *

Step 3 — What we must prove
===========================

Feasibility means

$$
a_i^T S^{-1} a_i \le 1 \quad\text{for all }i.
$$

This is a scalar inequality.  
We will prove it using a beautiful geometric idea: **Schur complements**.

* * *

Step 4 — Build a block matrix that is obviously positive semidefinite
=====================================================================

Fix some index  $i$ . Consider the block matrix

$$
M_i = \begin{bmatrix} S & a_i\\[4pt] a_i^T & 1 \end{bmatrix}.
$$

We will show that  $M_i \succeq 0$ .

Write it as a sum of outer products:

For  $k\neq i$ , define

$$
\tilde a_k = \begin{bmatrix} a_k \\ 0 \end{bmatrix}, \qquad \tilde a_i' = \begin{bmatrix} a_i \\ 1 \end{bmatrix}.
$$

Now compute

$$
\sum_{k\neq i} \tilde a_k \tilde a_k^T = \begin{bmatrix} \sum_{k\neq i} a_k a_k^T & 0\\ 0 & 0 \end{bmatrix},
$$
 
$$
\tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix}.
$$

Add them:

$$
\sum_{k\neq i} \tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_k a_k a_k^T & a_i\\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Each outer product is positive semidefinite, and sums of PSD matrices are PSD.  
So

$$
M_i \succeq 0.
$$

* * *

Step 5 — Apply the Schur complement
===================================

A basic theorem:

If  $S\succ 0$ , then

$$
\begin{bmatrix} S & u\\ u^T & \alpha \end{bmatrix} \succeq 0 \quad\Longleftrightarrow\quad \alpha - u^T S^{-1} u \ge 0.
$$

Apply it to  $M_i$ , where  $u=a_i$  and  $\alpha=1$ .

Since  $S\succ 0$  and  $M_i\succeq 0$ , we get

$$
1 - a_i^T S^{-1} a_i \ge 0.
$$

Therefore,

$$
a_i^T S^{-1} a_i \le 1.
$$

But  $S^{-1}=X_{\text{sim}}$ , so

$$
a_i^T X_{\text{sim}} a_i \le 1.
$$

This holds for every  $i$ .

* * *

Final conclusion (part a)
=========================

$$
\boxed{ X_{\text{sim}} = \Big(\sum_{k=1}^m a_k a_k^T\Big)^{-1} \text{ satisfies } a_i^T X_{\text{sim}} a_i \le 1 \text{ for all } i. }
$$

So the ellipsoid defined by  $X_{\text{sim}}$  contains all the points.  
It is a valid covering ellipsoid.

In the next step (part b), we’ll quantify **how far** this simple ellipsoid is from the best possible one, using the dual.

## Response:
Perfect — let’s do this in the clean mathematical style you’re asking for:

1.  **First: a crisp statement of part (a)**
2.  **Then: a slow, newcomer-level breakdown and proof, unpacking every step**

No shortcuts, no hidden tricks.

* * *

**Part (a) — Statement**
------------------------

Let  $a_1,\dots,a_m \in \mathbb{R}^n$  span  $\mathbb{R}^n$ , and define

$$
X_{\mathrm{sim}} \;=\; \Big( \sum_{k=1}^m a_k a_k^T \Big)^{-1}.
$$

**Claim:**  
 $X_{\mathrm{sim}}$  is feasible for the minimum-volume ellipsoid problem, i.e.,

$$
a_i^T X_{\mathrm{sim}} a_i \;\le\; 1 \quad \text{for all } i = 1,\dots,m.
$$

Equivalently, every point  $a_i$  lies inside the ellipsoid

$$
\mathcal E(X_{\mathrm{sim}}) = \{x : x^T X_{\mathrm{sim}} x \le 1\}.
$$

* * *

**Part (a) — Breakdown and Proof (Zero-to-Hero)**
-------------------------------------------------

* * *

**Step 1 — Introduce the core matrix**
--------------------------------------

Define

$$
S := \sum_{k=1}^m a_k a_k^T.
$$

Then

$$
X_{\mathrm{sim}} = S^{-1}.
$$

Before doing anything else, we must answer a basic question:

> **Does  $S^{-1}$  even exist?**

* * *

**Step 2 — Why  $S$  is invertible (and positive definite)**
------------------------------------------------------------

Because the vectors  $a_1,\dots,a_m$  **span  $\mathbb{R}^n$ **.

Take any vector  $x \in \mathbb{R}^n$ . Compute the quadratic form:

$$
x^T S x = x^T \Big( \sum_{k=1}^m a_k a_k^T \Big) x = \sum_{k=1}^m x^T a_k a_k^T x = \sum_{k=1}^m (a_k^T x)^2.
$$

This expression is:

*   a **sum of squares** → always  $\ge 0$ ,
*   equal to zero **only if** every  $a_k^T x = 0$ .

But  $a_1,\dots,a_m$  span  $\mathbb{R}^n$ , so the only vector orthogonal to all of them is  $x=0$ .

Therefore,

$$
x^T S x > 0 \quad \text{for all } x \neq 0.
$$

This means:

$$
S \succ 0 \quad \Rightarrow \quad S \text{ is invertible}.
$$

So  $X_{\mathrm{sim}} = S^{-1}$  is well-defined.

* * *

**Step 3 — What feasibility requires**
--------------------------------------

Feasibility means satisfying the ellipsoid constraints:

$$
a_i^T X_{\mathrm{sim}} a_i \le 1 \quad \text{for each } i.
$$

Substituting  $X_{\mathrm{sim}} = S^{-1}$ , the goal becomes:

$$
a_i^T S^{-1} a_i \le 1.
$$

This is **not obvious** from inspection. We need a structural argument.

* * *

**Step 4 — Build a block matrix that encodes the inequality**
-------------------------------------------------------------

Fix an index  $i$ .

Consider the block matrix:

$$
M_i := \begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

Our plan is:

1.  Show  $M_i \succeq 0$ ,
2.  Use the Schur complement to extract  $a_i^T S^{-1} a_i \le 1$ .

* * *

**Step 5 — Prove  $M_i$  is positive semidefinite**
---------------------------------------------------

We do this by writing  $M_i$  as a sum of **outer products**.

Define vectors in  $\mathbb{R}^{n+1}$ :

*   For  $k \neq i$ ,
    $$
    \tilde a_k := \begin{bmatrix} a_k \\ 0 \end{bmatrix}.
    $$
*   For index  $i$ ,
    $$
    \tilde a_i' := \begin{bmatrix} a_i \\ 1 \end{bmatrix}.
    $$

Compute the outer products:

$$
\tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0 \\ 0 & 0 \end{bmatrix}, \quad \tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

Now sum:

$$
\sum_{k \neq i} \tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_k a_k a_k^T & a_i \\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Each outer product is positive semidefinite.  
Sums of positive semidefinite matrices remain positive semidefinite.

Therefore,

$$
M_i \succeq 0.
$$

* * *

**Step 6 — Apply the Schur complement**
---------------------------------------

A fundamental result:

If  $S \succ 0$ , then

$$
\begin{bmatrix} S & u \\ u^T & \alpha \end{bmatrix} \succeq 0 \quad \Longleftrightarrow \quad \alpha - u^T S^{-1} u \ge 0.
$$

Apply this to  $M_i$ :

*    $u = a_i$ ,
*    $\alpha = 1$ .

Since  $S \succ 0$  and  $M_i \succeq 0$ , we obtain:

$$
1 - a_i^T S^{-1} a_i \ge 0.
$$

Equivalently,

$$
a_i^T S^{-1} a_i \le 1.
$$

* * *

**Step 7 — Conclude feasibility**
---------------------------------

Because this holds for **every** index  $i$ ,

$$
\boxed{ a_i^T X_{\mathrm{sim}} a_i \le 1 \quad \forall i, }
$$

which proves that  $X_{\mathrm{sim}}$  is feasible.

* * *

**What you should internalize**
-------------------------------

*    $S = \sum a_k a_k^T$  encodes _global spread_ of the points.
*   The inequality  $a_i^T S^{-1} a_i \le 1$  comes from a **hidden PSD structure**.
*   Schur complements translate block-matrix positivity into scalar quadratic bounds.
*   No magic: everything reduces to linear algebra and geometry.

When you’re ready, we move to **part (b)** — where duality turns this feasibility result into a **quantitative approximation guarantee**.

## Response:
Excellent — these are exactly the _nontrivial_ steps.  
What follows is a **slow, microscope-level unpacking** of **Steps 4, 5, and 6**, with every hidden idea dragged into the light.

I will **not** assume you already “believe” Schur complements or PSD block tricks. We will _build the logic_.

* * *

Where we are
============

We want to prove, for a fixed index  $i$ ,

$$
a_i^T S^{-1} a_i \;\le\; 1, \quad\text{where}\quad S = \sum_{k=1}^m a_k a_k^T.
$$

Directly proving this inequality is hard.  
So instead, we **encode it inside a matrix inequality** that we _can_ prove.

That is the purpose of Steps 4–6.

* * *

Step 4 — Why introduce the block matrix at all?
===============================================

### 4.1 The strategic problem

We want a scalar inequality involving  $S^{-1}$ :

$$
a_i^T S^{-1} a_i \le 1.
$$

But:

*    $S^{-1}$  is global and implicit,
*   scalar quadratic inequalities are hard to prove directly.

So we ask:

> Is there a **matrix inequality** whose truth _forces_ this scalar inequality?

The answer is yes — and that inequality is a **block PSD condition**.

* * *

### 4.2 The key idea (in words)

Instead of proving  
“this number is ≤ 1,”

we prove  
“this matrix is positive semidefinite.”

Why this works:

*   PSD matrices encode **infinitely many inequalities at once**.
*   Schur complements let us _extract_ the exact inequality we want.

* * *

### 4.3 The block matrix we construct

We define, for each  $i$ ,

$$
M_i := \begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

This is not random. Each block has meaning:

*   Upper-left block  $S$ : global geometry of all points
*   Off-diagonal blocks  $a_i$ : the specific point we are testing
*   Bottom-right scalar  $1$ : the ellipsoid boundary

The claim will be:

$$
M_i \succeq 0.
$$

Once that is proven, **Step 6 will extract the inequality**.

* * *

Step 5 — Why is  $M_i$  positive semidefinite?
==============================================

This is the most subtle part.  
We prove PSD by **construction**, not by eigenvalues.

* * *

5.1 Reminder: what does PSD mean?
---------------------------------

A symmetric matrix  $M$  is PSD if

$$
z^T M z \ge 0 \quad \text{for all vectors } z.
$$

A guaranteed way to get PSD matrices is:

> Any matrix of the form  $v v^T$  is PSD.

And sums of PSD matrices remain PSD.

* * *

5.2 Lift the vectors into higher dimension
------------------------------------------

We work in  $\mathbb{R}^{n+1}$ .

Define new vectors:

*   For  $k \neq i$ ,
    $$
    \tilde a_k = \begin{bmatrix} a_k \\ 0 \end{bmatrix}
    $$
*   For index  $i$ ,
    $$
    \tilde a_i' = \begin{bmatrix} a_i \\ 1 \end{bmatrix}
    $$

This “lifting” is deliberate:

*   the extra coordinate will generate the bottom-right block  $1$ ,
*   while keeping the original geometry in the top-left block.

* * *

5.3 Compute the outer products
------------------------------

For  $k \neq i$ :

$$
\tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0 \\ 0 & 0 \end{bmatrix}.
$$

For  $i$ :

$$
\tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

Each of these matrices is PSD because it is an outer product.

* * *

5.4 Sum them
------------

Now add everything:

$$
\sum_{k \neq i} \tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_k a_k a_k^T & a_i \\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Because:

*   each term is PSD,
*   sums of PSD matrices are PSD,

we conclude:

$$
\boxed{M_i \succeq 0.}
$$

This step is **pure geometry** — no inverses, no tricks.

* * *

Step 6 — Extracting the inequality via the Schur complement
===========================================================

Now comes the payoff.

* * *

6.1 What is the Schur complement saying?
----------------------------------------

Let

$$
M = \begin{bmatrix} A & u \\ u^T & \alpha \end{bmatrix}, \quad\text{with } A \succ 0.
$$

Then the following are equivalent:

$$
M \succeq 0 \quad \Longleftrightarrow \quad \alpha - u^T A^{-1} u \ge 0.
$$

This is not a trick — it is a theorem from linear algebra.

* * *

6.2 Why this makes sense intuitively
------------------------------------

Think of  $A$  as fixing the geometry in the first  $n$  coordinates.  
The scalar  $\alpha$  must be large enough to dominate the coupling  $u$ .

If  $\alpha$  is too small, the matrix becomes indefinite.

So positivity of the full matrix _forces_:

$$
u^T A^{-1} u \le \alpha.
$$

* * *

6.3 Apply it to our matrix
--------------------------

In our case:

*    $A = S$ ,
*    $u = a_i$ ,
*    $\alpha = 1$ .

We already proved:

$$
S \succ 0 \quad\text{and}\quad M_i \succeq 0.
$$

Therefore,

$$
1 - a_i^T S^{-1} a_i \ge 0.
$$

Rearranging:

$$
\boxed{ a_i^T S^{-1} a_i \le 1. }
$$

* * *

What just happened (big picture)
================================

Let’s say it plainly:

*   We **encoded** the inequality inside a matrix.
*   We **proved** that matrix is PSD by construction.
*   PSD + invertibility triggered the Schur complement.
*   The Schur complement **forces exactly the inequality we want**.

No guessing. No luck.

* * *

Why this method is powerful (and worth remembering)
===================================================

This pattern appears everywhere in convex optimization:

*   ellipsoids,
*   LMIs,
*   SDP relaxations,
*   control theory,
*   robust optimization.

Whenever you see a quadratic inequality involving an inverse, think:

> “Can I lift this into a block PSD matrix and use Schur complements?”

That instinct is what separates _symbol pushing_ from _geometric understanding_.

* * *

If you’re ready, the next logical step is **part (b)** — where duality turns this feasibility into a **quantitative approximation guarantee**.

## Response:
Excellent — this is the **core geometric step**, and it’s worth unpacking it until it feels _inevitable_, not clever.

We will prove carefully, from first principles, that

$$
M_i = \begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix} \quad\text{is positive semidefinite.}
$$

I will proceed in **three equivalent ways**, starting from the most fundamental.  
The **outer-product proof** is the one used in the solution, but I’ll also give a **direct quadratic-form proof** so you see the same fact from two angles.

* * *

0\. What does “positive semidefinite” mean?
-------------------------------------------

A symmetric matrix  $M$  is **positive semidefinite (PSD)** if

$$
z^T M z \;\ge\; 0 \quad \text{for every vector } z.
$$

There is **no reference to eigenvalues** here.  
This is the definition we will use.

* * *

1\. First-principles proof via outer products (the constructive proof)
----------------------------------------------------------------------

This proof shows **where the matrix comes from**, not just that it works.

* * *

### 1.1 Key fact (do not skip)

For any vector  $v$ ,

$$
v v^T \succeq 0.
$$

Why?

For any  $z$ ,

$$
z^T (v v^T) z = (v^T z)^2 \ge 0.
$$

This is the atomic building block of PSD matrices.

* * *

### 1.2 Lift the vectors into one higher dimension

We now move from  $\mathbb R^n$  to  $\mathbb R^{n+1}$ .

Define:

*   For  $k \neq i$ ,
    $$
    \tilde a_k = \begin{bmatrix} a_k \\ 0 \end{bmatrix},
    $$
*   For the index  $i$ ,
    $$
    \tilde a_i' = \begin{bmatrix} a_i \\ 1 \end{bmatrix}.
    $$

These are ordinary vectors — nothing fancy yet.

* * *

### 1.3 Compute their outer products explicitly

For  $k \neq i$ :

$$
\tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0 \\ 0 & 0 \end{bmatrix}.
$$

For  $i$ :

$$
\tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

Each of these matrices is PSD, because each is an outer product.

* * *

### 1.4 Sum them

Now add all of them:

$$
\sum_{k \neq i} \tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_k a_k a_k^T & a_i \\ a_i^T & 1 \end{bmatrix}.
$$

But recall the definition:

$$
S = \sum_k a_k a_k^T.
$$

So the sum becomes exactly:

$$
\boxed{ M_i = \begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix}. }
$$

Because:

*   each term is PSD,
*   sums of PSD matrices are PSD,

we conclude:

$$
\boxed{M_i \succeq 0.}
$$

This completes the proof.

* * *

2\. Direct quadratic-form proof (no lifting, no tricks)
-------------------------------------------------------

Now let’s prove the same fact **directly from the definition**.

* * *

### 2.1 Take an arbitrary vector

Let

$$
z = \begin{bmatrix} x \\ t \end{bmatrix} \in \mathbb R^{n+1}.
$$

We must show:

$$
z^T M_i z \ge 0.
$$

* * *

### 2.2 Expand the quadratic form

$$
\begin{aligned} z^T M_i z &= \begin{bmatrix} x^T & t \end{bmatrix} \begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix} \begin{bmatrix} x \\ t \end{bmatrix} \\ &= x^T S x + 2 t\, a_i^T x + t^2. \end{aligned}
$$

* * *

### 2.3 Expand  $x^T S x$ 

Recall:

$$
S = \sum_{k=1}^m a_k a_k^T.
$$

So:

$$
x^T S x = \sum_{k=1}^m (a_k^T x)^2.
$$

Substitute:

$$
z^T M_i z = \sum_{k=1}^m (a_k^T x)^2 + 2 t\, a_i^T x + t^2.
$$

* * *

### 2.4 Rearrange as a sum of squares

Split off the  $k=i$  term:

$$
= \sum_{k \neq i} (a_k^T x)^2 + \big( (a_i^T x)^2 + 2 t\, a_i^T x + t^2 \big).
$$

Recognize the perfect square:

$$
(a_i^T x + t)^2 = (a_i^T x)^2 + 2 t\, a_i^T x + t^2.
$$

Thus:

$$
z^T M_i z = \sum_{k \neq i} (a_k^T x)^2 + (a_i^T x + t)^2.
$$

* * *

### 2.5 Conclude positivity

Each term is a square, so each term is  $\ge 0$ .

Therefore:

$$
z^T M_i z \ge 0 \quad \text{for all } z.
$$

By definition,

$$
\boxed{M_i \succeq 0.}
$$

* * *

3\. What you should internalize
-------------------------------

*   The matrix  $M_i$  is **not arbitrary**.
*   It is literally a **sum of squared linear functionals**.
*   PSD here is not mysterious — it is _geometric inevitability_.

You can now see:

*   why the block matrix is chosen,
*   why the proof works,
*   why the Schur complement step that follows is valid.

This is one of the most important structural tricks in convex optimization — you’ve just unpacked it down to bedrock.

When you’re ready, we move on to **part (b)** and duality.

## Response:
Excellent catch. This is **exactly** the right place to slow down — nothing is allowed to “disappear” in a proof like this. Let’s resolve it cleanly and surgically.

* * *

Short answer (then we unpack it properly)
-----------------------------------------

The  $a_i a_i^T$  **did not go anywhere**.

It is contained **inside** the outer product  
 $\tilde a_i' \tilde a_i'^T$ .

When we sum:

*   all  $a_k a_k^T$  for  $k \neq i$ , and
*   the  $a_i a_i^T$  coming from  $\tilde a_i' \tilde a_i'^T$ ,

we recover **exactly**

$$
\sum_{k=1}^m a_k a_k^T = S
$$

in the upper-left block.

Now let’s unpack this _slowly and explicitly_ so nothing feels hand-wavy.

* * *

Step 1 — Write every outer product explicitly
---------------------------------------------

We defined two kinds of lifted vectors in  $\mathbb{R}^{n+1}$ .

### For  $k \neq i$ :

$$
\tilde a_k = \begin{bmatrix} a_k \\ 0 \end{bmatrix}
$$

Their outer product is:

$$
\tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0 \\ 0 & 0 \end{bmatrix}
$$

👉 **Upper-left block:**  $a_k a_k^T$   
👉 **No contribution** elsewhere

* * *

### For  $i$ :

$$
\tilde a_i' = \begin{bmatrix} a_i \\ 1 \end{bmatrix}
$$

Its outer product is:

$$
\tilde a_i' \tilde a_i'^T = \begin{bmatrix} \boxed{a_i a_i^T} & a_i \\ a_i^T & 1 \end{bmatrix}
$$

👉 **This already contains  $a_i a_i^T$ ** in the upper-left block  
👉 Plus the cross terms and the scalar  $1$ 

* * *

Step 2 — Now sum everything (very explicitly)
---------------------------------------------

We sum:

$$
\sum_{k \neq i} \tilde a_k \tilde a_k^T \;+\; \tilde a_i' \tilde a_i'^T
$$

Let’s add block by block.

* * *

### Upper-left block

From the first sum:

$$
\sum_{k \neq i} a_k a_k^T
$$

From the second term:

$$
+\, a_i a_i^T
$$

Total:

$$
\sum_{k \neq i} a_k a_k^T + a_i a_i^T = \sum_{k=1}^m a_k a_k^T = S
$$

✅ **Nothing disappeared. Nothing duplicated.**

* * *

### Upper-right block

*   From  $k \neq i$  terms: all zeros
*   From  $\tilde a_i' \tilde a_i'^T$ :  $a_i$ 

So total:

$$
a_i
$$

* * *

### Lower-left block

Same logic:

$$
a_i^T
$$

* * *

### Lower-right block

*   From  $k \neq i$  terms: all zeros
*   From  $\tilde a_i' \tilde a_i'^T$ :  $1$ 

So total:

$$
1
$$

* * *

Step 3 — Put it all together
----------------------------

After summing, the full matrix is:

$$
\begin{bmatrix} S & a_i \\ a_i^T & 1 \end{bmatrix} = M_i
$$

So the  $a_i a_i^T$ :

*   **was not removed**
*   **was not canceled**
*   **was not absorbed mysteriously**

It came **exactly once**, from the outer product of  
 $\begin{bmatrix} a_i \\ 1 \end{bmatrix}$ .

* * *

Step 4 — Why this construction is clever (conceptual insight)
-------------------------------------------------------------

This lifting trick is designed so that:

*   all points  $a_k$  contribute to the global geometry  $S$ ,
*   one special point  $a_i$  additionally creates:
    *   the off-diagonal coupling  $a_i$ ,
    *   the scalar  $1$ ,
*   all of it arises from **pure sums of squares**.

That’s why the resulting matrix is PSD _by construction_.

* * *

Final mental model (important)
------------------------------

Think of this as writing:

$$
z^T M_i z = \sum_{k \neq i} (a_k^T x)^2 + (a_i^T x + t)^2
$$

Every square contributes exactly once.

Nothing vanishes. Nothing sneaks in.

If you want, the next natural step is to **derive the Schur complement inequality directly from this sum-of-squares form**, without invoking any theorem name at all.

## Response:
Alright. Part (b) is where duality stops being “abstract” and becomes a **machine that prints approximation guarantees**.

I’ll do this in the same style: **state**, then **unpack step-by-step**, and end by converting the objective gap into the **volume ratio bound**.

* * *

Part (b) — Statement
--------------------

Let  $X^\star$  be an optimal solution of the primal (minimum-volume ellipsoid) problem, and let

$$
X_{\mathrm{sim}}=\Big(\sum_{k=1}^m a_k a_k^T\Big)^{-1}.
$$

Using the dual problem

$$
\begin{aligned} \max_{\lambda} \quad & \log\det\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big) - \mathbf 1^T\lambda + n\\ \text{s.t.}\quad & \lambda \succeq 0,\qquad \sum_{i=1}^m \lambda_i a_i a_i^T \succ 0, \end{aligned}
$$

show that

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \;\le\; \Big(\frac{m}{n}\Big)^{n/2}.
$$

* * *

1) What duality gives us: a sandwich inequality
-----------------------------------------------

Let the primal objective be

$$
f_0(X)=\log\det(X^{-1}).
$$

Let the optimal primal value be  $p^\star = f_0(X^\star)$ .  
Let the dual objective be  $d(\lambda)$ .

**Weak duality** says:

*   for any primal-feasible  $X$ :  $f_0(X)\ge p^\star$ ,
*   for any dual-feasible  $\lambda$ :  $d(\lambda)\le p^\star$ .

So for our  $X_{\mathrm{sim}}$  and any dual-feasible  $\lambda$ ,

$$
d(\lambda)\;\le\; p^\star\;\le\; f_0(X_{\mathrm{sim}}).
$$

This is the whole strategy:  
pick a **simple** feasible  $\lambda$ , compute  $d(\lambda)$ , and compare.

* * *

2) Compute the primal objective at  $X_{\mathrm{sim}}$ 
-------------------------------------------------------

Define again

$$
S := \sum_{k=1}^m a_k a_k^T.
$$

Then  $X_{\mathrm{sim}}=S^{-1}$ , hence  $X_{\mathrm{sim}}^{-1}=S$ .

So

$$
f_0(X_{\mathrm{sim}})=\log\det(X_{\mathrm{sim}}^{-1})=\log\det(S).
$$

* * *

3) Choose a simple dual-feasible  $\lambda$ : all equal weights
---------------------------------------------------------------

We take

$$
\lambda_1=\cdots=\lambda_m=t,\qquad t>0.
$$

Check feasibility:

*    $\lambda\succeq 0$  because  $t>0$ .
*    $\sum_i \lambda_i a_i a_i^T = t\sum_i a_i a_i^T = tS$ .  
    From part (a) / spanning,  $S\succ 0$ , so  $tS\succ 0$ .

So this  $\lambda$  is dual-feasible.

* * *

4) Evaluate the dual objective at  $\lambda=t\mathbf 1$ 
--------------------------------------------------------

Dual objective:

$$
d(\lambda)=\log\det\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big) - \mathbf 1^T\lambda + n.
$$

Plug in  $\lambda=t\mathbf 1$ :

*    $\sum_i \lambda_i a_i a_i^T = tS$ 
*    $\mathbf 1^T\lambda = \sum_{i=1}^m t = mt$ 

So

$$
d(t)=\log\det(tS)-mt+n.
$$

Now use the determinant scaling rule:

For  $n\times n$  matrix  $S$ ,

$$
\det(tS)=t^n\det(S) \quad\Rightarrow\quad \log\det(tS)=n\log t + \log\det(S).
$$

Thus

$$
d(t)=\log\det(S)+n\log t-mt+n.
$$

* * *

5) Optimize over  $t>0$  to get the best lower bound
----------------------------------------------------

We want the largest possible dual value, so maximize  $d(t)$  over  $t>0$ .

Ignore the constant  $\log\det(S)+n$  and maximize

$$
\psi(t)=n\log t - mt.
$$

Differentiate:

$$
\psi'(t)=\frac{n}{t}-m.
$$

Set to zero:

$$
\frac{n}{t}=m \quad\Rightarrow\quad t^\star=\frac{n}{m}.
$$

Second derivative:

$$
\psi''(t)=-\frac{n}{t^2}<0,
$$

so it’s a true maximum.

Plug  $t^\star$  back in:

$$
d(t^\star)=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-m\cdot\frac{n}{m}+n.
$$

Compute the last terms carefully:

*    $m\cdot \frac{n}{m}=n$ 

So

$$
d(t^\star)=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-n+n =\log\det(S)+n\log\Big(\frac{n}{m}\Big).
$$

Rewrite:

$$
n\log\Big(\frac{n}{m}\Big)=-n\log\Big(\frac{m}{n}\Big).
$$

So

$$
\boxed{ d(t^\star)=\log\det(S)-n\log\Big(\frac{m}{n}\Big). }
$$

* * *

6) Use weak duality to bound the primal suboptimality gap
---------------------------------------------------------

Weak duality gives

$$
p^\star \ge d(t^\star).
$$

So

$$
p^\star \ge \log\det(S)-n\log\Big(\frac{m}{n}\Big).
$$

But we also have

$$
f_0(X_{\mathrm{sim}})=\log\det(S).
$$

Subtract:

$$
f_0(X_{\mathrm{sim}})-p^\star \le \log\det(S) - \Big(\log\det(S)-n\log\Big(\frac{m}{n}\Big)\Big) = n\log\Big(\frac{m}{n}\Big).
$$

So the objective gap is at most

$$
\boxed{ f_0(X_{\mathrm{sim}})-f_0(X^\star) \le n\log\Big(\frac{m}{n}\Big). }
$$

* * *

7) Convert objective gap to a volume ratio
------------------------------------------

Volume of the ellipsoid  $\mathcal E(X)=\{x:x^T X x\le 1\}$  is

$$
\mathrm{vol}(\mathcal E(X)) = c_n \, \frac{1}{\sqrt{\det X}} = c_n \exp\Big(\frac12\log\det(X^{-1})\Big) = c_n \exp\Big(\frac12 f_0(X)\Big),
$$

where  $c_n=\mathrm{vol}(B_n)$  is a constant depending only on  $n$ .

Therefore, for any two ellipsoids  $X_1,X_2$ ,

$$
\frac{\mathrm{vol}(\mathcal E(X_1))}{\mathrm{vol}(\mathcal E(X_2))} = \exp\Big(\frac12(f_0(X_1)-f_0(X_2))\Big).
$$

Apply with  $X_1=X_{\mathrm{sim}}$ ,  $X_2=X^\star$ :

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \exp\Big(\frac12(f_0(X_{\mathrm{sim}})-f_0(X^\star))\Big) \le \exp\Big(\frac12 \, n\log\Big(\frac{m}{n}\Big)\Big).
$$

Compute:

$$
\exp\Big(\frac12 n\log(\tfrac{m}{n})\Big) = \Big(\exp(\log(\tfrac{m}{n}))\Big)^{n/2} = \Big(\frac{m}{n}\Big)^{n/2}.
$$

So we obtain the desired bound:

$$
\boxed{ \frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \;\le\; \Big(\frac{m}{n}\Big)^{n/2}. }
$$

* * *

If you want the “deeper why”: this is essentially saying the simple covariance-type ellipsoid is a dimension-dependent approximation to the Löwner–John ellipsoid, and the dual choice  $\lambda=t\mathbf 1$  is the cleanest possible certificate.

## Response:
Problem (restated cleanly)
--------------------------

You are given points  $a_1,\dots,a_m\in\mathbb{R}^n$  that **span**  $\mathbb{R}^n$ . Consider the centered ellipsoid

$$
\mathcal E(X):=\{x\in\mathbb{R}^n:\ x^T X x\le 1\},\qquad X\in\mathbb{S}_{++}^n,
$$

and the minimum-volume covering ellipsoid problem (center fixed at the origin):

$$
\begin{aligned} \min_{X\in\mathbb{S}_{++}^n}\quad & f_0(X):=\log\det(X^{-1})\\ \text{s.t.}\quad & a_i^T X a_i \le 1,\quad i=1,\dots,m. \end{aligned} \tag{P}
$$

(Recall:  $\mathrm{vol}(\mathcal E(X))\propto 1/\sqrt{\det X}$ , so minimizing volume is equivalent to minimizing  $\log\det(X^{-1})=-\log\det X$ .)

Define the “simple” candidate

$$
X_{\mathrm{sim}}:=\Big(\sum_{k=1}^m a_k a_k^T\Big)^{-1}.
$$

**(a)** Show  $X_{\mathrm{sim}}$  is feasible for (P), i.e.  $a_i^T X_{\mathrm{sim}} a_i\le 1$  for all  $i$ .

**(b)** The dual of (P) is given as

$$
\begin{aligned} \max_{\lambda\in\mathbb{R}^m}\quad & d(\lambda):=\log\det\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big)-\mathbf 1^T\lambda+n\\ \text{s.t.}\quad & \lambda\succeq 0,\qquad \sum_{i=1}^m \lambda_i a_i a_i^T \succ 0. \end{aligned} \tag{D}
$$

Using (D), show that the volume of  $\mathcal E(X_{\mathrm{sim}})$  is at most a factor  $(m/n)^{n/2}$  larger than the optimal ellipsoid volume.

* * *

Solution
========

Preliminaries: a key matrix and why it’s invertible
---------------------------------------------------

Define

$$
S := \sum_{k=1}^m a_k a_k^T \in \mathbb{S}^n.
$$

### Claim 0.1:  $S\succ 0$  (so  $S^{-1}$  exists)

Take any  $x\in\mathbb{R}^n$ . Compute the quadratic form:

$$
x^T S x = x^T\Big(\sum_{k=1}^m a_k a_k^T\Big)x = \sum_{k=1}^m x^T a_k a_k^T x = \sum_{k=1}^m (a_k^T x)^2.
$$

This is a sum of squares, hence  $\ge 0$ . If  $x^T S x=0$ , then  $(a_k^T x)^2=0$  for every  $k$ , i.e.  $a_k^T x=0$  for all  $k$ . That means  $x$  is orthogonal to  $\mathrm{span}\{a_1,\dots,a_m\}$ . Since the  $a_k$  span  $\mathbb{R}^n$ , the only vector orthogonal to all of  $\mathbb{R}^n$  is  $x=0$ . Therefore  $x^T S x>0$  for all  $x\neq 0$ , i.e.  $S\succ 0$ .

So  $S^{-1}$  exists and is positive definite.

Note that

$$
X_{\mathrm{sim}} = S^{-1}.
$$

* * *

Part (a): feasibility of  $X_{\mathrm{sim}}$ 
=============================================

We must show that for each  $i=1,\dots,m$ ,

$$
a_i^T X_{\mathrm{sim}} a_i = a_i^T S^{-1} a_i \le 1.
$$

Fix an index  $i$ . Consider the block matrix

$$
M_i := \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix}.
$$

Step (a1): prove  $M_i\succeq 0$ 
---------------------------------

We will show  $M_i$  is a sum of outer products, hence PSD.

Work in  $\mathbb{R}^{n+1}$ . Define lifted vectors:

*   For  $k\neq i$ ,
    $$
    \tilde a_k := \begin{bmatrix}a_k\\0\end{bmatrix},
    $$
*   For  $k=i$ ,
    $$
    \tilde a_i' := \begin{bmatrix}a_i\\1\end{bmatrix}.
    $$

Compute their outer products:

*   For  $k\neq i$ ,
    $$
    \tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0\\ 0 & 0 \end{bmatrix}\succeq 0,
    $$
*   For  $i$ ,
    $$
    \tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix}\succeq 0.
    $$

Now sum:

$$
\sum_{k\neq i}\tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_{k\neq i} a_k a_k^T + a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix} = \begin{bmatrix} \sum_{k=1}^m a_k a_k^T & a_i\\ a_i^T & 1 \end{bmatrix} = \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Each outer product is PSD, and sums of PSD matrices are PSD, hence

$$
M_i\succeq 0.
$$

(You can also verify directly: for  $z=[x;t]\in\mathbb{R}^{n+1}$ ,  
 $z^T M_i z = \sum_{k\neq i}(a_k^T x)^2 + (a_i^T x+t)^2\ge 0$ .)

Step (a2): apply the Schur complement to get  $a_i^T S^{-1} a_i\le 1$ 
----------------------------------------------------------------------

Since  $S\succ 0$ , the Schur complement theorem says:

$$
\begin{bmatrix} S & u\\ u^T & \alpha \end{bmatrix}\succeq 0 \quad\Longleftrightarrow\quad \alpha - u^T S^{-1}u \ge 0.
$$

Apply this with  $u=a_i$ ,  $\alpha=1$ . From  $M_i\succeq 0$  we obtain

$$
1 - a_i^T S^{-1} a_i \ge 0 \quad\Longrightarrow\quad a_i^T S^{-1} a_i \le 1.
$$

This holds for every  $i$ . Therefore

$$
a_i^T X_{\mathrm{sim}} a_i \le 1,\qquad i=1,\dots,m,
$$

so  $X_{\mathrm{sim}}$  is feasible.

$$
\boxed{\text{Part (a) proved.}}
$$

* * *

Part (b): dual lower bound  $\Rightarrow$  volume approximation factor
======================================================================

Let  $X^\star$  be optimal for (P), with optimal value

$$
p^\star := f_0(X^\star)=\min f_0(X).
$$

The dual objective is  $d(\lambda)$ . By **weak duality**:

$$
d(\lambda)\le p^\star\le f_0(X)\quad\text{for any dual-feasible }\lambda\text{ and primal-feasible }X.
$$

We will:

1.  evaluate  $f_0(X_{\mathrm{sim}})$ ,
2.  choose a simple dual-feasible  $\lambda$ ,
3.  optimize it to get the best lower bound on  $p^\star$ ,
4.  compare to get an objective gap bound,
5.  convert to a volume ratio bound.

* * *

Step (b1): compute  $f_0(X_{\mathrm{sim}})$ 
--------------------------------------------

Since  $X_{\mathrm{sim}}=S^{-1}$ , we have  $X_{\mathrm{sim}}^{-1}=S$ . Thus

$$
f_0(X_{\mathrm{sim}})=\log\det(X_{\mathrm{sim}}^{-1})=\log\det(S).
$$

* * *

Step (b2): choose a simple dual-feasible point  $\lambda=t\mathbf 1$ 
---------------------------------------------------------------------

Take

$$
\lambda_i = t\quad (i=1,\dots,m),\qquad t>0.
$$

Then

$$
\sum_{i=1}^m \lambda_i a_i a_i^T = \sum_{i=1}^m t\, a_i a_i^T = tS.
$$

Because  $S\succ 0$  and  $t>0$ , we have  $tS\succ 0$ . Also  $\lambda\succeq 0$ . Hence  $\lambda=t\mathbf 1$  is dual-feasible.

* * *

Step (b3): evaluate the dual objective at  $\lambda=t\mathbf 1$ 
----------------------------------------------------------------

$$
d(t):=d(t\mathbf 1) = \log\det(tS) - \mathbf 1^T(t\mathbf 1) + n = \log\det(tS) - mt + n.
$$

Use  $\det(tS)=t^n\det(S)$  for an  $n\times n$  matrix  $S$ . Taking logs:

$$
\log\det(tS)=\log(t^n\det(S))=n\log t + \log\det(S).
$$

Therefore

$$
d(t)=\log\det(S)+n\log t - mt + n.
$$

* * *

Step (b4): maximize over  $t>0$  to get the best bound
------------------------------------------------------

Only the term  $n\log t-mt$  depends on  $t$ . Define

$$
\psi(t):=n\log t - mt.
$$

Differentiate:

$$
\psi'(t)=\frac{n}{t}-m.
$$

Set  $\psi'(t)=0$ :

$$
\frac{n}{t}=m\quad\Longrightarrow\quad t^\star=\frac{n}{m}.
$$

Second derivative:

$$
\psi''(t)=-\frac{n}{t^2}<0,
$$

so  $t^\star$  is indeed the maximizer.

Plug  $t^\star$  into  $d(t)$ :

$$
\begin{aligned} d(t^\star) &=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-m\cdot\frac{n}{m}+n\\ &=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-n+n\\ &=\log\det(S)+n\log\Big(\frac{n}{m}\Big)\\ &=\log\det(S)-n\log\Big(\frac{m}{n}\Big). \end{aligned}
$$

Thus, by weak duality,

$$
p^\star \ge d(t^\star)=\log\det(S)-n\log\Big(\frac{m}{n}\Big).
$$

* * *

Step (b5): bound the primal objective gap of  $X_{\mathrm{sim}}$ 
-----------------------------------------------------------------

We know  $f_0(X_{\mathrm{sim}})=\log\det(S)$ . Therefore

$$
\begin{aligned} f_0(X_{\mathrm{sim}})-p^\star &\le \log\det(S)-\Big(\log\det(S)-n\log\Big(\frac{m}{n}\Big)\Big)\\ &=n\log\Big(\frac{m}{n}\Big). \end{aligned}
$$

So we have the explicit suboptimality bound

$$
\boxed{ f_0(X_{\mathrm{sim}})-f_0(X^\star)\le n\log\Big(\frac{m}{n}\Big). }
$$

* * *

Step (b6): convert objective gap into a volume ratio
----------------------------------------------------

Volume of  $\mathcal E(X)=\{x:x^T X x\le 1\}$  is

$$
\mathrm{vol}(\mathcal E(X)) = \mathrm{vol}(B_n)\,\det(X^{-1/2}) = \mathrm{vol}(B_n)\,\frac{1}{\sqrt{\det X}} = \mathrm{vol}(B_n)\,\exp\Big(\frac12\log\det(X^{-1})\Big) = C_n\,\exp\Big(\frac12 f_0(X)\Big),
$$

where  $C_n=\mathrm{vol}(B_n)$  depends only on  $n$ .

Hence for two matrices  $X_1,X_2$ ,

$$
\frac{\mathrm{vol}(\mathcal E(X_1))}{\mathrm{vol}(\mathcal E(X_2))} = \exp\Big(\frac12(f_0(X_1)-f_0(X_2))\Big).
$$

Apply  $X_1=X_{\mathrm{sim}}$ ,  $X_2=X^\star$ :

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \exp\Big(\frac12(f_0(X_{\mathrm{sim}})-f_0(X^\star))\Big) \le \exp\Big(\frac12\,n\log\Big(\frac{m}{n}\Big)\Big).
$$

Simplify:

$$
\exp\Big(\frac12\,n\log\Big(\frac{m}{n}\Big)\Big) = \Big(\exp(\log(m/n))\Big)^{n/2} = \Big(\frac{m}{n}\Big)^{n/2}.
$$

Therefore,

$$
\boxed{ \frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \le \Big(\frac{m}{n}\Big)^{n/2}. }
$$
 
$$
\boxed{\text{Part (b) proved.}}
$$

* * *

Final result (both parts)
=========================

*   (a)  $X_{\mathrm{sim}}=\big(\sum_{k=1}^m a_k a_k^T\big)^{-1}$  is **feasible**, i.e.  $a_i^T X_{\mathrm{sim}} a_i\le 1$  for all  $i$ .
*   (b) Its ellipsoid volume is within a guaranteed factor of optimal:
    
$$
\boxed{ \mathrm{vol}(\mathcal E(X_{\mathrm{sim}})) \le \Big(\frac{m}{n}\Big)^{n/2}\, \mathrm{vol}(\mathcal E(X^\star)). }
$$

That is the complete, rigorous solution.

## Response:
Got it. I’ll rewrite the full solution **much more slowly**, with the missing “glue” steps made explicit, and with the key lemmas (PSD via outer products, Schur complement, determinant scaling, weak duality → bounds, objective gap → volume ratio) **proved or at least derived cleanly**.

I’m going to keep the flow “newcomer-proof”: define every object, state what we need to show, then do it.

* * *

1) Problem setup, with the geometry made explicit
-------------------------------------------------

### 1.1 Ellipsoid parameterization

We consider ellipsoids centered at the origin written as

$$
\mathcal E(X)=\{x\in\mathbb R^n:\ x^T X x \le 1\}, \qquad X\in\mathbb S_{++}^n.
$$
*    $\mathbb S_{++}^n$  means:  $X$  is symmetric and **positive definite**.
*   Positive definite means  $x^T X x>0$  for all  $x\neq 0$ . This guarantees the set  $\{x: x^T X x\le 1\}$  is a bounded, “real” ellipsoid (not a cylinder or something unbounded).

### 1.2 Containment constraints

We are given points  $a_1,\dots,a_m\in\mathbb R^n$ . Requiring  $\mathcal E(X)$  to contain all of them is exactly:

$$
a_i\in\mathcal E(X)\quad\Longleftrightarrow\quad a_i^T X a_i\le 1,\qquad i=1,\dots,m.
$$

So the constraints are

$$
a_i^T X a_i \le 1\quad (i=1,\dots,m).
$$

### 1.3 Why the objective is  $\log\det(X^{-1})$ : volume

Key fact: the ellipsoid  $\mathcal E(X)$  is the image of the unit ball under the linear map  $X^{-1/2}$ :

*   Let  $u$  satisfy  $\|u\|_2\le 1$ .
*   Put  $x=X^{-1/2}u$ .
*   Then  $x^T X x = u^T X^{-1/2} X X^{-1/2} u = u^T u \le 1$ , so  $x\in\mathcal E(X)$ .
*   Conversely, any  $x\in \mathcal E(X)$  can be written as  $x=X^{-1/2}u$  with  $\|u\|_2\le 1$ .

Thus,

$$
\mathcal E(X)=X^{-1/2}(B),\quad B=\{u:\|u\|_2\le 1\}.
$$

Volume under a linear map  $A$  scales by  $|\det A|$ . Therefore

$$
\mathrm{vol}(\mathcal E(X))=\mathrm{vol}(X^{-1/2}B)=|\det(X^{-1/2})|\ \mathrm{vol}(B).
$$

Because  $X\succ 0$ ,  $\det(X^{-1/2})>0$ , so

$$
\mathrm{vol}(\mathcal E(X))=\det(X^{-1/2})\ \mathrm{vol}(B).
$$

Now  $\det(X^{-1/2})=(\det X)^{-1/2}$ . So

$$
\mathrm{vol}(\mathcal E(X))=\mathrm{vol}(B)\cdot \frac{1}{\sqrt{\det X}}.
$$

Taking logs (and ignoring constant  $\log\mathrm{vol}(B)$ ):

$$
\log \mathrm{vol}(\mathcal E(X)) = \text{const} - \frac12\log\det X = \text{const} + \frac12\log\det(X^{-1}).
$$

So minimizing volume is equivalent to minimizing  $\log\det(X^{-1})$ .

### 1.4 The primal optimization problem

$$
\begin{aligned} \min_{X\in\mathbb S_{++}^n}\quad & f_0(X)=\log\det(X^{-1})\\ \text{s.t.}\quad & a_i^T X a_i \le 1,\quad i=1,\dots,m. \end{aligned} \tag{P}
$$

* * *

2) Define the proposed simple solution
--------------------------------------

Define

$$
S := \sum_{k=1}^m a_k a_k^T,\qquad X_{\mathrm{sim}} := S^{-1}.
$$

Part (a) asks: prove  $X_{\mathrm{sim}}$  is feasible, i.e.

$$
a_i^T S^{-1} a_i \le 1\quad \forall i.
$$

Part (b) asks: using the dual, show the volume ratio bound

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \le \left(\frac{m}{n}\right)^{n/2}.
$$

* * *

Part (a) — Feasibility of  $X_{\mathrm{sim}}$ 
==============================================

A.1 First, show  $S$  is invertible (so  $S^{-1}$  exists)
----------------------------------------------------------

You’re given the crucial assumption: the points  $a_1,\dots,a_m$  **span**  $\mathbb R^n$ .

### Lemma A.1: If  $a_1,\dots,a_m$  span  $\mathbb R^n$ , then  $S=\sum a_k a_k^T$  is positive definite.

**Proof.** Take any nonzero  $x\in\mathbb R^n$ . Compute

$$
x^T S x = x^T\Big(\sum_{k=1}^m a_k a_k^T\Big)x = \sum_{k=1}^m x^T a_k a_k^T x = \sum_{k=1}^m (a_k^T x)^2.
$$

This is a sum of squares, so it’s  $\ge 0$ . It equals  $0$  iff each term is  $0$ , i.e. iff  $a_k^T x=0$  for all  $k$ . That means  $x$  is orthogonal to  $\mathrm{span}\{a_1,\dots,a_m\}$ . But the span is all of  $\mathbb R^n$ , so the only vector orthogonal to it is  $x=0$ , contradiction. Therefore  $x^T S x>0$  for all  $x\neq 0$ , which is exactly  $S\succ 0$ . ∎

So  $S^{-1}$  exists and  $X_{\mathrm{sim}}\in\mathbb S_{++}^n$ .

A.2 What we must prove
----------------------

Feasibility means:

$$
a_i^T X_{\mathrm{sim}} a_i \le 1 \quad\Longleftrightarrow\quad a_i^T S^{-1} a_i \le 1,\qquad i=1,\dots,m.
$$

Fix one index  $i$ . We will prove  $a_i^T S^{-1} a_i\le 1$ . Since  $i$  was arbitrary, it holds for all  $i$ .

A.3 Construct a block matrix that “contains” the inequality
-----------------------------------------------------------

Define

$$
M_i := \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix}.
$$

Plan:

1.  Prove  $M_i\succeq 0$ .
2.  Use Schur complement to deduce  $1-a_i^T S^{-1}a_i\ge 0$ .
3.  Conclude  $a_i^T S^{-1}a_i\le 1$ .

### Lemma A.2 (atomic PSD): For any vector  $v$ , the matrix  $v v^T$  is PSD.

**Proof.** For any  $z$ ,

$$
z^T (v v^T) z = (v^T z)^2 \ge 0.
$$

So  $vv^T\succeq 0$ . ∎

### Lemma A.3 (sums preserve PSD): If  $M_1\succeq 0$  and  $M_2\succeq 0$ , then  $M_1+M_2\succeq 0$ .

**Proof.** For any  $z$ ,

$$
z^T(M_1+M_2)z=z^T M_1 z + z^T M_2 z \ge 0+0=0.
$$

∎

A.4 Prove  $M_i\succeq 0$  by writing it as a sum of outer products
-------------------------------------------------------------------

We “lift” vectors to  $\mathbb R^{n+1}$ :

*   For each  $k\neq i$ , define
    $$
    \tilde a_k := \begin{bmatrix} a_k\\ 0\end{bmatrix}.
    $$
*   For  $i$ , define
    $$
    \tilde a_i' := \begin{bmatrix} a_i\\ 1\end{bmatrix}.
    $$

Compute outer products:

*   If  $k\neq i$ ,
    $$
    \tilde a_k \tilde a_k^T = \begin{bmatrix} a_k a_k^T & 0\\ 0 & 0 \end{bmatrix}.
    $$
*   For  $i$ ,
    $$
    \tilde a_i' \tilde a_i'^T = \begin{bmatrix} a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix}.
    $$

Now sum them:

$$
\sum_{k\neq i}\tilde a_k \tilde a_k^T + \tilde a_i' \tilde a_i'^T = \begin{bmatrix} \sum_{k\neq i} a_k a_k^T + a_i a_i^T & a_i\\ a_i^T & 1 \end{bmatrix} = \begin{bmatrix} \sum_{k=1}^m a_k a_k^T & a_i\\ a_i^T & 1 \end{bmatrix} = \begin{bmatrix} S & a_i\\ a_i^T & 1 \end{bmatrix} = M_i.
$$

Each outer product is PSD by Lemma A.2; their sum is PSD by Lemma A.3. Hence

$$
M_i\succeq 0.
$$

(If you prefer an even more “definition-only” check: for  $z=[x;t]$ ,  
 $z^T M_i z = \sum_{k\neq i}(a_k^T x)^2 + (a_i^T x+t)^2\ge 0$ . Same conclusion.)

A.5 Schur complement step (with the logic made explicit)
--------------------------------------------------------

We use a standard equivalence:

### Lemma A.4 (Schur complement, one direction we need)

If  $S\succ 0$  and

$$
\begin{bmatrix} S & u\\ u^T & \alpha \end{bmatrix}\succeq 0,
$$

then

$$
\alpha - u^T S^{-1} u \ge 0.
$$

**Proof (direct, not magic).** Let

$$
y := \begin{bmatrix} -S^{-1}u \\ 1\end{bmatrix}.
$$

Because the block matrix is PSD, we must have  $y^T M y\ge 0$ . Compute:

$$
My= \begin{bmatrix} S & u\\ u^T & \alpha \end{bmatrix} \begin{bmatrix} -S^{-1}u\\ 1 \end{bmatrix} = \begin{bmatrix} -S S^{-1}u + u\\ -u^T S^{-1}u + \alpha \end{bmatrix} = \begin{bmatrix} 0\\ \alpha-u^T S^{-1}u \end{bmatrix}.
$$

Then

$$
y^TMy = \begin{bmatrix} -S^{-1}u\\ 1 \end{bmatrix}^T \begin{bmatrix} 0\\ \alpha-u^T S^{-1}u \end{bmatrix} = \alpha-u^T S^{-1}u.
$$

Since  $y^TMy\ge 0$ , we get  $\alpha-u^T S^{-1}u\ge 0$ . ∎

Now apply Lemma A.4 to  $M_i$  with  $u=a_i$ ,  $\alpha=1$ . We already know:

*    $S\succ 0$  (Lemma A.1),
*    $M_i\succeq 0$  (A.4).

Thus:

$$
1 - a_i^T S^{-1} a_i \ge 0 \quad\Longrightarrow\quad a_i^T S^{-1} a_i \le 1.
$$

Since  $i$  was arbitrary, this holds for all  $i$ . Therefore  $X_{\mathrm{sim}}=S^{-1}$  satisfies all constraints and is feasible.

That finishes part (a).

* * *

Part (b) — Dual certificate → objective gap → volume ratio
==========================================================

You are given the dual:

$$
\begin{aligned} \max_{\lambda}\quad & d(\lambda):=\log\det\Big(\sum_{i=1}^m \lambda_i a_i a_i^T\Big)-\mathbf 1^T\lambda+n\\ \text{s.t.}\quad & \lambda\succeq 0,\qquad \sum_{i=1}^m \lambda_i a_i a_i^T \succ 0. \end{aligned} \tag{D}
$$

Let  $X^\star$  be primal-optimal and let

$$
p^\star := f_0(X^\star)=\min f_0(X).
$$

B.1 Weak duality: the inequality we’ll exploit
----------------------------------------------

**Weak duality says:** for any primal-feasible  $X$  and dual-feasible  $\lambda$ ,

$$
d(\lambda)\le p^\star \le f_0(X).
$$

We will plug in:

*    $X=X_{\mathrm{sim}}$  (we proved feasible),
*   a cleverly chosen feasible  $\lambda$ .

This will trap  $p^\star$  between two explicit numbers and bound the suboptimality of  $X_{\mathrm{sim}}$ .

B.2 Compute the primal objective at  $X_{\mathrm{sim}}$ 
--------------------------------------------------------

We have  $X_{\mathrm{sim}}=S^{-1}$ , so  $X_{\mathrm{sim}}^{-1}=S$ . Therefore:

$$
f_0(X_{\mathrm{sim}}) =\log\det(X_{\mathrm{sim}}^{-1}) =\log\det(S).
$$

B.3 Choose a very simple dual-feasible point:  $\lambda=t\mathbf 1$ 
--------------------------------------------------------------------

Let

$$
\lambda_i=t\quad\text{for all }i,\qquad t>0.
$$

Check feasibility:

*    $\lambda\succeq 0$  because  $t>0$ .
*    $\sum_{i=1}^m \lambda_i a_i a_i^T = t\sum_{i=1}^m a_i a_i^T = tS$ .  
    Since  $S\succ 0$ , we have  $tS\succ 0$ .

So  $\lambda=t\mathbf 1$  is dual-feasible for any  $t>0$ .

B.4 Evaluate the dual objective  $d(\lambda)$  at  $\lambda=t\mathbf 1$ 
------------------------------------------------------------------------

$$
d(t):=d(t\mathbf 1) = \log\det(tS)-\mathbf 1^T(t\mathbf 1)+n = \log\det(tS)-mt+n.
$$

Now we use a basic determinant identity:

### Lemma B.1 (determinant scaling)

For an  $n\times n$  matrix  $S$  and scalar  $t>0$ ,

$$
\det(tS)=t^n\det(S).
$$

**Reason:** scaling a matrix by  $t$  scales each eigenvalue by  $t$ ; determinant is the product of eigenvalues; there are  $n$  eigenvalues; hence factor  $t^n$ .

Taking logs:

$$
\log\det(tS)=\log(t^n\det S)=n\log t+\log\det S.
$$

So

$$
d(t)=\log\det(S)+n\log t - mt + n.
$$

B.5 Optimize over  $t>0$  to get the strongest lower bound
----------------------------------------------------------

Because  $d(t)\le p^\star$ , we want  $d(t)$  as large as possible. So maximize  $d(t)$ .

The only  $t$ \-dependent part is

$$
\psi(t)=n\log t - mt.
$$

Differentiate:

$$
\psi'(t)=\frac{n}{t}-m.
$$

Set  $\psi'(t)=0$ :

$$
\frac{n}{t}=m\quad\Rightarrow\quad t^\star=\frac{n}{m}.
$$

Second derivative:

$$
\psi''(t)=-\frac{n}{t^2}<0,
$$

so this is indeed the maximizer.

Now plug  $t^\star$  into  $d(t)$ :

$$
d(t^\star)=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-m\cdot\frac{n}{m}+n.
$$

Compute the linear term:

$$
m\cdot\frac{n}{m}=n.
$$

So

$$
d(t^\star)=\log\det(S)+n\log\Big(\frac{n}{m}\Big)-n+n =\log\det(S)+n\log\Big(\frac{n}{m}\Big).
$$

Rewrite as

$$
n\log\Big(\frac{n}{m}\Big)=-n\log\Big(\frac{m}{n}\Big),
$$

so

$$
d(t^\star)=\log\det(S)-n\log\Big(\frac{m}{n}\Big).
$$

B.6 Use weak duality to bound the primal optimal value
------------------------------------------------------

Weak duality gives:

$$
p^\star \ge d(t^\star)=\log\det(S)-n\log\Big(\frac{m}{n}\Big).
$$

But we computed:

$$
f_0(X_{\mathrm{sim}})=\log\det(S).
$$

So the objective gap satisfies:

$$
\begin{aligned} f_0(X_{\mathrm{sim}})-p^\star &\le \log\det(S) - \Big(\log\det(S)-n\log(\tfrac{m}{n})\Big)\\ &=n\log\Big(\frac{m}{n}\Big). \end{aligned}
$$

Since  $p^\star=f_0(X^\star)$ , we have

$$
\boxed{ f_0(X_{\mathrm{sim}})-f_0(X^\star)\le n\log\Big(\frac{m}{n}\Big). }
$$

That’s the “log-det suboptimality” bound.

B.7 Convert objective gap into a volume ratio bound
---------------------------------------------------

Recall the volume formula:

$$
\mathrm{vol}(\mathcal E(X)) =\mathrm{vol}(B)\cdot \det(X^{-1/2}) =\mathrm{vol}(B)\cdot \exp\Big(\tfrac12 \log\det(X^{-1})\Big) =\mathrm{vol}(B)\cdot \exp\Big(\tfrac12 f_0(X)\Big).
$$

Let  $C_n:=\mathrm{vol}(B)$  (constant in  $X$ ). Then:

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} = \frac{C_n e^{\frac12 f_0(X_{\mathrm{sim}})}}{C_n e^{\frac12 f_0(X^\star)}} = \exp\Big(\frac12(f_0(X_{\mathrm{sim}})-f_0(X^\star))\Big).
$$

Use the bound from B.6:

$$
\frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \le \exp\Big(\frac12\, n\log\Big(\frac{m}{n}\Big)\Big).
$$

Finally simplify the exponential-log:

$$
\exp\Big(\frac12\, n\log(\tfrac{m}{n})\Big) = \Big(\exp(\log(\tfrac{m}{n}))\Big)^{n/2} = \Big(\frac{m}{n}\Big)^{n/2}.
$$

So we conclude:

$$
\boxed{ \frac{\mathrm{vol}(\mathcal E(X_{\mathrm{sim}}))}{\mathrm{vol}(\mathcal E(X^\star))} \le \Big(\frac{m}{n}\Big)^{n/2}. }
$$

That completes part (b).

* * *

Final combined conclusion
-------------------------

Define  $S=\sum_{k=1}^m a_k a_k^T$  and  $X_{\mathrm{sim}}=S^{-1}$ .

1.  **Feasibility:** for every  $i$ ,
    
$$
a_i^T X_{\mathrm{sim}} a_i = a_i^T S^{-1} a_i \le 1.
$$
2.  **Approximation guarantee (volume):**
    
$$
\mathrm{vol}(\mathcal E(X_{\mathrm{sim}})) \le \Big(\frac{m}{n}\Big)^{n/2}\, \mathrm{vol}(\mathcal E(X^\star)).
$$

* * *

If you want to go even deeper, the next “upgrade” is to connect this to the KKT conditions of (P)/(D): at the optimum,  $\lambda_i$  live on the boundary points (“contact points”), and the identity  $\sum \lambda_i a_i a_i^T = X^{\star -1}$  emerges. That explains why choosing uniform  $\lambda$  gives a crude but universal bound.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)