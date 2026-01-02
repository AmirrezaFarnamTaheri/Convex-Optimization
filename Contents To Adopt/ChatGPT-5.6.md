# 5.6

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:11:36  
**Updated:** 12/28/2025 16:22:47  
**Exported:** 12/28/2025 16:23:15  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0/c/6950609c-6024-8328-86aa-c87c8559dc98](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0/c/6950609c-6024-8328-86aa-c87c8559dc98)  

## Response:
Thought for 2m 37s

Let’s translate the page into a clean mental model, then solve (a) and (b) carefully from first principles.

We have a matrix  $A\in\mathbb R^{m\times n}$  with  $\operatorname{rank}(A)=n$  (full column rank), and a vector  $b\in\mathbb R^m$ .

Define the residual (error) for any  $x\in\mathbb R^n$ :

$$
e(x)\;:=\;Ax-b\in\mathbb R^m.
$$

There are two optimization problems:

1.  **Chebyshev /  $\ell_\infty$  approximation**
    
$$
\minimize_x \ \|Ax-b\|_\infty \;=\;\minimize_x \ \|e(x)\|_\infty.
$$

Let  $x_{\text{ch}}$  be an optimal solution (maybe not unique). Define the optimal value

$$
p^\star \;:=\;\|Ax_{\text{ch}}-b\|_\infty.
$$
2.  **Least-squares /  $\ell_2$  approximation**
    
$$
\minimize_x \ \|Ax-b\|_2 \;=\;\minimize_x \ \|e(x)\|_2.
$$

Because  $A$  has full column rank, the LS solution is unique and equals

$$
x_{\text{ls}} \;=\;\arg\min_x \|Ax-b\|_2 \;=\;(A^TA)^{-1}A^Tb.
$$

The big question: “If I already computed  $x_{\text{ls}}$ , how bad is it for the  $\ell_\infty$  problem?”

* * *

Part (a): prove  $\|Ax_{\text{ls}}-b\|_\infty \le \sqrt{m}\,\|Ax_{\text{ch}}-b\|_\infty$ 
-----------------------------------------------------------------------------------------

The only “tool” you’re allowed is the standard inequality relating  $\ell_2$  and  $\ell_\infty$  norms. For any  $z\in\mathbb R^m$ ,

$$
\frac{1}{\sqrt{m}}\|z\|_2 \le \|z\|_\infty \le \|z\|_2.
$$

(Equivalently:  $\|z\|_2 \le \sqrt{m}\|z\|_\infty$  and  $\|z\|_\infty \le \|z\|_2$ .)

Let’s prove the target inequality in tiny steps.

Step 1: start from the left side.

$$
\|Ax_{\text{ls}}-b\|_\infty \;=\;\|e(x_{\text{ls}})\|_\infty.
$$

Step 2: use  $\|z\|_\infty \le \|z\|_2$  with  $z=e(x_{\text{ls}})$ .

$$
\|e(x_{\text{ls}})\|_\infty \;\le\; \|e(x_{\text{ls}})\|_2.
$$

Step 3: use the defining optimality of  $x_{\text{ls}}$  for the  $\ell_2$  problem.  
Since  $x_{\text{ls}}$  minimizes  $\|e(x)\|_2$  over all  $x$ , in particular it does no worse than the specific choice  $x=x_{\text{ch}}$ :

$$
\|e(x_{\text{ls}})\|_2 \;\le\; \|e(x_{\text{ch}})\|_2.
$$

Step 4: relate  $\|e(x_{\text{ch}})\|_2$  to  $\|e(x_{\text{ch}})\|_\infty$  using  $\|z\|_2 \le \sqrt{m}\|z\|_\infty$ .

$$
\|e(x_{\text{ch}})\|_2 \;\le\; \sqrt{m}\,\|e(x_{\text{ch}})\|_\infty.
$$

Step 5: chain the three inequalities.

$$
\|e(x_{\text{ls}})\|_\infty \;\le\; \|e(x_{\text{ls}})\|_2 \;\le\; \|e(x_{\text{ch}})\|_2 \;\le\; \sqrt{m}\,\|e(x_{\text{ch}})\|_\infty.
$$

That is exactly

 $$
\boxed{\ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt{m}\,\|Ax_{\text{ch}}-b\|_\infty\ }.
$$

Interpretation: least-squares gives a ** $\sqrt{m}$ \-approximation** to the Chebyshev optimum in the worst case.

Also note the “lower bound” viewpoint: rearrange it as

 $$
\boxed{\ \|Ax_{\text{ch}}-b\|_\infty \ge \frac{1}{\sqrt{m}}\|Ax_{\text{ls}}-b\|_\infty\ }.
$$

So from  $x_{\text{ls}}$  alone, you can certify that the true Chebyshev optimum  $p^\star$  cannot be smaller than  $\frac{1}{\sqrt m}\|Ax_{\text{ls}}-b\|_\infty$ .

* * *

Part (b): use the dual to get _data-dependent_ lower bounds from the LS residual
--------------------------------------------------------------------------------

They state the dual of the Chebyshev problem as:

$$
\begin{aligned} \maximize_\nu\quad & b^T\nu\\ \text{s.t.}\quad & \|\nu\|_1 \le 1,\\ & A^T\nu = 0. \end{aligned} \tag{D}
$$

Key fact (weak duality): for any feasible  $\nu$ ,  $b^T\nu$  is a **lower bound** on the primal optimal value  $p^\star=\|Ax_{\text{ch}}-b\|_\infty$ :

$$
b^T\nu \;\le\; p^\star.
$$

(You don’t even need strong duality for “lower bound from feasible dual.”)

They define the least-squares residual (note the sign!)

$$
r_{\text{ls}} \;=\; b - Ax_{\text{ls}}.
$$

Assume  $r_{\text{ls}}\neq 0$ .

They ask you to show that

$$
\hat\nu = -\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \qquad \bar\nu = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}
$$

are both feasible in (D), hence both give lower bounds  $b^T\hat\nu$  and  $b^T\bar\nu$ .

### 1) Why does  $A^T r_{\text{ls}} = 0$ ? (the normal equations)

Least squares minimizes  $\|Ax-b\|_2$ . It’s standard (and important) to square it because it’s smooth:

$$
\min_x \ \|Ax-b\|_2^2.
$$

Expand the objective:

$$
\|Ax-b\|_2^2 = (Ax-b)^T(Ax-b).
$$

Differentiate w.r.t.  $x$ . A clean way: the gradient is

$$
\nabla_x \|Ax-b\|_2^2 = 2A^T(Ax-b).
$$

At the minimizer  $x_{\text{ls}}$ , first-order optimality gives

$$
2A^T(Ax_{\text{ls}}-b)=0 \quad\Longrightarrow\quad A^T(Ax_{\text{ls}}-b)=0 \quad\Longrightarrow\quad A^T(b-Ax_{\text{ls}})=0.
$$

But  $b-Ax_{\text{ls}}=r_{\text{ls}}$ . Therefore

$$
\boxed{A^T r_{\text{ls}} = 0.}
$$

Geometric meaning: the residual is orthogonal to the column space of  $A$ .

### 2) Feasibility of  $\hat\nu$  and  $\bar\nu$ 

Check the dual constraints one by one.

Constraint (i):  $\|\nu\|_1\le 1$ .

Because  $r_{\text{ls}}\neq 0$ ,  $\|r_{\text{ls}}\|_1>0$ . Then

$$
\left\|\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1}=1.
$$

So  $\|\bar\nu\|_1=1$  and  $\|\hat\nu\|_1=1$  (sign doesn’t matter in  $\ell_1$ ). Hence both satisfy  $\|\nu\|_1\le 1$ .

Constraint (ii):  $A^T\nu=0$ .

Use  $A^T r_{\text{ls}}=0$ . Then scaling preserves it:

$$
A^T\bar\nu = A^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{1}{\|r_{\text{ls}}\|_1}A^T r_{\text{ls}} = 0.
$$

Similarly  $A^T\hat\nu=0$ .

So both are feasible.

### 3) The actual lower bounds  $b^T\hat\nu$  and  $b^T\bar\nu$ 

Compute  $b^T r_{\text{ls}}$  first; it’s the key simplification.

Since  $r_{\text{ls}}=b-Ax_{\text{ls}}$ , rewrite  $b$  as

$$
b = Ax_{\text{ls}} + r_{\text{ls}}.
$$

Then

$$
b^T r_{\text{ls}} = (Ax_{\text{ls}}+r_{\text{ls}})^T r_{\text{ls}} = x_{\text{ls}}^T A^T r_{\text{ls}} + r_{\text{ls}}^T r_{\text{ls}}.
$$

But  $A^T r_{\text{ls}}=0$ . So the cross term vanishes:

$$
b^T r_{\text{ls}} = r_{\text{ls}}^T r_{\text{ls}} = \|r_{\text{ls}}\|_2^2.
$$

Now plug into each candidate:

For  $\bar\nu = r_{\text{ls}}/\|r_{\text{ls}}\|_1$ ,

