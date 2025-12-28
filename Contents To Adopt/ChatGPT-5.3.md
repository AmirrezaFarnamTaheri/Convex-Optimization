# 5.3

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:08:13  
**Updated:** 12/28/2025 23:44:29  
**Exported:** 12/29/2025 0:10:49  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505fb4-8ba4-832f-ae91-380cc626a6a9](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505fb4-8ba4-832f-ae91-380cc626a6a9)  

## Response:
Thought for 48s

Let’s rewrite the exercise in plain language, then build the dual from absolute basics, step by step, and end by explaining why the dual you get is a **convex optimization problem** even though the primal might be wildly nonconvex.

* * *

0) The primal problem (what you start with)
-------------------------------------------

You are given a nonzero vector  $c\neq 0$  and a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  (think “extended-valued” so constraints can be encoded by  $+\infty$ , but even if you think  $f$  is ordinary real-valued, the derivation is the same).

The primal (original) problem is:

$$
\begin{aligned} \text{minimize}\quad & c^T x\\ \text{subject to}\quad & f(x)\le 0. \end{aligned} \qquad (P)
$$

Important: the exercise explicitly says **do not assume  $f$  is convex**. So  $(P)$  might be nonconvex.

Still, we can always form a Lagrange dual.

* * *

1) Lagrange multipliers: why we introduce  $\lambda\ge 0$ 
----------------------------------------------------------

The constraint is a single inequality:

$$
f(x)\le 0.
$$

The Lagrangian method penalizes violation of this inequality by adding  $\lambda f(x)$  to the objective, with  $\lambda\ge 0$ . Why  $\lambda\ge 0$ ? Because:

*   If  $f(x)\le 0$  (feasible), then  $\lambda f(x)\le 0$ , so adding it does **not** increase the objective (it can only help).
*   If  $f(x)>0$  (infeasible), then  $\lambda f(x)>0$ , so it penalizes infeasibility.

So define the **Lagrangian**

$$
L(x,\lambda) = c^T x + \lambda f(x), \qquad \lambda\ge 0.
$$

No convexity needed to _define_ this.

* * *

2) The dual function  $g(\lambda)$ : “best lower bound you can certify”
-----------------------------------------------------------------------

For each fixed  $\lambda\ge 0$ , define the **dual function**

$$
g(\lambda) = \inf_{x\in\mathbb{R}^n} L(x,\lambda) = \inf_{x} \big(c^T x + \lambda f(x)\big).
$$

Key property (weak duality): for every  $\lambda\ge 0$ ,

$$
g(\lambda)\le p^\star,
$$

where  $p^\star$  is the primal optimal value (if it exists). Intuition: for feasible  $x$ ,  $L(x,\lambda)\le c^T x$ , so taking inf over all  $x$  can’t exceed the inf over feasible  $x$ .

So  $g(\lambda)$  is a lower bound on the best possible primal value.

The **dual problem** is:

$$
\text{maximize } g(\lambda)\quad \text{subject to }\lambda\ge 0. \qquad (D)
$$

So far this is standard.

Now the exercise asks: express  $(D)$  in terms of the **conjugate**  $f^\star$ .

* * *

3) The convex conjugate  $f^\star$ : definition (works even if  $f$  is nonconvex)
----------------------------------------------------------------------------------

The Fenchel (convex) conjugate of  $f$  is defined by

$$
f^\star(y) = \sup_{x\in\mathbb{R}^n}\big( y^T x - f(x)\big).
$$

Two crucial facts:

1.  This definition makes sense for any function  $f$  (convex or not).
2.   $f^\star$  is **always convex** in  $y$ , even if  $f$  is nonconvex. (Because it’s a supremum of affine functions of  $y$ .)

We will use this definition to rewrite  $g(\lambda)$ .

* * *

4) Rewrite  $g(\lambda)=\inf_x(c^T x+\lambda f(x))$  using  $f^\star$ 
----------------------------------------------------------------------

Start from:

$$
g(\lambda) = \inf_x \big(c^T x + \lambda f(x)\big).
$$

### Case  $\lambda = 0$ 

If  $\lambda=0$ , then

$$
g(0)=\inf_x c^T x.
$$

Since  $c\neq 0$ ,  $\inf_x c^T x = -\infty$  (you can take  $x = -t c$  and send  $t\to\infty$ , making  $c^T x = -t\|c\|^2\to -\infty$ ).

So  $g(0)=-\infty$ . That means the dual optimizer (if any) will never pick  $\lambda=0$ . Practically, the dual domain is  $\lambda>0$ .

### Case  $\lambda>0$ 

Factor out  $\lambda$ :

$$
g(\lambda)=\inf_x\left(\lambda f(x) + c^T x\right) = \lambda \inf_x\left( f(x) + \frac{c^T x}{\lambda}\right) = \lambda \inf_x\left( f(x) + \left(\frac{c}{\lambda}\right)^T x\right).
$$

So we need a general identity for expressions of the form

$$
\inf_x \big(f(x) + a^T x\big).
$$

#### A key identity (directly from the definition of  $f^\star$ )

Take any  $a\in\mathbb{R}^n$ . Consider:

$$
\inf_x \big(f(x)+a^T x\big).
$$

Flip it into a supremum by pulling out a minus sign:

$$
\inf_x (f(x)+a^T x) = -\sup_x \big(-f(x)-a^T x\big) = -\sup_x \big( (-a)^T x - f(x)\big).
$$

But by definition,

$$
f^\star(-a) = \sup_x\big( (-a)^T x - f(x)\big).
$$

Therefore:

$$
\boxed{\inf_x \big(f(x)+a^T x\big) = - f^\star(-a).}
$$

Now plug  $a=\frac{c}{\lambda}$ :

$$
\inf_x\left(f(x)+\left(\frac{c}{\lambda}\right)^T x\right) = - f^\star\left(-\frac{c}{\lambda}\right).
$$

So:

$$
g(\lambda) = \lambda\left(- f^\star\left(-\frac{c}{\lambda}\right)\right) = -\lambda\, f^\star\left(-\frac{c}{\lambda}\right), \qquad \lambda>0.
$$

That’s the requested “in terms of  $f^\star$ ” form.

* * *

5) Final dual problem (clean statement)
---------------------------------------

Since  $g(0)=-\infty$ , we can write the dual as  $\lambda>0$  without loss:

$$
\boxed{ \begin{aligned} \text{maximize}\quad & -\lambda\, f^\star\!\left(-\frac{c}{\lambda}\right)\\ \text{subject to}\quad & \lambda>0. \end{aligned} } \qquad (D)
$$

Sometimes you’ll also see  $\lambda\ge 0$  written, with the understanding that  $\lambda=0$  gives  $-\infty$  and is irrelevant.

This is a **one-variable** optimization problem (just  $\lambda$ ), though the objective hides  $f^\star$ .

* * *

6) Why is this dual problem convex?
-----------------------------------

This is the subtle point of the exercise: the primal might not be convex, but the dual you wrote down is still a convex optimization problem.

There are two complementary ways to see it.

### Way A (most fundamental): “dual objective is concave because it’s an infimum of affine functions”

For each fixed  $x$ , the Lagrangian as a function of  $\lambda$  is:

$$
L(x,\lambda)=c^T x+\lambda f(x).
$$

For fixed  $x$ , this is an **affine** function of  $\lambda$  (a line): slope  $f(x)$ , intercept  $c^T x$ .

Then the dual function is

$$
g(\lambda)=\inf_x L(x,\lambda).
$$

A basic convex analysis fact:

*   The **pointwise infimum of affine functions is concave**.

So  $g(\lambda)$  is concave on  $\lambda\ge 0$ , regardless of whether  $f$  is convex, because convexity of  $f$  never entered:  $f(x)$  is just a number when  $x$  is fixed.

Therefore the dual problem

$$
\max_{\lambda\ge 0} g(\lambda)
$$

is maximizing a concave function over a convex set ( $\lambda\ge 0$  is an interval), which is exactly the definition of a **convex optimization problem** (equivalently, minimize  $-g(\lambda)$ , which is convex).

### Way B (explicitly using  $f^\star$ ): “negative of a perspective of a convex function”

We also have the explicit expression

$$
g(\lambda) = -\lambda f^\star\!\left(-\frac{c}{\lambda}\right),\qquad \lambda>0.
$$

Now use two facts:

1.   $f^\star$  is convex (always).
2.  The function
    
$$
(\lambda, y)\mapsto \lambda f^\star\left(\frac{y}{\lambda}\right),\quad \lambda>0,
$$

is the **perspective transform** of  $f^\star$ , and it is convex in  $(\lambda,y)$  whenever  $f^\star$  is convex.

Here  $y$  is fixed to  $y=-c$ . A convex function of  $(\lambda,y)$  restricted to a slice  $y=\text{constant}$  remains convex in  $\lambda$ . So

$$
\lambda \mapsto \lambda f^\star\left(-\frac{c}{\lambda}\right)
$$

is convex on  $\lambda>0$ . Multiply by  $-1$ , and

$$
\lambda \mapsto -\lambda f^\star\left(-\frac{c}{\lambda}\right)
$$

is concave. Maximize concave over  $\lambda>0$  → convex optimization problem.

* * *

7) What this means conceptually (important intuition)
-----------------------------------------------------

*   The primal may be nonconvex because  $f$  may be nonconvex.
*   The dual is still a convex problem because dualization “convexifies” via:
    *   taking an infimum over  $x$ ,
    *   and/or using the conjugate  $f^\star$ , which is always convex.

But: **strong duality is not guaranteed** here. Without convexity + constraint qualification, the dual optimum may be strictly less than the primal optimum (a duality gap).

* * *

8) Final answer (compact)
-------------------------

Primal:

$$
\min_x\ c^T x\ \text{s.t.}\ f(x)\le 0,\quad c\ne 0.
$$

Dual function:

$$
g(\lambda)=\inf_x\big(c^T x+\lambda f(x)\big) = \begin{cases} -\lambda\, f^\star\!\left(-\frac{c}{\lambda}\right), & \lambda>0,\\ -\infty, & \lambda=0. \end{cases}
$$

Dual problem:

$$
\boxed{ \max_{\lambda>0}\ -\lambda\, f^\star\!\left(-\frac{c}{\lambda}\right). }
$$

Why convex:  $g$  is concave because it is a pointwise infimum of affine functions of  $\lambda$  (or equivalently because it is the negative of the perspective of the convex function  $f^\star$ ).

* * *

If you want to go one layer deeper next, the natural continuation is: interpret this dual as optimizing over supporting hyperplanes to the epigraph of  $f$ , and relate it to the biconjugate  $f^{\star\star}$  (the “convex envelope” effect).

## Response:
Here’s a roadmap for mastering exactly the “single inequality constraint → dual via conjugate” pattern you just saw, in small, reliable steps. I’ll make it modular so we can walk it one step at a time and you’ll know what each step is buying you.

Roadmap (you’ll go in order; each step has a concrete checkpoint)

Step 1 — The objects (so nothing feels like magic)  
Goal: Know what counts as a “problem,” what the “optimal value” is, and what “feasible” means when functions can be nonconvex / extended-valued.  
Checkpoint: You can restate a constrained problem as minimizing an objective over a feasible set.

Step 2 — Lagrangian from first principles  
Goal: Understand why we write  $L(x,\lambda)=\text{objective}+\lambda\cdot(\text{constraint})$  and why  $\lambda\ge 0$  for “ $\le$ ” constraints.  
Checkpoint: You can prove weak duality in 3 lines without convexity assumptions.

Step 3 — Dual function as “best certified lower bound”  
Goal: Build  $g(\lambda)=\inf_x L(x,\lambda)$  and interpret it geometrically: for each  $\lambda$ , you’re producing a lower bound on the primal optimum.  
Checkpoint: You can explain why  $g$  is concave (infimum of affine functions in  $\lambda$ ) even if  $f$  is nonconvex.

Step 4 — Conjugate  $f^\star$  and the key identity  
Goal: Learn the definition  $f^\star(y)=\sup_x(y^Tx-f(x))$  and derive the identity

$$
\inf_x \big(f(x)+a^Tx\big)=-f^\star(-a)
$$

