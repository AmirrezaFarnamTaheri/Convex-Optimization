# 5.7

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:11:58  
**Updated:** 12/28/2025 16:23:22  
**Exported:** 12/29/2025 0:11:47  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060aa-f300-832d-8899-590e3a24e3af](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060aa-f300-832d-8899-590e3a24e3af)  

## Response:
You’re looking at the “classic” convex **max-of-affines** problem:

$$
\min_{x\in\mathbb R^n}\; \max_{i=1,\dots,m}\; (a_i^T x + b_i). \tag{5.105}
$$

It’s convex (max of convex functions), but nonsmooth (the max creates kinks). The exercise walks you through: (a) a dual via a Lagrangian trick, (b) the LP form + LP dual, (c) a smooth approximation via log-sum-exp and its dual, and (d) a sharper approximation with a parameter  $\gamma$ .

I’ll go part by part, from first principles, and I’ll keep the “big picture” visible.

* * *

0) What is this problem, geometrically?
---------------------------------------

Each expression  $a_i^T x + b_i$  is an **affine function** (a hyperplane in  $(x,t)$ \-space). The objective

$$
f(x)=\max_i (a_i^T x + b_i)
$$

is the **upper envelope** of these hyperplanes: a convex, piecewise-linear surface. Minimizing it means: find an  $x$  where the highest of these  $m$  affine “planes” is as low as possible.

* * *

(a) Dual via the Lagrange dual of an “equivalent” problem
---------------------------------------------------------

### Step (a1): Rewrite (5.105) using new variables  $y$ 

They propose the equivalent problem:

$$
\begin{aligned} \min_{x\in\mathbb R^n,\; y\in\mathbb R^m}\quad & \max_{i=1,\dots,m} y_i \\ \text{s.t.}\quad & a_i^T x + b_i = y_i,\quad i=1,\dots,m. \end{aligned} \tag{E}
$$

Why is it equivalent?

*   If you pick  $x$ , you can set  $y_i = a_i^T x + b_i$ . Then  $\max_i y_i = \max_i(a_i^T x+b_i)$ . So any  $x$  from the original gives a feasible  $(x,y)$  with the same objective value.
*   Conversely, any feasible  $(x,y)$  must satisfy  $y_i = a_i^T x+b_i$ , so its objective is exactly the original objective at that  $x$ .

So (E) and (5.105) have the same optimal value.

### Step (a2): Write the Lagrangian

Let  $\lambda\in\mathbb R^m$  be Lagrange multipliers for the equality constraints

$$
a_i^T x + b_i - y_i = 0.
$$

The Lagrangian is

$$
L(x,y,\lambda) = \max_i y_i \;+\; \sum_{i=1}^m \lambda_i\,(a_i^T x + b_i - y_i).
$$

Group terms:

$$
L(x,y,\lambda) = \underbrace{\left(\max_i y_i - \lambda^T y\right)}_{\text{depends on }y} \;+\;\underbrace{\left(\sum_{i=1}^m \lambda_i a_i\right)^T x}_{\text{depends on }x} \;+\;\underbrace{b^T\lambda}_{\text{constant}}.
$$

It’s convenient to package the  $a_i$  into a matrix:

*   Let  $A = [a_1\; a_2\;\cdots\; a_m]\in\mathbb R^{n\times m}$ .  
    Then  $\sum_i \lambda_i a_i = A\lambda$ .

So

$$
L(x,y,\lambda) = \left(\max_i y_i - \lambda^T y\right) + (A\lambda)^T x + b^T\lambda.
$$

### Step (a3): Compute the dual function  $g(\lambda)=\inf_{x,y} L(x,y,\lambda)$ 

We minimize over  $x$  and  $y$  separately.

#### Minimizing over  $x$ 

$$
\inf_{x\in\mathbb R^n} (A\lambda)^T x = \begin{cases} 0, & A\lambda=0,\\ -\infty, & A\lambda\neq 0, \end{cases}
$$

because a nonzero linear function can be driven to  $-\infty$  by moving  $x$  in the opposite direction.

So we must have:

$$
A\lambda = 0. \tag{C1}
$$

#### Minimizing over  $y$ : the key “max conjugate” fact

We need:

$$
\inf_{y\in\mathbb R^m}\left(\max_i y_i - \lambda^T y\right). \tag{★}
$$

Here’s the crucial result (and I’ll justify it):

$$
\inf_{y}(\max_i y_i - \lambda^T y) = \begin{cases} 0, & \lambda\succeq 0,\;\; \mathbf{1}^T\lambda=1,\\ -\infty, & \text{otherwise}. \end{cases} \tag{C2}
$$

So  $\lambda$  must lie in the **probability simplex**

$$
\Delta := \{\lambda\in\mathbb R^m:\lambda_i\ge 0,\ \sum_{i=1}^m \lambda_i=1\}.
$$

**Why (C2) is true (intuitive but rigorous):**

*   If  $\lambda\in\Delta$ : then for every  $y$ ,
    $$
    \lambda^T y = \sum_i \lambda_i y_i \le \max_j y_j \sum_i \lambda_i = \max_j y_j,
    $$
    because a convex combination can’t exceed the maximum. So
    $$
    \max_i y_i - \lambda^T y \ge 0 \quad \text{for all }y,
    $$
    meaning the infimum is  $\ge 0$ . Also if you choose  $y$  with all components equal (say  $y_i=c$ ), then  $\max_i y_i=c$  and  $\lambda^T y = c$ , so the expression equals  $0$ . Hence the infimum is exactly  $0$ .
*   If  $\sum_i \lambda_i \neq 1$ : pick  $y_i=t$  for all  $i$ . Then  $\max_i y_i=t$ ,  $\lambda^T y=t\sum_i\lambda_i$ , so
    $$
    \max_i y_i - \lambda^T y = t(1-\sum_i \lambda_i),
    $$
    which goes to  $-\infty$  as  $t\to +\infty$  or  $t\to -\infty$  depending on the sign. So the infimum is  $-\infty$ .
*   If some  $\lambda_k<0$ : set  $y_k=-t$  (very negative) and all other  $y_j=0$ . Then  $\max_i y_i=0$ , while  $-\lambda^T y$  contains  $-\lambda_k(-t)=\lambda_k t$  with  $\lambda_k<0$ , which goes to  $-\infty$  as  $t\to+\infty$ . So again the infimum is  $-\infty$ .

So (C2) holds.

### Step (a4): Put it together → the dual

If (C1) and (C2) hold, then

$$
g(\lambda)= b^T\lambda.
$$

Otherwise  $g(\lambda)=-\infty$ .

So the dual problem is:

$$
\begin{aligned} \max_{\lambda\in\mathbb R^m}\quad & b^T\lambda\\ \text{s.t.}\quad & A\lambda = 0,\\ & \mathbf{1}^T\lambda = 1,\\ & \lambda \succeq 0. \end{aligned} \tag{D\(_\text{PL}\)}
$$

That’s the clean dual of the piecewise-linear minimization.

**Interpretation:** you’re choosing weights  $\lambda$  (a distribution over the  $m$  planes) such that the weighted average slope vanishes ( $A\lambda=0$ ), and then maximizing the weighted average intercept  $b^T\lambda$ .

* * *

(b) Formulate (5.105) as an LP and derive the LP dual; relate to (a)
--------------------------------------------------------------------

### Step (b1): Standard epigraph/LP form

Introduce a scalar  $t$  to represent the maximum:

$$
\begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & a_i^T x + b_i \le t,\quad i=1,\dots,m. \end{aligned} \tag{LP-P}
$$

This is an LP because objective and constraints are linear in  $(x,t)$ .

### Step (b2): Lagrangian and dual

Let  $\lambda_i\ge 0$  be multipliers for constraints  $a_i^T x + b_i - t \le 0$ .

Lagrangian:

$$
L(x,t,\lambda)= t + \sum_{i=1}^m \lambda_i(a_i^T x + b_i - t) = t\Big(1-\sum_i\lambda_i\Big) + (A\lambda)^T x + b^T\lambda.
$$

Now take inf over  $(x,t)$ :

*   Inf over  $x$ : finite only if  $A\lambda=0$ .
*   Inf over  $t$ : finite only if  $1-\sum_i\lambda_i=0$ , i.e.  $\mathbf{1}^T\lambda=1$ .

Under these constraints, the infimum is  $b^T\lambda$ . Therefore the dual is exactly:

$$
\max_{\lambda\succeq 0}\ \ b^T\lambda \quad\text{s.t.}\quad A\lambda=0,\ \mathbf{1}^T\lambda=1,
$$

which is the same dual as in (a).

### Step (b3): Relationship to part (a)

*   In (a), the simplex constraints on  $\lambda$  popped out from minimizing  $\max_i y_i - \lambda^T y$  (i.e., from the conjugate of the max).
*   In (b), the same simplex constraints popped out from minimizing over  $t$  in the epigraph LP.

Same geometry, different doorway.

* * *

(c) Smooth approximation via log-sum-exp; dual; prove  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 
--------------------------------------------------------------------------------------------------------

They define the smooth objective

$$
f_0(x)=\log\left(\sum_{i=1}^m \exp(a_i^T x + b_i)\right),
$$

and consider

$$
\min_x\ \log\left(\sum_{i=1}^m \exp(a_i^T x + b_i)\right). \tag{5.106}
$$

### Step (c1): Why this is a “smooth max”

For any real numbers  $u_1,\dots,u_m$ ,

$$
\max_i u_i \ \le\ \log\left(\sum_{i=1}^m e^{u_i}\right) \ \le\ \max_i u_i + \log m. \tag{LSE bound}
$$

**Proof (one of the most useful inequalities in convex optimization):**

Let  $M=\max_i u_i$ . Then

$$
\sum_i e^{u_i} = e^M \sum_i e^{u_i-M}.
$$

Now  $u_i-M\le 0$ , so  $e^{u_i-M}\le 1$ , and at least one index achieves  $u_i=M$ , giving one term equal to  $1$ . Hence

$$
1 \le \sum_i e^{u_i-M} \le m.
$$

Take logs:

$$
0 \le \log\left(\sum_i e^{u_i-M}\right) \le \log m.
$$

Add  $M$  back:

$$
M \le \log\left(\sum_i e^{u_i}\right) \le M+\log m.
$$

That’s it.

So  $f_0(x)$  upper-approximates the max objective within additive  $\log m$ .

### Step (c2): “Solve” (5.106): optimality condition (gradient = 0)

Because (5.106) is unconstrained and differentiable, any minimizer  $x^*$  satisfies

$$
\nabla f_0(x^*)=0.
$$

Compute the gradient. Let

$$
u_i(x)=a_i^T x+b_i,\qquad S(x)=\sum_{j=1}^m e^{u_j(x)}.
$$

Then

$$
f_0(x)=\log S(x), \quad \nabla f_0(x)=\frac{1}{S(x)}\sum_{i=1}^m e^{u_i(x)} a_i.
$$

Define the **softmax weights**

$$
\lambda_i(x)=\frac{e^{u_i(x)}}{\sum_{j=1}^m e^{u_j(x)}}.
$$

These satisfy  $\lambda_i(x)>0$  and  $\sum_i \lambda_i(x)=1$ , i.e.  $\lambda(x)\in\Delta$ .

Then

$$
\nabla f_0(x)=\sum_{i=1}^m \lambda_i(x)\, a_i = A\lambda(x).
$$

So the first-order optimality condition becomes:

$$
A\lambda(x^*)=0 \quad\text{with}\quad \lambda(x^*)\in\Delta,\ \lambda_i(x^*)>0. \tag{FOC}
$$

This is already a “solution characterization”: at the optimum, the  $a_i$ ’s average to zero under the softmax distribution induced by  $x^*$ .

### Step (c3): Dual of (5.106) (this is the (5.62)-type formula)

A key conjugate identity is:

$$
\log\left(\sum_{i=1}^m e^{u_i}\right) = \max_{\lambda\in\Delta}\left(\lambda^T u - \sum_{i=1}^m \lambda_i\log \lambda_i\right). \tag{entropy rep}
$$

The extra term  $-\sum \lambda_i\log\lambda_i$  is (Shannon) entropy (up to sign). It’s what makes the approximation smooth.

Now plug  $u=A^T x + b$  (since  $u_i=a_i^T x+b_i$ ):