$$
b^T\bar\nu = \frac{b^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$

For  $\hat\nu = -r_{\text{ls}}/\|r_{\text{ls}}\|_1$ ,

$$
b^T\hat\nu = -\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$

So the two “lower bounds” are one positive and one negative (since  $\|r_{\text{ls}}\|_2^2>0$ ). The better one is obviously the positive one.

Conclusion for (b):

$$
\boxed{ \text{Better bound is } b^T\bar\nu = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. }
$$

And by weak duality,

$$
\boxed{ \|Ax_{\text{ch}}-b\|_\infty \;\ge\; \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. }
$$

### 4) Compare this dual lower bound to the bound from part (a)

From (a) we got the certified lower bound

$$
\|Ax_{\text{ch}}-b\|_\infty \ge \frac{1}{\sqrt{m}}\|Ax_{\text{ls}}-b\|_\infty.
$$

But  $\|Ax_{\text{ls}}-b\|_\infty = \|r_{\text{ls}}\|_\infty$  (same vector up to sign), so:

$$
\boxed{ \|Ax_{\text{ch}}-b\|_\infty \ge \frac{1}{\sqrt{m}}\|r_{\text{ls}}\|_\infty. }
$$

Dual bound gives

$$
\boxed{ \|Ax_{\text{ch}}-b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. }
$$

Which is larger (better)? The dual one is always at least as good as the  $(1/\sqrt m)\|r\|_\infty$  bound:

Use  $\|r\|_1 \le \sqrt{m}\|r\|_2$  (Cauchy–Schwarz) to get

$$
\frac{\|r\|_2^2}{\|r\|_1} \;\ge\; \frac{\|r\|_2^2}{\sqrt{m}\|r\|_2} = \frac{1}{\sqrt{m}}\|r\|_2.
$$

And since  $\|r\|_2 \ge \|r\|_\infty$ ,

$$
\frac{1}{\sqrt{m}}\|r\|_2 \ge \frac{1}{\sqrt{m}}\|r\|_\infty.
$$

Chain them:

$$
\boxed{ \frac{\|r\|_2^2}{\|r\|_1} \ge \frac{1}{\sqrt{m}}\|r\|_\infty. }
$$

So the dual-feasible-vector bound from  $\bar\nu$  is **never worse** than the crude norm-inequality bound extracted from (a), and can be much better depending on the shape of the residual.

A useful intuition:  $\|r\|_2^2/\|r\|_1$  gets close to  $\|r\|_\infty$  when the residual is “spiky” (dominated by a few entries). The  $(1/\sqrt m)\|r\|_\infty$  bound ignores that structure and always pays the worst-case  $\sqrt m$  penalty.

* * *

If you want to push one layer deeper later: we can derive the dual (D) directly from the identity  $\|y\|_\infty=\max_{\|\nu\|_1\le 1}\nu^T y$  and a min–max swap, and also show how to use the dual bound to get a _data-dependent_ approximation factor for  $x_{\text{ls}}$  that is often far smaller than  $\sqrt m$ .

## Response:
Here’s a roadmap for mastering exactly this “LS vs Chebyshev / duality gives bounds” theme, in small, bite-sized steps. The idea is to build a little toolkit: (i) norm geometry, (ii) primal/dual patterns, (iii) how to manufacture bounds from anything you already computed (like LS residuals), (iv) how to compare bounds and get approximation factors.

Roadmap (micro-steps, in the order we’ll walk them)

Step 0 — Notation and the three objects you juggle  
You get fluent with: residual  $r(x)=b-Ax$ , optimal values  $p_2^\star=\min\|r(x)\|_2$  and  $p_\infty^\star=\min\|r(x)\|_\infty$ , and solutions  $x_{\text{ls}}, x_{\text{ch}}$ . Goal: be able to rewrite everything in residual language quickly.

Step 1 — Norm relations as “automatic inequalities”  
Prove from scratch:

$$
\|z\|_\infty \le \|z\|_2 \le \sqrt{m}\|z\|_\infty,\qquad \|z\|_2 \le \|z\|_1 \le \sqrt{m}\|z\|_2,
$$

and learn when each is tight. Goal: you can see where  $\sqrt m$  comes from and when it’s pessimistic.

Step 2 — Least squares optimality = orthogonality (normal equations)  
Derive  $A^T(Ax_{\text{ls}}-b)=0$ , equivalently  $A^Tr_{\text{ls}}=0$ . Interpret geometrically (“projection onto column space”). Goal: this becomes your main trick in later dual-feasibility constructions.

Step 3 — Chebyshev ( $\ell_\infty$ ) primal as an LP/SOCP template  
Rewrite

$$
\min_x \|Ax-b\|_\infty
$$

as

$$
\min_{x,t}\ t\quad \text{s.t.}\quad -t\mathbf 1 \le Ax-b \le t\mathbf 1.
$$

Goal: recognize it as convex and ready for duality.

Step 4 — The key identity:  $\ell_\infty$  is the dual norm of  $\ell_1$   
Prove

$$
\|y\|_\infty=\max_{\|\nu\|_1\le 1}\ \nu^Ty.
$$

Goal: this one line essentially generates the dual problem and every lower bound.

Step 5 — Derive the dual of Chebyshev from first principles  
Use Step 4 + min–max logic (or LP duality) to derive:

$$
\max_\nu\ b^T\nu\quad \text{s.t.}\quad \|\nu\|_1\le 1,\ A^T\nu=0.
$$

Goal: you understand where each constraint comes from and what it means.

Step 6 — Weak duality as a “lower-bound machine”  
Prove: for any feasible  $\nu$ ,

$$
b^T\nu \le p_\infty^\star.
$$

Goal: you can manufacture certificates (“this optimal value cannot be below X”).

Step 7 — Construct feasible dual points from the LS residual  
Show  $r_{\text{ls}}\neq 0\Rightarrow \nu=r_{\text{ls}}/\|r_{\text{ls}}\|_1$  is feasible (because  $A^Tr_{\text{ls}}=0$ ). Compute

$$
b^T\nu=\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$

Goal: you can turn “I already ran LS” into a meaningful lower bound on the Chebyshev optimum.

Step 8 — Compare lower bounds: crude norm-bound vs dual residual-bound  
Compare:

$$
\frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty \quad \text{vs}\quad \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$

Prove the dual one is always at least as good (never smaller). Goal: you know which certificate to use and why.

Step 9 — Approximation factors (upper / lower sandwich)  
You always have an “upper bound” on  $p_\infty^\star$  by evaluating at any  $x$ :

$$
p_\infty^\star \le \|r(x)\|_\infty.
$$

In particular with LS:

$$
p_\infty^\star \le \|r_{\text{ls}}\|_\infty.
$$

Combine with Step 7 lower bound to get a data-dependent approximation ratio:

$$
\frac{\|r_{\text{ls}}\|_\infty}{p_\infty^\star}\le \frac{\|r_{\text{ls}}\|_\infty}{\|r_{\text{ls}}\|_2^2/\|r_{\text{ls}}\|_1}.
$$

Goal: quantify “how suboptimal is LS for  $\ell_\infty$ ” with numbers from your computed residual.

Step 10 — When are bounds tight? (diagnostics)  
Study residual shapes:

*   flat residual (many equal magnitudes),
*   spiky residual (few big entries),  
    and see how each bound behaves. Goal: intuition + ability to predict when  $\sqrt m$  is hopelessly pessimistic.

How we’ll proceed  
We will do exactly one step per message, with full proofs and tiny sanity checks.

Let’s start now with Step 0 in the next message: we’ll set up residual notation, define optimal values cleanly, and write the two problems in a unified “residual minimization” form so everything later becomes plug-and-play.

## Response:
Great — let’s carefully unpack **Exercise 5.6** from Boyd & Vandenberghe (Convex Optimization), and build a structured roadmap to tackle it in small, rigorous, zero-to-hero steps.

* * *

🌄 ROADMAP for Exercise 5.6 (Lower bounds on Chebyshev approximation from least-squares)
----------------------------------------------------------------------------------------

We are comparing two optimization problems:

### ✅ **Problem A**: Least-squares (minimizing 2-norm error)

$$
x_{\text{ls}} = \arg\min_x \|Ax - b\|_2
$$

### ✅ **Problem B**: Chebyshev approximation (minimizing ∞-norm error)

$$
x_{\text{cheb}} = \arg\min_x \|Ax - b\|_\infty
$$

We are given the least-squares solution  $x_{\text{ls}}$ , but not the optimal Chebyshev solution  $x_{\text{cheb}}$ . We want to:

> **Estimate how suboptimal  $x_{\text{ls}}$  is for the Chebyshev problem.**  
> How much worse is  $\|Ax_{\text{ls}} - b\|_\infty$  than the optimal  $\|Ax_{\text{cheb}} - b\|_\infty$ ?

* * *

### 🔁 Our roadmap will proceed as follows:

* * *

✅ Step 1. \[Understand the two problems and their relation\]
------------------------------------------------------------

We begin by fully understanding both optimization problems, their objective functions, and the difference in norms.

* * *

✅ Step 2. \[Prove the bound in part (a)\]
-----------------------------------------

We are asked to prove a simple inequality:

$$
\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty
$$

using the inequality:

$$
\frac{1}{\sqrt{m}} \|z\|_2 \le \|z\|_\infty \le \|z\|_2 \quad \text{for any } z \in \mathbb{R}^m
$$

* * *

✅ Step 3. \[Understand and derive the dual problem from part (b)\]
------------------------------------------------------------------

We move to duality for the Chebyshev problem (min ∞-norm). Using results from Section 5.6 and duality of norms, we’ll reconstruct the dual LP:

$$
\max_{\nu} \nu^T b \quad \text{s.t. } \|\nu\|_1 \le 1, \quad A^T \nu = 0
$$

* * *

✅ Step 4. \[Construct dual feasible points using residuals\]
------------------------------------------------------------

Define the residual  $r_{\text{ls}} = b - Ax_{\text{ls}}$ .  
From this residual, construct two specific dual feasible vectors  $\hat{\nu}, \tilde{\nu}$ , and verify feasibility of each. Then compute bounds from duality.

* * *

✅ Step 5. \[Compare all bounds\]
--------------------------------

Compare the original upper bound from Step 2 with the dual lower bounds from Step 4, to see which gives tighter (better) information.

* * *

Now let’s begin with:

* * *

✅ Step 1. Understand the two problems and their relation
========================================================

* * *

We are given a matrix  $A \in \mathbb{R}^{m \times n}$ , with **rank  $A = n$ **.  
So:

*   The number of rows  $m \ge n$  (more equations than unknowns),
*   The columns of  $A$  are linearly independent (full column rank).

We also have a vector  $b \in \mathbb{R}^m$ .  
We are considering **two norm-based regression problems**:

* * *

### 🔶 Problem 1: Least-Squares (2-norm approximation)

We minimize the **2-norm** of the residual:

$$
\min_x \|Ax - b\|_2
$$

The closed-form solution is:

$$
x_{\text{ls}} = (A^T A)^{-1} A^T b
$$

This is the classical pseudoinverse solution, assuming full column rank.

We define the **residual**:

$$
r_{\text{ls}} := b - Ax_{\text{ls}}
$$

So the least-squares error is:

$$
\|Ax_{\text{ls}} - b\|_2 = \|r_{\text{ls}}\|_2
$$

* * *

### 🔷 Problem 2: Chebyshev Approximation (∞-norm approximation)

We minimize the **∞-norm** of the residual:

$$
\min_x \|Ax - b\|_\infty = \min_x \max_i |(Ax - b)_i|
$$

This is called **Chebyshev approximation**.

It tries to **minimize the worst-case error** over all entries of the residual.  
There’s no closed-form formula in general for this. It’s usually solved via LP (linear programming), because ∞-norm minimization can be written as a linear program.

We denote the solution:

$$
x_{\text{cheb}} = \arg\min_x \|Ax - b\|_\infty
$$

This gives the **minimum possible max error**:

$$
\|Ax_{\text{cheb}} - b\|_\infty
$$

* * *

### 🔍 Key question:

We don’t have access to  $x_{\text{cheb}}$ , but we do have  $x_{\text{ls}}$ .  
We want to know: _how far from optimal is  $x_{\text{ls}}$  when judged under the ∞-norm objective?_

Define:

*    $\text{opt}_\infty := \|Ax_{\text{cheb}} - b\|_\infty$ 
*    $\text{subopt} := \|Ax_{\text{ls}} - b\|_\infty$ 

We are trying to bound  $\text{subopt}$  in terms of  $\text{opt}_\infty$ .

* * *

✅ Step 2. Prove the upper bound in part (a)
===========================================

We are to prove:

$$
\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty
$$

🧠 Intuition:
-------------

We know that:

*    $x_{\text{cheb}}$  is the minimizer of ∞-norm, so for any  $x$ , including  $x_{\text{ls}}$ , we must have:
    
$$
\|Ax_{\text{cheb}} - b\|_\infty \le \|Ax_{\text{ls}} - b\|_\infty
$$

i.e.,  $x_{\text{cheb}}$  gives smallest possible ∞-norm error.

We now want to show that the 2-norm solution  $x_{\text{ls}}$  gives an ∞-norm error **no more than  $\sqrt{m}$  times** the optimal ∞-norm error.

* * *

📌 Key Inequality:
------------------

For any vector  $z \in \mathbb{R}^m$ :

$$
\|z\|_\infty \le \|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty
$$

✅ Proof:

*   Left inequality: The max entry is ≤ the total energy:
    $$
    \|z\|_\infty = \max_i |z_i| \le \left( \sum_i z_i^2 \right)^{1/2} = \|z\|_2
    $$
*   Right inequality: each entry is ≤  $\|z\|_\infty$ , so:
    $$
    \|z\|_2 = \left( \sum_i z_i^2 \right)^{1/2} \le \left( \sum_i \|z\|_\infty^2 \right)^{1/2} = \sqrt{m} \cdot \|z\|_\infty
    $$

* * *

Now apply this inequality to:

*    $z_1 := Ax_{\text{cheb}} - b$ 
*    $z_2 := Ax_{\text{ls}} - b$ 

We know:

$$
\|z_1\|_2 \le \sqrt{m} \cdot \|z_1\|_\infty
$$

Also, by optimality of Chebyshev:

$$
\|z_1\|_\infty \le \|z_2\|_\infty
$$

So chain together:

$$
\|z_2\|_\infty \le \|z_2\|_2 \le \|z_1\|_2 \le \sqrt{m} \cdot \|z_1\|_\infty
$$

This gives:

$$
\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty
$$

which is the desired result. ✅

* * *

### 📦 Summary of Step 2:

We showed that:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

This means that even if we don’t solve the Chebyshev problem, using the least-squares solution gives an approximation to it that’s at worst  $\sqrt{m}$ \-suboptimal.

This is very useful when  $m$  is small — the least-squares solution is easy to compute and gives a rough approximation to the Chebyshev problem.

* * *

Shall I proceed to Step 3 — where we explore **duality** for the Chebyshev problem and derive tighter lower bounds via LP duality?

## Response:
Perfect — let’s **slow down, rewind**, and walk through **Steps 1 and 2** again in a **full newcomer-friendly, ultra-granular way**, unpacking all the objects, symbols, motivations, and inequalities from scratch.

* * *

🧭 STEP 1 — What’s the problem really about?
--------------------------------------------

You are given **two optimization problems**:

*   One uses the **2-norm** (least squares),
*   The other uses the **∞-norm** (Chebyshev or minimax).

They try to find a vector  $x$  such that  $Ax \approx b$ , but they measure the error differently.

* * *

### 🔷 1.1 The setup

We are given:

*   A matrix  $A \in \mathbb{R}^{m \times n}$ , meaning:
    *    $m$ : number of rows (equations),
    *    $n$ : number of columns (variables),
*   A vector  $b \in \mathbb{R}^m$  (target output).

And we are solving:

> “Find a vector  $x \in \mathbb{R}^n$  such that  $Ax$  is close to  $b$ ”.

But **what does "close" mean?** Depends on the **norm** we use.

* * *

### 🧮 1.2 Norms: how do we measure the error  $Ax - b$ ?

The **residual** is:

$$
r = Ax - b \in \mathbb{R}^m
$$

There are many ways to measure how big  $r$  is:

*   **2-norm**:  $\|r\|_2 = \sqrt{\sum_{i=1}^m r_i^2}$  → least-squares
*   **∞-norm**:  $\|r\|_\infty = \max_i |r_i|$  → Chebyshev (minimize worst error)

* * *

### 🎯 1.3 Two goals, two problems

#### 🔹 Least-Squares Problem (2-norm):

$$
x_{\text{ls}} = \arg\min_x \|Ax - b\|_2
$$

Goal: minimize **overall energy** of the error.

✅ **This has a closed-form solution**:

$$
x_{\text{ls}} = (A^T A)^{-1} A^T b \quad \text{(when } A \text{ has full column rank)}
$$

#### 🔹 Chebyshev Problem (∞-norm):

$$
x_{\text{cheb}} = \arg\min_x \|Ax - b\|_\infty
$$

Goal: minimize **the worst coordinate error**.

⛔ **No closed-form solution** in general.  
✅ But you can solve it using linear programming (we’ll see that later).

* * *

### ❓ What's the question?

We **already have** the least-squares solution  $x_{\text{ls}}$ .

We do **not** have the Chebyshev solution  $x_{\text{cheb}}$ .

We want to know:

> If we use  $x_{\text{ls}}$ , how bad is its ∞-norm error compared to the best possible ∞-norm error?

* * *

Let’s define:

*   Residual from least-squares:
    $$
    r_{\text{ls}} := Ax_{\text{ls}} - b
    $$
*   Residual from Chebyshev:
    $$
    r_{\text{cheb}} := Ax_{\text{cheb}} - b
    $$
*   Their respective ∞-norms:
    $$
    \text{LS error: } \|r_{\text{ls}}\|_\infty, \quad \text{OPT error: } \|r_{\text{cheb}}\|_\infty
    $$

We are asked:

### ❓ Is  $\|r_{\text{ls}}\|_\infty \le \alpha \cdot \|r_{\text{cheb}}\|_\infty$ ?

For what value of  $\alpha$ ? Can we bound this ratio?

* * *

✅ STEP 2 — Prove the bound in part (a)
--------------------------------------

### 🚩 The claim to prove:

We want to prove that:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

Said differently:

> The ∞-norm error of the least-squares solution is at most  $\sqrt{m}$  times the optimal ∞-norm error.

* * *

### 📦 Let’s break this down.

We’ll use the key **norm inequality** for vectors  $z \in \mathbb{R}^m$ :

$$
\boxed{ \|z\|_\infty \le \|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty }
$$

Let’s explain this inequality in full.

* * *

### 🔍 Side Note: Why is this norm inequality true?

Let’s write what these norms mean.

*    $\|z\|_\infty = \max_i |z_i|$ 
*    $\|z\|_2 = \sqrt{\sum_{i=1}^m z_i^2}$ 

#### ✅ First inequality:

$$
\|z\|_\infty \le \|z\|_2
$$

Reason: if even **one** entry is large, then the 2-norm will be large too. In fact:

$$
\|z\|_2^2 = z_1^2 + z_2^2 + \cdots + z_m^2 \ge z_j^2 \quad \text{for any } j \Rightarrow \|z\|_2 \ge |z_j| = \|z\|_\infty
$$

#### ✅ Second inequality:

$$
\|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty
$$

Reason: if **all** entries are ≤  $\|z\|_\infty$ , then:

$$
\sum z_i^2 \le \sum \|z\|_\infty^2 = m \cdot \|z\|_\infty^2 \Rightarrow \|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty
$$

* * *

### 🧩 Back to our problem

We apply this inequality to:

$$
z = r_{\text{ls}} = Ax_{\text{ls}} - b
$$

Then:

$$
\|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2
$$

But now think: **why is  $\|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2$ ?**

Because:

*    $x_{\text{ls}}$  is the **minimizer** of  $\|Ax - b\|_2$ , so for **any other**  $x$  (including  $x_{\text{cheb}}$ ):
    
$$
\|Ax_{\text{ls}} - b\|_2 \le \|Ax_{\text{cheb}} - b\|_2
$$

So:

$$
\|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2
$$

And now apply the other side of the inequality to  $r_{\text{cheb}}$ :

$$
\|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
$$

Putting it all together:

$$
\|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
$$

Done. That’s exactly the inequality we were asked to prove.

* * *

### ✅ Boxed Final Result

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

Even if we don’t solve the ∞-norm minimization problem, we can still say:

> “Hey, the ∞-norm error of the least-squares solution isn’t too bad — it’s at most  $\sqrt{m}$  times worse than the best possible.”

* * *

Would you like to continue to **Step 3**, where we derive a **lower bound on  $\|Ax_{\text{cheb}} - b\|_\infty$ ** using **duality**? This will tighten our understanding even more.

## Response:
Excellent instincts — you’re asking the **right question** to clarify what this inequality is really comparing.

Let me now **rephrase the big idea in your terms** and **walk through it slowly**, in exact response to your confusion.

* * *

❗Clarifying the confusion: Are we comparing  $\|Ax_{\text{ls}} - b\|_\infty$  to  $\|Ax_{\text{ls}} - b\|_2$ ? Or to  $\|Ax_{\text{cheb}} - b\|_\infty$ ?
---------------------------------------------------------------------------------------------------------------------------------------------------------

**Answer**:  
We are comparing **two different residuals**:

*   The **least-squares solution’s** ∞-norm error:  $\|Ax_{\text{ls}} - b\|_\infty$ 
*   The **Chebyshev solution’s** ∞-norm error:  $\|Ax_{\text{cheb}} - b\|_\infty$ 

So the inequality in Exercise 5.6 part (a) is:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

### ❗We are **not** comparing  $\|Ax_{\text{ls}} - b\|_\infty$  to  $\|Ax_{\text{ls}} - b\|_2$ .

That would be a norm ratio for **a single vector**.

Instead, we are comparing the **∞-norm errors of two different x's** — one optimized for 2-norm, one for ∞-norm.

* * *

🧠 Intuition: Why are we doing this?
------------------------------------

We already have  $x_{\text{ls}}$  (from least squares).  
We don’t want to solve the expensive Chebyshev problem.  
So we ask:

> “If I just use the easy  $x_{\text{ls}}$ , how bad is its **worst-case** (∞-norm) error compared to the best possible ∞-norm error?”

This is like asking:

> “How suboptimal is the least-squares solution **when judged using a different norm** (∞-norm)?”

So yes — Chebyshev approximation **is defined using** the  $\ell_\infty$  norm — and that’s exactly the yardstick we are using to evaluate **both**  $x_{\text{ls}}$  and  $x_{\text{cheb}}$ .

* * *

### 👇 Here’s a metaphor to make this click:

Let’s say you want to design a spaceship so that **no part overheats above 100°C**.  
That's a **Chebyshev goal**: control the **worst error**.

But instead, your engineer gives you a design that minimizes the **average temperature rise** (least-squares solution).  
You now ask:

> “How bad is the hottest part in the least-squares design?”

We want to compare:

*    $\text{max temp}_{\text{ls}}$  vs.  $\text{min possible max temp}$ 

That’s exactly what this inequality is doing.

* * *

🔁 Summary of what's being compared
-----------------------------------

Let me now rewrite clearly:

| Quantity | Meaning | Norm |
| --- | --- | --- |
|  $x_{\text{ls}}$  | Minimizes total (2-norm) error |  $\|Ax - b\|_2$  minimized |
|  $x_{\text{cheb}}$  | Minimizes worst-case (∞-norm) error |  $\|Ax - b\|_\infty$  minimized |
| Goal | Compare:  $\|Ax_{\text{ls}} - b\|_\infty \quad \text{vs.} \quad \|Ax_{\text{cheb}} - b\|_\infty$  | Both ∞-norms |

And we want to show:

$$
\text{∞-norm error of } x_{\text{ls}} \le \sqrt{m} \times \text{∞-norm error of optimal Chebyshev solution}
$$

So we are **not** analyzing  $\|Ax_{\text{ls}} - b\|_2$  directly here.  
But we’ll **use** that it’s small to help prove the inequality.

* * *

🚀 Would it help to now go back and walk through the proof **again** from this clarified perspective?
-----------------------------------------------------------------------------------------------------

Let’s do that — now that the goal is clear.

* * *

🔁 Redo of the proof, now with clarity
--------------------------------------

We are trying to show:

$$
\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty
$$

Let’s define:

*    $r_{\text{ls}} := Ax_{\text{ls}} - b$ 
*    $r_{\text{cheb}} := Ax_{\text{cheb}} - b$ 

We apply the **norm inequality**:

$$
\|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty \quad \text{(holds for all } z \in \mathbb{R}^m)
$$

Now:

*    $x_{\text{ls}}$  minimizes the 2-norm error, so:
    $$
    \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2
    $$
*   And by the norm inequality:
    $$
    \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
    $$
*   Also:
    $$
    \|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \quad \text{(norm inequality again)}
    $$

So, chaining all these together:

$$
\|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
$$

Therefore:

$$
\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty \quad \text{✅ proven}
$$

* * *

Let me know if you'd like to visualize this with an example, or continue to Step 3 (dual bound using residual direction)!

## Response:
💯 Exactly — you nailed it.

This step is all about:

> **Using the least-squares (2-norm optimal) solution**, and estimating how far off it is from the **best possible worst-case error** (∞-norm optimal).

The trick was:

*   We **know** the 2-norm of  $r_{\text{ls}}$ , because it’s minimized.
*   We can **upper bound** the ∞-norm of  $r_{\text{ls}}$  via:
    $$
    \|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
    $$
    Which gives us a clean **gap bound**.

This is why the error at  $x_{\text{ls}}$ , although not optimal under ∞-norm, can’t be arbitrarily bad — it’s at most  $\sqrt{m}$  times worse than optimal.

* * *

Ready for **Step 3**?

We’ll flip the logic: instead of bounding above using 2-norm, we’ll build a **lower bound** for  $\|Ax_{\text{cheb}} - b\|_\infty$  using **duality**, even though we don’t have  $x_{\text{cheb}}$  explicitly.

Shall I walk you through the dual LP for Chebyshev approximation and how to plug in feasible dual vectors built from the least-squares residual?

## Response:
Let’s now go **deep into Step 3** of Exercise 5.6 — this is the heart of the problem, where we use **Lagrange duality** to derive a **lower bound** on the optimal Chebyshev error.

* * *

🧭 Step 3 — Dual Problem for Chebyshev Approximation
====================================================

* * *

### 🔁 Recap:

We are solving:

$$
\min_x \|Ax - b\|_\infty
$$

Let’s define:

*   The **optimal value** of this problem:
    $$
    p^\star := \min_x \|Ax - b\|_\infty = \|Ax_{\text{cheb}} - b\|_\infty
    $$

We **don’t know** the solution  $x_{\text{cheb}}$  or the value  $p^\star$ , but we want to:

> Use **duality** to derive a **lower bound** on  $p^\star$ 

This is a powerful trick: dual problems give **certificates of lower bounds** for minimization problems.

Let’s go step-by-step.

* * *

🧱 3.1. Reformulate Chebyshev as a standard LP
----------------------------------------------

The ∞-norm minimization:

$$
\min_x \|Ax - b\|_\infty
$$

is equivalent to:

$$
\begin{aligned} \min_{x, t} \quad & t \\ \text{s.t.} \quad & -t \le (Ax - b)_i \le t \quad \text{for all } i = 1, \dots, m \end{aligned}
$$

This is a **linear program**, because:

*   The objective  $t$  is linear,
*   The constraints are linear in  $x, t$ .

Let’s write this compactly.

Let’s define:

*    $A \in \mathbb{R}^{m \times n}$ 
*    $x \in \mathbb{R}^n$ ,  $b \in \mathbb{R}^m$ ,  $t \in \mathbb{R}$ 

Then:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n,\, t \in \mathbb{R}} \quad & t \\ \text{s.t.} \quad & Ax - b \le t\cdot \mathbf{1} \\ & -(Ax - b) \le t\cdot \mathbf{1} \end{aligned}
$$