purely from that definition.  
Checkpoint: You can derive it cleanly, and you know exactly where the minus signs come from.

Step 5 — Express the dual in terms of  $f^\star$   
Goal: Apply Step 4 with  $a=c/\lambda$  to get

$$
g(\lambda)=-\lambda\, f^\star\!\left(-\frac{c}{\lambda}\right)
$$

and write the dual as a 1D maximize problem over  $\lambda>0$ .  
Checkpoint: You can handle the edge case  $\lambda=0$  (why it becomes  $-\infty$  when  $c\neq 0$ ).

Step 6 — “Why the dual is convex” in two independent ways  
Goal: Be able to justify convexity of the dual both ways:  
(A)  $g$  is concave as inf of affine functions in  $\lambda$ .  
(B)  $f^\star$  is convex and the “perspective transform”  $\lambda f^\star(y/\lambda)$  is convex, so  $-\lambda f^\star(-c/\lambda)$  is concave.  
Checkpoint: You can explain both without handwaving.

Step 7 — When duality is tight (and when it fails)  
Goal: Learn what extra conditions (convexity of  $f$ , Slater-type conditions) buy you: strong duality and KKT conditions.  
Checkpoint: You can name the missing assumptions in the exercise and predict “duality gap may occur.”

Step 8 — Practice patterns (so it becomes automatic)  
Goal: Do 5–10 variants:  
• replace  $f(x)\le 0$  with  $f(x)\le d$   
• replace objective  $c^Tx$  with general convex  $h(x)$   
• encode sets using indicator functions  
• derive duals with conjugates/perspectives repeatedly  
Checkpoint: You can dualize new problems without guessing.

Now we go “small steps one by one.” We start at Step 1.

Step 1 — The objects (mini-lesson)  
A general constrained optimization problem is:

$$
\text{minimize } \phi(x)\quad \text{subject to } x\in\mathcal{F}
$$

where

*    $\phi(x)$  is the objective (a function),
*    $\mathcal{F}$  is the feasible set (the allowed  $x$ ’s).

In your problem:

*   Objective:  $\phi(x)=c^T x$ .
*   Constraint:  $f(x)\le 0$ .  
    So the feasible set is
    
$$
\mathcal{F}=\{x\in\mathbb{R}^n:\ f(x)\le 0\}.
$$

The primal optimal value is

$$
p^\star = \inf\{c^T x:\ f(x)\le 0\}.
$$

(I’m using  $\inf$ , not  $\min$ , because a minimum might not be attained.)

Checkpoint for Step 1 (tiny but important):  
You should be completely comfortable rewriting the primal as

$$
p^\star=\inf_{x\in\mathbb{R}^n}\ \big\{c^Tx \;|\; f(x)\le 0\big\}.
$$

Next step (what we’ll do immediately after this): build the Lagrangian and prove weak duality with no convexity.

If you’re following along, here’s the “do it right now” micro-exercise:  
Take any feasible  $x$  (so  $f(x)\le 0$ ) and any  $\lambda\ge 0$ . Show directly that

$$
c^Tx+\lambda f(x)\le c^Tx.
$$

That single inequality is the seed from which the entire dual grows.

## Response:
Good. Let’s slow everything down and build the machinery from bedrock. No tricks, no “just trust me,” only definitions and logic.

We will do **Step 1** and **Step 2** in full mathematical depth.

* * *

STEP 1 — What exactly is a “constrained optimization problem”?
==============================================================

You are given:

• a variable  $x\in\mathbb{R}^n$   
• an objective function  $\phi(x)$   
• a constraint of the form  $f(x)\le 0$ 

In our problem,

$$
\phi(x)=c^Tx,\qquad f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\},\quad c\neq 0.
$$

* * *

1.1 What does “minimize” actually mean?
---------------------------------------

To “minimize”  $\phi(x)$  subject to a constraint means:

We are allowed to choose  $x$  only from those values that satisfy the constraint, and among those allowed values we want the smallest possible objective value.

So first define the **feasible set**

$$
\mathcal F = \{x\in\mathbb{R}^n : f(x)\le 0\}.
$$

This is the set of points you are allowed to pick.

Then the primal problem is nothing more than

$$
p^\star = \inf_{x\in\mathcal F} \phi(x) = \inf\{c^Tx : f(x)\le 0\}.
$$

This is the meaning of the primal optimal value.

We write  $\inf$  instead of  $\min$  because:  
• there might be no minimizer  
• the values might approach a number but never reach it

The number  $p^\star$  is the best cost you can possibly achieve.

* * *

1.2 What makes this problem dangerous?
--------------------------------------

We are **not** assuming  $f$  is convex.

That means:  
•  $\mathcal F$  can be disconnected  
• it can have holes  
• it can be fractal or wild  
• finding  $p^\star$  might be NP-hard

So the primal problem may be extremely hard.

Yet duality will still give us a **guaranteed lower bound** on  $p^\star$ . That is what the dual is.

* * *

STEP 2 — The Lagrangian from first principles
=============================================

The goal is to find **lower bounds** on the primal optimum  $p^\star$ .

If you can find any number  $L$  such that

$$
L \le c^Tx \quad \text{for every feasible } x,
$$

then automatically

$$
L \le p^\star.
$$

So the dual is about building certified lower bounds.

* * *

2.1 How to enforce a constraint using penalties
-----------------------------------------------

We have the constraint:

$$
f(x)\le 0.
$$

For any feasible  $x$ , this inequality is true.

Now pick any number  $\lambda\ge 0$ . Then

$$
\lambda f(x)\le 0.
$$

So for every feasible  $x$ ,

$$
c^Tx + \lambda f(x) \le c^Tx.
$$

This is the key inequality.

It says:  
**if  $x$  satisfies the constraint, adding  $\lambda f(x)$  can only decrease the objective.**

So for any feasible  $x$ ,

$$
c^Tx \ge c^Tx + \lambda f(x).
$$

Now take the smallest possible value of the right-hand side over all  $x$  (even infeasible ones):

$$
c^Tx \ge \inf_{z\in\mathbb{R}^n}\big(c^Tz+\lambda f(z)\big).
$$

This holds for every feasible  $x$ , so it holds for the best feasible one:

$$
p^\star = \inf_{x:\,f(x)\le 0} c^Tx \ge \inf_{z\in\mathbb{R}^n}\big(c^Tz+\lambda f(z)\big).
$$

Define

$$
g(\lambda) = \inf_{x\in\mathbb{R}^n} \big(c^Tx+\lambda f(x)\big).
$$

Then we have proven

$$
\boxed{g(\lambda)\le p^\star \quad \text{for every }\lambda\ge 0.}
$$

This is called **weak duality**.

No convexity was used.  
Only the inequality  $f(x)\le 0$  and the fact  $\lambda\ge 0$ .

* * *

2.2 Why  $\lambda\ge 0$  is essential
-------------------------------------

If  $\lambda<0$ , then for feasible  $x$ ,

$$
\lambda f(x) \ge 0,
$$

so

$$
c^Tx+\lambda f(x) \ge c^Tx.
$$

That would give an **upper bound**, not a lower bound. That destroys duality.

So dual multipliers must satisfy:

$$
\lambda \ge 0.
$$

This is not convention. It is forced by logic.

* * *

2.3 What the dual problem is trying to do
-----------------------------------------

For each  $\lambda\ge 0$ , you get one certified lower bound  $g(\lambda)$ .

Some choices of  $\lambda$  give weak bounds.  
Some give strong ones.

So you choose the best one:

$$
d^\star = \sup_{\lambda\ge 0} g(\lambda).
$$

This is the **dual optimal value**.

And always

$$
d^\star \le p^\star.
$$

Even when the primal is ugly, disconnected, or nonconvex.

* * *

2.4 Geometric intuition
-----------------------

For fixed  $x$ , the Lagrangian

$$
L(x,\lambda)=c^Tx+\lambda f(x)
$$

is a straight line in  $\lambda$  with slope  $f(x)$ .

The dual function

$$
g(\lambda)=\inf_x L(x,\lambda)
$$

is the **lower envelope** of all these lines.

Lower envelopes of lines are always concave.  
That is why the dual problem is convex.

* * *

We now have:

• a primal value  $p^\star$   
• a dual function  $g(\lambda)$   
• a dual problem  $\max_{\lambda\ge 0} g(\lambda)$   
• weak duality  $g(\lambda)\le p^\star$ 

Next step is Step 3 and Step 4, where this infimum over  $x$  gets rewritten using the conjugate  $f^\star$ , which makes everything computable and geometric.

## Response:
Great — let's fully unpack **Exercise 5.3 from Boyd & Vandenberghe**, step-by-step, in a complete newcomer walkthrough style. This is a deceptively simple-looking problem that builds duality theory using **Fenchel conjugates** and **Lagrangian duality** in a general setting — even when the constraint function  $f(x)$  is **not convex**.

* * *

🌍 Problem Statement (Restated)
-------------------------------

We are given the **primal optimization problem**:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n} \quad & c^T x \\ \text{subject to} \quad & f(x) \le 0, \end{aligned}
$$

with:

*    $c \in \mathbb{R}^n$ , and importantly  $c \ne 0$ ,
*    $f: \mathbb{R}^n \to \mathbb{R}$ , **not necessarily convex**.

* * *

🎯 Objective
------------

1.  Derive the **dual problem**, using the **convex conjugate**  $f^*$ .
2.  Show that your **dual problem is convex**, _even though  $f$  is not convex_.

* * *

✅ Step 1: Understand the Primal Problem Structure
=================================================

Let’s carefully analyze what’s given.

* * *

### 🔹 Objective Function:

$$
f_0(x) = c^T x
$$

This is a **linear function**, which is always convex (and concave) because its Hessian is zero.

So our goal is to **minimize** a **linear** function, which is convex.

* * *

### 🔹 Constraint Function:

$$
f(x) \le 0
$$

This is a **scalar inequality constraint** involving some function  $f$ . Crucially:

*   We are _not told_  $f$  is convex.
*   But we still want to **construct a valid dual problem**.

* * *

### 🔹 Feasible Set:

$$
\mathcal{F} = \{x \in \mathbb{R}^n \mid f(x) \le 0\}
$$

This is the set of all points where the constraint is satisfied.

But again: since  $f$  is not convex, this set may **not be convex**.

* * *

### 🔹 Summary:

*   **Minimize**: Linear cost  $c^T x$ 
*   **Subject to**: Single nonlinear scalar constraint  $f(x) \le 0$ 
*    $f$  may not be convex
*   Use the **conjugate  $f^*$ ** in dual
*   Derive a **convex dual problem**

* * *

✅ Step 2: Setup the Lagrangian Function
=======================================

The **Lagrangian** is the key object in forming a **dual problem**.

* * *

### 🎓 General Form of the Lagrangian

For a problem:

$$
\begin{aligned} \min_x \quad & f_0(x) \\ \text{subject to} \quad & f(x) \le 0 \end{aligned}
$$

We define the **Lagrangian**:

$$
L(x, \lambda) = f_0(x) + \lambda f(x)
$$

Where:

*    $\lambda \in \mathbb{R}_+$  is the **Lagrange multiplier** associated with the inequality constraint.
*    $\lambda \ge 0$  (because inequality constraints use nonnegative multipliers).

* * *

### ✅ Apply This to Our Problem

Here:

*    $f_0(x) = c^T x$ 
*   Constraint:  $f(x) \le 0$ 

So the **Lagrangian** is:

$$
L(x, \lambda) = c^T x + \lambda f(x), \quad \text{with } \lambda \ge 0
$$

* * *

### Intuition:

You can think of this as "penalizing" violations of the constraint. If  $f(x) > 0$ , it increases the cost through  $\lambda f(x)$ , pushing the optimizer back into the feasible set.

* * *

✅ Step 3: Define the Dual Function
==================================

We now define the **dual function** as the **infimum over  $x$ ** of the Lagrangian:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \, L(x, \lambda) = \inf_x \left( c^T x + \lambda f(x) \right)
$$

This function gives us a **lower bound** on the optimal value of the primal problem for each fixed  $\lambda \ge 0$ .