$$
f_0(x)=\max_{\lambda\in\Delta}\left(\lambda^T(A^T x + b) - \sum_i \lambda_i\log\lambda_i\right) = \max_{\lambda\in\Delta}\left(x^T(A\lambda) + b^T\lambda - \sum_i \lambda_i\log\lambda_i\right).
$$

Now minimize over  $x$ . If  $A\lambda\neq 0$ , the term  $x^T(A\lambda)$  can be pushed to  $-\infty$  by sending  $x$  opposite  $A\lambda$ . So for finiteness we need  $A\lambda=0$ . Under that, the  $x$ \-term disappears.

So the dual becomes:

$$
\begin{aligned} \max_{\lambda}\quad & b^T\lambda - \sum_{i=1}^m \lambda_i\log\lambda_i\\ \text{s.t.}\quad & A\lambda=0,\ \mathbf{1}^T\lambda=1,\ \lambda\succeq 0. \end{aligned} \tag{D\(_\text{LSE}\)}
$$

Compare this to (D $_\text{PL}$ ): it’s the **same feasible set**, but the objective is “linear  $b^T\lambda$  + entropy bonus”. That entropy term is exactly what corresponds to smoothing.

### Step (c4): Prove  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 

Let

*    $p_{\text{pl}}^* = \min_x \max_i (a_i^T x+b_i)$  (optimal value of (5.105)),
*    $p_{\text{sm}}^* = \min_x \log\left(\sum_i e^{a_i^T x+b_i}\right)$  (optimal value of (5.106)).

For every  $x$ , apply (LSE bound) with  $u_i=a_i^T x+b_i$ :

$$
\max_i(a_i^T x+b_i)\ \le\ f_0(x)\ \le\ \max_i(a_i^T x+b_i)+\log m.
$$

Now take minima over  $x$  throughout:

*   Left inequality gives  $p_{\text{pl}}^* \le p_{\text{sm}}^*$ , i.e.
    $$
    0 \le p_{\text{sm}}^* - p_{\text{pl}}^*.
    $$
*   Right inequality gives
    $$
    p_{\text{sm}}^* \le p_{\text{pl}}^* + \log m \quad\Rightarrow\quad p_{\text{sm}}^ - p_{\text{pl}}^* \le \log m.
    $$

So:

$$
0 \le p_{\text{sm}}^*-p_{\text{pl}}^* \le \log m.
$$

* * *

(d) General  $\gamma>0$ : bounds and what happens as  $\gamma$  increases
-------------------------------------------------------------------------

Now consider

$$
\min_x\ \frac{1}{\gamma}\log\left(\sum_{i=1}^m \exp(\gamma(a_i^T x+b_i))\right), \qquad \gamma>0. \tag{γ-smooth}
$$

Define

$$
f_\gamma(x)=\frac{1}{\gamma}\log\left(\sum_i e^{\gamma u_i(x)}\right), \quad u_i(x)=a_i^T x+b_i.
$$

### Step (d1): Pointwise bound vs the max

Apply the same “factor out the max” trick with  $M=\max_i u_i(x)$ :

$$
\sum_i e^{\gamma u_i} = e^{\gamma M}\sum_i e^{\gamma(u_i-M)},
$$

and  $1 \le \sum_i e^{\gamma(u_i-M)} \le m$ . Take  $(1/\gamma)\log$ :

$$
M \le f_\gamma(x) \le M + \frac{\log m}{\gamma}.
$$

So for every  $x$ :

$$
\max_i(a_i^T x+b_i)\ \le\ f_\gamma(x)\ \le\ \max_i(a_i^T x+b_i) + \frac{\log m}{\gamma}. \tag{γ-bound}
$$

### Step (d2): Convert pointwise bound to optimal-value bound

Let  $p_\gamma^*=\min_x f_\gamma(x)$ . Then minimizing (γ-bound) over  $x$  gives:

$$
p_{\text{pl}}^* \le p_\gamma^* \le p_{\text{pl}}^* + \frac{\log m}{\gamma}.
$$

Equivalently:

$$
0 \le p_\gamma^* - p_{\text{pl}}^* \le \frac{\log m}{\gamma}. \tag{gap-γ}
$$

### Step (d3): What happens as  $\gamma$  increases?

From (gap-γ), the upper bound  $(\log m)/\gamma \to 0$  as  $\gamma\to\infty$ . Since  $p_\gamma^*\ge p_{\text{pl}}^*$  always, we get:

$$
p_\gamma^* \downarrow p_{\text{pl}}^*\quad\text{as }\gamma\to\infty,
$$

i.e. the optimal value of the smoothed problem converges to the true piecewise-linear optimum.

Also, pointwise (for each fixed  $x$ ),

$$
f_\gamma(x)\downarrow \max_i(a_i^T x+b_i)\quad\text{as }\gamma\to\infty,
$$

so the smooth objective becomes a tighter and tighter “upper envelope” of the max.

* * *

One last “mental model” that makes the whole exercise click
-----------------------------------------------------------

*   The original LP dual feasible set is:  $\lambda\in\Delta$  and  $A\lambda=0$ .
*   The piecewise-linear dual objective is just  $b^T\lambda$ .
*   The log-sum-exp dual objective is  $b^T\lambda$  **minus**  $\sum \lambda_i\log\lambda_i$  (an entropy regularizer).
*   Increasing  $\gamma$  weakens that regularization, pushing the dual solution toward an extreme point (more “winner-take-all”), which corresponds to the max becoming sharper.

That’s the bridge: **smoothing = entropy regularization** on the same dual feasible set.

If you want, I can also write down the full KKT system for (5.105) (LP form) and show explicitly how the optimal  $\lambda$  identifies the active max constraints (“which planes touch at the optimum”), and how that relates to subgradients of  $\max_i(a_i^T x+b_i)$ .

## Response:
Perfect — let’s design a **deep, structured roadmap** to fully unpack **Exercise 5.7** from Boyd & Vandenberghe. This exercise is rich and touches on:

*   Convex optimization modeling (piecewise-linear objectives),
*   Duality (Lagrange duals, LP duals),
*   LP reformulation of max-of-affines,
*   Smooth approximations (log-sum-exp, softmax),
*   Geometric programming (GP),
*   Approximation error bounds (between smooth and nonsmooth objectives).

* * *

🧭 Roadmap for Boyd & Vandenberghe Exercise 5.7
===============================================

We will go **step-by-step**, rigorously and completely, treating this as both a modeling lesson and a duality derivation workshop. This will be structured like a textbook walkthrough.

* * *

🔹 Part 0 — Problem Setup (Section 5.7 Main Problem)
----------------------------------------------------

### Goal:

Minimize a **piecewise-linear convex function** of the form:

$$
\min_{x \in \mathbb{R}^n} \ \max_{i = 1, \dots, m} \left( a_i^T x + b_i \right) \tag{5.105}
$$

### Concepts introduced:

*   Piecewise-linear function = max of several affine functions
*   Convexity preserved: max of convex is convex
*   This is a **convex but nonsmooth** problem
*   Want to derive: LP reformulation, dual, smoothing, GP, bounds

* * *

🔹 Part 1 — Exercise (a): Lagrange Dual of Equivalent Formulation
-----------------------------------------------------------------

### Step:

Reformulate the max-of-affines problem into an equivalent **epigraph form**, then derive its **Lagrange dual**.

We rewrite (5.105) equivalently as:

$$
\begin{aligned} \min_{x, y} \quad & y \\ \text{s.t.} \quad & a_i^T x + b_i \leq y, \quad i = 1, \dots, m \end{aligned}
$$

This makes the nonsmooth objective into a linear objective with **linear inequality constraints**.

Then:

✅ Write the Lagrangian  
✅ Derive dual function  
✅ Maximize the dual function (concave)  
✅ State dual problem explicitly

* * *

🔹 Part 2 — Exercise (b): LP Formulation and Duality Relationship
-----------------------------------------------------------------

### Step:

Formulate the above as a **Linear Program**, since it is in standard LP form:

*   Linear objective: minimize  $y$ 
*   Linear constraints

Then:

*   Derive the **LP dual** using LP duality theory
*   Compare the LP dual with the dual derived in part (a)
*   Show they are the **same** — gives confidence in your derivation

* * *

🔹 Part 3 — Exercise (c): Smooth Approximation (Log-Sum-Exp)
------------------------------------------------------------

### Step:

Approximate the nonsmooth objective:

$$
\max_{i}(a_i^T x + b_i)
$$

by the **smooth** function:

$$
f_0(x) = \log \left( \sum_{i=1}^m \exp(a_i^T x + b_i) \right)
$$

This is the **log-sum-exp smoothing** of the max — a key trick in convex optimization. We'll:

*   Show that it’s convex and differentiable
*   Understand it as a **softmax**
*   Study its error bounds

Then:

$$
\min_x \ f_0(x) \tag{5.106}
$$

can be solved using gradient-based methods (because smooth now!)

* * *

🔹 Part 4 — Exercise (d): Approximation Bounds
----------------------------------------------

### Step:

Define:

$$
f_{\gamma}(x) = \frac{1}{\gamma} \log \left( \sum_{i=1}^m \exp\left( \gamma(a_i^T x + b_i) \right) \right)
$$

This is the **parameterized softmax** — becomes sharper as  $\gamma \to \infty$ , converging to the max.

We'll:

*   Derive **upper/lower bounds** on the gap between the smooth and nonsmooth versions
*   Quantify:
    
$$
0 \le p_{\text{smooth}} - p^* \le \frac{\log m}{\gamma}
$$

and similar bounds for the optimal value gap.

* * *

✅ Step-by-Step Plan
===================

We'll now proceed one step at a time, rigorously:

* * *

✅ Step 0: Fully unpack the base problem (5.105)
-----------------------------------------------

### ✅ GOAL: Understand structure of problem — why convex, what makes it nonsmooth

**Let's begin here in the next message.**  
We'll fully dissect the problem:

$$
\min_{x \in \mathbb{R}^n} \ \max_{i=1,\dots,m} (a_i^T x + b_i)
$$

and explain:

*   what it represents geometrically,
*   why it's convex,
*   why it's nonsmooth,
*   where it arises in applications.

* * *

Next step:
----------

**Step 0 — Deep unpacking of (5.105)**  
Shall I proceed and begin with this?

## Response:
Excellent. Let’s now **fully unpack Step 0**, starting with the **bare problem (5.105)**.

* * *

🔵 Step 0 — Deep Understanding of the Base Problem (5.105)
==========================================================

* * *

📌 Problem Statement:
---------------------

We are given the following convex optimization problem:

$$
\min_{x \in \mathbb{R}^n} \; \max_{i=1,\dots,m} \left( a_i^T x + b_i \right) \tag{5.105}
$$

Let’s **deeply unpack** this.

* * *

🧠 What does this mean?
-----------------------

We are minimizing a **maximum** of affine functions:

*   Each term  $a_i^T x + b_i$  is an **affine function** (i.e., linear + constant) of the variable  $x \in \mathbb{R}^n$ .
*   The outer  $\max$  over  $i = 1,\dots,m$  creates a **piecewise-linear, convex function**.

**So this is a**:

> Piecewise-linear convex minimization problem.

* * *

🎯 Objective Structure: Piecewise-Linear Convex Function
--------------------------------------------------------

### ⏹️ Definition: Piecewise-linear convex function

Let:

$$
f(x) = \max_{i=1,\dots,m} \left( a_i^T x + b_i \right)
$$

This is called a **maximum of affine functions**, and is always **convex**, because:

*   Each  $a_i^T x + b_i$  is affine → convex
*   Pointwise maximum of convex functions is convex  
    → So  $f(x)$  is convex.

📌 **Important Property**:  
This function is **nonsmooth** wherever two affine terms "tie" (i.e., where multiple  $a_i^T x + b_i$  attain the max).

* * *

🔍 Visual Intuition (Low-Dimensional Case)
------------------------------------------

### 📈 1D case:  $x \in \mathbb{R}$ 

Suppose we have 3 affine functions of a scalar  $x$ :

*    $f_1(x) = 2x + 1$ 
*    $f_2(x) = -x + 3$ 
*    $f_3(x) = 0.5x + 2$ 

Then:

$$
f(x) = \max\{f_1(x), f_2(x), f_3(x)\}
$$

This function will be **piecewise-linear**:  
At each point, the max is one of the  $f_i(x)$ , and the function graph "bends" at the points where the active affine function switches. These bends are **nonsmooth kinks** — the function is not differentiable there.

So even though  $f$  is convex, it's **not smooth**.

