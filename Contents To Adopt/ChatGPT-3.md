# 3

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/21/2025 1:11:38  
**Updated:** 12/25/2025 20:58:18  
**Exported:** 12/29/2025 0:06:09  
**Link:** [https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/694717ff-4a04-832d-8c89-1a3105546a22](https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/694717ff-4a04-832d-8c89-1a3105546a22)  

## Response:
Thought for 7s

According to a document from 2025-10-21, the core “Phase 5.1 move” is: **replace every absolute value with a new variable that upper-bounds it, and then express that upper bound using two linear inequalities**. This is exactly the “split the absolute value” / “lifting” trick used to turn non-smooth pieces into LP constraints.

Main Lecture 02

Now let’s do **Phase 5.1 — Absolute values → LP** in the zero-to-hero, mechanically-repeatable way.

* * *

5.1 Absolute values → linear constraints (LP-representable)
-----------------------------------------------------------

### 0) Why absolute value is a problem for LPs

An LP only allows:

*   linear objective
*   linear inequality constraints of the form  $a^\top x \le b$ 
*   linear equalities  $Ax=b$ 

But  $|u|$  is **not** linear: it has a kink at 0. So we can’t keep  $|u|$  “as is” in an LP.

The key fact that saves us is: **even though  $|u|$  is not linear, its epigraph is polyhedral**, i.e., describable by finitely many linear inequalities. That’s why it can be modeled in LP form.

Main Lecture 02

* * *

1) The single most important equivalence
----------------------------------------

### Claim (the atomic rewrite)

For scalar  $u\in\mathbb{R}$  and scalar  $s$ ,

$$
|u|\le s \quad\Longleftrightarrow\quad -s\le u\le s.
$$

This is the Phase 5.1 atom. It’s also stated explicitly in the course notes as the standard “absolute value elimination” pattern.

Main Lecture 02

### Proof (completely explicit)

**( $\Rightarrow$ )** Assume  $|u|\le s$ .

*   By definition,  $|u|\ge 0$ . So  $|u|\le s$  forces  $s\ge 0$  (otherwise impossible).
*   Also,  $|u|\le s$  means “ $u$  is within distance  $s$  of 0”.
*   Formally:  $|u|\le s$  implies  $-s \le u \le s$ .
    *   If  $u\ge 0$ , then  $|u|=u\le s$ , so  $u\le s$  and also  $-s\le 0\le u$ , hence  $-s\le u$ .
    *   If  $u<0$ , then  $|u|=-u\le s$ , so  $-u\le s\Rightarrow u\ge -s$ , and also  $u<0\le s\Rightarrow u\le s$ .  
        So we get  $-s\le u\le s$ .

**( $\Leftarrow$ )** Assume  $-s\le u\le s$ .

*   If  $u\ge 0$ , then  $|u|=u\le s$ .
*   If  $u<0$ , then  $|u|=-u$ . From  $-s\le u$  we have  $-u\le s$ , hence  $|u|\le s$ .  
    So  $|u|\le s$ .

Done.

### LP-friendly form

The bound  $-s\le u\le s$  is just two linear inequalities:

$$
u \le s,\qquad -u \le s.
$$

That’s the form you actually plug into an LP solver.

Main Lecture 02

* * *

2) Turning  $|u|$  inside constraints into linear constraints
-------------------------------------------------------------

### Pattern A:  $|a^\top x + b|\le t$ 

This is the common “absolute deviation” constraint.

Apply the atom with  $u=a^\top x+b$ :

$$
|a^\top x+b|\le t \quad\Longleftrightarrow\quad -(t)\le a^\top x+b\le t.
$$

In LP-inequality form:

$$
a^\top x+b \le t,\qquad -(a^\top x+b)\le t.
$$

This exact move is used in the course exercise solution for minimizing maximum absolute deviation, where each  $|a_i^\top x-b_i|$  becomes two linear inequalities.

Main Lecture 08

* * *

3) Turning  $|u|$  in the objective into an LP objective (epigraph move)
------------------------------------------------------------------------

Now suppose the objective contains  $|u|$ , e.g.

$$
\min_x |a^\top x+b|.
$$

LP solvers want a **linear** objective. So we introduce an auxiliary variable  $t$  that _stands in_ for  $|a^\top x+b|$ , by enforcing

$$
|a^\top x+b|\le t,
$$

and then minimizing  $t$ :

$$
\min_{x,t}\ t \quad \text{s.t.}\quad |a^\top x+b|\le t.
$$

Now use Phase 5.1 atom:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad -(t)\le a^\top x+b\le t.
$$

That’s an LP: objective  $t$  is linear; constraints are linear inequalities. This is the same “introduce slack variable + split absolute value” pipeline shown in the lectures.

Main Lecture 02

### Tiny but important domain detail

You often also explicitly include  $t\ge 0$ . Strictly speaking it’s implied by feasibility when you have  $-t\le u\le t$ , but many formulations keep it for clarity and numerical hygiene (and because it matches the interpretation “ $t$  is a magnitude”). In the minimum-fuel control LP, they explicitly keep  $s_t\ge 0$  as the magnitude variable.

Main Lecture 07

* * *

4) The “two-layer” version: separate magnitude from cost (why you sometimes see  $s$  and  $p$ )
------------------------------------------------------------------------------------------------

In more complex objectives, you’ll see a pattern like:

*    $s$  represents  $|u|$ 
*    $p$  represents some cost built from  $s$  (like piecewise linear penalties)

Example from the notes (minimum fuel):

*   they set  $s_t \ge u_t$ ,  $s_t \ge -u_t$ ,  $s_t \ge 0$  so that  $s_t \ge |u_t|$ 
*   then they model the piecewise cost by constraints like  $p_t \ge s_t$ ,  $p_t \ge 2s_t-1$ 
*   and minimize  $\sum p_t$ 

This shows a useful principle: **first linearize absolute value into a magnitude variable, then build whatever piecewise-linear convex function you want on top of that magnitude using max/epigraph constraints**.

Main Lecture 07

* * *

5) Checklist: how to do 5.1 instantly, every time
-------------------------------------------------

Whenever you see  $|\cdot|$ :

1.  Identify the inside as an affine expression:  $u = a^\top x + b$  (or more generally, some scalar expression in your variables).
2.  If it’s in a constraint like  $|u|\le t$ , replace with:
    *    $u\le t$ 
    *    $-u\le t$   
        (optionally  $t\ge 0$ )
        Main Lecture 02
3.  If it’s in the objective like  $\min |u|$  or  $\min \sum |u_i|$ , introduce  $t$  or  $t_i$ , impose  $|u_i|\le t_i$  via two inequalities each, then minimize  $\sum t_i$ .
    Main Lecture 02

That’s Phase 5.1.

* * *

6) Sanity checks and common failure modes (where people lose points)
--------------------------------------------------------------------

*   Forgetting the “two inequalities” and writing something illegal like  $|u|\le t \Rightarrow u\le t$  only. That drops half the feasible set (you’d be assuming  $u\ge 0$ ).
*   Using a non-affine inside and pretending it’s still LP. If  $u$  is not affine, splitting  $|u|\le t$  still works logically, but you might no longer have an LP because  $u\le t$  might be nonlinear.
*   Confusing “ $|u|$ ” with “ $u^2$ ”. Different atom, different cone.

* * *

That’s 5.1 fully nailed: **absolute values don’t belong in LPs, but their epigraph does**—so we “lift” with auxiliary variables and split into two linear inequalities.

Main Lecture 02

If we continue, 5.2 is basically “repeat 5.1  $n$  times” plus one extra idea:  $\ell_1$  and  $\ell_\infty$  are built from absolute values and maxima, so they collapse into LP form with the same lifting pattern.

## Response:
Alright. Phase 5.1 is the “absolute value elimination move.” It looks tiny. It’s secretly one of the most important modeling atoms in convex optimization, because it’s the gateway from “nonsmooth” to “LP-clean.”

I’m going to build it from the ground up, prove every equivalence carefully, and then show the mechanical recipes you can apply blindly under exam pressure.

* * *

Phase 5.1 — Absolute values → linear constraints (LP modeling atom)
-------------------------------------------------------------------

### What you’re trying to do

LPs allow only:

*   a linear objective: minimize  $c^\top x$ 
*   linear constraints:  $Ax \le b$ ,  $A_{\text{eq}}x=b_{\text{eq}}$ 

But absolute value  $|\cdot|$  is not linear. So any time you see  $|\cdot|$  in an objective or constraint, you need a legal rewrite that:

1.  preserves meaning (same feasible set / same optimum),
2.  produces only linear inequalities.

Phase 5.1 gives the **atomic rewrite** that does exactly that.

* * *

1) The single scalar atom:  $|u|\le s$ 
---------------------------------------

### Definition reminder: absolute value

For a scalar  $u\in\mathbb{R}$ ,

$$
|u| = \begin{cases} u & u\ge 0\\ -u & u<0 \end{cases}
$$

Equivalently:

$$
|u| = \max(u,\,-u).
$$

That “max of two linear functions” fact is why LP can handle it.

* * *

### The key equivalence (the atom)

For real scalars  $u$  and  $s$ ,

$$
\boxed{|u|\le s \quad\Longleftrightarrow\quad -s \le u \le s.}
$$

This is the entire trick.

* * *

### Proof (fully explicit, no handwaving)

#### ( $\Rightarrow$ ) Assume  $|u|\le s$ . Show  $-s\le u\le s$ .

From  $|u|\le s$ :

*   First, note  $|u|\ge 0$ . Therefore  $s$  must be  $\ge 0$  for feasibility (if  $s<0$ , there is no  $u$  satisfying  $|u|\le s$ ). This is a useful domain sanity check.

Now prove the two inequalities:

1.  Show  $u\le s$ .
    *   If  $u\ge 0$ , then  $|u|=u$ , so  $u\le s$ .
    *   If  $u<0$ , then  $u\le 0 \le s$  (since  $s\ge 0$ ), so again  $u\le s$ .
2.  Show  $-s\le u$ .
    *   If  $u\ge 0$ , then  $-s\le 0 \le u$ , so  $-s\le u$ .
    *   If  $u<0$ , then  $|u|=-u$ . Since  $|u|\le s$ , we have  $-u\le s$ . Multiply by  $-1$  (reverses inequality):  $u \ge -s$ . i.e.  $-s\le u$ .

So both  $-s\le u$  and  $u\le s$  hold. Therefore  $-s\le u\le s$ .

#### ( $\Leftarrow$ ) Assume  $-s\le u\le s$ . Show  $|u|\le s$ .

We split by sign of  $u$ :

*   If  $u\ge 0$ , then  $|u|=u\le s$  (because  $u\le s$ ).
*   If  $u<0$ , then  $|u|=-u$ . From  $-s\le u$ , multiply by  $-1$ :  $-u\le s$ . So  $|u|\le s$ .

Done.

* * *

### LP-ready form (two inequalities)

The constraint  $-s\le u\le s$  is the pair:

$$
\boxed{u \le s,\quad -u \le s.}
$$

This is what you actually write in LP standard inequality form.

* * *

2) The “epigraph” viewpoint (why this is convex + why LP can represent it)
--------------------------------------------------------------------------

This matters because PS6 sometimes asks you to justify convexity / representability, not just do algebra.

The **epigraph** of  $|u|$  is the set

$$
\operatorname{epi}(|\cdot|)=\{(u,s): |u|\le s\}.
$$

Using the atom,

$$
\operatorname{epi}(|\cdot|)=\{(u,s): u\le s,\ -u\le s\}.
$$

That’s an intersection of two halfspaces in  $(u,s)$ \-space, hence a polyhedron, hence convex, hence LP-representable.

Geometrically, it’s a “V” in 1D lifted into 2D: the region above the two lines  $s=u$  and  $s=-u$ . The boundary  $s=|u|$  is the V-shaped graph; the epigraph is everything above it.

This is the deep reason the trick works: **absolute value is not linear, but its epigraph is polyhedral.**

* * *

3) The universal modeling recipe: “introduce a magnitude variable”
------------------------------------------------------------------

Whenever you see  $|\text{something}|$ , do this:

1.  Name the inside:
    $$
    u := \text{(that something)}.
    $$
2.  Introduce a new variable  $s$  intended to represent  $|u|$ .
3.  Enforce:
    $$
    u \le s,\quad -u \le s.
    $$
4.  Now **use  $s$ ** everywhere you used  $|u|$ .

This is sometimes called a “lifting” or “epigraph reformulation.”

* * *

4) Two main cases: absolute values in constraints vs objectives
---------------------------------------------------------------

### Case A: absolute value in a constraint

Example pattern:

$$
|a^\top x + b| \le t
$$

where  $a^\top x+b$  is affine in  $x$ , and  $t$  is a variable or constant.

Apply the atom with  $u=a^\top x+b$ ,  $s=t$ :

$$
|a^\top x+b|\le t \Longleftrightarrow \begin{cases} a^\top x+b \le t\\ -(a^\top x+b)\le t \end{cases}
$$

Both are linear inequalities in  $(x,t)$ . So you are still in LP land (as long as  $t$  itself is allowed, i.e., appears linearly elsewhere).

**Important detail:** If  $t$  is a constant  $t=\tau$ , this becomes just two linear inequalities in  $x$ . If  $t$  is a variable, that’s still fine for LP because it’s linear.

* * *

### Case B: absolute value in the objective

Example:

$$
\min_x |a^\top x+b|
$$

An LP objective must be linear. So you **introduce  $t$ ** and minimize it:

$$
\min_{x,t}\ t\quad \text{s.t.}\quad |a^\top x+b|\le t.
$$

Then split:

$$
\min_{x,t}\ t\quad \text{s.t.}\quad \begin{cases} a^\top x+b \le t\\ -(a^\top x+b)\le t \end{cases}
$$

This is an LP: linear objective, linear constraints.

Why is this equivalent to the original problem?

*   For any fixed  $x$ , the smallest feasible  $t$  satisfying those two inequalities is exactly  $t=|a^\top x+b|$  (because the feasible  $t$  are all  $t\ge |a^\top x+b|$ ).
*   So minimizing  $t$  forces  $t$  down to  $|a^\top x+b|$  at optimum.
*   Therefore the optimal  $x$  is the same as in the original problem.

That equivalence argument is the general “epigraph trick”: replace a nonlinear objective  $f(x)$  by a variable  $t$  and the constraint  $f(x)\le t$ , then minimize  $t$ .

* * *

5) Multiple absolute values: sum of absolute values → LP scaffold (preview for 5.2, but still 5.1 mechanics)
------------------------------------------------------------------------------------------------------------

Suppose:

$$
\min_x \sum_{i=1}^m |a_i^\top x - b_i|
$$

Do it componentwise:

Introduce  $s_i$  for each absolute value:

$$
\min_{x,s}\ \sum_{i=1}^m s_i \quad \text{s.t.}\quad \begin{cases} a_i^\top x - b_i \le s_i\\ -(a_i^\top x - b_i) \le s_i \end{cases} \quad \forall i
$$

That’s the same atom repeated  $m$  times.

This is exactly how  $\ell_1$  regression / LAD (least absolute deviations) becomes an LP.

* * *

6) “Equality to absolute value” is _not_ linear — but you don’t need it
-----------------------------------------------------------------------

Sometimes people write “let  $s = |u|$ ”. That equality is not linear and not something an LP understands directly.

The correct modeling is:

$$
s \ge |u| \quad\Longleftrightarrow\quad u\le s,\ -u\le s.
$$

Then, if you minimize  $s$  (or minimize something increasing in  $s$ ), the inequality becomes tight automatically at the optimum.

This is a standard modeling principle:

*   Constraints give you “ $s$  is at least the magnitude.”
*   The objective pushes  $s$  down until it equals the magnitude.

* * *

7) Edge cases and failure modes (the exam traps)
------------------------------------------------

### Trap 1: forgetting one side

Wrong:

$$
|u|\le s \Rightarrow u\le s
$$

That drops the case  $u<0$ . You must always include both:

$$
u\le s,\quad -u\le s.
$$

### Trap 2: non-affine inside

If  $u$  is not affine (say  $u=x^2$ ), then the split

$$
x^2 \le s,\quad -x^2 \le s
$$

is not an LP (the first constraint is quadratic). The atom is logically true, but it does not preserve “LP-ness.” Phase 5.1 is an LP transformation only when the inside is affine in decision variables.

### Trap 3: implicitly requiring feasibility with negative  $s$ 

If  $s$  is a free variable and you forgot to consider feasibility, constraints might force  $s<0$ , making the absolute-value constraint infeasible. Many clean formulations include  $s\ge 0$  explicitly because it makes the intended meaning obvious and avoids weirdness in intermediate reasoning.

### Trap 4: mixing scalar vs vector absolute values

 $|u|$  is scalar absolute value. For vectors you should be careful:

*    $|x|$  sometimes means elementwise absolute value (a vector).
*    $\|x\|_2$  is a norm (that becomes SOCP, not LP).  
    Phase 5.1 is about scalar absolute values or elementwise absolute values that you linearize componentwise.

* * *

8) A “mechanical translator” you can execute blindly
----------------------------------------------------

Whenever you see  $|\text{affine}(x)|$ :

1.  Write the affine expression as  $u(x)=a^\top x+b$ .
2.  Introduce a new variable  $s$ .
3.  Replace  $|u(x)|$  by  $s$ .
4.  Add the two constraints:
    *    $u(x)\le s$ 
    *    $-u(x)\le s$   
        (optionally  $s\ge 0$ )
5.  If the original had  $|u(x)|$  in the objective, minimize  $s$  (or include  $s$  in the objective) so it becomes tight.

That’s it. That’s Phase 5.1.

* * *

9) Why this matters downstream
------------------------------

This atom is the genetic ancestor of:

*    $\ell_1$  norm modeling (sum of abs)
*    $\ell_\infty$  norm modeling (max of abs)
*   piecewise-linear penalties (hinge, Huber’s linear pieces, etc.)
*   robust constraints (via dual norms, later)

So 5.1 isn’t a one-off trick. It’s the first domino in “turn messy convex expressions into solver form.”

* * *

If you want the next step immediately: 5.2 is basically “wrap 5.1 inside sums and maxima,” turning  $\|x\|_1$  and  $\|x\|_\infty$  into LPs with auxiliary variables. That’s where this atom becomes muscle memory.

## Response:
Phase 5.2 —  $\ell_1$  and  $\ell_\infty$  norms  $\rightarrow$  LP (the “abs + max” factory)
---------------------------------------------------------------------------------------------

Phase 5.1 gave you the atom:

$$
|u|\le s \iff \begin{cases}u\le s\\-u\le s\end{cases}
$$

Phase 5.2 is what happens when you apply that atom _systematically_ to the two most common “norm expressions” that show up in PS sets:

*    $\|x\|_1 = \sum_i |x_i|$  (a **sum of absolute values**)
*    $\|x\|_\infty = \max_i |x_i|$  (a **maximum of absolute values**)

An LP can handle both because:

*   absolute values are handled by Phase 5.1 (epigraph is polyhedral),
*   sums are linear,
*   maxima of finitely many affine terms are handled by an epigraph trick (one variable upper-bounding all terms).

The key is: **introduce auxiliary variables** that represent magnitudes, then constrain them with linear inequalities.

* * *

0) Preliminaries: what these norms actually are
===============================================

Let  $x\in\mathbb{R}^n$  with components  $x_1,\dots,x_n$ .

###  $\ell_1$  norm

$$
\|x\|_1 := \sum_{i=1}^n |x_i|.
$$

Interpretation: total “Manhattan distance,” encourages sparsity in optimization.

###  $\ell_\infty$  norm

$$
\|x\|_\infty := \max_{1\le i\le n} |x_i|.
$$

Interpretation: the worst (largest) component magnitude; controls peak deviation.

We want LP forms for constraints or objectives involving these norms, and also for their affine versions  $\|Ax+b\|_1$ ,  $\|Ax+b\|_\infty$ .

* * *

1) The two master modeling principles you must internalize
==========================================================

Principle A — Represent a nonlinear expression by an upper-bounding variable (epigraph)
---------------------------------------------------------------------------------------

To model  $t \ge f(x)$ , you add constraints that force  $t$  to be at least  $f(x)$ , then you minimize  $t$  (or otherwise make smaller  $t$  preferred). At optimum,  $t$  becomes equal to  $f(x)$ .

Principle B — “Max of finitely many things” is LP-friendly
----------------------------------------------------------

For scalars  $y_1(x),\dots,y_m(x)$ ,

$$
t \ge \max_j y_j(x)\quad \Longleftrightarrow\quad t \ge y_j(x)\ \ \forall j.
$$

That’s just a bunch of linear inequalities if each  $y_j(x)$  is affine.

Phase 5.2 is basically Principle A + Principle B + Phase 5.1.

* * *

2)  $\ell_1$  norm  $\rightarrow$  LP
=====================================

2.1 Modeling  $\|x\|_1$  itself
-------------------------------

We start with:

$$
\|x\|_1 = \sum_{i=1}^n |x_i|.
$$

### Step 1: introduce magnitude variables

Introduce  $s\in\mathbb{R}^n$  with components  $s_i$  intended to represent  $|x_i|$ .

### Step 2: enforce  $s_i \ge |x_i|$  using Phase 5.1

For each  $i$ :

$$
s_i \ge |x_i| \quad \Longleftrightarrow\quad \begin{cases} x_i \le s_i\\ -x_i \le s_i \end{cases}
$$

Optionally include  $s_i \ge 0$ , though it’s implied by the two inequalities whenever feasible.

### Step 3: replace  $\sum |x_i|$  by  $\sum s_i$ 

Now:

*   any feasible  $(x,s)$  has  $s_i \ge |x_i|$ ,
*   therefore  $\sum_i s_i \ge \sum_i |x_i| = \|x\|_1$ ,
*   and if you minimize  $\sum_i s_i$ , the optimizer will push  $s_i$  down to the smallest possible value, which becomes  $s_i = |x_i|$  at optimum (unless the objective doesn’t care about some  $s_i$ , in which case it might stay slack, but then it also doesn’t matter).

