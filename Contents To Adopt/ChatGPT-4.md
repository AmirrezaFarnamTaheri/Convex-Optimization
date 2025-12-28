# 4

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/21/2025 1:54:55  
**Updated:** 12/22/2025 1:48:46  
**Exported:** 12/29/2025 0:03:28  
**Link:** [https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/69472235-a384-8326-9bf1-89b7b3aa1a17](https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/69472235-a384-8326-9bf1-89b7b3aa1a17)  

## Response:
Thought for 8s

Exercise 4.25 — Separating two **unions of ellipsoids** via an **SOCP feasibility** model (zero-to-hero, no gaps)
-----------------------------------------------------------------------------------------------------------------

We’re given ellipsoids in  $\mathbb R^n$ :

$$
\mathcal E_i=\{\,P_i u+q_i \mid \|u\|_2\le 1\,\},\qquad i=1,\dots,K+L,
$$

and we want a hyperplane  $a^T x+b=0$  that **strictly separates**

$$
\bigcup_{i=1}^K \mathcal E_i \quad\text{from}\quad \bigcup_{i=K+1}^{K+L} \mathcal E_i,
$$

i.e.

$$
a^Tx+b>0 \ \ \forall x\in\bigcup_{i=1}^K\mathcal E_i, \qquad a^Tx+b<0 \ \ \forall x\in\bigcup_{i=K+1}^{K+L}\mathcal E_i.
$$

Your task: express existence of such  $(a,b)$  as an **SOCP feasibility** problem.

(Conceptually, this is “separation + robust constraints over ellipsoids”, which is exactly the geometry toolkit you’ve been building.

Main Lecture 03

)

* * *

0) Two tiny sanity points (so we don’t step on landmines)
=========================================================

### (i) “Union separation” is just “separate each member”

The condition

$$
a^Tx+b>0\ \forall x\in\bigcup_{i=1}^K\mathcal E_i
$$

is **equivalent** to

$$
a^Tx+b>0\ \forall x\in\mathcal E_i\quad\text{for every }i=1,\dots,K,
$$

because “for all  $x$  in a union” means “for all  $x$  in each piece”.

Same for the negative side.

So we can treat ellipsoids one by one.

### (ii) You do _not_ really need  $P_i$  symmetric

The parametrization  $\mathcal E_i=\{P_iu+q_i:\|u\|\le 1\}$  covers (possibly degenerate) ellipsoids. In all computations below, the only thing that ever appears is  $P_i^T a$ . So symmetry doesn’t matter for modeling; it’s just a common convention.

* * *

1) Reduce “ $\forall x\in\mathcal E_i$ ” to a worst-case inequality over a ball
===============================================================================

Fix an index  $i$ . Any  $x\in\mathcal E_i$  has the form  $x=P_iu+q_i$  with  $\|u\|_2\le 1$ .

Evaluate the affine function  $x\mapsto a^Tx+b$  on such  $x$ :

$$
a^T x+b = a^T(P_i u+q_i)+b = (P_i^Ta)^T u + (a^Tq_i+b).
$$

Now:

*   To enforce  $a^Tx+b>0$  for **all**  $x\in\mathcal E_i$ , we need the **minimum** over allowable  $u$  to be positive:
    $$
    \min_{\|u\|_2\le 1}\Big((P_i^Ta)^T u + (a^Tq_i+b)\Big) \ >\ 0.
    $$
*   To enforce  $a^Tx+b<0$  for **all**  $x\in\mathcal E_i$ , we need the **maximum** to be negative:
    $$
    \max_{\|u\|_2\le 1}\Big((P_i^Ta)^T u + (a^Tq_i+b)\Big) \ <\ 0.
    $$

So everything reduces to: **maximize/minimize a linear form  $c^Tu$  over the Euclidean unit ball**.

* * *

2) Key lemma: extremum of a linear function over a Euclidean ball
=================================================================

Let  $c\in\mathbb R^n$ . Then

$$
\max_{\|u\|_2\le 1} c^T u = \|c\|_2,\qquad \min_{\|u\|_2\le 1} c^T u = -\|c\|_2.
$$

### Proof (no magic, just Cauchy–Schwarz + tightness)

For any  $\|u\|_2\le 1$ ,

$$
c^Tu \le \|c\|_2\|u\|_2 \le \|c\|_2
$$

by Cauchy–Schwarz. So the maximum is at most  $\|c\|_2$ .

If  $c\neq 0$ , choose  $u^\star = c/\|c\|_2$ . Then  $\|u^\star\|_2=1$  and

$$
c^T u^\star = c^T\frac{c}{\|c\|_2}=\frac{\|c\|_2^2}{\|c\|_2}=\|c\|_2,
$$

so the upper bound is achieved and is the true maximum.

Similarly, choosing  $u^\star=-c/\|c\|_2$  achieves  $-\|c\|_2$ , giving the minimum.

If  $c=0$ , both max and min are  $0$ , consistent with the formulas.

✅ Lemma proven.

Now apply it with  $c=P_i^T a$ .

* * *

3) Turn each “for all points in ellipsoid” condition into a single norm inequality
==================================================================================

3.1) Ellipsoids that must lie on the “positive” side ( $i=1,\dots,K$ )
----------------------------------------------------------------------

We need:

$$
\min_{\|u\|\le 1}\Big((P_i^Ta)^T u + (a^Tq_i+b)\Big) > 0.
$$

Split the constant term:

$$
\min_{\|u\|\le 1} (P_i^Ta)^T u + (a^Tq_i+b) > 0
$$

(because  $(a^Tq_i+b)$  doesn’t depend on  $u$ ).

By the lemma:

$$
\min_{\|u\|\le 1}(P_i^Ta)^T u = -\|P_i^Ta\|_2.
$$

So the condition becomes:

$$
-\|P_i^Ta\|_2 + (a^Tq_i+b) > 0 \quad\Longleftrightarrow\quad a^Tq_i+b > \|P_i^Ta\|_2.
$$

That’s already “SOC-shaped”: norm on one side, affine on the other.

3.2) Ellipsoids that must lie on the “negative” side ( $i=K+1,\dots,K+L$ )
--------------------------------------------------------------------------

We need:

$$
\max_{\|u\|\le 1}\Big((P_i^Ta)^T u + (a^Tq_i+b)\Big) < 0.
$$

Again split the constant:

$$
\max_{\|u\|\le 1}(P_i^Ta)^T u + (a^Tq_i+b) < 0.
$$

By the lemma:

$$
\max_{\|u\|\le 1}(P_i^Ta)^T u = \|P_i^Ta\|_2.
$$

So:

$$
\|P_i^Ta\|_2 + (a^Tq_i+b) < 0 \quad\Longleftrightarrow\quad -(a^Tq_i+b) > \|P_i^Ta\|_2.
$$

So strict separation is equivalent to the system:

$$
a^Tq_i+b > \|P_i^Ta\|_2\quad (i\le K),\qquad -(a^Tq_i+b) > \|P_i^Ta\|_2\quad (i>K).
$$

At this point, we have strict inequalities “ $>$ ”. SOCP solvers prefer “ $\le$ ” and non-strict constraints. Next step fixes that cleanly.

* * *

4) Remove strictness correctly (the scaling + margin argument)
==============================================================