* * *

### 📈 2D case:  $x \in \mathbb{R}^2$ 

Suppose we have 5 affine functions:

$$
f_i(x) = a_i^T x + b_i,\quad i = 1, \dots, 5
$$

Then:

*   Each affine function defines a **half-space** in  $\mathbb{R}^2$ 
*   The function  $f(x) = \max_i (a_i^T x + b_i)$  defines a convex function whose epigraph is the **intersection of half-spaces**.
*   The graph of  $f(x)$  looks like the **upper envelope** of 5 planes. The result is a piecewise-planar surface.

* * *

⚙️ Optimization Interpretation
------------------------------

We want to **choose a point  $x \in \mathbb{R}^n$ ** that **minimizes** the maximum value over all these affine functions.

This is a **minimax problem**:

*   Inner max: for any  $x$ , evaluates the worst-case cost among several linear functions.
*   Outer min: find the best  $x$  to minimize this worst-case cost.

This often appears in:

*   **Robust optimization**
*   **Worst-case loss minimization**
*   **Chebyshev approximation**
*   **Modeling uncertainty with multiple scenarios**

* * *

✅ Convexity Check
-----------------

Let’s rigorously verify convexity:

We define:

$$
f(x) = \max_{i} (a_i^T x + b_i)
$$

Each function  $f_i(x) = a_i^T x + b_i$  is affine ⇒ convex.

We invoke:

> If  $f_i$  are convex, then  $f(x) = \max_i f_i(x)$  is convex.

So,  $f$  is convex.

Hence, the full problem:

$$
\min_{x \in \mathbb{R}^n} f(x)
$$

is a **convex optimization problem**, although **nonsmooth**.

* * *

⚠️ Nonsmoothness: Why it matters
--------------------------------

Because of the  $\max$ , the objective is **not differentiable everywhere**. The nondifferentiability occurs at points where the maximum is attained by **more than one** affine function.

This means:

*   You cannot directly use gradient descent
*   Need to use **subgradient methods** or reformulate

That’s exactly what this exercise guides us to do — reformulate the problem into:

*   A **smooth approximation** (log-sum-exp),
*   An **LP** with slack variables,
*   Derive a **dual problem**,
*   Use tools from **duality** and **geometric programming**.

* * *

🔑 Summary of Step 0
--------------------

We now understand:

| Aspect | Explanation |
| --- | --- |
| Type of objective | Pointwise max of affine functions |
| Convexity? | ✅ Yes (max of convex is convex) |
| Smooth? | ❌ No (nondifferentiable where ties occur) |
| Why this is hard | Nonsmooth → standard gradient methods can't apply |
| Modeling interpretation | Worst-case cost, robust design |
| Optimization goal | Minimize the worst-case over  $m$  linear costs |

* * *

✅ Next Step: Step 1 (Part a)
----------------------------

> Derive a **dual problem**, based on the Lagrange dual of the equivalent epigraph form:

$$
\min_{x,y} \ y \quad \text{s.t.} \quad a_i^T x + b_i \le y \quad \forall i
$$

From there, derive:

*   Lagrangian
*   Dual function
*   Dual problem

* * *

Shall I proceed to **Step 1: Lagrange Dual derivation of part (a)**?

## Response:
Great — let's now begin **Step 1: Part (a)** of Exercise 5.7, and **derive the dual problem** via **Lagrangian duality**. We will go from first principles, extremely rigorously.

* * *

🔵 Step 1 — Exercise (a): Lagrange Dual of Equivalent Reformulation
===================================================================

* * *

📌 Original Problem (5.105)
---------------------------

We are minimizing the **maximum of affine functions**:

$$
\min_{x \in \mathbb{R}^n} \; \max_{i=1,\dots,m} \left( a_i^T x + b_i \right) \tag{5.105}
$$

This is convex but nonsmooth.

* * *

🎯 Goal of Step 1
-----------------

We want to **derive the Lagrange dual problem**, by:

1.  Reformulating the problem using an **auxiliary variable** (epigraph form),
2.  Writing the **Lagrangian**,
3.  Computing the **dual function**,
4.  Maximizing the dual function to obtain the **dual problem**,
5.  Understanding the interpretation and structure of the dual.

* * *

🔁 Step 1.1 — Reformulate (5.105) into an equivalent problem
------------------------------------------------------------

The key trick: turn the “max” into a constraint using an auxiliary scalar variable  $y$ .

We define the **epigraph formulation**:

$$
\begin{aligned} \min_{x, y} \quad & y \\ \text{s.t.} \quad & a_i^T x + b_i \le y, \quad i = 1, \dots, m \end{aligned} \tag{1}
$$

### ✅ Why this is equivalent

The constraint  $a_i^T x + b_i \le y \ \forall i$  means:

$$
\max_i (a_i^T x + b_i) \le y
$$

Then minimizing  $y$  is equivalent to minimizing the max. So this is **exactly equivalent** to (5.105), just written in a smoother format (which allows us to use duality).

* * *

🧮 Step 1.2 — Define Variables and Setup
----------------------------------------

Let’s be extremely clear:

*    $x \in \mathbb{R}^n$ : primal decision variable
*    $y \in \mathbb{R}$ : scalar upper bound on all affine expressions
*    $a_i \in \mathbb{R}^n, \ b_i \in \mathbb{R}$ : given data

So the **primal problem** becomes:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n, y \in \mathbb{R}} \quad & y \\ \text{s.t.} \quad & a_i^T x - y \le -b_i, \quad i = 1,\dots,m \end{aligned} \tag{P}
$$

Let’s now derive its Lagrange dual.

* * *

⚙️ Step 1.3 — Form Lagrangian
-----------------------------

We introduce **Lagrange multipliers**  $\lambda_i \ge 0$  for the inequality constraints:

$$
a_i^T x - y \le -b_i
$$

So:

*    $\lambda \in \mathbb{R}^m_+$ : one multiplier per constraint
*   Let’s write the Lagrangian  $\mathcal{L}(x, y, \lambda)$ 
    
$$
\begin{aligned} \mathcal{L}(x, y, \lambda) &= y + \sum_{i=1}^m \lambda_i \left( a_i^T x - y + b_i \right) \\ &= y + \sum_{i=1}^m \lambda_i a_i^T x - y \sum_{i=1}^m \lambda_i + \sum_{i=1}^m \lambda_i b_i \\ &= \left( 1 - \sum_{i=1}^m \lambda_i \right) y + \left( \sum_{i=1}^m \lambda_i a_i^T \right) x + \sum_{i=1}^m \lambda_i b_i \end{aligned}
$$

Let’s group this more cleanly:

$$
\mathcal{L}(x, y, \lambda) = \left(1 - \mathbf{1}^T \lambda \right)y + \lambda^T A x + \lambda^T b
$$

where:

*    $\mathbf{1}^T \lambda = \sum_i \lambda_i$ ,
*    $A \in \mathbb{R}^{m \times n}$ , with  $i$ \-th row  $a_i^T$ ,
*    $\lambda^T A x = \sum_i \lambda_i a_i^T x$ ,
*    $b \in \mathbb{R}^m$  collects  $b_i$ 

* * *

🧾 Step 1.4 — Dual Function
---------------------------

Now compute the **dual function**:

$$
g(\lambda) = \inf_{x, y} \ \mathcal{L}(x, y, \lambda)
$$

We split into two parts: minimization over  $y$  and over  $x$ .

* * *

### 🔸 Minimize over  $y \in \mathbb{R}$ :

$$
\inf_y \left(1 - \sum_i \lambda_i\right) y
$$

This is:

*    $-\infty$  if  $\sum_i \lambda_i \ne 1$ 
*    $0$  if  $\sum_i \lambda_i = 1$ 

So for the Lagrangian to be bounded below, we must have:

$$
\sum_i \lambda_i = 1 \tag{2}
$$

* * *

### 🔸 Minimize over  $x \in \mathbb{R}^n$ :

$$
\inf_x \left( \sum_i \lambda_i a_i^T \right) x = \inf_x \left( (\sum_i \lambda_i a_i)^T x \right)
$$

Again:

*    $= -\infty$  unless the coefficient is **zero vector**, i.e.:
    
$$
\sum_i \lambda_i a_i = 0 \tag{3}
$$

* * *

### ✅ So domain of dual function is:

$$
\begin{cases} \sum_i \lambda_i = 1 \\ \sum_i \lambda_i a_i = 0 \\ \lambda_i \ge 0 \quad \forall i \end{cases}
$$

* * *

🧮 Step 1.5 — Final Dual Function
---------------------------------

If constraints (2) and (3) are satisfied:

$$
g(\lambda) = \sum_i \lambda_i b_i = \lambda^T b
$$

Otherwise:  $g(\lambda) = -\infty$ 

* * *

🟣 Step 1.6 — Dual Problem (maximize the dual function)
-------------------------------------------------------

So the **dual problem** is:

$$
\begin{aligned} \max_{\lambda \in \mathbb{R}^m} \quad & \lambda^T b \\ \text{s.t.} \quad & \sum_{i=1}^m \lambda_i = 1 \\ & \sum_{i=1}^m \lambda_i a_i = 0 \\ & \lambda_i \ge 0, \quad i=1,\dots,m \end{aligned} \tag{D}
$$

Or compactly:

$$
\begin{aligned} \max_{\lambda \in \mathbb{R}^m_+} \quad & \lambda^T b \\ \text{s.t.} \quad & A^T \lambda = 0, \quad \mathbf{1}^T \lambda = 1 \end{aligned}
$$

* * *

🟩 Summary: Primal and Dual
---------------------------

| Primal (epigraph form) | Dual |
| --- | --- |
|  $\min_{x,y} \ y $  |  $\max_{\lambda} \ \lambda^T b$  |
|  $\text{s.t. } a_i^T x + b_i \le y$  |  $\sum_i \lambda_i = 1$  |
|  |  $\sum_i \lambda_i a_i = 0$  |
|  |  $\lambda_i \ge 0$  |

This is a standard structure in **robust optimization and LP duality** — the dual selects a worst-case affine function with minimal  $b_i$  offset, subject to equilibrium.

* * *

🔄 Next Step
------------

In Part (b), we:

*   Treat (5.105) as a **Linear Program** and derive its LP dual.
*   Then show it's **equivalent** to this dual we just derived.

* * *

Shall I proceed to **Step 2: Part (b) — LP reformulation and LP dual**?

## Response:
Part (b) — Formulate (5.105) as an LP, derive the LP dual, and relate it to part (a)
------------------------------------------------------------------------------------

We start from the original problem:

$$
\min_{x\in\mathbb R^n}\; \max_{i=1,\dots,m}(a_i^T x+b_i). \tag{5.105}
$$

### 1) LP formulation (the epigraph trick, done “the LP way”)

Introduce a scalar variable  $t\in\mathbb R$  that is supposed to be an upper bound on all the affine pieces  $a_i^T x+b_i$ . Enforcing “ $t$  is at least the maximum” is exactly the set of inequalities:

$$
a_i^T x + b_i \le t,\qquad i=1,\dots,m.
$$

Then minimizing the maximum becomes minimizing this upper bound:

$$
\begin{aligned} \min_{x\in\mathbb R^n,\; t\in\mathbb R}\quad & t\\ \text{s.t.}\quad & a_i^T x + b_i \le t,\quad i=1,\dots,m. \end{aligned} \tag{LP-P}
$$

This is a linear program: linear objective  $t$ , linear constraints.

Compact matrix form is useful for dual derivation. Let  $A\in\mathbb R^{m\times n}$  have rows  $a_i^T$ , let  $b\in\mathbb R^m$ , and let  $\mathbf 1\in\mathbb R^m$  be the all-ones vector. The constraints become

$$
Ax + b \le t\,\mathbf 1.
$$

So:

$$
\begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & Ax + b - t\mathbf 1 \le 0. \end{aligned} \tag{LP-P compact}
$$

* * *

### 2) Derive the LP dual (using the LP/Lagrangian route)

For each inequality constraint  $(Ax+b-t\mathbf 1)_i \le 0$ , introduce a dual variable  $\lambda_i \ge 0$ . Collect them in  $\lambda\in\mathbb R^m_+$ .

The Lagrangian is

$$
\begin{aligned} \mathcal L(x,t,\lambda) &= t + \lambda^T(Ax+b-t\mathbf 1)\\ &= t + \lambda^T Ax + \lambda^T b - t\,\lambda^T \mathbf 1\\ &= (1-\mathbf 1^T\lambda)\,t \;+\; (A^T\lambda)^T x \;+\; b^T\lambda. \end{aligned}
$$