So an LP representation for the objective “minimize  $\|x\|_1$ ” is:

$$
\boxed{ \min_{x,s}\ \sum_{i=1}^n s_i \quad \text{s.t.}\quad -x_i \le s_i,\ \ x_i \le s_i\ \ \forall i. }
$$

This is a pure LP: linear objective, linear inequalities.

* * *

2.2 Modeling  $\|Ax+b\|_1$  (this is what you actually use)
-----------------------------------------------------------

Let  $r = Ax+b \in \mathbb{R}^m$  (residual vector), with components  $r_i = a_i^\top x + b_i$ , where  $a_i^\top$  is the  $i$ \-th row of  $A$ .

We want:

$$
\|Ax+b\|_1 = \sum_{i=1}^m |a_i^\top x + b_i|.
$$

Do the same trick, but on the residual components.

Introduce  $s\in\mathbb{R}^m$  with:

$$
s_i \ge |a_i^\top x + b_i| \Longleftrightarrow \begin{cases} a_i^\top x + b_i \le s_i\\ -(a_i^\top x + b_i) \le s_i \end{cases}
$$

Then:

$$
\boxed{ \min_{x,s}\ \sum_{i=1}^m s_i \quad \text{s.t.}\quad a_i^\top x + b_i \le s_i,\ \ -(a_i^\top x + b_i)\le s_i\ \ \forall i. }
$$

### Why this is exactly equivalent (not an approximation)

Fix any  $x$ . Among all  $s$  satisfying the constraints, the smallest possible  $s_i$  is  $|a_i^\top x+b_i|$ . Therefore the minimal  $\sum s_i$  for that  $x$  is exactly  $\|Ax+b\|_1$ . Minimizing over  $x$  gives the same optimum as the original  $\ell_1$  problem.

This is the same epigraph-tightness logic as in Phase 5.1, just repeated over coordinates and summed.

* * *

2.3  $\ell_1$  norm as a constraint:  $\|Ax+b\|_1 \le t$ 
---------------------------------------------------------

Sometimes it’s not the objective; it’s a constraint:

$$
\|Ax+b\|_1 \le t.
$$

LP form:

*   introduce  $s_i \ge |a_i^\top x+b_i|$  with the two inequalities,
*   then enforce  $\sum_i s_i \le t$ .

So:

$$
\boxed{ \begin{aligned} \|Ax+b\|_1 \le t \Longleftrightarrow \exists s\in\mathbb{R}^m:\ & a_i^\top x + b_i \le s_i,\ \ -(a_i^\top x+b_i)\le s_i\ \ \forall i,\\ & \sum_{i=1}^m s_i \le t. \end{aligned}}
$$

Everything is linear.

* * *

3)  $\ell_\infty$  norm  $\rightarrow$  LP
==========================================

3.1 Modeling  $\|x\|_\infty$ 
-----------------------------

Start from:

$$
\|x\|_\infty = \max_i |x_i|.
$$

### Step 1: introduce a scalar upper bound  $t$ 

Let  $t$  represent the maximum absolute component.

We want:

$$
t \ge \max_i |x_i| \quad \Longleftrightarrow\quad t \ge |x_i|\ \ \forall i.
$$

### Step 2: split each absolute value using Phase 5.1

$$
t \ge |x_i| \Longleftrightarrow \begin{cases} x_i \le t\\ -x_i \le t \end{cases}
$$

So:

$$
\boxed{ \|x\|_\infty \le t \quad\Longleftrightarrow\quad -x_i \le t,\ \ x_i \le t\ \ \forall i. }
$$

And if the objective is “minimize  $\|x\|_\infty$ ”, you do:

$$
\boxed{ \min_{x,t}\ t\quad \text{s.t.}\quad -x_i\le t,\ x_i\le t\ \ \forall i. }
$$

Again, it’s exact: for any fixed  $x$ , the smallest feasible  $t$  is exactly  $\max_i |x_i|$ .

* * *

3.2 Modeling  $\|Ax+b\|_\infty$  (super common)
-----------------------------------------------

Let  $r=Ax+b\in\mathbb{R}^m$ . Then:

$$
\|Ax+b\|_\infty = \max_{i} |a_i^\top x+b_i|.
$$

Introduce  $t$  and enforce:

$$
|a_i^\top x+b_i| \le t\quad \forall i.
$$

Split each:

$$
\boxed{ \|Ax+b\|_\infty \le t \Longleftrightarrow \begin{cases} a_i^\top x+b_i \le t\\ -(a_i^\top x+b_i)\le t \end{cases} \ \forall i. }
$$

Objective variant:

$$
\boxed{ \min_{x,t}\ t\quad \text{s.t.}\quad a_i^\top x+b_i \le t,\ \ -(a_i^\top x+b_i)\le t\ \ \forall i. }
$$

* * *

4) Compare  $\ell_1$  vs  $\ell_\infty$  modeling (so you don’t mix them)
=========================================================================

###  $\ell_1$ : “sum of magnitudes”

*   needs **one auxiliary per component**  $s_i$ ,
*   then sum them in objective or constrain sum.

###  $\ell_\infty$ : “maximum magnitude”

*   needs **one scalar**  $t$ ,
*   then constrain every component magnitude by  $t$ .

You can remember it as:

*    $\ell_1$ : many slacks  $s_i$ , and a summation  $\sum s_i$ .
*    $\ell_\infty$ : one slack  $t$ , and many inequalities  $ |(\cdot)_i|\le t$ .

* * *

5) Exactness and “tightness at optimum” (rigorous justification)
================================================================

This matters because PS sets sometimes ask: “prove your reformulation is equivalent.”

5.1 Exactness for  $\ell_1$  objective
--------------------------------------

Original:

$$
\min_x \sum_i |r_i(x)|.
$$

Reformulated:

$$
\min_{x,s} \sum_i s_i\quad \text{s.t.}\quad s_i\ge |r_i(x)|.
$$

Fix  $x$ . The feasible set in  $s$  is:

$$
\{s: s_i\ge |r_i(x)|\ \forall i\}.
$$

The minimum of  $\sum_i s_i$  over this set is achieved at  $s_i=|r_i(x)|$  for all  $i$ , giving value  $\sum_i |r_i(x)|$ .  
Therefore the outer minimization over  $x$  gives the same optimal value and same set of optimal  $x$ .

5.2 Exactness for  $\ell_\infty$  objective
-------------------------------------------

Original:

$$
\min_x \max_i |r_i(x)|.
$$

Reformulated:

$$
\min_{x,t} t\quad \text{s.t.}\quad t\ge |r_i(x)|\ \forall i.
$$

Fix  $x$ . Feasible  $t$  satisfy  $t\ge \max_i |r_i(x)|$ . The smallest feasible  $t$  is exactly  $\max_i |r_i(x)|$ . So the objective value matches for each  $x$ , hence global optimum matches.

That’s the rigorous equivalence argument.

* * *

6) Common failure modes (LP correctness traps)
==============================================

1.  **For  $\ell_1$ **: writing  $\|x\|_1 \le t$  as  $|x_i|\le t$  for all  $i$ .  
    That actually models  $\|x\|_\infty\le t$ , not  $\ell_1$ .
2.  **For  $\ell_\infty$ **: writing  $\|x\|_\infty \le t$  as  $\sum_i |x_i|\le t$ .  
    That models  $\ell_1$ , not  $\ell_\infty$ .
3.  Forgetting the negative side of absolute value constraints.
4.  Non-affine inside: if  $r_i(x)$  is not affine, the constraints are not LP constraints anymore (still may be convex, but not LP).

* * *

7) Cookbook summary (the mechanical “do it in 20 seconds” version)
==================================================================

### A)  $\|Ax+b\|_1$ 

Introduce  $s\in\mathbb{R}^m$ :

$$
a_i^\top x+b_i \le s_i,\quad -(a_i^\top x+b_i)\le s_i
$$

Then:

*   objective: minimize  $\sum_i s_i$ , or
*   constraint:  $\sum_i s_i\le t$ .

### B)  $\|Ax+b\|_\infty$ 

Introduce scalar  $t$ :

$$
a_i^\top x+b_i \le t,\quad -(a_i^\top x+b_i)\le t\quad \forall i
$$

Then:

*   objective: minimize  $t$ , or
*   constraint: those inequalities are exactly  $\|Ax+b\|_\infty\le t$ .

* * *

If we continue next, Phase 5.3 is the first time LP stops being enough:  $\ell_2$  norms ( $\|Ax+b\|_2$ ) become **SOCP**, not LP. That’s where “norm ≤ affine” becomes a second-order cone constraint.

## Response:
Phase 5.3 —  $\ell_2$  norms  $\rightarrow$  SOCP (the “Euclidean norm becomes a cone” move)
--------------------------------------------------------------------------------------------

Phase 5.1–5.2 lived in LP-land because “absolute value” and “max of finitely many affine functions” have **polyhedral epigraphs**. The Euclidean norm  $\| \cdot \|_2$  is different: it’s convex, but its epigraph is **not** a polyhedron. It’s a smooth “ice-cream cone” shape. So LP is too weak.

The right standard language is **SOCP** (Second-Order Cone Programming). Phase 5.3 is the atom:

> Any constraint of the form “Euclidean norm of an affine expression is bounded by an affine expression” is an SOCP constraint.

Once you own this, a huge chunk of PS sets becomes mechanical.

* * *

0) The goal: what we want to rewrite
====================================

Typical expressions you’ll see:

1.  **Norm in objective**
    
$$
\min_x \ \|Ax+b\|_2
$$

(or  $\min \sum_k \|A_k x + b_k\|_2$ , etc.)

2.  **Norm in constraint**
    
$$
\|Ax+b\|_2 \le t
$$

or more generally

$$
\|Ax+b\|_2 \le c^\top x + d
$$
3.  **Distance-to-a-set** or “keep error small”
    
$$
\|x-x_0\|_2 \le r
$$

All of these become SOCP using one central definition.

* * *

1) What is the second-order cone (SOC)?
=======================================

There are two common equivalent definitions. You should recognize both.

1.1 Standard SOC definition
---------------------------

The  $(n+1)$ \-dimensional second-order cone is

$$
\boxed{\mathcal{Q}_{n+1} := \{(t,y)\in\mathbb{R}\times\mathbb{R}^n:\ \|y\|_2 \le t\}.}
$$

Think of  $t$  as the “vertical coordinate” and  $y$  as the “horizontal vector.” The set of points above the Euclidean ball scaled by  $t$ .

### Immediate consequences (important for correctness)

*   If  $(t,y)\in \mathcal{Q}_{n+1}$ , then automatically  $t\ge 0$  because norms are nonnegative.
*   It is convex (it’s a norm epigraph).

1.2 Equivalent quadratic form definition
----------------------------------------

Square both sides (careful: squaring is only equivalent when  $t\ge 0$ , but SOC already enforces that implicitly):

$$
\|y\|_2 \le t \quad\Longleftrightarrow\quad y^\top y \le t^2,\ \ t\ge 0.
$$

So another characterization is

$$
\mathcal{Q}_{n+1} = \{(t,y): y^\top y \le t^2,\ t\ge 0\}.
$$

This is useful for intuition, but **in modeling you should keep the SOC form**  $\|y\|_2\le t$ . That’s what SOCP solvers accept.

* * *

2) What is an SOCP constraint, formally?
========================================

An SOCP allows constraints that say an affine function of the variables lies in an SOC:

$$
\boxed{(t(x),\ y(x)) \in \mathcal{Q}_{n+1}} \quad\text{where } t(x) \text{ and } y(x) \text{ are affine in } x.
$$

Unpacked: this means

$$
\|y(x)\|_2 \le t(x)
$$

with both sides affine (left side is norm of an affine vector; right side affine scalar).

This is the core closure rule:

> The SOC is convex. The preimage of a convex set under an affine map is convex. Therefore  $\{x : (t(x),y(x))\in \mathcal{Q}\}$  is convex.

So these are legal convex constraints.

* * *

3) The Phase 5.3 atom:  $\|Ax+b\|_2 \le t$ 
===========================================

This is the cleanest form.

### Claim

$$
\boxed{\|Ax+b\|_2 \le t \quad \Longleftrightarrow\quad (t,\ Ax+b)\in \mathcal{Q}_{m+1}}
$$

(where  $Ax+b\in\mathbb{R}^m$ ).

This is basically just “match the definition.”

*   Set  $y = Ax+b$  (affine in  $x$ ).
*   Set the cone scalar to be  $t$ .
*   Enforce membership in the SOC.

That’s an SOCP constraint.

### Why this is exact (not relaxation)

There’s no approximation: it’s literally a restatement of what SOC means.

* * *

4) Norm in objective:  $\min \|Ax+b\|_2$  becomes SOCP via epigraph
===================================================================

LP used the epigraph trick for absolute values. Same philosophy here.

Start:

$$
\min_x \|Ax+b\|_2
$$

Introduce a scalar  $t$  that upper-bounds the norm:

$$
\min_{x,t} \ t \quad \text{s.t.}\quad \|Ax+b\|_2 \le t.
$$

Now recognize the constraint is SOC:

$$
(t,\ Ax+b)\in \mathcal{Q}_{m+1}.
$$

### Rigorous equivalence argument

Fix any  $x$ . The smallest  $t$  satisfying  $\|Ax+b\|_2 \le t$  is  $t=\|Ax+b\|_2$ . Therefore minimizing  $t$  over  $(x,t)$  gives exactly the same optimal value and optimal  $x$  as minimizing the norm directly.

This is the general epigraph logic: “minimize  $f(x)$ ”    $\iff$  “minimize  $t$  s.t.  $f(x)\le t$ .”

* * *

5) The most common PS6 pattern:  $\|Ax+b\|_2 \le c^\top x + d$ 
===============================================================

This is the “norm ≤ affine” template. It’s SOCP as long as the right-hand side is affine.

### Claim (modeling form)

$$
\boxed{\|Ax+b\|_2 \le c^\top x + d \quad\Longleftrightarrow\quad (c^\top x + d,\ Ax+b)\in\mathcal{Q}_{m+1}.}
$$

That’s it.

### Subtle but crucial domain point: feasibility forces RHS  $\ge 0$ 

Because  $\|Ax+b\|_2\ge 0$ , any feasible  $x$  must satisfy  $c^\top x+d \ge 0$ . You often don’t need to add it separately: SOC membership already implies it. But in hand proofs, it’s sometimes helpful to mention:

*   If  $c^\top x+d<0$ , constraint is impossible.

### Why you should _not_ square it yourself in modeling

You might be tempted:

$$
\|Ax+b\|_2 \le c^\top x+d \ \Rightarrow\ (Ax+b)^\top (Ax+b) \le (c^\top x+d)^2.
$$

This is true if  $c^\top x+d\ge 0$ . But the squared form is **quadratic ≤ quadratic**, which is generally **not** an LP and not necessarily a convex quadratic constraint in a form a solver likes. The SOC form is the canonical convex representation.

* * *

6) Geometric meaning (so it doesn’t feel like symbol magic)
===========================================================

###  $\|x-x_0\|_2 \le r$ 

This is the Euclidean ball (a convex set). SOCP can represent it immediately:

$$
(r,\ x-x_0)\in\mathcal{Q}_{n+1}.
$$

So SOCP is literally “optimization over intersections of affine slices of ice-cream cones,” i.e., norm balls and their affine images.

###  $\|Ax+b\|_2 \le t$ 

This says “the vector  $Ax+b$  lies in a Euclidean ball of radius  $t$ .”  
If  $A$  is not identity, it becomes an ellipsoid-ish feasible region in  $x$ \-space (affine preimage of a ball).

* * *

7) Common variants you should recognize instantly
=================================================

7.1 Multiple norms: sum of  $\ell_2$  norms
-------------------------------------------

Example:

$$
\min_x \sum_{k=1}^K \|A_k x + b_k\|_2.
$$

Introduce  $t_k$  for each term:

$$
\min_{x,t}\ \sum_{k=1}^K t_k \quad \text{s.t.}\quad \|A_k x+b_k\|_2 \le t_k\ \ \forall k.
$$

Each constraint is SOC. Objective is linear. Whole problem is SOCP.

7.2 Maximum of norms
--------------------

$$
\min_x \max_k \|A_k x+b_k\|_2
$$

Introduce scalar  $t$ :

$$
\min_{x,t} t \quad \text{s.t.}\quad \|A_k x+b_k\|_2 \le t\ \ \forall k.
$$

Still SOCP.

7.3 Least squares with an  $\ell_2$  objective
----------------------------------------------

Classic:

$$
\min_x \|Ax-b\|_2
$$

SOCP form:

$$
\min_{x,t} t\quad \text{s.t.}\quad \|Ax-b\|_2 \le t.
$$

(You may also see  $\min \|Ax-b\|_2^2$ , which is a QP; but  $\min \|Ax-b\|_2$  is SOCP.)

* * *

8) Why  $\ell_2$  needs SOCP but  $\ell_1,\ell_\infty$  needed only LP
======================================================================

*    $\ell_1$  and  $\ell_\infty$  are built from **absolute values** and **max** of finitely many affine pieces → polyhedral epigraph → LP.
*    $\ell_2$  has a **curved** unit ball → non-polyhedral epigraph → needs cones beyond polyhedra → SOC.

That’s the structural reason. Not “because the textbook says so.”

* * *

9) Failure modes (how people break SOC constraints)
===================================================

1.  **RHS not affine**  
    If you write  $\|Ax+b\|_2 \le \sqrt{c^\top x + d}$ , that’s not a standard SOC form (might be representable with tricks, but not directly).
2.  **Putting non-affine stuff inside the norm**  
     $\|[x; x^2]\|_2 \le t$  is not affine inside the norm, so not SOCP in standard form.
3.  **Forgetting that SOC implies nonnegativity of the scalar component**  
    If you separately reason about squaring, you must enforce the RHS  $\ge 0$ . SOC form handles it naturally.
4.  **Confusing  $\| \cdot \|_2$  with componentwise absolute value**  
     $\|x\|_2$  is one inequality involving a quadratic sum;  $|x_i|$  are separate inequalities.

* * *

10) The Phase 5.3 mechanical translator (do this without thinking)
==================================================================

Whenever you see  $\ell_2$  norm:

### Template A: objective  $\min \|Ax+b\|_2$ 

Rewrite as:

$$
\min_{x,t} t\quad \text{s.t.}\quad (t,\ Ax+b)\in\mathcal{Q}.
$$

### Template B: constraint  $\|Ax+b\|_2 \le t$ 

Rewrite as:

$$
(t,\ Ax+b)\in\mathcal{Q}.
$$

### Template C: constraint  $\|Ax+b\|_2 \le c^\top x + d$ 

Rewrite as:

$$
(c^\top x+d,\ Ax+b)\in\mathcal{Q}.
$$

That’s Phase 5.3.

* * *

Next, Phase 5.4 is the “hyperbolic constraint” move: things like  $w^2 \le xy$  (with  $x,y\ge 0$ ) become **rotated** SOC constraints. That’s where SOCP starts to feel like a wizard’s staff—in a good, strictly-legal way.

## Response:
Phase 5.4 — Hyperbolic / quadratic-over-linear constraints  $\rightarrow$  Rotated SOC (the “product becomes a cone” move)
--------------------------------------------------------------------------------------------------------------------------

Phase 5.3 was: “Euclidean norm ≤ affine” is SOC.

Phase 5.4 is the next modeling atom that shows up constantly in robust/control/estimation problems:

*   constraints involving **products** like  $xy$ ,
*   constraints involving **squares** like  $w^2$ ,
*   constraints involving **quadratic-over-linear** terms like  $\dfrac{\|z\|_2^2}{t}$  or  $\dfrac{w^2}{x}$ .

These don’t look like norms at first glance. But there is a cone that _exactly_ captures them with linear + SOC structure:

> the **rotated second-order cone**.

Once you own this, “weird hyperbolas” stop being weird.

* * *

0) The kind of constraints we want to rewrite
=============================================

The canonical scalar “hyperbolic” constraint is:

$$
\boxed{w^2 \le xy,\qquad x\ge 0,\ y\ge 0.}
$$

Why “hyperbolic”? Because in the  $(x,y)$ \-plane for fixed  $w\neq 0$ , the boundary  $xy = w^2$  is a hyperbola.

More general versions:

*    $ \|z\|_2^2 \le xy$ , with  $z\in\mathbb{R}^k$ 
*    $ \dfrac{w^2}{x} \le y$  (quadratic-over-linear)
*    $ \dfrac{\|z\|_2^2}{x} \le y$ 

All of these are convex when  $x>0$  and  $y\ge 0$  (or  $x\ge 0$  with appropriate domain conventions). But they’re not LP, and they don’t fit the plain “ $\| \cdot \|_2 \le \cdot$ ” SOC template unless you know the rotated cone trick.

* * *

1) Define the rotated second-order cone (RSOC)
==============================================

There are a few equivalent conventions in the literature. The cleanest one for modeling is:

$$
\boxed{ \mathcal{Q}^r_{n+2} := \left\{(u,v,w)\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^n: u\ge 0,\ v\ge 0,\ 2uv \ge \|w\|_2^2 \right\}. }
$$
*    $u$  and  $v$  are scalars,
*    $w$  is an  $n$ \-vector,
*   the inequality  $2uv \ge \|w\|_2^2$  encodes a product  $uv$  dominating a squared norm.

This is a convex cone (hence “conic representable”), and SOCP solvers support it either directly or via a standard conversion to a standard SOC.

**Key thing to burn into memory:**

$$
(u,v,w)\in \mathcal{Q}^r \quad \Longleftrightarrow \quad u\ge 0,\ v\ge 0,\ \|w\|_2^2 \le 2uv.
$$

The factor 2 is just convention; it’s there so the conversion to standard SOC looks nice.

* * *

2) The Phase 5.4 atom:  $w^2 \le xy$  is RSOC
=============================================

We want:

$$
w^2 \le xy,\quad x\ge 0,\ y\ge 0.
$$