* * *

### ❗ Key: This is where the **conjugate** comes in.

We want to write this infimum in terms of the **conjugate function  $f^*$ **.

To do that, we’ll **re-express** this infimum by **changing variables**.

Let’s factor out  $\lambda$  and define:

$$
g(\lambda) = \inf_x \left[ \lambda \left( \frac{1}{\lambda} c^T x + f(x) \right) \right] \quad \text{(if } \lambda > 0 \text{)}
$$

Now define:

$$
v := -\frac{1}{\lambda} c \in \mathbb{R}^n \quad \Rightarrow \quad c^T x = -\lambda v^T x
$$

So:

$$
g(\lambda) = \lambda \cdot \inf_x \left( f(x) - v^T x \right) = -\lambda \cdot \sup_x \left( v^T x - f(x) \right) = -\lambda \cdot f^*(v)
$$

Therefore:

$$
g(\lambda) = -\lambda \cdot f^*\left(-\frac{1}{\lambda} c\right) \quad \text{for } \lambda > 0
$$

For  $\lambda = 0$ , the Lagrangian becomes just  $c^T x$ , and its infimum is  $-\infty$  (unless constrained), so we usually restrict to  $\lambda > 0$  in the domain of the dual function.

* * *

✅ Step 4: Write the Dual Problem
================================

The **dual problem** is to **maximize the dual function** over  $\lambda \ge 0$ :

$$
\begin{aligned} \max_{\lambda \ge 0} \quad & g(\lambda) = -\lambda \cdot f^*\left(-\frac{1}{\lambda} c\right) \end{aligned}
$$

This is your **dual optimization problem**, expressed purely in terms of:

*    $f^*$ , the conjugate of the (possibly nonconvex!) function  $f$ ,
*   The multiplier  $\lambda \ge 0$ ,
*   The given cost vector  $c \ne 0$ .

* * *

### 🔍 Important Notes

*   Even if  $f$  is **not convex**, its **convex conjugate  $f^*$ ** is always convex — by definition of the supremum over linear functions.
*   Therefore, the function  $g(\lambda) = -\lambda f^*(-\tfrac{1}{\lambda} c)$  is **concave** in  $\lambda$ , making the **dual problem a convex maximization problem**.
*   So the dual problem is always convex, even if the primal is not.

* * *

### ✅ Final Dual Problem (boxed):

$$
\boxed{ \max_{\lambda \ge 0} \quad -\lambda \cdot f^*\left(-\frac{1}{\lambda} c\right) }
$$

This is the full dual problem, as requested.

* * *

🧠 Summary So Far
-----------------

| Step | Action | Result |
| --- | --- | --- |
| 1 | Define primal |  $\min c^T x \text{ s.t. } f(x) \le 0$  |
| 2 | Setup Lagrangian |  $L(x,\lambda) = c^T x + \lambda f(x)$  |
| 3 | Dual function |  $g(\lambda) = \inf_x \left( c^T x + \lambda f(x) \right)$  |
| 4 | Express in terms of conjugate |  $g(\lambda) = -\lambda f^*(-\frac{1}{\lambda} c)$  |
| 5 | Maximize |  $\max_{\lambda \ge 0} -\lambda f^*(-\frac{1}{\lambda} c)$  |

* * *

Let me know when you're ready for **Step 5: Interpretations, Graphs, Examples, and Edge Cases** — or if you want to apply this to a concrete  $f(x)$ .

## Response:
Time to zoom in on the one object that quietly did all the heavy lifting: the **conjugate**  $f^\star$ . This thing is not a trick; it is a geometric microscope.

I will build it from zero.

* * *

1) Why a conjugate even exists
------------------------------

Take any function

$$
f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}.
$$

It might be convex, nonconvex, discontinuous, ugly, whatever. Think of its graph in  $(x,z)$ \-space: the surface  $z=f(x)$ .

Now ask a geometric question:

> Among all affine (linear+constant) functions of the form
> 
> $$
> x\mapsto y^T x - \alpha,
> $$
> 
> which ones lie **below** the graph of  $f$ ?

Rewriting:

$$
y^T x - \alpha \le f(x)\quad \text{for all }x.
$$

That inequality is equivalent to

$$
\alpha \ge y^T x - f(x)\quad \text{for all }x.
$$

So the smallest such  $\alpha$  is

$$
\alpha = \sup_x \big(y^T x - f(x)\big).
$$

This number tells you:  
**how high a plane with slope  $y$  must be lifted so it touches (or lies below)  $f$ .**

That is the conjugate.

* * *

2) Formal definition
--------------------

The **convex conjugate** (also called Fenchel conjugate) of  $f$  is

$$
\boxed{ f^\star(y)=\sup_{x\in\mathbb{R}^n}\big(y^T x - f(x)\big). }
$$

That’s it. No convexity assumption. Just a supremum.

* * *

3) What does it mean intuitively?
---------------------------------

Fix a vector  $y$ .

Look at all linear functions  $x\mapsto y^T x$ .  
Compare them to  $f(x)$ .

The quantity

$$
y^T x - f(x)
$$

measures how much the linear function overshoots the function  $f$  at  $x$ .

So

$$
f^\star(y)
$$

is the **largest gap** between the linear function with slope  $y$  and the function  $f$ .

Geometrically:

*    $f^\star(y)$  is the vertical shift needed so that the plane
    $$
    z = y^T x - f^\star(y)
    $$
    lies below the graph of  $f$ .

So  $f^\star$  is a “support-function of the epigraph of  $f$ .”

* * *

4) Why is  $f^\star$  always convex?
------------------------------------

Because it is a supremum of linear functions of  $y$ .

Fix  $x$ .  
The map

$$
y\mapsto y^T x - f(x)
$$

is linear in  $y$ .

Then

$$
f^\star(y)=\sup_x\big(y^Tx-f(x)\big)
$$

is the pointwise supremum of linear functions of  $y$ .

And a fundamental theorem says:

> A supremum of affine (or linear) functions is convex.

So **even if  $f$  is nonconvex,  $f^\star$  is always convex.**

This is the deep reason the dual problem becomes convex.

* * *

5) Why the conjugate appears in duality
---------------------------------------

Recall in the dual we had to compute things like

$$
\inf_x\big(f(x)+a^T x\big).
$$

Using algebra:

$$
\inf_x\big(f(x)+a^Tx\big) = -\sup_x\big(-a^Tx-f(x)\big) = -f^\star(-a).
$$

So the conjugate is exactly the object that turns “min over  $x$  of a tilted function” into something explicit.

That is why it appears automatically when you eliminate  $x$  from the Lagrangian.

* * *

6) Simple example (so it becomes real)
--------------------------------------

Let

$$
f(x)=\tfrac12\|x\|^2.
$$

Compute the conjugate:

$$
f^\star(y)=\sup_x \big(y^Tx-\tfrac12\|x\|^2\big).
$$

Maximize over  $x$ : derivative  $y-x=0\Rightarrow x=y$ .  
Plug back:

$$
f^\star(y)=y^Ty-\tfrac12\|y\|^2=\tfrac12\|y\|^2.
$$

So the conjugate of a quadratic is another quadratic.

But if  $f$  is not convex? Still the same definition works.

* * *

7) Why this mattered for your dual
----------------------------------

Your dual became

$$
g(\lambda)=-\lambda f^\star\!\left(-\frac{c}{\lambda}\right).
$$

So what you are really doing is:  
• take all linear supports of  $f$ ,  
• tilt them by  $c$ ,  
• scale by  $\lambda$ ,  
• and choose the tightest lower bound on the primal objective.

The conjugate is the machine that encodes all linear lower bounds of  $f$ .

* * *

If you want, the next natural thing to see is the **biconjugate**

$$
f^{\star\star}
$$

which turns out to be the **convex envelope** of  $f$ , and that is exactly how duality “convexifies” a nonconvex primal without ever touching  $f$  directly.

## Response:
Great question. Let’s unpack **what a convex conjugate is**, why it matters, and how it connects to duality — **from first principles**, in the most beginner-friendly, rigorous, zero-to-hero way.

* * *

🧠 What Is a “Conjugate Function”  $f^*$ ? — Newcomer Walkthrough
=================================================================

We’ll start with intuition, then give the formal definition, and then unpack geometric meaning, examples, and properties.

* * *

🔹 0. Intuition: What Are We Trying to Do?
------------------------------------------

A **conjugate** is a way of converting a function  $f(x)$  (in **primal space**) into a new function  $f^*(y)$  (in **dual space**) by looking at how **linear functions** touch or "support"  $f$ .

It’s a way to **encode all the linear underestimators of  $f$ ** into a new function.

> Think of  $f^*(y)$  as measuring:
> 
> 👉 "How much can I support (touch from below) the function  $f$  using the line  $y^T x$ ?"

This idea is at the heart of **convex duality**, **supporting hyperplanes**, and **optimization**.

* * *

🔹 1. Formal Definition
-----------------------

Given a function  $f: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ , its **(Fenchel) convex conjugate**  $f^*: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$  is defined as:

$$
\boxed{ f^*(y) := \sup_{x \in \text{dom } f} \left( y^T x - f(x) \right) }
$$

### ⛏️ Let’s parse that:

*   Input: A vector  $y \in \mathbb{R}^n$ 
*   Output: A number (possibly  $+\infty$ )
*   You compute it by **scanning all  $x$ ** and taking the **maximum value** of the quantity:
    $$
    y^T x - f(x)
    $$
*   It’s a **supremum**, not minimum. So the conjugate tells you how big this expression can get.

* * *

🔹 2. What Is  $y^T x - f(x)$ ? Why Take the Sup?
-------------------------------------------------

Let’s isolate this quantity:

$$
y^T x - f(x) = \text{linear function in } x \quad - \quad \text{original function at } x
$$

This measures **how far above** the linear function  $y^T x$  is from the function  $f(x)$ , at any point  $x$ .

In other words:

> “How much profit do I make by **replacing**  $f(x)$  with the linear function  $y^T x$ ?”

So the supremum  $\sup_x (y^T x - f(x))$  asks:

> What’s the **worst-case gap** between the linear function  $y^T x$  and the function  $f(x)$ ? This tells us **how well** the linear function  $y^T x$  supports  $f(x)$  from below.

If  $f$  is convex, this gap makes geometric sense — it’s tied to **supporting hyperplanes**.

* * *

🔹 3. Geometric Picture: Supporting a Convex Function
-----------------------------------------------------

Let’s say  $f$  is convex. Then at any point, you can **touch its graph from below** with a straight line (this is the **subgradient** idea).

The conjugate:

*   For each slope  $y$ , tells you how **high you need to shift the line  $y^T x$ ** upward to make it touch the function from below.
*   That upward shift (vertical gap) is exactly  $f^*(y)$ .

This idea leads to:

$$
f(x) = \sup_{y} \left( y^T x - f^*(y) \right) \quad\text{(under certain conditions)}
$$

This is called the **Fenchel–Moreau Theorem**, and it tells you:

> You can fully recover a convex function from its conjugate.

* * *

🔹 4. Examples (Scalar Case:  $f:\mathbb{R} \to \mathbb{R}$ )
-------------------------------------------------------------

Let’s look at concrete examples of conjugates.

* * *

### Example 1:  $f(x) = \delta_C(x)$  — indicator function of a set

Define:

$$
\delta_C(x) = \begin{cases} 0 & x \in C \\ +\infty & x \notin C \end{cases}
$$

Then:

$$
f^*(y) = \sup_{x \in C} (y^T x - 0) = \sup_{x \in C} y^T x \Rightarrow f^*(y) = \sigma_C(y)
$$

So the conjugate of an indicator function is the **support function** of the set  $C$ .

* * *

### Example 2:  $f(x) = \frac{1}{2} \|x\|_2^2$ 

Let’s compute its conjugate.

We compute:

$$
f^*(y) = \sup_x \left( y^T x - \frac{1}{2} \|x\|^2 \right)
$$

This is a **quadratic maximization** problem in  $x$ , unconstrained.

We solve by setting gradient to zero:

$$
\nabla_x (y^T x - \frac{1}{2} \|x\|^2) = y - x = 0 \Rightarrow x = y
$$