Now form the dual function:

$$
g(\lambda)=\inf_{x,t}\mathcal L(x,t,\lambda).
$$

Minimize over  $t\in\mathbb R$ . The term involving  $t$  is  $(1-\mathbf 1^T\lambda)t$ . If its coefficient is nonzero, you can send  $t\to \pm\infty$  to make the Lagrangian  $-\infty$ . Therefore, for a finite infimum we must have

$$
\mathbf 1^T\lambda = 1. \tag{D1}
$$

Under (D1), the  $t$ \-term disappears.

Minimize over  $x\in\mathbb R^n$ . The remaining  $x$ \-term is  $(A^T\lambda)^T x$ . Same logic: unless  $A^T\lambda=0$ , we can drive it to  $-\infty$  by moving  $x$  along a direction that makes  $(A^T\lambda)^T x$  arbitrarily negative. So we need

$$
A^T\lambda = 0. \tag{D2}
$$

If (D1)–(D2) hold (and  $\lambda\ge 0$  by construction), then the infimum over  $x,t$  equals just the constant term  $b^T\lambda$ . So

$$
g(\lambda)=b^T\lambda \quad \text{when } \lambda\succeq 0,\ \mathbf 1^T\lambda=1,\ A^T\lambda=0,
$$

and  $g(\lambda)=-\infty$  otherwise.

The dual problem is to maximize  $g(\lambda)$ :

$$
\begin{aligned} \max_{\lambda\in\mathbb R^m}\quad & b^T\lambda\\ \text{s.t.}\quad & A^T\lambda = 0,\\ & \mathbf 1^T\lambda = 1,\\ & \lambda \succeq 0. \end{aligned} \tag{LP-D}
$$

That is the LP dual.

* * *

### 3) Relationship to part (a): it’s the same dual

In part (a), you derived a dual (via an equivalent formulation) and got:

*    $\lambda_i\ge 0$ ,
*    $\sum_i \lambda_i = 1$ ,
*    $\sum_i \lambda_i a_i = 0$ ,
*   maximize  $\sum_i \lambda_i b_i$ .

Notice that  $\sum_i \lambda_i a_i = 0$  is exactly  $A^T\lambda=0$  (since  $A$ ’s rows are  $a_i^T$ ), and  $\sum_i \lambda_i=1$  is  $\mathbf 1^T\lambda=1$ . So (LP-D) matches part (a) exactly.

Conceptually: part (a) and part (b) are two ways of seeing the same geometry. The primal is an LP; its LP dual is precisely the Lagrange dual you found.

* * *

### 4) Bonus: what the dual variables mean (ties directly to “which affine pieces are active”)

From LP KKT/complementary slackness, at optimality  $(x^*,t^*,\lambda^*)$ :

*   Primal feasibility:  $a_i^T x^* + b_i \le t^*$ .
*   Dual feasibility:  $\lambda^*\ge 0,\ \mathbf 1^T\lambda^*=1,\ A^T\lambda^*=0$ .
*   Complementary slackness:
    $$
    \lambda_i^*\,\big(a_i^T x^* + b_i - t^*\big)=0\quad \forall i.
    $$

So any index with  $\lambda_i^*>0$  must satisfy  $a_i^T x^* + b_i = t^*$ , i.e. that affine function is actually “touching the max” at the optimum. The dual weights form a probability distribution over the active pieces, and  $A^T\lambda^*=0$  says their weighted average slope cancels out (a subgradient optimality condition in disguise).

Next in the exercise, part (c) will replace the nonsmooth max by log-sum-exp; the dual keeps the same constraints but adds an entropy term.

## Response:
Short answer: **yes — essentially**.  
Long answer (the important one): **yes, but with a very specific and meaningful shift in viewpoint**. Part (b) is not introducing new mathematics; it is **re-deriving the same dual from the LP viewpoint**, making explicit what was implicit in part (a).

Let me unpack this carefully and precisely, because this distinction matters a lot for intuition.

* * *

1) What part (a) was _really_ doing
-----------------------------------

In **part (a)**, you did something slightly unusual on purpose:

*   You rewrote the problem using _auxiliary variables_  $y_i$ ,
*   You kept the objective as  $\max_i y_i$ ,
*   You then took a **Lagrange dual of a nonsmooth objective**.

So part (a) was conceptually:

> “Let me attack the max directly using conjugacy / Lagrangian ideas.”

When you minimized over  $y$ , you implicitly used a deep fact:

$$
\inf_y \big(\max_i y_i - \lambda^T y\big) = \begin{cases} 0 & \lambda \in \Delta\\ -\infty & \text{otherwise} \end{cases}
$$

That step is **not LP duality** in the classical sense; it’s the **convex conjugate of the max function** showing up in disguise.

So part (a) is best viewed as:

*   a **convex analysis derivation**,
*   using epigraphs + conjugates,
*   with dual feasibility emerging from boundedness conditions.

* * *

2) What part (b) is doing differently
-------------------------------------

In **part (b)**, the problem is rewritten as:

$$
\begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & a_i^T x + b_i \le t \quad \forall i \end{aligned}
$$

This is now:

*   explicitly a **linear program**,
*   in a form that any LP solver recognizes,
*   with **no max left anywhere**.

From here, everything follows from **standard LP duality rules**:

*   one dual variable per inequality,
*   dual feasibility = nonnegativity,
*   primal variables produce linear constraints in the dual,
*   objective coefficients swap roles.

So part (b) is conceptually:

> “Forget convex conjugates — treat this as a plain LP and write its LP dual.”

* * *

3) Why the duals come out identical
-----------------------------------

This is the key insight.

The two derivations **must** give the same dual, because:

*   the epigraph formulation in part (b) is _exactly_ the convex-optimization standard form of part (a),
*   LP duality is just a **special case** of Lagrange duality,
*   the feasible set and objective geometry are the same.

So when you compare the two duals:

$$
\begin{aligned} \max_{\lambda}\quad & b^T\lambda\\ \text{s.t.}\quad & A^T\lambda = 0,\\ & \mathbf 1^T\lambda = 1,\\ & \lambda \ge 0 \end{aligned}
$$

you see that:

*   the simplex constraint  $\mathbf 1^T\lambda=1$   
    ↔ came from minimizing over  $y$  in (a), and from minimizing over  $t$  in (b),
*   the equilibrium condition  $A^T\lambda=0$   
    ↔ came from minimizing over  $x$  in both,
*   nonnegativity  $\lambda\ge 0$   
    ↔ came from inequality constraints in both.

Different derivations, **same geometry**, same dual.

* * *

4) So what is the _real_ purpose of part (b)?
---------------------------------------------

Part (b) is not there to “do the same thing again” for fun. It is there to teach you **three deep lessons**:

### Lesson 1 — LP duality = Lagrange duality (in disguise)

What you derived abstractly in part (a) is exactly what LP duality produces automatically. No contradictions, no surprises.

### Lesson 2 — The max-of-affines problem _is_ an LP

Even though it doesn’t look like one at first glance, once you introduce  $t$ , it becomes a plain LP. This is why such problems are computationally easy.

### Lesson 3 — Dual variables identify active affine pieces

From the LP dual/KKT conditions, you immediately see:

*   which affine functions are tight at the optimum,
*   how their gradients combine to give a zero subgradient,
*   why  $\lambda$  lives in the simplex.

This interpretation is much harder to see from part (a) alone.

* * *

5) Precise answer in one sentence
---------------------------------

**Yes** — part (b) is _mathematically equivalent_ to part (a) and produces the same dual, but it is **not redundant**: it reframes the result as a classical LP dual, making the structure, interpretation, and computational meaning explicit.

* * *

Next, part (c) will change the game:  
we will **smooth** the max, keep the _same dual constraints_, and add an entropy term — revealing log-sum-exp as _entropy-regularized LP duality_.

## Response:
Part (c) is where the problem suddenly turns into something that looks like “machine learning math,” but it’s really just convex analysis wearing a hoodie. We replace the nonsmooth max by a smooth “soft-max,” derive a dual, and prove a clean approximation gap.

I’ll denote the original (piecewise-linear) objective by

$$
f_{\text{pl}}(x):=\max_{i=1,\dots,m}(a_i^T x+b_i), \qquad p_{\text{pl}}^*:=\min_x f_{\text{pl}}(x).
$$

And the smooth objective in part (c) by

$$
f_{\text{sm}}(x):=\log\!\Big(\sum_{i=1}^m e^{a_i^T x+b_i}\Big), \qquad p_{\text{sm}}^*:=\min_x f_{\text{sm}}(x).
$$

* * *

1) Why log-sum-exp is a “smooth max”
------------------------------------

Take any real numbers  $u_1,\dots,u_m$ . Define

$$
\operatorname{LSE}(u):=\log\Big(\sum_{i=1}^m e^{u_i}\Big).
$$

This is called log-sum-exp.

Key inequality (the one you’ll use forever):

$$
\max_i u_i \;\le\; \log\Big(\sum_{i=1}^m e^{u_i}\Big) \;\le\; \max_i u_i + \log m. \tag{★}
$$

Proof (fully explicit):  
Let  $M:=\max_i u_i$ . Then factor out  $e^M$ :

$$
\sum_{i=1}^m e^{u_i} = e^M \sum_{i=1}^m e^{u_i-M}.
$$

Now, because  $u_i-M\le 0$ , we have  $e^{u_i-M}\le 1$ . Also at least one index achieves the max, so for that index  $u_i-M=0$  and  $e^{u_i-M}=1$ . Therefore

$$
1 \le \sum_{i=1}^m e^{u_i-M} \le m.
$$

Take logs:

$$
0 \le \log\Big(\sum_{i=1}^m e^{u_i-M}\Big)\le \log m.
$$

Add  $M$  back (since  $\log(e^M \cdot S)=M+\log S$ ):

$$
M \le \log\Big(\sum_{i=1}^m e^{u_i}\Big)\le M+\log m.
$$

That’s (★).

Now apply this with

$$
u_i(x)=a_i^T x+b_i.
$$

Then (★) becomes, for every  $x$ :

$$
f_{\text{pl}}(x)\le f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m. \tag{1}
$$

So log-sum-exp is a smooth upper approximation to max, with a worst-case additive error  $\log m$ .

* * *

2) Derive the dual of the smooth problem
----------------------------------------

The smooth primal is:

$$
\min_{x\in\mathbb R^n}\; \log\Big(\sum_{i=1}^m e^{a_i^T x+b_i}\Big). \tag{5.106}
$$

There are two clean ways to get the dual. The most “Boyd-ish” way uses a famous variational identity: log-sum-exp is the convex conjugate of negative entropy. I’ll derive it enough that it doesn’t feel like magic.

### 2.1 A variational identity you need

For any vector  $u\in\mathbb R^m$ ,

$$
\log\Big(\sum_{i=1}^m e^{u_i}\Big) = \max_{\lambda\in\Delta}\left(\sum_{i=1}^m \lambda_i u_i - \sum_{i=1}^m \lambda_i\log\lambda_i\right), \tag{2}
$$

where  $\Delta=\{\lambda\in\mathbb R^m:\lambda\succeq 0,\ \mathbf 1^T\lambda=1\}$  is the probability simplex, and we interpret  $0\log 0:=0$ .

What (2) is saying: log-sum-exp is the best possible tradeoff between “pick large  $u_i$ ” and “don’t concentrate too hard” (the entropy term punishes extreme concentration).

Why (2) is true (a tight, self-contained argument):  
Fix  $u$ . Consider the optimization problem over  $\lambda\in\Delta$ :

$$
\max_{\lambda\in\Delta}\; \Phi(\lambda):=\lambda^T u - \sum_i \lambda_i\log\lambda_i.
$$

This is a concave maximization (linear minus convex entropy term). Use KKT.

Set up Lagrangian for constraints  $\sum_i\lambda_i=1$ ,  $\lambda_i\ge 0$ . For interior optimum ( $\lambda_i>0$ ), derivative condition:

$$
\frac{\partial}{\partial \lambda_i}\Big(\lambda^T u - \sum_j \lambda_j\log\lambda_j - \nu(\sum_j\lambda_j-1)\Big)=0
$$

gives