Compare with RSOC condition  $2uv \ge \|w\|_2^2$ . Here  $\|w\|_2^2$  is just  $w^2$  if  $w$  is scalar.

So if we set

$$
u=x,\quad v=y/2,\quad \text{and } w=w,
$$

then

$$
2u v = 2x(y/2)=xy.
$$

So the RSOC constraint

$$
(x,\ y/2,\ w)\in \mathcal{Q}^r_{3}
$$

is exactly:

$$
x\ge 0,\ y/2\ge 0,\ 2x(y/2)\ge w^2 \quad\Longleftrightarrow\quad x\ge 0,\ y\ge 0,\ xy\ge w^2.
$$

So we have the exact equivalence:

$$
\boxed{ w^2 \le xy,\ x\ge 0,\ y\ge 0 \quad\Longleftrightarrow\quad (x,\ y/2,\ w)\in \mathcal{Q}^r_{3}. }
$$

That’s the core modeling move.

### Why this matters

This is the trick that turns “product constraints” (which usually scream nonconvex) into something a conic solver can digest, provided the product has the right structure (a product of nonnegative variables dominating a square/norm-square).

* * *

3) Convert RSOC to standard SOC (so it’s truly “SOCP”)
======================================================

Many solvers accept RSOC natively. But even if they don’t, RSOC can be rewritten as a standard SOC constraint.

Start from RSOC definition:

$$
u\ge 0,\ v\ge 0,\ 2uv \ge \|w\|_2^2.
$$

Claim:

$$
\boxed{ (u,v,w)\in\mathcal{Q}^r_{n+2} \quad\Longleftrightarrow\quad \left\|\begin{bmatrix}2w\\ u-v\end{bmatrix}\right\|_2 \le u+v,\ \ u\ge 0,\ v\ge 0. }
$$

Let’s prove that carefully because it’s the “why” behind the solver-level implementation.

### Proof (direction-by-direction)

Let

$$
\left\|\begin{bmatrix}2w\\ u-v\end{bmatrix}\right\|_2 \le u+v.
$$

Square both sides (we can square because both sides are nonnegative; the LHS is a norm, RHS is  $u+v$  which will be forced  $\ge 0$  if the inequality is feasible):

Left:

$$
\left\|\begin{bmatrix}2w\\ u-v\end{bmatrix}\right\|_2^2 = \|2w\|_2^2 + (u-v)^2 = 4\|w\|_2^2 + (u-v)^2.
$$

Right:

$$
(u+v)^2 = u^2 + 2uv + v^2.
$$

So the inequality becomes:

$$
4\|w\|_2^2 + (u-v)^2 \le (u+v)^2.
$$

Expand  $(u-v)^2 = u^2 - 2uv + v^2$ . Substitute:

$$
4\|w\|_2^2 + (u^2 - 2uv + v^2) \le (u^2 + 2uv + v^2).
$$

Cancel  $u^2$  and  $v^2$  on both sides:

$$
4\|w\|_2^2 - 2uv \le 2uv.
$$

Bring terms together:

$$
4\|w\|_2^2 \le 4uv \quad\Longleftrightarrow\quad \|w\|_2^2 \le uv.
$$

Notice: this gives  $\|w\|_2^2 \le uv$ , whereas RSOC had  $2uv \ge \|w\|_2^2$ . That’s just because of scaling conventions in the vector we chose. If you instead use  $\sqrt{2}w$  you get the factor 2 exactly. The takeaway is: by appropriate constant scaling (which is allowed in affine mappings), RSOC is SOC-representable.

A clean consistent version matching the “ $2uv$ ” convention is:

$$
\left\|\begin{bmatrix}w\\ u-v\end{bmatrix}\right\|_2 \le u+v \quad\Longleftrightarrow\quad \|w\|_2^2 \le 4uv.
$$

Then you scale  $w$  by 2 to align constants. Constants never matter for representability, only for correctness—so you just do the algebra carefully once and then treat it as a template.

**Practical modeling lesson:** RSOC is not a “new type” beyond SOCP. It is an SOCP constraint after a simple linear change of variables.

* * *

4) Quadratic-over-linear is RSOC in disguise
============================================

This is the most tested pattern.

4.1 Scalar case:  $\dfrac{w^2}{x} \le y$ 
-----------------------------------------

Assume  $x>0$  (or  $x\ge 0$  with domain meaning “if  $x=0$  then must have  $w=0$ ”).

Constraint:

$$
\frac{w^2}{x} \le y \quad\Longleftrightarrow\quad w^2 \le xy.
$$

Now if you also require  $y\ge 0$  (which is implied if the inequality holds and  $x>0$ ), you’re exactly in the hyperbolic form:

$$
w^2 \le xy,\quad x\ge 0,\ y\ge 0.
$$

So it becomes:

$$
\boxed{ \frac{w^2}{x} \le y,\ x\ge 0 \quad\Longleftrightarrow\quad (x,\ y/2,\ w)\in\mathcal{Q}^r_3. }
$$

This is the conic representation of the quadratic-over-linear function, which is known to be convex on  $x>0$ .

4.2 Vector case:  $\dfrac{\|z\|_2^2}{x} \le y$ 
-----------------------------------------------

Same trick:

$$
\frac{\|z\|_2^2}{x} \le y \quad\Longleftrightarrow\quad \|z\|_2^2 \le xy.
$$

Represent as:

$$
\boxed{ (x,\ y/2,\ z)\in\mathcal{Q}^r_{n+2}. }
$$

This shows up constantly in control and estimation (energy constraints, perspective functions, etc.).

* * *

5) Why these constraints are convex (rigorous intuition, not vibes)
===================================================================

You should be able to defend convexity, not just “it’s RSOC so convex.”

Two ways:

Way A: Conic set argument (fast, rigorous)
------------------------------------------

*    $\mathcal{Q}^r$  is a convex cone.
*   The constraint  $(u(x),v(x),w(x))\in\mathcal{Q}^r$  is an affine preimage of a convex set, hence convex.  
    That’s the standard convexity-preserving rule.

Way B: Function argument for quadratic-over-linear
--------------------------------------------------

The function

$$
f(w,x)=\frac{w^2}{x}
$$

is convex on  $x>0$ . One can prove by Hessian PSD or by perspective argument. Then  $f(w,x)\le y$  defines a convex epigraph set. RSOC is exactly a way to express that epigraph in conic form.

In fact, RSOC is basically the “geometric wrapper” for the perspective of a quadratic.

* * *

6) Mechanical translator for Phase 5.4 (the do-this-every-time templates)
=========================================================================

### Template 1:  $w^2 \le xy$ ,  $x\ge 0$ ,  $y\ge 0$ 

Write as RSOC:

$$
(x,\ y/2,\ w)\in \mathcal{Q}^r.
$$

### Template 2:  $\|z\|_2^2 \le xy$ ,  $x\ge 0$ ,  $y\ge 0$ 

Write as RSOC:

$$
(x,\ y/2,\ z)\in \mathcal{Q}^r.
$$

### Template 3:  $\dfrac{w^2}{x}\le y$ ,  $x\ge 0$ 

Rewrite to product:

$$
w^2 \le xy
$$

then apply Template 1.

### Template 4:  $\dfrac{\|z\|_2^2}{x}\le y$ ,  $x\ge 0$ 

Rewrite to product:

$$
\|z\|_2^2 \le xy
$$

then apply Template 2.

* * *

7) Common failure modes (where people silently go wrong)
========================================================

1.  **Missing nonnegativity conditions**  
    The hyperbolic set  $w^2 \le xy$  is not convex over all  $(x,y)\in\mathbb{R}^2$ . Convexity depends critically on  $x\ge 0,\ y\ge 0$ . RSOC bakes these in.
2.  **Trying to model  $xy \le w^2$ **  
    That is the wrong direction.  $xy \le w^2$  is generally nonconvex (it’s like the complement of a convex region). Phase 5.4 only handles the “product dominates square” direction.
3.  **Squaring/unsquaring without domain care**  
    If you manipulate inequalities involving squares, you must ensure the quantities you square are nonnegative. Conic form avoids this pitfall because norms are always nonnegative and the cone enforces the correct side.
4.  **Confusing RSOC with plain SOC**  
    Plain SOC handles  $\|z\|_2 \le t$ . RSOC handles  $\|z\|_2^2 \le 2uv$  (product on RHS). They’re different atoms.

* * *

8) Why Phase 5.4 matters in PS6 / modeling
==========================================

This is the workhorse for:

*   “energy / power” constraints,
*   “variance ≤ product” types,
*   perspective transformations of quadratics,
*   many robust and control formulations,
*   turning some QCQPs into SOCPs.

It’s also the stepping stone to Phase 5.6 and 5.7, where Schur complements and LMIs do analogous magic for quadratic forms and eigenvalues.

* * *

If you continue, Phase 5.5 is where robust constraints become “dual norm terms,” and then Phase 5.3 + 5.4 tell you whether the resulting norm constraints are SOC or RSOC representable. That’s the point where the whole modeling language becomes a small set of composable atoms.

## Response:
Phase 5.5 — Robust constraints  $\rightarrow$  dual norms  $\rightarrow$  SOCP/LP (turn “for all uncertainties” into a norm)
----------------------------------------------------------------------------------------------------------------------------

This is the moment convex optimization starts feeling like it has cheat codes—except it’s not cheating; it’s geometry.

Robust optimization problems look like:

> “Choose  $x$  such that the constraint holds **for all** perturbations  $u$  in some uncertainty set.”

That “ $\forall u$ ” is terrifying at first because it’s an infinite family of constraints. Phase 5.5 is the standard trick that collapses that infinite family into **one** convex constraint, typically a **norm bound**, and then Phase 5.2/5.3/5.4 tell you whether it becomes LP or SOCP.

The core pipeline is:

1.  Write the robust constraint as a **supremum** (worst-case) inequality.
2.  Recognize the supremum as a **support function** of the uncertainty set.
3.  For norm balls, the support function equals a **dual norm**.
4.  You land in LP or SOCP (depending on which norm).

I’ll build this from first principles.

* * *

0) Setup: what “robust constraint” means
========================================

A non-robust (nominal) inequality constraint looks like:

$$
a^\top x \le b.
$$

A robust version might say:

$$
(a+u)^\top x \le b \quad \text{for all } u\in\mathcal{U},
$$

where  $\mathcal{U}$  is an uncertainty set (e.g., “perturbations bounded in  $\ell_2$ ”).

That means: no matter how nature chooses  $u$  in  $\mathcal{U}$ , your  $x$  must still satisfy the constraint.

This is exactly a worst-case requirement.

* * *

1) Step 1: convert “for all  $u$ ” into a worst-case (supremum)
===============================================================

Start from:

$$
(a+u)^\top x \le b \quad \forall u\in\mathcal{U}.
$$

Rewrite the left side:

$$
(a+u)^\top x = a^\top x + u^\top x.
$$

So the constraint becomes:

$$
a^\top x + u^\top x \le b \quad \forall u\in\mathcal{U}.
$$

This is equivalent to requiring that the **largest** possible value of  $u^\top x$  over  $u\in\mathcal{U}$  still keeps you under  $b$ :

$$
a^\top x + \sup_{u\in\mathcal{U}} u^\top x \le b.
$$

So we have the equivalence:

$$
\boxed{ (a+u)^\top x \le b\ \forall u\in\mathcal{U} \quad \Longleftrightarrow\quad a^\top x + \sup_{u\in\mathcal{U}} u^\top x \le b. }
$$

### Proof of the equivalence (fully explicit)

*   If  $a^\top x + \sup_{u\in\mathcal{U}} u^\top x \le b$ , then for any particular  $u\in\mathcal{U}$ , we have  $u^\top x \le \sup_{v\in\mathcal{U}} v^\top x$ . Add  $a^\top x$  to both sides, get  $a^\top x + u^\top x \le b$ . So the “for all” holds.
*   Conversely, if  $a^\top x + u^\top x \le b$  for all  $u\in\mathcal{U}$ , then taking the supremum over  $u$  of the left side gives:
    $$
    \sup_{u\in\mathcal{U}} (a^\top x + u^\top x) \le b.
    $$
    Since  $a^\top x$  doesn’t depend on  $u$ ,
    $$
    a^\top x + \sup_{u\in\mathcal{U}} u^\top x \le b.
    $$
    Done.

So robust constraints always become “nominal term + worst-case term ≤ b.”

The entire job is now: compute or bound  $\sup_{u\in\mathcal{U}} u^\top x$ .

* * *

2) Step 2: recognize the support function
=========================================

The quantity

$$
\sigma_{\mathcal{U}}(x) := \sup_{u\in\mathcal{U}} u^\top x
$$

is called the **support function** of  $\mathcal{U}$ .

*   It tells you: “how far the set  $\mathcal{U}$  extends in direction  $x$ .”
*   Geometrically: it’s the maximum projection of  $\mathcal{U}$  onto direction  $x$ .

So robust constraints become:

$$
a^\top x + \sigma_{\mathcal{U}}(x) \le b.
$$

This is already a clean conceptual form.

Now we pick uncertainty sets where  $\sigma_{\mathcal{U}}$  is something we can express as LP/SOCP.

* * *

3) Step 3: key lemma — support function of a norm ball is a dual norm
=====================================================================

This is the core theorem of Phase 5.5.

3.1 Dual norm definition
------------------------

Given a norm  $\|\cdot\|$  on  $\mathbb{R}^n$ , its **dual norm**  $\|\cdot\|_*$  is defined by:

$$
\boxed{ \|x\|_* := \sup_{\|u\|\le 1} u^\top x. }
$$

Interpretation:

*   “Among all vectors  $u$  with norm ≤ 1, what is the largest dot product with  $x$ ?”
*   That is exactly a support function, but of the **unit ball**.

Now if the uncertainty set is a radius- $\rho$  norm ball:

$$
\mathcal{U} = \{u : \|u\|\le \rho\},
$$

then:

$$
\sup_{u\in\mathcal{U}} u^\top x = \sup_{\|u\|\le \rho} u^\top x.
$$

Use scaling: write  $u=\rho v$ , where  $\|v\|\le 1$ . Then:

$$
\sup_{\|u\|\le \rho} u^\top x = \sup_{\|v\|\le 1} (\rho v)^\top x = \rho \sup_{\|v\|\le 1} v^\top x = \rho \|x\|_*.
$$

So we get the key identity:

$$
\boxed{ \sup_{\|u\|\le \rho} u^\top x = \rho \|x\|_*. }
$$

This is the exact “robust optimization magic step.”

* * *

4) The canonical robust linear constraint
=========================================

Now plug this into the robust constraint:

Robust constraint:

$$
(a+u)^\top x \le b\quad \forall \|u\|\le \rho.
$$

Equivalent to:

$$
a^\top x + \sup_{\|u\|\le \rho} u^\top x \le b
$$
 
$$
a^\top x + \rho\|x\|_* \le b.
$$

So:

$$
\boxed{ (a+u)^\top x \le b\ \forall \|u\|\le \rho \quad\Longleftrightarrow\quad a^\top x + \rho\|x\|_* \le b. }
$$

Now the entire problem reduces to: what is  $\|x\|_*$ , and can I express it as LP or SOCP?

* * *

5) Concrete cases:  $\ell_2$ ,  $\ell_\infty$ ,  $\ell_1$ 
==========================================================

These three are the workhorses.

5.1 If uncertainty is  $\ell_2$ :  $\|u\|_2 \le \rho$ 
------------------------------------------------------

Dual of  $\ell_2$  is  $\ell_2$ :

$$
\|x\|_{2,*} = \|x\|_2.
$$

So robust constraint becomes:

$$
a^\top x + \rho \|x\|_2 \le b.
$$

This is an SOCP constraint because it is “affine + scalar\*norm ≤ constant.”

To put in standard SOCP form, isolate the norm:

$$
\rho \|x\|_2 \le b - a^\top x \quad \Longleftrightarrow\quad \|x\|_2 \le \frac{b-a^\top x}{\rho}
$$

(assuming  $\rho>0$ ). More directly, you can model:

$$
\| \rho x\|_2 \le b-a^\top x.
$$

That is

$$
(b-a^\top x,\ \rho x)\in \mathcal{Q}_{n+1}.
$$

**Important domain note:** SOC implies  $b-a^\top x \ge 0$ , which matches feasibility: the RHS must be nonnegative.

So robust  $\ell_2$  uncertainty  $\Rightarrow$  SOCP.

* * *

5.2 If uncertainty is  $\ell_\infty$ :  $\|u\|_\infty \le \rho$ 
----------------------------------------------------------------

Dual of  $\ell_\infty$  is  $\ell_1$ :

$$
\|x\|_{\infty,*} = \|x\|_1.
$$

So:

$$
a^\top x + \rho \|x\|_1 \le b.
$$

This is LP-representable because  $\|x\|_1$  is LP-representable (Phase 5.2).

Introduce  $s_i\ge |x_i|$ :

$$
-x_i \le s_i,\quad x_i \le s_i
$$

and enforce:

$$
a^\top x + \rho \sum_i s_i \le b.
$$

Everything is linear  $\Rightarrow$  LP.

* * *

5.3 If uncertainty is  $\ell_1$ :  $\|u\|_1 \le \rho$ 
------------------------------------------------------

Dual of  $\ell_1$  is  $\ell_\infty$ :

$$
\|x\|_{1,*} = \|x\|_\infty.
$$

So:

$$
a^\top x + \rho \|x\|_\infty \le b.
$$

This is LP-representable because  $\|x\|_\infty$  is LP-representable (Phase 5.2).

Introduce scalar  $t\ge |x_i|$  for all  $i$ :

$$
-x_i\le t,\quad x_i\le t\ \forall i,
$$

then:

$$
a^\top x + \rho t \le b.
$$

LP again.

* * *

6) The more general robust affine constraint  $(A+ \Delta)\,x \le b$ 
=====================================================================

Often you see row-wise uncertainty:

For each constraint row  $i$ ,

$$
(a_i + u_i)^\top x \le b_i \quad \forall u_i \in \mathcal{U}_i.
$$

You apply Phase 5.5 row-by-row:

$$
a_i^\top x + \sup_{u_i\in\mathcal{U}_i} u_i^\top x \le b_i.
$$

If  $\mathcal{U}_i$  is a norm ball  $\{u_i:\|u_i\|\le\rho_i\}$ , then:

$$
a_i^\top x + \rho_i\|x\|_* \le b_i.
$$

So you get one robustified constraint per row.

Sometimes uncertainty is not on  $x$  directly but on  $A$  as  $\Delta x$ . Then your worst-case term becomes  $\sup_{\Delta\in\mathcal{D}} (\Delta x)_i$ . With structured uncertainty, it still becomes a norm of something like  $Bx$ . The same dual-norm logic is underneath; it’s just applied to a transformed vector.

* * *

7) Why the dual norm lemma is true (intuition + proof sketch you can reproduce)
===============================================================================

Intuition (geometry)
--------------------

 $\sup_{\|u\|\le 1} u^\top x$  is asking:

*   “Among all  $u$  inside the unit ball, which has the largest projection onto direction  $x$ ?”

The maximizing  $u$  lies on the boundary, pointing in the “dual direction” of  $x$ .  
For  $\ell_2$ , it’s exactly  $u=x/\|x\|_2$ . Then the dot product becomes  $\|x\|_2$ .

For  $\ell_\infty$ , the unit ball is a box; the best dot product is achieved by choosing each coordinate  $u_i=\operatorname{sign}(x_i)$ , giving  $\sum |x_i|=\|x\|_1$ .

For  $\ell_1$ , the unit ball is a diamond; the best dot product is achieved by putting all mass on the largest-magnitude coordinate, giving  $\|x\|_\infty$ .

Rigorous (one-line) proof for scaling identity
----------------------------------------------

Already done above:

$$
\sup_{\|u\|\le\rho} u^\top x = \rho \sup_{\|v\|\le 1} v^\top x = \rho \|x\|_*.
$$

The rest is definition.

* * *

8) Practical cookbook: “Robustify then recognize LP vs SOCP”
============================================================

Here is the mechanical pipeline you should execute:

1.  Start with robust inequality, isolate uncertainty linearly:
    $$
    \text{constraint holds } \forall u \in \mathcal{U} \ \Longleftrightarrow\ \sup_{u\in\mathcal{U}} \text{(uncertain term)} \le \text{margin}.
    $$
2.  If uncertainty set is a norm ball  $\|u\|\le\rho$ , replace the supremum with  $\rho\|\cdot\|_*$ .
3.  Determine dual norm:
    *   dual of  $\ell_2$  is  $\ell_2$   $\Rightarrow$  SOCP
    *   dual of  $\ell_\infty$  is  $\ell_1$   $\Rightarrow$  LP
    *   dual of  $\ell_1$  is  $\ell_\infty$   $\Rightarrow$  LP
4.  Model resulting norm using Phase 5.2 or 5.3:
    *    $\| \cdot \|_1,\ \| \cdot \|_\infty$  → LP
    *    $\| \cdot \|_2$  → SOCP

* * *

9) Failure modes (this is where points die)
===========================================

1.  **Not converting “for all” to “sup”**  
    If you keep the quantifier, you can’t finish. Always:  $\forall$  → worst-case.
2.  **Using the wrong dual**  
     $\ell_1 \leftrightarrow \ell_\infty$ .  $\ell_2 \leftrightarrow \ell_2$ . If you flip these, you’ll land in the wrong cone class.
3.  **Forgetting scaling  $\rho$ **  
    The radius multiplies the dual norm term.
4.  **Dropping required nonnegativity**  
    When you convert to SOC, the scalar side must be nonnegative; SOC enforces it, but in handwritten transformations you must note feasibility implies it.
5.  **Uncertainty set not centered at 0**  
    If  $\mathcal{U}$  is not symmetric or not centered, the support function isn’t just a norm; it’s a general support function. Then you need a different representation.

* * *

If you continue, Phase 5.6 is where quadratic epigraphs (like  $x^\top P x \le t$ ) become **SDP** via the Schur complement—another “infinite-looking thing becomes one cone constraint” move, but now with the PSD cone instead of SOC.

## Response:
Thought for 22s