This is the subtle step people handwave. Let’s do it properly.

4.1) The separation inequalities are homogeneous in  $(a,b)$ 
-------------------------------------------------------------

If  $(a,b)$  satisfies strict separation, then for any  $\gamma>0$ ,

$$
(\tilde a,\tilde b) := (\gamma a,\gamma b)
$$

also satisfies strict separation, because

$$
\tilde a^T x+\tilde b = \gamma(a^T x+b),
$$

and multiplying by a positive scalar preserves “ $>\,0$ ” and “ $<\,0$ ”.

So we can scale the separator freely.

4.2) Strictness + compactness ⇒ there is a positive margin
----------------------------------------------------------

Each ellipsoid  $\mathcal E_i$  is compact (image of the compact ball  $\{u:\|u\|\le1\}$  under an affine map). A continuous function on a compact set attains its min and max.

Define for  $i\le K$ :

$$
m_i := \min_{x\in\mathcal E_i}(a^Tx+b).
$$

Strict separation gives  $m_i>0$ . Because the min is attained,  $m_i$  is a real positive number.

For  $i>K$ , define

$$
m_i := \min_{x\in\mathcal E_i} (-(a^Tx+b)) = -\max_{x\in\mathcal E_i}(a^Tx+b).
$$

Strict separation gives  $\max_{x\in\mathcal E_i}(a^Tx+b)<0$ , hence  $m_i>0$ .

Now take the minimum over finitely many ellipsoids:

$$
m := \min_{i=1,\dots,K+L} m_i.
$$

Since there are finitely many positive numbers,  $m>0$ .

This  $m$  is the **global strict margin**: every “positive” ellipsoid lies at least  $m$  above the hyperplane, and every “negative” ellipsoid lies at least  $m$  below it (in signed distance units of  $a^Tx+b$ , not Euclidean distance).

4.3) Use scaling to normalize the margin to 1
---------------------------------------------

If  $m>0$ , choose  $\gamma = 1/m$ . Then for the scaled  $(\tilde a,\tilde b)$ ,  
all margins become  $\ge 1$ .

Concretely, the strict constraints

$$
a^Tq_i+b - \|P_i^Ta\|_2 > 0
$$

become

$$
\tilde a^Tq_i+\tilde b - \|P_i^T\tilde a\|_2 \ge 1,
$$

and similarly on the other side.

So: **existence of a strict separator** is equivalent to feasibility of the **non-strict, margin-1** system:

$$
a^Tq_i+b - \|P_i^Ta\|_2 \ge 1\quad (i\le K),
$$
 
$$
-(a^Tq_i+b) - \|P_i^Ta\|_2 \ge 1\quad (i>K).
$$

(You could pick any positive constant instead of  $1$ . Picking  $1$  just fixes scale.)

* * *

5) Put it in clean SOCP form (norm ≤ affine)
============================================

Rewrite each inequality as “norm ≤ affine RHS”.

For  $i=1,\dots,K$ :
--------------------

$$
a^Tq_i+b - \|P_i^Ta\|_2 \ge 1 \quad\Longleftrightarrow\quad \|P_i^Ta\|_2 \le a^Tq_i+b-1.
$$

For  $i=K+1,\dots,K+L$ :
------------------------

$$
-(a^Tq_i+b) - \|P_i^Ta\|_2 \ge 1 \quad\Longleftrightarrow\quad \|P_i^Ta\|_2 \le -a^Tq_i-b-1.
$$

That’s it.

Each constraint has the standard SOC pattern

$$
\|A z + r\|_2 \le c^T z + d
$$

with decision vector  $z=(a,b)$ .

No objective needed: it’s a **feasibility** problem.

* * *

6) Final answer: SOCP feasibility model
=======================================

**Variables:**  $a\in\mathbb R^n$ ,  $b\in\mathbb R$ .

**Feasibility constraints:**

$$
\boxed{ \begin{aligned} \|P_i^T a\|_2 &\le a^T q_i + b - 1, && i=1,\dots,K,\\[2mm] \|P_i^T a\|_2 &\le -a^T q_i - b - 1, && i=K+1,\dots,K+L. \end{aligned}}
$$

If feasible, any feasible  $(a,b)$  gives a strictly separating hyperplane  $a^Tx+b=0$  (with normalized margin 1). If infeasible, no strict separator exists.

* * *

7) Tiny “expert checks” (these are the usual grading traps)
===========================================================

1.  **RHS must be nonnegative automatically.**  
    SOC constraints  $\|v\|_2 \le t$  force  $t\ge 0$ . So if some RHS is negative, the constraint becomes impossible, which is exactly what you want.
2.  **Degenerate ellipsoid  $P_i$  rank-deficient is fine.**  
    Then  $\mathcal E_i$  is a lower-dimensional ellipsoid (a “flat pancake”). The formula still holds because the support function of  $P_i$ ball is still  $\|P_i^Ta\|_2$ .
3.  **Why not just keep strict inequalities?**  
    Because convex solvers require closed feasible sets; strict constraints are open. The margin-normalization is the standard way to convert “strict separation exists” into a closed feasibility set.
4.  **Alternative viewpoint (support function) in one line.**  
    For any compact convex set  $C$ ,  $\max_{x\in C} a^Tx = \sigma_C(a)$  (support function). For ellipsoid  $P\mathbb B_2 + q$ ,
    
$$
\sigma_{\mathcal E}(a)=a^Tq+\|P^Ta\|_2.
$$

Then the “negative side” condition is  $\sigma_{\mathcal E_i}(a)+b<0$ , etc. Same result, just more “convex analysis-y”.

* * *

If you keep going after 4.25, the next “pattern” is exactly 4.26: converting quadratic-over-linear / products into rotated SOC, which is the other main modeling primitive in this cluster.

## Response:
Thought for 21s

Exercise 4.26 — “Hyperbolic” constraints as **rotated SOC** constraints (deep, step-by-step)
--------------------------------------------------------------------------------------------

This exercise is the modeling atom behind a ton of SOCP reformulations: anything that looks like a **product**  $xy$  bounding a **square**  $w^2$  (or a norm squared  $\|w\|_2^2$ ) becomes a **rotated second-order cone** constraint.

I’ll build it from scratch, including the annoying constant factors that trip people in quizzes.

* * *

1) The two cones you must not confuse
=====================================

1.1 Standard second-order cone (SOC, Lorentz cone)
--------------------------------------------------

For  $z\in\mathbb R^n$ ,  $t\in\mathbb R$ :

$$
\mathcal Q^{n+1} \;=\; \{(t,z): \|z\|_2 \le t\}.
$$

This is the “ice-cream cone”. Constraint form:

$$
\| \text{affine}(x)\|_2 \le \text{affine}(x).
$$

1.2 Rotated second-order cone (RSOC)
------------------------------------

There are **two equivalent conventions** floating around. Be consistent with whichever your book/solver uses.

**Convention A (BV/very common):**

$$
\mathcal Q_r^{n+2} = \{(u,v,w)\in\mathbb R\times\mathbb R\times\mathbb R^n:\ u\ge 0,\ v\ge 0,\ 2uv \ge \|w\|_2^2\}.
$$

**Convention B (no factor 2):**