Plug back:

$$
f^*(y) = y^T y - \frac{1}{2} \|y\|^2 = \frac{1}{2} \|y\|^2
$$

So:

$$
\boxed{ f(x) = \frac{1}{2} \|x\|^2 \quad \Rightarrow \quad f^*(y) = \frac{1}{2} \|y\|^2 }
$$

In this case, the conjugate is self-dual:  $f = f^*$ 

* * *

### Example 3:  $f(x) = \log\left( \sum_{i=1}^n e^{x_i} \right)$  — the log-sum-exp

This is a **smooth approximation to max**.

Its conjugate is the **negative entropy function**:

$$
f^*(y) = \begin{cases} \sum_i y_i \log y_i & y \in \Delta \\ +\infty & \text{otherwise} \end{cases}
$$

Where  $\Delta = \{y \in \mathbb{R}^n_+ : \sum y_i = 1\}$  is the probability simplex.

* * *

🔹 5. Key Properties of the Conjugate
-------------------------------------

Here’s a table of major facts.

| Property | Description |
| --- | --- |
|  $f^*$  is always convex | Even if  $f$  is not convex |
| Biconjugate:  $f^{**}$  |  $f^{**} = \text{conv}(f)$ , the convex closure |
| Support function duality |  $\delta_C^* = \sigma_C$ ,  $\sigma_C^* = \delta_C$  |
| Duality | Primal–dual problems often arise from conjugates |
| Dual norms | The conjugate of  $f(x) = \|x\|$  is the indicator of the dual norm ball |

* * *

🧠 Summary (Cheat Sheet)
------------------------

| Concept | Formula |
| --- | --- |
| Convex conjugate |  $f^*(y) = \sup_x \left( y^T x - f(x) \right)$  |
| Interpretation | Best linear underestimator (support) of  $f$  |
| Always convex? | ✅ Yes, even if  $f$  is not |
| Used for? | Duality, Fenchel duals, subgradients, supporting planes |
| Dual function | Often involves  $f^*(-A^T \lambda)$ , etc. |
| Recovery |  $f(x) = \sup_y (y^T x - f^*(y))$  under mild assumptions |

* * *

Let me know if you want:

*   Full derivation of biconjugates  $f^{**}$ 
*   More geometric illustrations
*   Programming examples (e.g. using `cvxpy`, `scipy.optimize`)
*   Applications in economics, entropy, machine learning

Or we can move to the **next step in the duality walkthrough**.

## Response:
Perfect. Let’s now **solve the original problem** in a fully structured, rigorous walkthrough — starting from the formulation and working all the way to the derived **dual problem**.

We already unpacked Steps 1–4, which you understood.

Now we’ll:

*   Recap the full structure so far (clean boxed setup)
*   Go step-by-step through solving for the **dual function**
*   Derive the **final dual optimization problem**
*   Confirm that it's convex (even if primal isn’t!)
*   Preview **what comes next**: special cases, duality gap, examples

* * *

📦 RECAP: Problem Setup
=======================

### 🟧 Primal Problem (given):

Minimize a linear function subject to a scalar nonlinear constraint:

$$
\tag{P} \begin{aligned} \min_{x \in \mathbb{R}^n} \quad & c^T x \\ \text{subject to} \quad & f(x) \le 0, \end{aligned}
$$
*    $f: \mathbb{R}^n \to \mathbb{R}$ , not necessarily convex
*    $c \in \mathbb{R}^n$ , with  $c \ne 0$ 

Our goal is to **derive the Lagrange dual** of this problem.

* * *

✅ Step-by-Step Dual Derivation
==============================

* * *

🔹 Step 1: Lagrangian
---------------------

We define the **Lagrangian function**:

$$
L(x, \lambda) = c^T x + \lambda f(x), \quad \lambda \ge 0
$$
*    $\lambda$  is the Lagrange multiplier for inequality constraint
*    $L(x, \lambda)$  combines the objective and constraint

* * *

🔹 Step 2: Dual Function
------------------------

We define the **dual function**:

$$
g(\lambda) := \inf_{x \in \mathbb{R}^n} L(x, \lambda) = \inf_{x} \left( c^T x + \lambda f(x) \right)
$$

We want to express this in terms of the **conjugate function**  $f^*$ .

* * *

🔹 Step 3: Manipulate Into Conjugate Form
-----------------------------------------

Observe:

$$
g(\lambda) = \inf_x \left( c^T x + \lambda f(x) \right) = \lambda \cdot \inf_x \left( \frac{1}{\lambda} c^T x + f(x) \right) \quad \text{(for } \lambda > 0 \text{)}
$$

Let’s define:

$$
v := -\frac{1}{\lambda} c \quad \text{so that} \quad c^T x = -\lambda v^T x
$$

Then:

$$
g(\lambda) = \lambda \cdot \inf_x \left( -v^T x + f(x) \right) = -\lambda \cdot \sup_x \left( v^T x - f(x) \right) = -\lambda f^*(v) = -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

So:

$$
\boxed{ g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right), \quad \text{for } \lambda > 0 }
$$

⚠️ For  $\lambda = 0$ , the expression becomes  $g(0) = \inf_x c^T x$ , which is  $-\infty$  since no constraints — so the supremum becomes infinite. So we restrict to  $\lambda > 0$ .

* * *

🔹 Step 4: Final Dual Problem
-----------------------------

The **dual problem** is to maximize the dual function over  $\lambda \ge 0$ :

$$
\boxed{ \begin{aligned} \text{(D)} \qquad \max_{\lambda > 0} \quad & -\lambda f^*\left( -\frac{1}{\lambda} c \right) \end{aligned} }
$$

* * *

🔹 Step 5: Properties of Dual Problem
-------------------------------------

### ✅ The dual problem is convex!

Why?

Because:

*   The function  $f^*$  is always convex, even if  $f$  is not
*    $\lambda \mapsto -\lambda f^*(-\tfrac{1}{\lambda} c)$  is a **concave** function of  $\lambda$ 

So, **we are maximizing a concave function** over a convex domain  $\lambda > 0$ .

That makes the dual problem a convex maximization problem.

* * *

🔍 Deep Intuition
-----------------

*    $f^*(-\tfrac{1}{\lambda} c)$  measures how "expensive" it is to support  $f$  with a plane of slope  $-\tfrac{1}{\lambda} c$ 
*   Scaling by  $\lambda$  gives the cost in original units
*   We’re trying to get the tightest lower bound on the primal value, using only dual information

* * *

💡 Summary (boxed)
------------------

| Concept | Formula |
| --- | --- |
| Lagrangian |  $L(x, \lambda) = c^T x + \lambda f(x)$  |
| Dual function |  $g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right)$  |
| Dual problem |  $\max_{\lambda > 0} \, -\lambda f^*\left( -\frac{1}{\lambda} c \right)$  |
| Dual is convex? | ✅ Yes — always convex in  $\lambda$  |

* * *

### ✅ Ready to proceed?

Let me know and I’ll walk you through:

1.  **Dual optimal value vs primal** — when is there **zero duality gap**?
2.  **Examples** — plug in real  $f(x)$  (e.g. quadratic, norm, exponential) and compute dual
3.  **Visualization** — graphs of  $f$ ,  $f^*$ , and their geometric interpretation
4.  **Sufficient conditions for strong duality**
5.  Or continue with next exercise (e.g., 5.4)

Just say “continue” or pick one of the branches.

## Response:
Good. We now zoom into the **engine room**: how the variable  $x$  disappears, how the conjugate enters, and why the final one–variable dual problem is convex. No recap, no fluff, just the math with all gears visible.

We start from where Steps 1–2 left us:

$$
g(\lambda)=\inf_{x\in\mathbb{R}^n}\big(c^Tx+\lambda f(x)\big), \qquad \lambda\ge0.
$$

Everything now is about computing this infimum.

* * *

Step 3 — Eliminating  $x$  using the conjugate
----------------------------------------------

Assume  $\lambda>0$ . (We will deal with  $\lambda=0$  separately.)

Start from

$$
g(\lambda)=\inf_x \big(c^Tx+\lambda f(x)\big).
$$

Factor out  $\lambda$ :

$$
g(\lambda)=\lambda \inf_x \left(f(x)+\frac{1}{\lambda}c^Tx\right).
$$

So the problem reduces to computing an expression of the form

$$
\inf_x\big(f(x)+a^Tx\big) \quad\text{with}\quad a=\frac{c}{\lambda}.
$$

This is where the conjugate enters.

By pure algebra,

$$
\inf_x\big(f(x)+a^Tx\big) = -\sup_x\big(-f(x)-a^Tx\big) = -\sup_x\big((-a)^Tx - f(x)\big).
$$

But the definition of the conjugate is

$$
f^*(y)=\sup_x (y^Tx-f(x)).
$$

So with  $y=-a$ ,

$$
\sup_x\big((-a)^Tx - f(x)\big)=f^*(-a).
$$

Therefore

$$
\inf_x\big(f(x)+a^Tx\big)=-f^*(-a).
$$

Now substitute back  $a=\frac{c}{\lambda}$ :

$$
\inf_x\left(f(x)+\frac{c^Tx}{\lambda}\right) =-f^*\!\left(-\frac{c}{\lambda}\right).
$$

So

$$
g(\lambda) =\lambda\left(-f^*\!\left(-\frac{c}{\lambda}\right)\right) =-\lambda\,f^*\!\left(-\frac{c}{\lambda}\right), \qquad \lambda>0.
$$

That is the explicit dual function.

This step is not a trick. It is just algebra plus the definition of the conjugate.

* * *

Step 4 — What about  $\lambda=0$ ?
----------------------------------

If  $\lambda=0$ , the dual function is

$$
g(0)=\inf_x c^Tx.
$$

Since  $c\neq0$ , the linear function  $c^Tx$  is unbounded below:  
take  $x=-tc$  and let  $t\to\infty$ , then  $c^Tx=-t\|c\|^2\to-\infty$ .

So

$$
g(0)=-\infty.
$$

That means  $\lambda=0$  is useless for maximizing  $g$ . The dual optimizer, if it exists, must have  $\lambda>0$ .

So the dual problem becomes

$$
\max_{\lambda>0}\; -\lambda\,f^*\!\left(-\frac{c}{\lambda}\right).
$$

This is now a one–variable optimization problem.

* * *

Step 5 — Why this dual problem is convex
----------------------------------------

There are two logically independent ways to see this. Both matter.

### Method A: from the definition of  $g$ 

Recall

$$
g(\lambda)=\inf_x\big(c^Tx+\lambda f(x)\big).
$$

For each fixed  $x$ , the function

$$
\lambda\mapsto c^Tx+\lambda f(x)
$$

is affine (a straight line) in  $\lambda$ .

The dual function  $g(\lambda)$  is the pointwise infimum of all these lines as  $x$  varies.

A fundamental fact from convex analysis:

> The pointwise infimum of affine functions is concave.

Therefore  $g(\lambda)$  is concave on  $\lambda\ge0$ , regardless of whether  $f$  is convex.

Maximizing a concave function over a convex set ( $\lambda\ge0$ ) is a convex optimization problem.

This already proves the dual is convex.

* * *

### Method B: from the conjugate expression

We have

$$
g(\lambda)=-\lambda f^*\!\left(-\frac{c}{\lambda}\right).
$$

We know:

*    $f^*$  is convex (always, even if  $f$  is not).
*   The function
    $$
    (\lambda,y)\mapsto \lambda f^*\!\left(\frac{y}{\lambda}\right), \quad \lambda>0,
    $$
    is the **perspective transform** of  $f^*$ , and it is convex whenever  $f^*$  is convex.

Here  $y=-c$  is fixed, so

$$
\lambda\mapsto \lambda f^*\!\left(-\frac{c}{\lambda}\right)
$$

is convex in  $\lambda$ .

Multiply by  $-1$ , and

$$
\lambda\mapsto -\lambda f^*\!\left(-\frac{c}{\lambda}\right)
$$

is concave.

So again: we are maximizing a concave function of  $\lambda$ . That is a convex dual problem.

* * *