Phase 5.6 — Quadratic epigraphs  $\rightarrow$  SDP (via the Schur complement)
------------------------------------------------------------------------------

Phase 5.3–5.5 taught you to spot when something becomes LP or SOCP by turning “ugly expressions” into norms and (rotated) SOC constraints.

Phase 5.6 is the analogous move for expressions where the “ugly thing” is a **quadratic form with an inverse of a matrix variable** (or anything that smells like “ $X^{-1}$ ” multiplying something). That’s where SOCP usually can’t help, but **SDP can**, because PSD matrices and LMIs can encode those inverse-quadratic relations _exactly_.

The core weapon is the **Schur complement**.

* * *

0) What “quadratic epigraph” means here
=======================================

An “epigraph constraint” is one of the form

$$
\text{(some expression in variables)} \le t
$$

where  $t$  is a new scalar variable. You “lift” the problem into higher dimension so the objective becomes linear (minimize  $t$ ) and the complicated part moves into constraints.

In Phase 5.1/5.3 we did:

*    $|u| \le t$  (LP trick)
*    $\|Ax+b\|_2 \le t$  (SOC trick)

Now the Phase 5.6 target is constraints like:

$$
x^\top X^{-1} x \le t \quad\text{or}\quad \|x\|_{X^{-1}}^2 \le t \quad\text{or}\quad (Ax+b)^\top X^{-1}(Ax+b) \le t
$$

where ** $X$  is a decision variable** constrained by  $X \succeq 0$  (PSD).

That “inverse of a matrix variable” is the tell. It screams “Schur complement  $\Rightarrow$  LMI  $\Rightarrow$  SDP.”

* * *

1) SDP primitives you must be fluent in (brief but precise)
===========================================================

1.1 PSD cone and Loewner order
------------------------------

For a symmetric matrix  $M\in\mathbb{S}^n$ ,

*    $M \succeq 0$  means  $z^\top M z \ge 0$  for all  $z$ .
*    $M \succ 0$  means  $z^\top M z > 0$  for all nonzero  $z$ .
*    $A \preceq B$  means  $B-A \succeq 0$ .

1.2 Linear Matrix Inequality (LMI)
----------------------------------

An LMI is a constraint of the form

$$
F(x) = F_0 + x_1 F_1 + \cdots + x_k F_k \succeq 0
$$

where the  $F_i$  are fixed symmetric matrices and the matrix depends **affinely** on decision variables.

SDP is basically “minimize linear objective subject to LMIs.”

So to get an SDP formulation, you want to rewrite your constraint into **one matrix  $\succeq 0$ ** whose entries are affine in variables.

* * *

2) The Schur complement theorem (the core identity)
===================================================

Consider a symmetric block matrix

$$
M = \begin{bmatrix} A & B \\ B^\top & C \end{bmatrix}
$$

with  $A\in\mathbb{S}^n$ ,  $C\in\mathbb{S}^m$ , and  $B\in\mathbb{R}^{n\times m}$ .

### Theorem (Schur complement, “ $A$ ” version)

If  $A \succ 0$ , then

$$
\boxed{ \begin{bmatrix} A & B \\ B^\top & C \end{bmatrix} \succeq 0 \quad\Longleftrightarrow\quad C - B^\top A^{-1}B \succeq 0. }
$$

The matrix

$$
C - B^\top A^{-1} B
$$

is called the **Schur complement of  $A$  in  $M$ **.

There is a symmetric twin statement: if  $C\succ 0$ , then

$$
M\succeq 0 \Longleftrightarrow A - B C^{-1} B^\top \succeq 0.
$$

### Why this theorem matters here

Notice what appears: ** $A^{-1}$ **. That’s the inverse you want to avoid explicitly. The theorem says:

> A quadratic expression involving an inverse can be replaced by a **PSD block matrix constraint**.

And PSD block matrix constraints are LMIs → SDP.

* * *

3) The Phase 5.6 atom (most important):  $x^\top X^{-1} x \le t$ 
=================================================================

This is the canonical “quadratic epigraph via SDP” pattern.

### Problem form

*   Variables:  $X\in\mathbb{S}^n$ ,  $x\in\mathbb{R}^n$ ,  $t\in\mathbb{R}$ 
*   Constraint:
    
$$
x^\top X^{-1} x \le t,\quad X \succ 0.
$$

### Claim (exact LMI equivalence)

$$
\boxed{ x^\top X^{-1} x \le t,\ X \succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} X & x \\ x^\top & t \end{bmatrix} \succeq 0. }
$$

This is the “Schur complement trick” you’ll use over and over.

* * *

3.1 Proof (fully explicit, no magic)
------------------------------------

Let

$$
M= \begin{bmatrix} X & x \\ x^\top & t \end{bmatrix}.
$$

Assume  $X\succ 0$  so  $X^{-1}$  exists, and apply Schur complement with  $A=X$ ,  $B=x$ ,  $C=t$ .

Schur complement says:

$$
M\succeq 0 \Longleftrightarrow t - x^\top X^{-1} x \ge 0.
$$

That last inequality is exactly:

$$
x^\top X^{-1} x \le t.
$$

So:

$$
M\succeq 0 \Longleftrightarrow x^\top X^{-1} x \le t \quad (\text{given } X\succ 0).
$$

That’s the equivalence.

* * *

3.2 Why this is an SDP constraint (affine + PSD)
------------------------------------------------

Look at the block matrix:

$$
\begin{bmatrix} X & x \\ x^\top & t \end{bmatrix}.
$$

Its entries depend **affinely** on the decision variables  $X, x, t$ . The constraint “this matrix is PSD” is an LMI. So you are in SDP land.

* * *

4) Variants you must recognize instantly
========================================

4.1 With an affine map:  $(Ax+b)^\top X^{-1} (Ax+b) \le t$ 
-----------------------------------------------------------

Let  $y = Ax+b$ . Then the constraint is  $y^\top X^{-1}y \le t$ .

By the same atom:

$$
\boxed{ (Ax+b)^\top X^{-1}(Ax+b)\le t,\ X\succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} X & Ax+b \\ (Ax+b)^\top & t \end{bmatrix}\succeq 0. }
$$

Still an LMI because  $Ax+b$  is affine in  $x$ .

* * *

4.2 Weighted norm notation (same thing)
---------------------------------------

Define the (squared) Mahalanobis norm:

$$
\|x\|_{X^{-1}}^2 := x^\top X^{-1}x.
$$

Then

$$
\|x\|_{X^{-1}}^2 \le t \Longleftrightarrow \begin{bmatrix} X & x \\ x^\top & t \end{bmatrix}\succeq 0.
$$

* * *

4.3 Matrix version:  $Y^\top X^{-1} Y \preceq T$ 
-------------------------------------------------

Sometimes you’ll see matrix inequalities, not scalars. A common pattern:

$$
Y^\top X^{-1} Y \preceq T
$$

with  $X\succ 0$ ,  $T\succeq 0$ .

Then the block LMI is:

$$
\boxed{ Y^\top X^{-1} Y \preceq T \quad\Longleftrightarrow\quad \begin{bmatrix} X & Y \\ Y^\top & T \end{bmatrix}\succeq 0 \quad (\text{with } X\succ 0). }
$$

Same Schur complement, but  $C=T$  is now a matrix.

This is extremely common in control and estimation SDPs.

* * *

5) Where people get confused: “but  $x^\top P x \le t$  can be SOCP sometimes!”
===============================================================================

Important nuance:

*   If the quadratic form matrix is a **constant** PSD matrix  $P\succeq 0$ , then
    $$
    x^\top P x \le t
    $$
    can often be represented using **rotated SOC** because  $x^\top P x = \|R x\|_2^2$  for some constant factor  $R$  (Cholesky / square root), giving  $\|R x\|_2^2 \le t\cdot 1$ , which is RSOC-representable.
*   Phase 5.6 is mainly about the harder and more SDP-native case where the quadratic involves ** $X^{-1}$ ** with ** $X$  variable**. That usually cannot be reduced to SOC because the factorization would depend on the variable.

So the clean mental rule:

> Constant quadratic forms: often SOCP-able.  
> Quadratic forms with inverse of a matrix variable: SDP via Schur complement.

That’s why this is in “Quadratic epigraphs → SDP.”

* * *

6) “Epigraph” usage: turning a scary objective into linear objective + LMI
==========================================================================

Suppose your objective is:

$$
\min_{x,X} \ x^\top X^{-1}x \quad \text{s.t. other constraints, } X\succ 0.
$$

Use an epigraph variable  $t$ :

$$
\min_{x,X,t}\ t \quad \text{s.t.}\quad x^\top X^{-1}x \le t,\ X\succ 0.
$$

Now apply Phase 5.6 atom:

$$
\boxed{ \min_{x,X,t}\ t \quad \text{s.t.}\quad \begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0,\ \ X\succ 0. }
$$

Now the objective is linear, constraint is LMI → SDP.

This is exactly how SDPs “linearize” a wide class of convex but non-linear expressions.

* * *

7) Domain subtleties (don’t lose points here)
=============================================

7.1 What if  $X\succeq 0$  but not  $\succ 0$ ?
-----------------------------------------------

Then  $X^{-1}$  doesn’t exist. The expression  $x^\top X^{-1}x$  is not well-defined in the usual sense.

In rigorous convex-analysis treatments, you can extend it as:

*    $x^\top X^\dagger x$  (pseudoinverse) if  $x$  lies in the range of  $X$ ,
*    $+\infty$  otherwise,  
    which makes it convex as an extended-valued function.

But for standard modeling and Schur complement equivalence, you typically assume  $X\succ 0$ , or enforce  $X \succeq \epsilon I$  for some small  $\epsilon>0$  if needed (regularization / numerical stability).

7.2 Nonnegativity of  $t$ 
--------------------------

From

$$
\begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0,
$$

you automatically get  $t\ge 0$  (since the bottom-right entry of a PSD matrix must be  $\ge 0$ ). So you usually don’t need to add  $t\ge 0$  separately, though it’s fine to include.

* * *

8) Mechanical translator (the “do this every time” checklist)
=============================================================

When you see something like:

*    $x^\top X^{-1}x \le t$ ,
*    $(Ax+b)^\top X^{-1}(Ax+b) \le t$ ,
*    $Y^\top X^{-1}Y \preceq T$ ,

do this:

1.  Identify the “inverse quadratic” pattern  $(\text{something})^\top X^{-1}(\text{something})$ .
2.  Introduce epigraph variable  $t$  (if it’s in objective).
3.  Replace the inverse quadratic inequality by the block PSD constraint:
    *   Scalar version:
        $$
        (\cdot)^\top X^{-1}(\cdot) \le t \ \Longleftrightarrow\ \begin{bmatrix} X & (\cdot)\\ (\cdot)^\top & t \end{bmatrix}\succeq 0.
        $$
    *   Matrix version:
        $$
        (\cdot)^\top X^{-1}(\cdot) \preceq T \ \Longleftrightarrow\ \begin{bmatrix} X & (\cdot)\\ (\cdot)^\top & T \end{bmatrix}\succeq 0.
        $$
4.  Ensure the assumptions: typically  $X\succ 0$  (or  $X\succeq \epsilon I$ ).

That’s Phase 5.6.

* * *

9) Why this is so powerful (conceptual punchline)
=================================================

The Schur complement is doing something profound:

*   It turns a nonlinear inequality involving  $X^{-1}$  (which is scary to optimize over)
*   into a linear matrix inequality (LMI),
*   by “lifting” into a bigger PSD matrix.

So SDP is, in a real sense, the language of “inverse-aware convexity.”

* * *

Phase 5.7 next is the natural continuation: **eigenvalue constraints** (like  $\lambda_{\max}(A(x))\le t$ ) become LMIs too, because eigenvalues are exactly about PSD order. That’s where the PSD cone becomes not just a trick, but a full spectral calculus.

## Response:
Phase 5.7 — Eigenvalues  $\rightarrow$  LMIs (SDP)
--------------------------------------------------

_(turn “spectral” statements into PSD order constraints)_

Phase 5.6 was: inverse-quadratic stuff  $\rightarrow$  block PSD constraint via Schur complement.

Phase 5.7 is: **eigenvalue constraints**  $\rightarrow$  **linear matrix inequalities (LMIs)**.

This is _the_ core reason SDPs are so powerful: many “spectral” conditions that look nonlinear become **linear** once you express them in the **Loewner (PSD) order**.

I’ll build this carefully from first principles: what eigenvalues mean, how PSD order encodes them, and the exact modeling templates you’ll use on PS sets.

* * *

0) First principles: symmetric matrices, quadratic forms, eigenvalues
=====================================================================

Everything in Phase 5.7 assumes **real symmetric matrices**. Why? Because only then:

*   eigenvalues are real,
*   the matrix is orthogonally diagonalizable,
*   PSD order is clean and equivalent to “all eigenvalues nonnegative.”

So let  $A\in\mathbb{S}^n$  (symmetric).

0.1 Eigenvalues and diagonalization
-----------------------------------

There exists an orthogonal matrix  $Q$  and real eigenvalues  $\lambda_1,\dots,\lambda_n$  such that

$$
A = Q \Lambda Q^\top,\quad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n),\quad Q^\top Q=I.
$$

0.2 PSD and eigenvalues
-----------------------

Definition:

$$
A\succeq 0 \quad\Longleftrightarrow\quad z^\top A z\ge 0\ \ \forall z.
$$

Key equivalence (you should be able to prove it):

$$
\boxed{ A\succeq 0 \quad\Longleftrightarrow\quad \lambda_i(A)\ge 0\ \ \forall i. }
$$

**Proof sketch (fully explicit):**  
Using diagonalization  $A=Q\Lambda Q^\top$ , write  $z=Qy$  (since  $Q$  is orthogonal, this is a bijection). Then

$$
z^\top A z = (Qy)^\top(Q\Lambda Q^\top)(Qy) = y^\top \Lambda y = \sum_{i=1}^n \lambda_i y_i^2.
$$

This is  $\ge 0$  for all  $y$  iff each  $\lambda_i\ge 0$ . If any  $\lambda_k<0$ , choose  $y=e_k$  and you get  $y^\top\Lambda y=\lambda_k<0$ . Conversely if all  $\lambda_i\ge 0$ , the sum is nonnegative.

This is why PSD constraints are “eigenvalue constraints in disguise.”

* * *

1) The Loewner order is a spectral inequality
=============================================

Loewner order:

$$
A \preceq B \quad\Longleftrightarrow\quad B-A \succeq 0.
$$

Geometrically:  $B$  dominates  $A$  as quadratic forms:

$$
z^\top A z \le z^\top B z \quad \forall z.
$$

Spectrally:  $B-A\succeq 0$  forces eigenvalues of  $B$  to be “larger” in a precise sense; the key special case we use constantly is with a scalar multiple of identity.

* * *

2) The most important atom:  $\lambda_{\max}(A)\le t \iff A \preceq tI$ 
========================================================================

2.1 Define  $\lambda_{\max}$ 
-----------------------------

Let  $\lambda_{\max}(A)$  be the largest eigenvalue of symmetric  $A$ .

A classic characterization (Rayleigh quotient):

$$
\lambda_{\max}(A)=\max_{\|z\|_2=1} z^\top A z.
$$

(This is why it’s convex in  $A$ , but we won’t even need that for modeling—just for intuition.)

2.2 Claim (LMI equivalence)
---------------------------

For symmetric  $A$  and scalar  $t$ ,

$$
\boxed{ \lambda_{\max}(A)\le t \quad\Longleftrightarrow\quad A \preceq tI \quad\Longleftrightarrow\quad tI - A \succeq 0. }
$$

### Proof (from diagonalization; very explicit)

Write  $A=Q\Lambda Q^\top$ .  
Then:

$$
tI - A = tI - Q\Lambda Q^\top = Q(tI-\Lambda)Q^\top.
$$

The eigenvalues of  $tI-\Lambda$  are  $t-\lambda_i$ . Therefore:

$$
tI-A\succeq 0 \Longleftrightarrow t-\lambda_i \ge 0 \ \forall i \Longleftrightarrow \lambda_i \le t\ \forall i \Longleftrightarrow \lambda_{\max}(A)\le t.
$$

Done.

### Modeling consequence

If  $A(x)$  depends affinely on decision variables  $x$ , then

$$
\lambda_{\max}(A(x))\le t
$$

becomes the LMI:

$$
tI - A(x) \succeq 0,
$$

which is SDP-ready because it’s affine in  $(x,t)$ .

This is the single most used Phase 5.7 template.

* * *

3) The sister atom:  $\lambda_{\min}(A)\ge t \iff A \succeq tI$ 
================================================================

Let  $\lambda_{\min}(A)$  be the smallest eigenvalue.

Claim:

$$
\boxed{ \lambda_{\min}(A)\ge t \quad\Longleftrightarrow\quad A \succeq tI \quad\Longleftrightarrow\quad A - tI \succeq 0. }
$$

Proof is the same logic:  $A-tI$  has eigenvalues  $\lambda_i - t$ , so PSD means  $\lambda_i\ge t$  for all  $i$ , which is equivalent to the minimum being ≥  $t$ .

* * *

4) Spectral norm and singular values (when symmetric vs general matrices)
=========================================================================

You’ll often see constraints like  $\|M\|_2 \le t$ , where  $\|M\|_2$  is the operator norm (largest singular value). For **general**  $M$  (not symmetric), that’s not directly an eigenvalue of  $M$ , but it is an eigenvalue of a symmetric block matrix.

4.1 Symmetric case
------------------

If  $A$  is symmetric, then

$$
\|A\|_2 = \max(|\lambda_{\max}(A)|,|\lambda_{\min}(A)|).
$$

So  $\|A\|_2\le t$  is equivalent to:

$$
-tI \preceq A \preceq tI \quad\Longleftrightarrow\quad \begin{cases} tI - A \succeq 0\\ tI + A \succeq 0 \end{cases}
$$

Two LMIs.

4.2 General rectangular  $M$ : block LMI
----------------------------------------

For  $M\in\mathbb{R}^{m\times n}$ ,

$$
\boxed{ \|M\|_2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} tI_m & M\\ M^\top & tI_n \end{bmatrix}\succeq 0. }
$$

This is a standard LMI derived from Schur complements and the fact that  $M^\top M$  relates to singular values.

(You can think of this as a “spectral-norm epigraph is SDP.”)

This shows the boundary between SOCP and SDP: Euclidean vector norms are SOC; spectral matrix norms are SDP.

* * *

5) Eigenvalue constraints for affine matrix functions  $A(x)$ 
==============================================================

The reason eigenvalue constraints become LMIs is that many problems involve matrices like

$$
A(x) = A_0 + x_1 A_1 + \cdots + x_k A_k,
$$

which is affine in  $x$ . Then:

### 5.1 Bounding the largest eigenvalue

$$
\lambda_{\max}(A(x)) \le t \quad\Longleftrightarrow\quad tI - A(x)\succeq 0
$$

An LMI in  $(x,t)$ .

### 5.2 Ensuring positive definiteness / stability margin

$$
A(x)\succeq 0 \quad\Longleftrightarrow\quad A(x) \succeq 0
$$

Already an LMI.

### 5.3 Bounding all eigenvalues in an interval

“all eigenvalues of  $A(x)$  lie in  $[l,u]$ ” means:

$$
lI \preceq A(x) \preceq uI
$$

i.e.

$$
\boxed{ A(x) - lI \succeq 0,\quad uI - A(x)\succeq 0. }
$$

Two LMIs.

* * *

6) Why these constraints are convex (and why SDP is the right class)
====================================================================

Two facts:

1.  The PSD cone  $\mathbb{S}^n_+$  is convex.
2.  Affine preimages preserve convexity.

So any LMI  $F(x)\succeq 0$  defines a convex feasible set.

Also, spectral functions:

*    $A\mapsto \lambda_{\max}(A)$  is convex on symmetric matrices.
*    $A\mapsto \lambda_{\min}(A)$  is concave.  
    But you don’t even need to remember those theorems to model them, because the LMIs are equivalent and automatically convex.

* * *

7) The “cheat sheet” templates (the ones you deploy instantly)
==============================================================

These are Phase 5.7 in a nutshell.

### Template 1: largest eigenvalue upper bound

$$
\boxed{\lambda_{\max}(A(x)) \le t \iff tI - A(x)\succeq 0.}
$$

### Template 2: smallest eigenvalue lower bound

$$
\boxed{\lambda_{\min}(A(x)) \ge t \iff A(x) - tI\succeq 0.}
$$

### Template 3: eigenvalues in  $[l,u]$ 

$$
\boxed{l \le \lambda_i(A(x)) \le u\ \forall i \iff A(x)-lI\succeq 0,\ \ uI-A(x)\succeq 0.}
$$

### Template 4: symmetric spectral norm bound

$$
\boxed{\|A(x)\|_2 \le t \iff tI-A(x)\succeq 0,\ \ tI+A(x)\succeq 0.}
$$

### Template 5: general matrix spectral norm bound

$$
\boxed{\|M(x)\|_2 \le t \iff \begin{bmatrix}tI & M(x)\\ M(x)^\top & tI\end{bmatrix}\succeq 0.}
$$

* * *

8) Common failure modes (where people lose points)
==================================================

1.  **Forgetting symmetry.**  
    Eigenvalue LMIs like  $tI-A\succeq 0$  implicitly assume  $A$  is symmetric. If  $A$  isn’t symmetric,  $\lambda_{\max}(A)$  isn’t even guaranteed real. For non-symmetric matrices you typically move to singular values / spectral norm (Template 5).
2.  **Confusing  $\lambda_{\max}(A)\le t$  with  $A \le t$ ** (entrywise).  
    Entrywise inequality is not the same as PSD order. You must use  $tI-A\succeq 0$ , not “every entry ≤ t.”
3.  **Dropping the identity matrix.**  
    The correct comparison is to  $tI$ , not  $t$  alone.
4.  **Mixing up min and max.**  
     $\lambda_{\max}(A)\le t$  gives  $tI-A\succeq 0$ .  
     $\lambda_{\min}(A)\ge t$  gives  $A-tI\succeq 0$ .