$$
\tilde{\mathcal Q}_r^{n+2} = \{(u,v,w): u\ge0,\ v\ge0,\ uv \ge \|w\|_2^2\}.
$$

These are the same cone up to scaling  $w$  by  $\sqrt{2}$ . So don’t panic: constants are bookkeeping.

* * *

2) The “hyperbolic constraint” you want to encode
=================================================

The prototype is:

### Scalar version

$$
x\ge 0,\quad y\ge 0,\quad w^2 \le xy.
$$

### Vector version (more general, same idea)

$$
x\ge 0,\quad y\ge 0,\quad \|w\|_2^2 \le xy.
$$

This set is convex (it’s the epigraph of a quadratic-over-linear, or the RSOC slice), but it’s not in “ $\| \cdot \| \le \cdot$ ” form until we do the trick.

* * *

3) Direct RSOC representation (the cleanest statement)
======================================================

Using Convention A ( $2uv\ge \|w\|^2$ ):

### 3.1 Scalar hyperbola

We want  $w^2 \le xy$ . Compare with  $2uv \ge \|w\|^2$ .

If we set  $u=x$ ,  $v=y$ , then RSOC gives  $2xy \ge w^2$ , i.e.  $w^2 \le 2xy$ . That’s off by a factor  $2$ .

Fix it by scaling the “ $w$ ” entry:

$$
2xy \ge (\sqrt{2}\,w)^2 = 2w^2 \quad\Longleftrightarrow\quad xy \ge w^2.
$$

So the **exact** encoding is:

$$
\boxed{ x\ge 0,\ y\ge 0,\ w^2 \le xy \quad\Longleftrightarrow\quad (x,\ y,\ \sqrt{2}\,w)\in \mathcal Q_r^{3}. }
$$

### 3.2 Vector version

Same logic:

$$
\|w\|_2^2 \le xy \quad\Longleftrightarrow\quad \|\sqrt{2}\,w\|_2^2 \le 2xy \quad\Longleftrightarrow\quad (x,\ y,\ \sqrt{2}\,w)\in \mathcal Q_r^{n+2}.
$$

So:

$$
\boxed{ x\ge0,\ y\ge0,\ \|w\|_2^2 \le xy \quad\Longleftrightarrow\quad (x,\ y,\ \sqrt{2}\,w)\in \mathcal Q_r^{n+2}. }
$$

If your solver uses Convention B ( $uv\ge\|w\|^2$ ), then it’s even simpler:

$$
(x,y,w)\in \tilde{\mathcal Q}_r^{n+2}.
$$

* * *

4) Why this is convex (and why RSOC is “right”)
===============================================

A useful mental model: the constraint  $\|w\|_2^2 \le xy$  with  $x,y\ge 0$  describes a **convex cone** because if you scale  $(x,y,w)$  by  $\alpha>0$ , the inequality scales correctly:

$$
\| \alpha w\|^2 = \alpha^2\|w\|^2 \le \alpha^2 xy = (\alpha x)(\alpha y).
$$

So it’s a cone, and it’s actually exactly the rotated cone (up to scaling conventions). RSOC is _the_ canonical cone for “product dominates square”.

* * *

5) Equivalence to a standard SOC (optional but very exam-useful)
================================================================

Some solvers only talk about “SOC”, not “rotated SOC”. There’s a standard algebraic equivalence:

Start from Convention B for simplicity:

$$
uv \ge \|w\|^2,\ u\ge0,\ v\ge0.
$$

Define:

$$
t = u+v,\qquad s = u-v.
$$

Then note the identity:

$$
t^2 - s^2 = (u+v)^2 - (u-v)^2 = 4uv.
$$

Now consider the SOC constraint:

$$
\| (s,\ 2w)\|_2 \le t.
$$

Square both sides:

$$
s^2 + 4\|w\|^2 \le t^2 \quad\Longleftrightarrow\quad 4\|w\|^2 \le t^2 - s^2 = 4uv \quad\Longleftrightarrow\quad \|w\|^2 \le uv.
$$

So we have the exact equivalence:

$$
\boxed{ u\ge0,\ v\ge0,\ uv \ge \|w\|^2 \quad\Longleftrightarrow\quad \|(u-v,\ 2w)\|_2 \le u+v. }
$$

If you’re using Convention A ( $2uv\ge\|w\|^2$ ), the same derivation gives:

$$
\|(u-v,\ \sqrt{2}\,w)\|_2 \le u+v.
$$

This is a very practical “convert RSOC → SOC” identity.

* * *

6) The quadratic-over-linear form (the version you actually use in 4.27)
========================================================================

This is the real workhorse:

### Goal

Represent

$$
\frac{\|w\|_2^2}{x} \le t,\qquad x\ge 0.
$$

### Step 1: clear the denominator (carefully)

For  $x>0$ , this is equivalent to

$$
\|w\|_2^2 \le x t.
$$

To keep it convex and well-defined at  $x=0$ , we impose also  $t\ge 0$ , and interpret it as:

*   if  $x=0$ , then  $\|w\|^2 \le 0\Rightarrow w=0$  (otherwise infeasible),
*   if  $x>0$ , it’s the usual inequality.

So the proper closed constraint set is:

$$
x\ge 0,\ t\ge 0,\ \|w\|_2^2 \le xt.
$$

### Step 2: encode as RSOC

Using Convention A:

$$
\|w\|_2^2 \le xt \quad\Longleftrightarrow\quad \|\sqrt{2}\,w\|_2^2 \le 2xt \quad\Longleftrightarrow\quad (x,\ t,\ \sqrt{2}\,w)\in\mathcal Q_r^{n+2}.
$$

So:

$$
\boxed{ \frac{\|w\|_2^2}{x} \le t,\ x\ge0 \quad\Longleftrightarrow\quad x\ge0,\ t\ge0,\ (x,\ t,\ \sqrt{2}\,w)\in\mathcal Q_r^{n+2}. }
$$

Scalar version: replace  $\|w\|_2^2$  by  $w^2$ .

* * *

7) “Solver-ready” patterns you should memorize (quiz mode)
==========================================================

1.  **Product dominates square**
    
$$
w^2 \le xy,\ x\ge0,\ y\ge0 \;\;\Longleftrightarrow\;\; (x,y,\sqrt{2}w)\in \mathcal Q_r^{3}.
$$
2.  **Product dominates norm squared**
    
$$
\|w\|_2^2 \le xy,\ x\ge0,\ y\ge0 \;\;\Longleftrightarrow\;\; (x,y,\sqrt{2}w)\in \mathcal Q_r^{n+2}.
$$
3.  **Quadratic-over-linear**
    
$$
\frac{\|w\|_2^2}{x} \le t,\ x\ge0 \;\;\Longleftrightarrow\;\; (x,t,\sqrt{2}w)\in \mathcal Q_r^{n+2},\ x\ge0,\ t\ge0.
$$
4.  **RSOC → SOC conversion**
    
$$
uv \ge \|w\|^2,\ u,v\ge0 \;\;\Longleftrightarrow\;\; \|(u-v,2w)\|_2 \le u+v.
$$

* * *

That’s 4.26 completely: it’s the cone identity that lets you turn “multiply two nonnegatives to bound a square” into a conic constraint.