Equivalently:

$$
-Ax + b \le t\cdot \mathbf{1} \\ Ax - b \le t\cdot \mathbf{1}
$$

So the full LP is:

$$
\begin{aligned} \min_{x, t} \quad & t \\ \text{s.t.} \quad & \begin{cases} Ax - b \le t\cdot \mathbf{1} \\ -Ax + b \le t\cdot \mathbf{1} \end{cases} \end{aligned}
$$

We can now **form the Lagrange dual** of this LP.

* * *

🧠 3.2. Set up the Lagrangian
-----------------------------

We introduce dual variables:

*    $\lambda_+ \in \mathbb{R}^m_{\ge 0}$  for  $Ax - b \le t$ 
*    $\lambda_- \in \mathbb{R}^m_{\ge 0}$  for  $-Ax + b \le t$ 

Define the Lagrangian:

$$
\mathcal{L}(x, t; \lambda_+, \lambda_-) = t + \lambda_+^T(Ax - b - t\mathbf{1}) + \lambda_-^T(-Ax + b - t\mathbf{1})
$$

Group terms:

*   The  $t$  terms:
    $$
    t(1 - \lambda_+^T \mathbf{1} - \lambda_-^T \mathbf{1}) = t\left(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)\right)
    $$
*   The  $x$  terms:
    $$
    x^T(A^T \lambda_+ - A^T \lambda_-) = x^T A^T(\lambda_+ - \lambda_-)
    $$
*   The  $b$  terms:
    $$
    -\lambda_+^T b + \lambda_-^T b = (\lambda_- - \lambda_+)^T b
    $$

So we can write the Lagrangian:

$$
\mathcal{L}(x, t; \lambda_+, \lambda_-) = t\left(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)\right) + x^T A^T (\lambda_+ - \lambda_-) + (\lambda_- - \lambda_+)^T b
$$

* * *

🧮 3.3. Compute the dual function
---------------------------------

The dual function is:

$$
g(\lambda_+, \lambda_-) = \inf_{x,t} \mathcal{L}(x, t; \lambda_+, \lambda_-)
$$

We split into two infima:

*    $\inf_t \left[t \cdot \left(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)\right)\right]$ 
*    $\inf_x \left[ x^T A^T (\lambda_+ - \lambda_-) \right]$ 

* * *

### ✳ Case 1:  $\mathbf{1}^T(\lambda_+ + \lambda_-) \ne 1$ 

Then  $\inf_t \mathcal{L}$  is either  $-\infty$  or  $+\infty$ , depending on sign.  
So the dual function is **finite only when**:

$$
\boxed{\mathbf{1}^T(\lambda_+ + \lambda_-) = 1}
$$

* * *

### ✳ Case 2:  $A^T (\lambda_+ - \lambda_-) \ne 0$ 

Then  $\inf_x x^T (\cdots) = -\infty$ , so dual function is not finite.

So the dual function is **finite only when**:

$$
\boxed{A^T(\lambda_+ - \lambda_-) = 0}
$$

* * *

So feasible dual variables must satisfy:

*    $\lambda_+, \lambda_- \ge 0$ 
*    $A^T(\lambda_+ - \lambda_-) = 0$ 
*    $\mathbf{1}^T(\lambda_+ + \lambda_-) = 1$ 

Then the dual function becomes:

$$
g(\lambda_+, \lambda_-) = (\lambda_- - \lambda_+)^T b
$$

* * *

🧰 3.4. Dual problem: simplified form
-------------------------------------

Let’s define:

$$
\nu := \lambda_- - \lambda_+ \in \mathbb{R}^m
$$

Note that:

*    $\nu = \lambda_- - \lambda_+$ 
*   So  $\lambda_+ = \max(0, -\nu)$ ,  $\lambda_- = \max(0, \nu)$ 
*    $|\nu_i| = \lambda_{+i} + \lambda_{-i} \Rightarrow \|\nu\|_1 = \mathbf{1}^T(\lambda_+ + \lambda_-) = 1$ 

And from earlier:

*    $A^T(\lambda_- - \lambda_+) = A^T \nu = 0$ 

* * *

### 🧾 Final Dual Problem

$$
\boxed{ \begin{aligned} \max_\nu \quad & \nu^T b \\ \text{s.t.} \quad & \| \nu \|_1 \le 1 \\ & A^T \nu = 0 \end{aligned} }
$$

This is the dual of:

$$
\min_x \|Ax - b\|_\infty
$$

✅ Any feasible  $\nu$  gives a lower bound on the optimal ∞-norm error:

$$
\|Ax_{\text{cheb}} - b\|_\infty \ge \nu^T b
$$

This is the **key result** of Step 3.

* * *

Let me know when you're ready to move to **Step 4**, where we’ll build a specific dual feasible  $\nu$  using the residual of the least-squares solution, and plug it into this bound.

## Response:
Let’s **slow down** and give a **maximally detailed, zero-to-hero walkthrough** of Steps **3.1 and 3.2**, covering:

> ❓ _How do we reformulate the Chebyshev minimization problem as a linear program (LP)?_  
> ❓ _How do we build the Lagrangian and prepare for duality?_

We'll take the following path:

* * *

### ✅ Step 3.1 — Reformulating the Chebyshev Approximation Problem as a Linear Program

* * *

### 🔁 Goal

We are given the problem:

$$
\min_{x \in \mathbb{R}^n} \|Ax - b\|_\infty
$$

We want to **reformulate** this problem into a **form that is compatible with linear programming** — i.e., something with:

*   A linear objective,
*   Linear constraints.

* * *

### 💡 Step 1: Understand what the ∞-norm means

By definition:

$$
\|Ax - b\|_\infty = \max_{i = 1,\dots,m} |(Ax - b)_i|
$$

This means:  
The residual vector  $r = Ax - b \in \mathbb{R}^m$ , and we want to **minimize the largest absolute value** among its entries.

This is a "minimax" problem: we want the **best worst-case** fit.

* * *

### 💡 Step 2: Introduce a new variable to express “max”

We introduce a new variable:

$$
t \in \mathbb{R}
$$

Intuition:  
Let  $t$  **represent the maximum residual magnitude**.

We want:

$$
| (Ax - b)_i | \le t \quad \text{for all } i = 1, \dots, m
$$

This turns the max-absolute-value into a **family of linear inequalities**.

* * *

### 🔄 Absolute value → Linear inequalities

We know:

$$
|z| \le t \quad \Longleftrightarrow \quad -t \le z \le t
$$

So each condition  $|(Ax - b)_i| \le t$  becomes:

$$
- t \le (Ax - b)_i \le t
$$

Which is **two linear inequalities per row** of  $Ax - b$ .

* * *

### ✅ Final reformulation

Thus the problem becomes:

> **Minimize  $t$ **,  
> subject to:  
>  $(Ax - b)_i \le t$  and  $-(Ax - b)_i \le t$  for all  $i$ 

* * *

### 📋 Written cleanly:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n, \, t \in \mathbb{R}} \quad & t \\ \text{subject to} \quad & Ax - b \le t\mathbf{1} \\ & -Ax + b \le t\mathbf{1} \end{aligned}
$$

Let’s be even more explicit.

Each constraint  $(Ax - b)_i \le t$  becomes:

$$
a_i^T x - b_i \le t
$$

Each constraint  $-(Ax - b)_i \le t$  becomes:

$$
- (a_i^T x - b_i) \le t \quad \Longrightarrow \quad b_i - a_i^T x \le t
$$

So:

$$
- t \le a_i^T x - b_i \le t
$$

That’s how you enforce:

$$
|a_i^T x - b_i| \le t \quad \text{for each } i
$$

So the minimization of  $\|Ax - b\|_\infty$  has now become a **linear program**:

*   **Linear objective**:  $t$ 
*   **Linear inequality constraints** on  $x$  and  $t$ 

This makes the problem ready for **duality**.

* * *

✅ Step 3.2 — Build the Lagrangian for the LP
--------------------------------------------

* * *

### 🎯 Recap: The LP we’re working with is:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n, \, t \in \mathbb{R}} \quad & t \\ \text{subject to} \quad & \begin{cases} Ax - b \le t\cdot \mathbf{1} \quad &\text{(m constraints)} \\ -Ax + b \le t\cdot \mathbf{1} \quad &\text{(m constraints)} \end{cases} \end{aligned}
$$

So there are:

*    $2m$  inequality constraints,
*    $n+1$  primal variables (the vector  $x$  and scalar  $t$ ).