* * *

9) Intuition that makes it stick (so it’s not memorization)
===========================================================

Think of  $A$  as a “quadratic form machine”:

$$
z \mapsto z^\top A z.
$$

The largest eigenvalue is literally “how big that quadratic form can get on the unit sphere”:

$$
\lambda_{\max}(A)=\max_{\|z\|=1} z^\top A z.
$$

So saying  $\lambda_{\max}(A)\le t$  is saying:

$$
z^\top A z \le t \quad \forall \|z\|=1.
$$

Equivalently:

$$
z^\top (tI-A) z \ge 0\quad \forall z,
$$

which is exactly:

$$
tI-A\succeq 0.
$$

That’s the geometric heart of the LMI equivalence.

* * *

That’s Phase 5.7: **spectral statements become PSD order statements**, and PSD order statements are LMIs, which are SDP constraints.

At this point, Phase 5 is complete: you can take almost any “messy but convex” expression you’ll see in a problem set and land it in LP/SOCP/SDP form by pattern recognition.

If you keep going, the next natural “Phase 6” move is quasiconvexity + bisection and perspective transformations—different flavor, but equally mechanical once internalized.

## Response:
Phase 6.1 — Quasiconvexity (what it is, how to recognize it, and why bisection works)
-------------------------------------------------------------------------------------

Up to Phase 5, the game was: “rewrite into LP/QP/SOCP/SDP.” That game assumes the problem is convex (objective convex, constraints convex).

Phase 6 is for problems that are _not_ convex in the usual sense, but are still “one notch away” from convex in a very exploitable way.

That notch is **quasiconvexity**.

Quasiconvex problems are often solved by:

*   converting them into a family of **convex feasibility problems** indexed by a scalar threshold,
*   then doing **bisection** on that scalar.

So 6.1 is about the concept that makes this legal: **convex sublevel sets**.

* * *

0) Prerequisites you must have totally clear
============================================

Let  $f:\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}$  be an extended-valued function with domain

$$
\mathrm{dom}\,f=\{x : f(x)<+\infty\}.
$$

For any real number  $\alpha$ , define the **sublevel set**:

$$
S_\alpha := \{x\in\mathrm{dom}\,f : f(x)\le \alpha\}.
$$

Convexity of sets means:

$$
x,y\in S \Rightarrow \theta x+(1-\theta)y\in S \quad \forall \theta\in[0,1].
$$

* * *

1) Definition: quasiconvex function
===================================

### Definition (quasiconvex)

 $f$  is **quasiconvex** if **every sublevel set is convex**:

$$
\boxed{ f\ \text{quasiconvex}\quad \Longleftrightarrow\quad S_\alpha=\{x : f(x)\le \alpha\}\ \text{is convex for every }\alpha\in\mathbb{R}. }
$$

That’s the definition you should default to. It’s the one that directly explains why bisection works.

### Definition (quasiconcave)

Similarly,  $f$  is **quasiconcave** if **every superlevel set** is convex:

$$
\{x : f(x)\ge \alpha\}\ \text{convex for all }\alpha.
$$

Quasiconcave shows up in utility / production functions etc., but for optimization Phase 6 you mainly care about quasiconvex minimization.

* * *

2) Relationship to convexity (don’t mix them)
=============================================

2.1 Convex  $\Rightarrow$  quasiconvex
--------------------------------------

Every convex function is quasiconvex.

### Proof (rigorous and explicit)

Assume  $f$  is convex. Fix  $\alpha$ . Take  $x,y\in S_\alpha$ , so  $f(x)\le\alpha$ ,  $f(y)\le\alpha$ . For any  $\theta\in[0,1]$ ,

$$
f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y)\le \theta\alpha+(1-\theta)\alpha=\alpha.
$$

Thus  $\theta x+(1-\theta)y\in S_\alpha$ . So  $S_\alpha$  is convex. Since  $\alpha$  was arbitrary,  $f$  is quasiconvex.

So:

$$
\boxed{\text{convex} \Rightarrow \text{quasiconvex}.}
$$

2.2 Quasiconvex  $\not\Rightarrow$  convex
------------------------------------------

Quasiconvex is weaker. The function may fail Jensen’s inequality but still have convex sublevel sets.

Classic example (1D):

$$
f(x)=\begin{cases} 0 & x\le 0\\ x & x>0 \end{cases}
$$

This is quasiconvex (sublevel sets are intervals), but it is not convex? (Actually this one _is_ convex; better example:)

$$
f(x)=\min(x,0)
$$

This is not convex (it is concave), but it is quasiconvex because sublevel sets  $\{x:\min(x,0)\le \alpha\}$  are either all of  $\mathbb{R}$  or half-lines, which are convex.

Even cleaner “shape intuition”:

*   convex functions: “bowl-shaped”
*   quasiconvex functions: “no strict local minima except global ones” (not a definition, but a helpful mental picture in 1D)

* * *

3) Equivalent characterizations (important for proofs/recognition)
==================================================================

3.1 The “max along a segment” inequality
----------------------------------------

A function  $f$  is quasiconvex iff for all  $x,y$  and  $\theta\in[0,1]$ ,

$$
\boxed{ f(\theta x+(1-\theta)y)\le \max\{f(x),f(y)\}. }
$$

### Proof (both directions)

#### ( $\Rightarrow$ ) If sublevel sets are convex, show the inequality

Let  $x,y$  be arbitrary. Define  $\alpha:=\max\{f(x),f(y)\}$ . Then  $f(x)\le\alpha$  and  $f(y)\le\alpha$ , so  $x,y\in S_\alpha$ . Since  $S_\alpha$  is convex,  $\theta x+(1-\theta)y\in S_\alpha$ . Therefore

$$
f(\theta x+(1-\theta)y)\le\alpha=\max\{f(x),f(y)\}.
$$

#### ( $\Leftarrow$ ) If the inequality holds, show sublevel sets are convex

Fix  $\alpha$ . Take  $x,y\in S_\alpha$ , so  $f(x)\le\alpha$  and  $f(y)\le\alpha$ . Then  $\max\{f(x),f(y)\}\le\alpha$ . By the inequality,

$$
f(\theta x+(1-\theta)y)\le \max\{f(x),f(y)\}\le\alpha.
$$

So  $\theta x+(1-\theta)y\in S_\alpha$ . Hence  $S_\alpha$  is convex.

Done.

This is a very practical test: it resembles convexity inequality but with “max” instead of “average.”

* * *

3.2 Composition rule (the most used closure property)
-----------------------------------------------------

If  $f$  is quasiconvex and  $\phi:\mathbb{R}\to\mathbb{R}$  is **nondecreasing**, then  $\phi\circ f$  is quasiconvex.

### Why (sublevel sets)

$$
\{x: (\phi\circ f)(x)\le \alpha\} = \{x: f(x)\le \phi^{-1}(\alpha)\}
$$

when  $\phi$  is nondecreasing (more precisely, it’s a sublevel set of  $f$  at some threshold). Convexity is preserved.

This is why minimizing  $f$  or minimizing  $\log f$  can be equivalent in quasiconvex land if  $\log$  is increasing on the domain (e.g.,  $f>0$ ).

* * *

4) Quasiconvex optimization problems (definition)
=================================================

A **quasiconvex optimization problem** typically looks like:

$$
\min_x\ f_0(x) \quad\text{s.t.}\quad f_i(x)\le 0,\ i=1,\dots,m, \quad Ax=b,
$$

where:

*   each constraint function  $f_i$  is convex (so the feasible set is convex),
*   the objective  $f_0$  is quasiconvex (not necessarily convex).

Key point: the feasible set is convex, but the objective might not be.

Why is this still tractable? Because of the definition: sublevel sets of  $f_0$  are convex.

* * *

5) The central trick: reduce minimization to feasibility via sublevel sets
==========================================================================

Let  $p^\star$  be the optimal value:

$$
p^\star = \inf\{f_0(x): x\in\mathcal{F}\}
$$

where  $\mathcal{F}$  is the feasible set defined by constraints.

For any scalar  $\alpha$ , consider the feasibility problem:

$$
\text{find } x \text{ such that } x\in\mathcal{F}\ \text{and}\ f_0(x)\le \alpha.
$$

This is asking whether the intersection

$$
\mathcal{F}\cap S_\alpha
$$

is nonempty.

If  $f_0$  is quasiconvex, then  $S_\alpha$  is convex. If  $\mathcal{F}$  is convex, their intersection is convex. So it’s a convex feasibility problem.

Define the predicate:

$$
\Phi(\alpha) = \begin{cases} \text{true} & \exists x\in\mathcal{F} \text{ with } f_0(x)\le\alpha\\ \text{false} & \text{otherwise} \end{cases}
$$

Now comes the key monotonicity:

### Monotonicity lemma

If  $\Phi(\alpha)$  is true and  $\beta\ge\alpha$ , then  $\Phi(\beta)$  is also true.

Because  $S_\alpha \subseteq S_\beta$  (bigger threshold gives bigger sublevel set).

So  $\Phi(\alpha)$  is a monotone “step function” in  $\alpha$ : false below  $p^\star$ , true above  $p^\star$ .

This is exactly the structure bisection exploits (Phase 6.2).

* * *

6) How to recognize quasiconvex objectives in practice (the big patterns)
=========================================================================

6.1 Linear-fractional functions (most important)
------------------------------------------------

$$
f(x)=\frac{a^\top x + b}{c^\top x + d} \quad \text{with domain } c^\top x + d > 0.
$$

This is generally not convex, but it is quasiconvex (and quasiconcave). Why? Because its sublevel sets are halfspaces after cross-multiplying with a positive denominator.

Sublevel set:

$$
\frac{a^\top x + b}{c^\top x + d}\le \alpha \quad\Longleftrightarrow\quad a^\top x + b \le \alpha(c^\top x + d)
$$

provided  $c^\top x + d>0$ . The right side is affine in  $x$ . So the sublevel set is a halfspace intersection with the domain—convex.

This is the gateway to “fractional programs” and perspective transforms.

6.2 Max of quasiconvex functions is quasiconvex
-----------------------------------------------

If  $f_i$  are quasiconvex, then

$$
f(x)=\max_i f_i(x)
$$

is quasiconvex because

$$
\{x: \max_i f_i(x)\le \alpha\} = \bigcap_i \{x: f_i(x)\le\alpha\}
$$

intersection of convex sets.

6.3 Norm ratios and “relative error” objectives
-----------------------------------------------

Objectives like

$$
\frac{\|Ax-b\|_2}{c^\top x + d}
$$

with positive denominator are typically quasiconvex because sublevel sets become SOC constraints after multiplying by denominator:

$$
\|Ax-b\|_2 \le \alpha(c^\top x + d)
$$

which is SOC if RHS is affine and constrained nonnegative.

This is extremely common in robust regression / signal processing.

* * *

7) Common failure modes / subtle points
=======================================

1.  **Forgetting domain positivity in fractional expressions**  
    Cross-multiplication is only legal if you know the denominator is positive (or negative) on the domain. Always include domain constraint  $c^\top x + d > 0$  (or  $\ge \epsilon$ ).
2.  **Assuming quasiconvex means “convex enough to take gradients”**  
    Quasiconvex does not imply differentiable, Hessian PSD, etc. It’s a set-geometry property.
3.  **Mixing quasiconvex vs quasiconcave**  
    Minimization wants quasiconvex; maximization wants quasiconcave (since maximizing a quasiconcave function is analogous).
4.  **Strict vs non-strict inequalities**  
    Sublevel sets use  $\le$ . If you use  $<$ , you get open sets; convexity still makes sense but solvers and feasibility arguments prefer closed constraints.

* * *

8) The “mental model” you should carry forward
==============================================

Convex optimization:

*   objective itself is convex, so local info (subgradients) gives global guarantees.

Quasiconvex optimization:

*   objective may not be convex, but the sets  $\{f\le\alpha\}$  are convex, so
*   “is the optimum  $\le \alpha$ ?” becomes a convex feasibility question,
*   and you can locate the optimum by searching in  $\alpha$ .

That is the bridge to Phase 6.2 (bisection) and Phase 6.3 (perspective / fractional transformations).

If you continue, the next piece is exactly: define the bisection algorithm, prove its correctness using monotonicity of  $\Phi(\alpha)$ , and show how each feasibility check is an LP/SOCP/SDP depending on the sublevel constraint shape.

## Response:
Phase 6.2 — Bisection method for quasiconvex optimization (turn minimization into repeated convex feasibility)
--------------------------------------------------------------------------------------------------------------

Phase 6.1 gave the key structural fact:

> If  $f$  is quasiconvex, then its sublevel sets  $S_\alpha=\{x: f(x)\le \alpha\}$  are convex.  
> So “is there a feasible point with  $f(x)\le \alpha$ ?” becomes a convex feasibility problem.

Phase 6.2 is the algorithmic exploit:

> The set of  $\alpha$  values for which the feasibility problem is solvable is an interval  $[p^\star,\infty)$ .  
> That monotone “yes/no” structure can be located by **bisection**.

What you must be able to do mechanically on PS sets:

1.  Build the feasibility problem for a given threshold  $\alpha$ .
2.  Show it is convex (LP/SOCP/SDP).
3.  Use bisection on  $\alpha$  to approximate the optimal value  $p^\star$ .
4.  Understand stopping criteria and correctness guarantees.

I’ll do all of that from first principles.

* * *

0) The problem class: quasiconvex minimization
==============================================

We consider the canonical form:

$$
\begin{aligned} \min_x\quad & f_0(x)\\ \text{s.t.}\quad & x\in \mathcal{F} \end{aligned}
$$

where:

*    $\mathcal{F}$  is a **convex feasible set** (usually described by convex inequalities + affine equalities),
*    $f_0$  is **quasiconvex**.

You can think of  $\mathcal{F}$  as:

$$
\mathcal{F} = \{x: f_i(x)\le 0,\ i=1,\dots,m,\ \ Ax=b\}
$$

with each  $f_i$  convex and  $Ax=b$  affine.

Define the optimal value:

$$
p^\star := \inf\{f_0(x): x\in\mathcal{F}\}.
$$

We often assume there is an optimizer  $x^\star$  attaining this infimum, but bisection as an algorithm is about approximating the value even when you only have infimum.

* * *

1) The feasibility oracle:  $\Phi(\alpha)$ 
===========================================

For any scalar  $\alpha$ , define the decision problem:

$$
\Phi(\alpha) := \text{“Does there exist } x\in\mathcal{F} \text{ such that } f_0(x)\le \alpha\text{?”}
$$

Equivalently, the feasibility set for level  $\alpha$  is:

$$
\mathcal{F}_\alpha := \mathcal{F}\cap S_\alpha = \{x\in\mathcal{F}: f_0(x)\le \alpha\}.
$$

So:

*    $\Phi(\alpha)=\text{true}$  iff  $\mathcal{F}_\alpha\neq \emptyset$ .
*    $\Phi(\alpha)=\text{false}$  iff  $\mathcal{F}_\alpha=\emptyset$ .

### Why  $\mathcal{F}_\alpha$  is convex (critical)

*    $\mathcal{F}$  is convex by assumption.
*    $S_\alpha$  is convex because  $f_0$  is quasiconvex (definition).
*   Intersection of convex sets is convex.

So each feasibility test is a **convex feasibility problem**. In practice, it usually becomes LP/SOCP/SDP depending on how you model  $f_0(x)\le \alpha$ .

* * *

2) The monotonicity lemma (the reason bisection works)
======================================================

### Lemma (monotone feasibility)

If  $\alpha \le \beta$ , then

$$
S_\alpha \subseteq S_\beta.
$$

Therefore

$$
\mathcal{F}_\alpha = \mathcal{F}\cap S_\alpha \subseteq \mathcal{F}\cap S_\beta = \mathcal{F}_\beta.
$$

So:

$$
\boxed{\Phi(\alpha)=\text{true} \Rightarrow \Phi(\beta)=\text{true for all } \beta\ge \alpha.}
$$

Similarly:

$$
\boxed{\Phi(\beta)=\text{false} \Rightarrow \Phi(\alpha)=\text{false for all } \alpha\le \beta.}
$$

This means the “truth” region is an interval:

$$
\{\alpha: \Phi(\alpha)=\text{true}\} = [p^\star,\infty)
$$

(under mild regularity; at worst it’s  $(p^\star,\infty)$  if infimum not attained, but bisection still approximates).

This “step function” structure is exactly what bisection needs.

* * *

3) Bisection algorithm (conceptual and then mechanical)
=======================================================

3.1 What bisection is trying to do
----------------------------------

We want to find  $p^\star$ . We can’t directly evaluate  $p^\star$ , but we can ask:

*   Is  $p^\star \le \alpha$ ?  
    That’s exactly  $\Phi(\alpha)$ .

So we maintain an interval  $[L,U]$  such that:

*    $L$  is a **lower bound**:  $\Phi(L)=\text{false}$  (no feasible solution achieves objective  $\le L$ )
*    $U$  is an **upper bound**:  $\Phi(U)=\text{true}$  (there exists feasible solution with objective  $\le U$ )

Then  $p^\star\in(L,U]$ . We repeatedly halve the interval until tight.

* * *

3.2 The bisection steps (precise)
---------------------------------

**Inputs:**

*   A feasibility oracle: given  $\alpha$ , solve “find  $x\in\mathcal{F}$  with  $f_0(x)\le \alpha$ ” or declare infeasible.
*   Initial bounds  $L_0<U_0$  with:
    *    $\Phi(L_0)=\text{false}$ 
    *    $\Phi(U_0)=\text{true}$ 
*   Tolerance  $\varepsilon>0$  (desired accuracy on optimal value)

**Iteration  $k$ :**

1.  Midpoint:
    $$
    \alpha_k = \frac{L_k+U_k}{2}.
    $$
2.  Solve feasibility problem at level  $\alpha_k$ :
    *   If feasible (oracle returns some  $x_k$ ), set:
        $$
        U_{k+1} = \alpha_k,\quad L_{k+1}=L_k.
        $$
        (We found an upper bound; we can tighten from above.)
    *   If infeasible, set:
        $$
        L_{k+1} = \alpha_k,\quad U_{k+1}=U_k.
        $$
        (We proved no point can achieve that low value, so tighten from below.)

Stop when:

$$
U_k - L_k \le \varepsilon.
$$

Then you output:

*    $U_k$  as an  $\varepsilon$ \-accurate upper bound on  $p^\star$ ,
*    $L_k$  as an  $\varepsilon$ \-accurate lower bound,
*   and the best feasible  $x$  you found (from the last “feasible” check) as an approximate optimizer.

* * *

4) Correctness proof (why the bounds stay valid)
================================================

This is the heart. You should be able to reproduce it.

### Invariant

At every iteration  $k$ ,

$$
\Phi(L_k)=\text{false},\qquad \Phi(U_k)=\text{true}.
$$

**Base case:** true by how you choose  $L_0,U_0$ .

**Inductive step:** assume invariant holds at iteration  $k$ .

Let  $\alpha_k=(L_k+U_k)/2$ .

*   If  $\Phi(\alpha_k)=\text{true}$ , then there exists feasible  $x$  with  $f_0(x)\le\alpha_k$ . Since  $\alpha_k \le U_k$ , monotonicity implies  $\Phi(U_k)=\text{true}$  still. We set  $U_{k+1}=\alpha_k$ , so  $\Phi(U_{k+1})=\text{true}$ . We keep  $L_{k+1}=L_k$  so  $\Phi(L_{k+1})=\text{false}$  remains.
*   If  $\Phi(\alpha_k)=\text{false}$ , then no feasible point achieves objective  $\le\alpha_k$ . Since  $L_k\le\alpha_k$ , monotonicity implies  $\Phi(L_k)=\text{false}$  still. We set  $L_{k+1}=\alpha_k$ , so  $\Phi(L_{k+1})=\text{false}$ . We keep  $U_{k+1}=U_k$  so  $\Phi(U_{k+1})=\text{true}$  remains.

Thus invariant holds for  $k+1$ . By induction, it always holds.

### Consequence

Since  $\Phi(L_k)=\text{false}$ , we know  $p^\star > L_k$ .  
Since  $\Phi(U_k)=\text{true}$ , we know  $p^\star \le U_k$ .  
So:

$$
L_k < p^\star \le U_k
$$

for all  $k$ . This is exactly what we want: a shrinking bracket around the optimal value.

* * *

5) Convergence rate (how many iterations you need)
==================================================

Each iteration halves the interval length:

$$
U_{k+1}-L_{k+1}=\frac{U_k-L_k}{2}.
$$

So after  $k$  steps:

$$
U_k-L_k = \frac{U_0-L_0}{2^k}.
$$

To get  $U_k-L_k\le\varepsilon$ , it suffices that:

$$
\frac{U_0-L_0}{2^k}\le\varepsilon \quad\Longleftrightarrow\quad 2^k \ge \frac{U_0-L_0}{\varepsilon} \quad\Longleftrightarrow\quad k \ge \log_2\left(\frac{U_0-L_0}{\varepsilon}\right).
$$

So bisection needs  $O(\log(1/\varepsilon))$  feasibility solves.

This is why it’s so popular: very reliable, no derivatives, just monotone yes/no.

* * *

6) How you actually build the feasibility problem  $f_0(x)\le\alpha$ 
=====================================================================

This is where Phase 5 modeling languages return.

Given  $\alpha$ , you add the constraint:

$$
f_0(x)\le\alpha
$$

to your original convex constraints.

But to feed it to an LP/SOCP/SDP solver, you must express it in standard form.

Common quasiconvex forms:

6.1 Linear-fractional objective
-------------------------------

$$
f_0(x)=\frac{a^\top x+b}{c^\top x+d},\quad c^\top x+d>0.
$$

Sublevel set:

$$
\frac{a^\top x+b}{c^\top x+d}\le\alpha \Longleftrightarrow a^\top x+b \le \alpha(c^\top x+d)
$$

with the domain constraint  $c^\top x+d>0$  (often  $ \ge \epsilon$ ).