Next, 4.27 is basically: “explode an inverse quadratic form into  $\|v\|^2 + \sum w_i^2/x_i$ ” and then apply this atom  $n$  times.

## Response:
Thought for 31s

Exercise 4.27 — Matrix fractional minimization as an SOCP (full derivation, no handwaving)
------------------------------------------------------------------------------------------

### 0) Problem statement, cleaned and dimension-checked

Given  $A\in\mathbb R^{m\times n}$ ,  $b\in\mathbb R^m$ ,  $B\in\mathbb R^{m\times n}$ , solve

$$
\min_{x\succeq 0}\quad (Ax+b)^T\Big(I + B\,\mathrm{diag}(x)\,B^T\Big)^{-1}(Ax+b).
$$

Define, for a given  $x$ :

*    $D := \mathrm{diag}(x)\in\mathbb R^{n\times n}$  (diagonal),
*    $y := Ax+b\in\mathbb R^m$ ,
*    $M := I + B D B^T\in\mathbb S^m$ .

If  $x\succeq 0$ , then  $D\succeq 0$  and  $BD B^T\succeq 0$ , hence  $M = I + BD B^T \succeq I \succ 0$ . So  $M^{-1}$  exists and the objective is well-defined for every feasible  $x$ .

Goal: rewrite the whole thing as an SOCP (specifically using rotated SOCs).

* * *

1) The key identity (what you “wish” the inverse quadratic form were)
---------------------------------------------------------------------

For fixed  $x$  (so fixed  $D$  and  $M$ ), we claim:

$$
\boxed{ y^T(I+BD B^T)^{-1}y = \min_{v\in\mathbb R^m,\;w\in\mathbb R^n}\Big\{\|v\|_2^2 + w^T D^{-1}w \ \ \text{s.t.}\ \ v + Bw = y\Big\}. }
$$

This is the heart of the exercise. Once you have it, the rest is purely “modeling gymnastics” with rotated SOCs.

Two things to be careful about right now:

1.   $D^{-1}$  is a problem if some  $x_i=0$ . The correct interpretation is **extended-value**:
    
$$
w^T D^{-1} w = \sum_{i=1}^n \frac{w_i^2}{x_i},
$$

where  $\frac{w_i^2}{0}$  is understood as:

*    $0$  if  $w_i=0$ ,
*    $+\infty$  if  $w_i\neq 0$ .

Equivalently: when  $x_i=0$ , you must enforce  $w_i=0$ .

2.  This identity is true for all  $x\succeq 0$  (including zeros), if interpreted that way.

Now I’ll prove it cleanly.

* * *

2) Proof of the identity (via Lagrange duality, step by step)
-------------------------------------------------------------

Fix  $x\succeq 0$ , hence  $D=\mathrm{diag}(x)$  and  $M=I+BD B^T \succ 0$ . Consider the optimization problem

$$
\min_{v,w}\ \ \|v\|_2^2 + w^T D^{-1} w \quad\text{s.t.}\quad v + Bw = y.
$$

Call it  $(P_x)$ .

### 2.1 Lagrangian

Introduce a multiplier  $\lambda\in\mathbb R^m$  for the equality  $v+Bw=y$ . Write it as  $y - v - Bw = 0$ . The Lagrangian is

$$
\mathcal L(v,w,\lambda) = \|v\|_2^2 + w^T D^{-1}w + \lambda^T(y - v - Bw).
$$

We compute the dual function  $g(\lambda)=\inf_{v,w}\mathcal L(v,w,\lambda)$  by minimizing over  $v$  and  $w$  explicitly.

* * *

### 2.2 Minimize over  $v$ 

The  $v$ \-part is

$$
\|v\|_2^2 - \lambda^T v.
$$

This is a strictly convex quadratic in  $v$ . Take gradient and set to zero:

$$
\nabla_v(\|v\|_2^2 - \lambda^T v)= 2v - \lambda = 0 \quad\Rightarrow\quad v^\star = \lambda/2.
$$

Plug back to get the minimum value:

$$
\|v^\star\|_2^2 - \lambda^T v^\star = \|\lambda/2\|_2^2 - \lambda^T(\lambda/2) = \frac14\|\lambda\|_2^2 - \frac12\|\lambda\|_2^2 = -\frac14\|\lambda\|_2^2.
$$

So after minimizing out  $v$ , the Lagrangian becomes:

$$
\inf_v \mathcal L = -\frac14\|\lambda\|_2^2 + w^T D^{-1} w + \lambda^T y - \lambda^T B w.
$$

* * *

### 2.3 Minimize over  $w$ 

Now the  $w$ \-dependent part is

$$
w^T D^{-1} w - \lambda^T B w.
$$

This is also convex quadratic (extended-valued if some  $x_i=0$ , but still convex). Take gradient in the “regular” case  $x_i>0$  (so  $D\succ 0$ ) first:

$$
\nabla_w\big(w^T D^{-1} w - \lambda^T B w\big) = 2D^{-1}w - B^T\lambda.
$$

Set to zero:

$$
2D^{-1}w = B^T\lambda \quad\Rightarrow\quad w^\star = \frac12 D B^T\lambda.
$$

Plug back to compute the minimum value:

First term:

$$
(w^\star)^T D^{-1} w^\star = \left(\tfrac12 DB^T\lambda\right)^T D^{-1}\left(\tfrac12 DB^T\lambda\right) = \frac14 \lambda^T B D B^T \lambda.
$$

Second term:

$$
-\lambda^T B w^\star = -\lambda^T B \left(\tfrac12 DB^T\lambda\right) = -\frac12 \lambda^T B D B^T \lambda.
$$

So

$$
\inf_w \big(w^T D^{-1} w - \lambda^T B w\big) = \frac14 \lambda^T B D B^T \lambda - \frac12 \lambda^T B D B^T \lambda = -\frac14 \lambda^T B D B^T \lambda.
$$

If some  $x_i=0$ : the minimizer condition forces  $w_i^\star = \tfrac12 x_i (b_i^T\lambda)$ , so indeed  $w_i^\star=0$  when  $x_i=0$ . This matches the extended-value interpretation perfectly.

* * *

### 2.4 Dual function and dual problem

Combine the minimized pieces:

$$
g(\lambda) = \lambda^T y -\frac14\|\lambda\|_2^2 -\frac14 \lambda^T B D B^T \lambda = \lambda^T y - \frac14 \lambda^T(I + BD B^T)\lambda.
$$

But  $I+BD B^T = M$ . So:

$$
g(\lambda)=\lambda^T y - \frac14 \lambda^T M \lambda.
$$

The dual problem is

$$
\max_{\lambda\in\mathbb R^m}\ \ \lambda^T y - \frac14 \lambda^T M \lambda.
$$

This is a concave quadratic maximization. Complete the square:

Because  $M\succ 0$ ,

$$
\lambda^T y - \frac14 \lambda^T M\lambda = y^T M^{-1} y \;-\; \frac14(\lambda - 2M^{-1}y)^T M(\lambda - 2M^{-1}y).
$$

The second term is  $\le 0$ , with equality at  $\lambda^\star = 2M^{-1}y$ . Therefore the dual optimal value is exactly

$$
\max_\lambda g(\lambda) = y^T M^{-1} y.
$$