At this point the original nonconvex problem has been transformed into a **one–dimensional convex problem** whose objective is built from the conjugate  $f^*$ . The geometry hiding underneath is “find the best linear support of  $f$  whose slope is aligned with  $c$ .”

That is the full logic of Steps 3–5.

## Response:
Let’s now **unpack Step 3 in full** — **line by line**, with detailed justifications, rigorous transformations, and clear motivations for each algebraic step. We'll fully explain **why** each manipulation is valid and what **intuition** lies behind it.

* * *

🎯 GOAL OF STEP 3:
==================

We want to rewrite the dual function:

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( c^T x + \lambda f(x) \right)
$$

in a form involving the **conjugate**  $f^*$ , i.e.:

$$
g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

Let’s go step-by-step.

* * *

🔁 LINE-BY-LINE UNPACKING OF STEP 3
===================================

* * *

🔹 LINE 1:
----------

$$
g(\lambda) = \inf_{x \in \mathbb{R}^n} \left( c^T x + \lambda f(x) \right)
$$

### 🔍 What’s going on?

*   This is the **definition** of the **dual function**.
*   It comes directly from duality theory: we take the infimum of the **Lagrangian** over all primal variables  $x$ , holding  $\lambda$  fixed.

Nothing tricky here — this is our starting point.

* * *

🔹 LINE 2:
----------

$$
= \lambda \cdot \inf_{x \in \mathbb{R}^n} \left( \frac{1}{\lambda} c^T x + f(x) \right) \quad \text{(for } \lambda > 0 \text{)}
$$

### ❓ Why is this valid?

Because  $\lambda > 0$ , we can **factor it out** safely:

*    $c^T x + \lambda f(x) = \lambda \left( \frac{1}{\lambda} c^T x + f(x) \right)$ 

Then take the infimum:

*   The infimum of a function scaled by  $\lambda$  is  $\lambda$  times the infimum (again, since  $\lambda > 0$ , this preserves order).

So we move the  $\lambda$  **outside** the infimum.

> ✅ This is a legal step due to positivity:  $\inf (\lambda g(x)) = \lambda \inf g(x)$  for  $\lambda > 0$ 

* * *

### 🔎 Intuition:

We are **rescaling** the first term to match the structure of the conjugate definition:

$$
f^*(y) = \sup_x (y^T x - f(x))
$$

We want to isolate the  $f(x)$ , and have a **linear function of  $x$ ** added to it.

* * *

🔹 LINE 3:
----------

$$
= \lambda \cdot \inf_{x \in \mathbb{R}^n} \left( -v^T x + f(x) \right) \quad \text{where } v := -\frac{1}{\lambda} c
$$

### ❓ Why define  $v = -\frac{1}{\lambda} c$ ?

This is a **clever substitution** to match the standard form in the conjugate.

Recall:

$$
f^*(v) = \sup_{x} \left( v^T x - f(x) \right) \Rightarrow -f^*(v) = \inf_{x} \left( -v^T x + f(x) \right)
$$

We are trying to **write the expression inside the inf** as:

$$
-f^*(v)
$$

To do this, we **define**  $v$  such that:

$$
\frac{1}{\lambda} c^T x = -v^T x \Rightarrow v = -\frac{1}{\lambda} c
$$

> ✅ This is just a change of notation to make the form match the conjugate.

* * *

### 🔎 Intuition:

We are preparing to **invoke the definition of the conjugate** — so we define a variable  $v$  that will eventually become the **input to  $f^*$ **.

This allows the entire infimum expression to be rewritten directly using  $f^*$ .

* * *

🔹 LINE 4:
----------

$$
= -\lambda \cdot \sup_{x \in \mathbb{R}^n} \left( v^T x - f(x) \right)
$$

### ❓ Why is this valid?

This is **algebraically equivalent**:

$$
\inf_x (-v^T x + f(x)) = - \sup_x (v^T x - f(x))
$$

> ✅ Always true:  $\inf_x (-g(x)) = -\sup_x g(x)$ 

So we just rewrite the infimum as a **negative of a supremum**.

And that supremum is **exactly the definition** of the conjugate:

$$
f^*(v) := \sup_x (v^T x - f(x)) \Rightarrow \text{this is } -f^*(v)
$$

* * *

### 🔎 Intuition:

This is the **pivot point** where we switch from primal form to dual form.

We are now saying:

*   "This dual function  $g(\lambda)$  can be expressed in terms of the conjugate of  $f$ , evaluated at  $v = -\frac{1}{\lambda} c$ "

* * *

🔹 LINE 5:
----------

$$
= -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

### ❓ Why is this final line valid?

Just plug back the definition of  $v$ :

$$
v = -\frac{1}{\lambda} c \Rightarrow f^*(v) = f^*\left( -\frac{1}{\lambda} c \right) \Rightarrow -\lambda f^*(v) = -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

This completes the derivation.

* * *

✅ Final Expression for Dual Function:
-------------------------------------

$$
\boxed{ g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right) } \quad \text{for } \lambda > 0
$$

* * *

✅ Summary of Step 3 Transformations
===================================

| Step | Action | Justification |
| --- | --- | --- |
| (1) |  $g(\lambda) = \inf_x \left( c^T x + \lambda f(x) \right)$  | Definition of dual function |
| (2) | Factor out  $\lambda$ :  $= \lambda \inf_x \left( \frac{1}{\lambda} c^T x + f(x) \right)$  | Allowed since  $\lambda > 0$  |
| (3) | Define  $v := -\tfrac{1}{\lambda} c$ , so inside becomes  $-v^T x + f(x)$  | Change of variables to match conjugate structure |
| (4) | Use identity:  $\inf(-g) = -\sup(g)$  | Switch to sup for conjugate |
| (5) | Recognize definition:  $= -\lambda f^*(-\tfrac{1}{\lambda} c)$  | Apply definition of  $f^*$  |

* * *

Let me know when you’re ready for:

*   Step 4: Turning this into an explicit **dual problem**
*   Step 5: Why this is a **convex optimization problem**
*   Step 6: **Examples** of computing conjugates and solving the dual
*   Step 7: **Strong duality conditions**

Or we can pick a concrete function  $f$  and go end-to-end.

## Response:
Let’s now rigorously unpack **Step 4 and Step 5** of the duality derivation, in the style you requested: clean, deep, and newcomer-friendly. These are crucial final steps where we:

*   **Step 4:** Formulate the final **dual optimization problem**
*   **Step 5:** Prove/verify that this dual problem is **convex** — _even when the primal isn’t!_

* * *

✅ Step 4 — Final Form of the Dual Problem
-----------------------------------------

### 🎯 Goal:

We’ve derived the **dual function**  $g(\lambda)$  as:

$$
\boxed{ g(\lambda) = -\lambda \cdot f^*\left( -\frac{1}{\lambda} c \right) \quad \text{for } \lambda > 0 }
$$

The **dual optimization problem** is:

$$
\boxed{ \text{maximize } g(\lambda) \quad \text{subject to } \lambda \ge 0 }
$$

* * *

### 🧩 Step-by-step formulation:

We define the dual problem formally as:

$$
\begin{aligned} \text{maximize}_{\lambda \in \mathbb{R}} \quad & g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right) \\ \text{subject to} \quad & \lambda \ge 0 \end{aligned}
$$

But observe that:

*   For  $\lambda = 0$ , the dual function becomes:
    
$$
g(0) = \inf_x c^T x + 0 \cdot f(x) = \inf_x c^T x = -\infty
$$

Because there’s no constraint, minimizing a linear function  $c^T x$  with  $c \ne 0$  leads to  $-\infty$ .  
So  $\lambda = 0$  is **not a feasible or useful point** in the dual.

Thus, we **restrict to strictly positive multipliers**:

$$
\boxed{ \textbf{(D)} \quad \max_{\lambda > 0} \left\{ -\lambda f^*\left( -\frac{1}{\lambda} c \right) \right\} }
$$

This is the **Lagrange dual problem**.

* * *

### 📌 Important properties:

*   The objective function:
    $$
    h(\lambda) := -\lambda f^*\left( -\frac{1}{\lambda} c \right)
    $$
    is a **scalar function** in one variable  $\lambda > 0$ .
*   It depends only on:
    *   The cost vector  $c$ 
    *   The conjugate function  $f^*$ 
*   Even though the primal involves a (possibly) **nonconvex** function  $f$ , the dual problem involves  $f^*$ , which is always convex.

* * *

### 🔎 Why is this dual formulation powerful?

*   You don’t need to know whether  $f$  is convex.
*   You don’t need to solve the primal.
*   If you can evaluate  $f^*$ , you can **solve the dual problem directly** as a scalar maximization problem.
*   You can recover **lower bounds** on the primal optimal value.

* * *

### 🧠 What does the dual problem represent?

*   You’re choosing a scalar multiplier  $\lambda > 0$ 
*   For each  $\lambda$ , you get a lower bound on the primal value via:
    $$
    g(\lambda) = \inf_x \left( c^T x + \lambda f(x) \right)
    $$
*   The dual maximization chooses the best such lower bound.

* * *

✅ Step 5 — Why the Dual Problem is Convex (even if  $f$  isn’t)
---------------------------------------------------------------

### 🎯 Goal:

We now prove that the dual problem:

$$
\max_{\lambda > 0} \left\{ -\lambda f^*\left( -\frac{1}{\lambda} c \right) \right\}
$$

is a **convex optimization problem**.

* * *

### 🧠 Key concept: Convexity of the **objective function**

We want to show that the objective function:

$$
h(\lambda) := -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

is a **concave** function in  $\lambda \in (0, \infty)$ .

Why?

Because we are **maximizing**  $h(\lambda)$ . So for the optimization problem to be convex, the function we are maximizing must be **concave**.

* * *

### 🔍 Strategy:

We’ll use the following fact:

> If  $f^*$  is convex, and  $\lambda \mapsto -\frac{1}{\lambda}$  is convex and decreasing, then the composition  $\lambda \mapsto f^*(-\frac{1}{\lambda} c)$  is **convex**, and so  $-\lambda f^*(-\frac{1}{\lambda} c)$  is **concave**.

Let’s break it down.

* * *

### 🔹 1. Fact:  $f^*$  is convex

By definition of the conjugate:

$$
f^*(y) = \sup_x (y^T x - f(x)) \quad \Rightarrow \quad f^* \text{ is convex}
$$

Even if  $f$  is not convex, its conjugate  $f^*$  **is convex**.

✅ Proven.

* * *

### 🔹 2. Transformation:  $\lambda \mapsto -\frac{1}{\lambda} c$ 

Let’s define:

$$
z(\lambda) := -\frac{1}{\lambda} c
$$
*   This is a **smooth**, nonlinear transformation.
*   It maps  $\lambda \in (0, \infty)$  to vectors in  $\mathbb{R}^n$ .

So the function  $\lambda \mapsto f^*\left( -\frac{1}{\lambda} c \right)$  is a **composition of a convex function** with a convex (nonlinear) map.

Under certain regularity conditions (which hold here), this preserves **convexity**.

* * *

### 🔹 3. Multiply by  $-\lambda$ 

Now we look at:

$$
h(\lambda) := -\lambda f^*\left( -\frac{1}{\lambda} c \right)
$$

We multiply a **convex** function  $f^*(-\frac{1}{\lambda} c)$  by  $-\lambda$ , which is negative.

This operation **flips the function**, turning a convex function into a **concave** one.

✅ Therefore, the function  $h(\lambda)$  is **concave** on  $(0, \infty)$ .

* * *

✅ Final Conclusion:
-------------------

*   The dual problem:
    $$
    \boxed{ \max_{\lambda > 0} \left\{ -\lambda f^*\left( -\frac{1}{\lambda} c \right) \right\} }
    $$
    is a **concave maximization problem** over a convex domain  $(0, \infty)$ 
*   So it is a **convex optimization problem**, even though the original primal problem was **not** convex.

* * *

### 💡 What’s next?

Let me know if you’d like to:

*   🔢 Plug in a **specific function**  $f(x)$  (e.g.,  $f(x) = \|x\|^2 - 1$ , or  $f(x) = \exp(x_1) + x_2^2 - 3$ ) and solve the dual end-to-end
*   🔍 Analyze **duality gap** and when **strong duality** holds
*   🧠 Go further into **Fenchel duality**, convex conjugate identities
*   📈 Visualize the dual function and primal feasible set geometrically

Or we can move to Exercise 5.4 or another item in the queue.

## Response:
Let’s zoom all the way in on **Step 4** and unpack every piece until nothing is mysterious. This step is where we go from a formula for  $g(\lambda)$  to a **bona‑fide optimization problem**.

We already have, from Step 3:

$$
g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right), \qquad \lambda>0.
$$

Now we must answer one question:

> What is the **dual problem**?

* * *

1\. What is a “dual problem” in general?
----------------------------------------

From Lagrange duality, the dual problem is **always**:

$$
\text{maximize } g(\lambda)\quad \text{subject to } \lambda \ge 0.
$$

Nothing fancy. This is the definition.

Here  $g(\lambda)$  is the dual function we computed.

So the formal dual is:

$$
\max_{\lambda\ge 0} g(\lambda).
$$

Now we substitute our explicit formula for  $g(\lambda)$ .

* * *

2\. Substituting  $g(\lambda)$ 
-------------------------------

We found

$$
g(\lambda)= \begin{cases} -\lambda f^\*\!\left(-\frac{c}{\lambda}\right), & \lambda>0,\\ -\infty, & \lambda=0. \end{cases}
$$

So the dual problem becomes

$$
\max_{\lambda\ge 0} \begin{cases} -\lambda f^\*\!\left(-\frac{c}{\lambda}\right), & \lambda>0,\\ -\infty, & \lambda=0. \end{cases}
$$

But if a feasible point gives value  $-\infty$ , it will **never** be chosen by a maximization problem. So  $\lambda=0$  is useless.

Therefore we restrict the domain to

$$
\lambda>0.
$$

This is not an assumption — it is forced by the math.

* * *

3\. Final dual problem
----------------------

So the dual problem is

$$
\boxed{ \max_{\lambda>0}\; -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). }
$$

That is it.

One scalar variable  $\lambda$ .  
One objective function built from  $f^\*$ .  
No constraints except  $\lambda>0$ .

This is the dual.

* * *

4\. What this expression really means
-------------------------------------

Look carefully:

$$
-\lambda f^\*\!\left(-\frac{c}{\lambda}\right).
$$

The argument of  $f^\*$  is

$$
y=-\frac{c}{\lambda}.
$$

That means:

*   We are choosing a slope  $y$  proportional to  $c$ ,
*   But we allow its magnitude to vary by scaling with  $\lambda$ .

Then  $f^\*(y)$  tells us:

> “How expensive is it to support  $f$  with a plane of slope  $y$ ?”

Multiplying by  $\lambda$  rescales that support back to the primal units.

The dual is choosing **which supporting hyperplane of  $f$ ** gives the tightest lower bound on the primal objective  $c^Tx$ .

* * *

5\. Why this is astonishing
---------------------------

The primal problem was:

$$
\min c^Tx \quad \text{s.t. } f(x)\le 0,
$$

which may be nonconvex, ugly, or disconnected.

The dual is:

$$
\max_{\lambda>0} -\lambda f^\*\!\left(-\frac{c}{\lambda}\right),
$$

which is a **1‑dimensional convex optimization problem** (as Step 5 shows).

So Step 4 is the moment where:

*   All  $x$ ’s disappear,
*   All nonconvexity disappears,
*   Everything is encoded into the conjugate  $f^\*$ .

That’s the magic of duality — but it is pure algebra plus geometry of supporting hyperplanes.

* * *

If you want, the next natural move is to take a specific  $f(x)$  and compute  $f^\*$  and the dual explicitly, so you can see this machine working on something concrete.

## Response:
Excellent — now let’s **unpack Step 4 and Step 5** again, this time **deeper**, **line-by-line**, and with full **granularity**, **motivation**, and **justification** — as if you're learning this from scratch and want to master every corner of the derivation.

We’ll treat:

*   **Step 4:** Turning the dual function  $g(\lambda) = -\lambda f^*\left( -\frac{1}{\lambda} c \right)$  into a formal **optimization problem**
*   **Step 5:** Proving rigorously that this dual problem is a **convex optimization problem**, despite the primal being possibly nonconvex

* * *

✅ STEP 4 — Build the Dual Problem from the Dual Function
========================================================

* * *

🎯 Step 4 Objective
-------------------

We already computed the **dual function**:

$$
g(\lambda) = -\lambda f^*\left(-\frac{1}{\lambda} c\right)
$$

Now we want to convert this into a **formal optimization problem**: the **Lagrange dual** of the primal problem.

* * *

### 🔹 What is a Dual Problem?

In general, for any Lagrange dual function  $g(\lambda)$ , the **dual problem** is defined as:

$$
\boxed{ \max_{\lambda \ge 0} g(\lambda) }
$$

That’s the whole idea: we're trying to get the **best possible lower bound** on the **primal optimal value**, by maximizing the dual function over all dual variables  $\lambda \ge 0$ .

* * *

### 🔹 Apply it here

Given:

$$
g(\lambda) = -\lambda f^*\left(-\frac{1}{\lambda} c\right)
$$

So we write:

$$
\boxed{ \textbf{(D)} \qquad \max_{\lambda \ge 0} \left\{ -\lambda f^*\left(-\frac{1}{\lambda} c\right) \right\} }
$$

* * *

### 🔹 But wait: what about  $\lambda = 0$ ? Is it valid?

Let’s test what happens at  $\lambda = 0$ :

$$
g(0) = \inf_{x \in \mathbb{R}^n} c^T x + 0 \cdot f(x) = \inf_x c^T x = -\infty
$$

This happens because:

*   There are no constraints
*    $c^T x$  is unbounded below if  $c \ne 0$ 

✅ So:  $\lambda = 0$  gives us a meaningless lower bound — it's always  $-\infty$ 

* * *

### 🔹 Final domain:  $\lambda > 0$ 

So the **actual domain** where  $g(\lambda)$  gives meaningful (finite) values is:

$$
\boxed{ \lambda > 0 }
$$

So the **final form of the dual problem** is:

$$
\boxed{ \textbf{(D)} \qquad \max_{\lambda > 0} \left\{ -\lambda f^*\left(-\frac{1}{\lambda} c\right) \right\} }
$$

* * *

### 🔍 Let's interpret this function

This function:

$$
\lambda \mapsto -\lambda f^*\left(-\frac{1}{\lambda} c\right)
$$

tells you:

*   How good a lower bound on the primal you get for each dual multiplier  $\lambda > 0$ 
*   The dual problem picks the **best** such bound (i.e., the maximum over all  $\lambda > 0$ )

Even if  $f$  is not convex, we can define this dual function and optimize it.

* * *

### ✅ Summary of Step 4

| What we had | What we did |
| --- | --- |
| Dual function  $g(\lambda) = -\lambda f^*(-\frac{1}{\lambda} c)$  | Derived from Lagrangian |
| Domain check |  $\lambda = 0 \Rightarrow -\infty$  → restrict to  $\lambda > 0$  |
| Dual problem |  $\max_{\lambda > 0} \left\{ -\lambda f^*\left(-\frac{1}{\lambda} c\right) \right\}$  |

* * *

✅ STEP 5 — Why the Dual Problem is Convex
=========================================

* * *

🎯 Goal
-------

Even though the primal problem:

$$
\min_{x} c^T x \quad \text{subject to } f(x) \le 0
$$

might be **nonconvex** (because  $f$  is arbitrary), the **dual problem**:

$$
\boxed{ \max_{\lambda > 0} \left\{ -\lambda f^*\left(-\frac{1}{\lambda} c\right) \right\} }
$$

is **always a convex optimization problem**.

Let’s rigorously prove that.

* * *

🔍 Key Concepts to Use
----------------------

To show that this is a convex problem, we need to prove:

*   The **objective function**  $h(\lambda) := -\lambda f^*(-\tfrac{1}{\lambda} c)$  is **concave**
*   The domain  $(0, \infty)$  is a **convex set**

Then, we’ll be **maximizing a concave function over a convex domain**, which qualifies as a **convex optimization problem**.

* * *

🔹 Step 1: Show that  $f^*$  is convex
--------------------------------------

From the definition:

$$
f^*(y) = \sup_x (y^T x - f(x))
$$

This is a **pointwise supremum** over affine functions of  $y$ , so  $f^*$  is always convex — even if  $f$  is not.

✅ So:

$$
f^*: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\} \quad \text{is convex}
$$

* * *

🔹 Step 2: Define the function  $h(\lambda) := -\lambda f^*(-\frac{1}{\lambda} c)$ 
-----------------------------------------------------------------------------------

Let’s define:

$$
h(\lambda) := -\lambda f^*\left(-\frac{1}{\lambda} c\right)
$$

We want to prove this is **concave in  $\lambda \in (0, \infty)$ **.

* * *

🔹 Step 3: Use Composition Rules
--------------------------------

We are looking at the composition:

$$
h(\lambda) = -\lambda \cdot \underbrace{f^*\left(-\frac{1}{\lambda} c\right)}_{\text{convex in } \lambda}
$$

Let’s denote:

$$
z(\lambda) := -\frac{1}{\lambda} c
$$

This is a smooth, **nonlinear** function of  $\lambda$ . The map  $\lambda \mapsto z(\lambda)$  is **convex** on  $(0, \infty)$  because it is the composition of:

*    $\lambda \mapsto \frac{1}{\lambda}$ : convex and decreasing on  $(0, \infty)$ 
*    $x \mapsto -x c$ : affine

Then, since:

*    $f^*$  is convex
*   Composition of a convex function with a convex map can preserve convexity

So:

$$
\lambda \mapsto f^*(-\tfrac{1}{\lambda} c) \quad \text{is convex}
$$

* * *

🔹 Step 4: Multiply by  $-\lambda$ 
-----------------------------------

Now look at:

$$
h(\lambda) = -\lambda f^*(-\tfrac{1}{\lambda} c)
$$

We are multiplying a convex function  $\phi(\lambda) := f^*(-\tfrac{1}{\lambda} c)$  by  $-\lambda$ , which is **negative** for  $\lambda > 0$ .

Multiplying a convex function by a **negative scalar** flips it to a **concave** function.

Therefore:

$$
\boxed{ h(\lambda) \text{ is concave on } (0, \infty) }
$$

* * *

🔹 Step 5: Conclusion — Convex Optimization Problem
---------------------------------------------------

Now we’ve shown:

*   The **domain** of the optimization  $\lambda \in (0, \infty)$  is convex
*   The **objective function**  $h(\lambda)$  is **concave**

So the optimization problem:

$$
\boxed{ \max_{\lambda > 0} \left\{ -\lambda f^*\left(-\frac{1}{\lambda} c\right) \right\} }
$$

is a **concave maximization** over a convex set — which is a **convex optimization problem**.

* * *

✅ Step 5 Conclusion
-------------------

| What we needed | What we proved |
| --- | --- |
| Is  $f^*$  convex? | ✅ Yes — always |
| Is  $\lambda \mapsto f^*(-\frac{1}{\lambda} c)$  convex? | ✅ Yes |
| Is  $h(\lambda) = -\lambda f^*(-\frac{1}{\lambda} c)$  concave? | ✅ Yes |
| Convex optimization problem? | ✅ Yes — maximizing concave function over convex domain |

* * *

🧠 What this tells us:
----------------------

Even if the **primal is not convex**, we still get a **well-posed convex dual** problem — which we can solve to get **lower bounds** on the primal value.

In special cases, we’ll get **strong duality** (i.e., primal = dual optimum) — more on that later.

* * *

Let me know when you're ready to:

*   🔢 Plug in a real example  $f(x)$ 
*   📈 Graph the dual/primal behavior
*   🔁 Study biconjugates and strong duality
*   🧪 Do Exercise 5.4 next

Or say “continue” and I’ll walk you through the next step.

## Response:
Thought for 9s

Yes — **for any Lagrangian dual**, you can always prove “the dual is convex” with that one-line envelope argument. You just need to say it correctly:

*   The dual objective  $g(\cdot)$  is **concave**, because it is a **pointwise infimum of affine functions** of the dual variables.
*   Equivalently,  $-g(\cdot)$  is **convex**, because it is a **pointwise supremum of affine functions**.

That’s the universal, convexity-free reason Lagrange duals are convex optimization problems.

Here’s the clean version with the exact logic (and the common pitfall fixed).

* * *

1) The universal fact behind Lagrange duality
---------------------------------------------

Take a generic constrained problem with Lagrangian

$$
L(x,\lambda,\nu)= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \nu^T h(x),
$$

with  $\lambda \ge 0$  for inequality constraints,  $\nu\in\mathbb{R}^p$  free for equalities.

For any **fixed**  $x$ , the function of the dual variables

$$
(\lambda,\nu)\mapsto L(x,\lambda,\nu)
$$

is **affine** (linear + constant) in  $(\lambda,\nu)$ . That’s because it’s literally “constant in  $(\lambda,\nu)$ ” plus “linear combination of  $\lambda,\nu$ ”.

Then the dual function is

$$
g(\lambda,\nu)=\inf_x L(x,\lambda,\nu).
$$

Now apply the envelope rule:

> The pointwise **infimum** of affine functions is **concave**.

So  $g$  is concave in  $(\lambda,\nu)$ , always — no assumptions on convexity of the primal functions  $f_i,h$ .

And since the dual problem is

$$
\max_{\lambda\ge 0,\ \nu\ \text{free}} g(\lambda,\nu),
$$

you are maximizing a concave function over a convex set (halfspace/product with  $\mathbb{R}^p$ ), which is exactly what “convex optimization problem” means in dual form.

* * *

2) The “one-line proof” written explicitly
------------------------------------------

Pick two dual points  $u_1=(\lambda_1,\nu_1)$ ,  $u_2=(\lambda_2,\nu_2)$ , and  $0\le\theta\le 1$ . Let  $u_\theta=\theta u_1+(1-\theta)u_2$ .

Because  $L(x,u)$  is affine in  $u$ ,

$$
L(x,u_\theta)=\theta L(x,u_1)+(1-\theta)L(x,u_2).
$$

Now take inf over  $x$  on both sides:

$$
g(u_\theta)=\inf_x L(x,u_\theta) =\inf_x\big(\theta L(x,u_1)+(1-\theta)L(x,u_2)\big).
$$

Use the basic inequality (true for any functions  $A,B$ ):

$$
\inf_x \big(\theta A(x)+(1-\theta)B(x)\big)\ \ge\ \theta\inf_x A(x)+(1-\theta)\inf_x B(x).
$$

Apply it with  $A(x)=L(x,u_1)$ ,  $B(x)=L(x,u_2)$ :

$$
g(u_\theta)\ \ge\ \theta g(u_1)+(1-\theta)g(u_2).
$$

That is exactly concavity of  $g$ .

* * *

3) The pitfall: “supremum of affine” vs “infimum of affine”
-----------------------------------------------------------

People often say “supremum of affine is convex” (true) and then accidentally use “supremum” when the dual has an “inf”.

For the dual function, the right statement is:

*    $g = \inf_x(\text{affine in dual vars})$  ⇒ **concave**.
*    $-g = \sup_x(-\text{affine})$  ⇒ **convex**.

So if you really want the “supremum of affine” slogan, you can apply it to  $-g$ , not  $g$ .

* * *

4) Edge cases (still fine, just say “extended-valued concave”)
--------------------------------------------------------------

Sometimes  $g(\lambda)\equiv -\infty$  for some region (like  $\lambda=0$  in your exercise), or  $g$  may take  $-\infty$  at some points. That does **not** break concavity; it just means  $g$  is concave as an **extended-valued** function. The dual is still a convex optimization problem; you simply restrict attention to the effective domain where  $g>-\infty$ .

* * *

So yes: in your exercise (and in general), you can always certify “the dual is convex” by the envelope argument. It’s the cleanest proof because it doesn’t even mention conjugates, perspectives, or convexity of  $f$  — it only uses that  $L$  is affine in the dual variables and that  $g$  is an infimum over  $x$ .

## Response:
Thought for 8s

Problem
-------

Given  $c\in\mathbb{R}^n$  with  $c\neq 0$  and a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  (not assumed convex), consider

$$
\begin{aligned} \min_{x\in\mathbb{R}^n}\quad & c^T x\\ \text{s.t.}\quad & f(x)\le 0. \end{aligned} \tag{P}
$$
1.  Derive the Lagrange dual in terms of the conjugate  $f^\*$ .
2.  Show the dual is a convex optimization problem (even if  $f$  is not convex).

* * *

Step 1: Lagrangian
------------------

There is one inequality constraint  $f(x)\le 0$ , so we introduce one multiplier  $\lambda\ge 0$ .

The **Lagrangian** is

$$
L(x,\lambda)=c^T x+\lambda f(x),\qquad \lambda\ge 0.
$$

No convexity assumptions are needed to define  $L$ .

* * *

Step 2: Dual function  $g(\lambda)$ 
------------------------------------

The **dual function** is the infimum of the Lagrangian over the primal variable:

$$
g(\lambda)=\inf_{x\in\mathbb{R}^n} L(x,\lambda) =\inf_{x\in\mathbb{R}^n}\big(c^T x+\lambda f(x)\big),\qquad \lambda\ge 0.
$$

This is always a lower bound on the primal optimum  $p^\*$  (weak duality), but we won’t need that fact to compute  $g$ .

* * *

Step 3: Express  $g(\lambda)$  using the conjugate  $f^\*$ 
-----------------------------------------------------------

### 3.1 Definition of conjugate

The (Fenchel/convex) conjugate of  $f$  is

$$
f^\*(y)=\sup_{x\in\mathbb{R}^n}\big(y^T x - f(x)\big).
$$

This definition makes sense even if  $f$  is nonconvex;  $f^\*$  is always convex in  $y$ .

### 3.2 A key identity

For any  $a\in\mathbb{R}^n$ ,

$$
\inf_{x}\big(f(x)+a^T x\big) = -\,f^\*(-a). \tag{★}
$$

**Proof of (★):**

$$
\inf_x (f(x)+a^T x) = -\sup_x\big(-(f(x)+a^T x)\big) = -\sup_x\big((-a)^T x - f(x)\big) = -f^\*(-a).
$$

Done.

### 3.3 Apply the identity to  $g(\lambda)$  (case  $\lambda>0$ )

Assume  $\lambda>0$ . Then

$$
g(\lambda)=\inf_x\big(c^T x+\lambda f(x)\big) =\lambda \inf_x\Big(f(x)+\frac{1}{\lambda}c^T x\Big)
$$

(using  $\inf_x(\lambda \phi(x))=\lambda\inf_x\phi(x)$  for  $\lambda>0$ ).

Let  $a=\frac{c}{\lambda}$ . Then by (★),

$$
\inf_x\Big(f(x)+\frac{1}{\lambda}c^T x\Big)=\inf_x\big(f(x)+a^T x\big)=-f^\*(-a) =-f^\*\!\left(-\frac{c}{\lambda}\right).
$$

Therefore, for  $\lambda>0$ ,

$$
\boxed{ g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). } \tag{1}
$$

### 3.4 The edge case  $\lambda=0$ 

$$
g(0)=\inf_x\big(c^T x+0\cdot f(x)\big)=\inf_x c^T x.
$$

Since  $c\neq 0$ , the linear function  $c^T x$  is unbounded below, hence

$$
\boxed{g(0)=-\infty.} \tag{2}
$$

So the only potentially useful values for the dual maximization are  $\lambda>0$ .

* * *

Step 4: The dual problem
------------------------

By definition, the Lagrange dual problem is

$$
\max_{\lambda\ge 0} g(\lambda).
$$

Using (1)–(2), we can equivalently write it as maximizing over  $\lambda>0$ :

$$
\boxed{ \begin{aligned} \text{maximize}\quad & -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right)\\ \text{subject to}\quad & \lambda>0. \end{aligned} } \tag{D}
$$

That is the dual problem in terms of the conjugate  $f^\*$ .

* * *

Step 5: Why the dual is a convex optimization problem
-----------------------------------------------------

A “convex optimization problem” can be written either as:

*   minimize a **convex** function over a convex set, or
*   maximize a **concave** function over a convex set.

Here the feasible set  $\{\lambda>0\}$  (or  $\{\lambda\ge 0\}$  with  $g(0)=-\infty$ ) is convex (an interval). So we just need to show the dual objective is concave in  $\lambda$ .

### Method A (the universal one-line argument)

For each fixed  $x$ , the Lagrangian is affine in  $\lambda$ :

$$
L(x,\lambda)=c^T x+\lambda f(x) \quad\text{(a line in }\lambda\text{)}.
$$

The dual function is the pointwise infimum of these affine functions:

$$
g(\lambda)=\inf_x L(x,\lambda).
$$

**Fact:** the pointwise infimum of affine functions is concave.  
Therefore  $g(\lambda)$  is concave on  $\lambda\ge 0$  (as an extended-valued concave function, allowing  $-\infty$ ).

So  $\max_{\lambda\ge 0} g(\lambda)$  (equivalently  $\max_{\lambda>0} g(\lambda)$ ) is maximizing a concave function over a convex set ⇒ a convex optimization problem.

### Method B (optional, via conjugates/perspectives)

From (1),

$$
g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right).
$$

Since  $f^\*$  is convex, the function  $\lambda\mapsto \lambda f^\*(y/\lambda)$  is the **perspective** of  $f^\*$  and is convex in  $(\lambda,y)$  for  $\lambda>0$ . Fixing  $y=-c$ ,  $\lambda\mapsto \lambda f^\*(-c/\lambda)$  is convex; multiplying by  $-1$  gives concavity of  $g$ .

Either way, the dual is convex.

* * *

Final answer (boxed)
--------------------

*   Conjugate:
    
$$
f^\*(y)=\sup_x (y^T x-f(x)).
$$
*   Dual function:
    
$$
g(\lambda)=\inf_x(c^T x+\lambda f(x))= \begin{cases} -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right), & \lambda>0,\\ -\infty, & \lambda=0, \end{cases} \quad (\text{since }c\neq 0).
$$
*   Dual problem:
    
$$
\boxed{ \max_{\lambda>0}\; -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). }
$$
*   Convexity of the dual:  $g$  is concave because it is the pointwise infimum (over  $x$ ) of affine functions of  $\lambda$ ; hence maximizing  $g$  over  $\lambda>0$  is a convex optimization problem.

One important caveat: because  $f$  is not assumed convex, **strong duality is not guaranteed** (there may be a duality gap). Weak duality always holds.

## Response:
Absolutely. I’ll write a “final solution” that is **maximally explicit**: every definition, every inequality, every algebraic transformation, every domain issue, and the exact reason the dual is convex even when  $f$  is not.

* * *

0) The primal problem and what “optimal value” means
----------------------------------------------------

You are given:

*   a vector  $c\in\mathbb{R}^n$  with  $c\neq 0$ ,
*   a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  (possibly nonconvex; possibly extended-valued).

The primal problem is

$$
\begin{aligned} \text{minimize}\quad & c^T x \\ \text{subject to}\quad & f(x)\le 0. \end{aligned} \qquad (P)
$$

Define the feasible set

$$
\mathcal{F}=\{x\in\mathbb{R}^n:\ f(x)\le 0\}.
$$

Define the primal optimal value (use  $\inf$  because a minimizer might not exist)

$$
p^\star=\inf_{x\in\mathcal{F}} c^T x.
$$

No convexity assumptions so far.

* * *

1) Lagrangian: why it has the form  $c^Tx+\lambda f(x)$  and why  $\lambda\ge 0$ 
---------------------------------------------------------------------------------

There is one inequality constraint  $f(x)\le 0$ . The Lagrangian attaches a nonnegative multiplier  $\lambda\ge 0$ :

$$
L(x,\lambda)=c^T x+\lambda f(x),\qquad \lambda\ge 0.
$$

Why must  $\lambda\ge 0$ ? Because for feasible  $x$  we have  $f(x)\le 0$ , so multiplying by  $\lambda\ge 0$  preserves the inequality:

$$
f(x)\le 0 \ \Rightarrow\ \lambda f(x)\le 0.
$$

Therefore, for every feasible  $x$  and every  $\lambda\ge 0$ ,

$$
c^T x+\lambda f(x)\le c^T x. \tag{1}
$$

This inequality (1) is the seed of duality: it says the Lagrangian is always  $\le$  the objective on feasible points.

* * *

2) Dual function  $g(\lambda)$ : definition and its meaning as a certified lower bound
--------------------------------------------------------------------------------------

Define the dual function by minimizing the Lagrangian over the primal variable:

$$
g(\lambda)=\inf_{x\in\mathbb{R}^n} L(x,\lambda) =\inf_{x\in\mathbb{R}^n}\big(c^Tx+\lambda f(x)\big), \qquad \lambda\ge 0.
$$

Why does  $g(\lambda)$  give a lower bound on the primal optimum? Because for any feasible  $x$ ,

$$
g(\lambda) =\inf_z \big(c^Tz+\lambda f(z)\big) \le c^Tx+\lambda f(x) \le c^Tx
$$

(using first “inf ≤ value at feasible  $x$ ” and then (1)). Taking inf over feasible  $x$  gives

$$
g(\lambda)\le p^\star \qquad \forall \lambda\ge 0. \tag{2}
$$

This is **weak duality**, and it holds with zero convexity assumptions.

* * *

3) The dual problem: definition
-------------------------------

Since each  $\lambda\ge 0$  yields a lower bound  $g(\lambda)\le p^\star$ , we try to make that lower bound as large (tight) as possible:

$$
\text{maximize } g(\lambda)\quad \text{subject to } \lambda\ge 0. \qquad (D\_\text{abstract})
$$

So far this is purely definitional.

The exercise asks: compute  $g(\lambda)$  in terms of the conjugate  $f^\*$ , and then show the resulting dual is convex.

* * *

4) Conjugate  $f^\*$ : definition (works even if  $f$  is nonconvex)
--------------------------------------------------------------------

Define the (Fenchel) conjugate:

$$
f^\*(y)=\sup_{x\in\mathbb{R}^n}\big(y^T x - f(x)\big). \tag{3}
$$

Two important meta-facts:

1.  This definition does **not** require  $f$  convex.
2.   $f^\*$  is **always convex** in  $y$  because it is a supremum of affine functions of  $y$  (each term  $y\mapsto y^Tx-f(x)$  is affine).

We’ll use (3) as an algebraic tool.

* * *

5) Compute  $g(\lambda)$  in terms of  $f^\*$  (this is the heart)
------------------------------------------------------------------

### 5.1 A key identity you must know (and we prove it)

For any vector  $a\in\mathbb{R}^n$ ,

$$
\inf_{x}\big(f(x)+a^T x\big)=-f^\*(-a). \tag{4}
$$

Proof of (4), line-by-line:

Start from the left:

$$
\inf_x \big(f(x)+a^Tx\big).
$$

Use the general identity  $\inf u = -\sup(-u)$ :

$$
\inf_x \big(f(x)+a^Tx\big) = -\sup_x\big(-(f(x)+a^Tx)\big).
$$

Distribute the minus sign:

$$
-(f(x)+a^Tx) = -f(x)-a^Tx = (-a)^Tx - f(x).
$$

So:

$$
\inf_x \big(f(x)+a^Tx\big) = -\sup_x\big((-a)^Tx - f(x)\big).
$$

Now compare with the definition (3): the right-hand supremum is exactly  $f^\*(-a)$ . Therefore

$$
\inf_x \big(f(x)+a^Tx\big)=-f^\*(-a).
$$

Done.

This identity is true regardless of convexity.

* * *

### 5.2 Apply the identity to  $g(\lambda)$  for  $\lambda>0$ 

Start from:

$$
g(\lambda)=\inf_x\big(c^Tx+\lambda f(x)\big).
$$

Assume  $\lambda>0$ . Factor  $\lambda$  out **carefully**:

$$
c^Tx+\lambda f(x) =\lambda\left(f(x)+\frac{1}{\lambda}c^Tx\right).
$$

Now use the order-preserving property of scaling an infimum by a positive number:

If  $\lambda>0$ , then

$$
\inf_x \lambda\,\phi(x)=\lambda\inf_x \phi(x).
$$

(Reason: multiplying by a positive constant does not change which value is smallest, it just scales all values.)

So:

$$
g(\lambda) = \lambda \inf_x\left(f(x)+\frac{1}{\lambda}c^Tx\right).
$$

Now set

$$
a=\frac{c}{\lambda}.
$$

Then  $\frac{1}{\lambda}c^Tx=a^Tx$ , so

$$
g(\lambda) = \lambda \inf_x\big(f(x)+a^Tx\big).
$$

Apply identity (4):

$$
\inf_x\big(f(x)+a^Tx\big)=-f^\*(-a).
$$

Thus:

$$
g(\lambda) = \lambda\left(-f^\*(-a)\right) = -\lambda f^\*(-a) = -\lambda f^\*\left(-\frac{c}{\lambda}\right).
$$

So for  $\lambda>0$ ,

$$
\boxed{ g(\lambda)= -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right). } \tag{5}
$$

* * *

### 5.3 The edge case  $\lambda=0$  (why the dual domain effectively becomes  $\lambda>0$ )

At  $\lambda=0$ ,

$$
g(0)=\inf_x \big(c^Tx+0\cdot f(x)\big)=\inf_x c^Tx.
$$

Because  $c\neq 0$ , the linear function  $x\mapsto c^Tx$  is unbounded below. Explicitly: take  $x_t=-t c$ . Then

$$
c^T x_t = c^T(-t c)=-t\|c\|^2\to -\infty \quad (t\to\infty).
$$

Hence

$$
\boxed{g(0)=-\infty.} \tag{6}
$$

So  $\lambda=0$  will never be optimal for maximizing  $g$ .

* * *

6) The final explicit dual problem (in terms of  $f^\*$ )
---------------------------------------------------------

By definition, the dual is  $\max_{\lambda\ge 0} g(\lambda)$ . Using (5)–(6), we can write it equivalently as:

$$
\boxed{ \begin{aligned} \text{maximize}\quad & -\lambda\, f^\*\!\left(-\frac{c}{\lambda}\right) \\ \text{subject to}\quad & \lambda>0. \end{aligned} } \qquad (D)
$$

That is the requested dual in terms of  $f^\*$ .

* * *

7) Why the dual problem is convex (even if  $f$  is nonconvex)
--------------------------------------------------------------

You want to show that the dual optimization problem is a **convex optimization problem**.

Since it is written as a maximization, the criterion is:

*   feasible set must be convex,
*   objective must be concave.

### 7.1 The feasible set is convex

The domain  $\{\lambda>0\}\subset\mathbb{R}$  is an interval, hence convex. (Same for  $\{\lambda\ge 0\}$ , but we exclude  $\lambda=0$  because it gives  $-\infty$ .)

So we only need concavity of  $g(\lambda)$ .

* * *

### 7.2 Universal one-line concavity proof (the cleanest and always valid)

Recall

$$
g(\lambda)=\inf_x \big(c^Tx+\lambda f(x)\big).
$$

Fix any  $x$ . Consider the function of  $\lambda$ :

$$
\ell_x(\lambda)=c^Tx+\lambda f(x).
$$

For fixed  $x$ ,  $c^Tx$  and  $f(x)$  are just numbers, so  $\ell_x(\lambda)$  is an **affine (linear) function** of  $\lambda$ .

Now  $g(\lambda)$  is the pointwise infimum (over all  $x$ ) of these affine functions:

$$
g(\lambda)=\inf_x \ell_x(\lambda).
$$

**Fact:** pointwise infimum of affine functions is concave.

If you want the inequality proof (no “facts” taken on faith), here it is:

Take any  $\lambda_1,\lambda_2\ge 0$  and  $\theta\in[0,1]$ . Let  $\lambda_\theta=\theta\lambda_1+(1-\theta)\lambda_2$ .

For each fixed  $x$ ,

$$
\ell_x(\lambda_\theta) = c^Tx+\lambda_\theta f(x) = c^Tx+\big(\theta\lambda_1+(1-\theta)\lambda_2\big)f(x) = \theta(c^Tx+\lambda_1 f(x))+(1-\theta)(c^Tx+\lambda_2 f(x)) = \theta\ell_x(\lambda_1)+(1-\theta)\ell_x(\lambda_2).
$$

Now take inf over  $x$  on both sides:

$$
g(\lambda_\theta) =\inf_x \ell_x(\lambda_\theta) =\inf_x \big(\theta\ell_x(\lambda_1)+(1-\theta)\ell_x(\lambda_2)\big).
$$

Use the general inequality (true for any real-valued functions  $A(x),B(x)$ ):

$$
\inf_x\big(\theta A(x)+(1-\theta)B(x)\big)\ \ge\ \theta\inf_x A(x)+(1-\theta)\inf_x B(x).
$$

(Reason: for every  $x$ ,  $A(x)\ge \inf A$  and  $B(x)\ge \inf B$ ; multiply by  $\theta,(1-\theta)$  and add; then take inf over  $x$ .)

Apply it with  $A(x)=\ell_x(\lambda_1)$ ,  $B(x)=\ell_x(\lambda_2)$ :

$$
g(\lambda_\theta)\ \ge\ \theta g(\lambda_1)+(1-\theta)g(\lambda_2).
$$

That is exactly the definition of concavity of  $g$ .

So  $g$  is concave on  $\lambda\ge 0$  (allowing value  $-\infty$  at  $\lambda=0$ ).

Therefore, the dual problem  $(D)$  is maximizing a concave function over a convex set, hence it is a **convex optimization problem**.

Crucially: this argument never used convexity of  $f$ . The only property used is: for fixed  $x$ , the Lagrangian is affine in  $\lambda$ .

* * *

### 7.3 Optional “conjugate/perspective” viewpoint (secondary proof)

You can also see concavity from the explicit form (5):

$$
g(\lambda)=-\lambda f^\*\!\left(-\frac{c}{\lambda}\right).
$$

Since  $f^\*$  is convex, the map  $(\lambda,y)\mapsto \lambda f^\*(y/\lambda)$  is the **perspective** of  $f^\*$  and is convex on  $\lambda>0$ . Fixing  $y=-c$  yields convexity of  $\lambda\mapsto \lambda f^\*(-c/\lambda)$ . Multiply by  $-1$  gives concavity of  $g$ . Same conclusion.

* * *

8) What you can and cannot conclude (important caveat)
------------------------------------------------------

*   The dual is always convex (as shown).
*   Weak duality always holds:  $d^\star\le p^\star$ .
*   But since  $f$  is not assumed convex, **strong duality can fail**: you can have a strict duality gap  $d^\star<p^\star$ , and KKT conditions need not hold.

This is exactly why the exercise is interesting: it separates “duals are convex” (always true) from “duals are tight” (needs convexity/regularity).

* * *

Final boxed answer
------------------

Conjugate:

$$
f^\*(y)=\sup_x(y^Tx-f(x)).
$$

Dual function:

$$
g(\lambda)=\inf_x(c^Tx+\lambda f(x))= \begin{cases} -\lambda f^\*\!\left(-\dfrac{c}{\lambda}\right), & \lambda>0,\\[6pt] -\infty, & \lambda=0, \end{cases} \quad (\text{since }c\neq 0).
$$

Dual problem:

$$
\boxed{ \max_{\lambda>0}\ -\lambda f^\*\!\left(-\frac{c}{\lambda}\right). }
$$

Convexity:  
 $g(\lambda)$  is concave because it is the pointwise infimum (over  $x$ ) of affine functions of  $\lambda$ ; hence maximizing  $g$  over the convex set  $\{\lambda>0\}$  is a convex optimization problem.

* * *

If you want to really “cement” this, the next best move is: pick a concrete  $f(x)$  (say quadratic, norm constraint, exponential, indicator of a set), compute  $f^\*$  explicitly, and solve the 1D dual. That’s where the machinery stops being symbolic and becomes muscle memory.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)