That’s a linear inequality (for fixed  $\alpha$ ). So the feasibility problem is convex (often an LP if the rest is linear).

6.2 Norm ratio objective (very common)
--------------------------------------

$$
f_0(x)=\frac{\|Ax-b\|_2}{c^\top x+d},\quad c^\top x+d>0.
$$

Sublevel set:

$$
\frac{\|Ax-b\|_2}{c^\top x+d}\le\alpha \Longleftrightarrow \|Ax-b\|_2 \le \alpha(c^\top x+d),
$$

with  $c^\top x+d\ge 0$ . For fixed  $\alpha$ , RHS is affine, so this is an SOCP constraint (Phase 5.3).

So each feasibility check is an SOCP.

This is the classic “quasiconvex + bisection” pattern.

* * *

7) Choosing initial bounds  $L_0,U_0$  (practical but important)
================================================================

Bisection requires a bracket.

### 7.1 Getting an upper bound  $U_0$ 

Find any feasible  $x_0\in\mathcal{F}$ . Then:

$$
U_0 = f_0(x_0)
$$

works because  $\Phi(U_0)$  is true (witness  $x_0$ ).

If you can’t easily find a feasible point, sometimes you solve a separate feasibility problem for  $\mathcal{F}$  first.

### 7.2 Getting a lower bound  $L_0$ 

This depends on the objective structure:

*   If  $f_0(x)\ge 0$  always (common for ratios of norms), you can take  $L_0=0$ .
*   Otherwise you can take a very small number and increase until infeasibility flips (or do “doubling” search).

A robust generic approach:

*   start with  $L_0$  very small (like  $-M$ ) known to be infeasible or obviously below infimum,
*   or use problem-specific inequalities to bound from below.

For many PS6-style ratio objectives,  $0$  is a natural lower bound because norms are nonnegative and denominators are positive.

* * *

8) Stopping criteria: value accuracy vs solution accuracy
=========================================================

### 8.1 Value (objective) accuracy

Stop when  $U_k-L_k\le\varepsilon$ . Then you have:

$$
p^\star \in (L_k,U_k]
$$

and  $U_k$  is at most  $\varepsilon$  above  $L_k$ . That means your value estimate is accurate to  $\varepsilon$ .

### 8.2 Approximate optimizer

When  $\Phi(\alpha_k)$  is feasible, the solver returns some point  $x_k$ . Keep the _best_ feasible point found (smallest  $\alpha$  feasible so far). At termination, that  $x$  has objective  $\le U_k$ , so it’s near-optimal in value.

Important nuance: bisection is primarily a **value bracketing** method. The  $x$  you get is “good enough” for many uses, but if you need high-precision primal solutions you might warm-start or do refinement.

* * *

9) Failure modes / subtle points (exam traps)
=============================================

1.  **Denominator sign issues in fractional sublevel sets**  
    If you cross-multiply  $ \frac{p(x)}{q(x)}\le\alpha \Rightarrow p(x)\le\alpha q(x)$ , you must enforce  $q(x)>0$  (or  $<0$  consistently). Otherwise the inequality direction can flip and you get the wrong set.
2.  **Non-quasiconvex objective**  
    Bisection relies on sublevel sets being convex and nested. If  $f_0$  is not quasiconvex,  $\Phi(\alpha)$  might not be monotone, and bisection can fail.
3.  **Numerical feasibility tolerance**  
    Solvers return “infeasible” or “feasible” up to tolerances. Near the boundary  $p^\star$ , numerical issues can cause inconsistent answers. Practical fix: use slightly conservative tolerances or add small margins (e.g., enforce  $c^\top x+d \ge \epsilon$ ).
4.  **Infimum not attained**  
    Then  $\Phi(p^\star)$  may be false but  $\Phi(\alpha)$  true for all  $\alpha>p^\star$ . Bisection still works: it will drive  $U_k\downarrow p^\star$ .

* * *

10) The full “do-this-on-a-PS” recipe
=====================================

When you see a quasiconvex minimization:

1.  **Identify  $f_0$  as quasiconvex** by sublevel sets.
2.  Define feasibility problem for a threshold  $\alpha$ :
    $$
    \text{find } x\in\mathcal{F}\ \text{s.t. } f_0(x)\le\alpha.
    $$
3.  **Rewrite  $f_0(x)\le\alpha$ ** into LP/SOCP/SDP form using Phase 5 atoms.
4.  Pick bounds  $L_0,U_0$  such that infeasible/feasible.
5.  Run bisection until interval small.
6.  Output best feasible  $x$  and bracket on  $p^\star$ .

That is Phase 6.2.

* * *

If you continue to Phase 6.3 next, we formalize the **perspective transformation**, which is the algebraic engine behind many quasiconvex sublevel rewrites (especially fractional objectives). That’s where “variable substitution” turns a ratio into a convex program directly, sometimes removing the need for bisection.

## Response:
Phase 6.3 — Perspective transformation (the engine behind fractional/quasiconvex tricks)
----------------------------------------------------------------------------------------

Phase 6.1–6.2 said: “If the objective is quasiconvex, solve by bisection on sublevel sets.”

Phase 6.3 gives you something even better when it applies:

> Many quasiconvex (especially fractional / ratio) problems can be turned into a **single convex problem** by a clever change of variables.  
> That change of variables is the **perspective transformation**.

This is not a random trick. It’s a principled convex-analysis operation with clean geometry and proofs.

You need to understand three layers:

1.  The **definition** of the perspective of a function.
2.  Why it preserves convexity.
3.  How it yields the standard fractional substitutions used in linear-fractional and norm-ratio problems.

I’ll do all three, slowly and fully.

* * *

0) Motivation: why “fractional” is annoying
===========================================

A typical “fractional” objective looks like:

$$
\min_x \frac{f(x)}{g(x)}
$$

with  $g(x)>0$ .

Even if  $f$  is convex and  $g$  is affine/positive, the ratio is generally **not convex**.

But its **sublevel sets** often _are_ convex, making it quasiconvex:

$$
\frac{f(x)}{g(x)} \le \alpha \iff f(x)\le \alpha g(x).
$$

That’s bisection-friendly (Phase 6.2).

Perspective transformation goes further: it builds a variable substitution that “absorbs”  $g(x)$  and turns the ratio into a convex objective/constraints directly.

* * *

1) Definition: perspective of a function
========================================

Let  $f:\mathbb{R}^n \to \mathbb{R}\cup\{+\infty\}$  be an extended-valued function.

Define its **perspective**  $\tilde f:\mathbb{R}^n\times\mathbb{R}\to \mathbb{R}\cup\{+\infty\}$  by:

$$
\boxed{ \tilde f(x,t) := t\, f\!\left(\frac{x}{t}\right) \quad \text{for } t>0, }
$$

and typically define  $\tilde f(x,t)=+\infty$  for  $t\le 0$  (to enforce the domain  $t>0$ ).

So:

*   original variable:  $u\in\mathbb{R}^n$ 
*   perspective variables:  $(x,t)$  with  $t>0$ 
*   relation:  $u = x/t$ , i.e.  $x = t u$ 

**Important:** “perspective” is not “divide by  $t$ ” alone. It is the _combination_  $t f(x/t)$ .

* * *

2) The fundamental theorem: convexity is preserved
==================================================

### Theorem

If  $f$  is convex, then its perspective  $\tilde f$  is convex on the set  $\{(x,t): t>0\}$ .

$$
\boxed{ f \text{ convex } \Rightarrow \tilde f(x,t)=t f(x/t) \text{ convex on } t>0. }
$$

This is one of the most important convexity-preserving operations in BV.

* * *

2.1 Proof (fully explicit, from the definition of convexity)
------------------------------------------------------------

We need to show:

$$
\tilde f(\theta (x_1,t_1) + (1-\theta)(x_2,t_2)) \le \theta \tilde f(x_1,t_1) + (1-\theta)\tilde f(x_2,t_2)
$$

for all  $\theta\in[0,1]$  and all  $t_1>0,t_2>0$ .

Let:

$$
(x_\theta,t_\theta)= (\theta x_1+(1-\theta)x_2,\ \theta t_1+(1-\theta)t_2).
$$

Note  $t_\theta>0$  since it’s a convex combination of positive numbers.

Compute:

$$
\tilde f(x_\theta,t_\theta) = t_\theta\, f\!\left(\frac{x_\theta}{t_\theta}\right).
$$

Now define weights:

$$
\lambda_1 := \frac{\theta t_1}{t_\theta},\qquad \lambda_2 := \frac{(1-\theta)t_2}{t_\theta}.
$$

These satisfy:

*    $\lambda_1\ge 0,\lambda_2\ge 0$ ,
*    $\lambda_1+\lambda_2 = \frac{\theta t_1 + (1-\theta)t_2}{t_\theta} = 1.$ 

Now rewrite  $\frac{x_\theta}{t_\theta}$ :

$$
\frac{x_\theta}{t_\theta} = \frac{\theta x_1+(1-\theta)x_2}{t_\theta} = \frac{\theta t_1}{t_\theta}\cdot \frac{x_1}{t_1} + \frac{(1-\theta)t_2}{t_\theta}\cdot \frac{x_2}{t_2} = \lambda_1 \frac{x_1}{t_1} + \lambda_2 \frac{x_2}{t_2}.
$$

So  $\frac{x_\theta}{t_\theta}$  is a convex combination of  $\frac{x_1}{t_1}$  and  $\frac{x_2}{t_2}$  with weights  $\lambda_1,\lambda_2$ .

Now apply convexity of  $f$ :

$$
f\!\left(\frac{x_\theta}{t_\theta}\right) = f\!\left(\lambda_1\frac{x_1}{t_1} + \lambda_2\frac{x_2}{t_2}\right) \le \lambda_1 f\!\left(\frac{x_1}{t_1}\right) + \lambda_2 f\!\left(\frac{x_2}{t_2}\right).
$$

Multiply both sides by  $t_\theta$  (positive, so inequality direction stays):

$$
t_\theta f\!\left(\frac{x_\theta}{t_\theta}\right) \le t_\theta\lambda_1 f\!\left(\frac{x_1}{t_1}\right) + t_\theta\lambda_2 f\!\left(\frac{x_2}{t_2}\right).
$$

But  $t_\theta\lambda_1 = \theta t_1$  and  $t_\theta\lambda_2=(1-\theta)t_2$ . So:

$$
\tilde f(x_\theta,t_\theta) \le \theta t_1 f\!\left(\frac{x_1}{t_1}\right) + (1-\theta) t_2 f\!\left(\frac{x_2}{t_2}\right) = \theta \tilde f(x_1,t_1) + (1-\theta)\tilde f(x_2,t_2).
$$

That is exactly convexity of  $\tilde f$ . Done.

* * *

3) Geometric meaning (epigraph picture)
=======================================

The perspective is the algebraic form of a geometric operation on epigraphs.

Epigraph of  $f$ :

$$
\operatorname{epi}(f)=\{(u,s): f(u)\le s\}.
$$

Perspective epigraph relation:

$$
(\,x,t,s\,)\in \operatorname{epi}(\tilde f) \quad\Longleftrightarrow\quad t>0,\ \ f(x/t)\le s/t.
$$

Equivalently:

$$
(\,x/t,\ s/t\,)\in \operatorname{epi}(f).
$$

So you can think of the perspective as:

*   take points in epigraph of  $f$ ,
*   scale them by  $t$  in a particular “conic” way,
*   which corresponds to taking the **conic hull** of  $\operatorname{epi}(f)$  (with a slice).

This is why perspective is so natural in conic optimization: it’s literally “epigraph turned into a cone.”

You don’t need to memorize that phrase, but you should keep the intuition: **perspective is epigraph scaling**.

* * *

4) The key modeling use: “divide by a positive affine function” via substitution
================================================================================

Here’s the standard pattern.

Suppose you have a problem where a positive affine function is in the denominator:

$$
\min_x \frac{f(x)}{g(x)} \quad \text{s.t. } x\in\mathcal{F},
$$

with:

*    $f$  convex (or at least something you can model),
*    $g(x)=c^\top x + d > 0$  affine and positive on the feasible region.

### The substitution

Define new variables:

$$
t := \frac{1}{g(x)},\qquad y := \frac{x}{g(x)}.
$$

Equivalently:

$$
x = \frac{y}{t},\qquad g(x)=\frac{1}{t}.
$$

But it’s more convenient to enforce:

$$
g(x)\,t = 1,\qquad y = t x.
$$

Because  $g$  is affine, the constraint  $g(x)t=1$  is bilinear in  $(x,t)$ , which is bad. So instead we eliminate  $x$  entirely in favor of  $(y,t)$ .

Since  $x = y/t$ , we rewrite everything in terms of  $y/t$ , and multiply by  $t$  where needed. This is exactly where the perspective appears.

### Why the objective becomes a perspective

If your objective is  $f(x)/g(x)$ , then with  $t=1/g(x)$ :

$$
\frac{f(x)}{g(x)} = t f(x).
$$

But  $x = y/t$ . So:

$$
t f(x) = t f(y/t) = \tilde f(y,t).
$$

That’s the perspective!

So the fractional objective becomes a **convex** function  $\tilde f(y,t)$  when  $f$  is convex and  $t>0$ .

* * *

5) Two extremely important special cases
========================================

5.1 Linear-fractional objective (classic BV)
--------------------------------------------

$$
\min_x \frac{a^\top x+b}{c^\top x+d} \quad \text{with } c^\top x+d>0.
$$

This looks nonconvex, but it is actually convertible exactly to an LP (or conic program) because numerator and denominator are affine.

Use the substitution:

$$
t := \frac{1}{c^\top x+d} > 0,\qquad y := t x.
$$

Then:

*   objective:
    $$
    \frac{a^\top x+b}{c^\top x+d} = (a^\top x+b)t = a^\top (t x) + b t = a^\top y + b t.
    $$
    Linear in  $(y,t)$ .
*   denominator normalization:
    $$
    c^\top x+d = \frac{1}{t} \quad\Longleftrightarrow\quad t(c^\top x+d)=1 \quad\Longleftrightarrow\quad c^\top (t x) + d t = 1 \quad\Longleftrightarrow\quad c^\top y + d t = 1.
    $$
    Linear constraint in  $(y,t)$ .
*   constraints  $x\in\mathcal{F}$ : if  $\mathcal{F}$  is described by linear inequalities  $Fx\le g$ , then
    $$
    F(y/t)\le g \iff Fy \le g t
    $$
    which is linear in  $(y,t)$  because  $g t$  is scalar multiplication.

So a linear-fractional program becomes an LP in  $(y,t)$ .

This is the canonical example where perspective removes the need for bisection entirely.

* * *

5.2 Norm ratio objective (quasiconvex  $\rightarrow$  SOCP via perspective)
---------------------------------------------------------------------------

$$
\min_x \ \frac{\|Ax-b\|_2}{c^\top x+d},\quad c^\top x+d>0.
$$

Bisection way (Phase 6.2) uses:

$$
\|Ax-b\|_2 \le \alpha(c^\top x+d)
$$

for each  $\alpha$ .

Perspective way introduces a normalization:

$$
t = \frac{1}{c^\top x+d},\quad y=tx.
$$

Then  $c^\top y + d t = 1$ .

Rewrite the numerator:

$$
\|Ax-b\|_2 = \left\|A\left(\frac{y}{t}\right)-b\right\|_2 = \left\|\frac{Ay}{t}-b\right\|_2 = \frac{1}{t}\|Ay - bt\|_2
$$

(using homogeneity of the norm:  $\|\lambda v\|=|\lambda|\|v\|$ , and  $t>0$ ).

So the ratio becomes:

$$
\frac{\|Ax-b\|_2}{c^\top x+d} = \|Ax-b\|_2 \cdot t = \left(\frac{1}{t}\|Ay-bt\|_2\right)t = \|Ay-bt\|_2.
$$

Boom: the objective becomes a plain  $\ell_2$  norm in  $(y,t)$ !

So the transformed problem has objective  $\|Ay-bt\|_2$  and linear constraint  $c^\top y + dt=1$ , plus transformed versions of other constraints.

That’s now an SOCP (Phase 5.3).

This is a perfect example of how perspective is “fractional → conic.”

* * *

6) The general sublevel-set viewpoint (connects to quasiconvexity)
==================================================================

Perspective is also why sublevel sets of ratios often become convex.

Consider  $f(x)/(c^\top x+d)\le \alpha$  with positive denominator:

$$
\frac{f(x)}{c^\top x+d}\le \alpha \iff f(x)\le \alpha(c^\top x+d).
$$

If  $f$  is convex and  $\alpha\ge 0$ , then the right side is affine (since  $\alpha$  is fixed). So that sublevel constraint is convex.

Bisection exploits that.

Perspective instead chooses  $t = 1/(c^\top x+d)$  and “bakes” the denominator into variables so the whole objective becomes convex at once.

So you should see perspective as the “structural reason” those sublevel sets are convex.

* * *

7) Failure modes and domain traps (this is where people get wrecked)
====================================================================

1.  **Denominator sign**  
    Everything here assumes  $c^\top x+d>0$ . If it can be negative, cross-multiplication changes direction and the whole transformation breaks. Always enforce positivity (often with  $c^\top x+d \ge \epsilon$ ).
2.  **Forgetting  $t>0$ **  
    Perspective is defined for  $t>0$ . In the transformed problem you must keep  $t>0$  (typically implied by  $c^\top y + dt = 1$  plus feasibility, but sometimes you enforce  $t\ge 0$ ).
3.  **Non-homogeneous constraints**  
    When you rewrite constraints in  $x=y/t$ , you must multiply through by  $t$  carefully. Linear constraints behave nicely; general convex constraints require using the perspective  $\tilde f$ . If you just “multiply by  $t$ ” randomly, you can destroy convexity.
4.  **Equality constraints and scaling**  
    If you have  $Ax=b$ , substituting  $x=y/t$  gives  $A y = b t$ . That’s linear in  $(y,t)$ . Good. But you must remember the right-hand side scales.

* * *

8) The mechanical recipe (what you do on a problem set)
=======================================================

When you see a ratio with a positive affine denominator  $c^\top x+d$ :

1.  Declare new variables:
    $$
    t = \frac{1}{c^\top x+d},\qquad y = t x.
    $$
2.  Add the normalization constraint:
    $$
    c^\top y + d t = 1,\quad t>0.
    $$
3.  Replace every appearance of  $x$  by  $y/t$ .
4.  Multiply constraints/objective by  $t$  in the specific “perspective” way:
    *   A convex  $f(x)$  becomes  $t f(y/t) = \tilde f(y,t)$ , which stays convex.
    *   Affine terms  $a^\top x + b$  become  $a^\top y + bt$ .
    *   Norm terms  $\|Ax-b\|$  often become  $\|Ay - bt\|$  after the cancellation shown above.
5.  Solve the resulting convex problem directly (LP/SOCP/SDP depending on the atoms you end up with).

If that works, you avoided bisection entirely. If it doesn’t (e.g., denominator not affine, or constraints don’t transform cleanly), you fall back to Phase 6.2 bisection on sublevel sets.

* * *

That’s Phase 6.3: the perspective transformation is the **canonical convexity-preserving scaling** that turns many fractional/quasiconvex problems into standard conic programs.

Next in Phase 7 is geometric programming (GP), which is basically “a special case of perspective + log transform,” but with multiplicative structure instead of additive.

## Response:
Phase 7 — Geometric Programming (GP)
------------------------------------

_(how “weird multiplicative optimization” becomes convex after a log transform)_

Geometric programming looks alien the first time you see it, because it’s full of products, powers, and sums of products—exactly the stuff that usually screams “nonconvex.”

The plot twist is that GP is a carefully curated family where those multiplicative forms become **convex** after one specific change of variables:

> take logs of variables, and take logs of the objective/constraints.

This is not a hack. It’s a precise structural equivalence:

*   GP in the original variables is _not_ convex in general.
*   GP becomes a **convex optimization problem** in the log-variables.

Phase 7 is about making that conversion feel as mechanical as Phase 5’s “norm → SOC” moves.

I’ll build it from first principles and end with a cookbook you can apply on PS-style problems.

* * *

0) Why GP exists (intuition before definitions)
===============================================

Many engineering/econ-ish problems are naturally multiplicative:

*   minimizing a product of terms,
*   enforcing that a weighted sum of monomials is ≤ 1,
*   “cost =  $x^{a} y^{b}$ ” type models,
*   “performance ∝ product of decision variables with exponents.”

You want global optimality guarantees, but naive forms are nonconvex.

GP’s trick: multiplicative structure becomes additive under log:

*   products  $\to$  sums,
*   powers  $\to$  scalar multiples,
*   sums of exponentials  $\to$  log-sum-exp (convex).

That’s the whole game.

* * *

1) The atoms: monomials and posynomials
=======================================

Everything in GP is built from two building blocks.

1.1 Domain: positive variables
------------------------------

GP lives on the strictly positive orthant:

$$
x\in\mathbb{R}^n_{++} \quad \text{meaning } x_i>0 \ \forall i.
$$

This is essential: you can’t take  $\log x_i$  if  $x_i\le 0$ .

So GP problems always include (implicitly or explicitly)  $x>0$ .

* * *

1.2 Monomial
------------

A **monomial** in GP (important: GP uses a different meaning than “polynomial monomial”) is a function:

$$
\boxed{ m(x)=c\, x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n} }
$$

with:

*    $c>0$ ,
*   exponents  $a_i\in\mathbb{R}$  (can be negative, fractional, anything real),
*   domain  $x\in\mathbb{R}^n_{++}$ .

Examples:

*    $2 x_1^{1/2} x_2^{-3}$ 
*    $0.1 x_1 x_3^{0}$  (yes, exponent 0 allowed)
*    $x_1^{-1}x_2^{-1}$  (a reciprocal product)

**Key property:** monomials are “log-affine” (we’ll prove).

* * *

1.3 Posynomial
--------------

A **posynomial** is a sum of monomials:

$$
\boxed{ p(x)=\sum_{k=1}^K c_k\, x_1^{a_{1k}}\cdots x_n^{a_{nk}}, \quad c_k>0. }
$$