### 2.5 Why strong duality holds (so primal optimum = dual optimum)

The primal  $(P_x)$  is a convex problem with an affine equality constraint. For  $D\succ 0$  it is strictly feasible trivially (pick any  $w$ , set  $v=y-Bw$ ). For  $D\succeq 0$  with zeros, you can pick  $w$  with  $w_i=0$  whenever  $x_i=0$ , again making feasibility easy.

Hence strong duality applies (standard convex quadratic + affine constraints setting). Therefore the primal optimal value equals the dual optimal value:

$$
\min_{v,w:\ v+Bw=y}\Big(\|v\|^2 + w^T D^{-1}w\Big) = y^T M^{-1}y.
$$

That proves the identity.

* * *

3) Use the identity to rewrite the _original_ problem
-----------------------------------------------------

Substitute  $y=Ax+b$  and  $D=\mathrm{diag}(x)$ . Then the original problem is equivalent to:

$$
\min_{x\succeq 0,\;v,w}\quad \|v\|_2^2 + w^T\mathrm{diag}(x)^{-1}w \quad\text{s.t.}\quad v + Bw = Ax+b.
$$

Now we turn that into an SOCP by introducing epigraph variables for each quadratic-over-linear term.

* * *

4) Epigraph trick: replace nonlinear objective by linear objective + conic constraints
--------------------------------------------------------------------------------------

### 4.1 Split the objective into pieces

$$
\|v\|_2^2 + w^T\mathrm{diag}(x)^{-1}w = \|v\|_2^2 + \sum_{i=1}^n \frac{w_i^2}{x_i}.
$$

We will upper-bound each piece by a new variable and minimize the sum.

Introduce:

*    $s \in \mathbb R$  for  $\|v\|_2^2$ ,
*    $z\in\mathbb R^n$  with components  $z_i$  for  $\frac{w_i^2}{x_i}$ .

Impose:

$$
s \ge \|v\|_2^2, \qquad z_i \ge \frac{w_i^2}{x_i}\quad (i=1,\dots,n), \qquad x\succeq 0,\ z\succeq 0,\ s\ge 0.
$$

Then minimizing  $s+\sum_i z_i$  will force these inequalities to hold at equality at optimum (because objective penalizes them), so this epigraph formulation is equivalent.

So we aim for:

$$
\min\ s + \sum_{i=1}^n z_i \quad\text{s.t.}\quad v + Bw = Ax+b,\ \ x\succeq 0, \ \ s \ge \|v\|^2,\ \ z_i \ge w_i^2/x_i.
$$

Now: represent those last two as rotated SOC constraints (that’s exactly 4.26).

* * *

5) Convert  $z_i \ge w_i^2/x_i$  into rotated SOC constraints
-------------------------------------------------------------

Start from

$$
z_i \ge \frac{w_i^2}{x_i}.
$$

For  $x_i>0$ , equivalent to

$$
w_i^2 \le x_i z_i.
$$

For  $x_i=0$ , the correct closed interpretation is: must have  $w_i=0$  and then  $z_i$  can be  $0$  (and the objective will indeed drive it to  $0$ ). The conic form below enforces exactly that.

Use the rotated SOC (BV convention):

$$
\mathcal Q_r^{3}=\{(u,v,t): u\ge0,\ v\ge0,\ 2uv\ge t^2\}.
$$

To encode  $w_i^2 \le x_i z_i$ , write it as  $2x_i z_i \ge 2w_i^2$ , i.e.

$$
2x_i z_i \ge (\sqrt{2}\,w_i)^2.
$$

So the exact rotated SOC constraint is:

$$
\boxed{(x_i,\ z_i,\ \sqrt{2}\,w_i)\in \mathcal Q_r^{3}\qquad i=1,\dots,n.}
$$

This single constraint simultaneously enforces  $x_i\ge0$ ,  $z_i\ge0$ , and the product bound.

* * *

6) Convert  $s \ge \|v\|_2^2$  into a rotated SOC constraint
------------------------------------------------------------

We want:

$$
s \ge \|v\|_2^2.
$$

Using rotated SOC in  $\mathbb R^{m+2}$ :

$$
\mathcal Q_r^{m+2}=\{(u,v,w)\in\mathbb R\times\mathbb R\times\mathbb R^m:\ u\ge0,\ v\ge0,\ 2uv\ge \|w\|_2^2\}.
$$

Choose  $u=s$ , choose  $v=\frac12$ . Then  $2uv = 2s\cdot \frac12 = s$ . So

$$
2uv \ge \|w\|^2 \quad\Longleftrightarrow\quad s \ge \|v\|_2^2.
$$

Thus:

$$
\boxed{(s,\ 1/2,\ v)\in\mathcal Q_r^{m+2}.}
$$

This also forces  $s\ge 0$  automatically.

* * *

7) Final SOCP (rotated SOC form)
--------------------------------

**Variables**

$$
x\in\mathbb R^n,\quad v\in\mathbb R^m,\quad w\in\mathbb R^n,\quad z\in\mathbb R^n,\quad s\in\mathbb R.
$$

**SOCP**

$$
\boxed{ \begin{aligned} \min\quad & s + \sum_{i=1}^n z_i\\ \text{s.t.}\quad & v + B w = A x + b,\\ & (s,\ 1/2,\ v)\in \mathcal Q_r^{m+2},\\ & (x_i,\ z_i,\ \sqrt{2}\,w_i)\in \mathcal Q_r^{3},\qquad i=1,\dots,n. \end{aligned}}
$$

That is an SOCP because:

*   objective is linear,
*   constraints are affine equalities and rotated SOC constraints.

Feasible set is closed, and the “ $x_i=0$ ” edge case is handled correctly by the rotated cones (they force  $w_i=0$ ).

* * *

8) Sanity checks (the stuff graders love)
-----------------------------------------

1.  **Dimensions:**  
     $v\in\mathbb R^m$ ,  $Bw\in\mathbb R^m$ ,  $Ax+b\in\mathbb R^m$ . OK.
2.  **Edge case  $x_i=0$ :**  
     $(x_i,z_i,\sqrt2 w_i)\in Q_r^3$  with  $x_i=0$  implies  $0\cdot z_i \ge w_i^2\Rightarrow w_i=0$ . Exactly what the extended-value  $w_i^2/x_i$  means.
3.  **Why minimizing  $s+\sum z_i$  is equivalent:**  
    At optimum, you’ll always tighten to  $s=\|v\|^2$  and  $z_i=w_i^2/x_i$  (when  $x_i>0$ ), because any slack increases the objective and doesn’t help feasibility.
4.  **If your solver only supports _standard_ SOC, not rotated:**  
    There’s a standard conversion:
    
$$
(u,v,w)\in Q_r \iff \|(u-v,\ 2w)\|_2 \le u+v
$$

(up to the same factor conventions). So you can rewrite each rotated cone as an ordinary SOC if needed.

* * *

If you want the “quiz speedrun” version of 4.27: the only two patterns to remember are  
(1) inverse quadratic form    $\;y^T(I+BD B^T)^{-1}y\;$  becomes  $\min \|v\|^2+\sum w_i^2/x_i$  with  $v+Bw=y$ , and  
(2) each  $w_i^2\le x_i z_i$  is rotated SOC.