$$
u_i - (\log\lambda_i + 1) - \nu = 0 \quad\Rightarrow\quad \log\lambda_i = u_i - 1 - \nu \quad\Rightarrow\quad \lambda_i = C e^{u_i}
$$

for some constant  $C=e^{-1-\nu}$ .  
Enforce  $\sum_i\lambda_i=1$ :

$$
1=\sum_i\lambda_i = C\sum_i e^{u_i} \quad\Rightarrow\quad C=\frac{1}{\sum_i e^{u_i}}.
$$

So the maximizer is the softmax:

$$
\lambda_i^*=\frac{e^{u_i}}{\sum_j e^{u_j}}. \tag{3}
$$

Now evaluate  $\Phi(\lambda^*)$ . First compute  $\log\lambda_i^*$ :

$$
\log\lambda_i^* = u_i - \log\Big(\sum_j e^{u_j}\Big).
$$

Then

$$
\sum_i \lambda_i^*\log\lambda_i^* = \sum_i \lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big)\sum_i\lambda_i^* = \sum_i \lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big).
$$

Plug into  $\Phi$ :

$$
\Phi(\lambda^*) = \sum_i\lambda_i^* u_i - \left(\sum_i\lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big)\right) = \log\Big(\sum_j e^{u_j}\Big).
$$

So the maximum equals log-sum-exp, proving (2).

Good. Now we use it.

### 2.2 Plug  $u_i(x)=a_i^T x+b_i$  into the identity

Let  $u(x)=A x + b$ , where  $A\in\mathbb R^{m\times n}$  has rows  $a_i^T$ . Then

$$
f_{\text{sm}}(x)=\log\Big(\sum_i e^{u_i(x)}\Big) =\max_{\lambda\in\Delta}\left(\lambda^T(Ax+b)-\sum_i\lambda_i\log\lambda_i\right).
$$

Expand:

$$
\lambda^T(Ax+b)=\lambda^T Ax + \lambda^T b = x^T(A^T\lambda)+ b^T\lambda.
$$

So

$$
f_{\text{sm}}(x)=\max_{\lambda\in\Delta}\left(x^T(A^T\lambda)+ b^T\lambda - \sum_i\lambda_i\log\lambda_i\right). \tag{4}
$$

### 2.3 Turn the primal min over  $x$  into the dual max over  $\lambda$ 

The primal optimal value is

$$
p_{\text{sm}}^*=\min_x f_{\text{sm}}(x) =\min_x \max_{\lambda\in\Delta}\left(x^T(A^T\lambda)+ b^T\lambda - \sum_i\lambda_i\log\lambda_i\right).
$$

Under standard convexity/closedness conditions (which hold here), you can swap min and max (this is the saddle-point / strong duality logic for this unconstrained convex problem):

$$
p_{\text{sm}}^*=\max_{\lambda\in\Delta}\min_x \left(x^T(A^T\lambda)+ b^T\lambda - \sum_i\lambda_i\log\lambda_i\right). \tag{5}
$$

Now look at the inner minimization over  $x$ :

$$
\min_x x^T(A^T\lambda).
$$

This is exactly the same phenomenon as in parts (a)/(b):

*   If  $A^T\lambda\neq 0$ , the linear function  $x^T(A^T\lambda)$  can be made arbitrarily negative by sending  $x$  in the direction  $-A^T\lambda$ . So the minimum is  $-\infty$ .
*   If  $A^T\lambda=0$ , then  $x^T(A^T\lambda)=0$  for all  $x$ , so the minimum is  $0$ .

Therefore, the only  $\lambda$  that give a finite value satisfy:

$$
A^T\lambda=0. \tag{6}
$$

Under (6), the inner min over  $x$  drops out, leaving:

$$
p_{\text{sm}}^* = \max_{\lambda\in\Delta,\; A^T\lambda=0}\left(b^T\lambda - \sum_{i=1}^m \lambda_i\log\lambda_i\right). \tag{D-sm}
$$

So the dual of the smooth problem is:

$$
\begin{aligned} \max_{\lambda\in\mathbb R^m}\quad & b^T\lambda - \sum_{i=1}^m \lambda_i\log\lambda_i\\ \text{s.t.}\quad & A^T\lambda = 0,\\ & \mathbf 1^T\lambda = 1,\\ & \lambda \succeq 0. \end{aligned}
$$

Compare this to the dual of the original piecewise-linear/LP problem:

$$
\max_{\lambda\in\Delta,\;A^T\lambda=0} b^T\lambda.
$$

Same feasible set. The smooth dual adds an “entropy bonus”  $-\sum \lambda_i\log\lambda_i$  that encourages spreading  $\lambda$  out instead of putting all mass on a few indices. That is literally smoothing.

* * *

3) Prove the bound  $0 \le p_{\text{sm}}^* - p_{\text{pl}}^* \le \log m$ 
-------------------------------------------------------------------------

We already have the pointwise bound (1):

$$
f_{\text{pl}}(x)\le f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m\quad \forall x.
$$

Now translate pointwise bounds into optimal-value bounds.

First inequality:  
For all  $x$ ,  $f_{\text{pl}}(x)\le f_{\text{sm}}(x)$ .  
Take minimum over  $x$  on both sides:

$$
\min_x f_{\text{pl}}(x)\le \min_x f_{\text{sm}}(x) \quad\Rightarrow\quad p_{\text{pl}}^*\le p_{\text{sm}}^*.
$$

So

$$
0\le p_{\text{sm}}^*-p_{\text{pl}}^*.
$$

Second inequality:  
For all  $x$ ,  $f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m$ .  
Take minimum over  $x$  on both sides:

$$
\min_x f_{\text{sm}}(x)\le \min_x (f_{\text{pl}}(x)+\log m).
$$

But  $\log m$  is a constant independent of  $x$ , so

$$
\min_x (f_{\text{pl}}(x)+\log m)=\min_x f_{\text{pl}}(x)+\log m=p_{\text{pl}}^*+\log m.
$$

Therefore:

$$
p_{\text{sm}}^*\le p_{\text{pl}}^*+\log m \quad\Rightarrow\quad p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m.
$$

Combine both:

$$
0 \le p_{\text{sm}}^*-p_{\text{pl}}^* \le \log m.
$$

That completes part (c).

* * *

4) Tiny intuition that will help in part (d)
--------------------------------------------

The entropy term satisfies:

$$
0 \le -\sum_i \lambda_i\log\lambda_i \le \log m
$$

over the simplex (maximum entropy is uniform, giving  $\log m$ ). That’s why the “gap constant” is  $\log m$ . Part (d) will scale this by  $1/\gamma$ , shrinking the gap to  $(\log m)/\gamma$ .

If you keep one mental picture: smoothing the max is equivalent to adding an entropy regularizer in the dual, on exactly the same feasible set.

Next step is part (d), where we introduce  $\gamma$  and get the tighter bound  $(\log m)/\gamma$  and the limit  $\gamma\to\infty$  recovering the original max.

## Response:
Below is a single, self-contained, fully worked solution to the whole exercise (5.105)–(5.106): parts (a)–(d). I’ll be explicit about every transformation, every dual variable, and exactly where each constraint comes from.

* * *

Problem data and notation
-------------------------

*   Given vectors  $a_i\in\mathbb R^n$  and scalars  $b_i\in\mathbb R$ , for  $i=1,\dots,m$ .
*   Define the affine functions  $f_i(x)=a_i^T x+b_i$ .
*   Define the piecewise-linear convex function
    $$
    f_{\text{pl}}(x):=\max_{i=1,\dots,m}(a_i^T x+b_i).
    $$
*   Define the optimal value of the original problem:
    $$
    p_{\text{pl}}^*:=\inf_{x\in\mathbb R^n} f_{\text{pl}}(x).
    $$
    (I’ll write “ $\inf$ ” since existence of a minimizer depends on the data; the derivations do not require attainment.)

The primal problem is

$$
\boxed{ \text{(PL)}\quad \min_{x\in\mathbb R^n}\ \max_{i=1,\dots,m}(a_i^T x+b_i). } \tag{5.105}
$$

* * *

(a) Derive the dual via the Lagrange dual of an equivalent problem
==================================================================

### Step (a1): Introduce auxiliary variables  $y\in\mathbb R^m$ 

Consider the equivalent problem:

$$
\boxed{ \begin{aligned} \min_{x\in\mathbb R^n,\ y\in\mathbb R^m}\quad & \max_{i=1,\dots,m} y_i\\ \text{s.t.}\quad & y_i = a_i^T x + b_i,\quad i=1,\dots,m. \end{aligned}} \tag{E}
$$

**Why equivalent?**

*   Given any  $x$ , define  $y_i=a_i^T x+b_i$ . Then  $\max_i y_i=\max_i(a_i^T x+b_i)$ .
*   Any feasible  $(x,y)$  must satisfy  $y_i=a_i^T x+b_i$ , so its objective equals the original objective at that  $x$ .

So (E) has the same optimal value as (PL).

* * *

### Step (a2): Form the Lagrangian

Introduce multipliers  $\lambda\in\mathbb R^m$  for equality constraints  $a_i^T x+b_i-y_i=0$ .

Lagrangian:

$$
\mathcal L(x,y,\lambda) = \max_i y_i + \sum_{i=1}^m \lambda_i(a_i^T x+b_i-y_i).
$$

Group terms:

$$
\mathcal L(x,y,\lambda) = \underbrace{\big(\max_i y_i - \lambda^T y\big)}_{\text{depends on }y} \;+\;\underbrace{\Big(\sum_{i=1}^m \lambda_i a_i\Big)^T x}_{\text{depends on }x} \;+\; b^T\lambda.
$$

Let  $A=[a_1\ a_2\ \cdots\ a_m]\in\mathbb R^{n\times m}$ . Then  $\sum_i\lambda_i a_i=A\lambda$ . So:

$$
\mathcal L(x,y,\lambda)=\big(\max_i y_i-\lambda^T y\big)+(A\lambda)^T x + b^T\lambda.
$$

* * *

### Step (a3): Dual function  $g(\lambda)=\inf_{x,y}\mathcal L(x,y,\lambda)$ 

We take the infimum over  $x$  and  $y$  separately.

#### Infimum over  $x\in\mathbb R^n$ 

$$
\inf_{x}(A\lambda)^T x= \begin{cases} 0, & A\lambda=0,\\ -\infty, & A\lambda\neq 0. \end{cases}
$$

So to avoid  $-\infty$ , we must impose:

$$
\boxed{A\lambda=0.} \tag{A1}
$$

#### Infimum over  $y\in\mathbb R^m$ 

We need

$$
\inf_y \big(\max_i y_i - \lambda^T y\big).
$$

**Claim (key fact):**

$$
\inf_y(\max_i y_i-\lambda^T y)= \begin{cases} 0, & \lambda\succeq 0\ \text{and}\ \mathbf 1^T\lambda=1,\\ -\infty, & \text{otherwise}. \end{cases} \tag{A2}
$$

**Proof of the claim.**

1.  If  $\lambda\succeq 0$  and  $\mathbf 1^T\lambda=1$ : for any  $y$ ,
    
$$
\lambda^T y=\sum_i\lambda_i y_i \le \max_j y_j\sum_i\lambda_i=\max_j y_j,
$$

so  $\max_i y_i-\lambda^T y\ge 0$  for all  $y$ . Taking  $y=c\mathbf 1$  gives equality  $0$ . Hence infimum is  $0$ .

2.  If  $\mathbf 1^T\lambda\neq 1$ : take  $y=c\mathbf 1$ , then expression equals  $c(1-\mathbf 1^T\lambda)$ , which can be made  $-\infty$  by sending  $c\to\pm\infty$ . So infimum is  $-\infty$ .
3.  If some  $\lambda_k<0$ : take  $y_k=-t$ ,  $y_j=0$  for  $j\neq k$ . Then  $\max_i y_i=0$  and  $-\lambda^T y = -\lambda_k(-t)=\lambda_k t\to-\infty$  as  $t\to\infty$ . So infimum is  $-\infty$ .

So (A2) is proved.

Thus to avoid  $-\infty$  from the  $y$ \-infimum, we must impose:

$$
\boxed{\lambda\succeq 0,\qquad \mathbf 1^T\lambda=1.} \tag{A3}
$$

* * *

### Step (a4): Dual problem

Under (A1) and (A3), the infimum over  $x,y$  yields  $g(\lambda)=b^T\lambda$ . Therefore the dual is:

$$
\boxed{ \begin{aligned} \max_{\lambda\in\mathbb R^m}\quad & b^T\lambda\\ \text{s.t.}\quad & A\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{D\(_{\text{pl}}\)}
$$

This is the dual of the original piecewise-linear problem.

* * *

(b) Formulate (5.105) as an LP and derive its LP dual; relate to (a)
====================================================================

### Step (b1): Epigraph LP formulation

Introduce scalar  $t\in\mathbb R$  representing the maximum value. The constraint  $t\ge a_i^T x+b_i$  for all  $i$  is:

$$
a_i^T x+b_i \le t,\quad i=1,\dots,m.
$$

So the LP is:

$$
\boxed{ \begin{aligned} \min_{x,t}\quad & t\\ \text{s.t.}\quad & a_i^T x+b_i \le t,\quad i=1,\dots,m. \end{aligned}} \tag{LP-P}
$$

This LP is exactly equivalent to (5.105).

In matrix form with  $A\in\mathbb R^{m\times n}$  having rows  $a_i^T$ , constraints are  $Ax+b\le t\mathbf 1$ .

* * *

### Step (b2): LP dual via Lagrangian

Let  $\lambda\succeq 0$  be multipliers for constraints  $Ax+b-t\mathbf 1\le 0$ .

Lagrangian:

$$
\mathcal L(x,t,\lambda)= t + \lambda^T(Ax+b-t\mathbf 1) = (1-\mathbf 1^T\lambda)t + (A^T\lambda)^T x + b^T\lambda.
$$

Dual function  $g(\lambda)=\inf_{x,t}\mathcal L(x,t,\lambda)$  is finite only if:

*   Minimizing over  $t$  requires  $1-\mathbf 1^T\lambda=0\Rightarrow \mathbf 1^T\lambda=1$ .
*   Minimizing over  $x$  requires  $A^T\lambda=0$ .

Under these constraints,  $g(\lambda)=b^T\lambda$ . So the dual is:

$$
\boxed{ \begin{aligned} \max_{\lambda}\quad & b^T\lambda\\ \text{s.t.}\quad & A^T\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{LP-D}
$$

This is the same as (D $_{\text{pl}}$ ); the difference between  $A\lambda=0$  vs  $A^T\lambda=0$  is just which orientation you chose for  $A$  (columns vs rows). With rows  $a_i^T$ , the correct compact form is  $A^T\lambda=0$ . With columns  $a_i$ , it’s  $A\lambda=0$ . They are the same statement.

**Relationship to (a):** part (b) shows the problem is an LP; LP duality reproduces exactly the Lagrange dual found in (a).

* * *

(c) Smooth approximation, its dual, and prove  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 
================================================================================================

Define the smooth objective (log-sum-exp):

$$
f_{\text{sm}}(x):=\log\Big(\sum_{i=1}^m e^{a_i^T x+b_i}\Big),
$$

and the smooth problem:

$$
\boxed{ \text{(SM)}\quad \min_{x\in\mathbb R^n}\ \log\Big(\sum_{i=1}^m e^{a_i^T x+b_i}\Big). } \tag{5.106}
$$

Let  $p_{\text{sm}}^*:=\inf_x f_{\text{sm}}(x)$ .

* * *

(c1) Dual of the smooth problem
-------------------------------

### Step (c1.1): Variational representation of log-sum-exp

For any  $u\in\mathbb R^m$ ,

$$
\log\Big(\sum_{i=1}^m e^{u_i}\Big) = \max_{\lambda\in\Delta}\left(\lambda^T u - \sum_{i=1}^m \lambda_i\log\lambda_i\right), \tag{C1}
$$

where  $\Delta=\{\lambda\succeq 0,\ \mathbf 1^T\lambda=1\}$ .

(We proved this earlier via KKT; the maximizer is  $\lambda_i=\frac{e^{u_i}}{\sum_j e^{u_j}}$ .)

Now set  $u(x)=(a_1^T x+b_1,\dots,a_m^T x+b_m)=Ax+b$ . Then:

$$
f_{\text{sm}}(x)=\max_{\lambda\in\Delta}\left(\lambda^T(Ax+b)-\sum_i\lambda_i\log\lambda_i\right) =\max_{\lambda\in\Delta}\left(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\right).
$$

### Step (c1.2): Swap min and max and eliminate  $x$ 

$$
p_{\text{sm}}^*=\min_x f_{\text{sm}}(x) =\min_x\max_{\lambda\in\Delta}\Big(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\Big).
$$

Because this is a convex–concave saddle structure (convex in  $x$ , concave in  $\lambda$  over a compact convex set  $\Delta$ ), we can swap min and max (standard minimax theorem conditions hold here):

$$
p_{\text{sm}}^*=\max_{\lambda\in\Delta}\min_x\Big(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\Big).
$$

For fixed  $\lambda$ , the inner term is linear in  $x$ :  $\min_x x^T(A^T\lambda)$  is finite iff  $A^T\lambda=0$ ; otherwise it is  $-\infty$ . Therefore the dual feasible set includes  $A^T\lambda=0$ , and under that constraint the inner minimum equals  $0$ .

So the smooth dual is:

$$
\boxed{ \begin{aligned} \max_{\lambda}\quad & b^T\lambda-\sum_{i=1}^m \lambda_i\log\lambda_i\\ \text{s.t.}\quad & A^T\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{D\(_{\text{sm}}\)}
$$

**Interpretation:** same feasible set as the piecewise-linear dual, but with an added “entropy bonus”  $-\sum \lambda_i\log\lambda_i$  that smooths the solution.

* * *

(c2) Prove  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 
-------------------------------------------------------------

We use the pointwise inequality for any  $u\in\mathbb R^m$ :

$$
\max_i u_i \le \log\Big(\sum_i e^{u_i}\Big)\le \max_i u_i + \log m. \tag{C2}
$$

**Proof of (C2):** Let  $M=\max_i u_i$ . Then

$$
\sum_i e^{u_i}=e^M\sum_i e^{u_i-M},
$$

and  $1\le \sum_i e^{u_i-M}\le m$ . Taking log gives  $M\le \log\sum_i e^{u_i}\le M+\log m$ .

Now apply (C2) with  $u_i=a_i^T x+b_i$ . For every  $x$ :

$$
f_{\text{pl}}(x)\le f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m. \tag{C3}
$$

Take infimum over  $x$  in (C3):

*   Left inequality gives  $p_{\text{pl}}^*\le p_{\text{sm}}^*$ .
*   Right inequality gives  $p_{\text{sm}}^*\le p_{\text{pl}}^*+\log m$ .

Thus:

$$
\boxed{0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m.}
$$

* * *

(d) General smoothing parameter  $\gamma>0$ : derive bound and limit behavior
=============================================================================

Define the  $\gamma$ \-scaled smooth approximation:

$$
f_\gamma(x):=\frac{1}{\gamma}\log\Big(\sum_{i=1}^m \exp(\gamma(a_i^T x+b_i))\Big), \qquad \gamma>0.
$$

Let

$$
p_\gamma^*:=\inf_x f_\gamma(x).
$$

* * *

(d1) Pointwise approximation bound
----------------------------------

For any  $u\in\mathbb R^m$ , apply (C2) to the vector  $\gamma u$ :

$$
\max_i (\gamma u_i)\le \log\Big(\sum_i e^{\gamma u_i}\Big)\le \max_i (\gamma u_i)+\log m.
$$

Divide by  $\gamma>0$ :

$$
\max_i u_i \le \frac{1}{\gamma}\log\Big(\sum_i e^{\gamma u_i}\Big)\le \max_i u_i + \frac{\log m}{\gamma}. \tag{D1}
$$

Now set  $u_i(x)=a_i^T x+b_i$ . Then for all  $x$ :

$$
f_{\text{pl}}(x)\le f_\gamma(x)\le f_{\text{pl}}(x)+\frac{\log m}{\gamma}. \tag{D2}
$$

* * *

(d2) Optimal-value bound
------------------------

Take infimum over  $x$  in (D2):

*   From  $f_{\text{pl}}(x)\le f_\gamma(x)$  for all  $x$ , we get
    $$
    p_{\text{pl}}^*\le p_\gamma^*.
    $$
*   From  $f_\gamma(x)\le f_{\text{pl}}(x)+\frac{\log m}{\gamma}$  for all  $x$ , we get
    $$
    p_\gamma^*\le p_{\text{pl}}^*+\frac{\log m}{\gamma}.
    $$

So:

$$
\boxed{ 0\le p_\gamma^*-p_{\text{pl}}^*\le \frac{\log m}{\gamma}. } \tag{D3}
$$

* * *

(d3) What happens as  $\gamma\to\infty$ ?
-----------------------------------------

From (D3), the gap is squeezed:

$$
0\le p_\gamma^*-p_{\text{pl}}^*\le \frac{\log m}{\gamma}\xrightarrow[\gamma\to\infty]{}0.
$$

Therefore:

$$
\boxed{p_\gamma^*\downarrow p_{\text{pl}}^*\quad \text{as }\gamma\to\infty.}
$$

Also pointwise, from (D2):

$$
f_\gamma(x)\downarrow f_{\text{pl}}(x)\quad \text{for each fixed }x.
$$

So increasing  $\gamma$  makes the approximation tighter (less smoothing).

* * *

Final collected answers (clean “exam-style” statements)
=======================================================

1.  **(a) Dual of (5.105):**
    
$$
\boxed{ \max_{\lambda\succeq 0}\ b^T\lambda \quad\text{s.t.}\quad A^T\lambda=0,\ \mathbf 1^T\lambda=1. }
$$
2.  **(b) LP formulation and LP dual:**

Primal LP:

$$
\boxed{ \min_{x,t}\ t\ \ \text{s.t.}\ \ a_i^T x+b_i\le t,\ i=1,\dots,m. }
$$

Dual LP (same as in (a)):

$$
\boxed{ \max_{\lambda\succeq 0}\ b^T\lambda \quad\text{s.t.}\quad A^T\lambda=0,\ \mathbf 1^T\lambda=1. }
$$
3.  **(c) Smooth problem dual and bound:**

Smooth primal:

$$
\boxed{ \min_x\ \log\Big(\sum_{i=1}^m e^{a_i^T x+b_i}\Big). }
$$

Dual:

$$
\boxed{ \max_{\lambda\succeq 0}\ \Big(b^T\lambda-\sum_{i=1}^m \lambda_i\log\lambda_i\Big) \ \ \text{s.t.}\ \ A^T\lambda=0,\ \mathbf 1^T\lambda=1. }
$$

Optimal value gap:

$$
\boxed{ 0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m. }
$$
4.  **(d)  $\gamma$ \-scaled approximation bound and limit:**
    
$$
\boxed{ f_\gamma(x)=\frac{1}{\gamma}\log\Big(\sum_{i=1}^m e^{\gamma(a_i^T x+b_i)}\Big) }
$$

and

$$
\boxed{ 0\le p_\gamma^*-p_{\text{pl}}^*\le \frac{\log m}{\gamma}, \qquad p_\gamma^*\to p_{\text{pl}}^* \text{ as }\gamma\to\infty. }
$$

That’s the full, detailed, rigorous solution.

## Response:
Alright — let’s crank the microscope up. I’ll rewrite the entire solution with (i) more first-principles definitions, (ii) every equivalence justified, (iii) every “bounded below implies constraint” step proved cleanly, (iv) the minimax swap and entropy identity derived in full, and (v) the geometry/KKT interpretation made explicit so you can _see_ why the dual constraints are what they are.

I’ll keep the same structure (a)–(d), but each part will be “zero-to-hero”.

* * *

0) Preliminaries: what objects we’re manipulating
=================================================

0.1 Data and variables
----------------------

*   Decision variable:  $x \in \mathbb{R}^n$ .
*   Given data:  $a_i \in \mathbb{R}^n$ ,  $b_i \in \mathbb{R}$  for  $i=1,\dots,m$ .

Define affine functions

$$
f_i(x) := a_i^T x + b_i.
$$

Define their pointwise maximum:

$$
f_{\text{pl}}(x) := \max_{i=1,\dots,m} f_i(x) = \max_i (a_i^T x + b_i).
$$

The primal optimal value is

$$
p_{\text{pl}}^* := \inf_{x\in \mathbb{R}^n} f_{\text{pl}}(x).
$$

(Using  $\inf$  is the mathematically safe version; the minimum may or may not be attained depending on whether  $f_{\text{pl}}(x)\to -\infty$  along some direction, etc.)

* * *

0.2 Why the objective is convex (fully justified)
-------------------------------------------------

Each  $f_i(x)$  is affine, hence convex. The pointwise maximum of convex functions is convex:

**Claim:** If  $g_i$  are convex, then  $g(x):=\max_i g_i(x)$  is convex.

**Proof:** For any  $x,y$  and  $\theta\in[0,1]$ ,

$$
g(\theta x+(1-\theta)y)=\max_i g_i(\theta x+(1-\theta)y) \le \max_i \big(\theta g_i(x)+(1-\theta)g_i(y)\big) \le \theta \max_i g_i(x) + (1-\theta)\max_i g_i(y) = \theta g(x)+(1-\theta)g(y).
$$

So  $g$  is convex. ∎

So (5.105) is a convex optimization problem, but nonsmooth because max creates “kinks”.

* * *

The problem
===========

$$
\boxed{ \text{(PL)}\quad \min_{x\in\mathbb R^n}\ \max_{i=1,\dots,m}(a_i^T x+b_i). } \tag{5.105}
$$

* * *

(a) Derive a dual by taking the Lagrange dual of an equivalent problem
======================================================================

The book’s part (a) takes a slightly less standard equivalent formulation to expose the conjugacy of the max.

(a1) Equivalent reformulation with  $y\in\mathbb R^m$ 
------------------------------------------------------

Consider

$$
\boxed{ \begin{aligned} \min_{x\in\mathbb R^n,\ y\in\mathbb R^m}\quad & \max_{i=1,\dots,m} y_i\\ \text{s.t.}\quad & y_i = a_i^T x + b_i,\quad i=1,\dots,m. \end{aligned}} \tag{E}
$$

### Why exactly equivalent to (PL)

*   Given any  $x$ , define  $y = (a_1^T x+b_1,\dots,a_m^T x+b_m)$ . Then constraints hold and objective equals  $\max_i (a_i^T x+b_i)$ .
*   Conversely any feasible  $(x,y)$  satisfies  $y_i=a_i^T x+b_i$ , so objective  $\max_i y_i = \max_i(a_i^T x+b_i)$ .

Thus feasible  $x$ ’s correspond 1-to-1 and objective values match. So optimal values match.

* * *

(a2) Write the Lagrangian
-------------------------

Equality constraints:

$$
a_i^T x + b_i - y_i = 0,\quad i=1,\dots,m.
$$

Introduce multipliers  $\lambda\in\mathbb R^m$  (no sign restriction for equality constraints). The Lagrangian:

$$
\mathcal L(x,y,\lambda) = \max_i y_i + \sum_{i=1}^m \lambda_i(a_i^T x + b_i - y_i).
$$

Rearrange:

$$
\mathcal L(x,y,\lambda) = \underbrace{\Big(\max_i y_i - \lambda^T y\Big)}_{\text{depends on }y} \;+\;\underbrace{\Big(\sum_{i=1}^m \lambda_i a_i\Big)^T x}_{\text{depends on }x} \;+\; b^T\lambda.
$$

Let  $A=[a_1\ \cdots\ a_m]\in\mathbb R^{n\times m}$ . Then  $\sum_i \lambda_i a_i = A\lambda$ . So

$$
\mathcal L(x,y,\lambda)=\big(\max_i y_i - \lambda^T y\big) + (A\lambda)^T x + b^T\lambda.
$$

* * *

(a3) Dual function  $g(\lambda)=\inf_{x,y}\mathcal L(x,y,\lambda)$ 
-------------------------------------------------------------------

We compute the infimum over  $x$  and  $y$  separately because they appear in separable terms.

### Step 1: inf over  $x\in\mathbb R^n$ 

We need

$$
\inf_{x\in\mathbb R^n} (A\lambda)^T x.
$$

**Fact:** For a fixed vector  $c$ ,

$$
\inf_{x} c^T x= \begin{cases} 0, & c=0,\\ -\infty, & c\neq 0. \end{cases}
$$

**Proof:** If  $c\neq 0$ , take  $x=-t c$  with  $t\to+\infty$ . Then  $c^T x=-t\|c\|^2\to -\infty$ . If  $c=0$ , then  $c^T x=0$  always. ∎

Apply with  $c=A\lambda$ . So finiteness requires:

$$
\boxed{A\lambda=0.} \tag{A1}
$$

Under this condition, the inf over  $x$  contributes  $0$ .

* * *

### Step 2: inf over  $y\in\mathbb R^m$ 

We need

$$
\inf_{y\in\mathbb R^m}\ \big(\max_i y_i - \lambda^T y\big). \tag{Y}
$$

This is where the simplex constraint comes from.

#### Claim:

$$
\inf_{y}\big(\max_i y_i - \lambda^T y\big)= \begin{cases} 0, & \lambda\succeq 0,\ \mathbf 1^T\lambda=1,\\ -\infty, & \text{otherwise}. \end{cases} \tag{A2}
$$

I’ll prove each direction cleanly.

##### (i) If  $\lambda\succeq 0$  and  $\mathbf 1^T\lambda=1$ , then infimum is  $0$ 

For any  $y$ ,

$$
\lambda^T y=\sum_i \lambda_i y_i \le \sum_i \lambda_i \max_j y_j = (\mathbf 1^T\lambda)\max_j y_j = \max_j y_j,
$$

since each  $y_i\le \max_j y_j$  and  $\lambda_i\ge 0$ .

So

$$
\max_i y_i - \lambda^T y \ge 0 \quad \forall y.
$$

Therefore the infimum is  $\ge 0$ .

Now choose  $y=c\mathbf 1$  (all coordinates equal). Then  $\max_i y_i=c$ , and  $\lambda^T y=c(\mathbf 1^T\lambda)=c$ . So the expression equals  $0$ . Hence the infimum is exactly  $0$ .

##### (ii) If  $\mathbf 1^T\lambda\neq 1$ , then infimum is  $-\infty$ 

Pick again  $y=c\mathbf 1$ . Then

$$
\max_i y_i - \lambda^T y = c - c(\mathbf 1^T\lambda) = c(1-\mathbf 1^T\lambda).
$$

If  $1-\mathbf 1^T\lambda>0$ , send  $c\to -\infty$ . If  $1-\mathbf 1^T\lambda<0$ , send  $c\to +\infty$ . In either case the expression  $\to -\infty$ . So the infimum is  $-\infty$ .

##### (iii) If some  $\lambda_k<0$ , then infimum is  $-\infty$ 

Choose  $y_k=-t$  and all other  $y_j=0$ . Then  $\max_i y_i=0$ . Also

$$
-\lambda^T y = -(\lambda_k(-t)+0)=\lambda_k t.
$$

Since  $\lambda_k<0$ ,  $\lambda_k t\to -\infty$  as  $t\to+\infty$ . So the expression  $\to -\infty$ , hence infimum is  $-\infty$ .

This proves the claim (A2).

So finiteness of the  $y$ \-infimum requires:

$$
\boxed{\lambda\succeq 0,\qquad \mathbf 1^T\lambda=1.} \tag{A3}
$$

* * *

### Step 3: assemble  $g(\lambda)$ 

If (A1) and (A3) hold, then

$$
g(\lambda)=b^T\lambda + 0 + 0 = b^T\lambda.
$$

Otherwise  $g(\lambda)=-\infty$ .

* * *

(a4) The dual problem
---------------------

The dual is maximize the dual function:

$$
\boxed{ \begin{aligned} \max_{\lambda\in\mathbb R^m}\quad & b^T\lambda\\ \text{s.t.}\quad & A\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{D\(_{\text{pl}}\)}
$$

Interpretation:  $\lambda$  is a probability vector (simplex constraints) such that the weighted average direction of the  $a_i$ ’s equals zero ( $A\lambda=0$ ).

* * *

(b) LP formulation + LP dual + relationship to (a)
==================================================

Part (b) is the “standard epigraph LP route”.

(b1) LP epigraph reformulation
------------------------------

Introduce  $t\in\mathbb R$  such that  $t\ge a_i^T x+b_i$  for all  $i$ . Then

$$
t \ge \max_i (a_i^T x+b_i).
$$

Minimizing the max is equivalent to minimizing such a  $t$ .

So the LP is:

$$
\boxed{ \begin{aligned} \min_{x\in\mathbb R^n,\ t\in\mathbb R}\quad & t\\ \text{s.t.}\quad & a_i^T x+b_i \le t,\quad i=1,\dots,m. \end{aligned}} \tag{LP-P}
$$

This is literally a linear program: objective linear, constraints linear.

### Equivalent proof (formal)

Define feasible set

$$
\mathcal F:=\{(x,t): a_i^T x+b_i\le t,\ \forall i\}.
$$

For any  $x$ , the smallest  $t$  that makes  $(x,t)$  feasible is  $t=\max_i(a_i^T x+b_i)$ . Therefore minimizing  $t$  over  $\mathcal F$  equals minimizing  $\max_i(a_i^T x+b_i)$  over  $x$ . ∎

* * *

(b2) Derive LP dual via Lagrangian (fully explicit)
---------------------------------------------------

Let’s stack constraints as

$$
a_i^T x+b_i - t \le 0.
$$

Introduce multipliers  $\lambda_i\ge 0$  for each inequality;  $\lambda\in\mathbb R^m_+$ .

Lagrangian:

$$
\mathcal L(x,t,\lambda)= t + \sum_{i=1}^m \lambda_i(a_i^T x+b_i - t).
$$

Expand and regroup:

$$
\mathcal L(x,t,\lambda)= t\Big(1-\sum_{i=1}^m \lambda_i\Big) + \Big(\sum_{i=1}^m \lambda_i a_i\Big)^T x + \sum_{i=1}^m \lambda_i b_i.
$$

In matrix form with  $A=[a_1\ \cdots\ a_m]$  (columns):

$$
\mathcal L(x,t,\lambda)= (1-\mathbf 1^T\lambda)t + (A\lambda)^T x + b^T\lambda.
$$

Now compute dual function

$$
g(\lambda)=\inf_{x,t}\mathcal L(x,t,\lambda).
$$

### Inf over  $t\in\mathbb R$ 

If  $1-\mathbf 1^T\lambda \neq 0$ , then the linear function in  $t$  can be driven to  $-\infty$  by choosing  $t\to \pm\infty$ . Hence finiteness requires

$$
\boxed{\mathbf 1^T\lambda=1.} \tag{B1}
$$

### Inf over  $x\in\mathbb R^n$ 

Similarly, finiteness requires the coefficient of  $x$  to be zero:

$$
\boxed{A\lambda=0.} \tag{B2}
$$

If (B1) and (B2) hold, then the infimum over  $x,t$  equals  $b^T\lambda$ . So the dual is:

$$
\boxed{ \begin{aligned} \max_{\lambda}\quad & b^T\lambda\\ \text{s.t.}\quad & A\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{LP-D}
$$

Same dual as (a).

* * *

(b3) Relationship to part (a) (what is “really” the same)
---------------------------------------------------------

*   In (a), simplex constraints came from minimizing  $\max_i y_i - \lambda^T y$  (conjugate of max).
*   In (b), simplex constraints came from minimizing  $(1-\mathbf 1^T\lambda)t$  over free scalar  $t$ .

Same math in different clothing.

* * *

(b4) KKT interpretation (this is the “active planes” story)
-----------------------------------------------------------

For LP-P, KKT conditions (when strong duality holds and solutions exist) include:

1.  Primal feasibility:  $a_i^T x^*+b_i \le t^*$ .
2.  Dual feasibility:  $\lambda^*\ge 0$ ,  $\mathbf 1^T\lambda^*=1$ ,  $A\lambda^*=0$ .
3.  Complementary slackness:
    
$$
\lambda_i^*(a_i^T x^*+b_i-t^*)=0,\quad \forall i.
$$

So:

*   If  $\lambda_i^*>0$ , then  $a_i^T x^*+b_i=t^*$ : that plane is _active_ at the maximum.
*    $\lambda^*$  puts weight only on active planes (in general).
*    $A\lambda^*=0$  means the weighted average of the active slopes cancels — exactly the subgradient optimality condition  $0\in\partial f_{\text{pl}}(x^*)$ .

This is the geometric skeleton: at the optimum, you’re at a point where the “upper envelope” is supported by a set of planes whose slopes balance to zero.

* * *

(c) Smooth approximation: dual, and prove  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 
============================================================================================

Define

$$
f_{\text{sm}}(x):=\log\left(\sum_{i=1}^m \exp(a_i^T x+b_i)\right), \qquad p_{\text{sm}}^*:=\inf_x f_{\text{sm}}(x). \tag{5.106}
$$

This function is convex and smooth because:

*   each  $x\mapsto e^{a_i^T x+b_i}$  is convex,
*   sum preserves convexity,
*   log of sum of exponentials is convex (can be proved via Hessian or via the variational form below),
*   it’s differentiable everywhere.

* * *

(c1) The key inequality: log-sum-exp approximates max
-----------------------------------------------------

Let  $u_i\in\mathbb R$ . Let  $M=\max_i u_i$ .

Then

$$
\sum_i e^{u_i}=e^M\sum_i e^{u_i-M}.
$$

Since  $u_i-M\le 0$ , we have  $e^{u_i-M}\le 1$ . Also at least one term achieves  $u_i=M$ , giving one term equal to  $1$ . Thus:

$$
1 \le \sum_i e^{u_i-M} \le m.
$$

Take log:

$$
0 \le \log\left(\sum_i e^{u_i-M}\right)\le \log m.
$$

Add  $M$ :

$$
M \le \log\left(\sum_i e^{u_i}\right)\le M+\log m.
$$

So for all  $u$ :

$$
\boxed{ \max_i u_i \le \log\Big(\sum_i e^{u_i}\Big) \le \max_i u_i+\log m. } \tag{C-LSE}
$$

Now apply with  $u_i(x)=a_i^T x+b_i$ :

$$
\boxed{ f_{\text{pl}}(x)\le f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m,\quad \forall x. } \tag{C1}
$$

* * *

(c2) Derive the smooth dual (entropy regularization appears)
------------------------------------------------------------

### Step (c2.1): Prove the variational representation of log-sum-exp

We prove:

$$
\boxed{ \log\Big(\sum_{i=1}^m e^{u_i}\Big) = \max_{\lambda\in\Delta}\left(\lambda^T u - \sum_{i=1}^m \lambda_i\log\lambda_i\right), } \tag{C2}
$$

where  $\Delta=\{\lambda\succeq 0,\ \mathbf 1^T\lambda=1\}$ .

**Derivation via KKT (full):**

Consider

$$
\max_{\lambda\in\Delta}\ \Phi(\lambda):=\lambda^T u - \sum_i \lambda_i\log\lambda_i.
$$

This is concave because  $-\sum \lambda_i\log\lambda_i$  is concave on  $\Delta$ .

Form Lagrangian for constraint  $\sum_i\lambda_i=1$  with multiplier  $\nu$ :

$$
\mathcal J(\lambda,\nu) = \sum_i \lambda_i u_i - \sum_i \lambda_i\log\lambda_i - \nu\left(\sum_i\lambda_i-1\right).
$$

Take derivative w.r.t.  $\lambda_i$  (assuming interior optimum so  $\lambda_i>0$ ):

$$
\frac{\partial \mathcal J}{\partial \lambda_i} = u_i - (\log\lambda_i+1) - \nu = 0.
$$

So

$$
\log\lambda_i = u_i - 1 - \nu \quad\Rightarrow\quad \lambda_i = e^{u_i-1-\nu} = C e^{u_i}
$$

where  $C=e^{-1-\nu}$ .

Enforce  $\sum_i\lambda_i=1$ :

$$
1=\sum_i \lambda_i = C\sum_i e^{u_i} \quad\Rightarrow\quad C=\frac{1}{\sum_i e^{u_i}}.
$$

Thus the maximizer is

$$
\boxed{ \lambda_i^*=\frac{e^{u_i}}{\sum_j e^{u_j}}. } \tag{softmax}
$$

Now compute optimal value  $\Phi(\lambda^*)$ . Note:

$$
\log\lambda_i^* = u_i - \log\Big(\sum_j e^{u_j}\Big).
$$

Then

$$
\sum_i \lambda_i^*\log\lambda_i^* = \sum_i \lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big)\sum_i \lambda_i^* = \sum_i \lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big).
$$

Therefore

$$
\Phi(\lambda^*) = \sum_i \lambda_i^* u_i - \left(\sum_i \lambda_i^* u_i - \log\Big(\sum_j e^{u_j}\Big)\right) = \log\Big(\sum_j e^{u_j}\Big).
$$

So the max equals log-sum-exp. Done.

* * *

### Step (c2.2): Apply with  $u(x)=Ax+b$ 

Let  $A\in\mathbb R^{m\times n}$  have rows  $a_i^T$ , so  $u(x)=Ax+b$  is in  $\mathbb R^m$ .

Then

$$
f_{\text{sm}}(x)=\log\Big(\sum_i e^{(Ax+b)_i}\Big) = \max_{\lambda\in\Delta}\left(\lambda^T(Ax+b)-\sum_i \lambda_i\log\lambda_i\right).
$$

Expand:

$$
\lambda^T(Ax+b)=\lambda^T Ax + \lambda^T b = x^T(A^T\lambda)+b^T\lambda.
$$

So:

$$
f_{\text{sm}}(x)=\max_{\lambda\in\Delta}\left(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\right). \tag{C3}
$$

### Step (c2.3): Take  $\inf_x$  and get the dual constraint  $A^T\lambda=0$ 

Now:

$$
p_{\text{sm}}^*=\inf_x f_{\text{sm}}(x) =\inf_x \max_{\lambda\in\Delta}\Big(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\Big).
$$

We want to swap inf and max. Here’s the safe way to see it without handwaving:

*   Define  $\psi(x,\lambda)=x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i$ .
*   For fixed  $\lambda$ ,  $\psi(\cdot,\lambda)$  is affine in  $x$ , hence convex.
*   For fixed  $x$ ,  $\psi(x,\cdot)$  is concave in  $\lambda$  on  $\Delta$  (linear minus convex).
*    $\Delta$  is compact convex.  
    These conditions are enough for a standard minimax theorem (Sion’s theorem) to justify:
    
$$
\inf_x \max_{\lambda\in\Delta}\psi(x,\lambda)=\max_{\lambda\in\Delta}\inf_x \psi(x,\lambda).
$$

So:

$$
p_{\text{sm}}^*=\max_{\lambda\in\Delta}\inf_x \Big(x^T(A^T\lambda)+b^T\lambda-\sum_i\lambda_i\log\lambda_i\Big).
$$

Now focus on the inner  $\inf_x$ . The only  $x$ \-dependent piece is  $x^T(A^T\lambda)$ . As in parts (a)/(b):

$$
\inf_x x^T(A^T\lambda)= \begin{cases} 0, & A^T\lambda=0,\\ -\infty, & A^T\lambda\neq 0. \end{cases}
$$

Thus finite dual value requires:

$$
\boxed{A^T\lambda=0.} \tag{C4}
$$

Under this constraint, the  $\inf_x$  drops out and equals  $0$ , leaving:

$$
\boxed{ \begin{aligned} \max_{\lambda}\quad & b^T\lambda-\sum_{i=1}^m \lambda_i\log\lambda_i\\ \text{s.t.}\quad & A^T\lambda=0,\\ & \mathbf 1^T\lambda=1,\\ & \lambda\succeq 0. \end{aligned}} \tag{D\(_{\text{sm}}\)}
$$

This is the smooth dual.

**Comparison to piecewise-linear dual:** identical feasible set, plus an extra entropy term  $-\sum \lambda_i\log\lambda_i$ . That entropy term is exactly the smoothing regularizer.

* * *

(c3) Prove the optimal value gap:  $0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m$ 
------------------------------------------------------------------------------------

From (C1), for all  $x$ :

$$
f_{\text{pl}}(x)\le f_{\text{sm}}(x)\le f_{\text{pl}}(x)+\log m.
$$

Take  $\inf_x$  of each side:

*   Left inequality:
    $$
    \inf_x f_{\text{pl}}(x)\le \inf_x f_{\text{sm}}(x) \quad\Rightarrow\quad p_{\text{pl}}^*\le p_{\text{sm}}^*.
    $$
*   Right inequality:
    $$
    \inf_x f_{\text{sm}}(x)\le \inf_x (f_{\text{pl}}(x)+\log m) = \inf_x f_{\text{pl}}(x)+\log m = p_{\text{pl}}^*+\log m.
    $$

So:

$$
\boxed{ 0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m. }
$$

That completes (c).

* * *

(d) The  $\gamma$ \-family: tighter approximation and convergence
=================================================================

Define for  $\gamma>0$ :

$$
f_\gamma(x):=\frac{1}{\gamma}\log\Big(\sum_{i=1}^m \exp(\gamma(a_i^T x+b_i))\Big), \qquad p_\gamma^*:=\inf_x f_\gamma(x).
$$

This is the “temperature” parameter: as  $\gamma$  grows, softmax becomes closer to max.

* * *

(d1) Pointwise bound: max vs  $f_\gamma$ 
-----------------------------------------

Apply the log-sum-exp inequality (C-LSE) to the numbers  $\gamma u_i$ :

For any  $u$ ,

$$
\max_i (\gamma u_i)\le \log\Big(\sum_i e^{\gamma u_i}\Big)\le \max_i (\gamma u_i)+\log m.
$$

Divide by  $\gamma>0$ :

$$
\max_i u_i \le \frac{1}{\gamma}\log\Big(\sum_i e^{\gamma u_i}\Big)\le \max_i u_i + \frac{\log m}{\gamma}.
$$

Now set  $u_i(x)=a_i^T x+b_i$ :

$$
\boxed{ f_{\text{pl}}(x)\le f_\gamma(x)\le f_{\text{pl}}(x)+\frac{\log m}{\gamma}\quad \forall x. } \tag{D1}
$$

* * *

(d2) Optimal value bound
------------------------

Take  $\inf_x$  of (D1):

*   Lower:
    $$
    p_{\text{pl}}^* \le p_\gamma^*.
    $$
*   Upper:
    $$
    p_\gamma^* \le p_{\text{pl}}^*+\frac{\log m}{\gamma}.
    $$

Hence:

$$
\boxed{ 0\le p_\gamma^*-p_{\text{pl}}^*\le \frac{\log m}{\gamma}. } \tag{D2}
$$

* * *

(d3) Convergence as  $\gamma\to\infty$ 
---------------------------------------

Since  $(\log m)/\gamma \to 0$ , the squeeze (D2) implies:

$$
\boxed{ p_\gamma^*\to p_{\text{pl}}^*\quad \text{as }\gamma\to\infty. }
$$

Also for each fixed  $x$ , (D1) shows  $f_\gamma(x)\downarrow f_{\text{pl}}(x)$ .

* * *

Final “one-page” summary of all answers
=======================================

Primal (5.105)
--------------

$$
\min_x \max_i (a_i^T x+b_i).
$$

LP reformulation
----------------

$$
\min_{x,t} t \quad \text{s.t. } a_i^T x+b_i\le t.
$$

Dual of piecewise-linear/LP problem
-----------------------------------

$$
\boxed{ \max_{\lambda\succeq 0}\ b^T\lambda \quad \text{s.t.}\quad A^T\lambda=0,\ \mathbf 1^T\lambda=1. }
$$

Smooth approximation (5.106)
----------------------------

$$
\min_x \log\Big(\sum_i e^{a_i^T x+b_i}\Big).
$$

Smooth dual
-----------

$$
\boxed{ \max_{\lambda\succeq 0}\left(b^T\lambda-\sum_i \lambda_i\log\lambda_i\right) \quad \text{s.t.}\quad A^T\lambda=0,\ \mathbf 1^T\lambda=1. }
$$

Approximation gap
-----------------

$$
\boxed{ 0\le p_{\text{sm}}^*-p_{\text{pl}}^*\le \log m. }
$$

 $\gamma$ \-approximation gap
-----------------------------

$$
\boxed{ 0\le p_{\gamma}^*-p_{\text{pl}}^*\le \frac{\log m}{\gamma},\quad p_\gamma^*\to p_{\text{pl}}^* \text{ as }\gamma\to\infty. }
$$

* * *

If you want to push even deeper (totally optional but very illuminating), the next natural layer is: **derive  $\nabla f_{\text{sm}}(x)$ ** and show it equals a softmax-weighted average of the  $a_i$ , then connect the condition  $\nabla f_{\text{sm}}(x^*)=0$  directly to the dual feasibility condition  $A^T\lambda=0$  with  $\lambda=\text{softmax}(Ax+b)$ . That’s the clean primal–dual bridge for the smooth case.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)