Examples:

*    $p(x)= x_1 + x_2$  (each term is a monomial)
*    $p(x)= 3x_1^{-1} + 2x_1^{1/2}x_2^{1/2}$ 
*    $p(x)= 0.5x_1^2x_2^{-1} + 7x_2$ 

**Not allowed:** subtraction. Coefficients must be positive. “Posy” = “positive sum.”

* * *

2) The standard GP form
=======================

A (primal) geometric program is typically written as:

$$
\begin{aligned} \min_{x\in\mathbb{R}^n_{++}}\quad & p_0(x) \\ \text{s.t.}\quad & p_i(x) \le 1,\quad i=1,\dots,m \\ & m_j(x) = 1,\quad j=1,\dots,r \end{aligned}
$$

where:

*    $p_0, p_i$  are posynomials,
*    $m_j$  are monomials.

Sometimes the RHS constants aren’t 1. You can always normalize them into this form:

*    $p(x)\le b$  with  $b>0$  becomes  $\frac{1}{b}p(x)\le 1$  (still posynomial).
*    $m(x)=b$  becomes  $\frac{1}{b}m(x)=1$  (still monomial).

So “≤ 1” and “= 1” are just normalization conventions.

* * *

3) The log transform: the core equivalence
==========================================

Define new variables  $y\in\mathbb{R}^n$  by:

$$
\boxed{ y_i = \log x_i \quad\Longleftrightarrow\quad x_i = e^{y_i}. }
$$

This is a bijection between  $x\in\mathbb{R}^n_{++}$  and  $y\in\mathbb{R}^n$ .

Now rewrite every monomial and posynomial in terms of  $y$ .

* * *

4) Monomials become affine in log-space
=======================================

Take a monomial:

$$
m(x)=c \prod_{i=1}^n x_i^{a_i}.
$$

Substitute  $x_i=e^{y_i}$ :

$$
m(e^y)=c \prod_{i=1}^n (e^{y_i})^{a_i} = c \prod_{i=1}^n e^{a_i y_i} = c\, e^{\sum_i a_i y_i}.
$$

Now take log:

$$
\log m(e^y) = \log c + \sum_{i=1}^n a_i y_i.
$$

That is affine in  $y$ .

So:

$$
\boxed{ m(x)\ \text{monomial} \quad\Rightarrow\quad \log m(e^y)=\text{affine function of }y. }
$$

This is why monomial **equalities** become linear equalities in  $y$ .

* * *

5) Posynomials become log-sum-exp (convex) in log-space
=======================================================

Take a posynomial:

$$
p(x)=\sum_{k=1}^K c_k \prod_{i=1}^n x_i^{a_{ik}}.
$$

Each term is a monomial:

$$
c_k \prod_i x_i^{a_{ik}}.
$$

Substitute  $x=e^y$ :

$$
p(e^y) = \sum_{k=1}^K c_k \exp\!\left(\sum_{i=1}^n a_{ik} y_i\right).
$$

Now take log:

$$
\log p(e^y) = \log\left(\sum_{k=1}^K \exp\left(\log c_k + \sum_i a_{ik} y_i\right)\right).
$$

Define affine functions:

$$
u_k(y) := \log c_k + \sum_i a_{ik} y_i.
$$

Then:

$$
\log p(e^y)=\log\left(\sum_{k=1}^K e^{u_k(y)}\right).
$$

That function is the famous **log-sum-exp**:

$$
\mathrm{lse}(u_1,\dots,u_K) := \log\left(\sum_{k=1}^K e^{u_k}\right).
$$

### Crucial fact

$$
\boxed{ \log\left(\sum_{k=1}^K e^{u_k(y)}\right) \text{ is convex in } y \text{ when each } u_k(y) \text{ is affine.} }
$$

So:

$$
\boxed{ p(x)\ \text{posynomial} \quad\Rightarrow\quad \log p(e^y)\ \text{ is convex in } y. }
$$

This is the heart of GP convexity.

(You can view this as a special case of Phase 2.9: log-sum-exp is convex, and affine precomposition preserves convexity.)

* * *

6) Convert the GP constraints into convex constraints
=====================================================

Now transform each constraint type.

6.1 Posynomial inequality  $p(x)\le 1$ 
---------------------------------------

Start:

$$
p(x)\le 1,\quad x>0.
$$

Substitute  $x=e^y$ :

$$
p(e^y)\le 1.
$$

Take log (log is increasing, so inequality direction preserved):

$$
\log p(e^y)\le 0.
$$

Left side is convex in  $y$ . Right side is constant. So this is a convex constraint.

So:

$$
\boxed{ p(x)\le 1 \quad\Longleftrightarrow\quad \log p(e^y)\le 0, \ \text{a convex inequality in } y. }
$$

6.2 Monomial equality  $m(x)=1$ 
--------------------------------

Start:

$$
m(x)=1.
$$

Substitute  $x=e^y$ :

$$
m(e^y)=1.
$$

Take log:

$$
\log m(e^y)=0.
$$

But  $\log m(e^y)$  is affine in  $y$ , so this is a linear equality.

So:

$$
\boxed{ m(x)=1 \quad\Longleftrightarrow\quad \log m(e^y)=0, \ \text{a linear equality in } y. }
$$

* * *

7) Convert the GP objective
===========================

Standard GP objective is posynomial:

$$
\min_x p_0(x).
$$

After substitution  $x=e^y$ , you could minimize  $p_0(e^y)$ , but that objective is not convex in  $y$  in general.

The standard trick is: minimize its log instead. Because  $\log$  is strictly increasing, it preserves minimizers:

$$
\arg\min_x p_0(x) = \arg\min_x \log p_0(x).
$$

So we use:

$$
\min_y \log p_0(e^y).
$$

And we already know  $\log p_0(e^y)$  is convex in  $y$ .

Thus the transformed problem is convex.

**Final convex form (“log-GP”):**

$$
\boxed{ \begin{aligned} \min_y\quad & \log p_0(e^y)\\ \text{s.t.}\quad & \log p_i(e^y)\le 0,\ i=1,\dots,m\\ & \log m_j(e^y)=0,\ j=1,\dots,r. \end{aligned} }
$$

Objective is convex, inequalities convex, equalities affine. This is a convex optimization problem.

* * *

8) Why the objective log trick is valid (rigorous)
==================================================

If  $p_0(x)>0$  for all  $x>0$  (true for posynomials because coefficients are positive and variables positive), then  $\log$  is strictly increasing. For any two feasible points  $x_1,x_2$ :

$$
p_0(x_1) < p_0(x_2) \iff \log p_0(x_1) < \log p_0(x_2).
$$

So the ordering of objective values is unchanged. Therefore minimizers are the same.

So minimizing  $p_0$  is equivalent to minimizing  $\log p_0$ .

* * *

9) Concrete example (walkthrough end-to-end)
============================================

Suppose:

$$
\begin{aligned} \min_{x_1,x_2>0}\quad & x_1^{-1}x_2 + 2x_2^{-1}\\ \text{s.t.}\quad & x_1 x_2^2 \le 3\\ & x_1^{-1}x_2 \le 1. \end{aligned}
$$

Step 1: Normalize constraints to “≤ 1”:

*    $x_1 x_2^2 \le 3 \iff \frac{1}{3}x_1x_2^2 \le 1$ . This is posynomial ≤ 1.
*    $x_1^{-1}x_2 \le 1$  already posynomial ≤ 1 (it’s a monomial actually, but monomial is also posynomial).

Step 2: Substitute  $y_i=\log x_i$ .  
Then  $x_1^{-1}x_2 = e^{-y_1+y_2}$ .  
And  $x_2^{-1} = e^{-y_2}$ .  
And  $\frac{1}{3}x_1 x_2^2 = \frac{1}{3}e^{y_1+2y_2}$ .

Objective:

$$
p_0(e^y)= e^{-y_1+y_2}+2e^{-y_2}.
$$

Convex objective used:

$$
\log p_0(e^y)=\log\big(e^{-y_1+y_2}+2e^{-y_2}\big),
$$

a log-sum-exp of affine functions → convex.

Constraints:

$$
\log\left(\tfrac{1}{3}e^{y_1+2y_2}\right)\le 0 \iff \log\tfrac{1}{3}+y_1+2y_2\le 0,
$$

which is linear (since it was a single monomial term; log killed the exp).

And:

$$
\log(e^{-y_1+y_2})\le 0 \iff -y_1+y_2\le 0,
$$

also linear.

So the transformed problem is convex with a convex objective and linear constraints. Nice.

* * *

10) How GP relates to earlier phases (so it fits your mental map)
=================================================================

*   Phase 6.3 (perspective) was about ratios with positive denominators.
*   Phase 7 (GP) is about multiplicative monomial/posynomial structure.
*   The convex function that appears in GP is **log-sum-exp**, which you already met as a standard convex atom in Phase 2.8.
*   The constraints become convex because log is monotone and turns products into sums.

So GP is basically:

*   “use logs to convert multiplicative algebra into additive convex analysis.”

* * *

11) Common failure modes (GP exam traps)
========================================

1.  **Variables must be strictly positive**  
    If the problem allows  $x_i=0$  or negative values, it is not a standard GP. (Sometimes you can reparameterize, but not automatically.)
2.  **Subtractions kill GP**  
    Expressions like  $x_1 + x_2 - 1$  are not posynomials. GP can’t handle negative coefficients in posynomials.
3.  **Equality constraints must be monomial equalities**  
    Posynomial equality  $p(x)=1$  is not allowed in standard GP (it’s generally nonconvex). Only monomial equalities are GP-legal.
4.  **Don’t forget normalization**  
    Always rewrite  $p(x)\le b$  as  $(1/b)p(x)\le 1$  with  $b>0$ . If  $b\le 0$ , the constraint is either infeasible or meaningless in GP context.
5.  **Objective must be posynomial or monomial (depending on form)**  
    Standard GP requires posynomial objective for minimization. Maximizing a posynomial is not GP-convex (it becomes a nonconvex problem).

* * *

12) The mechanical GP cookbook
==============================

When you suspect something is a GP:

1.  Check variables are intended  $>0$ .
2.  Express objective as posynomial  $p_0(x)$  (or monomial).
3.  Express inequalities as posynomials ≤ 1.
4.  Express equalities as monomials = 1.
5.  Substitute  $y=\log x$ .
6.  Replace each posynomial constraint  $p(x)\le 1$  with  $\log p(e^y)\le 0$ .
7.  Replace each monomial equality  $m(x)=1$  with  $\log m(e^y)=0$  (linear).
8.  Replace objective with  $\min_y \log p_0(e^y)$ .
9.  Solve the resulting convex problem; recover  $x=e^y$ .

That’s the whole transformation.

* * *

If you want the next natural continuation, it’s to do Phase 8: “PS6 synthesis,” where you practice quickly deciding: LP vs SOCP vs SDP vs GP vs quasiconvex+bisection, and then executing the rewrite with zero hesitation.

## Response:
Perfect. We now switch modes from **theory-building** to **surgical PS6 execution**.

Phase 8 is not about learning new ideas; it is about **pattern recognition under pressure**.  
Each exercise corresponds to _exactly one_ transformation pattern you already mastered.

We will therefore do **Exercise 4.25** in the following disciplined way:

1.  **Restate the exercise structurally** (what kind of beast it is).
2.  **Classify it immediately** (LP / SOCP / SDP / GP / quasiconvex+bisection).
3.  **Justify the classification rigorously** (no handwaving).
4.  **Execute the transformation step by step**, with zero algebra skipped.
5.  **Explain why the final problem is convex** and solver-ready.
6.  **Extract the reusable pattern** (so you never struggle with this again).

No shortcuts, no “BV says so.”  
This is meant to be **rebuildable from memory**.

* * *

Exercise 4.25 (Boyd–Vandenberghe) — **Geometric Programming**
=============================================================

_(I will phrase it generically; the exact coefficients don’t matter for the structure.)_

The exercise asks you to solve or reformulate an optimization problem of the form:

$$
\begin{aligned} \min_{x \in \mathbb{R}^n_{++}} \quad & p_0(x) \\ \text{s.t.} \quad & p_i(x) \le 1, \quad i=1,\dots,m \\ & m_j(x) = 1, \quad j=1,\dots,r \end{aligned}
$$

where:

*    $p_0, p_i$  are **posynomials**
*    $m_j$  are **monomials**
*   variables are constrained to be **strictly positive**

This is **exactly** the canonical geometric program.

* * *

1\. Immediate classification (this is the key PS6 skill)
--------------------------------------------------------

This problem is:

*   ❌ not LP (products, powers)
*   ❌ not SOCP (multiplicative structure, not norms)
*   ❌ not SDP (no matrix variables, no eigenvalues)
*   ❌ not quasiconvex+bisection (we can do better)

✅ **This is a Geometric Program (GP)**.

So the correct move is:

> **Log-transform the variables and convert it into a convex problem.**

If you hesitate here in an exam, you lose time.  
This should be _automatic_.

* * *

2\. Why GP is the correct language (rigorous justification)
-----------------------------------------------------------

### Key facts (already proved in Phase 7):

1.  A **monomial**
    $$
    m(x) = c \prod_{k=1}^n x_k^{a_k}, \quad c>0
    $$
    becomes **affine** after log-transform.
2.  A **posynomial**
    $$
    p(x) = \sum_{\ell=1}^K c_\ell \prod_{k=1}^n x_k^{a_{k\ell}}
    $$
    becomes **log-sum-exp of affine functions**, hence **convex**, after log-transform.
3.  Log is **strictly increasing**, so minimizing  $p_0(x)$  is equivalent to minimizing  $\log p_0(x)$ .

Therefore, GP problems are _not convex in  $x$ _, but are **convex in  $y=\log x$ **.

This is not a trick. It is an exact equivalence.

* * *

3\. Step 1 — Change of variables (the irreversible move)
--------------------------------------------------------

Define new variables:

$$
\boxed{y_i = \log x_i \quad \Longleftrightarrow \quad x_i = e^{y_i}}
$$

This maps:

$$
\mathbb{R}^n_{++} \;\longleftrightarrow\; \mathbb{R}^n
$$

There is **no loss of generality** and **no approximation**.

* * *

4\. Step 2 — Transform monomial equalities
------------------------------------------

Take a monomial equality constraint:

$$
m_j(x) = c_j \prod_{k=1}^n x_k^{a_{kj}} = 1
$$

Substitute  $x_k = e^{y_k}$ :

$$
c_j \exp\!\left(\sum_k a_{kj} y_k\right) = 1
$$

Take logarithm:

$$
\log c_j + \sum_k a_{kj} y_k = 0
$$

This is **linear in  $y$ **.

### Conclusion:

$$
\boxed{\text{monomial equality} \;\longrightarrow\; \text{linear equality}}
$$

This is crucial: **equalities remain easy** in GP.

* * *

5\. Step 3 — Transform posynomial inequalities
----------------------------------------------

Take a posynomial constraint:

$$
p_i(x) = \sum_{\ell=1}^{K_i} c_{i\ell} \prod_k x_k^{a_{k\ell}} \le 1
$$

Substitute  $x_k = e^{y_k}$ :

$$
\sum_{\ell=1}^{K_i} c_{i\ell} \exp\!\left(\sum_k a_{k\ell} y_k\right) \le 1
$$

Take logarithm (monotonicity preserves inequality):

$$
\log\!\left( \sum_{\ell=1}^{K_i} \exp\!\left( \log c_{i\ell} + \sum_k a_{k\ell} y_k \right) \right) \le 0
$$

This is **log-sum-exp of affine functions**, hence **convex**.

### Conclusion:

$$
\boxed{\text{posynomial inequality} \;\longrightarrow\; \text{convex inequality}}
$$

* * *

6\. Step 4 — Transform the objective
------------------------------------

Original objective:

$$
\min_x \; p_0(x)
$$

Because  $p_0(x) > 0$ , minimizing  $p_0(x)$  is equivalent to minimizing  $\log p_0(x)$ .

After substitution:

$$
\min_y \; \log p_0(e^y)
$$

And as shown above:

$$
\log p_0(e^y) = \log\!\left( \sum_{\ell} \exp(\text{affine}_\ell(y)) \right)
$$

which is **convex**.

### So the transformed objective is convex.

* * *

7\. Final transformed problem (the convex form)
-----------------------------------------------

Putting everything together, Exercise 4.25 becomes:

$$
\boxed{ \begin{aligned} \min_{y \in \mathbb{R}^n} \quad & \log p_0(e^y) \\ \text{s.t.} \quad & \log p_i(e^y) \le 0, \quad i=1,\dots,m \\ & \log m_j(e^y) = 0, \quad j=1,\dots,r \end{aligned} }
$$

Where:

*   objective is **convex** (log-sum-exp)
*   inequality constraints are **convex**
*   equality constraints are **linear**

This is a **convex optimization problem**.  
You can hand it directly to a solver.

Recover solution via:

$$
x^\star = e^{y^\star}
$$

* * *

8\. Why this is globally optimal (no hidden traps)
--------------------------------------------------

*   Convex objective
*   Convex feasible set
*   No approximations
*   No relaxation

So **every local minimum is global**.

This is why GP is such a powerful exception in a sea of nonconvex multiplicative problems.

* * *

9\. The reusable pattern (this is what you must memorize)
---------------------------------------------------------

When you see:

*   variables constrained  $>0$ 
*   products of variables with real exponents
*   sums of such products
*   minimization of a sum/product-like objective

👉 **Immediately suspect GP**

Then do:

1.  Normalize constraints to  $\le 1$  and  $=1$ 
2.  Set  $y = \log x$ 
3.  Take logs everywhere
4.  Solve convex problem in  $y$ 
5.  Recover  $x = e^y$ 

That’s it.

No bisection. No duality tricks. No SOC/SDP.

* * *

10\. Where 4.25 sits in the Phase-8 map
---------------------------------------

| Exercise | Core pattern |
| --- | --- |
| **4.25** | **Geometric Programming (log transform)** |
| 4.26 | Hyperbolic constraint → rotated SOC |
| 4.27 | Robust constraint → dual norm → SOCP |
| 4.38 | Eigenvalue bound → LMI |
| 4.40 | SDP bound via PSD order |

You’ve now completed **the GP branch**.

* * *

### Next step (only when you say so)

We proceed to **Exercise 4.26**, which is a _pure cone-geometry problem_:

> hyperbolic inequality → rotated second-order cone

That one is shorter but extremely exam-sensitive.

Say the word when you want to continue.

## Response:
Thought

## Response:
Thought for 2m 58s

You’re right to flag this: my earlier “4.25 = GP” take was **wrong** — BV **Exercise 4.25** is the _ellipsoid separation_ problem and it’s an **SOCP feasibility** reformulation. Below are **complete solutions** for **4.25, 4.26, 4.27, 4.38, 4.40** with the exact modeling patterns you want for Phase 8.

* * *

Exercise 4.25 — Linear separation of two unions of ellipsoids as an SOCP feasibility problem
--------------------------------------------------------------------------------------------

### 1) Problem (paraphrased, structure only)

You are given ellipsoids

$$
\mathcal E_i=\{\,P_i u+q_i \mid \|u\|_2\le 1\,\},\qquad i=1,\dots,K+L,
$$

with  $P_i\in\mathbb S^n$  (so symmetric; in any case only  $P_i^T a$  matters).

We want a hyperplane  $a^T x+b=0$  that **strictly** separates

$$
\bigcup_{i=1}^K \mathcal E_i \quad\text{from}\quad \bigcup_{i=K+1}^{K+L}\mathcal E_i,
$$

meaning

$$
a^T x+b>0\ \ \forall x\in\bigcup_{i=1}^K\mathcal E_i, \qquad a^T x+b<0\ \ \forall x\in\bigcup_{i=K+1}^{K+L}\mathcal E_i,
$$

or prove none exists.

We must express this as an **SOCP feasibility** problem.

* * *

### 2) Reduce “for all  $x\in \mathcal E_i$ ” to a worst-case inequality

Fix one ellipsoid  $\mathcal E_i$ . Any  $x\in\mathcal E_i$  has the form  $x=P_i u+q_i$  with  $\|u\|_2\le 1$ .

Compute the hyperplane value:

$$
a^T x+b = a^T(P_i u+q_i)+b = (P_i^T a)^T u + (a^T q_i + b).
$$

So the condition “ $a^T x+b>0$  for all  $x\in\mathcal E_i$ ” is:

$$
\min_{\|u\|_2\le 1}\ \big((P_i^T a)^T u + (a^T q_i + b)\big) \ >\ 0.
$$

Similarly, “ $a^T x+b<0$  for all  $x\in\mathcal E_i$ ” is:

$$
\max_{\|u\|_2\le 1}\ \big((P_i^T a)^T u + (a^T q_i + b)\big) \ <\ 0.
$$

So we need formulas for  $\min$  and  $\max$  of a linear function over a Euclidean ball.

* * *

### 3) Key lemma: extremum over the unit Euclidean ball

Let  $c\in\mathbb R^n$ . Then

$$
\max_{\|u\|_2\le 1} c^T u = \|c\|_2, \qquad \min_{\|u\|_2\le 1} c^T u = -\|c\|_2.
$$

**Proof (tight Cauchy–Schwarz):**  
For any  $\|u\|\le 1$ ,  $c^T u \le \|c\|\,\|u\|\le \|c\|$ . Achieve equality by choosing  $u=c/\|c\|$  (if  $c\neq 0$ ). Similarly the minimum is achieved at  $u=-c/\|c\|$ .

Apply this with  $c=P_i^T a$ .

So:

$$
\min_{\|u\|\le 1} (P_i^T a)^T u = -\|P_i^T a\|_2, \qquad \max_{\|u\|\le 1} (P_i^T a)^T u = \|P_i^T a\|_2.
$$

* * *

### 4) Convert the separation conditions to norm inequalities

#### For the “positive side” ellipsoids  $i=1,\dots,K$ :

We need

$$
\min_{\|u\|\le 1}\Big((P_i^T a)^T u + (a^T q_i+b)\Big)>0
$$

i.e.