## Response:
Thought for 23s

Exercise 4.38 — One-variable SDP and generalized eigenvalues (fully unpacked)
-----------------------------------------------------------------------------

You’re given symmetric matrices  $A,B\in\mathbb S^n$ , with  $B$  **nonsingular**, and you’re told there exists a nonsingular matrix  $R$  such that

$$
R^T A R=\operatorname{diag}(a_1,\dots,a_n),\qquad R^T B R=\operatorname{diag}(b_1,\dots,b_n).
$$

(So  $A$  and  $B$  are **simultaneously diagonalizable by congruence**.)

Generalized eigenvalues of the pair  $(A,B)$  are defined as the roots of

$$
\det(\lambda B-A)=0 \quad\text{(equivalently }\det(A-\lambda B)=0\text{)}.
$$

The exercise asks:

1.  Show generalized eigenvalues are real and equal to  $\lambda_i=a_i/b_i$ .
2.  Solve the one-variable SDP
    
$$
\min\ c\,t\quad\text{s.t.}\quad tB\succeq A.
$$

I’ll do both with all the little linear algebra facts made explicit.

* * *

Part (a) Generalized eigenvalues are  $\lambda_i=a_i/b_i$  and are real
=======================================================================

### Step 1: Rewrite  $\lambda B-A$  using the congruence diagonalization

Because  $R$  is nonsingular, we can insert  $I = R^{-T}R^T$  and  $I = R R^{-1}$  in the right places:

$$
\lambda B-A = \lambda\big(R^{-T}(R^TBR)R^{-1}\big) \;-\; \big(R^{-T}(R^TAR)R^{-1}\big) = R^{-T}\big(\lambda R^TBR - R^TAR\big)R^{-1}.
$$

Now substitute the diagonal forms:

$$
\lambda R^TBR - R^TAR = \lambda\,\operatorname{diag}(b) - \operatorname{diag}(a) = \operatorname{diag}(\lambda b_1-a_1,\dots,\lambda b_n-a_n).
$$

So:

$$
\lambda B-A = R^{-T}\,\operatorname{diag}(\lambda b_i-a_i)\,R^{-1}.
$$

### Step 2: Take determinants carefully

Use  $\det(ABC)=\det(A)\det(B)\det(C)$  and  $\det(R^{-T})=\det(R^{-1})=\det(R)^{-1}$ :

$$
\det(\lambda B-A) = \det(R^{-T})\;\det\!\big(\operatorname{diag}(\lambda b_i-a_i)\big)\;\det(R^{-1}) = \det(R)^{-2}\;\prod_{i=1}^n(\lambda b_i-a_i).
$$

A diagonal matrix’s determinant is the product of its diagonal entries, hence the product.

### Step 3: Identify the roots

The scalar prefactor  $\det(R)^{-2}\neq 0$  never affects the roots. Therefore,

$$
\det(\lambda B-A)=0 \quad\Longleftrightarrow\quad \prod_{i=1}^n(\lambda b_i-a_i)=0 \quad\Longleftrightarrow\quad \exists i:\ \lambda b_i-a_i=0.
$$

So the generalized eigenvalues are exactly

$$
\boxed{\lambda_i=\frac{a_i}{b_i}\quad (i=1,\dots,n).}
$$

### Step 4: Why they are real, and why  $b_i\neq 0$ 

You’re told  $a_i,b_i\in\mathbb R$  (because the diagonal matrices are real symmetric). So  $a_i/b_i\in\mathbb R$  as soon as  $b_i\neq 0$ .

Why is  $b_i\neq 0$  for all  $i$ ? Because  $B$  is nonsingular, so  $\det(B)\neq 0$ . But

$$
\det(R^TBR)=\det(R)^2\det(B)\neq 0,
$$

so  $R^TBR$  is nonsingular. Since  $R^TBR=\operatorname{diag}(b)$ , a diagonal matrix is nonsingular iff every diagonal entry is nonzero. Hence  $b_i\neq 0$  for all  $i$ .

That completes (a).

* * *

Part (b) Solve  $\min c t$  subject to  $tB\succeq A$ 
======================================================

We need to characterize all  $t\in\mathbb R$  such that

$$
tB-A\succeq 0.
$$

### Step 1: Use congruence to diagonalize the LMI

Key fact: for nonsingular  $R$ ,

$$
X\succeq 0 \quad\Longleftrightarrow\quad R^T X R \succeq 0.
$$

(Reason:  $x^TXx\ge 0\ \forall x$  iff  $(Ry)^T X (Ry)\ge 0\ \forall y$ , since  $R$  is bijective.)

Apply this to  $X=tB-A$ :

$$
tB-A\succeq 0 \quad\Longleftrightarrow\quad R^T(tB-A)R\succeq 0.
$$

Compute:

$$
R^T(tB-A)R = t(R^TBR)-(R^TAR) = t\operatorname{diag}(b)-\operatorname{diag}(a) = \operatorname{diag}(t b_i-a_i).
$$

So the LMI is equivalent to

$$
\operatorname{diag}(t b_i-a_i)\succeq 0.
$$

### Step 2: PSD for a diagonal matrix = nonnegative diagonal entries

A diagonal matrix is PSD iff each diagonal entry is  $\ge 0$ . Therefore:

$$
tB\succeq A \quad\Longleftrightarrow\quad t b_i-a_i\ge 0\quad\text{for all }i.
$$

That is just a bunch of scalar inequalities.

### Step 3: Solve each inequality depending on the sign of  $b_i$ 

Because  $b_i\neq 0$ , each inequality is one of two types:

*   If  $b_i>0$ :
    $$
    t b_i-a_i\ge 0 \iff t\ge \frac{a_i}{b_i}.
    $$
*   If  $b_i<0$ :
    $$
    t b_i-a_i\ge 0 \iff t\le \frac{a_i}{b_i}
    $$
    (inequality flips when dividing by a negative).

So the feasible set of  $t$  is an interval (possibly unbounded):

$$
\boxed{ t \in \Big[\ \underbrace{\max_{i:\,b_i>0}\frac{a_i}{b_i}}_{=:L}\ ,\ \underbrace{\min_{i:\,b_i<0}\frac{a_i}{b_i}}_{=:U}\ \Big], }
$$

with the conventions:

*   If there are **no** indices with  $b_i>0$ , then  $L=-\infty$ .
*   If there are **no** indices with  $b_i<0$ , then  $U=+\infty$ .

Feasibility condition:

$$
\boxed{L\le U.}
$$

If  $L>U$ , the constraints contradict each other and the SDP is infeasible.

### Step 4: Optimize  $\min c t$  over that interval

Now it’s a 1-D linear program: minimize a linear function on an interval. The optimizer sits at an endpoint unless the objective is flat.

*   If  $c>0$ : minimizing  $ct$  means minimizing  $t$ . So choose the **smallest feasible**  $t$ , i.e.
    $$
    \boxed{t^\star = L=\max_{b_i>0}\frac{a_i}{b_i}}
    $$
    provided feasibility  $L\le U$ .  
    If  $L=-\infty$  (i.e. all  $b_i<0$ ), then the problem is **unbounded below** (you can send  $t\to -\infty$  and still satisfy all upper-bound constraints).