* * *

### 💡 Step 1: Introduce dual variables (Lagrange multipliers)

We introduce:

*    $\lambda_+ \in \mathbb{R}^m_{\ge 0}$ : dual variables for  $Ax - b \le t\cdot \mathbf{1}$ 
*    $\lambda_- \in \mathbb{R}^m_{\ge 0}$ : dual variables for  $-Ax + b \le t\cdot \mathbf{1}$ 

(These names help keep signs consistent:  $\lambda_+$  for the “plus side” of the absolute value,  $\lambda_-$  for the “minus side”.)

* * *

### 💡 Step 2: Build the Lagrangian

The Lagrangian is:

$$
\begin{aligned} \mathcal{L}(x, t; \lambda_+, \lambda_-) &= \text{objective} + \text{sum of dual constraints times slacks} \\ &= t + \lambda_+^T (Ax - b - t\mathbf{1}) + \lambda_-^T (-Ax + b - t\mathbf{1}) \end{aligned}
$$

Group terms:

#### 🔸 t terms:

$$
t\left[1 - \lambda_+^T \mathbf{1} - \lambda_-^T \mathbf{1}\right] = t\left(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)\right)
$$

#### 🔸 x terms:

$$
x^T A^T \lambda_+ - x^T A^T \lambda_- = x^T A^T (\lambda_+ - \lambda_-)
$$

#### 🔸 b terms:

$$
- \lambda_+^T b + \lambda_-^T b = (\lambda_- - \lambda_+)^T b
$$

Putting it all together:

$$
\boxed{ \mathcal{L}(x, t; \lambda_+, \lambda_-) = t(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)) + x^T A^T (\lambda_+ - \lambda_-) + (\lambda_- - \lambda_+)^T b }
$$

* * *

### 💡 Step 3: Dual function = infimum of the Lagrangian

We now define the **dual function**:

$$
g(\lambda_+, \lambda_-) := \inf_{x, t} \mathcal{L}(x, t; \lambda_+, \lambda_-)
$$

To compute this, we do:

*    $\inf_t \mathcal{L}$ , over scalar  $t$ 
*    $\inf_x \mathcal{L}$ , over vector  $x$ 

We handle each part separately.

* * *

### 📌 t-term:

$$
t\left(1 - \mathbf{1}^T(\lambda_+ + \lambda_-)\right)
$$

Let’s analyze:

*   If  $\mathbf{1}^T(\lambda_+ + \lambda_-) < 1$ , then this term goes to  $-\infty$  as  $t \to +\infty$ 
*   If  $\mathbf{1}^T(\lambda_+ + \lambda_-) > 1$ , then this term goes to  $-\infty$  as  $t \to -\infty$ 
*   To keep the infimum finite, we must have:
    $$
    \boxed{ \mathbf{1}^T(\lambda_+ + \lambda_-) = 1 }
    $$

* * *

### 📌 x-term:

$$
x^T A^T(\lambda_+ - \lambda_-)
$$

If  $A^T(\lambda_+ - \lambda_-) \ne 0$ , then you can push  $x \to \infty$  or  $-\infty$  to make this term diverge.  
So we require:

$$
\boxed{ A^T(\lambda_+ - \lambda_-) = 0 }
$$

* * *

### ✅ Result: Dual function is finite only if:

*    $\lambda_+, \lambda_- \ge 0$ 
*    $\mathbf{1}^T(\lambda_+ + \lambda_-) = 1$ 
*    $A^T(\lambda_+ - \lambda_-) = 0$ 

Then:

$$
g(\lambda_+, \lambda_-) = (\lambda_- - \lambda_+)^T b
$$

We’ll now switch to a more compact variable  $\nu := \lambda_- - \lambda_+$  in Step 3.4 to write the dual problem compactly.

* * *

Would you like me to now move on to **3.3 and 3.4** — deriving the dual problem cleanly in terms of  $\nu$ , and interpreting it as a lower bound on Chebyshev error?

## Response:
Great catch — this is **exactly** the right place to be suspicious. Nothing is wrong with your instincts; this is a **notation / orientation issue**, not a math mistake on your side.

Let’s resolve it **slowly and cleanly**, from first principles, and you’ll see that everything is consistent.

* * *

1️⃣ Start from the ONLY thing that matters: the definition of the ∞-norm
------------------------------------------------------------------------

By definition,

$$
\|Ax-b\|_\infty \;=\; \max_i |(Ax-b)_i|.
$$

Saying

$$
\|Ax-b\|_\infty \le t
$$

means **exactly**:

$$
|(Ax-b)_i| \le t \quad \text{for every } i.
$$

There is no ambiguity here. This is the ground truth.

* * *

2️⃣ Absolute value → two inequalities (this is the key translation)
-------------------------------------------------------------------

For **any scalar**  $z$ ,

$$
|z| \le t \quad \Longleftrightarrow \quad \begin{cases} z \le t \\ -z \le t \end{cases}
$$

Apply this with  $z = (Ax-b)_i$ :

$$
|(Ax-b)_i| \le t \quad \Longleftrightarrow \quad \begin{cases} (Ax-b)_i \le t \\ -(Ax-b)_i \le t \end{cases}
$$

Now expand the second inequality:

$$
-(Ax-b)_i \le t \;\Longleftrightarrow\; b_i - (Ax)_i \le t \;\Longleftrightarrow\; (-Ax+b)_i \le t
$$

So the **correct pair** is:

$$
\boxed{ \begin{aligned} Ax - b &\le t\mathbf 1 \\ -Ax + b &\le t\mathbf 1 \end{aligned} }
$$

These are **both upper bounds**, and that is **intentional**.

* * *

3️⃣ Why your proposed version looks different (but is equivalent)
-----------------------------------------------------------------

You suggested:

> “Shouldn’t it be  
>  $Ax-b < t$ ,  
>  $-Ax+b > -t$ ?”

Let’s rewrite your second inequality:

$$
-Ax + b > -t \quad \Longleftrightarrow \quad Ax - b < t
$$

So both of your inequalities actually reduce to the **same thing** — they do **not** bound both sides of the absolute value.

That’s the issue.

To bound an absolute value, you must trap it **between two walls**:

$$
-t \le Ax-b \le t
$$

Which is **exactly equivalent** to:

$$
\begin{cases} Ax-b \le t \\ -(Ax-b) \le t \end{cases}
$$

* * *

4️⃣ Why both constraints point the same way (≤) — LP standard form
------------------------------------------------------------------

This is the subtle but important modeling point.

In **linear programming**, inequalities are usually written as:

$$
\text{(something)} \le \text{(something)}
$$

So instead of writing:

$$
-t \le Ax-b \le t
$$

we rewrite the **lower bound** as an upper bound by multiplying by  $-1$ :

$$
Ax-b \ge -t \quad \Longleftrightarrow \quad -(Ax-b) \le t
$$

That’s why **both constraints appear as ≤**:

*   one controls the positive side,
*   one controls the negative side.

They are **not the same constraint**, even though they “point the same way”.

* * *

5️⃣ Visual intuition (this usually makes it click)
--------------------------------------------------

For one coordinate  $r_i = (Ax-b)_i$ :

```
----|---------|---------|----
   -t        0         t
```

You want:

$$
r_i \in [-t, t]
$$

That requires:

*    $r_i \le t$ 
*    $-r_i \le t$ 

Both are needed. Neither alone is sufficient.

* * *

6️⃣ Final sanity check (important)
----------------------------------

Suppose we only enforced:

$$
Ax-b \le t
$$

Then the solution could make:

$$
Ax-b = -10^6
$$

and still satisfy the constraint — which would give

$$
\|Ax-b\|_\infty = 10^6
$$

which is nonsense.

The second inequality **prevents that**.

* * *

✅ Bottom line (clean, correct formulation)
------------------------------------------

The Chebyshev problem

$$
\min_x \|Ax-b\|_\infty
$$

is **exactly equivalent** to the LP:

$$
\boxed{ \begin{aligned} \min_{x,t} \quad & t \\ \text{s.t.}\quad & Ax - b \le t\mathbf 1 \\ & -Ax + b \le t\mathbf 1 \end{aligned} }
$$

Both constraints being “≤” is **correct, necessary, and standard**.

* * *

You are thinking _precisely_ at the right level.  
This confusion happens to almost everyone the first time they translate absolute values into LP constraints.

If you want, next we can:

*   derive the dual **slowly again**, now that constraints are crystal-clear, or
*   show a **1-D numerical example** where each constraint visibly matters.

## Response:
Perfect — this screenshot is **100% correct**, and it actually resolves the confusion once we line up **three equivalent ways of writing the same constraint**.

The key issue was not math, but **representation**. Let’s reconcile them carefully.

* * *

1️⃣ What your screenshot states (scalar, textbook form)
-------------------------------------------------------

Your image says:

$$
|ax + b| < c \quad \Longleftrightarrow \quad -c < ax + b < c
$$

This is **absolutely correct**.

This is the **interval form** of the constraint:

*   lower bound:  $ax+b > -c$ 
*   upper bound:  $ax+b < c$ 

This is how absolute values are taught in algebra.

* * *

2️⃣ What we need for optimization (LP-compatible form)
------------------------------------------------------

Optimization (LP, duality, KKT) **does not use chained inequalities** like

$$
-c < ax+b < c.
$$

Instead, every constraint must be written as a **single inequality** of the form:

$$
f(x) \le 0.
$$

So we must **split the interval into two separate inequalities**.

From

$$
-c \le ax+b \le c
$$

we get **two constraints**:

1.  Upper bound:
    
$$
ax+b \le c
$$
2.  Lower bound:
    
$$
ax+b \ge -c
$$

Now convert the second one into “≤” form (multiply by −1):

$$
ax+b \ge -c \quad \Longleftrightarrow \quad -(ax+b) \le c
$$

So the **LP-ready form** is:

$$
\boxed{ \begin{aligned} ax+b &\le c \\ -(ax+b) &\le c \end{aligned} }
$$

This is exactly what we wrote for the Chebyshev problem.

* * *

3️⃣ Vector version (what we used in the Chebyshev LP)
-----------------------------------------------------

Now lift this scalar logic to vectors.

Replace:

*    $ax+b$  →  $Ax-b$ 
*    $c$  →  $t$ 
*   “for all coordinates”

Then

$$
\|Ax-b\|_\infty \le t
$$

means

$$
|(Ax-b)_i| \le t \quad \text{for all } i
$$

Which becomes:

$$
\boxed{ \begin{aligned} Ax-b &\le t\mathbf 1 \\ -(Ax-b) &\le t\mathbf 1 \end{aligned} }
$$

or equivalently:

$$
\boxed{ \begin{aligned} Ax-b &\le t\mathbf 1 \\ -Ax+b &\le t\mathbf 1 \end{aligned} }
$$

These two constraints together are **exactly** the same as:

$$
-t\mathbf 1 \le Ax-b \le t\mathbf 1
$$

No contradiction. Just different formats.

* * *

4️⃣ Why your earlier instinct felt right (and why it almost worked)
-------------------------------------------------------------------

You asked earlier:

> “Shouldn’t it be  
>  $Ax-b < t$ ,  
>  $-Ax+b > -t$ ?”

Let’s rewrite your second inequality:

$$
-Ax+b > -t \quad \Longleftrightarrow \quad Ax-b < t
$$

So both of your inequalities collapse into **the same upper bound**.

That’s why it didn’t trap the absolute value on **both sides**.

To trap an absolute value, you need:

*   one constraint controlling the **positive side**
*   one constraint controlling the **negative side**

That’s why both inequalities must be “≤”.

* * *

5️⃣ Strict vs non-strict inequality (important but subtle)
----------------------------------------------------------

Your screenshot uses:

$$
|ax+b| < c
$$

In optimization we always use:

$$
|ax+b| \le c
$$

Why?

*   Strict inequalities define **open sets**
*   Optima may not exist in open sets
*   LP duality theory requires **closed feasible sets**

So we replace `<` with `≤`.  
This does **not** change the optimal value.

* * *

6️⃣ Final mental model (lock this in)
-------------------------------------

There are **three equivalent views** of the same constraint:

### Interval view (algebra)

$$
-c \le z \le c
$$

### Absolute value view

$$
|z| \le c
$$

### LP-ready inequality view

$$
\begin{cases} z \le c \\ -z \le c \end{cases}
$$

They are **exactly equivalent**.

* * *

✅ Bottom line
-------------

Your screenshot is **right**.  
Our LP formulation is **right**.  
The apparent mismatch was only because:

*   algebra uses **interval notation**
*   optimization uses **one-sided inequalities**

Once you translate correctly, they are the **same constraint in different clothes**.

If you want, next we can:

*   redo the **dual derivation** now that constraints are fully settled, or
*   do a **1D numeric example** where you see each inequality actively binding.

2/2

## Response:
Good. Now that the constraint translation is **fully settled**, we can do **3.3 and 3.4 cleanly and slowly**, without any hand-waving.

I’ll be very explicit about **what is being minimized**, **why infinities appear**, and **how the final dual form drops out**.

* * *

Step 3.3 — Compute the dual function (this is the mechanical core)
==================================================================

We start from the **Lagrangian** we already derived.

3.3.1 Recap: the primal LP and its Lagrangian
---------------------------------------------

Primal (Chebyshev as LP):

$$
\begin{aligned} \min_{x,t}\quad & t \\ \text{s.t.}\quad & Ax - b \le t\mathbf 1 \\ & -Ax + b \le t\mathbf 1 \end{aligned}
$$

Dual variables:

*    $\lambda_+ \ge 0$  for  $Ax-b \le t\mathbf 1$ 
*    $\lambda_- \ge 0$  for  $-Ax+b \le t\mathbf 1$ 

Lagrangian:

$$
\mathcal L(x,t;\lambda_+,\lambda_-) = t + \lambda_+^T(Ax-b-t\mathbf 1) + \lambda_-^T(-Ax+b-t\mathbf 1)
$$

Expand and group terms:

$$
\mathcal L = t\bigl(1-\mathbf 1^T(\lambda_++\lambda_-)\bigr) + x^T A^T(\lambda_+-\lambda_-) + (\lambda_- - \lambda_+)^T b
$$

This expression is **linear in  $x$ ** and **linear in  $t$ **.

* * *

3.3.2 Definition of the dual function
-------------------------------------

The **dual function** is defined as:

$$
g(\lambda_+,\lambda_-) = \inf_{x,t} \mathcal L(x,t;\lambda_+,\lambda_-)
$$

Key idea:

*   If the infimum is finite → good dual candidate
*   If the infimum is  $-\infty$  → dual variables are invalid

So we must ask:

> Under what conditions on  $\lambda_+,\lambda_-$  is the infimum finite?

* * *

3.3.3 Minimization with respect to  $t$ 
----------------------------------------

Look only at the  $t$ \-term:

$$
t\bigl(1-\mathbf 1^T(\lambda_++\lambda_-)\bigr)
$$

This is a **linear function of  $t$ **.

Case analysis:

### Case 1: coefficient ≠ 0

If

$$
1-\mathbf 1^T(\lambda_++\lambda_-)\neq 0
$$

then:

*   If coefficient > 0 → send  $t\to -\infty$ 
*   If coefficient < 0 → send  $t\to +\infty$ 