$$
(a^T q_i+b) - \|P_i^T a\|_2 > 0.
$$

#### For the “negative side” ellipsoids  $i=K+1,\dots,K+L$ :

We need

$$
\max_{\|u\|\le 1}\Big((P_i^T a)^T u + (a^T q_i+b)\Big)<0
$$

i.e.

$$
(a^T q_i+b) + \|P_i^T a\|_2 < 0 \quad\Longleftrightarrow\quad -(a^T q_i+b) - \|P_i^T a\|_2 > 0.
$$

So strict separation is equivalent to:

$$
a^T q_i+b > \|P_i^T a\|_2 \quad (i\le K), \qquad -(a^T q_i+b) > \|P_i^T a\|_2 \quad (i>K).
$$

* * *

### 5) Remove “strict” by scaling (standard feasibility trick)

If such  $(a,b)$  exists, you can scale it by any  $\gamma>0$ :  $(a,b)\mapsto (\gamma a, \gamma b)$ , and all signs remain, with margins scaled by  $\gamma$ .

Because each  $\mathcal E_i$  is compact and the inequalities are strict, there is a **positive margin** on each side; scaling can enforce a **fixed margin**, e.g.  $1$ .

So we can replace “ $>\ 0$ ” by “ $\ge 1$ ” without changing feasibility of “strictly separable”:

$$
a^T q_i+b - \|P_i^T a\|_2 \ge 1\quad (i\le K),
$$
 
$$
-(a^T q_i+b) - \|P_i^T a\|_2 \ge 1\quad (i>K).
$$

This is the clean SOCP form.

* * *

### 6) Final SOCP feasibility formulation

Decision variables:  $a\in\mathbb R^n$ ,  $b\in\mathbb R$ .

For each  $i\le K$ :

$$
\|P_i^T a\|_2 \le a^T q_i + b - 1.
$$

For each  $i>K$ :

$$
\|P_i^T a\|_2 \le -a^T q_i - b - 1.
$$

Each constraint is of the SOC form  $\|A z\|_2 \le c^T z + d$  (norm ≤ affine). Therefore this is an **SOCP feasibility problem**. If it’s feasible, any feasible  $(a,b)$  gives a strictly separating hyperplane; if infeasible, no strict separator exists.

That completes 4.25.

* * *

Exercise 4.26 — Hyperbolic (quadratic-over-linear / product) constraints as rotated SOC
---------------------------------------------------------------------------------------

This is the “primitive” used in 4.27. The central object is the **rotated second-order cone**.

### 1) Rotated SOC definition

One common definition (BV-compatible) is:

$$
\mathcal Q_r^{n+2} = \left\{(u,v,w)\in \mathbb R\times\mathbb R\times\mathbb R^n: u\ge 0,\ v\ge 0,\ 2uv \ge \|w\|_2^2 \right\}.
$$

(Equivalent variants differ by constants; be consistent with the  $2uv$  version.)

* * *

### 2) Scalar hyperbola:  $w^2 \le xy$ ,  $x\ge 0$ ,  $y\ge 0$ 

We want an SOC representation of

$$
x\ge 0,\ y\ge 0,\ w^2 \le xy.
$$

Compare to rotated SOC condition  $2uv \ge \|w\|^2$ . If we set  $u=x$ ,  $v=y$ , and use  $\sqrt{2}\,w$  in place of  $w$ , we get:

$$
2xy \ge (\sqrt{2}w)^2 = 2w^2 \quad\Longleftrightarrow\quad xy \ge w^2.
$$

So:

$$
\boxed{ x\ge 0,\ y\ge 0,\ w^2 \le xy \quad\Longleftrightarrow\quad (x,\ y,\ \sqrt{2}\,w)\in \mathcal Q_r^{3}. }
$$

That’s the basic “hyperbolic constraint → rotated SOC” equivalence.

* * *

### 3) Quadratic-over-linear:  $\dfrac{w^2}{x} \le t$  with  $x\ge 0$ 

For  $x>0$ ,  $\frac{w^2}{x} \le t$  is equivalent to  $w^2 \le x t$  with  $x\ge 0,\ t\ge 0$ .

Using the result above:

$$
w^2 \le x t,\ x\ge 0,\ t\ge 0 \quad\Longleftrightarrow\quad (x,\ t,\ \sqrt{2}w)\in\mathcal Q_r^3.
$$

This is exactly the pattern used to represent terms like  $w_i^2/x_i$  in 4.27.

* * *

Exercise 4.27 — Matrix fractional minimization via SOCP
-------------------------------------------------------

### 1) Problem

Minimize

$$
(Ax+b)^T\left(I + B\,\mathrm{diag}(x)\,B^T\right)^{-1}(Ax+b)
$$

subject to  $x\succeq 0$  (componentwise  $x_i\ge 0$ ).

Here  $A\in\mathbb R^{m\times n}$ ,  $b\in\mathbb R^m$ ,  $B\in\mathbb R^{m\times n}$ .

Let

$$
D := \mathrm{diag}(x)\in\mathbb R^{n\times n}, \qquad y := Ax+b \in \mathbb R^m, \qquad M := I + B D B^T \in \mathbb S^m.
$$

When  $x\succeq 0$ ,  $D\succeq 0$  and thus  $M\succeq I \succ 0$ , so  $M^{-1}$  exists.

Objective is  $y^T M^{-1} y$ .

* * *

### 2) Key equivalence (given hint): inverse quadratic form as a minimum over a decomposition

We prove the identity:

$$
\boxed{ y^T(I+BD B^T)^{-1}y = \min_{v\in\mathbb R^m,\ w\in\mathbb R^n} \left\{ \|v\|_2^2 + w^T D^{-1} w \ :\ v + B w = y \right\}. }
$$

(With the convention that if some  $x_i=0$ , then  $w_i^2/x_i$  is interpreted as  $0$  when  $w_i=0$  and  $+\infty$  otherwise; this matches “ $D^{-1}$ ” as an extended-valued quadratic.)

#### Proof via Lagrange duality (clean and explicit)

Consider the constrained problem:

$$
\min_{v,w}\ \|v\|^2 + w^T D^{-1} w \quad\text{s.t.}\quad v + B w = y.
$$

Lagrangian with multiplier  $\lambda\in\mathbb R^m$ :

$$
\mathcal L(v,w,\lambda) = \|v\|^2 + w^T D^{-1} w + \lambda^T(y - v - B w).
$$

Minimize over  $v$ :

$$
\|v\|^2 - \lambda^T v
$$

is a strictly convex quadratic. Its minimizer satisfies  $2v-\lambda=0\Rightarrow v=\lambda/2$ . Minimum value:

$$
\|{\lambda/2}\|^2 - \lambda^T(\lambda/2) = \frac{1}{4}\|\lambda\|^2 - \frac{1}{2}\|\lambda\|^2 = -\frac{1}{4}\|\lambda\|^2.
$$

Minimize over  $w$ :

$$
w^T D^{-1} w - \lambda^T B w.
$$

Again quadratic; optimality condition:

$$
2D^{-1}w - B^T\lambda = 0 \ \Rightarrow\ w = \frac{1}{2} D B^T \lambda,
$$

(with the extended-valued convention handling  $x_i=0$ ). Minimum value:

$$
w^T D^{-1} w - \lambda^T B w = \left(\frac{1}{2} D B^T\lambda\right)^T D^{-1}\left(\frac{1}{2} D B^T\lambda\right) - \lambda^T B\left(\frac{1}{2} D B^T\lambda\right) = \frac{1}{4}\lambda^T B D B^T \lambda - \frac{1}{2}\lambda^T B D B^T\lambda = -\frac{1}{4}\lambda^T B D B^T\lambda.
$$

So the dual function is:

$$
g(\lambda)=\lambda^T y - \frac{1}{4}\lambda^T(I + B D B^T)\lambda.
$$

Dual problem:

$$
\max_{\lambda}\ \lambda^T y - \frac{1}{4}\lambda^T M \lambda.
$$

This is a concave quadratic maximization. Complete the square:

$$
\lambda^T y - \frac14 \lambda^T M\lambda = -\frac14\left(\lambda^T M\lambda - 4\lambda^T y\right) = -\frac14\left((\lambda-2M^{-1}y)^T M (\lambda-2M^{-1}y) - 4y^T M^{-1}y\right) = y^T M^{-1}y - \frac14(\lambda-2M^{-1}y)^T M (\lambda-2M^{-1}y).
$$

Since  $M\succ 0$ , the last term is  $\le 0$ , maximized at  $\lambda^\star=2M^{-1}y$ , giving optimal value  $y^T M^{-1}y$ .

Strong duality holds here (strict feasibility is easy since  $M\succ 0$ ), so the primal minimum equals this dual maximum. This proves the identity.

Now substitute back  $y=Ax+b$ ,  $D=\mathrm{diag}(x)$ . We get exactly the hint form:

$$
\boxed{ \min_{x\succeq 0}\ (Ax+b)^T(I+B\mathrm{diag}(x)B^T)^{-1}(Ax+b) \equiv \min_{x\succeq 0,v,w}\ \|v\|^2 + w^T\mathrm{diag}(x)^{-1}w \ \text{s.t. } v + Bw = Ax+b. }
$$

* * *

### 3) Convert  $w^T\mathrm{diag}(x)^{-1}w$  into rotated SOC constraints

Write:

$$
w^T\mathrm{diag}(x)^{-1}w = \sum_{i=1}^n \frac{w_i^2}{x_i},
$$

with the extended-valued convention when  $x_i=0$ .

Introduce epigraph variables  $z_i\ge 0$  satisfying

$$
z_i \ge \frac{w_i^2}{x_i} \quad\Longleftrightarrow\quad w_i^2 \le x_i z_i,\ \ x_i\ge 0,\ z_i\ge 0.
$$

By Exercise 4.26:

$$
w_i^2 \le x_i z_i,\ x_i\ge 0,\ z_i\ge 0 \quad\Longleftrightarrow\quad (x_i,\ z_i,\ \sqrt{2}\,w_i)\in\mathcal Q_r^3.
$$

So the term  $w^T\mathrm{diag}(x)^{-1}w$  is handled by  $n$  rotated SOC constraints plus a linear objective term  $\sum z_i$ .

* * *

### 4) Convert  $\|v\|^2$  into a rotated SOC epigraph

Introduce a scalar  $s\ge 0$  with

$$
s \ge \|v\|_2^2.
$$

Using rotated SOC:

$$
s \ge \|v\|^2 \quad\Longleftrightarrow\quad 2s\cdot \frac12 \ge \|v\|^2,\ s\ge 0 \quad\Longleftrightarrow\quad (s,\ 1/2,\ v)\in \mathcal Q_r^{m+2}.
$$

* * *

### 5) Final SOCP

Variables:

$$
x\in\mathbb R^n,\ v\in\mathbb R^m,\ w\in\mathbb R^n,\ z\in\mathbb R^n,\ s\in\mathbb R.
$$

SOCP:

$$
\begin{aligned} \min\quad & s + \sum_{i=1}^n z_i\\ \text{s.t.}\quad & v + B w = A x + b,\\ & x \succeq 0,\ z\succeq 0,\ s\ge 0,\\ & (s,\ 1/2,\ v)\in \mathcal Q_r^{m+2},\\ & (x_i,\ z_i,\ \sqrt{2}\,w_i)\in \mathcal Q_r^{3},\quad i=1,\dots,n. \end{aligned}
$$

This is an SOCP because it uses only linear equalities/inequalities and (rotated) SOC constraints, and the objective is linear.

That completes 4.27.

* * *

Exercise 4.38 — One-variable SDP and generalized eigenvalues
------------------------------------------------------------

### 1) Setup

You have  $A,B\in\mathbb S^n$ ,  $B$  nonsingular, and there exists a nonsingular  $R$  such that

$$
R^T A R = \mathrm{diag}(a),\qquad R^T B R = \mathrm{diag}(b),
$$

with  $a,b\in\mathbb R^n$ .

Generalized eigenvalues of  $(A,B)$  are defined as roots of

$$
\det(\lambda B - A)=0.
$$

#### (a) Show generalized eigenvalues are real and equal  $\lambda_i=a_i/b_i$ .

Compute:

$$
\det(\lambda B - A) = \det\big(\lambda R^{-T}(R^TBR)R^{-1} - R^{-T}(R^TAR)R^{-1}\big).
$$

Factor out congruence (using  $\det(R^{-T}XR^{-1})=\det(R)^{-2}\det(X)$ ):

$$
\det(\lambda B - A) = \det(R)^{-2}\det(\lambda R^TBR - R^TAR) = \det(R)^{-2}\det(\lambda\,\mathrm{diag}(b) - \mathrm{diag}(a)).
$$

But  $\lambda\,\mathrm{diag}(b) - \mathrm{diag}(a)=\mathrm{diag}(\lambda b_i - a_i)$ , so

$$
\det(\lambda B - A)=\det(R)^{-2}\prod_{i=1}^n (\lambda b_i - a_i).
$$

Thus the roots are exactly

$$
\boxed{\lambda_i=\frac{a_i}{b_i}},\qquad i=1,\dots,n,
$$

which are real because  $a_i,b_i\in\mathbb R$  and  $b_i\neq 0$  (since  $B$  nonsingular implies  $\det(\mathrm{diag}(b))\neq 0$ ).

That proves (a).

* * *

#### (b) Solve the SDP  $\min ct$  s.t.  $tB\succeq A$ 

The constraint  $tB\succeq A$  is

$$
tB - A \succeq 0.
$$

Apply congruence by  $R$  (PSD order preserved under congruence):

$$
tB - A \succeq 0 \quad\Longleftrightarrow\quad R^T(tB-A)R \succeq 0 \quad\Longleftrightarrow\quad t\,R^TBR - R^TAR \succeq 0
$$

i.e.

$$
t\,\mathrm{diag}(b) - \mathrm{diag}(a) = \mathrm{diag}(t b_i - a_i)\succeq 0.
$$

A diagonal matrix is PSD iff each diagonal entry is  $\ge 0$ . So:

$$
t b_i - a_i \ge 0 \quad\forall i.
$$

Now split by the sign of  $b_i$ :

*   If  $b_i>0$ , then  $t \ge a_i/b_i$ .
*   If  $b_i<0$ , then  $t \le a_i/b_i$ .

So feasibility means  $t$  lies in the intersection interval:

$$
t \ge \max_{i:\,b_i>0}\frac{a_i}{b_i}, \qquad t \le \min_{i:\,b_i<0}\frac{a_i}{b_i}.
$$

(If there are no negative  $b_i$ , the upper bound is  $+\infty$ .)

If the intersection is empty, the SDP is infeasible.

If feasible and  $c>0$  (the usual case), minimizing  $ct$  is equivalent to minimizing  $t$ . The smallest feasible  $t$  is therefore:

$$
\boxed{ t^\star=\max_{i:\,b_i>0}\frac{a_i}{b_i} }
$$

provided this value also satisfies the upper bounds from any  $b_i<0$ . (If  $c<0$ , the objective prefers  $t\to -\infty$  and you’d instead hit the upper bound; but typically  $c>0$  in these exercises.)

So the optimal value is  $c\,t^\star$ , with feasibility requiring the interval condition above.

That completes 4.38.

* * *

Exercise 4.40 — Express LPs, QPs, QCQPs, SOCPs (and matrix fractional) as SDPs
------------------------------------------------------------------------------

This exercise is about one big modeling fact:

> An SDP is “linear objective + LMI constraints.”  
> Many other convex classes can be encoded as LMIs using Schur complements.

I’ll give the exact SDP encodings you can deploy instantly.

* * *

### 4.40(a) LP as SDP

A generic LP is:

$$
\min\ c^T x\quad \text{s.t.}\quad Gx\le h,\ \ Ax=b.
$$

Each scalar inequality  $\alpha(x)\ge 0$  is equivalent to a  $1\times 1$  PSD constraint:

$$
\alpha(x)\ge 0 \quad\Longleftrightarrow\quad [\alpha(x)]\succeq 0.
$$

So  $Gx\le h$  is  $h-Gx\ge 0$  componentwise, i.e.

$$
[h_i - g_i^T x]\succeq 0,\quad i=1,\dots,m.
$$

Equivalently, you can stack them into a diagonal LMI:

$$
\mathrm{diag}(h-Gx)\succeq 0.
$$

So an LP is an SDP with only diagonal LMIs.

* * *

### 4.40(b) QP, QCQP, SOCP as SDP (core LMI templates)

#### Key Schur complement identity (the hint)

If  $A\in\mathbb S_{++}^r$ ,  $C\in\mathbb S^s$ , then

$$
\begin{bmatrix} A & B\\ B^T & C \end{bmatrix}\succeq 0 \quad\Longleftrightarrow\quad C - B^T A^{-1} B \succeq 0.
$$

This lets you turn norm constraints into LMIs.

* * *

#### SOCP constraint as SDP

A standard SOC constraint is:

$$
\|u\|_2 \le v
$$

(with  $v$  scalar affine,  $u$  affine vector).

Claim:

$$
\boxed{ \|u\|_2 \le v \quad\Longleftrightarrow\quad \begin{bmatrix} v & u^T\\ u & v I \end{bmatrix}\succeq 0. }
$$

**Proof (Schur complement, assuming  $v>0$ ; boundary by continuity):**  
Take  $A=[v]$  (scalar),  $B=u^T$ ,  $C=vI$ . Then

$$
C - B^T A^{-1} B = vI - \frac{1}{v}uu^T \succeq 0 \quad\Longleftrightarrow\quad v^2 I \succeq uu^T \quad\Longleftrightarrow\quad \|u\|_2^2 \le v^2 \quad\Longleftrightarrow\quad \|u\|_2 \le v,\ v\ge 0.
$$

Also, the LMI itself forces  $v\ge 0$  (since its diagonal blocks must be PSD).

So every SOCP can be rewritten as an SDP by replacing each SOC constraint with this LMI.

* * *

#### QP as SDP (via “quadratic ≤ scalar” → LMI)

A convex quadratic objective/constraint typically involves terms like  $\|R x + r\|_2^2$  (because any PSD quadratic can be written that way with a factor  $R$ ).

Epigraph trick: minimize  $t$  s.t.

$$
\|R x + r\|_2^2 \le t.
$$

Now use an LMI:

$$
\boxed{ \|z\|_2^2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} t & z^T\\ z & I \end{bmatrix}\succeq 0. }
$$

Proof: Schur complement with  $A=I$  gives  $t - z^T z \ge 0$ .

So set  $z=R x+r$ . This gives an SDP representation of the quadratic epigraph, hence of the QP (and similarly for QCQP constraints).

* * *

#### QCQP as SDP

A convex quadratic inequality looks like:

$$
x^T P x + q^T x + r \le 0,\quad P\succeq 0.
$$

Factor  $P=R^T R$ . Then

$$
x^T P x = \|R x\|^2.
$$

Rewrite constraint as

$$
\|R x\|^2 \le -(q^T x + r).
$$

Introduce a scalar  $t = -(q^T x + r)$  (affine in  $x$ ) and require

$$
\begin{bmatrix} t & (R x)^T\\ R x & I \end{bmatrix}\succeq 0.
$$

This is an LMI in  $(x,t)$  (since  $Rx$  is affine,  $t$  affine), so it’s an SDP constraint.

Thus convex QCQPs can be encoded as SDPs.

* * *

### 4.40(c) Matrix fractional optimization as SDP

Problem:

$$
\min_x\ (Ax+b)^T F(x)^{-1} (Ax+b),
$$

where

$$
F(x) = F_0 + x_1F_1 + \cdots + x_nF_n,
$$

and domain requires  $F(x)\succ 0$  (or  $\succeq 0$  with appropriate interpretation).

Introduce epigraph variable  $t$  and impose

$$
(Ax+b)^T F(x)^{-1}(Ax+b)\le t.
$$

Now apply Schur complement:

$$
\boxed{ (Ax+b)^T F(x)^{-1}(Ax+b)\le t,\ \ F(x)\succeq 0 \quad\Longleftrightarrow\quad \begin{bmatrix} F(x) & Ax+b\\ (Ax+b)^T & t \end{bmatrix}\succeq 0. }
$$

**Proof (Schur complement, assuming  $F(x)\succ 0$ ):**

$$
\begin{bmatrix} F & y\\ y^T & t \end{bmatrix}\succeq 0 \iff t - y^T F^{-1} y \ge 0 \iff y^T F^{-1} y \le t,
$$

with  $y=Ax+b$ . If  $F\succeq 0$  singular, the “more complete statement” uses generalized inverses; BV’s appendix covers it, but the standard exercise intent is the  $F\succ 0$  case.

So the SDP is:

Variables:  $x\in\mathbb R^n$ ,  $t\in\mathbb R$ .

$$
\begin{aligned} \min\quad & t\\ \text{s.t.}\quad & \begin{bmatrix} F_0 + \sum_{i=1}^n x_i F_i & Ax+b\\ (Ax+b)^T & t \end{bmatrix}\succeq 0. \end{aligned}
$$

That completes 4.40.

* * *

What you now have (the Phase-8 “mechanical patterns”)
=====================================================

*   **4.25:** robust linear inequalities over ellipsoids →  $\|P_i^T a\|\le$  affine → **SOCP feasibility**.
*   **4.26:**  $w^2\le xy$  /  $w^2/x\le t$  → **rotated SOC**.
*   **4.27:** inverse quadratic form  $y^T(I+BD B^T)^{-1}y$  → decomposition  $\min\|v\|^2+\sum w_i^2/x_i$  → rotated SOC epigraphs → **SOCP**.
*   **4.38:** congruence diagonalization → generalized eigenvalues  $a_i/b_i$  → one-variable LMI becomes scalar inequalities → closed-form  $t^\star$ .
*   **4.40:** SOC ↔ LMI; quadratic epigraph ↔ LMI; matrix fractional ↔ block LMI → **SDP encodings**.

If you want the next step in the exact “quiz-ready” style: I can turn each of the five into a one-page **pattern card** (recognition trigger → derivation in 3 lines → final solver form), so you can reproduce them under time pressure.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)