*   If  $c<0$ : minimizing  $ct$  means maximizing  $t$ . So choose the **largest feasible**  $t$ , i.e.
    $$
    \boxed{t^\star = U=\min_{b_i<0}\frac{a_i}{b_i}}
    $$
    again provided feasibility  $L\le U$ .  
    If  $U=+\infty$  (i.e. all  $b_i>0$ ), then the problem is **unbounded below** (you can send  $t\to +\infty$ , then  $ct\to -\infty$ ).
*   If  $c=0$ : objective is identically  $0$ . Any feasible  $t\in[L,U]$  is optimal.

So the clean “closed form” solution is:

$$
\boxed{ \text{Feasible } \iff L\le U,\quad L=\max_{b_i>0}\frac{a_i}{b_i}\ (=-\infty\text{ if none}),\quad U=\min_{b_i<0}\frac{a_i}{b_i}\ (=+\infty\text{ if none}). }
$$
 
$$
\boxed{ t^\star = \begin{cases} L, & c>0 \text{ and } L\le U \text{ and } L>-\infty,\\ U, & c<0 \text{ and } L\le U \text{ and } U<+\infty,\\ \text{any }t\in[L,U], & c=0 \text{ and } L\le U. \end{cases}}
$$

And the optimal value is  $c\,t^\star$  in the bounded cases.

* * *

Extra intuition (helps you not forget)
======================================

The constraint  $tB\succeq A$  means: for every vector  $x$ ,

$$
x^T(tB-A)x \ge 0 \quad\Longleftrightarrow\quad t\,x^T Bx \ge x^T A x.
$$

If  $B\succ 0$  (all  $b_i>0$ ), this is exactly:

$$
t \ge \sup_{x\neq 0}\frac{x^TAx}{x^TBx},
$$

the maximum generalized Rayleigh quotient, which equals the largest generalized eigenvalue. In your diagonalized coordinates, that supremum becomes  $\max_i a_i/b_i$ , matching  $L$ .

If  $B$  is indefinite, some directions have  $x^TBx<0$ , and those directions create **upper bounds** on  $t$  instead of lower bounds. That’s why the feasible set becomes an interval  $[L,U]$  rather than just  $[L,\infty)$ .

* * *

If you want, I can rewrite (b) in “solver language” as: “the feasible set for  $t$  is an interval determined by generalized eigenvalues split by the inertia of  $B$ , and the optimum is the appropriate endpoint depending on  $\operatorname{sign}(c)$ .”

## Response:
Thought for 24s

Exercise 4.40 — Represent LPs, QPs, QCQPs, SOCPs, and matrix-fractional problems as SDPs
----------------------------------------------------------------------------------------

The meta-fact this exercise wants you to internalize is:

An SDP is “linear objective + linear equalities + **linear matrix inequalities** (LMIs)”.

An LMI looks like

$$
F(x)\succeq 0,\qquad F(x)=F_0+\sum_{j=1}^n x_j F_j,
$$

where each  $F_j\in\mathbb S^k$  is symmetric and  $\succeq 0$  means “positive semidefinite”.

So the whole game is: take whatever constraint/objective you have, and rewrite it as an LMI using one tool: the **Schur complement**.

* * *

0) The Schur complement theorem (the one hammer)
================================================

Let  $A\in\mathbb S^p$  and  $C\in\mathbb S^q$ , and consider the symmetric block matrix

$$
X=\begin{bmatrix}A & B\\ B^T & C\end{bmatrix}.
$$

### Version 1 (when  $A\succ 0$ )

If  $A$  is positive definite, then

$$
X\succeq 0 \quad\Longleftrightarrow\quad C - B^T A^{-1}B \succeq 0.
$$

The matrix  $C - B^T A^{-1}B$  is the Schur complement of  $A$  in  $X$ .

### Version 2 (when  $A\succeq 0$  may be singular)

There’s a more general statement using the Moore–Penrose pseudoinverse  $A^\dagger$  plus a range condition. For almost all modeling in BV Chapter 4, you can safely use Version 1 by arranging  $A$  to be  $I$  or a positive scalar, which is always  $\succ 0$ .

We’ll do exactly that.

* * *

1) (a) LP as an SDP
===================

A generic LP:

$$
\min\ c^T x \quad\text{s.t.}\quad Gx\le h,\ \ Ax=b.
$$

### Step 1: Scalar inequality is a 1×1 LMI

A scalar inequality  $\alpha(x)\ge 0$  is equivalent to

$$
[\alpha(x)]\succeq 0
$$

because a  $1\times 1$  symmetric matrix is PSD iff its single entry is  $\ge 0$ .

### Step 2: Turn  $Gx\le h$  into diagonal PSD

 $Gx\le h$  means  $h-Gx\ge 0$  componentwise. Stack them:

$$
\operatorname{diag}(h-Gx)\succeq 0.
$$

This is an LMI because  $\operatorname{diag}(h-Gx)$  is an affine function of  $x$ .

### Final SDP form of the LP

$$
\boxed{ \begin{aligned} \min\ & c^T x\\ \text{s.t. } & Ax=b,\\ & \operatorname{diag}(h-Gx)\succeq 0. \end{aligned}}
$$

That’s an SDP with only diagonal LMIs (so it’s “SDP-easy”).

* * *

2) A key micro-template:  $\|z\|_2^2\le t$  as an LMI
=====================================================

This is the template you’ll reuse for QPs and QCQPs.

Claim:

$$
\boxed{ \|z\|_2^2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} t & z^T\\ z & I \end{bmatrix}\succeq 0. }
$$

### Proof (Schur complement with  $A=I\succ 0$ )

Let

$$
X=\begin{bmatrix} t & z^T\\ z & I \end{bmatrix}.
$$

Here  $A=I$  and  $B=z$ ,  $C=t$  (or swap blocks; same result). Take Schur complement of  $I$ :

$$
X\succeq 0 \iff t - z^T I^{-1} z \ge 0 \iff t - z^T z \ge 0 \iff \|z\|_2^2 \le t.
$$

Done. Also note  $X\succeq 0$  automatically implies  $t\ge 0$  (principal minors), so the inequality is well-posed.

* * *

3) (b) Convex QP as an SDP
==========================

A convex QP objective is quadratic with PSD Hessian. Write a typical convex QP as

$$
\min_x\ \frac12 x^T P x + q^T x + r \quad\text{s.t.}\quad \text{(linear constraints)},
$$

with  $P\succeq 0$ .

### Step 1: Epigraph the quadratic objective

Introduce  $t$  and minimize  $t$  instead:

$$
\min_{x,t}\ t \quad\text{s.t.}\quad \frac12 x^T P x + q^T x + r \le t,
$$

plus the original linear constraints.

This is equivalent because at optimum  $t$  will be pushed down to the objective value.

### Step 2: Factor the PSD quadratic form

Since  $P\succeq 0$ , there exists  $R$  with  $P=R^T R$  (e.g., Cholesky if  $P\succ 0$ , or any square root / eigen-factorization if semidefinite).  
Then

$$
x^T P x = x^T R^T R x = \|Rx\|_2^2.
$$

So the epigraph constraint becomes