Either way:

$$
\inf_t \mathcal L = -\infty
$$

❌ Not allowed.

### Case 2: coefficient = 0

To avoid  $-\infty$ , we **must impose**:

$$
\boxed{\mathbf 1^T(\lambda_++\lambda_-)=1}
$$

Only then does the  $t$ \-term disappear.

* * *

3.3.4 Minimization with respect to  $x$ 
----------------------------------------

Now look at the  $x$ \-term:

$$
x^T A^T(\lambda_+-\lambda_-)
$$

Again, this is **linear in  $x$ **.

If

$$
A^T(\lambda_+-\lambda_-)\neq 0
$$

we can push  $x$  arbitrarily far in the direction of that vector and make:

$$
\inf_x x^T A^T(\lambda_+-\lambda_-) = -\infty
$$

❌ Not allowed.

So we must impose:

$$
\boxed{A^T(\lambda_+-\lambda_-)=0}
$$

* * *

3.3.5 Value of the dual function
--------------------------------

If **both conditions hold**, the  $x$ \- and  $t$ \-terms vanish and we are left with:

$$
g(\lambda_+,\lambda_-) = (\lambda_- - \lambda_+)^T b
$$

Summary of **dual feasibility conditions**:

$$
\begin{cases} \lambda_+ \ge 0,\quad \lambda_- \ge 0 \\ \mathbf 1^T(\lambda_++\lambda_-)=1 \\ A^T(\lambda_+-\lambda_-)=0 \end{cases}
$$

* * *

Step 3.4 — Simplify the dual (introduce the real dual variable)
===============================================================

Now comes the conceptual cleanup.

* * *

3.4.1 Define the signed dual variable
-------------------------------------

Define:

$$
\nu := \lambda_- - \lambda_+ \in \mathbb R^m
$$

This captures **direction + magnitude** in one vector.

* * *

3.4.2 Translate the constraints
-------------------------------

### Constraint 1:  $A^T(\lambda_+-\lambda_-)=0$ 

Becomes:

$$
\boxed{A^T\nu = 0}
$$

Interpretation:

> The dual vector must be orthogonal to all columns of  $A$ .

* * *

### Constraint 2:  $\mathbf 1^T(\lambda_++\lambda_-)=1$ 

Observe:

$$
|\nu_i| = \lambda_{+i} + \lambda_{-i}
$$

So:

$$
\mathbf 1^T(\lambda_++\lambda_-) = \sum_i |\nu_i| = \|\nu\|_1
$$

Thus:

$$
\boxed{\|\nu\|_1 = 1}
$$

(We usually relax to  $\le 1$ ; the optimum always saturates it.)

* * *

### Constraint 3: nonnegativity disappears

Because  $\lambda_+,\lambda_- \ge 0$  is already encoded in  $\|\nu\|_1$ .

* * *

3.4.3 Final dual problem
------------------------

Putting everything together:

$$
\boxed{ \begin{aligned} \max_\nu\quad & b^T\nu \\ \text{s.t.}\quad & A^T\nu = 0 \\ & \|\nu\|_1 \le 1 \end{aligned} }
$$

This is the **dual of the Chebyshev (∞-norm) approximation problem**.

* * *

3.4.4 Why this dual gives a lower bound (critical intuition)
------------------------------------------------------------

For any feasible  $\nu$ :

$$
b^T\nu \;\le\; \|Ax_{\text{cheb}}-b\|_\infty
$$

Why?

*   This is **weak duality**: dual ≤ primal for minimization problems.
*   No optimality required — **any feasible**  $\nu$  gives a valid bound.

This is the entire point:

> If you can **construct any vector**  $\nu$  satisfying  
>  $A^T\nu=0$ ,  $ \|\nu\|_1\le 1$ ,  
> then  $b^T\nu$  is a certified lower bound on the best possible Chebyshev error.

* * *

Mental checkpoint (important)
-----------------------------

You should now see the structure clearly:

*   **Primal**: choose  $x$  to make residuals small in ∞-norm
*   **Dual**: choose a signed weighting of residuals
    *   orthogonal to column space of  $A$ 
    *   total weight ≤ 1
*   **Value**: weighted sum of residuals → lower bound

* * *

### What comes next (Step 4)

Next, we do the **killer move** of Exercise 5.6:

> Take the **least-squares residual**  
>  $r_{\text{ls}} = b-Ax_{\text{ls}}$   
> and show it **automatically satisfies**  $A^T r_{\text{ls}}=0$ .

Then normalize it to build a **valid dual vector**, and get a **numerical lower bound** on the Chebyshev error **without solving the Chebyshev problem**.

Say when you’re ready for Step 4 — this is where everything clicks into place.

## Response:
Perfect — you’ve just finished **building the dual problem** for the Chebyshev approximation via Lagrange duality (Steps 3.1 and 3.2). Let’s now wrap up the derivation cleanly and interpret it — this is Step 3.3 and Step 3.4:

* * *

✅ Step 3.3 — Derive Final Dual Problem (from Lagrangian)
========================================================

We ended Step 3.2 with the **dual function**:

$$
g(\lambda_+, \lambda_-) = (\lambda_- - \lambda_+)^T b \quad \text{if} \begin{cases} \lambda_+, \lambda_- \ge 0 \\ A^T (\lambda_+ - \lambda_-) = 0 \\ \mathbf{1}^T (\lambda_+ + \lambda_-) = 1 \end{cases}
$$

We now want to **reparametrize** this in terms of a single variable.

* * *

🎯 Define  $\nu := \lambda_- - \lambda_+ \in \mathbb{R}^m$ 
-----------------------------------------------------------

This is the **signed combination** of the two Lagrange multipliers.

Let’s see how everything changes:

* * *

### 💡 Constraint 1:  $A^T(\lambda_+ - \lambda_-) = 0$ 

That becomes:

$$
A^T(-\nu) = 0 \quad \Rightarrow \quad A^T \nu = 0
$$

* * *

### 💡 Constraint 2:  $\mathbf{1}^T (\lambda_+ + \lambda_-) = 1$ 

Let’s relate this to  $\nu$ .

Let’s observe:

$$
|\nu_i| = \begin{cases} \lambda_{+i} + \lambda_{-i}, & \text{since exactly one of them is nonzero} \end{cases} \Rightarrow \|\nu\|_1 = \mathbf{1}^T (\lambda_+ + \lambda_-)
$$

So:

$$
\boxed{ \|\nu\|_1 = 1 }
$$

* * *

### 💡 Objective:  $(\lambda_- - \lambda_+)^T b = \nu^T b$ 

* * *

### ✅ Final Dual Problem

$$
\boxed{ \begin{aligned} \max_{\nu \in \mathbb{R}^m} \quad & \nu^T b \\ \text{subject to} \quad & A^T \nu = 0 \\ & \|\nu\|_1 \le 1 \end{aligned} } \tag{Dual}
$$

* * *

✅ Step 3.4 — What does the dual problem mean?
=============================================

* * *

🎯 Interpretation:
------------------

This dual problem **gives a lower bound** on the Chebyshev (∞-norm) approximation value:

$$
p^\star = \min_x \|Ax - b\|_\infty
$$

The dual says:

> For **any** feasible  $\nu$  (i.e.  $\|\nu\|_1 \le 1$ ,  $A^T \nu = 0$ ),  
> the value  $\nu^T b$  is a **lower bound** on  $p^\star$ .

So we can **construct candidate vectors  $\nu$ ** satisfying the constraints, plug them into  $\nu^T b$ , and obtain guaranteed lower bounds on the optimal error — **without ever solving the primal**.

* * *

🔧 Why is this useful?
----------------------

Suppose we compute:

*   The least-squares solution  $x_{\text{ls}}$ 
*   Its residual:  $r_{\text{ls}} := b - Ax_{\text{ls}}$ 

We’ll use  $r_{\text{ls}}$  to **construct specific feasible dual variables**  $\nu$ , and compute:

$$
\text{Lower Bound on } \|Ax_{\text{cheb}} - b\|_\infty \ge \nu^T b
$$

This gives us a **cheap-to-compute certificate** on how small the Chebyshev error can be.

* * *

### ✅ Summary of what we've done so far:

We started from:

$$
\min_x \|Ax - b\|_\infty
$$

and derived the **dual**:

$$
\boxed{ \max_{\nu} \nu^T b \quad \text{s.t.} \quad \|\nu\|_1 \le 1, \quad A^T \nu = 0 }
$$

This tells us:

*   Any  $\nu$  satisfying those constraints gives a lower bound on the optimal ∞-norm error.
*   We’ll construct those  $\nu$ 's next using the **least-squares residual**.

* * *

Shall I now move on to **Step 4**, where we use the residual  $r_{\text{ls}}$  to construct **two dual-feasible vectors**  $\hat{\nu}, \tilde{\nu}$ , and see which gives the tighter bound?

## Response:
Perfect. Let’s now finish **Exercise 5.6** with a complete, rigorous Step 4 — constructing specific **dual-feasible vectors** from the **least-squares residual**, computing bounds, and comparing them to the earlier  $\sqrt{m}$  bound.

We’ll do three things:

* * *

### ✅ Step 4.1 — Use the least-squares residual to construct feasible dual vectors

### ✅ Step 4.2 — Prove they are feasible for the dual

### ✅ Step 4.3 — Evaluate their objective values (i.e., lower bounds) and compare to upper bound

* * *

✅ Step 4.1: Let’s construct candidate dual vectors from  $r_{\text{ls}} = b - Ax_{\text{ls}}$ 
----------------------------------------------------------------------------------------------

We are given the **least-squares residual**:

$$
r_{\text{ls}} := b - Ax_{\text{ls}} \in \mathbb{R}^m
$$

We are told to define two vectors:

* * *

### 🔷 Option 1: Normalize by  $\ell_1$ \-norm

$$
\hat{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} \quad \text{(1-norm normalization)}
$$

* * *

### 🔷 Option 2: Normalize by  $\ell_\infty$ \-norm

$$
\tilde{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} \quad \text{(∞-norm normalization)}
$$

Note:

*   Both are just **directional scalings** of the same residual vector.
*   They **preserve** the direction of  $r_{\text{ls}}$ , but scale its magnitude to make it norm-bounded.

* * *

✅ Step 4.2: Are  $\hat{\nu}, \tilde{\nu}$  feasible for the dual?
-----------------------------------------------------------------

Recall: the dual constraints are:

$$
\boxed{ \begin{aligned} A^T \nu &= 0 \quad \text{(orthogonal to columns of A)} \\ \|\nu\|_1 &\le 1 \\ \end{aligned} }
$$

Let’s check each vector.

* * *

### ✅ 1. Orthogonality constraint:  $A^T \nu = 0$ 

We are told that the residual  $r_{\text{ls}}$  satisfies:

$$
A^T (Ax_{\text{ls}} - b) = -A^T r_{\text{ls}} = 0 \quad \Rightarrow \quad A^T r_{\text{ls}} = 0
$$

So  $r_{\text{ls}} \in \text{null}(A^T)$ , meaning:

$$
A^T r_{\text{ls}} = 0 \Rightarrow A^T \hat{\nu} = 0, \quad A^T \tilde{\nu} = 0
$$

Why? Because scaling by a scalar doesn’t change orthogonality.

✅ So both vectors satisfy  $A^T \nu = 0$ .

* * *

### ✅ 2.  $\ell_1$ \-norm constraint:  $\|\nu\|_1 \le 1$ 

Let’s compute:

*    $\|\hat{\nu}\|_1 = \left\| \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} \right\|_1 = 1$ 
*    $\|\tilde{\nu}\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_\infty} \ge 1$ 

So:

*    $\hat{\nu}$  is feasible
*    $\tilde{\nu}$  may **not** be feasible unless  $\|r_{\text{ls}}\|_1 \le \|r_{\text{ls}}\|_\infty$  (which never happens unless vector is sparse with one nonzero)

Therefore, **only  $\hat{\nu}$ ** is always dual feasible.

* * *

✅ Step 4.3: Use dual objective to compute lower bounds
------------------------------------------------------

Dual objective is:

$$
\text{maximize } \nu^T b \quad \text{(for feasible } \nu)
$$

We compute:

* * *

### 🔷 1. Bound from  $\hat{\nu}$ :

$$
\hat{\nu} = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} \quad \Rightarrow \quad \hat{\nu}^T b = \frac{r_{\text{ls}}^T b}{\|r_{\text{ls}}\|_1}
$$

But remember:

$$
r_{\text{ls}} = b - Ax_{\text{ls}} \Rightarrow r_{\text{ls}}^T b = b^T r_{\text{ls}} = \|r_{\text{ls}}\|_2^2 + x_{\text{ls}}^T A^T r_{\text{ls}} = \|r_{\text{ls}}\|_2^2 + 0
$$

Because  $A^T r_{\text{ls}} = 0$ 

So:

$$
\boxed{ \hat{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} } \quad \text{(valid lower bound)}
$$

* * *

### 🔷 2. Bound from  $\tilde{\nu}$ :

$$
\tilde{\nu} = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} \quad \Rightarrow \quad \tilde{\nu}^T b = \frac{r_{\text{ls}}^T b}{\|r_{\text{ls}}\|_\infty} = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty}
$$

But in this case:

*   It is a **better (larger)** numerical value
*   However,  $\tilde{\nu}$  is **not necessarily feasible** (if  $\|\tilde{\nu}\|_1 > 1$ ), so we can’t always use it

If  $\tilde{\nu}$  is feasible (i.e.  $\|r_{\text{ls}}\|_1 \le \|r_{\text{ls}}\|_\infty$ ), then:

$$
\boxed{ \tilde{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty} } \quad \text{(valid lower bound only if feasible)}
$$

Otherwise: discard.

* * *

✅ Final Summary of All Bounds
-----------------------------

Let’s gather everything:

| Bound Type | Expression | When Valid | Value |
| --- | --- | --- | --- |
| 🔼 **Upper bound** (from Step 2) |  $\|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty$  | Always | Loose but safe |
| 🔽 **Lower bound** via  $\hat{\nu}$  |  $\|Ax_{\text{cheb}} - b\|_\infty \ge \dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}$  | Always | Safe |
| 🔽 **Lower bound** via  $\tilde{\nu}$  |  $\|Ax_{\text{cheb}} - b\|_\infty \ge \dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty}$  | Only if feasible | Tighter |

So:

*    $\hat{\nu}$  is always dual feasible → always safe to use
*    $\tilde{\nu}$  may violate  $\|\nu\|_1 \le 1$  → check before using

* * *

✅ Final Takeaways from Exercise 5.6
-----------------------------------

*   The least-squares solution is **not optimal** for ∞-norm error, but its ∞-norm error is upper bounded by  $\sqrt{m}$  times the optimal one.
*   The **duality-based lower bounds** give us certificates for how small the true Chebyshev error can be.
*   These dual bounds come **for free** if you’ve already computed the least-squares solution (no extra optimization required).

* * *

Would you like me to summarize all this in a compact "one-sheet" version for your notes or course materials?

## Response:
Sure — here is the **final full solution for part (a)** of Exercise 5.6 (Boyd & Vandenberghe), clearly, cleanly, and self-contained:

* * *

✅ Exercise 5.6(a) — Upper bound on ∞-norm error of least-squares solution
-------------------------------------------------------------------------

We are given:

*   A matrix  $A \in \mathbb{R}^{m \times n}$  with **full column rank**  $\text{rank}(A) = n$ 
*   A vector  $b \in \mathbb{R}^m$ 
*   Two problems:
    *   **Chebyshev (∞-norm) approximation**:
        $$
        x_{\text{cheb}} := \arg\min_x \|Ax - b\|_\infty
        $$
    *   **Least-squares (2-norm) approximation**:
        $$
        x_{\text{ls}} := \arg\min_x \|Ax - b\|_2 = (A^T A)^{-1} A^T b
        $$

We want to **compare**:

$$
\|Ax_{\text{ls}} - b\|_\infty \quad \text{vs.} \quad \|Ax_{\text{cheb}} - b\|_\infty
$$

* * *

### 🎯 Goal:

**Prove** the inequality:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

This tells us that the ∞-norm error from the **least-squares solution** is at most  $\sqrt{m}$  times larger than the optimal ∞-norm error.

* * *

### 🧠 Key facts:

For any vector  $z \in \mathbb{R}^m$ , we have:

$$
\boxed{ \|z\|_\infty \le \|z\|_2 \le \sqrt{m} \cdot \|z\|_\infty } \quad \text{(norm equivalence)}
$$

* * *

### ✅ Step-by-step proof:

Let:

*    $r_{\text{ls}} := Ax_{\text{ls}} - b$ 
*    $r_{\text{cheb}} := Ax_{\text{cheb}} - b$ 
    1.  By norm inequality:
    $$
    \|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2
    $$
2.  By definition of  $x_{\text{ls}}$  as 2-norm minimizer:
    $$
    \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2
    $$
3.  Again by norm inequality:
    $$
    \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty
    $$

Chaining these:

$$
\|Ax_{\text{ls}} - b\|_\infty = \|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_2 \le \|r_{\text{cheb}}\|_2 \le \sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty = \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty
$$

* * *

### ✅ Final Result:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty } \quad \text{(proved)}
$$

This shows that the 2-norm solution is at worst  $\sqrt{m}$ \-suboptimal when judged under ∞-norm.

* * *

Let me know if you want the one-sheet summary for all of Exercise 5.6 (including part b)!

## Response:
Here is a **clean, complete, rigorous final solution for Exercise 5.6(b)** from Boyd & Vandenberghe — fully self-contained.

* * *

✅ Exercise 5.6(b) — Dual-based lower bounds for Chebyshev approximation
-----------------------------------------------------------------------

* * *

### 🎯 Problem:

Given the Chebyshev (∞-norm) approximation problem:

$$
\min_x \|Ax - b\|_\infty
$$

Its **dual** is derived in Section 5.6 (page 254), and can be written as:

$$
\boxed{ \begin{aligned} \max_{\nu \in \mathbb{R}^m} \quad & \nu^T b \\ \text{subject to} \quad & \|\nu\|_1 \le 1 \\ & A^T \nu = 0 \end{aligned} } \tag{1}
$$

By **weak duality**, any feasible  $\nu$  gives a **lower bound**:

$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \nu^T b }
$$

We now construct two **candidate dual vectors** from the **least-squares residual**:

$$
r_{\text{ls}} := b - Ax_{\text{ls}} \neq 0
$$

* * *

### 🔧 Construct dual candidates:

Let:

1.  **1-norm normalized vector**:
    $$
    \hat{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}
    $$
2.  **∞-norm normalized vector**:
    $$
    \tilde{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty}
    $$

* * *

### ✅ Check feasibility of each vector for the dual:

#### 1\. Orthogonality:

We know from least-squares theory that:

$$
A^T r_{\text{ls}} = 0 \quad \Rightarrow \quad A^T \hat{\nu} = A^T \tilde{\nu} = 0
$$

✅ Both satisfy  $A^T \nu = 0$ 

#### 2\. 1-norm bound:

*    $\|\hat{\nu}\|_1 = 1$  ✅
*    $\|\tilde{\nu}\|_1 = \dfrac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_\infty} \ge 1$ 

✅  $\hat{\nu}$  is always feasible  
⚠️  $\tilde{\nu}$  is **not always feasible**

* * *

### 🧮 Compute lower bounds:

**Dual objective** is  $\nu^T b$ 

* * *

#### For  $\hat{\nu}$ :

$$
\begin{aligned} \hat{\nu}^T b &= \frac{r_{\text{ls}}^T b}{\|r_{\text{ls}}\|_1} = \frac{r_{\text{ls}}^T (Ax_{\text{ls}} + r_{\text{ls}})}{\|r_{\text{ls}}\|_1} = \frac{r_{\text{ls}}^T Ax_{\text{ls}} + \|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \end{aligned}
$$

But from least-squares orthogonality:

$$
r_{\text{ls}}^T A = 0 \quad \Rightarrow \quad r_{\text{ls}}^T Ax_{\text{ls}} = 0
$$

So:

$$
\boxed{ \hat{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} } \quad \text{(valid lower bound)}
$$

* * *

#### For  $\tilde{\nu}$ :

Assuming  $\tilde{\nu}$  is feasible (i.e.,  $\|\tilde{\nu}\|_1 \le 1$ ), we get:

$$
\boxed{ \tilde{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty} } \quad \text{(only valid if } \|\tilde{\nu}\|_1 \le 1 \text{)}
$$

* * *

📊 Compare bounds
-----------------

| Method | Bound on  $\|Ax_{\text{cheb}} - b\|_\infty$  | Always valid? |
| --- | --- | --- |
| 🔼 Upper bound from part (a) |  $\sqrt{m} \cdot \|r_{\text{cheb}}\|_\infty$  | ✅ |
| 🔽 Lower bound via  $\hat{\nu}$  |  $\dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}$  | ✅ |
| 🔽 Lower bound via  $\tilde{\nu}$  |  $\dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty}$  | ❌ Only if feasible |

**Which is better?**  
If feasible,  $\tilde{\nu}^T b > \hat{\nu}^T b$  (since  $\|r_{\text{ls}}\|_\infty \le \|r_{\text{ls}}\|_1$ ), so it gives a **tighter bound**.

Otherwise,  $\hat{\nu}$  is **safe and always usable**.

* * *

✅ Final boxed answers
---------------------

**(1) Dual formulation:**

$$
\boxed{ \max_\nu \ \nu^T b \quad \text{s.t.} \quad \|\nu\|_1 \le 1, \quad A^T \nu = 0 }
$$

**(2) Dual feasible vectors:**

$$
\boxed{ \hat{\nu} = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \quad \tilde{\nu} = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} }
$$

**(3) Bounds:**

$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \quad \text{(always valid)} }
$$
 
$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty} \quad \text{(if feasible)} }
$$

* * *

This completes Exercise 5.6 — both primal inequality and dual certificate bounds, fully unpacked.

Let me know if you want these rendered as a printable PDF / typeset LaTeX sheet.

## Response:
Absolutely — let's now **unpack part (b) of Exercise 5.6** in the same ultra-granular, step-by-step, from-scratch style. We’ll make everything crystal clear for a newcomer.

* * *

🧭 What are we doing in Part (b)?
---------------------------------

We're continuing from the Chebyshev approximation problem:

$$
\min_x \|Ax - b\|_\infty
$$

This problem minimizes the **maximum residual error** — i.e., the largest entry in absolute value of  $r = Ax - b \in \mathbb{R}^m$ . It’s a **minimax** or **worst-case** approximation.

In part (a), we upper-bounded the ∞-norm error from the least-squares solution (2-norm minimizer) using a  $\sqrt{m}$  factor.

Now, in part (b), we want to:

> **Construct lower bounds** on the Chebyshev approximation error  
> without solving the optimization problem directly,  
> using **duality** and the known least-squares residual.

* * *

✅ Step 1: Recall the dual problem (from Section 5.6)
----------------------------------------------------

We already derived in previous steps that the **dual** of the Chebyshev approximation problem is:

$$
\boxed{ \max_{\nu \in \mathbb{R}^m} \ \nu^T b \quad \text{subject to:} \quad \| \nu \|_1 \le 1, \quad A^T \nu = 0 } \tag{D}
$$
*   This is a **linear program**.
*   The dual objective  $\nu^T b$  gives a **lower bound** on the primal optimal value:
    $$
    \nu^T b \le \min_x \|Ax - b\|_\infty = \|Ax_{\text{cheb}} - b\|_\infty
    $$

✅ So **any feasible  $\nu$ ** (i.e., satisfying the dual constraints) gives a valid lower bound.

* * *

✅ Step 2: Define the least-squares residual
-------------------------------------------

We are told to use the **least-squares residual**:

$$
r_{\text{ls}} := b - Ax_{\text{ls}} \in \mathbb{R}^m
$$

This is the vector of errors when using the 2-norm optimal solution.

From least-squares theory:

$$
x_{\text{ls}} := (A^T A)^{-1} A^T b \quad \Rightarrow \quad A^T r_{\text{ls}} = 0
$$

✅ This tells us that  $r_{\text{ls}} \in \text{null}(A^T)$ , which is exactly what we want for dual feasibility.

So we want to use this vector  $r_{\text{ls}}$  to **construct feasible dual variables**  $\nu$ .

* * *

✅ Step 3: Construct two candidate dual vectors
----------------------------------------------

We want to take  $r_{\text{ls}}$ , and **normalize it** to satisfy  $\| \nu \|_1 \le 1$ .

We try two normalizations:

* * *

### 🔹 Option 1 — 1-norm normalization:

$$
\boxed{ \hat{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} }
$$
*   The denominator  $\|r_{\text{ls}}\|_1$  is a scalar.
*   This guarantees:
    *    $A^T \hat{\nu} = 0$  ✅ (since  $r_{\text{ls}} \in \text{null}(A^T)$ )
    *    $\|\hat{\nu}\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1} = 1$  ✅

Therefore,  $\hat{\nu}$  is **dual feasible**.

* * *

### 🔹 Option 2 — ∞-norm normalization:

$$
\boxed{ \tilde{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} }
$$
*   This guarantees:
    *    $A^T \tilde{\nu} = 0$  ✅ (same reason)
    *   But  $\|\tilde{\nu}\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_\infty} \ge 1$ 

So  $\tilde{\nu}$  **is not necessarily feasible** — only if  $\|r_{\text{ls}}\|_1 \le \|r_{\text{ls}}\|_\infty$ , which is rare.

Hence:

*    $\hat{\nu}$  is always feasible ✅
*    $\tilde{\nu}$  might not be ❌

* * *

✅ Step 4: Plug into the dual objective
--------------------------------------

The dual objective is:

$$
\nu^T b \le \|Ax_{\text{cheb}} - b\|_\infty
$$

Let’s compute  $\nu^T b$  for both cases.

* * *

### 🔸 For  $\hat{\nu} = \dfrac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}$ 

$$
\hat{\nu}^T b = \frac{r_{\text{ls}}^T b}{\|r_{\text{ls}}\|_1} = \frac{(b - Ax_{\text{ls}})^T b}{\|r_{\text{ls}}\|_1}
$$

Now expand:

$$
r_{\text{ls}}^T b = b^T b - x_{\text{ls}}^T A^T b
$$

But from least-squares optimality:

$$
x_{\text{ls}} = (A^T A)^{-1} A^T b \quad \Rightarrow \quad A^T (Ax_{\text{ls}} - b) = 0 \quad \Rightarrow \quad A^T r_{\text{ls}} = 0
$$

So:

$$
r_{\text{ls}}^T Ax_{\text{ls}} = 0 \quad \Rightarrow \quad r_{\text{ls}}^T b = \|r_{\text{ls}}\|_2^2
$$

Therefore:

$$
\boxed{ \hat{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} } \quad \text{(lower bound on Chebyshev error)}
$$

✅ Always valid.

* * *

### 🔸 For  $\tilde{\nu} = \dfrac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty}$ 

If  $\tilde{\nu}$  is feasible (i.e.,  $\|\tilde{\nu}\|_1 \le 1$ ), then:

$$
\boxed{ \tilde{\nu}^T b = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty} } \quad \text{(tighter lower bound if feasible)}
$$

* * *

✅ Step 5: Compare bounds and close the argument
-----------------------------------------------

### 🔼 From part (a):

We had the upper bound:

$$
\boxed{ \|Ax_{\text{ls}} - b\|_\infty \le \sqrt{m} \cdot \|Ax_{\text{cheb}} - b\|_\infty }
$$

### 🔽 From part (b):

We now have dual-based **lower bounds**:

| Bound source | Value | Feasibility |
| --- | --- | --- |
|  $\hat{\nu}$  |  $\dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}$  | Always feasible ✅ |
|  $\tilde{\nu}$  |  $\dfrac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty}$  | Only if  $\|r_{\text{ls}}\|_1 \le \|r_{\text{ls}}\|_\infty$  ❌ usually invalid |

So:

*   If you're unsure: **use  $\hat{\nu}$ ** — always valid
*   If you check feasibility and it passes, ** $\tilde{\nu}$ ** gives a tighter (larger) bound

* * *

📦 Final Summary
----------------

Let’s summarize part (b) completely:

### ✅ The dual of the Chebyshev problem is:

$$
\boxed{ \max_\nu \nu^T b \quad \text{s.t.} \quad A^T \nu = 0, \ \|\nu\|_1 \le 1 }
$$

### ✅ We construct feasible dual points from the least-squares residual:

$$
\boxed{ \hat{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} \quad\text{and}\quad \tilde{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} }
$$

### ✅ These give lower bounds:

$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \quad \text{(always valid)} }
$$
 
$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_\infty} \quad \text{(if feasible)} }
$$

✅ These can be compared to the upper bound from part (a) to bracket the true optimal error  $\|Ax_{\text{cheb}} - b\|_\infty$ .

* * *

Would you like a LaTeX or typeset note version of both parts now?

## Response:
Excellent. Let’s now **slow down and fully unpack the first three steps of Part (b)** of Exercise 5.6, **line by line, from scratch**, as a complete newcomer walkthrough.

We’ll go step-by-step:

* * *

✅ Step 1 — Understanding what we want: a **lower bound** on Chebyshev error
---------------------------------------------------------------------------

* * *

### 🎯 The primal problem:

We are working with the **Chebyshev approximation** problem, which is:

$$
\min_x \|Ax - b\|_\infty
$$

This means:

> Among all possible vectors  $x \in \mathbb{R}^n$ , find one that makes the residual  $Ax - b \in \mathbb{R}^m$  as **uniformly small as possible**, by minimizing the **largest absolute value** among its entries.

We don’t have a closed-form for the Chebyshev solution  $x_{\text{cheb}}$ , but we want to **estimate** the true minimum value:

$$
\|Ax_{\text{cheb}} - b\|_\infty
$$

* * *

### ❗Key goal of part (b):

We already derived the **upper bound** on this quantity in part (a) using the least-squares solution. Now we want to:

> Use **duality theory** to compute **lower bounds** on this quantity, by constructing feasible points in the **dual** problem.

Why? Because in any convex minimization problem:

$$
\boxed{ \text{Dual value } \le \text{Primal optimal value} }
$$

That’s called **weak duality** — and it lets us safely **underestimate** the true solution by solving or evaluating the dual.

* * *

✅ Step 2 — Recall or derive the dual problem
--------------------------------------------

We’re told (and we’ve derived) that the dual of the Chebyshev problem is:

$$
\boxed{ \begin{aligned} \max_{\nu \in \mathbb{R}^m} \quad & \nu^T b \\ \text{subject to} \quad & \|\nu\|_1 \le 1 \\ & A^T \nu = 0 \end{aligned} } \tag{★}
$$

* * *

### 🧠 Why this makes sense:

*    $\nu^T b$  is the **dual objective** — it gives us a lower bound on  $\|Ax - b\|_\infty$ 
*   The constraint  $A^T \nu = 0$  ensures compatibility with the primal's residual structure
*   The constraint  $\|\nu\|_1 \le 1$  comes from the dual norm of the ∞-norm:
    $$
    \text{dual of } \ell_\infty = \ell_1
    $$

* * *

### ✅ So the plan is:

We’ll **construct a vector  $\nu$ ** satisfying:

*    $A^T \nu = 0$ 
*    $\|\nu\|_1 \le 1$ 

Then plug it into  $\nu^T b$  to get:

$$
\boxed{ \|Ax_{\text{cheb}} - b\|_\infty \ge \nu^T b } \quad \text{(dual lower bound)}
$$

* * *

✅ Step 3 — Construct dual-feasible  $\nu$  from least-squares residual
----------------------------------------------------------------------

Here’s the clever trick.

We already **know** the least-squares solution  $x_{\text{ls}}$ , which minimizes  $\|Ax - b\|_2$ , and we can compute its residual:

$$
r_{\text{ls}} := b - Ax_{\text{ls}}
$$

### ❗Key fact:

From least-squares optimality, the residual  $r_{\text{ls}}$  is **orthogonal** to the column space of  $A$ :

$$
\boxed{ A^T r_{\text{ls}} = 0 }
$$

This tells us:

*    $r_{\text{ls}} \in \text{null}(A^T)$ 
*   So **any scaling of  $r_{\text{ls}}$ ** also lies in the nullspace:
    $$
    A^T \left( \alpha \cdot r_{\text{ls}} \right) = \alpha \cdot A^T r_{\text{ls}} = 0 \quad \forall \alpha \in \mathbb{R}
    $$

Therefore, we can **use  $r_{\text{ls}}$ ** as a building block for a dual vector  $\nu$  satisfying  $A^T \nu = 0$ .

* * *

### Now we need to enforce:  $\|\nu\|_1 \le 1$ 

We do this by **normalizing**  $r_{\text{ls}}$ :

* * *

### 🔹 Candidate 1: Normalize by  $\ell_1$ \-norm

Let’s define:

$$
\boxed{ \hat{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} }
$$

Check feasibility:

*    $A^T \hat{\nu} = A^T \left( \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1} \right) = 0$ 
*    $\|\hat{\nu}\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1} = 1$ 

✅ This is a valid dual point. Always feasible.

* * *

### 🔹 Candidate 2: Normalize by  $\ell_\infty$ \-norm

Define:

$$
\boxed{ \tilde{\nu} := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_\infty} }
$$

Check feasibility:

*    $A^T \tilde{\nu} = 0$  ✅
*    $\|\tilde{\nu}\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_\infty}$ 

Now:

*   If  $\|r_{\text{ls}}\|_1 \le \|r_{\text{ls}}\|_\infty$ , then  $\|\tilde{\nu}\|_1 \le 1$  ✅ feasible
*   But usually  $\|r_{\text{ls}}\|_1 \gg \|r_{\text{ls}}\|_\infty$  (unless the residual is sparse), so:
    
$$
\boxed{ \tilde{\nu} \text{ is usually not dual-feasible} }
$$

* * *

So:

*    $\hat{\nu}$ : always valid, safe bound
*    $\tilde{\nu}$ : better bound if feasible, but must be checked

* * *

Would you like me to now walk through **Steps 4–5**, where we compute and interpret the lower bounds  $\nu^T b$ ?

## Response:
Thought for 30s

Below is a single, complete, rigorous, step-by-step solution to **Exercise 5.6 (a)–(b)**.

* * *

Problem setup and notation
--------------------------

Let  $A\in\mathbb R^{m\times n}$  with  $\operatorname{rank}(A)=n$  (full column rank) and  $b\in\mathbb R^m$ .

Define the **Chebyshev (∞-norm) approximation problem**

$$
\min_{x\in\mathbb R^n}\ \|Ax-b\|_\infty. \tag{P\(_\infty\)}
$$

Let  $x_{\text{ch}}$  be an optimal solution and denote the optimal value by

$$
p^\star := \|Ax_{\text{ch}}-b\|_\infty.
$$

Define the **least-squares (2-norm) approximation problem**

$$
\min_{x\in\mathbb R^n}\ \|Ax-b\|_2. \tag{P\(_2\)}
$$

Because  $A$  has full column rank, the least-squares minimizer is unique and equals

$$
x_{\text{ls}} = (A^TA)^{-1}A^Tb.
$$

Define the least-squares residual

$$
r_{\text{ls}} := b-Ax_{\text{ls}}.
$$

Note  $\|Ax_{\text{ls}}-b\|_\infty = \|-r_{\text{ls}}\|_\infty = \|r_{\text{ls}}\|_\infty$ .

We will use the standard norm relations (given):

$$
\frac{1}{\sqrt m}\|z\|_2 \le \|z\|_\infty \le \|z\|_2,\qquad \forall z\in\mathbb R^m.
$$

Equivalently,

$$
\|z\|_2 \le \sqrt m\,\|z\|_\infty \quad \text{and}\quad \|z\|_\infty\le \|z\|_2.
$$

* * *

(a) Prove   $\ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty$ 
-------------------------------------------------------------------------------------

### Step 1: Start with the LS ∞-error and bound it by its 2-error

Apply  $\|z\|_\infty \le \|z\|_2$  to  $z = Ax_{\text{ls}}-b$ :

$$
\|Ax_{\text{ls}}-b\|_\infty \le \|Ax_{\text{ls}}-b\|_2. \tag{1}
$$

### Step 2: Use the defining optimality of  $x_{\text{ls}}$  for the 2-norm problem

Since  $x_{\text{ls}}$  minimizes  $\|Ax-b\|_2$  over all  $x$ , it does no worse than the particular choice  $x=x_{\text{ch}}$ :

$$
\|Ax_{\text{ls}}-b\|_2 \le \|Ax_{\text{ch}}-b\|_2. \tag{2}
$$

### Step 3: Relate the Chebyshev residual’s 2-norm to its ∞-norm

Apply  $\|z\|_2 \le \sqrt m\,\|z\|_\infty$  to  $z = Ax_{\text{ch}}-b$ :

$$
\|Ax_{\text{ch}}-b\|_2 \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty. \tag{3}
$$

### Step 4: Chain (1)–(3)

$$
\|Ax_{\text{ls}}-b\|_\infty \le \|Ax_{\text{ls}}-b\|_2 \le \|Ax_{\text{ch}}-b\|_2 \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty.
$$

So

 $$
\boxed{\ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty.\ }
$$

A useful rearrangement (a **lower bound** on the unknown optimum  $p^\star$ ) is:

 $$
\boxed{\ p^\star=\|Ax_{\text{ch}}-b\|_\infty \ge \frac{1}{\sqrt m}\|Ax_{\text{ls}}-b\|_\infty = \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty.\ }
$$

* * *

(b) Construct dual-feasible  $\nu$  from  $r_{\text{ls}}$ , compute the bounds, compare
---------------------------------------------------------------------------------------

### Step 0: The dual problem and the “lower bound machine”

You are given the dual of  $(P_\infty)$ :

$$
\boxed{ \begin{aligned} \max_{\nu\in\mathbb R^m}\quad & b^T\nu\\ \text{s.t.}\quad & \|\nu\|_1 \le 1,\\ & A^T\nu = 0. \end{aligned}} \tag{D}
$$

**Weak duality** says: for any feasible  $\nu$ ,

$$
b^T\nu \ \le\ p^\star=\min_x\|Ax-b\|_\infty.
$$

So every feasible  $\nu$  gives a certified **lower bound**  $b^T\nu$  on the optimal Chebyshev error.

* * *

### Step 1: Show  $A^T r_{\text{ls}} = 0$  (normal equations)

Least squares minimizes  $\|Ax-b\|_2^2$ . The gradient is

$$
\nabla_x \|Ax-b\|_2^2 = 2A^T(Ax-b).
$$

At the minimizer  $x_{\text{ls}}$ , first-order optimality gives

$$
A^T(Ax_{\text{ls}}-b)=0 \quad\Longleftrightarrow\quad A^T(b-Ax_{\text{ls}})=0 \quad\Longleftrightarrow\quad \boxed{A^T r_{\text{ls}}=0.}
$$

* * *

### Step 2: Define the two proposed dual candidates and prove feasibility

Assume  $r_{\text{ls}}\neq 0$ . Define

$$
\hat\nu := -\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \qquad \bar\nu := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}.
$$

#### (i) Check the  $\ell_1$  constraint

$$
\|\bar\nu\|_1 = \left\|\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1} = 1 \le 1.
$$

Similarly  $\|\hat\nu\|_1 = 1\le 1$  (sign doesn’t affect  $\ell_1$ ).

#### (ii) Check the orthogonality constraint

Using  $A^Tr_{\text{ls}}=0$ ,

$$
A^T\bar\nu = A^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) =\frac{1}{\|r_{\text{ls}}\|_1}A^Tr_{\text{ls}}=0.
$$

Similarly  $A^T\hat\nu=0$ .

So both  $\hat\nu$  and  $\bar\nu$  are feasible for (D).

* * *

### Step 3: Evaluate the dual objectives  $b^T\hat\nu$  and  $b^T\bar\nu$ 

We first compute  $b^T r_{\text{ls}}$ .

Since  $r_{\text{ls}} = b-Ax_{\text{ls}}$ , we can write  $b = Ax_{\text{ls}} + r_{\text{ls}}$ . Then

$$
b^T r_{\text{ls}} = (Ax_{\text{ls}} + r_{\text{ls}})^T r_{\text{ls}} = x_{\text{ls}}^T A^T r_{\text{ls}} + r_{\text{ls}}^T r_{\text{ls}}.
$$

But  $A^T r_{\text{ls}}=0$ , so the first term vanishes:

$$
b^T r_{\text{ls}} = \|r_{\text{ls}}\|_2^2.
$$

Now:

$$
b^T\bar\nu = b^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{b^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} = \boxed{\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$
 
$$
b^T\hat\nu = b^T\left(-\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = -\boxed{\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$

By weak duality, both are lower bounds on  $p^\star$ :

$$
\boxed{p^\star \ge b^T\bar\nu = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}},\qquad \boxed{p^\star \ge b^T\hat\nu = -\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$

* * *

### Step 4: Which lower bound is better?

Since  $\|r_{\text{ls}}\|_2^2/\|r_{\text{ls}}\|_1>0$ , we have:

*    $b^T\bar\nu$  is **positive**
*    $b^T\hat\nu$  is **negative**

Because  $p^\star=\min_x\|Ax-b\|_\infty \ge 0$  always, the negative lower bound is essentially useless (it is true but very weak).

So the better bound is:

$$
\boxed{\text{Better lower bound: } \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.}
$$

* * *

### Step 5: Compare the dual lower bound to the bound from part (a)

From part (a) we obtained the (computable) lower bound:

$$
p^\star \ge \frac{1}{\sqrt m}\|Ax_{\text{ls}}-b\|_\infty = \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty. \tag{LB\(_a\)}
$$

From part (b) we obtained the dual-feasible lower bound:

$$
p^\star \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}. \tag{LB\(_b\)}
$$

Now compare them. Using Cauchy–Schwarz,  $\|r\|_1 \le \sqrt m\,\|r\|_2$ . Therefore

$$
\frac{\|r\|_2^2}{\|r\|_1} \ \ge\ \frac{\|r\|_2^2}{\sqrt m\,\|r\|_2} = \frac{1}{\sqrt m}\|r\|_2.
$$

And since  $\|r\|_2 \ge \|r\|_\infty$ ,

$$
\frac{1}{\sqrt m}\|r\|_2 \ge \frac{1}{\sqrt m}\|r\|_\infty.
$$

Combine:

 $$
\boxed{\ \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \ \ge\ \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty. \ }
$$

So the dual lower bound from  $\bar\nu$  is **always at least as good as** the part (a) lower bound (and often strictly better).

* * *

Final “closed” summary (what you can compute from  $x_{\text{ls}}$ )
--------------------------------------------------------------------

Let  $r_{\text{ls}}=b-Ax_{\text{ls}}\neq 0$ . Then:

*   **Upper bound on the unknown optimum** (just evaluate the primal at  $x_{\text{ls}}$ ):
    $$
    p^\star \le \|Ax_{\text{ls}}-b\|_\infty = \|r_{\text{ls}}\|_\infty.
    $$
*   **Lower bound from part (a)**:
    $$
    p^\star \ge \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty.
    $$
*   **Dual-based lower bound from part (b)** (better):
    $$
    p^\star \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
    $$
*   Among the two proposed dual vectors,  $\bar\nu = r_{\text{ls}}/\|r_{\text{ls}}\|_1$  yields the useful positive bound;  $\hat\nu$  yields the same magnitude but negative, hence weaker.

That completes the full solution.

## Response:
Thought for 26s

Got it. I’ll give you a **more detailed, more rigorous, more “nothing implicit”** solution for **both (a) and (b)**, including (i) the norm inequalities, (ii) why least-squares gives the “orthogonality” condition, (iii) exactly why dual-feasible  $\nu$  produces a **lower bound** on the Chebyshev optimum, and (iv) the clean comparison to the bound from (a). No leaps.

* * *

0) What the problem is comparing
--------------------------------

You have two different ways to measure the residual error  $Ax-b\in\mathbb R^m$ .

*   Chebyshev (∞-norm, “worst coordinate”):
    
$$
(P_\infty)\quad \min_{x\in\mathbb R^n}\ \|Ax-b\|_\infty, \qquad \|y\|_\infty := \max_{i=1,\dots,m}|y_i|.
$$

Let an optimizer be  $x_{\text{ch}}$  and define the optimal value

$$
p^\star := \|Ax_{\text{ch}}-b\|_\infty.
$$
*   Least squares (2-norm, “energy”):
    
$$
(P_2)\quad \min_{x\in\mathbb R^n}\ \|Ax-b\|_2, \qquad \|y\|_2 := \sqrt{\sum_{i=1}^m y_i^2}.
$$

Let the (unique) minimizer be  $x_{\text{ls}}$  (unique because  $\operatorname{rank}(A)=n$ ), and define the least-squares residual

$$
r_{\text{ls}} := b-Ax_{\text{ls}}.
$$

Note:  $Ax_{\text{ls}}-b = -r_{\text{ls}}$ , so  $\|Ax_{\text{ls}}-b\|_\infty=\|r_{\text{ls}}\|_\infty$ , etc.

The point of the exercise: **If you already computed  $x_{\text{ls}}$ , what can you say about the unknown Chebyshev optimum  $p^\star$ ?**

* * *

1) The norm inequalities (proved, not assumed)
----------------------------------------------

You are allowed to use

$$
\frac{1}{\sqrt m}\|z\|_2 \le \|z\|_\infty \le \|z\|_2 \quad \forall z\in\mathbb R^m.
$$

Let me prove both sides so nothing feels like magic.

### 1.1 Prove  $\|z\|_\infty \le \|z\|_2$ 

Let  $j$  be an index that attains the max:  $|z_j|=\|z\|_\infty$ .  
Then

$$
\|z\|_2^2=\sum_{i=1}^m z_i^2 \ge z_j^2 = \|z\|_\infty^2.
$$

Taking square roots:

$$
\|z\|_2 \ge \|z\|_\infty.
$$

### 1.2 Prove  $\|z\|_2 \le \sqrt m\,\|z\|_\infty$ 

For every coordinate  $i$ ,  $|z_i| \le \|z\|_\infty$ , so  $z_i^2 \le \|z\|_\infty^2$ . Sum over  $i$ :

$$
\|z\|_2^2=\sum_{i=1}^m z_i^2 \le \sum_{i=1}^m \|z\|_\infty^2 = m\|z\|_\infty^2.
$$

Take square roots:

$$
\|z\|_2 \le \sqrt m\,\|z\|_\infty.
$$

Equivalently  $\frac{1}{\sqrt m}\|z\|_2 \le \|z\|_\infty$ .

* * *

(a) Prove  $\|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty$ 
----------------------------------------------------------------------------------

We want to compare the **∞-error** of the LS solution to the **optimal ∞-error**.

Define two residual vectors:

$$
r_{\text{ls}}^{(A)} := Ax_{\text{ls}}-b,\qquad r_{\text{ch}}^{(A)} := Ax_{\text{ch}}-b.
$$

(Just to remind ourselves these are residuals in the  $Ax-b$  sign convention.)

### Step A1: Convert LS ∞-error to LS 2-error

Using  $\|z\|_\infty \le \|z\|_2$  with  $z=r_{\text{ls}}^{(A)}$ ,

$$
\|Ax_{\text{ls}}-b\|_\infty = \|r_{\text{ls}}^{(A)}\|_\infty \le \|r_{\text{ls}}^{(A)}\|_2 = \|Ax_{\text{ls}}-b\|_2.
$$

### Step A2: Use that  $x_{\text{ls}}$  minimizes the 2-norm residual

By definition of  $x_{\text{ls}}$ ,

$$
\|Ax_{\text{ls}}-b\|_2 \le \|Ax-b\|_2 \quad \forall x.
$$

In particular, choose  $x=x_{\text{ch}}$ :

$$
\|Ax_{\text{ls}}-b\|_2 \le \|Ax_{\text{ch}}-b\|_2.
$$

### Step A3: Convert Chebyshev 2-error to Chebyshev ∞-error

Using  $\|z\|_2 \le \sqrt m\,\|z\|_\infty$  with  $z=r_{\text{ch}}^{(A)}$ ,

$$
\|Ax_{\text{ch}}-b\|_2 \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty.
$$

### Step A4: Chain the three inequalities

Putting A1–A3 together:

$$
\|Ax_{\text{ls}}-b\|_\infty \le \|Ax_{\text{ls}}-b\|_2 \le \|Ax_{\text{ch}}-b\|_2 \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty.
$$

So

 $$
\boxed{\ \|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,\|Ax_{\text{ch}}-b\|_\infty.\ }
$$

A very useful rearrangement (a computable lower bound on the unknown optimum  $p^\star$ ) is:

 $$
\boxed{\ p^\star = \|Ax_{\text{ch}}-b\|_\infty \ge \frac{1}{\sqrt m}\|Ax_{\text{ls}}-b\|_\infty.\ }
$$

* * *

(b) Use the dual to get _explicit lower bounds_ from  $r_{\text{ls}}$ 
----------------------------------------------------------------------

### 2) The dual problem (given)

The dual of  $(P_\infty)$  is:

$$
(D)\quad \max_{\nu\in\mathbb R^m}\ b^T\nu \quad\text{s.t.}\quad \|\nu\|_1 \le 1,\ \ A^T\nu=0.
$$

What part (b) asks you to do:

1.  Using  $r_{\text{ls}}:=b-Ax_{\text{ls}}\neq 0$ , define
    
$$
\hat\nu := -\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \qquad \bar\nu := \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}.
$$
2.  Show both are feasible for (D).
3.  Therefore  $b^T\hat\nu$  and  $b^T\bar\nu$  are lower bounds on  $p^\star$ .
4.  Compare these bounds to the bound from (a).

We’ll do each line carefully.

* * *

2.1 Why dual-feasible  $\nu$  gives a lower bound (weak duality, unpacked)
--------------------------------------------------------------------------

We want to justify:

$$
\text{If } \|\nu\|_1\le 1,\ A^T\nu=0,\ \text{ then } b^T\nu \le p^\star.
$$

A clean way to see it (no black boxes) is to use a basic inequality about norms.

### Fact: For any  $y\in\mathbb R^m$  and any  $\nu$  with  $\|\nu\|_1\le 1$ ,

$$
\nu^T y \le \|y\|_\infty.
$$

Why? Because

$$
\nu^T y = \sum_{i=1}^m \nu_i y_i \le \sum_{i=1}^m |\nu_i||y_i| \le \left(\max_i |y_i|\right)\sum_{i=1}^m |\nu_i| = \|y\|_\infty \|\nu\|_1 \le \|y\|_\infty.
$$

That’s fully explicit: triangle inequality + bounding each  $|y_i|$  by the max.

Now choose  $y = b-Ax$ . Note  $\|b-Ax\|_\infty=\|Ax-b\|_\infty$  (same entries, just sign).  
Then for any  $x$  and any  $\nu$  with  $\|\nu\|_1\le 1$ ,

$$
\nu^T(b-Ax) \le \|Ax-b\|_\infty.
$$

If in addition  $A^T\nu=0$ , then  $\nu^T Ax = x^T(A^T\nu)=0$ , so

$$
\nu^T(b-Ax) = \nu^T b - \nu^T Ax = \nu^T b.
$$

Therefore, for all  $x$ ,

$$
b^T\nu \le \|Ax-b\|_\infty.
$$

Now take the minimum over  $x$  on the right:

$$
b^T\nu \le \min_x \|Ax-b\|_\infty = p^\star.
$$

So indeed any dual-feasible  $\nu$  yields a certified lower bound.

That’s the logic of duality here: feasibility in the dual gives a universal inequality that holds for every primal  $x$ .

* * *

2.2 Show  $A^T r_{\text{ls}}=0$  (least-squares normal equations, fully derived)
--------------------------------------------------------------------------------

This is the key “bridge” from least squares to the dual constraint  $A^T\nu=0$ .

Least squares minimizes  $\|Ax-b\|_2$ . It’s easier (and equivalent) to minimize the square:

$$
\min_x \|Ax-b\|_2^2.
$$

Expand:

$$
\|Ax-b\|_2^2 = (Ax-b)^T(Ax-b) = x^TA^TAx - 2b^TAx + b^Tb.
$$

Differentiate w.r.t.  $x$ . Standard result (you can verify term-by-term):

*   derivative of  $x^TA^TAx$  is  $2A^TAx$ ,
*   derivative of  $-2b^TAx$  is  $-2A^Tb$ ,
*   derivative of constant  $b^Tb$  is 0.

So

$$
\nabla_x \|Ax-b\|_2^2 = 2A^T(Ax-b).
$$

At the minimizer  $x_{\text{ls}}$ , the gradient must be zero:

$$
2A^T(Ax_{\text{ls}}-b)=0 \quad\Longrightarrow\quad A^T(Ax_{\text{ls}}-b)=0 \quad\Longrightarrow\quad A^T(b-Ax_{\text{ls}})=0.
$$

But  $b-Ax_{\text{ls}} = r_{\text{ls}}$ , so

$$
\boxed{A^T r_{\text{ls}}=0.}
$$

Geometric meaning:  $Ax_{\text{ls}}$  is the orthogonal projection of  $b$  onto the column space of  $A$ , and the residual  $r_{\text{ls}}$  is orthogonal to that space.

* * *

2.3 Construct  $\hat\nu,\bar\nu$  and prove feasibility
-------------------------------------------------------

Assume  $r_{\text{ls}}\neq 0$  so  $\|r_{\text{ls}}\|_1>0$  and the definitions make sense:

$$
\hat\nu = -\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}, \qquad \bar\nu = \frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}.
$$

Dual feasibility requires two things:

### (i)  $\|\nu\|_1 \le 1$ 

Compute:

$$
\|\bar\nu\|_1 = \left\|\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right\|_1 = \frac{\|r_{\text{ls}}\|_1}{\|r_{\text{ls}}\|_1} = 1.
$$

Similarly  $\|\hat\nu\|_1=1$  (sign doesn’t change the  $\ell_1$ \-norm).

So both satisfy  $\|\nu\|_1\le 1$ .

### (ii)  $A^T\nu=0$ 

Using  $A^Tr_{\text{ls}}=0$ :

$$
A^T\bar\nu = A^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{1}{\|r_{\text{ls}}\|_1}A^Tr_{\text{ls}}=0.
$$

And

$$
A^T\hat\nu = -\frac{1}{\|r_{\text{ls}}\|_1}A^Tr_{\text{ls}}=0.
$$

Therefore,

$$
\boxed{\hat\nu\ \text{and}\ \bar\nu\ \text{are both feasible for the dual}.}
$$

* * *

2.4 Evaluate the dual objectives  $b^T\hat\nu$  and  $b^T\bar\nu$ 
------------------------------------------------------------------

Since these are feasible, both values are lower bounds on  $p^\star$ . Let’s compute them explicitly.

First compute  $b^T r_{\text{ls}}$ .

Because  $r_{\text{ls}} = b-Ax_{\text{ls}}$ , we can write

$$
b = Ax_{\text{ls}} + r_{\text{ls}}.
$$

Then

$$
b^T r_{\text{ls}} = (Ax_{\text{ls}} + r_{\text{ls}})^T r_{\text{ls}} = (Ax_{\text{ls}})^T r_{\text{ls}} + r_{\text{ls}}^T r_{\text{ls}}.
$$

Now show  $(Ax_{\text{ls}})^T r_{\text{ls}}=0$ . Indeed,

$$
(Ax_{\text{ls}})^T r_{\text{ls}} = x_{\text{ls}}^T A^T r_{\text{ls}} = x_{\text{ls}}^T \cdot 0 = 0.
$$

So

$$
b^T r_{\text{ls}} = r_{\text{ls}}^T r_{\text{ls}} = \|r_{\text{ls}}\|_2^2.
$$

Now compute each objective:

*   For  $\bar\nu$ :
    
$$
b^T\bar\nu = b^T\left(\frac{r_{\text{ls}}}{\|r_{\text{ls}}\|_1}\right) = \frac{b^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} = \boxed{\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$
*   For  $\hat\nu$ :
    
$$
b^T\hat\nu = -\frac{b^T r_{\text{ls}}}{\|r_{\text{ls}}\|_1} = -\boxed{\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$

By weak duality (proved in 2.1),

$$
\boxed{p^\star \ge b^T\bar\nu = \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}, \qquad \boxed{p^\star \ge b^T\hat\nu = -\frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}}.
$$

Which is better? Since  $p^\star\ge 0$  always (norms are nonnegative), the negative bound is automatically weaker. The useful bound is:

$$
\boxed{\text{Best of the two is } \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.}
$$

* * *

2.5 Compare this lower bound to the lower bound from part (a)
-------------------------------------------------------------

From (a), we can rearrange:

$$
\|Ax_{\text{ls}}-b\|_\infty \le \sqrt m\,p^\star \quad\Longrightarrow\quad p^\star \ge \frac{1}{\sqrt m}\|Ax_{\text{ls}}-b\|_\infty.
$$

Since  $\|Ax_{\text{ls}}-b\|_\infty=\|r_{\text{ls}}\|_\infty$ ,

$$
\boxed{p^\star \ge \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty.} \tag{LB\(_a\)}
$$

From (b), we have

$$
\boxed{p^\star \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.} \tag{LB\(_b\)}
$$

Now show  $LB_b \ge LB_a$  (the dual bound is never worse).

Use two standard inequalities (both provable by Cauchy–Schwarz and norm ordering):

1.   $\|r\|_1 \le \sqrt m\,\|r\|_2$ .  
    Proof:  $\|r\|_1=\sum |r_i| \le \sqrt{m}\sqrt{\sum r_i^2}=\sqrt m\,\|r\|_2$ .
2.   $\|r\|_2 \ge \|r\|_\infty$ . (proved earlier)

Then:

$$
\frac{\|r\|_2^2}{\|r\|_1} \ge \frac{\|r\|_2^2}{\sqrt m\,\|r\|_2} = \frac{1}{\sqrt m}\|r\|_2 \ge \frac{1}{\sqrt m}\|r\|_\infty.
$$

Apply this to  $r=r_{\text{ls}}$ :

$$
\boxed{ \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \ge \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty. }
$$

So the dual-based lower bound from (b) is always at least as strong as the crude lower bound you can extract from (a).

* * *

3) Edge case: what if  $r_{\text{ls}}=0$ ?
------------------------------------------

The problem assumes  $r_{\text{ls}}\neq 0$  so division by  $\|r_{\text{ls}}\|_1$  is defined. But it’s worth knowing what happens:

If  $r_{\text{ls}}=0$ , then  $b=Ax_{\text{ls}}$ , so you can fit exactly. Then

$$
p^\star = \min_x \|Ax-b\|_\infty = 0.
$$

Everything becomes trivial.

* * *

4) Final “closed-form” conclusion you can compute from least squares
--------------------------------------------------------------------

Once you compute  $x_{\text{ls}}$  and  $r_{\text{ls}}=b-Ax_{\text{ls}}$ , you have:

*   A trivial **upper bound** on the Chebyshev optimum (evaluate primal at  $x_{\text{ls}}$ ):
    
$$
p^\star \le \|Ax_{\text{ls}}-b\|_\infty = \|r_{\text{ls}}\|_\infty.
$$
*   A dual-based **lower bound** (best bound from part (b)):
    
$$
p^\star \ge \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1}.
$$
*   And a weaker lower bound implied by part (a):
    
$$
p^\star \ge \frac{1}{\sqrt m}\|r_{\text{ls}}\|_\infty,
$$

which is always dominated by the dual bound above.

So you can **sandwich** the unknown optimum  $p^\star$  as:

$$
\boxed{ \frac{\|r_{\text{ls}}\|_2^2}{\|r_{\text{ls}}\|_1} \ \le\ p^\star \ \le\ \|r_{\text{ls}}\|_\infty. }
$$

That is the “complete closure”: without solving the Chebyshev LP, you still get a certified interval where the optimal worst-case error must lie.

* * *

If you want, I can also rewrite the whole thing as a compact “exam solution” version (still correct, just shorter), or I can add a small numeric toy example to make each inequality feel physically real.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)