$$
\frac12 \|Rx\|_2^2 + q^T x + r \le t \quad\Longleftrightarrow\quad \|Rx\|_2^2 \le 2(t - q^T x - r).
$$

Define the affine scalar

$$
s := 2(t - q^T x - r).
$$

Then the constraint is  $\|Rx\|_2^2\le s$ , i.e.  $\|z\|^2\le s$  with  $z=Rx$ .

### Step 3: Use the LMI template

$$
\|Rx\|_2^2 \le s \Longleftrightarrow \begin{bmatrix} s & (Rx)^T\\ Rx & I \end{bmatrix}\succeq 0.
$$

Substitute back  $s=2(t-q^T x-r)$ . This is affine in  $(x,t)$  in the  $(1,1)$  entry and affine in  $x$  in the off-diagonal block.

### Final SDP for the convex QP

If your linear constraints are  $Gx\le h,\ Ax=b$ , a clean SDP is:

$$
\boxed{ \begin{aligned} \min\ & t\\ \text{s.t. }& Ax=b,\quad Gx\le h,\\ & \begin{bmatrix} 2(t-q^T x-r) & (Rx)^T\\ Rx & I \end{bmatrix}\succeq 0. \end{aligned}}
$$

(And  $Gx\le h$  can itself be written as a diagonal LMI as in part (a), if you want a “pure LMI only” view.)

* * *

4) Convex QCQP as an SDP
========================

A convex QCQP has quadratic constraints with PSD quadratic parts:

$$
x^T P_i x + q_i^T x + r_i \le 0,\qquad P_i\succeq 0.
$$

### Step 1: Factor each  $P_i$ 

Write  $P_i=R_i^T R_i$ . Then  $x^T P_i x = \|R_i x\|_2^2$ .

Constraint becomes:

$$
\|R_i x\|_2^2 + q_i^T x + r_i \le 0 \quad\Longleftrightarrow\quad \|R_i x\|_2^2 \le -(q_i^T x + r_i).
$$

### Step 2: LMI template

Apply  $\|z\|^2\le t \iff \begin{bmatrix}t & z^T\\ z & I\end{bmatrix}\succeq 0$  with  $z=R_i x$  and  $t=-(q_i^T x+r_i)$ :

$$
\boxed{ \begin{bmatrix} -(q_i^T x+r_i) & (R_i x)^T\\ R_i x & I \end{bmatrix}\succeq 0. }
$$

This is an LMI in  $x$  (all blocks are affine in  $x$  except the constant  $I$ ).

So: a convex QCQP becomes an SDP by replacing each quadratic inequality with one such LMI.

* * *

5) SOCP as an SDP
=================

A standard SOC constraint is:

$$
\|u\|_2 \le v,
$$

where  $u$  is an affine vector expression and  $v$  is an affine scalar expression.

The key equivalence (the BV-style one) is:

$$
\boxed{ \|u\|_2 \le v \quad\Longleftrightarrow\quad \begin{bmatrix} v & u^T\\ u & vI \end{bmatrix}\succeq 0. }
$$

### Proof (Schur complement, done carefully)

Assume first  $v>0$ . Take Schur complement of the scalar block  $[v]$  (so  $A=v$ ):

$$
\begin{bmatrix} v & u^T\\ u & vI \end{bmatrix}\succeq 0 \iff vI - u \frac{1}{v} u^T \succeq 0.
$$

Multiply by  $v>0$ :

$$
v^2 I - u u^T \succeq 0.
$$

Now,  $v^2 I - uu^T\succeq 0$  is equivalent to the largest eigenvalue of  $uu^T$  being  $\le v^2$ . But  $uu^T$  is rank-1 with eigenvalues  $\|u\|_2^2$  and zeros. So this is equivalent to

$$
\|u\|_2^2 \le v^2 \quad\Longleftrightarrow\quad \|u\|_2\le v.
$$

If  $v=0$ , the LMI forces  $u=0$  (since the bottom-right block is  $0\cdot I$ ), and that matches  $\|u\|\le 0$ . So by continuity, the equivalence holds for  $v\ge 0$ . And the LMI itself enforces  $v\ge 0$  (principal minors).

So every SOC constraint becomes an LMI of size  $(n+1)\times(n+1)$ . Therefore, any SOCP (linear objective + affine constraints + SOC constraints) can be rewritten as an SDP.

* * *

6) (c) Matrix fractional optimization as an SDP
===============================================

This is the cleanest Schur-complement trick of them all.

Problem class:

$$
\min_x\ y(x)^T F(x)^{-1} y(x),
$$

where

*    $y(x)=Ax+b$  is affine,
*    $F(x)$  is affine symmetric:
    $$
    F(x)=F_0+\sum_{i=1}^n x_i F_i,
    $$

and we require  $F(x)\succ 0$  (or at least  $\succeq 0$  with a generalized-inverse interpretation).

### Step 1: Epigraph the objective

Introduce  $t$  and write:

$$
\min_{x,t}\ t \quad\text{s.t.}\quad y(x)^T F(x)^{-1} y(x) \le t,\quad F(x)\succ 0.
$$

### Step 2: Schur complement equivalence

Claim:

$$
\boxed{ y^T F^{-1} y \le t,\ \ F\succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} F & y\\ y^T & t \end{bmatrix}\succeq 0. }
$$

Proof: Take Schur complement of  $F\succ 0$ :

$$
\begin{bmatrix} F & y\\ y^T & t \end{bmatrix}\succeq 0 \iff t - y^T F^{-1} y \ge 0 \iff y^T F^{-1} y \le t.
$$

### Final SDP

Plug in  $F(x)$  and  $y(x)$ :

$$
\boxed{ \begin{aligned} \min\ & t\\ \text{s.t. }& \begin{bmatrix} F_0+\sum_{i=1}^n x_i F_i & Ax+b\\ (Ax+b)^T & t \end{bmatrix}\succeq 0. \end{aligned}}
$$

If your version of the exercise also wants explicit domain constraints, you can add  $F(x)\succeq 0$  separately, but it’s actually implied by the block LMI (its principal submatrix must be PSD). The subtlety is strictness ( $\succ 0$ ) vs semidefinite; for modeling in SDP solvers, you usually accept  $\succeq 0$  and the optimum typically lands where the expression is well-defined (or you interpret via pseudoinverse if needed).

* * *

7) What to memorize (the “pattern card” you want in your head)
==============================================================

1.  Scalar inequality  $\alpha(x)\ge 0$  is an LMI:  $[\alpha(x)]\succeq 0$ .
2.  Vector inequality  $h-Gx\ge 0$  is diagonal LMI:  $\mathrm{diag}(h-Gx)\succeq 0$ .
3.  Quadratic epigraph:
    
$$
\|z\|^2\le t \iff \begin{bmatrix}t&z^T\\ z&I\end{bmatrix}\succeq 0.
$$
4.  SOC epigraph:
    
$$
\|u\|\le v \iff \begin{bmatrix}v&u^T\\ u&vI\end{bmatrix}\succeq 0.
$$
5.  Matrix fractional:
    
$$
y^T F^{-1}y \le t \iff \begin{bmatrix}F&y\\ y^T&t\end{bmatrix}\succeq 0.
$$

That’s the entire exercise in five reusable equivalences.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)