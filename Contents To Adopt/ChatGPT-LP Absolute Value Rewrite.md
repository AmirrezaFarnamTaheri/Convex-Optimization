# LP Absolute Value Rewrite

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/25/2025 20:42:59  
**Updated:** 12/25/2025 21:04:08  
**Exported:** 12/29/2025 0:13:39  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/694d706f-7d68-8328-a696-4e6adb97d806](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/694d706f-7d68-8328-a696-4e6adb97d806)  

## Response:
Good. Let’s slow this down even further, strip it to bedrock, and then rebuild it so cleanly that it becomes _mechanical_, not clever. I’ll repeat ideas from multiple angles on purpose; that redundancy is how this becomes reflex instead of a fragile trick.

What follows is not just “how to rewrite absolute values,” but **why this rewrite is inevitable** once you understand what LPs are allowed to express.

* * *

Phase 5.1 — Absolute values → linear constraints
------------------------------------------------

_(The most important LP modeling atom you will ever learn)_

### Big picture first (why this even exists)

A **linear program** lives in a very narrow universe. It only understands:

• linear functions  
• linear inequalities (halfspaces)  
• intersections of halfspaces (polyhedra)

That’s it. No curves. No bends. No kinks. No conditionals.

Absolute value looks innocent, but it secretly contains **a kink**. That kink is exactly what breaks linearity. Phase 5.1 is about learning how to _hide the kink_ using extra variables, without changing the meaning of the problem.

If you master this, LP modeling stops feeling like magic and starts feeling like algebraic plumbing.

* * *

0) What LPs can and cannot say (crystal clear)
----------------------------------------------

An LP may contain:

• Objective:

$$
\min c^\top x
$$

• Constraints:

$$
Ax \le b, \quad A_{\text{eq}}x = b_{\text{eq}}
$$

Each constraint is a **single linear inequality**. Geometrically: a halfspace.

An LP cannot directly contain:

• max  
• min  
• absolute value  
• products of variables  
• powers (squares, roots, etc.)

So whenever you see `|·|`, your brain should immediately fire:

> “This is illegal. I must rewrite.”

Phase 5.1 gives the atomic rewrite.

* * *

1) Absolute value, dismantled completely
----------------------------------------

### 1.1 Definition (no shortcuts)

For a real scalar  $u$ :

$$
|u| = \begin{cases} u & \text{if } u \ge 0 \\ -u & \text{if } u < 0 \end{cases}
$$

This definition is **piecewise**. That’s the problem. LPs do not do “if / else.”

Now rewrite it in a form LP _can_ reason about:

$$
|u| = \max(u,\,-u)
$$

This is the key insight. Absolute value is the **maximum of two linear functions**.

•  $u$  is linear  
•  $-u$  is linear  
• the maximum is convex but not linear

LPs cannot compute the maximum directly, but they _can_ represent its **epigraph**. That word matters.

* * *

2) The atomic equivalence: the heart of Phase 5.1
-------------------------------------------------

### The statement (memorize this)

For real scalars  $u$  and  $s$ :

$$
\boxed{|u| \le s \quad \Longleftrightarrow \quad -s \le u \le s}
$$

This is not a trick. It is a **logical equivalence**.

Everything in Phase 5.1 is just this statement, applied again and again.

* * *

3) Proof — brutally explicit, no intuition gaps
-----------------------------------------------

We prove both directions because LP modeling requires logical equivalence, not just plausibility.

* * *

### Direction 1:

$$
|u| \le s \;\Rightarrow\; -s \le u \le s
$$

Start with the premise:

$$
|u| \le s
$$

First observation:

$$
|u| \ge 0 \Rightarrow s \ge 0
$$

If  $s < 0$ , the constraint is infeasible. This matters later when  $s$  is a variable.

Now we prove the two inequalities separately.

#### Show  $u \le s$ 

Case analysis on the sign of  $u$ :

• If  $u \ge 0$ :  
 $|u| = u \le s$ 

• If  $u < 0$ :  
 $u \le 0 \le s$ 

So in all cases:

$$
u \le s
$$

#### Show  $-s \le u$ 

• If  $u \ge 0$ :  
 $-s \le 0 \le u$ 

• If  $u < 0$ :  
 $|u| = -u \le s \Rightarrow -u \le s$   
Multiply both sides by  $-1$  (inequality flips):

$$
u \ge -s
$$

So again:

$$
-s \le u
$$

Combining:

$$
-s \le u \le s
$$

* * *

### Direction 2:

$$
-s \le u \le s \;\Rightarrow\; |u| \le s
$$

Again split by sign:

• If  $u \ge 0$ :  
 $|u| = u \le s$ 

• If  $u < 0$ :  
 $-s \le u \Rightarrow -u \le s \Rightarrow |u| \le s$ 

Thus:

$$
|u| \le s
$$

QED. No geometry, no intuition shortcuts. Just logic.

* * *

4) LP-ready form (what you actually write)
------------------------------------------

The inequality

$$
-s \le u \le s
$$

is equivalent to **two linear inequalities**:

$$
\boxed{ \begin{aligned} u &\le s \\ -\,u &\le s \end{aligned} }
$$

This is the _atomic LP representation_ of an absolute value bound.

Whenever you see `|u|`, your hands should automatically write those two lines.

* * *

5) The epigraph viewpoint (this is the real reason it works)
------------------------------------------------------------

This section explains **why LPs can handle absolute value at all**, despite it being nonlinear.

### 5.1 Epigraph definition

The epigraph of a function  $f(u)$  is:

$$
\operatorname{epi}(f) = \{(u,s) : f(u) \le s\}
$$

For  $f(u) = |u|$ :

$$
\operatorname{epi}(|\cdot|) = \{(u,s) : |u| \le s\}
$$

Using the atom:

$$
\operatorname{epi}(|\cdot|) = \{(u,s) : u \le s,\ -u \le s\}
$$

That is the **intersection of two halfspaces** in  $(u,s)$ \-space.

Intersection of halfspaces ⇒ polyhedron  
Polyhedron ⇒ LP-representable

That’s the deep reason. Not algebra. Geometry.

The function is nonlinear, but its epigraph is **flat-sided**.

* * *

6) The universal modeling recipe (do this blindly)
--------------------------------------------------

Whenever you encounter `|something|` in an LP context:

1.  **Name the inside**
    $$
    u := \text{that affine expression}
    $$
2.  **Introduce a new variable**
    $$
    s \quad \text{(intended to represent } |u|)
    $$
3.  **Add the two inequalities**
    $$
    u \le s,\quad -u \le s
    $$
4.  **Replace every appearance of `|u|` with `s`**

That’s it. No creativity. No interpretation.

This is called:  
• epigraph reformulation  
• lifting  
• auxiliary-variable modeling

All the same idea.

* * *

7) Absolute value in constraints
--------------------------------

Example:

$$
|a^\top x + b| \le t
$$

Here  $a^\top x + b$  is affine. Good.

Rewrite:

$$
\begin{aligned} a^\top x + b &\le t \\ -(a^\top x + b) &\le t \end{aligned}
$$

If  $t$  is a constant → pure LP constraints  
If  $t$  is a variable → still linear

Nothing nonlinear has been introduced.

* * *

8) Absolute value in objectives (epigraph trick)
------------------------------------------------

Original problem:

$$
\min_x |a^\top x + b|
$$

Illegal objective.

### Step-by-step repair

1.  Introduce a variable  $t$ 
2.  Minimize  $t$ 
3.  Constrain it to dominate the absolute value
    
$$
\begin{aligned} \min_{x,t} \quad & t \\ \text{s.t.} \quad & a^\top x + b \le t \\ & -(a^\top x + b) \le t \end{aligned}
$$

### Why this is equivalent (no handwaving)

Fix any  $x$ . The feasible values of  $t$  satisfy:

$$
t \ge |a^\top x + b|
$$

The smallest feasible  $t$  is exactly:

$$
t = |a^\top x + b|
$$

Since the objective minimizes  $t$ , the inequality becomes tight at optimum.

Thus the optimizer picks the same  $x$  as the original problem.

* * *

9) Equality to absolute value is fake — and unnecessary
-------------------------------------------------------

Never write:

$$
s = |u|
$$

That equality is nonlinear and useless to LPs.

Correct modeling is:

$$
s \ge |u|
$$

Which becomes:

$$
u \le s,\quad -u \le s
$$

Then the objective forces tightness.

This is a **general modeling principle**:

> Inequalities define feasible structure.  
> Objectives enforce equality at optimality.

* * *

10) Multiple absolute values (preview of 5.2, but same atom)
------------------------------------------------------------

Example:

$$
\min_x \sum_{i=1}^m |a_i^\top x - b_i|
$$

Introduce  $s_i$  for each term:

$$
\begin{aligned} \min_{x,s} \quad & \sum_{i=1}^m s_i \\ \text{s.t.} \quad & a_i^\top x - b_i \le s_i \\ & -(a_i^\top x - b_i) \le s_i \end{aligned}
$$

That is a pure LP.

This is **least absolute deviations regression** in disguise.

* * *

11) Edge cases and exam traps (read carefully)
----------------------------------------------

### Trap 1: Dropping one inequality

Wrong:

$$
|u| \le s \Rightarrow u \le s
$$

This ignores negative  $u$ .

Always two inequalities. Always.

* * *

### Trap 2: Non-affine inside

If  $u = x^2$ , then:

$$
x^2 \le s
$$

is **not linear**. The atom is logically true but not LP-representable.

Phase 5.1 only works when the inside is affine.

* * *

### Trap 3: Forgetting  $s \ge 0$ 

Often redundant, but sometimes necessary to avoid nonsense reasoning.

Clean formulations usually include:

$$
s \ge 0
$$

* * *

### Trap 4: Confusing scalar vs vector absolute value

• Scalar: Phase 5.1 (LP)  
• Vector norms: Phase 5.2 (LP / SOCP depending on norm)

* * *

12) Mental summary (burn this in)
---------------------------------

Absolute value is illegal in LPs.

But:

• `|u| ≤ s`  
• is equivalent to  
• two linear inequalities  
• which define a polyhedron  
• whose geometry exactly matches the absolute value epigraph

Everything else is bookkeeping.

* * *

Phase 5.1 is not a trick.  
It is the **DNA** of LP modeling.

Phase 5.2 will stack this atom into norms and maxima. Phase 5.3 will show where LP breaks and SOCP takes over. But everything traces back to this single equivalence.

Once this is automatic, LP modeling becomes mechanical rather than clever.

## Response:
Alright. We’re going to take Phase 5.1 and squeeze every last drop of meaning out of it: logic, geometry, polyhedral/LP representability, projection (“lifting”), tightness at optimum, standard-form conversion, and the exact “why this is the _only_ reasonable LP encoding” story.

I’m going to be intentionally verbose and repetitive in a structured way: first principles → equivalence → geometric meaning → modeling templates → correctness proofs (feasible set + optimal value) → edge cases → “mechanical compiler” rules.

* * *

Phase 5.1 — Absolute value → linear constraints (LP modeling atom), ultra-unpacked
==================================================================================

0) What “LP modeling atom” really means
---------------------------------------

An “atom” here means: a small rewrite rule that you can apply locally to a piece of an optimization model, and it has these properties:

1.  **Semantic correctness**: it does not change the meaning (feasible set / optimal value / optimal solutions) once used properly.
2.  **Syntactic legality**: the result fits LP syntax (linear objective + linear constraints).
3.  **Composability**: you can apply it repeatedly to larger expressions (sum of absolute values, max of absolute values, piecewise linear functions, robust constraints, etc).

Phase 5.1 is the atom for the absolute value.

* * *

1) Absolute value from bedrock
==============================

Let  $u \in \mathbb{R}$ . The absolute value is:

$$
|u| = \begin{cases} u & \text{if } u \ge 0\\ -u & \text{if } u < 0 \end{cases}
$$

This is **not** linear because it is **piecewise**. Linear functions cannot “switch formulas” depending on sign.

Two crucial alternative characterizations:

### 1.1 Max-of-two-linear form (convexity + polyhedral epigraph)

$$
|u| = \max\{u,\, -u\}.
$$

This is the single most useful identity for modeling.

### 1.2 Smallest nonnegative number dominating both  $u$  and  $-u$ 

Equivalently:

>  $|u|$  is the **smallest** real number  $s$  such that  $s \ge u$  and  $s \ge -u$ .

That sentence is basically the modeling rule already.

* * *

2) The core equivalence:  $|u|\le s$  ⇔ two linear inequalities
===============================================================

2.1 Statement (the atom)
------------------------

For real scalars  $u, s$ :

$$
\boxed{|u| \le s \iff (u \le s \text{ and } -u \le s).}
$$

You also often see it written as:

$$
|u| \le s \iff -s \le u \le s.
$$

Same thing; “ $-s \le u$ ” is equivalent to “ $-u \le s$ ”.

The LP-ready form is the **two inequalities**:

$$
\boxed{u \le s,\quad -u \le s.}
$$

2.2 Proof, but even more explicit than before
---------------------------------------------

We prove:

$$
|u| \le s \iff (u \le s \wedge -u \le s).
$$

### (⇒) Assume  $|u| \le s$ . Show  $u \le s$  and  $-u \le s$ .

We use the trivial fact:

$$
|u| \ge u \quad \text{and} \quad |u| \ge -u.
$$

Why are those true? Check both sign cases:

*   If  $u\ge 0$ :  $|u|=u \ge u$  and  $|u|=u \ge -u$  because  $u\ge 0 \Rightarrow u \ge -u$ .
*   If  $u<0$ :  $|u|=-u \ge u$  because  $-u > 0 > u$ . Also  $|u|=-u \ge -u$  trivially.

So indeed:

$$
|u| \ge u,\qquad |u| \ge -u.
$$

Now since  $|u|\le s$ , we chain inequalities:

*   From  $u \le |u| \le s$ , we get  $u \le s$ .
*   From  $-u \le |u| \le s$ , we get  $-u \le s$ .

Done.

### (⇐) Assume  $u \le s$  and  $-u \le s$ . Show  $|u|\le s$ .

Since  $|u|=\max\{u,-u\}$ , and we assumed both  $u \le s$  and  $-u \le s$ , the maximum of them is also ≤  $s$ :

$$
|u| = \max\{u,-u\} \le s.
$$

Done.

That proof is “modeler’s proof”: it uses max and domination directly, which is exactly what LP can encode (domination by linear inequalities).

* * *

3) Hidden but crucial domain fact: why  $s\ge 0$  shows up
==========================================================

From definition,  $|u|\ge 0$  always. So if  $|u|\le s$ , then necessarily  $s\ge 0$ .

In the two-inequality representation, does  $s\ge 0$  follow automatically? Yes:

If  $u \le s$  and  $-u \le s$ , then add them:

$$
u + (-u) \le s + s \Rightarrow 0 \le 2s \Rightarrow s \ge 0.
$$

So **for the pure constraint**  $|u|\le s$ ,  $s\ge 0$  is redundant. But people still include it because:

*   It makes interpretation clear (“ $s$  is a magnitude”).
*   It prevents confusion in more complex models where  $s$  appears elsewhere.
*   It helps humans (and sometimes solvers) avoid silly intermediate reasoning.

* * *

4) Geometry: the epigraph is a polyhedron (this is why LP can do it)
====================================================================

4.1 Epigraph definition
-----------------------

For a function  $f:\mathbb{R}\to\mathbb{R}$ ,

$$
\mathrm{epi}(f)=\{(u,s)\in\mathbb{R}^2: f(u)\le s\}.
$$

For  $f(u)=|u|$ :

$$
\mathrm{epi}(|\cdot|)=\{(u,s): |u|\le s\}.
$$

Apply the atom:

$$
\mathrm{epi}(|\cdot|)=\{(u,s): u\le s,\ -u\le s\}.
$$

That is the intersection of two halfspaces:

*   Halfspace 1:  $s-u \ge 0$  (above the line  $s=u$ )
*   Halfspace 2:  $s+u \ge 0$  (above the line  $s=-u$ )

Intersection of finitely many halfspaces = **polyhedron** = LP representable.

4.2 Why this matters beyond pretty geometry
-------------------------------------------

A key modeling theorem (informal but correct):

> LPs can represent exactly those feasible sets that are polyhedra (intersection of finitely many linear inequalities/equalities).

So the reason absolute value is “LP-friendly” is not because absolute value is linear (it isn’t), but because the _set_  $\{(u,s): |u|\le s\}$  is a polyhedron.

This is the correct mental model:

*   Absolute value function: nonlinear
*   Epigraph of absolute value: polyhedral
*   LP works with polyhedra
*   Therefore LP can model absolute value constraints/objectives via epigraph lifting

* * *

5) “Lifting” and “projection”: how we legally add variables without changing the problem
========================================================================================

This is the part that many people handwave; we’ll do it carefully.

5.1 The idea
------------

Original problem has variables  $x$ . You introduce an auxiliary variable  $s$ . Now the problem is in  $(x,s)$ \-space, which is higher-dimensional. Why is that okay?

Because you only care about the induced feasible set in  $x$ \-space after you “forget”  $s$ . That is a **projection**.

Formally: if  $F \subseteq \mathbb{R}^{n+m}$  is feasible set in  $(x,s)$ , the feasible set in  $x$  alone is:

$$
\{x : \exists s \text{ such that } (x,s)\in F\}.
$$

LP modeling often works by:

1.  create a simple polyhedron in higher dimension,
2.  whose projection matches the original complicated set.

For absolute value:

*   the “complicated” set in  $(x)$  might be described by  $|a^\top x+b|\le t$ ,
*   the “simple” set in  $(x,t)$  is the intersection of two halfspaces.

This is why the method scales: it’s geometric.

* * *

6) Absolute value inside constraints: full correctness argument
===============================================================

Take a standard pattern:

$$
|a^\top x + b| \le t
$$

where  $a^\top x+b$  is affine in  $x$ .

Define:

$$
u(x) := a^\top x + b.
$$

Then:

$$
|u(x)|\le t \iff u(x)\le t \ \text{and}\ -u(x)\le t.
$$

Written explicitly:

$$
a^\top x + b \le t,
$$
 
$$
-(a^\top x + b)\le t \iff -a^\top x - b \le t.
$$

Both are linear inequalities in  $(x,t)$ . So if  $t$  is a variable, still LP; if  $t$  is constant, still LP.

Correctness is immediate because we used a logical equivalence for each  $(x,t)$  point.

* * *

7) Absolute value in the objective: full equivalence proof (feasible set + optimal value)
=========================================================================================

Original problem:

$$
\min_{x\in X} |a^\top x + b|
$$

where  $X$  is some LP-feasible set (polyhedron):  $X=\{x: A x \le d\}$ , etc.

LP reformulation:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad x\in X,\quad |a^\top x+b|\le t.
$$

Then use atom:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad x\in X, \quad a^\top x+b\le t, \quad -(a^\top x+b)\le t.
$$

Now the rigorous equivalence:

7.1 For any fixed  $x$ , characterize feasible  $t$ 
----------------------------------------------------

Fix  $x$ . Define  $y:=a^\top x+b$  (a scalar). The constraints become:

$$
y \le t,\quad -y \le t.
$$

This is equivalent to:

$$
t \ge \max\{y,-y\} = |y|.
$$

So the feasible set of  $t$  for that  $x$  is:

$$
\{t: t \ge |a^\top x + b|\}.
$$

Therefore, for each fixed  $x$ , the minimum possible  $t$  is exactly:

$$
t^*(x)=|a^\top x+b|.
$$

7.2 Now minimize over  $x$ 
---------------------------

The reformulated problem’s optimal value is:

$$
\min_{x\in X} t^*(x) = \min_{x\in X} |a^\top x+b|,
$$

which is exactly the original optimal value.

7.3 Relation of optimal solutions
---------------------------------

*   If  $x^\star$  solves original, then set  $t^\star=|a^\top x^\star+b|$ . That pair is feasible and achieves objective  $t^\star$ , so it solves the LP.
*   If  $(x^\star,t^\star)$  solves LP, then  $t^\star \ge |a^\top x^\star+b|$ . But if strict inequality held, you could reduce  $t^\star$  slightly and remain feasible (because constraints only require  $t$  to be ≥ that absolute value), contradicting optimality. So at optimum:
    
$$
t^\star = |a^\top x^\star+b|.
$$

Therefore  $x^\star$  must minimize the original objective as well.

So you get same optimal  $x$ , same optimal value, and tightness of the inequality is forced.

This is the “epigraph trick” in its fully formal form.

* * *

8) Why the “two inequalities” encoding is not arbitrary (it is essentially minimal)
===================================================================================

You might wonder: could there be another set of linear constraints equivalent to  $|u|\le s$ ? Sure, you could add redundant constraints, change basis, etc.

But conceptually, the representation:

$$
u\le s,\ -u\le s
$$

is minimal in the sense that:

*   the set  $\{(u,s): |u|\le s\}$  is a wedge with **two supporting lines**  $s=u$  and  $s=-u$ ,
*   you need at least those two halfspaces to carve out that wedge.

Drop one inequality and you get the wrong shape: a halfspace instead of a wedge (you lose one side of the “V”).

This “two faces” geometry explains why the algebra always produces two inequalities.

* * *

9) Elementwise absolute values (vector version) without confusing it with norms
===============================================================================

When you see  $|x|$  for a vector  $x\in\mathbb{R}^n$ , it is ambiguous in casual writing. In convex optimization modeling, common meanings:

### 9.1 Elementwise absolute value (vector)

$$
|x| := (|x_1|,\dots,|x_n|).
$$

To model  $|x|\le s$  elementwise, you do it per component:

$$
-x_i \le s_i,\quad x_i \le s_i,\quad i=1,\dots,n.
$$

All linear. This is still LP.

### 9.2 Norms (not the same thing)

 $\|x\|_2$  is the Euclidean norm → SOCP generally, not LP.  
 $\|x\|_1 = \sum_i |x_i|$  is sum of abs → LP using Phase 5.1 repeatedly.  
 $\|x\|_\infty = \max_i |x_i|$  is max of abs → LP using Phase 5.1 plus a “max epigraph” variable.

Phase 5.1 is the scalar atom that powers  $\ell_1$  and  $\ell_\infty$  LP representations.

* * *

10) Standard form details: how to fit this into “Ax ≤ b” cleanly
================================================================

Suppose  $u = a^\top x + b$  and you introduce  $s$ .

You write:

$$
a^\top x + b \le s \quad\Rightarrow\quad a^\top x - s \le -b
$$
 
$$
-(a^\top x + b)\le s \quad\Rightarrow\quad -a^\top x - s \le b
$$

So in matrix form, if your variables are  $(x,s)$ , these become rows in  $A$  and entries in  $b$ .

This matters in exams because they might ask for explicit  $A$  and  $b$ .

* * *

11) Concrete numerical sanity checks (so you _feel_ the equivalence)
====================================================================

Take  $u=-3$ .

*   True absolute value:  $|u|=3$ .

Constraint  $|u|\le s$  means  $3\le s$ .

Two inequalities:

*    $u\le s$  →  $-3 \le s$  (always true if  $s\ge 3$ , but not sufficient alone!)
*    $-u\le s$  →  $3 \le s$  (this is the binding one here)

So for negative  $u$ , the second inequality is the one that “catches” it. That’s exactly why dropping it is fatal.

Take  $u=+3$ .

*    $|u|=3$ , so again  $3\le s$ .
*   inequalities:
    *    $u\le s$  →  $3\le s$  (binding)
    *    $-u\le s$  →  $-3 \le s$  (slack)

So for positive  $u$ , the first inequality is binding.

That is the cleanest way to understand “two inequalities = cover both sign cases.”

* * *

12) Common failure modes, but explained more deeply
===================================================

### Failure 1: “Let s = |u|” (wrong mindset)

In LP you rarely enforce equalities to nonlinear expressions. You enforce an inequality:

$$
s \ge |u|
$$

then objective makes it tight.

Why this pattern is universal:

*   Constraints define a **superset** of the nonlinear graph (a relaxation).
*   The objective pushes the relaxation to become exact at optimum.

This is exactly the epigraph philosophy.

### Failure 2: Non-affine inside breaks LP closure

If  $u(x)$  isn’t affine, then  $u(x)\le s$  isn’t linear. LP closure is about **affine functions**.

So the real condition for Phase 5.1 being an LP transformation is:

> The inside of the absolute value must be affine in the decision variables.

### Failure 3: Thinking absolute value itself is “almost linear”

No. The graph has a kink at 0. That kink is exactly what creates non-differentiability and piecewise structure. LP can’t represent kinks in functions, but it can represent kinks in **feasible set boundaries** (polyhedral corners). That’s why epigraph modeling works: corners are allowed in polyhedra.

* * *

13) The “compiler rule” you should memorize (mechanical translation)
====================================================================

Whenever you see  $|\text{affine}(x)|$ :

*   Introduce a new variable  $s$ .
*   Replace  $|\text{affine}(x)|$  with  $s$ .
*   Add two constraints:
    
$$
\text{affine}(x) \le s,\qquad -\text{affine}(x) \le s,
$$

(optionally  $s\ge 0$ , often redundant but clarifying).

Then:

*   If it was in a constraint, you’re done.
*   If it was in an objective, you minimize  $s$  (or minimize something increasing in  $s$ ).

That is Phase 5.1 in pure algorithm form.

* * *

14) Why this matters downstream (but now in a more “structural” way)
====================================================================

This atom is the primitive that lets LPs represent **piecewise-linear convex functions**.

Because piecewise-linear convex functions are exactly maxima of finitely many affine functions. Absolute value is the simplest nontrivial example:

$$
|u| = \max\{u,-u\}.
$$

Once you believe “LP can represent epigraphs of maxima of affine functions,” then:

*    $\ell_\infty$  norm (max of abs) becomes LP,
*   hinge loss  $\max(0,1-y)$  becomes LP,
*   Huber loss (piecewise quadratic/linear) becomes QP/SOCP depending on how represented,
*   robust LP constraints become LP via duality (later).

So Phase 5.1 is not “about absolute value.” It is about the general technique:

> Convert a convex expression into linear constraints by modeling its epigraph using auxiliary variables.

* * *

If you continue to Phase 5.2, the only new ideas will be: (i) how to model a sum of these  $s_i$ ’s cleanly, and (ii) how to model a maximum using a single upper-bound variable. The _engine_ remains exactly Phase 5.1.

## Response:
Alright. Phase 5.2 is where Phase 5.1 stops being a single “abs” trick and turns into a **factory**: you feed it sums and maxima, and out come LPs. I’ll rebuild everything from first principles, prove equivalence carefully (feasible sets + optimal values), show the geometry (why these norms are polyhedral), show multiple modeling patterns (objective vs constraint), and flag the classic traps that kill exam points.

I’ll use consistent notation:

*   Decision variable:  $x \in \mathbb{R}^n$ 
*   Affine map:  $r(x) := Ax + b \in \mathbb{R}^m$  (think “residuals”)
*   Component  $i$ :  $r_i(x)$  is the  $i$ \-th entry of  $r(x)$ 
*    $\ell_1$  norm:  $\|v\|_1 := \sum_i |v_i|$ 
*    $\ell_\infty$  norm:  $\|v\|_\infty := \max_i |v_i|$ 

(Your text used  $|\cdot|_1, |\cdot|_\infty$ ; I’ll switch to  $\|\cdot\|_1,\|\cdot\|_\infty$  since that’s standard, but it’s the same object.)

* * *

0) What Phase 5.2 is really doing (conceptual core)
---------------------------------------------------

Phase 5.1 gave the primitive inequality representation of a scalar absolute value:

$$
|u| \le s \iff \big(u \le s \ \text{and}\ -u \le s\big).
$$

Phase 5.2 uses two more “LP-friendly” facts:

1.  **Sums are linear**  
    If you introduce variables  $s_i$ , then  $\sum_i s_i$  is linear, so it’s a legal LP objective/constraint.
2.  **Max of finitely many scalars is epigraph-representable by linear inequalities**  
    For scalar expressions  $y_1,\dots,y_m$ :
    
$$
t \ge \max_j y_j \iff t \ge y_j \ \forall j.
$$

If each  $y_j$  is affine (or at least linear in variables), then  $t \ge y_j$  is a linear inequality.

So Phase 5.2 = Phase 5.1 (absolute values) + “sum is linear” + “max is inequalities”.

* * *

1) Preliminaries: what  $\ell_1$  and  $\ell_\infty$  actually mean
-------------------------------------------------------------------

Let  $v \in \mathbb{R}^m$ , with components  $v_1,\dots,v_m$ .

### 1.1  $\ell_1$  norm

$$
\|v\|_1 = \sum_{i=1}^m |v_i|.
$$

Interpretation: total magnitude across components. In optimization, it tends to “prefer” solutions where many components are exactly zero (sparsity), but that’s a behavioral aside; modeling-wise it’s just a sum of absolute values.

### 1.2  $\ell_\infty$  norm

$$
\|v\|_\infty = \max_{1\le i \le m} |v_i|.
$$

Interpretation: worst-case magnitude among components. It’s a “minimize the maximum deviation” type expression.

### 1.3 Why these two norms are LP-friendly (deep reason)

Their **unit balls** are polyhedra:

*    $\|v\|_1 \le 1$  is a cross-polytope (polyhedral).
*    $\|v\|_\infty \le 1$  is a box (polyhedral).

Polyhedral sets = describable by finitely many linear inequalities = LP representable.

This is **not true** for  $\ell_2$ :  $\|v\|_2 \le 1$  is a sphere/ball (curved boundary), not polyhedral; that’s why Phase 5.3 moves to SOCP.

* * *

2) Two master modeling principles (made fully rigorous)
-------------------------------------------------------

### Principle A: Epigraph modeling = “introduce an upper bound variable”

To model  $t \ge f(x)$ , you enforce constraints that imply  $t \ge f(x)$ . Then:

*   If  $t$  is minimized (or appears with positive weight in objective), optimality typically forces **tightness**:  $t = f(x)$  at optimum.
*   If  $t$  is not in the objective, it might remain slack, but that doesn’t matter as long as you only care about feasibility or about  $x$ .

### Principle B: Epigraph of max = many inequalities

For any real numbers  $y_1,\dots,y_m$ ,

$$
t \ge \max_i y_i \iff t \ge y_i \ \forall i.
$$

This is exact, not an approximation.

**Proof**:

*   If  $t \ge \max_i y_i$ , then  $t \ge y_i$  for each  $i$  because each  $y_i \le \max_j y_j$ .
*   If  $t \ge y_i$  for all  $i$ , then  $t$  is ≥ every  $y_i$ , hence ≥ their maximum.

No convexity is needed; it’s pure order logic.

* * *

3)  $\ell_1$  norm → LP
-----------------------

### 3.1 Modeling  $\|x\|_1$  (basic case)

We want to represent:

$$
\|x\|_1 = \sum_{i=1}^n |x_i|.
$$

#### Step 1: Introduce magnitude variables

Introduce  $s \in \mathbb{R}^n$ , with intended meaning  $s_i \approx |x_i|$ .

#### Step 2: Enforce  $s_i \ge |x_i|$  via Phase 5.1

$$
s_i \ge |x_i| \iff \begin{cases} x_i \le s_i\\ -x_i \le s_i \end{cases} \quad \text{for each } i.
$$

These are linear inequalities in  $(x,s)$ .

#### Step 3: Replace  $\sum |x_i|$  with  $\sum s_i$ 

Now you can express:

**Objective form**:

$$
\boxed{ \min_{x,s} \ \sum_{i=1}^n s_i \ \text{s.t.}\ x_i \le s_i,\ -x_i \le s_i \ \forall i }
$$

This is a pure LP: linear objective, linear constraints.

* * *

### 3.2 Why the  $\ell_1$  reformulation is exactly equivalent (full proof)

This is the part people wave away; we’ll do it as a theorem.

#### Theorem (exactness of  $\ell_1$  epigraph lifting)

Define the function

$$
F(x) := \sum_{i=1}^n |x_i|.
$$

Consider the lifted feasible set

$$
\mathcal{S}(x) := \{ s \in \mathbb{R}^n : s_i \ge |x_i| \ \forall i\}.
$$

Then:

1.  For any fixed  $x$ , the minimum of  $\sum_i s_i$  over  $s \in \mathcal{S}(x)$  equals  $F(x)$ .
2.  Therefore,  $\min_x F(x)$  equals  $\min_{x,s} \sum_i s_i$  subject to  $s \in \mathcal{S}(x)$ , and the minimizing  $x$ ’s coincide.

**Proof**:

Fix  $x$ . For any feasible  $s\in\mathcal{S}(x)$ , we have  $s_i \ge |x_i|$  for each  $i$ . Summing inequalities preserves order:

$$
\sum_{i=1}^n s_i \ge \sum_{i=1}^n |x_i| = F(x).
$$

So the sum is always at least  $F(x)$ .

Now choose  $s^\star$  defined by  $s^\star_i := |x_i|$ . This  $s^\star$  is feasible (since equality holds). For this choice:

$$
\sum_i s^\star_i = \sum_i |x_i| = F(x).
$$

So the minimum over  $s$  is exactly  $F(x)$ . That proves (1).

Then:

$$
\min_{x,s \in \mathcal{S}(x)} \sum_i s_i = \min_x \left( \min_{s \in \mathcal{S}(x)} \sum_i s_i \right) = \min_x F(x).
$$

Also, if  $x^\star$  minimizes  $F$ , then  $(x^\star, |x^\star|)$  is optimal for the lifted LP. Conversely, if  $(x^\star,s^\star)$  is optimal for lifted LP, then  $x^\star$  must minimize  $F$ , because the objective value equals  $F(x^\star)$  by part (1). QED.

That is a complete equivalence proof.

* * *

### 3.3 Modeling  $\|Ax+b\|_1$  (the actually-used case)

Let residuals  $r(x) := Ax+b \in \mathbb{R}^m$ . We want:

$$
\|Ax+b\|_1 = \sum_{i=1}^m |r_i(x)|.
$$

But  $r_i(x)$  is affine:

$$
r_i(x) = a_i^\top x + b_i
$$

where  $a_i^\top$  is the  $i$ \-th row of  $A$ .

Introduce  $s \in \mathbb{R}^m$  and enforce:

$$
s_i \ge |a_i^\top x + b_i| \iff \begin{cases} a_i^\top x + b_i \le s_i \\ -(a_i^\top x + b_i) \le s_i \end{cases} \quad \forall i.
$$

Then:

**Objective**  $\min \|Ax+b\|_1$ :

$$
\boxed{ \min_{x,s}\ \sum_{i=1}^m s_i \ \text{s.t.}\ a_i^\top x + b_i \le s_i,\ -(a_i^\top x + b_i) \le s_i \ \forall i. }
$$

**Constraint**  $\|Ax+b\|_1 \le t$ :

$$
\boxed{ \exists s:\ a_i^\top x + b_i \le s_i,\ -(a_i^\top x + b_i)\le s_i\ \forall i,\ \sum_{i=1}^m s_i \le t. }
$$

Everything is linear.

* * *

4)  $\ell_\infty$  norm → LP
----------------------------

### 4.1 Modeling  $\|x\|_\infty$ 

We start from:

$$
\|x\|_\infty = \max_{i} |x_i|.
$$

This is a max of absolute values. So we combine:

*   max epigraph:  $t \ge \max_i |x_i| \iff t \ge |x_i| \ \forall i$ 
*   abs atom:  $t \ge |x_i| \iff x_i \le t \ \text{and} \ -x_i \le t$ 

So:

$$
\boxed{ \|x\|_\infty \le t \iff x_i \le t,\ -x_i \le t\quad \forall i. }
$$

**Objective**  $\min \|x\|_\infty$ :

$$
\boxed{ \min_{x,t}\ t \ \text{s.t.}\ x_i \le t,\ -x_i \le t\ \forall i. }
$$

One scalar  $t$ , and 2n inequalities.

* * *

### 4.2 Why the  $\ell_\infty$  reformulation is exactly equivalent (full proof)

Define  $G(x) := \max_i |x_i|$ .

Consider the lifted problem:

$$
\min_{x,t} t\quad \text{s.t.}\quad t \ge |x_i|\ \forall i.
$$

Fix  $x$ . The constraint says  $t$  must be at least each  $|x_i|$ . Therefore it must be at least their maximum:

$$
t \ge \max_i |x_i| = G(x).
$$

So for this fixed  $x$ , the feasible  $t$  are exactly  $[G(x),\infty)$ , and the smallest feasible is  $t^\star(x)=G(x)$ .

Therefore:

$$
\min_{x,t} t = \min_x t^\star(x) = \min_x G(x),
$$

with the same optimal  $x$ . At optimality,  $t = G(x)$  must hold; otherwise you could reduce  $t$  and remain feasible.

That is the complete equivalence.

* * *

### 4.3 Modeling  $\|Ax+b\|_\infty$  (super common)

Residuals  $r(x)=Ax+b\in\mathbb{R}^m$ . Then

$$
\|Ax+b\|_\infty = \max_i |r_i(x)| = \max_i |a_i^\top x + b_i|.
$$

Introduce scalar  $t$  and enforce for every  $i$ :

$$
|a_i^\top x + b_i|\le t \iff \begin{cases} a_i^\top x + b_i \le t \\ -(a_i^\top x + b_i) \le t \end{cases}
$$

So:

**Constraint**  $\|Ax+b\|_\infty \le t$ :

$$
\boxed{ a_i^\top x+b_i \le t,\quad -(a_i^\top x+b_i)\le t\quad \forall i. }
$$

**Objective**  $\min \|Ax+b\|_\infty$ :

$$
\boxed{ \min_{x,t}\ t\quad \text{s.t.}\ a_i^\top x+b_i \le t,\ -(a_i^\top x+b_i)\le t\ \forall i. }
$$

Again a pure LP.

* * *

5) Compare  $\ell_1$  vs  $\ell_\infty$  modeling so you never mix them
-----------------------------------------------------------------------

This is a “pattern recognition” section. If you internalize these signatures, you’ll never confuse them again.

###  $\ell_1$ : “sum of magnitudes”

*   You need **one auxiliary variable per component**:  $s_i$ .
*   You enforce  $s_i \ge |(\cdot)_i|$ .
*   Then you either minimize  $\sum_i s_i$  or constrain  $\sum_i s_i \le t$ .

So the structure looks like:

*   many  $s_i$ 
*   plus a **sum** constraint/objective

###  $\ell_\infty$ : “maximum magnitude”

*   You need **one scalar**  $t$ .
*   You enforce  $|(\cdot)_i| \le t$  for all  $i$ .
*   Then you minimize  $t$  (or constrain  $t\le \tau$ ).

So the structure looks like:

*   one  $t$ 
*   many inequalities “each component ≤ t”

Mnemonic that is actually correct:

*    $\ell_1$ : “many slacks + one sum”
*    $\ell_\infty$ : “one slack + many bounds”

* * *

6) Geometry connection (polyhedral balls) — why LP can do these norms
---------------------------------------------------------------------

### 6.1  $\ell_\infty$  ball is a box

$$
\|x\|_\infty \le t \iff |x_i| \le t\ \forall i \iff -t \le x_i \le t\ \forall i.
$$

That is literally a hyper-rectangle (box). Boxes are polyhedra.

### 6.2  $\ell_1$  ball is a polytope (cross-polytope)

$$
\|x\|_1 \le t \iff \sum_i |x_i|\le t.
$$

The boundary is made of flat facets (in higher-dim). Not curved. So it is also polyhedral and representable with finitely many linear inequalities (the auxiliary-variable representation is one such finite description).

This is why these two norms “belong to LP land.”

* * *

7) Standard exam-style templates (objective vs constraint, affine version)
--------------------------------------------------------------------------

I’m going to list the canonical four cases you’ll see, with zero ambiguity.

### 7.1 Minimize  $\|Ax+b\|_1$ 

$$
\min_{x,s}\ \mathbf{1}^\top s \quad \text{s.t.}\quad Ax+b \le s,\quad -(Ax+b)\le s.
$$

(These vector inequalities mean componentwise.)

### 7.2 Constrain  $\|Ax+b\|_1 \le t$ 

$$
\exists s:\quad Ax+b \le s,\quad -(Ax+b)\le s,\quad \mathbf{1}^\top s \le t.
$$

### 7.3 Minimize  $\|Ax+b\|_\infty$ 

$$
\min_{x,t}\ t \quad \text{s.t.}\quad Ax+b \le t\mathbf{1},\quad -(Ax+b)\le t\mathbf{1}.
$$

### 7.4 Constrain  $\|Ax+b\|_\infty \le t$ 

$$
Ax+b \le t\mathbf{1},\quad -(Ax+b)\le t\mathbf{1}.
$$

These are extremely “copy-paste” patterns.

* * *

8) The subtle point about “tightness” (when does  $s_i = |r_i|$  actually hold?)
--------------------------------------------------------------------------------

This is a nuance that sometimes comes up.

*   If you **minimize**  $\sum_i s_i$ , then yes, each  $s_i$  is pushed as low as possible given constraints, and you get  $s_i = |r_i(x)|$  at optimum.
*   If  $\sum_i s_i$  is **not** minimized and you only use  $s$  to certify feasibility (e.g.,  $\sum_i s_i \le t$  with no objective involving  $s$ ), you still get that the existence of some  $s$  is equivalent to the original constraint. In that case you do not need equality; you only need the feasibility of some  $s$ . If a feasible  $s$  is slack, it just means you picked a non-minimal certificate, but feasibility still holds.

So “tightness at optimum” is a property of objectives; “existence of certificate” is a property of constraints.

* * *

9) Common traps (and why they’re traps, not just “wrong”)
---------------------------------------------------------

### Trap A: Confusing  $\ell_1$  constraint with  $\ell_\infty$  constraint

People incorrectly write:

$$
\|x\|_1 \le t \quad \text{as} \quad |x_i|\le t\ \forall i.
$$

But  $|x_i|\le t\ \forall i$  is exactly  $\|x\|_\infty \le t$ , not  $\ell_1$ .

Why it’s wrong:  $\ell_1$  sums magnitudes;  $\ell_\infty$  caps the largest magnitude. They define different sets.

### Trap B: Swapping them the other way

Writing

$$
\|x\|_\infty \le t \quad \text{as} \quad \sum_i |x_i| \le t
$$

is also wrong: that is  $\|x\|_1 \le t$ .

### Trap C: Forgetting the negative inequality

Absolute value requires two-sided bounding. Always.

### Trap D: Non-affine residuals

If  $r_i(x)$  is nonlinear in  $x$ , then  $r_i(x) \le s_i$  isn’t linear anymore. The template is valid as a logical equivalence, but not an LP.

* * *

10) Mechanical translator (“compiler”) you can execute under time pressure
--------------------------------------------------------------------------

When you see  $\|v(x)\|_1$  where  $v(x)\in\mathbb{R}^m$  is affine:

1.  Introduce  $s\in\mathbb{R}^m$ 
2.  Add:  $-s \le v(x) \le s$  (i.e.,  $v(x)\le s$  and  $-v(x)\le s$ )
3.  Replace  $\|v(x)\|_1$  by  $\mathbf{1}^\top s$ 

When you see  $\|v(x)\|_\infty$ :

1.  Introduce scalar  $t$ 
2.  Add:  $-t\mathbf{1} \le v(x) \le t\mathbf{1}$ 
3.  Replace  $\|v(x)\|_\infty$  by  $t$ 

That’s Phase 5.2 in two lines.

* * *

If you want to push this to “exam dominance” level, the next thing to internalize is how these LP forms relate to dual norms and robust constraints (and why  $\ell_\infty$  constraints correspond to bounded componentwise uncertainty). That’s the bridge from Phase 5.2 to later duality/robustness material, and it’s where these patterns stop being memorized templates and become inevitable consequences of geometry.

## Response:
Got it. Phase 5.3 is the moment LP “runs out of geometry” and we upgrade to SOCP. I’m going to unpack this so thoroughly that:

*   you can derive the SOC definition from first principles (epigraph of  $\ell_2$ ),
*   you can prove convexity in multiple ways (norm properties, triangle inequality, quadratic form),
*   you can prove equivalence of all reformulations (objective/constraint, affine RHS),
*   you can see exactly why “squaring both sides” is conceptually ok but practically the wrong modeling language,
*   you can mechanically translate any  $\ell_2$  norm expression into a standard SOCP form.

I’ll keep everything explicit.

* * *

Phase 5.3 —  $\ell_2$  norms  $\rightarrow$  SOCP
=================================================

“Euclidean norm becomes a cone”
-------------------------------

0) Why LP fails and SOCP enters (structural reason, not slogan)
---------------------------------------------------------------

### 0.1 What LP can represent

LP feasible sets are **polyhedra**:

$$
\{x : A x \le b,\ A_{\text{eq}}x=b_{\text{eq}}\}.
$$

Geometrically, polyhedra have **flat faces**: they are intersections of finitely many halfspaces.

Equivalently (key viewpoint): LP can represent exactly sets whose boundaries are made of finitely many hyperplane pieces.

### 0.2 What the  $\ell_2$  epigraph looks like

Consider the set:

$$
\{(t,y): \|y\|_2 \le t\}.
$$

This is the epigraph of the norm  $\|y\|_2$ . The boundary is

$$
t = \|y\|_2,
$$

which is **curved**, not piecewise-flat. In 2D it’s a V? No—unlike  $|u|$ , it’s a smooth cone surface.

Because this boundary is not a finite union of hyperplane pieces, it is not a polyhedron. Hence LP cannot represent it exactly using finitely many linear inequalities.

So we need a larger convex modeling language than “polyhedra.” SOCP is exactly that: it adds a canonical non-polyhedral convex cone: the second-order cone.

* * *

1) Euclidean norm from bedrock
==============================

Let  $y \in \mathbb{R}^n$ . The Euclidean norm is:

$$
\|y\|_2 := \sqrt{y_1^2+\cdots+y_n^2}.
$$

Key properties:

1.   $\|y\|_2 \ge 0$  with equality iff  $y=0$ .
2.  Homogeneity:  $\|\alpha y\|_2 = |\alpha|\,\|y\|_2$ .
3.  Triangle inequality:  $\|y+z\|_2 \le \|y\|_2 + \|z\|_2$ .

Those are not just trivia: they’re exactly what make the SOC convex, and what makes “norm ≤ affine” constraints convex.

* * *

2) The second-order cone (SOC): definition and meaning
======================================================

2.1 Standard SOC definition (the one solvers use)
-------------------------------------------------

The  $(n+1)$ \-dimensional second-order cone is:

$$
\boxed{\mathcal{Q}_{n+1} := \{(t,y)\in\mathbb{R}\times\mathbb{R}^n : \|y\|_2 \le t\}.}
$$

Interpretation:

*    $t$  is the “height.”
*    $y$  is an  $n$ \-dimensional “horizontal vector.”
*   The constraint says: the horizontal radius is at most the height.

It’s literally the “ice-cream cone” in  $(t,y)$ \-space.

### Immediate consequences (write these down—they matter)

If  $(t,y)\in\mathcal{Q}_{n+1}$ , then:

1.   $t \ge 0$ .  
    Reason:  $\|y\|_2 \ge 0$ , so  $\|y\|_2 \le t$  implies  $t\ge 0$ .
2.  The cone is closed and convex (we’ll prove convexity carefully soon).
3.  Scaling property (cone property): if  $(t,y)\in \mathcal{Q}_{n+1}$  and  $\alpha \ge 0$ , then  $(\alpha t, \alpha y)\in \mathcal{Q}_{n+1}$ .  
    Reason:  $\|\alpha y\|_2 = \alpha \|y\|_2 \le \alpha t$ .

This “cone” behavior is why it’s called a cone and why conic solvers like it.

* * *

2.2 Equivalent “quadratic” characterization
-------------------------------------------

Starting from  $\|y\|_2 \le t$ :

*   Square both sides:
    
$$
\|y\|_2^2 \le t^2.
$$
*   And recall:
    
$$
\|y\|_2^2 = y^\top y.
$$

So:

$$
\|y\|_2 \le t \iff y^\top y \le t^2 \ \text{and}\ t\ge 0.
$$

Thus an equivalent definition is:

$$
\boxed{\mathcal{Q}_{n+1} = \{(t,y) : y^\top y \le t^2,\ t\ge 0\}.}
$$

### Why “ $t\ge 0$ ” is not optional

Without  $t\ge 0$ , squaring would introduce fake solutions because  $t^2$  cannot distinguish  $t$  from  $-t$ . Example: if  $y\neq 0$  and  $t=-100$ , then  $y^\top y \le t^2$  might hold, but  $\|y\|_2 \le t$  cannot, since RHS is negative.

SOC membership automatically enforces  $t\ge 0$ , so the norm form is the cleanest.

* * *

3) Convexity: why SOC constraints are “legal convex constraints”
================================================================

You cited a closure rule (“preimage under affine map”), which is true, but let’s also prove the SOC itself is convex. That’s foundational.

3.1 Prove the SOC set is convex (directly)
------------------------------------------

We need to show:  
if  $(t_1,y_1)\in \mathcal{Q}_{n+1}$  and  $(t_2,y_2)\in \mathcal{Q}_{n+1}$ , then for any  $\theta \in [0,1]$ ,

$$
(\theta t_1 + (1-\theta)t_2,\ \theta y_1 + (1-\theta)y_2)\in\mathcal{Q}_{n+1}.
$$

Given membership:

$$
\|y_1\|_2 \le t_1,\quad \|y_2\|_2 \le t_2.
$$

Now apply triangle inequality and homogeneity:

$$
\|\theta y_1 + (1-\theta)y_2\|_2 \le \|\theta y_1\|_2 + \|(1-\theta)y_2\|_2 = \theta\|y_1\|_2 + (1-\theta)\|y_2\|_2 \le \theta t_1 + (1-\theta) t_2.
$$

This is exactly the SOC condition for the convex combination. Done.

So SOC is convex because norms satisfy triangle inequality.

That’s the “why” behind conic modeling.

* * *

4) What is an SOCP constraint (formal modeling language)
========================================================

An SOCP lets you impose constraints of the form:

$$
\boxed{(t(x),\ y(x)) \in \mathcal{Q}_{k}}
$$

where  $t(x)$  is an affine scalar function of decision variables and  $y(x)$  is an affine vector function.

Unpacked:

$$
\boxed{\|y(x)\|_2 \le t(x)}
$$

with  $y(x)$  affine and  $t(x)$  affine.

This set is convex because:

*    $\mathcal{Q}_k$  is convex,
*   affine maps preserve convex combinations,
*   the preimage of a convex set under an affine map is convex.

So “norm of affine ≤ affine” is a convex constraint.

* * *

5) The Phase 5.3 atom:  $\|Ax+b\|_2 \le t$ 
===========================================

This is the most important template.

Let  $Ax+b \in \mathbb{R}^m$ . Define:

*    $y(x) := Ax+b$  (affine vector)
*    $t(x) := t$  (scalar variable, affine)

Then:

$$
\boxed{\|Ax+b\|_2 \le t \iff (t,\ Ax+b)\in \mathcal{Q}_{m+1}.}
$$

### Why this is exact (not a relaxation)

Because it is literally the definition of membership in  $\mathcal{Q}_{m+1}$ . There is no approximation step.

This is important: in Phase 5.1/5.2 we often introduced extra variables and relied on objectives to force tightness; here, if it’s purely a constraint, it’s still exact because we’re not replacing with an inequality that’s looser—we’re rewriting the same inequality in the solver’s accepted conic syntax.

* * *

6) Norm in objective:  $\min \|Ax+b\|_2$  via epigraph
======================================================

Start with:

$$
\min_x \ \|Ax+b\|_2.
$$

SOCPs accept linear objectives.  $\|Ax+b\|_2$  is not linear. So we epigraph it:

Introduce  $t$  and write:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad \|Ax+b\|_2 \le t.
$$

Then recognize SOC membership:

$$
(t,\ Ax+b)\in \mathcal{Q}_{m+1}.
$$

6.1 Full equivalence proof (same style as 5.1/5.2)
--------------------------------------------------

Fix any  $x$ . Consider the set of feasible  $t$  values:

$$
\{t : \|Ax+b\|_2 \le t\}.
$$

This is exactly:

$$
[\ \|Ax+b\|_2,\ \infty\ ).
$$

So the smallest feasible  $t$  for that  $x$  is:

$$
t^\star(x)=\|Ax+b\|_2.
$$

Therefore:

$$
\min_{x,t}\ t = \min_x \left(\min_{t\ge \|Ax+b\|_2} t \right) = \min_x \|Ax+b\|_2.
$$

Also, at optimality,  $t=\|Ax+b\|_2$  must hold; otherwise, you could decrease  $t$  and remain feasible.

So the epigraph form is exactly equivalent: same optimal value and same optimizing  $x$ .

* * *

7) The “norm ≤ affine” template:  $\|Ax+b\|_2 \le c^\top x + d$ 
================================================================

This is the most common PS pattern.

Let:

*   LHS:  $\|Ax+b\|_2$  (convex)
*   RHS:  $c^\top x + d$  (affine)

The SOCP form is immediate:

$$
\boxed{\|Ax+b\|_2 \le c^\top x + d \iff (c^\top x + d,\ Ax+b)\in \mathcal{Q}_{m+1}.}
$$

### Feasibility implies RHS ≥ 0 (domain sanity check)

Since  $\|Ax+b\|_2 \ge 0$ , any feasible  $x$  must satisfy:

$$
c^\top x + d \ge 0.
$$

You typically don’t add it separately because SOC membership forces it (the first component of SOC is always ≥ 0). But in proofs, stating it shows you understand the domain.

* * *

7.1 Why “don’t square it” is good advice (nuanced and precise)
--------------------------------------------------------------

Mathematically:

$$
\|Ax+b\|_2 \le c^\top x + d \quad \Rightarrow\quad (Ax+b)^\top(Ax+b) \le (c^\top x + d)^2
$$

is valid **provided**  $c^\top x+d \ge 0$ .

But there are two practical issues:

1.  The squared constraint becomes:
    
$$
x^\top A^\top A x + 2 b^\top A x + b^\top b \le (c^\top x + d)^2 = x^\top(cc^\top)x + 2d c^\top x + d^2.
$$

So you get “quadratic ≤ quadratic” with quadratic terms on both sides. Rearranged, it’s one quadratic inequality:

$$
x^\top(A^\top A - cc^\top)x + \cdots \le 0.
$$

This is **not automatically convex**. It is convex only if the resulting quadratic form is convex (i.e., the left side is convex in  $x$ ), which depends on PSD conditions that may fail.

The SOC form, by contrast, is convex by construction.

2.  Even when it is convex, many solvers want the **conic canonical form**  $(t,y)\in \mathcal{Q}$  rather than a “difference of quadratics.” The conic form is numerically stable and standardized.

So: squaring is not “wrong math,” but it’s the wrong _modeling language_ and can even destroy convexity if you rearrange incorrectly.

* * *

8) Geometric meaning (so it stops feeling like symbol-matching)
===============================================================

8.1  $\|x-x_0\|_2 \le r$ : Euclidean ball
-----------------------------------------

This is the ball of radius  $r$  centered at  $x_0$ . SOCP form:

$$
(r,\ x-x_0)\in\mathcal{Q}_{n+1}.
$$

Meaning: “the vector  $x-x_0$  lies inside a Euclidean ball.”

8.2  $\|Ax+b\|_2 \le t$ : preimage of a ball
--------------------------------------------

$$
\|Ax+b\|_2 \le t
$$

means:

$$
Ax+b \in \{y:\|y\|_2\le t\}.
$$

So  $x$  must lie in the **preimage** of that ball under the affine map  $x \mapsto Ax+b$ . This set is convex.

If  $A$  is invertible, it’s an ellipsoid-like region in  $x$ \-space (more precisely:  $x$  lies in an affine transformation of a ball). If  $A$  is not full rank, you get a “cylinder-ish” convex set. Still convex.

This is a good geometric sanity check.

* * *

9) Common variants and how to model them instantly
==================================================

9.1 Sum of  $\ell_2$  norms
---------------------------

Problem:

$$
\min_x \sum_{k=1}^K \|A_k x + b_k\|_2.
$$

Lift each norm with its own scalar  $t_k$ :

$$
\min_{x,t}\ \sum_{k=1}^K t_k \quad \text{s.t.}\quad \|A_k x + b_k\|_2 \le t_k\ \forall k.
$$

Each constraint is SOC; objective is linear. Whole thing is SOCP.

Exactness is the same “for fixed  $x$ , minimal  $t_k$  equals the norm” argument, componentwise.

9.2 Max of  $\ell_2$  norms
---------------------------

$$
\min_x \max_k \|A_k x+b_k\|_2.
$$

Epigraph with one  $t$ :

$$
\min_{x,t}\ t\quad \text{s.t.}\quad \|A_k x+b_k\|_2 \le t\ \forall k.
$$

Again SOCP.

9.3 Least squares in  $\ell_2$  (two flavors!)
----------------------------------------------

Classic objective:

$$
\min_x \|Ax-b\|_2
$$

is SOCP via epigraph.

But:

$$
\min_x \|Ax-b\|_2^2
$$

is a QP (quadratic objective). Both are convex, but they are different formulations.

Important subtlety: minimizing  $\|r\|_2$  and minimizing  $\|r\|_2^2$  have the **same minimizers** (because squaring is monotone on  $[0,\infty)$ ), but not the same objective value. Depending on the context/solver, one is used over the other.

* * *

10) Failure modes (with deeper explanation)
===========================================

1.  **RHS not affine**  
    Constraint  $\|Ax+b\|_2 \le \sqrt{c^\top x + d}$  is not in standard SOCP form because RHS is concave in  $x$  (square root of affine is concave on domain). Sometimes you can rewrite by squaring plus domain constraints, but you must be very careful: you can break convexity or introduce nonconvex constraints. Standard SOCP wants affine RHS.
2.  **Non-affine inside the norm**  
     $\|[x; x^2]\|_2 \le t$  has non-affine components inside the norm; that’s not a standard conic constraint. “Norm of nonlinear vector” is not generally SOC-representable.
3.  **Mis-handling the nonnegativity condition**  
    If you do any squaring manipulations by hand, you must ensure the RHS is nonnegative. SOC form handles this automatically.
4.  **Confusing  $\ell_2$  with componentwise abs**  
     $\|x\|_2 \le t$  is one coupled constraint involving all components;  $|x_i|\le t$  for all  $i$  is  $\|x\|_\infty \le t$ . These are different feasible sets.

* * *

11) Mechanical translator (the “no-thinking” rule set)
======================================================

Whenever you see  $\ell_2$  norms:

### Template A:  $\|Ax+b\|_2 \le t$ 

Write:

$$
(t,\ Ax+b)\in\mathcal{Q}_{m+1}.
$$

### Template B:  $\|Ax+b\|_2 \le c^\top x + d$ 

Write:

$$
(c^\top x + d,\ Ax+b)\in\mathcal{Q}_{m+1}.
$$

### Template C: Objective  $\min \|Ax+b\|_2$ 

Lift:

$$
\min_{x,t} t\quad \text{s.t.}\quad (t,\ Ax+b)\in\mathcal{Q}_{m+1}.
$$

### Template D: Sum / max of multiple norms

Give each norm its own  $t_k$  (sum) or share one  $t$  (max), and constrain each with an SOC inequality.

That is Phase 5.3.

* * *

If you want the “next domino” (Phase 5.4), the key new object is the **rotated second-order cone**, which represents constraints like  $2uv \ge \|w\|_2^2$  with  $u,v\ge 0$ . That’s the bridge from “norm cones” to “product / quadratic-over-linear / hyperbolic” constraints—and it’s exactly where SOCP starts to subsume a surprisingly large chunk of convex quadratic inequalities.

## Response:
Absolutely. Phase 5.4 is _the_ moment where “products” stop being instant nonconvex panic and become a clean conic template—provided they appear in the **right convex shape** (product of nonnegatives bounding a square / squared norm). I’ll rebuild this from first principles and make the equivalences airtight.

I’m going to do five things in a very explicit way:

1.  Define the rotated SOC (RSOC) cleanly and explain what it _means_.
2.  Prove the key equivalence: hyperbolic constraint  $w^2 \le xy,\ x,y\ge 0$  ⇔ RSOC membership.
3.  Show the conversion RSOC ⇔ standard SOC (so it’s truly SOCP-representable even if the solver “only knows” standard SOC).
4.  Derive quadratic-over-linear as a special case (and discuss domains carefully).
5.  Give a mechanical translation cookbook + traps.

* * *

Phase 5.4 — Hyperbolic / quadratic-over-linear  $\rightarrow$  Rotated SOC
==========================================================================

“Product becomes a cone”
------------------------

0) What kinds of constraints are we talking about?
--------------------------------------------------

### 0.1 The canonical scalar hyperbolic constraint

$$
\boxed{w^2 \le xy,\qquad x\ge 0,\ y\ge 0.}
$$

Why it’s called “hyperbolic”: for fixed  $w\neq 0$ , the boundary  $xy=w^2$  in the  $(x,y)$ \-plane is a hyperbola.

### 0.2 Vector generalization (squared norm)

$$
\boxed{\|z\|_2^2 \le xy,\qquad x\ge 0,\ y\ge 0, \ z\in\mathbb{R}^n.}
$$

### 0.3 Quadratic-over-linear (QoL) form

Scalar:

$$
\boxed{\frac{w^2}{x} \le y,\qquad x>0\ (\text{or }x\ge 0\text{ with conventions}).}
$$

Vector:

$$
\boxed{\frac{\|z\|_2^2}{x} \le y,\qquad x>0.}
$$

The algebra link is immediate (but domain-sensitive):

$$
\frac{w^2}{x}\le y \iff w^2 \le xy \quad (\text{requires } x>0 \text{ for equivalence without ambiguity}).
$$

These are convex constraints in their proper domains, but they are not polyhedral and not plain SOC in the form  $\|(\cdot)\|_2 \le \text{affine}$ . RSOC is the missing atom.

* * *

1) The rotated second-order cone (RSOC): definition and meaning
===============================================================

There are several conventions. I’ll use the one that is standard in convex optimization texts and matches your writeup.

1.1 Definition (dimension bookkeeping explicit)
-----------------------------------------------

For  $n\ge 1$ , define the **rotated second-order cone** in  $\mathbb{R}^{n+2}$  as:

$$
\boxed{ \mathcal{Q}^{r}_{n+2} := \left\{(u,v,w)\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^n: u\ge 0,\ v\ge 0,\ 2uv \ge \|w\|_2^2 \right\}. }
$$
*    $u$  and  $v$ : scalars, constrained nonnegative.
*    $w$ :  $n$ \-vector.
*   The inequality  $2uv \ge \|w\|_2^2$  is the “product dominates square” structure.

1.2 Why the factor 2 is there (not cosmetic)
--------------------------------------------

The factor 2 makes the algebra-to-standard-SOC conversion come out with clean “ $u+v$ ” and “ $u-v$ ” expressions without extra constants. Constants can always be handled by scaling (affine maps), but a good convention saves mistakes.

1.3 RSOC is convex (prove it, not just assert)
----------------------------------------------

We can prove convexity in a robust way:

**Claim:**  $\mathcal{Q}^{r}_{n+2}$  is a convex cone.

*   Cone property: if  $(u,v,w)$  is feasible and  $\alpha\ge 0$ , then  $(\alpha u,\alpha v,\alpha w)$  is feasible since
    $$
    2(\alpha u)(\alpha v) = \alpha^2(2uv)\ \ge\ \alpha^2\|w\|_2^2=\|\alpha w\|_2^2.
    $$
*   Convexity: we’ll prove it via its standard SOC representation (Section 3). Since standard SOC is convex and RSOC is an affine image / preimage thereof, RSOC is convex. (You can also prove convexity directly via Cauchy–Schwarz and triangle inequality, but the SOC conversion is the cleanest “modeling-level” proof.)

* * *

2) The Phase 5.4 atom:  $w^2 \le xy$  is RSOC
=============================================

This is the core.

2.1 Scalar case as RSOC membership
----------------------------------

We want:

$$
w^2 \le xy,\quad x\ge 0,\ y\ge 0.
$$

RSOC condition for  $n=1$  is:

$$
(u,v,w)\in\mathcal{Q}^r_{3} \iff u\ge 0,\ v\ge 0,\ 2uv \ge w^2.
$$

To match  $xy$  on the right side, choose:

$$
u := x,\qquad v := y/2,\qquad w := w.
$$

Then

$$
2uv = 2\cdot x \cdot (y/2) = xy.
$$

So:

$$
(x,\ y/2,\ w)\in\mathcal{Q}^r_3 \iff x\ge 0,\ y/2\ge 0,\ xy \ge w^2 \iff x\ge 0,\ y\ge 0,\ w^2 \le xy.
$$

Thus the exact equivalence:

$$
\boxed{ w^2 \le xy,\ x\ge 0,\ y\ge 0 \quad\Longleftrightarrow\quad (x,\ y/2,\ w)\in \mathcal{Q}^r_3. }
$$

No approximation. It’s literally substitution into the cone definition.

* * *

2.2 Vector case:  $\|z\|_2^2 \le xy$ 
-------------------------------------

Now let  $z\in\mathbb{R}^n$ . RSOC says:

$$
(u,v,z)\in\mathcal{Q}^{r}_{n+2} \iff u\ge 0,\ v\ge 0,\ 2uv \ge \|z\|_2^2.
$$

Same substitution:

$$
u := x,\qquad v := y/2,\qquad w := z.
$$

Then  $2uv = xy$ . So:

$$
\boxed{ \|z\|_2^2 \le xy,\ x\ge 0,\ y\ge 0 \quad\Longleftrightarrow\quad (x,\ y/2,\ z)\in\mathcal{Q}^r_{n+2}. }
$$

This is the _workhorse_ form for quadratic-over-linear and “energy” constraints.

* * *

3) RSOC  $\leftrightarrow$  standard SOC (so it’s truly SOCP)
=============================================================

Some solvers expose RSOC directly. But even if they don’t, RSOC can be represented using a **single standard SOC** plus nonnegativity constraints. This is crucial.

3.1 Standard SOC reminder
-------------------------

$$
\mathcal{Q}_{k} := \{(t,y)\in\mathbb{R}\times\mathbb{R}^{k-1} : \|y\|_2 \le t\}.
$$

3.2 The key identity (clean and constant-correct)
-------------------------------------------------

**Claim:**

$$
\boxed{ (u,v,w)\in\mathcal{Q}^{r}_{n+2} \iff \left\| \begin{bmatrix} 2w\\ u-v \end{bmatrix} \right\|_2 \le u+v,\qquad u\ge 0,\ v\ge 0. }
$$

This is the canonical conversion.

### Proof (fully explicit)

Assume  $u\ge 0$ ,  $v\ge 0$ . Then  $u+v \ge 0$ , so squaring an inequality of the form “norm ≤ nonnegative scalar” preserves equivalence.

Start from the SOC inequality:

$$
\left\| \begin{bmatrix} 2w\\ u-v \end{bmatrix} \right\|_2 \le u+v.
$$

Square both sides:

Left side squared:

$$
\left\| \begin{bmatrix} 2w\\ u-v \end{bmatrix} \right\|_2^2 = \|2w\|_2^2 + (u-v)^2 = 4\|w\|_2^2 + (u-v)^2.
$$

Right side squared:

$$
(u+v)^2 = u^2 + 2uv + v^2.
$$

So the squared inequality is:

$$
4\|w\|_2^2 + (u-v)^2 \le (u+v)^2.
$$

Now expand  $(u-v)^2$ :

$$
(u-v)^2 = u^2 - 2uv + v^2.
$$

Substitute:

$$
4\|w\|_2^2 + (u^2 - 2uv + v^2) \le u^2 + 2uv + v^2.
$$

Cancel  $u^2$  and  $v^2$  from both sides:

$$
4\|w\|_2^2 - 2uv \le 2uv.
$$

Add  $2uv$  to both sides:

$$
4\|w\|_2^2 \le 4uv.
$$

Divide by 4:

$$
\|w\|_2^2 \le uv.
$$

Now compare with RSOC’s defining inequality  $2uv \ge \|w\|_2^2$ . We got  $\|w\|_2^2 \le uv$ , which is actually _stronger_ by a factor of 2. That means we used the “2w” scaling and “u+v” form but matched a slightly different convention.

So let’s fix constants carefully to match your RSOC convention exactly.

### 3.3 Getting the exact “ $2uv$ ” version (constant hygiene)

We want:

$$
\|w\|_2^2 \le 2uv.
$$

If we repeat the above derivation but replace  $2w$  with  $\sqrt{2}\,w$ , we get:

Consider:

$$
\left\| \begin{bmatrix} \sqrt{2}\,w\\ u-v \end{bmatrix} \right\|_2 \le u+v.
$$

Square:

Left squared:

$$
\|\sqrt{2}\,w\|_2^2 + (u-v)^2 = 2\|w\|_2^2 + (u-v)^2.
$$

Then:

$$
2\|w\|_2^2 + (u^2-2uv+v^2) \le u^2+2uv+v^2
$$

Cancel  $u^2,v^2$ :

$$
2\|w\|_2^2 - 2uv \le 2uv
$$

So:

$$
2\|w\|_2^2 \le 4uv \iff \|w\|_2^2 \le 2uv.
$$

Perfect.

So the **exact conversion** matching the definition in your notes is:

$$
\boxed{ (u,v,w)\in\mathcal{Q}^{r}_{n+2} \iff \left\| \begin{bmatrix} \sqrt{2}\,w\\ u-v \end{bmatrix} \right\|_2 \le u+v,\qquad u\ge 0,\ v\ge 0. }
$$

And this is now a single standard SOC constraint (norm ≤ scalar) plus linear nonnegativity.

**Practical modeling point:** Many modeling packages hide these constants; you just declare “rotated cone” and it handles the  $\sqrt{2}$  scaling internally. But in handwritten derivations, you must keep the constants consistent.

* * *

4) Quadratic-over-linear is RSOC in disguise (with full domain logic)
=====================================================================

This is the most tested pattern.

4.1 Scalar quadratic-over-linear:  $\dfrac{w^2}{x} \le y$ 
----------------------------------------------------------

Assume  $x>0$ . Then multiplying both sides by  $x$  preserves inequality direction:

$$
\frac{w^2}{x} \le y \iff w^2 \le xy.
$$

Now if  $x>0$ , the inequality  $w^2 \le xy$  implies  $y\ge 0$  automatically, because  $w^2\ge 0$  and dividing by  $x>0$  gives  $y \ge w^2/x \ge 0$ . So you don’t need to separately impose  $y\ge 0$  if  $x>0$  is enforced.

Thus:

$$
\boxed{ \frac{w^2}{x}\le y,\ x>0 \iff w^2 \le xy,\ x\ge 0,\ y\ge 0 \iff (x,\ y/2,\ w)\in\mathcal{Q}^{r}_3. }
$$

### Edge case  $x=0$  (why people insist on domains)

If you allow  $x=0$ , the expression  $w^2/x$  is undefined. But the hyperbolic inequality  $w^2\le xy$  _is_ defined at  $x=0$ . At  $x=0$ , it becomes:

$$
w^2 \le 0\cdot y = 0 \implies w=0.
$$

So the natural closed convex extension of the quadratic-over-linear epigraph includes the point  $x=0$  only if  $w=0$  (and  $y\ge 0$ ). RSOC captures exactly that closure (because RSOC allows  $u=0$  or  $v=0$  only if  $w=0$ ).

So the safest modeling language is:

*   If the problem truly wants  $w^2/x$ , impose  $x>0$  or  $x\ge \epsilon$ .
*   If you want the closed convex set, model  $w^2 \le xy,\ x\ge 0,\ y\ge 0$  via RSOC.

* * *

4.2 Vector quadratic-over-linear:  $\dfrac{\|z\|_2^2}{x} \le y$ 
----------------------------------------------------------------

Assume  $x>0$ . Multiply through:

$$
\frac{\|z\|_2^2}{x} \le y \iff \|z\|_2^2 \le xy.
$$

Then:

$$
\boxed{ \frac{\|z\|_2^2}{x}\le y,\ x>0 \iff (x,\ y/2,\ z)\in\mathcal{Q}^{r}_{n+2}. }
$$

This is exactly the conic representation of the quadratic-over-linear function’s epigraph, which is known to be convex on  $x>0$ .

* * *

5) Why these sets are convex (two rigorous routes)
==================================================

Route A: Conic representability (fastest)
-----------------------------------------

*    $\mathcal{Q}^r$  is convex (as an SOC-representable cone).
*   If  $u(x),v(x),w(x)$  are affine in decision variables, then
    
$$
(u(x),v(x),w(x))\in\mathcal{Q}^r
$$

defines a convex feasible set, because it’s the preimage of a convex set under an affine map.

This is the clean “modeling correctness” argument.

Route B: Function epigraph argument (what’s really inside)
----------------------------------------------------------

Define

$$
f(z,x) := \frac{\|z\|_2^2}{x}
$$

on domain  $x>0$ . This is a convex function (it is the perspective of the convex quadratic  $q(z)=\|z\|_2^2$ ). Then the constraint

$$
\frac{\|z\|_2^2}{x} \le y
$$

is exactly

$$
(y \text{ is above } f(z,x)),
$$

i.e., an epigraph constraint, which defines a convex set.

RSOC is simply the conic “syntax” that expresses that epigraph.

* * *

6) How to recognize when RSOC applies (the “shape test”)
========================================================

RSOC models constraints of the form:

$$
\|w\|_2^2 \le 2uv,\quad u\ge 0,\ v\ge 0.
$$

So you should look for any of these equivalent-looking shapes:

1.  **Product dominates square/norm-square**
    
$$
\|w\|_2^2 \le xy \quad (x,y\ge 0)
$$

(then set  $u=x,\ v=y/2$ .)

2.  **Quadratic-over-linear**
    
$$
\frac{\|w\|_2^2}{x} \le y \quad (x>0)
$$

(then multiply to  $\|w\|_2^2 \le xy$ .)

3.  **“Energy ≤ power × time”-type constraints**  
    These almost always reduce to  $\|w\|^2 \le (\text{nonneg})(\text{nonneg})$ .

If it instead looks like:

$$
xy \le \|w\|_2^2
$$

or

$$
w^2 \ge xy,
$$

that’s typically nonconvex and not RSOC.

Direction matters.

* * *

7) Mechanical translator (templates you can apply under exam time)
==================================================================

Template 1: Scalar hyperbolic
-----------------------------

Constraint:

$$
w^2 \le xy,\quad x\ge 0,\ y\ge 0.
$$

RSOC form:

$$
\boxed{(x,\ y/2,\ w)\in\mathcal{Q}^r_3.}
$$

Template 2: Vector hyperbolic
-----------------------------

Constraint:

$$
\|z\|_2^2 \le xy,\quad x\ge 0,\ y\ge 0.
$$

RSOC form:

$$
\boxed{(x,\ y/2,\ z)\in\mathcal{Q}^r_{n+2}.}
$$

Template 3: Scalar quadratic-over-linear
----------------------------------------

Constraint:

$$
\frac{w^2}{x} \le y,\quad x>0.
$$

Rewrite  $w^2 \le xy$ , then Template 1:

$$
\boxed{(x,\ y/2,\ w)\in\mathcal{Q}^r_3.}
$$

Template 4: Vector quadratic-over-linear
----------------------------------------

Constraint:

$$
\frac{\|z\|_2^2}{x} \le y,\quad x>0.
$$

Rewrite  $\|z\|_2^2 \le xy$ , then Template 2:

$$
\boxed{(x,\ y/2,\ z)\in\mathcal{Q}^r_{n+2}.}
$$

Template 5: If your solver only accepts standard SOC
----------------------------------------------------

Use the exact SOC conversion (constants correct):

$$
(u,v,w)\in\mathcal{Q}^r_{n+2} \iff u\ge 0,\ v\ge 0,\ \left\| \begin{bmatrix} \sqrt{2}\,w\\ u-v \end{bmatrix} \right\|_2 \le u+v.
$$

This is standard SOC form: norm ≤ affine.

* * *

8) Traps and failure modes (explained, not just listed)
=======================================================

Trap A: Dropping  $x\ge 0, y\ge 0$ 
-----------------------------------

The set  $\{(x,y,w): w^2 \le xy\}$  without sign constraints is not convex. The convexity is tied to the fact that  $xy$  behaves like an “area” only when both are nonnegative and you’re effectively modeling a geometric mean type relationship.

RSOC enforces  $u\ge 0, v\ge 0$ . That is not optional.

Trap B: Wrong direction (product ≤ square)
------------------------------------------

$$
xy \le w^2
$$

is generally nonconvex (it describes the outside of the convex region in the  $(x,y)$  plane for fixed  $w$ ). RSOC handles the “inside” direction: square ≤ product.

Trap C: Mishandling  $x=0$  in quadratic-over-linear
----------------------------------------------------

If you write  $w^2/x \le y$  and allow  $x=0$ , the expression is undefined. The RSOC/hyperbolic form gives the _closed convex extension_ where  $x=0$  forces  $w=0$ . Know which your problem intends.

Trap D: Constant scaling mistakes
---------------------------------

People often write  $(x,y,w)\in \mathcal{Q}^r$  when it should be  $(x,y/2,w)$  or vice versa. The factor 2 is not “whatever”—it’s exactly what matches the convention  $2uv \ge \|w\|^2$ . If you get this wrong, your feasible set changes.

A safe approach: always compute  $2uv$  explicitly and match it to the product you want.

* * *

9) Why Phase 5.4 is a big deal (the modeling payoff)
====================================================

This atom is the gateway to expressing a huge class of convex constraints:

*   quadratic-over-linear penalties and constraints (ubiquitous in estimation/control),
*   many “variance / energy / power” relationships,
*   perspectives of quadratic forms,
*   certain QCQP constraints becoming SOCP,
*   robust constraints that produce quadratic-over-linear pieces.

It’s the “product-shaped” sibling of Phase 5.3’s “norm ≤ affine.”

* * *

If you want the natural next step after 5.4: there’s a very clean bridge between RSOC and the Schur complement in SDP land. In many places,  $w^2 \le xy$  also corresponds to a  $2\times 2$  PSD constraint  $\begin{bmatrix}x & w\\ w & y\end{bmatrix}\succeq 0$  (with  $x,y\ge 0$ ). That’s the same geometry expressed in SDP language. This is exactly how the cones relate under the hood.

## Response:
Phase 5.5 is genuinely one of the “convex optimization superpowers,” but it only feels like magic because it compresses an _infinite_ family of constraints into _one_ norm inequality using geometry. I’ll build the pipeline from scratch, prove each equivalence carefully, and then show how it lands in LP vs SOCP depending on the uncertainty norm.

I’m going to keep the discussion concrete: robust **linear** constraints with additive uncertainty, because that’s the canonical PS/assignment pattern and the cleanest place where dual norms appear.

* * *

0) What a robust constraint really is (no handwaving)
-----------------------------------------------------

### 0.1 Nominal constraint

A standard (non-robust) linear constraint is

$$
a^\top x \le b,
$$

where  $a\in\mathbb{R}^n$ ,  $x\in\mathbb{R}^n$ ,  $b\in\mathbb{R}$ .

### 0.2 Robust version (additive uncertainty in coefficients)

A robust constraint says the inequality must hold for **all** perturbations  $u$  in some uncertainty set  $\mathcal U$ :

$$
(a+u)^\top x \le b \qquad \forall u\in \mathcal U.
$$

This means: Nature gets to pick  $u$  adversarially after seeing your  $x$ , and you still must satisfy the constraint.

This “ $\forall u$ ” is an **infinite conjunction** of inequalities (one for each  $u$ ). The entire job of robust optimization is to rewrite that infinite conjunction as a single tractable convex constraint.

* * *

1) Step 1: turn “for all” into a worst-case supremum
----------------------------------------------------

Start with:

$$
(a+u)^\top x \le b \quad \forall u\in\mathcal U.
$$

Expand:

$$
(a+u)^\top x = a^\top x + u^\top x.
$$

So:

$$
a^\top x + u^\top x \le b \quad \forall u\in\mathcal U.
$$

### Key equivalence

$$
\boxed{ a^\top x + u^\top x \le b\ \forall u\in\mathcal U \iff a^\top x + \sup_{u\in\mathcal U} u^\top x \le b. }
$$

#### Proof (both directions, fully explicit)

**( $\Rightarrow$ )** Assume  $a^\top x + u^\top x \le b$  for all  $u\in\mathcal U$ .  
Then the set of values  $\{u^\top x : u\in\mathcal U\}$  is all bounded above by  $b-a^\top x$ . Therefore its supremum is also bounded above:

$$
\sup_{u\in\mathcal U} u^\top x \le b-a^\top x.
$$

Rearrange:

$$
a^\top x + \sup_{u\in\mathcal U} u^\top x \le b.
$$

**( $\Leftarrow$ )** Assume  $a^\top x + \sup_{u\in\mathcal U} u^\top x \le b$ .  
Pick any specific  $u\in\mathcal U$ . By definition of supremum,

$$
u^\top x \le \sup_{v\in\mathcal U} v^\top x.
$$

Add  $a^\top x$  to both sides:

$$
a^\top x + u^\top x \le a^\top x + \sup_{v\in\mathcal U} v^\top x \le b.
$$

So the inequality holds for that  $u$ , and since  $u$  was arbitrary, it holds for all  $u\in\mathcal U$ .

So robust constraints are _always_ equivalent to:

$$
a^\top x + \text{(worst-case contribution from uncertainty)} \le b.
$$

Everything now boils down to computing / representing

$$
\sup_{u\in\mathcal U} u^\top x.
$$

* * *

2) Step 2: recognize the support function (the geometric object you’re computing)
---------------------------------------------------------------------------------

Define the **support function** of a set  $\mathcal U\subseteq\mathbb{R}^n$ :

$$
\boxed{\sigma_{\mathcal U}(x) := \sup_{u\in\mathcal U} u^\top x.}
$$

Interpretation (very important intuition):

*    $u^\top x$  is the projection of  $u$  onto direction  $x$  (up to scaling).
*    $\sigma_{\mathcal U}(x)$  is the **furthest extent** of  $\mathcal U$  in direction  $x$ .
*   So robust constraints become:
    
$$
a^\top x + \sigma_{\mathcal U}(x) \le b.
$$

Now: if  $\mathcal U$  is “nice” (especially a norm ball),  $\sigma_{\mathcal U}(x)$  becomes a norm (specifically a dual norm).

* * *

3) Step 3: norm balls ⇒ dual norms (the main theorem)
-----------------------------------------------------

This is the central theorem of Phase 5.5.

### 3.1 Dual norm definition (from first principles)

Let  $\|\cdot\|$  be a norm on  $\mathbb{R}^n$ . Its **dual norm**  $\|\cdot\|_*$  is defined as:

$$
\boxed{\|x\|_* := \sup_{\|u\|\le 1} u^\top x.}
$$

That is: maximize dot product with  $x$  over the **unit ball** of the primal norm.

This is exactly a support function:

$$
\|x\|_* = \sigma_{B}(x) \quad \text{where } B=\{u:\|u\|\le 1\}.
$$

### 3.2 Support function of a radius- $\rho$  norm ball

Let uncertainty set be a norm ball:

$$
\mathcal U := \{u : \|u\|\le \rho\}.
$$

Then:

$$
\boxed{\sup_{\|u\|\le\rho} u^\top x = \rho\|x\|_*.}
$$

#### Proof (clean scaling argument)

Let  $u=\rho v$ . Then  $\|u\|\le\rho \iff \|\rho v\|\le\rho \iff \|v\|\le 1$  (by norm homogeneity).  
So:

$$
\sup_{\|u\|\le\rho} u^\top x = \sup_{\|v\|\le 1} (\rho v)^\top x = \rho \sup_{\|v\|\le 1} v^\top x = \rho \|x\|_*.
$$

Done.

This is the “collapse infinite constraints to one norm inequality” step.

* * *

4) The canonical robust linear constraint (final collapsed form)
----------------------------------------------------------------

Start from:

$$
(a+u)^\top x \le b\quad \forall u:\ \|u\|\le\rho.
$$

We already showed this is equivalent to:

$$
a^\top x + \sup_{\|u\|\le\rho} u^\top x \le b.
$$

Apply the theorem:

$$
a^\top x + \rho\|x\|_* \le b.
$$

So the robust constraint becomes:

$$
\boxed{ (a+u)^\top x \le b\ \forall \|u\|\le\rho \quad\Longleftrightarrow\quad a^\top x + \rho\|x\|_* \le b. }
$$

This is the key output of Phase 5.5.

Now Phase 5.2–5.4 decide whether  $\|x\|_*$  produces an LP, SOC, or rotated SOC constraint.

* * *

5) Compute the dual norms for  $\ell_2,\ell_\infty,\ell_1$  (and prove them)
----------------------------------------------------------------------------

You used these facts:

*   dual of  $\ell_2$  is  $\ell_2$ 
*   dual of  $\ell_\infty$  is  $\ell_1$ 
*   dual of  $\ell_1$  is  $\ell_\infty$ 

I’ll prove each from the dual definition. This matters because robust optimization problems often hinge on picking the right dual.

### 5.1 Dual of  $\ell_2$  is  $\ell_2$ 

We need:

$$
\|x\|_{2,*} := \sup_{\|u\|_2\le 1} u^\top x.
$$

By Cauchy–Schwarz:

$$
u^\top x \le \|u\|_2\|x\|_2 \le 1\cdot \|x\|_2 = \|x\|_2.
$$

So the supremum is at most  $\|x\|_2$ .

Achievability: if  $x\neq 0$ , choose  $u = x/\|x\|_2$ . Then  $\|u\|_2=1$  and

$$
u^\top x = \frac{x^\top x}{\|x\|_2} = \frac{\|x\|_2^2}{\|x\|_2} = \|x\|_2.
$$

So the supremum is exactly  $\|x\|_2$ .

Thus:

$$
\boxed{\|x\|_{2,*} = \|x\|_2.}
$$

### 5.2 Dual of  $\ell_\infty$  is  $\ell_1$ 

Compute:

$$
\|x\|_{\infty,*} := \sup_{\|u\|_\infty\le 1} u^\top x.
$$

The constraint  $\|u\|_\infty\le 1$  means  $|u_i|\le 1$  for every component.

Then:

$$
u^\top x = \sum_{i=1}^n u_i x_i \le \sum_{i=1}^n |u_i||x_i| \le \sum_{i=1}^n |x_i| = \|x\|_1.
$$

So supremum ≤  $\|x\|_1$ .

Achievability: pick  $u_i = \operatorname{sign}(x_i)$  (with  $\operatorname{sign}(0)$  any value in  $[-1,1]$ ). Then  $|u_i|\le 1$ , and

$$
u^\top x = \sum_i \operatorname{sign}(x_i)x_i = \sum_i |x_i| = \|x\|_1.
$$

So supremum =  $\|x\|_1$ .

Thus:

$$
\boxed{\|x\|_{\infty,*} = \|x\|_1.}
$$

### 5.3 Dual of  $\ell_1$  is  $\ell_\infty$ 

Compute:

$$
\|x\|_{1,*} := \sup_{\|u\|_1\le 1} u^\top x.
$$

We can bound:

$$
u^\top x = \sum_i u_i x_i \le \sum_i |u_i||x_i| \le \left(\max_i |x_i|\right)\sum_i |u_i| \le \|x\|_\infty \cdot 1 = \|x\|_\infty.
$$

So supremum ≤  $\|x\|_\infty$ .

Achievability: let  $j$  be an index where  $|x_j|=\|x\|_\infty$ . Choose  $u$  with all mass on coordinate  $j$ :

$$
u_j = \operatorname{sign}(x_j),\quad u_i=0\ (i\neq j).
$$

Then  $\|u\|_1 = 1$  and

$$
u^\top x = \operatorname{sign}(x_j)x_j = |x_j| = \|x\|_\infty.
$$

So supremum =  $\|x\|_\infty$ .

Thus:

$$
\boxed{\|x\|_{1,*} = \|x\|_\infty.}
$$

Those three dualities are the engine behind “uncertainty norm ⇒ robust constraint norm ⇒ LP/SOCP.”

* * *

6) Concrete robust constraints and solver class (LP vs SOCP)
------------------------------------------------------------

We now plug the dual norms into:

$$
a^\top x + \rho\|x\|_* \le b.
$$

### 6.1 If uncertainty is  $\ell_2$ :  $\|u\|_2\le\rho$ 

Then  $\|x\|_*=\|x\|_2$ , so robust constraint is:

$$
a^\top x + \rho\|x\|_2 \le b.
$$

Rearrange into a standard SOC form:

$$
\rho\|x\|_2 \le b-a^\top x.
$$

This is exactly “norm ≤ affine”, hence SOCP:

$$
\boxed{(b-a^\top x,\ \rho x)\in \mathcal{Q}_{n+1}.}
$$

Feasibility automatically enforces  $b-a^\top x\ge 0$ , as it must (since the LHS is nonnegative).

**Conclusion:**  $\ell_2$  uncertainty → SOC constraint → SOCP.

* * *

### 6.2 If uncertainty is  $\ell_\infty$ :  $\|u\|_\infty\le\rho$ 

Then  $\|x\|_*=\|x\|_1$ , so:

$$
a^\top x + \rho\|x\|_1 \le b.
$$

 $\|x\|_1$  is LP-representable (Phase 5.2). Introduce  $s_i\ge |x_i|$ :

$$
x_i \le s_i,\quad -x_i \le s_i,\quad i=1,\dots,n.
$$

Then  $\|x\|_1 = \sum_i |x_i|$  becomes  $\sum_i s_i$  in the lifted formulation:

$$
a^\top x + \rho\sum_{i=1}^n s_i \le b.
$$

All linear.

**Conclusion:**  $\ell_\infty$  uncertainty → dual  $\ell_1$  term → LP.

* * *

### 6.3 If uncertainty is  $\ell_1$ :  $\|u\|_1\le\rho$ 

Then  $\|x\|_*=\|x\|_\infty$ , so:

$$
a^\top x + \rho\|x\|_\infty \le b.
$$

 $\|x\|_\infty$  is LP-representable (Phase 5.2). Introduce scalar  $t$  with  $|x_i|\le t$ :

$$
x_i \le t,\quad -x_i \le t,\quad \forall i,
$$

then  $\|x\|_\infty$  becomes  $t$  in lifted form:

$$
a^\top x + \rho t \le b.
$$

All linear.

**Conclusion:**  $\ell_1$  uncertainty → dual  $\ell_\infty$  term → LP.

* * *

7) Row-wise robustification (multiple constraints)
--------------------------------------------------

Often you have many constraints, each with its own uncertain row:

$$
(a_i + u_i)^\top x \le b_i,\qquad \forall u_i\in \mathcal U_i,\quad i=1,\dots,m.
$$

This is equivalent to imposing, for each  $i$ ,

$$
a_i^\top x + \sup_{u_i\in\mathcal U_i} u_i^\top x \le b_i.
$$

If  $\mathcal U_i = \{u:\|u\|\le \rho_i\}$ , then

$$
a_i^\top x + \rho_i\|x\|_* \le b_i.
$$

So robustification is typically **row-separable**: each constraint picks up its own norm penalty term.

Solver class again depends on  $\|\cdot\|_*$ .

* * *

8) More general robust affine constraints (uncertainty through a linear map)
----------------------------------------------------------------------------

A very common extension is uncertainty enters as  $B u$ , not  $u$  directly:

$$
(a + B u)^\top x \le b \quad \forall u:\ \|u\|\le\rho.
$$

Expand:

$$
a^\top x + u^\top (B^\top x) \le b\quad \forall \|u\|\le\rho.
$$

Worst case:

$$
a^\top x + \sup_{\|u\|\le\rho} u^\top (B^\top x) \le b.
$$

By the same theorem:

$$
\sup_{\|u\|\le\rho} u^\top (B^\top x)=\rho\|B^\top x\|_*.
$$

So:

$$
\boxed{a^\top x + \rho\|B^\top x\|_* \le b.}
$$

This is where robust constraints often produce norms of _linear transforms_ of  $x$ , like  $\|M x\|_2$  or  $\|M x\|_1$ , etc., which then map to SOCP or LP via Phase 5.2/5.3.

* * *

9) Why this is convex (not vibes—actual reason)
-----------------------------------------------

After robustification, you get constraints like:

$$
a^\top x + \rho\|M x\|_* \le b.
$$
*    $a^\top x$  is affine.
*    $\|M x\|_*$  is a norm of an affine map, hence convex.
*   Convex function ≤ constant defines a convex set.

And if you express the norm via LP atoms ( $\ell_1,\ell_\infty$ ) or SOC atoms ( $\ell_2$ ), you get an LP or SOCP formulation.

* * *

10) Common traps (the ones that silently ruin correctness)
----------------------------------------------------------

1.  **Forgetting to center the uncertainty set at 0**  
    The dual norm identity  $\sup_{\|u\|\le\rho} u^\top x = \rho\|x\|_*$  assumes the set is a centered norm ball.  
    If  $\mathcal U$  is shifted (e.g.,  $u\in u_0 + \rho B$ ), the support function becomes  $u_0^\top x + \rho\|x\|_*$ . You must include the shift.
2.  **Wrong dual norm pairing**  
     $\ell_1 \leftrightarrow \ell_\infty$ ,  $\ell_2 \leftrightarrow \ell_2$ ,  $\ell_\infty \leftrightarrow \ell_1$ . One swap and you’ll end up with the wrong cone class.
3.  **Mixing “robustification of coefficients” vs “robustification of RHS”**  
    If  $b$  is uncertain too, the robust constraint becomes:
    
$$
(a+u)^\top x \le b - \delta \quad \forall (u,\delta)\in\mathcal U,
$$

and you must move  $-\delta$  into the supremum carefully:

$$
\sup_{(u,\delta)\in\mathcal U} (u^\top x + \delta) \le b-a^\top x.
$$

Same support-function idea, but in a higher-dimensional uncertainty set.

4.  **Thinking “ $\forall u$ ” always becomes a norm**  
    It becomes a support function  $\sigma_{\mathcal U}(x)$ . It is a norm **only** when  $\mathcal U$  is a centered symmetric convex body that is a scaled unit ball of a norm. Otherwise it can be something else (still convex, but not necessarily a norm).

* * *

11) The mechanical pipeline (what you do in 20 seconds)
-------------------------------------------------------

Given:

$$
(a+ \text{uncertainty})^\top x \le b \quad \forall u\in\mathcal U,
$$

do:

1.  Expand:  $a^\top x + u^\top(\text{something in }x)\le b$ .
2.  Replace  $\forall$  with supremum:
    
$$
a^\top x + \sup_{u\in\mathcal U} u^\top(\cdot)\le b.
$$
3.  If  $\mathcal U$  is a norm ball  $\|u\|\le\rho$ , replace supremum with  $\rho\|\cdot\|_*$ .
4.  Identify dual norm, then model it:
    *    $\|\cdot\|_1,\|\cdot\|_\infty$  → LP atoms (Phase 5.2)
*    $\|\cdot\|_2$  → SOC atom (Phase 5.3)

That’s Phase 5.5.

* * *

If you want to go one layer deeper than your notes: the whole story is really “robustification = support function; support function of a polar set; dual norm = gauge of the polar.” That’s the convex-geometry core that unifies everything (and makes later duality proofs feel inevitable rather than memorized).

## Response:
Phase 5.6 is where “matrix inverse inside a quadratic” stops being terrifying and becomes one clean **PSD block matrix** constraint. The Schur complement is the exact bridge.

I’ll do this in a way you can reproduce on an exam:

1.  define precisely what we’re modeling (and why it’s convex),
2.  state Schur complement correctly (including the _conditions_ under which it is equivalent),
3.  derive the canonical atom  $x^\top X^{-1}x \le t \iff \begin{bmatrix}X&x\\x^\top&t\end{bmatrix}\succeq 0$ ,
4.  handle the important variants (affine maps; matrix RHS),
5.  clarify the subtle domain issues ( $X\succeq 0$  vs  $X\succ 0$ ),
6.  explain when a quadratic can be SOCP instead (constant matrix case) so you don’t mix 5.4 and 5.6,
7.  give a mechanical translator.

* * *

0) What “quadratic epigraph” means in Phase 5.6
-----------------------------------------------

### 0.1 Epigraph trick (general principle)

Given some possibly complicated function  $f(\text{variables})$ , an **epigraph constraint** is

$$
f(\cdot)\le t
$$

where  $t$  is a new scalar variable.

Why we do this: if our original objective is to minimize  $f(\cdot)$ , we can rewrite

$$
\min f(\cdot) \quad\Longleftrightarrow\quad \min_{(\cdot),t} t \ \text{s.t.}\ f(\cdot)\le t.
$$

This makes the objective linear (minimize  $t$ ) and moves all complexity into constraints.

You already used this for:

*    $|u|\le t$  (LP epigraph),
*    $\|Ax+b\|_2\le t$  (SOC epigraph).

### 0.2 What’s new here

Now  $f$  is of the form

$$
x^\top X^{-1}x,
$$

or more generally,

$$
(Ax+b)^\top X^{-1}(Ax+b),
$$

where crucially ** $X$  itself is a decision variable** (typically symmetric PSD).

This is the “tell”: _inverse of a matrix variable inside a quadratic form_.

LP and SOCP are usually too weak to encode this exactly. SDP can, because it allows **linear matrix inequalities (LMIs)** involving PSD matrices, and the Schur complement turns inverse-quadratic relations into LMIs.

* * *

1) SDP primitives you must be fluent in (precise and usable)
------------------------------------------------------------

### 1.1 PSD cone and Loewner order

Let  $\mathbb{S}^n$  be symmetric  $n\times n$  matrices.

*    $M\succeq 0$  (PSD) means:
    $$
    z^\top M z \ge 0\quad \forall z\in\mathbb{R}^n.
    $$
*    $M\succ 0$  (PD) means:
    $$
    z^\top M z > 0\quad \forall z\neq 0.
    $$
*    $A\preceq B$  means  $B-A\succeq 0$ .

### 1.2 What is an LMI?

An LMI is:

$$
F(x)=F_0+x_1F_1+\cdots+x_kF_k \succeq 0,
$$

where each  $F_i$  is a fixed symmetric matrix, and dependence on decision variables is **affine**.

An SDP is “minimize linear objective subject to LMIs”.

So: to show “this is SDP-representable”, you want to rewrite constraints into the form “a symmetric matrix affine in variables is PSD”.

* * *

2) The Schur complement theorem (state it correctly)
----------------------------------------------------

Consider a symmetric block matrix

$$
M= \begin{bmatrix} A & B\\ B^\top & C \end{bmatrix},
$$

with  $A\in\mathbb{S}^n$ ,  $C\in\mathbb{S}^m$ ,  $B\in\mathbb{R}^{n\times m}$ .

### 2.1 Theorem (Schur complement w.r.t.  $A$ )

If  $A\succ 0$ , then:

$$
\boxed{ \begin{bmatrix} A & B\\ B^\top & C \end{bmatrix}\succeq 0 \quad\Longleftrightarrow\quad C - B^\top A^{-1}B \succeq 0. }
$$

The matrix  $C-B^\top A^{-1}B$  is the **Schur complement of  $A$  in  $M$ **.

### 2.2 Twin version (w.r.t.  $C$ )

If  $C\succ 0$ , then:

$$
\boxed{ M\succeq 0 \quad\Longleftrightarrow\quad A - B C^{-1} B^\top \succeq 0. }
$$

### 2.3 Why this theorem is the “inverse eliminator”

The “hard” object  $A^{-1}$  appears in the Schur complement. The theorem says:

*   A PSD block constraint (nice for SDP),
*   is equivalent to a constraint involving  $A^{-1}$  (hard to model directly),

provided the block you invert is PD.

So it’s literally a legal algebraic mechanism for removing  $X^{-1}$  from your formulation.

* * *

3) The Phase 5.6 atom:  $x^\top X^{-1}x \le t$  ⇔ block LMI
-----------------------------------------------------------

### 3.1 Problem form

Variables:

*    $X\in\mathbb{S}^n$  (typically  $X\succ 0$ ),
*    $x\in\mathbb{R}^n$ ,
*    $t\in\mathbb{R}$ .

Constraint:

$$
x^\top X^{-1}x \le t,\qquad X\succ 0.
$$

### 3.2 Claim (exact equivalence)

$$
\boxed{ x^\top X^{-1}x \le t,\ X\succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0. }
$$

This is the canonical modeling move.

* * *

### 3.3 Proof (direction-by-direction, fully explicit)

Let

$$
M := \begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}.
$$

This is symmetric.

Assume  $X\succ 0$ , so  $X^{-1}$  exists. Apply Schur complement w.r.t.  $A=X$ . Here:

*    $A=X$ ,
*    $B=x$  (viewed as an  $n\times 1$  column),
*    $C=t$  (a  $1\times 1$  matrix, i.e., scalar).

Schur complement says:

$$
M\succeq 0 \quad\Longleftrightarrow\quad t - x^\top X^{-1}x \ge 0.
$$

But  $t - x^\top X^{-1}x \ge 0$  is exactly:

$$
x^\top X^{-1}x \le t.
$$

So under  $X\succ 0$ ,

$$
M\succeq 0 \iff x^\top X^{-1}x \le t.
$$

That’s the equivalence.

* * *

### 3.4 Why this is an SDP constraint

The block matrix

$$
\begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}
$$

is **affine** in variables  $(X,x,t)$ : entries are either components of  $X$ , components of  $x$ , or  $t$ , with no products between decision variables.

Constraint “this matrix is PSD” is an LMI. Therefore the set is SDP-representable.

* * *

4) Variants you must recognize instantly
----------------------------------------

### 4.1 Affine expression inside the quadratic:  $(Ax+b)^\top X^{-1}(Ax+b)\le t$ 

Let  $y := Ax+b$  (so  $y$  is affine in  $x$ ). Then the constraint is  $y^\top X^{-1}y \le t$ . Apply the same atom:

$$
\boxed{ (Ax+b)^\top X^{-1}(Ax+b)\le t,\ X\succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} X & Ax+b\\ (Ax+b)^\top & t \end{bmatrix}\succeq 0. }
$$

Why still LMI:  $Ax+b$  is affine in  $x$ , so every block entry is affine in decision variables.

* * *

### 4.2 “Weighted norm / Mahalanobis norm” notation

Define:

$$
\|x\|_{X^{-1}}^2 := x^\top X^{-1}x.
$$

Then:

$$
\boxed{ \|x\|_{X^{-1}}^2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0, \ \ (X\succ 0). }
$$

* * *

### 4.3 Matrix inequality version:  $Y^\top X^{-1}Y \preceq T$ 

Now  $Y\in\mathbb{R}^{n\times k}$ ,  $T\in\mathbb{S}^k$ . Consider:

$$
Y^\top X^{-1}Y \preceq T,\quad X\succ 0.
$$

Form the block matrix:

$$
M= \begin{bmatrix} X & Y\\ Y^\top & T \end{bmatrix}.
$$

Apply Schur complement w.r.t.  $X$ :

$$
M\succeq 0 \iff T - Y^\top X^{-1}Y \succeq 0 \iff Y^\top X^{-1}Y \preceq T.
$$

So:

$$
\boxed{ Y^\top X^{-1}Y \preceq T,\ X\succ 0 \quad\Longleftrightarrow\quad \begin{bmatrix} X & Y\\ Y^\top & T \end{bmatrix}\succeq 0. }
$$

This form appears constantly in control/estimation (Kalman filtering, covariance bounds, etc.).

* * *

5) “But  $x^\top P x \le t$  can be SOCP sometimes”—what’s the boundary?
------------------------------------------------------------------------

This is a crucial conceptual fork. You pointed it out, and you must keep it straight.

### 5.1 Constant quadratic form (often SOCP/RSOC)

If  $P\succeq 0$  is a **constant matrix** (not a decision variable), then you can factor it as  $P=R^\top R$  (Cholesky or square root). Then:

$$
x^\top P x = x^\top R^\top R x = \|Rx\|_2^2.
$$

So:

$$
x^\top P x \le t \iff \|Rx\|_2^2 \le t.
$$

And  $\|Rx\|_2^2 \le t$  is a **rotated SOC** constraint (Phase 5.4) or SOC with auxiliary variables. So constant-quadratic constraints can live in SOCP land.

### 5.2 Variable inverse quadratic (SDP-native)

If the matrix is a **variable**  $X$  and the expression is  $x^\top X^{-1}x$ , you cannot pre-factor  $X^{-1}$  with a constant  $R$ . The factorization would depend on decision variables, which breaks SOC representability in general.

So Phase 5.6 is about the genuinely SDP-flavored case: **inverse of a matrix variable**.

Mental rule you should internalize:

*   “ $\|Ax\|_2$ ” → SOC (Phase 5.3),
*   “ $\|Ax\|_2^2 \le xy$ ” → rotated SOC (Phase 5.4),
*   “ $x^\top X^{-1}x$ ” with  $X$  variable → Schur complement → SDP (Phase 5.6).

* * *

6) Epigraph usage: turning a scary objective into linear objective + LMI
------------------------------------------------------------------------

Suppose you want:

$$
\min_{x,X} x^\top X^{-1}x \quad \text{s.t. } X\succ 0,\ \text{other constraints}.
$$

Introduce epigraph  $t$ :

$$
\min_{x,X,t} t \quad \text{s.t.}\quad x^\top X^{-1}x \le t,\ \ X\succ 0.
$$

Now replace the quadratic epigraph constraint using the atom:

$$
\boxed{ \min_{x,X,t} t \quad\text{s.t.}\quad \begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0,\ \ X\succ 0,\ \text{(other constraints)}. }
$$

Now you have: linear objective + LMIs → SDP.

* * *

7) Domain subtleties that matter (where people lose points)
-----------------------------------------------------------

### 7.1 What if  $X\succeq 0$  but not  $X\succ 0$ ?

Then  $X^{-1}$  does not exist, so the expression  $x^\top X^{-1}x$  is not defined in the usual sense.

There are two common ways this is handled:

1.  **Strict PD assumption in the model**: require  $X\succ 0$  (or numerically  $X\succeq \epsilon I$ ) so inverse exists.
2.  **Convex closed extension** (advanced): interpret  $x^\top X^{-1}x$  as
    $$
    \begin{cases} x^\top X^\dagger x & \text{if } x\in \mathrm{Range}(X),\\ +\infty & \text{otherwise,} \end{cases}
    $$
    where  $X^\dagger$  is the pseudoinverse. Under this interpretation, the block LMI  
     $\begin{bmatrix}X&x\\x^\top&t\end{bmatrix}\succeq 0$   
    describes the epigraph of that closed convex function even when  $X$  is singular.

Most course/homework settings keep it simple and state  $X\succ 0$ . If they only say  $X\succeq 0$ , it’s a hint they may want you to recognize the block LMI is still the right convex representation (it automatically enforces compatibility between  $x$  and  $X$ ).

### 7.2 Nonnegativity of  $t$ 

From PSD:

$$
\begin{bmatrix} X & x\\ x^\top & t \end{bmatrix}\succeq 0 \Rightarrow t\ge 0
$$

because principal minors / diagonal entries of a PSD matrix are nonnegative. So you usually don’t need to add  $t\ge 0$ .

* * *

8) Mechanical translator (the “no-thinking” checklist)
------------------------------------------------------

Whenever you see an inverse quadratic pattern:

### Pattern A: scalar

$$
(\text{affine vector})^\top X^{-1}(\text{affine vector}) \le t,\quad X\succ 0.
$$

Replace with:

$$
\boxed{ \begin{bmatrix} X & \text{affine vector}\\ (\text{affine vector})^\top & t \end{bmatrix}\succeq 0. }
$$

### Pattern B: matrix

$$
(\text{matrix})^\top X^{-1}(\text{matrix}) \preceq T,\quad X\succ 0.
$$

Replace with:

$$
\boxed{ \begin{bmatrix} X & \text{matrix}\\ (\text{matrix})^\top & T \end{bmatrix}\succeq 0. }
$$

### Pattern C: objective

If the inverse quadratic is the objective, introduce  $t$  and minimize  $t$ , then apply Pattern A/B.

That’s Phase 5.6.

* * *

9) Conceptual punchline (what’s really happening)
-------------------------------------------------

The Schur complement is a **lifting identity**:

*   A constraint with an inverse (nonlinear, scary),
*   becomes PSD of a larger block matrix (linear in variables, solver-friendly).

SDP is the language where “inverse-aware convexity” becomes linear constraints in the PSD cone.

* * *

If you want the natural continuation, Phase 5.7 is where “spectral” constraints like  $\lambda_{\max}(F(x))\le t$  become LMIs via  $F(x)\preceq tI$ . It’s the same Loewner-order worldview: eigenvalues become PSD inequalities, and PSD inequalities are SDPs.

## Response:
Phase 5.7 is the “spectral-to-LMI dictionary.” Once you internalize it, anything that smells like “largest eigenvalue,” “smallest eigenvalue,” “spectral norm,” “all eigenvalues in an interval,” or “matrix is PSD” becomes a clean **PSD-order inequality**, i.e. an **LMI**, i.e. an SDP constraint.

I’m going to build this from bedrock and keep it exam-proof: definitions → theorems → equivalences → modeling templates → tricky edge cases → the “don’t die on points” traps.

* * *

0) Ground layer: why symmetry is non-negotiable
-----------------------------------------------

Everything below is about **real symmetric matrices**  $A\in\mathbb{S}^n$ .

Why?

1.  A symmetric real matrix has **real** eigenvalues.
2.  It is **orthogonally diagonalizable**:
    
$$
A = Q\Lambda Q^\top,\qquad Q^\top Q = I,\qquad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n)\in\mathbb{R}^{n\times n}.
$$
3.  PSD order has a clean meaning in terms of eigenvalues.

If  $A$  is not symmetric, eigenvalues may be complex and PSD order is not defined for it in the same way. For non-symmetric matrices you usually pivot to **singular values** / **spectral norm**, which are always real and can be handled via a symmetric block matrix (we’ll do that later).

* * *

1) PSD order is “eigenvalues are nonnegative” (prove it properly)
-----------------------------------------------------------------

### 1.1 Definitions

*    $A\succeq 0$  means:
    
$$
z^\top A z \ge 0\quad \forall z\in\mathbb{R}^n.
$$
*    $A\succ 0$  means:
    
$$
z^\top A z > 0\quad \forall z\neq 0.
$$

### 1.2 Fundamental equivalence

$$
\boxed{ A\succeq 0 \quad\Longleftrightarrow\quad \lambda_i(A)\ge 0\ \ \forall i. }
$$

#### Proof (fully explicit via diagonalization)

Assume  $A$  is symmetric, so  $A = Q\Lambda Q^\top$  with orthogonal  $Q$ .

Take any  $z\in\mathbb{R}^n$ . Because  $Q$  is orthogonal, the map  $y\mapsto z=Qy$  is a bijection; i.e., “for all  $z$ ” is the same as “for all  $y$ ”.

Compute:

$$
z^\top A z = (Qy)^\top (Q\Lambda Q^\top)(Qy) = y^\top \Lambda y = \sum_{i=1}^n \lambda_i y_i^2.
$$

Now:

*   If all  $\lambda_i\ge 0$ , then each term  $\lambda_i y_i^2 \ge 0$ , so the sum is  $\ge 0$  for all  $y$ , hence for all  $z$ . So  $A\succeq 0$ .
*   Conversely, if some  $\lambda_k<0$ , choose  $y=e_k$  (the vector with 1 in position  $k$ , 0 elsewhere). Then
    
$$
y^\top \Lambda y = \lambda_k < 0,
$$

so  $z^\top A z<0$  for  $z=Qe_k$ , contradicting  $A\succeq 0$ . Therefore no eigenvalue can be negative.

So PSD is exactly “all eigenvalues are nonnegative.”

This is the core reason eigenvalue constraints become PSD constraints.

* * *

2) Loewner order is “quadratic form dominance”
----------------------------------------------

### 2.1 Definition

$$
A \preceq B \quad\Longleftrightarrow\quad B-A \succeq 0.
$$

### 2.2 Equivalent “for all vectors” form

$$
A\preceq B \quad\Longleftrightarrow\quad z^\top A z \le z^\top B z\ \ \forall z.
$$

#### Proof

 $B-A\succeq 0$  means  $z^\top(B-A)z\ge 0\ \forall z$ , i.e.

$$
z^\top B z - z^\top A z \ge 0\ \forall z \iff z^\top A z \le z^\top B z\ \forall z.
$$

So PSD order is literally an “all directions” inequality of quadratic forms.

This perspective is what makes the spectral templates feel inevitable rather than memorized.

* * *

3) The single most important atom:  $\lambda_{\max}(A)\le t$  ⇔  $A\preceq tI$ 
-------------------------------------------------------------------------------

### 3.1 Define  $\lambda_{\max}$  rigorously

For symmetric  $A$ , let its eigenvalues be ordered  $\lambda_1\le \cdots\le \lambda_n$ . Then:

$$
\lambda_{\max}(A) := \lambda_n.
$$

There is also the Rayleigh quotient characterization (useful intuition, and sometimes used in proofs):

$$
\boxed{\lambda_{\max}(A)=\max_{\|z\|_2=1} z^\top A z.}
$$

I’ll justify it later, but the LMI equivalence can be proved without it.

### 3.2 The equivalence

$$
\boxed{ \lambda_{\max}(A)\le t \quad\Longleftrightarrow\quad A \preceq tI \quad\Longleftrightarrow\quad tI - A \succeq 0. }
$$

#### Proof (diagonalization; clean and exam-friendly)

Diagonalize  $A=Q\Lambda Q^\top$ . Then

$$
tI - A = tI - Q\Lambda Q^\top = Q(tI-\Lambda)Q^\top.
$$

Key fact: orthogonal similarity  $Q(\cdot)Q^\top$  preserves eigenvalues. So the eigenvalues of  $tI-A$  are the diagonal entries of  $tI-\Lambda$ , i.e.  $t-\lambda_i$ .

Therefore:

$$
tI-A\succeq 0 \iff t-\lambda_i \ge 0\ \forall i \iff \lambda_i \le t\ \forall i \iff \lambda_{\max}(A)\le t.
$$

Done.

### 3.3 Modeling consequence

If  $A(x)$  is **affine** in decision variables  $x$  (i.e.  $A(x)=A_0+\sum_j x_j A_j$ ), then

$$
\lambda_{\max}(A(x))\le t
$$

becomes

$$
\boxed{tI - A(x)\succeq 0,}
$$

which is an LMI because its entries are affine in  $(x,t)$ .

This is the workhorse of spectral SDPs.

* * *

4) Sister atom:  $\lambda_{\min}(A)\ge t$  ⇔  $A\succeq tI$ 
------------------------------------------------------------

Define  $\lambda_{\min}(A)=\lambda_1$ . Then:

$$
\boxed{ \lambda_{\min}(A)\ge t \quad\Longleftrightarrow\quad A\succeq tI \quad\Longleftrightarrow\quad A-tI\succeq 0. }
$$

Proof: eigenvalues of  $A-tI$  are  $\lambda_i-t$ . PSD means  $\lambda_i-t\ge 0\ \forall i$ , i.e. all  $\lambda_i\ge t$ , i.e. the minimum is  $\ge t$ .

* * *

5) “All eigenvalues lie in  $[l,u]$ ” becomes two LMIs
------------------------------------------------------

Statement:

$$
l \le \lambda_i(A) \le u\quad \forall i.
$$

This is equivalent to:

*   smallest eigenvalue  $\ge l$ ,
*   largest eigenvalue  $\le u$ .

So:

$$
\boxed{ lI \preceq A \preceq uI \quad\Longleftrightarrow\quad A-lI\succeq 0,\ \ uI-A\succeq 0. }
$$

If  $A=A(x)$  is affine, this becomes two LMIs affine in  $x$ .

* * *

6) Spectral norm / operator norm: symmetric vs general matrices
---------------------------------------------------------------

This is where people commonly confuse SOCP vs SDP territory.

### 6.1 Symmetric matrix case:  $\|A\|_2\le t$ 

For symmetric  $A$ , singular values are  $|\lambda_i(A)|$ . So:

$$
\|A\|_2 = \max_i |\lambda_i(A)| = \max\{\lambda_{\max}(A),\ -\lambda_{\min}(A)\}.
$$

Thus:

$$
\|A\|_2 \le t \iff -\;t \le \lambda_i(A) \le t\ \forall i \iff -tI \preceq A \preceq tI.
$$

Which is two LMIs:

$$
\boxed{ \|A\|_2\le t \quad\Longleftrightarrow\quad tI-A\succeq 0,\ \ tI + A\succeq 0. }
$$

### 6.2 General rectangular matrix case:  $\|M\|_2\le t$ 

Let  $M\in\mathbb{R}^{m\times n}$ . Then  $\|M\|_2$  is the largest singular value. Singular values are square roots of eigenvalues of  $M^\top M$  (or  $MM^\top$ ):

$$
\|M\|_2\le t \iff M^\top M \preceq t^2 I_n \iff MM^\top \preceq t^2 I_m.
$$

But  $M^\top M \preceq t^2I$  is **not** an LMI in  $(M,t)$  if  $M$  is variable, because it involves quadratic terms in  $M$ . The SDP trick is to use a symmetric block matrix:

$$
\boxed{ \|M\|_2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} tI_m & M\\ M^\top & tI_n \end{bmatrix}\succeq 0. }
$$

This is a standard, extremely important template.

#### Proof (via Schur complement; explicit)

Assume  $t>0$  (we’ll discuss  $t=0$  after). Consider:

$$
S= \begin{bmatrix} tI_m & M\\ M^\top & tI_n \end{bmatrix}.
$$

Take Schur complement with respect to  $tI_m\succ 0$ :

$$
S\succeq 0 \iff tI_n - M^\top (tI_m)^{-1} M \succeq 0.
$$

Since  $(tI_m)^{-1} = \frac{1}{t}I_m$ ,

$$
tI_n - \frac{1}{t}M^\top M \succeq 0.
$$

Multiply by  $t>0$ :

$$
t^2 I_n - M^\top M \succeq 0 \iff M^\top M \preceq t^2 I_n.
$$

Now  $M^\top M \preceq t^2 I$  means all eigenvalues of  $M^\top M$  are  $\le t^2$ , so the largest singular value squared is  $\le t^2$ , i.e.  $\|M\|_2\le t$ .

Conversely, if  $\|M\|_2\le t$ , then  $M^\top M\preceq t^2I$ , which implies  $S\succeq 0$  by reversing the steps.

For  $t=0$ :  $\|M\|_2\le 0$  implies  $M=0$ , and the block matrix becomes  $\begin{bmatrix}0&M\\M^\top&0\end{bmatrix}$ , PSD only if  $M=0$ . So the equivalence still holds.

So the template is exact.

**Modeling consequence:** if  $M(x)$  is affine in decision variables, then  $\|M(x)\|_2\le t$  is an LMI → SDP.

This is one of the clearest “SDP beats SOCP” boundary lines: vector Euclidean norms are SOC; matrix spectral norms are SDP.

* * *

7) Rayleigh quotient: why  $\lambda_{\max}(A)=\max_{\|z\|=1} z^\top A z$ 
-------------------------------------------------------------------------

This is not strictly required to model  $\lambda_{\max}$  as an LMI, but it builds the intuition and is sometimes asked.

Let  $A=Q\Lambda Q^\top$ . For  $\|z\|_2=1$ , write  $z=Qy$ . Since  $Q$  is orthogonal,  $\|y\|_2=\|z\|_2=1$ .

Then:

$$
z^\top A z = y^\top \Lambda y = \sum_i \lambda_i y_i^2.
$$

Because  $y_i^2\ge 0$  and  $\sum_i y_i^2 = 1$ , the quantity  $\sum_i \lambda_i y_i^2$  is a convex combination of the  $\lambda_i$ ’s, hence lies between  $\min\lambda_i$  and  $\max\lambda_i$ . The maximum possible value is achieved by putting all weight on the largest eigenvalue coordinate: choose  $y=e_{i^*}$  where  $\lambda_{i^*}=\lambda_{\max}$ . Then  $z=Qe_{i^*}$  gives:

$$
z^\top A z = \lambda_{\max}.
$$

So:

$$
\max_{\|z\|=1} z^\top A z = \lambda_{\max}(A).
$$

Similarly:

$$
\min_{\|z\|=1} z^\top A z = \lambda_{\min}(A).
$$

This is the deep link: PSD order statements are “uniform over all directions” quadratic inequalities, and eigenvalues are extreme directional quadratic values.

* * *

8) Affine matrix functions  $A(x)$ : why eigenvalue constraints become SDPs
---------------------------------------------------------------------------

Most real modeling uses

$$
A(x)=A_0+\sum_{j=1}^k x_j A_j,
$$

with fixed symmetric  $A_j$ .

Then:

*    $A(x)\succeq 0$  is already an LMI.
*    $\lambda_{\max}(A(x))\le t$  becomes  $tI-A(x)\succeq 0$ .
*    $\lambda_{\min}(A(x))\ge t$  becomes  $A(x)-tI\succeq 0$ .
*   eigenvalues in  $[l,u]$  becomes  $A(x)-lI\succeq 0$  and  $uI-A(x)\succeq 0$ .
*   symmetric  $\|A(x)\|_2\le t$  becomes  $tI\pm A(x)\succeq 0$ .
*   general  $\|M(x)\|_2\le t$  becomes the block LMI  $\begin{bmatrix}tI & M(x)\\M(x)^\top & tI\end{bmatrix}\succeq 0$ .

All are affine-in-variables PSD constraints → SDP.

* * *

9) The templates (what you “deploy instantly”)
----------------------------------------------

I’ll write them in the exact form you’d drop into a solver or into a PS solution.

### Template 1: largest eigenvalue upper bound

For symmetric  $A(x)$ :

$$
\boxed{\lambda_{\max}(A(x))\le t\ \Longleftrightarrow\ tI-A(x)\succeq 0.}
$$

### Template 2: smallest eigenvalue lower bound

$$
\boxed{\lambda_{\min}(A(x))\ge t\ \Longleftrightarrow\ A(x)-tI\succeq 0.}
$$

### Template 3: spectrum in an interval  $[l,u]$ 

$$
\boxed{lI\preceq A(x)\preceq uI\ \Longleftrightarrow\ A(x)-lI\succeq 0,\ \ uI-A(x)\succeq 0.}
$$

### Template 4: symmetric spectral norm bound

(assuming  $A(x)$  symmetric)

$$
\boxed{\|A(x)\|_2\le t\ \Longleftrightarrow\ tI-A(x)\succeq 0,\ \ tI+A(x)\succeq 0.}
$$

### Template 5: general (rectangular) spectral norm bound

$$
\boxed{\|M(x)\|_2\le t\ \Longleftrightarrow\ \begin{bmatrix}tI_m & M(x)\\M(x)^\top & tI_n\end{bmatrix}\succeq 0.}
$$

(Here  $M(x)\in\mathbb{R}^{m\times n}$ .)

* * *

10) Failure modes (the silent point-killers)
--------------------------------------------

### 10.1 Forgetting symmetry

Constraints like  $tI-A\succeq 0$  require  $A$  symmetric. If your matrix expression isn’t symmetric, you must either:

*   symmetrize it (if the problem intended that), e.g. use  $(A+A^\top)/2$ , or
*   switch to singular values / spectral norm using Template 5.

### 10.2 Confusing PSD order with entrywise inequality

 $A\preceq tI$  does **not** mean “each entry of  $A$  is  $\le t$ ”. PSD order is about quadratic forms / eigenvalues, not elementwise comparisons.

### 10.3 Dropping the identity

The comparison is always to  $tI$ , not to a scalar  $t$ . The PSD cone lives in matrix space; the scalar must be lifted via  $I$ .

### 10.4 Mixing up min vs max

*    $\lambda_{\max}(A)\le t$  →  $tI-A\succeq 0$ .
*    $\lambda_{\min}(A)\ge t$  →  $A-tI\succeq 0$ .  
    Swap these and you invert the constraint.

### 10.5 Sign mistakes for spectral norm

For symmetric  $A$ ,  $\|A\|_2\le t$  requires both sides:

$$
-tI\preceq A\preceq tI \iff tI-A\succeq 0\ \text{and}\ tI+A\succeq 0.
$$

People often write only one and accidentally bound only  $\lambda_{\max}$ , not absolute eigenvalues.

* * *

11) The intuition that makes it stick (so you don’t memorize)
-------------------------------------------------------------

Think of the inequality  $\lambda_{\max}(A)\le t$  as:

“On the unit sphere, the quadratic form  $z^\top A z$  is never bigger than  $t$ .”

Because:

$$
\lambda_{\max}(A)=\max_{\|z\|=1} z^\top A z.
$$

So  $\lambda_{\max}(A)\le t$  is exactly:

$$
z^\top A z \le t\quad \forall \|z\|=1.
$$

Multiply by  $\|z\|^2$  idea: equivalently for all  $z$ ,

$$
z^\top A z \le t z^\top I z \iff z^\top (tI-A) z \ge 0\ \forall z \iff tI-A\succeq 0.
$$

That’s the whole story: eigenvalue bounds are “for all directions” quadratic bounds, which are PSD constraints.

* * *

At this point, Phase 5.6 + 5.7 complete the conic modeling arc:

*   LP: polyhedral epigraphs (abs, max of affine),
*   SOCP: Euclidean norms and quadratic-over-linear,
*   SDP: inverse-quadratic and spectral constraints.

If you want the next natural step after 5.7 (still in the same spirit), it’s usually: “how to derive these LMIs from Schur complements / block matrices systematically,” because many SDPs are just Schur complements wearing different hats.

## Response:
Alright. Phase 6.1 is the point where convex optimization stops being “everything is convex, push KKT” and becomes “the objective might be nonconvex-looking, but its **sublevel sets** are convex, so we can still solve it by repeatedly solving **convex feasibility** problems.”

I’ll build this as a newcomer walkthrough from absolute first principles, and I’ll be painfully explicit about what is true, what is not, and why bisection is logically justified.

* * *

1) Start from the geometry you already know: sets, convexity, and “sublevel sets”
---------------------------------------------------------------------------------

### 1.1 Convex sets (the one definition you must be able to replay)

A set  $C\subseteq \mathbb{R}^n$  is **convex** if:

*   whenever  $x\in C$  and  $y\in C$ ,
*   then every convex combination  $\theta x + (1-\theta)y$  is also in  $C$ ,
*   for every  $\theta\in[0,1]$ .

Formally:

$$
x,y\in C \ \Rightarrow\ \theta x + (1-\theta)y\in C\quad \forall \theta\in[0,1].
$$

Geometric meaning: “the straight line segment between any two points in the set stays inside the set.”

### 1.2 Extended-valued functions and domain (why we allow  $+\infty$ )

In convex analysis and modeling, it’s very common to encode constraints by defining a function that equals  $+\infty$  outside the allowed region.

We consider

$$
f:\mathbb{R}^n \to \mathbb{R}\cup\{+\infty\}.
$$

Its **domain** is

$$
\mathrm{dom}\,f := \{x\in\mathbb{R}^n : f(x) < +\infty\}.
$$

Why this matters: if  $x\notin \mathrm{dom}\,f$ , then  $f(x)$  is “forbidden” or “not meaningful,” and you should not treat it like an ordinary real number.

### 1.3 Sublevel sets: the central object

For a real number  $\alpha$ , the ** $\alpha$ \-sublevel set** is

$$
S_\alpha := \{x\in\mathrm{dom}\,f : f(x)\le \alpha\}.
$$

Interpretation: “all points whose objective value is at most  $\alpha$ .”

Important: sublevel sets are sets. Quasiconvexity is a property about the geometry of these sets.

* * *

2) Definition of quasiconvexity (the real one)
----------------------------------------------

### 2.1 Quasiconvex function

A function  $f$  is **quasiconvex** if **every sublevel set is convex**:

$$
\boxed{ f \text{ is quasiconvex} \quad\Longleftrightarrow\quad S_\alpha=\{x: f(x)\le \alpha\} \text{ is convex for all } \alpha\in\mathbb{R}. }
$$

That’s it. That is the definition you should default to, because it is exactly what makes bisection work.

### 2.2 Quasiconcave (for completeness)

 $f$  is **quasiconcave** if all **superlevel** sets are convex:

$$
\{x: f(x)\ge \alpha\} \text{ convex for all }\alpha.
$$

This is the “maximize-friendly” cousin: maximizing a quasiconcave function is often handled similarly.

* * *

3) Relationship to convexity: what implies what, and what does NOT
------------------------------------------------------------------

### 3.1 Convex ⇒ quasiconvex (always true)

Claim:

$$
\boxed{\text{If } f \text{ is convex, then } f \text{ is quasiconvex.}}
$$

Proof (completely explicit):

Assume  $f$  is convex. Fix any  $\alpha\in\mathbb{R}$ . Take any  $x,y\in S_\alpha$ . That means:

$$
f(x)\le \alpha,\qquad f(y)\le \alpha.
$$

Take any  $\theta\in[0,1]$ . By convexity of  $f$ ,

$$
f(\theta x+(1-\theta)y)\le \theta f(x) + (1-\theta)f(y).
$$

Using the bounds  $f(x)\le\alpha$ ,  $f(y)\le\alpha$ ,

$$
\theta f(x) + (1-\theta)f(y) \le \theta \alpha + (1-\theta)\alpha = \alpha.
$$

So

$$
f(\theta x+(1-\theta)y)\le \alpha,
$$

meaning  $\theta x+(1-\theta)y\in S_\alpha$ . Since this holds for all  $\theta\in[0,1]$ ,  $S_\alpha$  is convex. Since  $\alpha$  was arbitrary,  $f$  is quasiconvex.

### 3.2 Quasiconvex ⇏ convex (strictly weaker)

Quasiconvexity is weaker. A function may violate Jensen’s inequality but still have convex sublevel sets.

A good _clean_ example is:

$$
f(x)=\min(x,0)\quad\text{on }\mathbb{R}.
$$

This function is concave (not convex). But it is quasiconvex because its sublevel sets are always convex intervals/half-lines.

Let’s verify explicitly.

Fix  $\alpha$ .

*   If  $\alpha\ge 0$ , then  $f(x)=\min(x,0)\le 0 \le \alpha$  for all  $x$ . So  $S_\alpha=\mathbb{R}$ , convex.
*   If  $\alpha < 0$ , then  $f(x)\le \alpha$  means  $\min(x,0)\le \alpha$ . Since  $\alpha<0$ , this forces  $x\le \alpha$  (because if  $x>\alpha$ , then  $\min(x,0)\ge \alpha$  fails when  $x$  is closer to 0). More concretely: for  $x\le 0$ ,  $f(x)=x$ , so  $x\le\alpha$ ; for  $x>0$ ,  $f(x)=0\not\le\alpha$ . So:
    
$$
S_\alpha = (-\infty,\alpha],
$$

convex.

So all sublevel sets are convex, hence quasiconvex, but the function is not convex. This proves quasiconvexity does not imply convexity.

* * *

4) Equivalent characterization you will actually use: the “max on a segment” inequality
---------------------------------------------------------------------------------------

This is the quasiconvex analogue of Jensen.

### 4.1 The theorem

$$
\boxed{ f \text{ is quasiconvex} \quad\Longleftrightarrow\quad f(\theta x+(1-\theta)y) \le \max\{f(x),f(y)\} \ \ \forall x,y,\ \forall\theta\in[0,1]. }
$$

Read this slowly: “Along the line segment between  $x$  and  $y$ , the function never goes above the worse endpoint value.”

That is exactly what “convex sublevel sets” means.

### 4.2 Proof, direction-by-direction

#### (⇒) Sublevel sets convex ⇒ max-inequality

Assume  $f$  is quasiconvex. Fix any  $x,y$  and  $\theta\in[0,1]$ . Define

$$
\alpha := \max\{f(x), f(y)\}.
$$

Then  $f(x)\le \alpha$  and  $f(y)\le \alpha$ , so  $x,y\in S_\alpha$ . Since  $S_\alpha$  is convex, the point  $\theta x+(1-\theta)y\in S_\alpha$ , meaning

$$
f(\theta x+(1-\theta)y)\le \alpha = \max\{f(x),f(y)\}.
$$

#### (⇐) Max-inequality ⇒ sublevel sets convex

Assume the inequality holds for all  $x,y,\theta$ . Fix  $\alpha$ , and take any  $x,y\in S_\alpha$ . Then  $f(x)\le \alpha$  and  $f(y)\le \alpha$ , hence  $\max\{f(x),f(y)\}\le \alpha$ . Apply the inequality:

$$
f(\theta x+(1-\theta)y)\le \max\{f(x),f(y)\}\le \alpha.
$$

So  $\theta x+(1-\theta)y\in S_\alpha$ . Since this holds for all  $\theta$ , the set  $S_\alpha$  is convex.

So the two definitions are equivalent.

* * *

5) The optimization viewpoint: why quasiconvexity is “one notch away” from convex
---------------------------------------------------------------------------------

### 5.1 What a convex optimization problem requires (reminder)

A standard convex minimization problem looks like:

$$
\min_x f_0(x)\quad\text{s.t.}\quad f_i(x)\le 0,\ i=1,\dots,m,\quad Ax=b,
$$

with:

*    $f_0$  convex,
*   each  $f_i$  convex,
*    $Ax=b$  affine.

Then the feasible set is convex, and the objective is convex.

### 5.2 Quasiconvex optimization: the standard setup

A **quasiconvex optimization problem** (in the classic Boyd–Vandenberghe sense) is:

$$
\min_x f_0(x)\quad\text{s.t.}\quad f_i(x)\le 0,\ i=1,\dots,m,\quad Ax=b,
$$

where:

*   the feasible set is convex (constraints  $f_i$  convex + affine equalities),
*   but the objective  $f_0$  is only **quasiconvex**, not necessarily convex.

So: the feasible region is a convex set  $\mathcal{F}$ . The objective is not a convex bowl, but it has convex sublevel sets.

The key idea: minimization cares about sublevel sets, not about the epigraph being convex in the full  $(x,t)$ \-space.

* * *

6) The central reduction: minimization ↔ feasibility of sublevel sets
---------------------------------------------------------------------

This is the entire reason bisection is legal.

Let the feasible set be:

$$
\mathcal{F} := \{x : f_i(x)\le 0,\ i=1,\dots,m,\ Ax=b\}.
$$

Assume  $\mathcal{F}$  is convex (true if  $f_i$  are convex).

Define the optimal value:

$$
p^\star := \inf\{f_0(x): x\in\mathcal{F}\}.
$$

Now fix a candidate threshold  $\alpha\in\mathbb{R}$ . Consider the **feasibility problem**:

> Find  $x$  such that  $x\in\mathcal{F}$  and  $f_0(x)\le \alpha$ .

Equivalently:

$$
\text{find } x \in \mathcal{F}\cap S_\alpha.
$$

### 6.1 Why this is a convex feasibility problem

If  $f_0$  is quasiconvex, then  $S_\alpha$  is convex.

If  $\mathcal{F}$  is convex, then intersection  $\mathcal{F}\cap S_\alpha$  is convex (intersection of convex sets is convex).

So checking “is there an  $x$  with objective  $\le \alpha$ ?” becomes checking feasibility of a convex set.

This is the big shift: you replace a possibly nonconvex-looking objective with a convex constraint  $f_0(x)\le\alpha$ .

### 6.2 The predicate  $\Phi(\alpha)$  and its monotonicity

Define:

$$
\Phi(\alpha) := \begin{cases} \text{true} & \exists x\in\mathcal{F}\ \text{with}\ f_0(x)\le \alpha,\\ \text{false} & \text{otherwise.} \end{cases}
$$

Now the crucial monotonicity fact:

$$
\boxed{ \alpha \le \beta \ \ \Rightarrow\ \ S_\alpha \subseteq S_\beta. }
$$

Proof: if  $f_0(x)\le \alpha$ , then certainly  $f_0(x)\le \beta$  when  $\beta\ge \alpha$ . So membership in a smaller sublevel implies membership in a larger sublevel.

Therefore:

$$
\boxed{ \Phi(\alpha)=\text{true} \ \text{and}\ \beta\ge \alpha\ \Rightarrow\ \Phi(\beta)=\text{true}. }
$$

So  $\Phi(\alpha)$  is a monotone “false → true” switch as  $\alpha$  increases.

### 6.3 The key logical equivalence with  $p^\star$ 

*   If  $\alpha < p^\star$ , then  $\Phi(\alpha)=\text{false}$  (by definition of infimum: nothing feasible achieves value  $\le \alpha$ ).
*   If  $\alpha > p^\star$ , then typically  $\Phi(\alpha)=\text{true}$  (under mild conditions; at minimum, for any  $\epsilon>0$ ,  $\Phi(p^\star+\epsilon)=\text{true}$  because there exists a feasible point with value within  $\epsilon$  of the infimum).

So  $\Phi$  behaves like a step function around the optimal value, which is exactly what bisection exploits.

This is “why bisection works” at the logic level, before you even write an algorithm.

* * *

7) Recognition: how do you know a function is quasiconvex?
----------------------------------------------------------

You do not usually prove quasiconvexity by calculus. You prove it by showing sublevel sets are convex.

Here are the patterns that matter most in problem sets.

### 7.1 Linear-fractional (the #1 classic)

Let

$$
f(x)=\frac{a^\top x+b}{c^\top x+d}
$$

with domain restriction:

$$
c^\top x+d>0.
$$

Claim:  $f$  is quasiconvex (and also quasiconcave) on that domain.

Proof via sublevel sets:

Consider the sublevel set  $f(x)\le \alpha$ :

$$
\frac{a^\top x+b}{c^\top x+d}\le \alpha.
$$

Because  $c^\top x+d>0$  on the domain, multiplying both sides by the denominator preserves the inequality direction:

$$
a^\top x+b \le \alpha(c^\top x+d).
$$

Bring all terms to one side:

$$
(a-\alpha c)^\top x + (b-\alpha d) \le 0.
$$

That is an affine inequality in  $x$ , i.e. a halfspace. Intersect with the domain  $c^\top x+d>0$  (also a halfspace). Intersection of halfspaces is convex. Hence every sublevel set is convex. Therefore  $f$  is quasiconvex.

Crucial trap: if you forget the domain sign, the cross-multiplication is not valid globally.

### 7.2 Max of quasiconvex functions is quasiconvex

Let  $f_i$  be quasiconvex. Define

$$
f(x)=\max_i f_i(x).
$$

Then:

$$
\{x: f(x)\le \alpha\} = \{x: \max_i f_i(x)\le \alpha\} = \bigcap_i \{x: f_i(x)\le \alpha\}.
$$

Each set in the intersection is convex, so the intersection is convex. Hence  $f$  is quasiconvex.

This is extremely common because many objectives are “minimize worst-case something.”

### 7.3 Norm-ratio / relative error (common in signal processing / estimation)

A typical form:

$$
f(x)=\frac{\|Ax-b\|_2}{c^\top x+d}, \quad c^\top x+d>0.
$$

Sublevel set  $f(x)\le \alpha$  becomes:

$$
\|Ax-b\|_2 \le \alpha(c^\top x+d).
$$

If  $c^\top x+d$  is affine, then the RHS is affine times scalar  $\alpha$ . For fixed  $\alpha$ , this is an SOC constraint (because “norm ≤ affine” is SOC, provided the RHS is constrained nonnegative; SOC membership enforces that).

So each sublevel set is convex (SOC representable), giving quasiconvexity.

* * *

8) What quasiconvexity “feels like” in 1D (intuition you can safely use)
------------------------------------------------------------------------

In one dimension, convex sublevel sets are just intervals (possibly infinite rays). So quasiconvex in 1D means:

*   for every  $\alpha$ , the set  $\{x: f(x)\le \alpha\}$  is an interval.

That implies a useful phenomenon: quasiconvex functions in 1D have no “two separated valleys” below the same height; they can be flat, step-like, or bowl-like, but sublevel sets never split into disjoint pieces.

This intuition breaks in higher dimensions if you lean on it too casually, but the “sublevel sets are convex blobs” picture remains correct.

* * *

9) Why bisection is the natural algorithmic consequence (high-level, but logically tight)
-----------------------------------------------------------------------------------------

You now have three facts:

1.  Minimizing  $f_0$  over  $\mathcal{F}$  is equivalent to finding the smallest  $\alpha$  for which  $\mathcal{F}\cap S_\alpha\neq\emptyset$ .
2.  For each fixed  $\alpha$ , checking whether  $\mathcal{F}\cap S_\alpha\neq\emptyset$  is a **convex feasibility problem** (if  $f_0$  quasiconvex and  $\mathcal{F}$  convex).
3.  The feasibility predicate  $\Phi(\alpha)$  is **monotone** in  $\alpha$ .

Monotone predicate + ability to test it = bisection territory. That is not a heuristic; it is literally the standard decision-to-optimization reduction.

Phase 6.2 will be: pick lower/upper bounds  $l<u$  with  $\Phi(l)=$ false and  $\Phi(u)=$ true, and then repeatedly test the midpoint to shrink the bracket.

But the key point for 6.1 is: **bisection is valid only because of convex sublevel sets**, which give monotonic feasibility and convex feasibility checks.

* * *

10) Common “lose points” traps (quasiconvex edition)
----------------------------------------------------

1.  **Illegal cross-multiplication in fractional functions**  
    You must enforce the denominator has a known sign on the domain (usually  $>0$ ). Otherwise the inequality direction may flip for some points and your “sublevel set is a halfspace” proof collapses.
2.  **Thinking quasiconvex means epigraph is convex**  
    No. Convexity is “epigraph convex.” Quasiconvexity is “sublevel sets convex.” Different geometry.
3.  **Confusing quasiconvex with convex along lines**  
    Quasiconvex does imply “along any line, the 1D restriction is quasiconvex,” but that does not mean it’s convex along lines. The inequality is with a max, not an average.
4.  **Assuming differentiability / Hessians matter**  
    They often do not. Many quasiconvex functions are nonsmooth or piecewise-defined. The correct tool is sublevel-set geometry.
5.  **Open vs closed constraints**  
    Optimization and feasibility are usually written with  $\le$  to get closed sets. Strict constraints (<) can cause numerical and theoretical issues (attainment), and bisection logic is clearest with closed sublevel sets.

* * *

11) The “do-this-every-time” recipe for recognizing quasiconvexity
------------------------------------------------------------------

When you see an objective  $f_0(x)$  that doesn’t look convex:

1.  Write down the sublevel constraint  $f_0(x)\le \alpha$ .
2.  Manipulate it _for fixed  $\alpha$ _ into a recognizable convex constraint form:
    *   affine inequality (halfspace) → LP-feasible set,
*   norm ≤ affine → SOCP-feasible set,
*   LMI / PSD constraint → SDP-feasible set,
*   intersection of convex constraints → convex.
    3.  If you can do this for every  $\alpha$  (on the correct domain), then  $f_0$  is quasiconvex.
4.  Then minimization becomes: solve feasibility for different  $\alpha$  and bisection.

That’s Phase 6.1 in operational form.

* * *

If you continue to 6.2, we’ll formalize bisection precisely: how to choose initial bounds, what “accuracy” means (absolute vs relative gap), how feasibility tolerance interacts with solver tolerances, and how you can certify near-optimality by the final bracket  $[l,u]$ .

## Response:
Phase 6.2 — Bisection for quasiconvex optimization, from zero to hero
---------------------------------------------------------------------

Phase 6.1 gave you the structural “physics law”:

*    $f_0$  quasiconvex  $\Rightarrow$  every sublevel set  $S_\alpha=\{x:f_0(x)\le \alpha\}$  is convex.
*   If your feasible set  $\mathcal F$  is convex, then  $\mathcal F\cap S_\alpha$  is convex.
*   Therefore the question “is there a feasible point with objective  $\le \alpha$ ?” becomes a **convex feasibility** question.

Phase 6.2 is the algorithmic exploitation of one extra fact:

*   As  $\alpha$  increases,  $S_\alpha$  only gets bigger.
*   So feasibility as a function of  $\alpha$  is **monotone** (false → true exactly once).

Bisection is just the “binary search” for the switch point.

I’ll build this carefully: problem class → oracle → monotonicity → algorithm → correctness → convergence → how to construct each feasibility check in LP/SOCP/SDP form → practical bounds + tolerances + failure modes.

* * *

0) The exact problem class and what we assume
---------------------------------------------

We consider the canonical quasiconvex minimization:

$$
\min_{x}\ f_0(x) \quad\text{s.t.}\quad x\in\mathcal F
$$

where:

1.  ** $\mathcal F$  is convex.** Typically
    $$
    \mathcal F = \{x:\ f_i(x)\le 0,\ i=1,\dots,m,\ \ Ax=b\}
    $$
    with each  $f_i$  convex and  $Ax=b$  affine.
2.  ** $f_0$  is quasiconvex.** Meaning all sets  $\{x:f_0(x)\le \alpha\}$  are convex.

Define the optimal value:

$$
p^\star := \inf\{f_0(x): x\in\mathcal F\}.
$$

Two important logical possibilities:

*   **Attained optimum:** there exists  $x^\star\in\mathcal F$  with  $f_0(x^\star)=p^\star$ .
*   **Only an infimum:** no feasible point hits  $p^\star$ , but you can get arbitrarily close.

Bisection is primarily a method to approximate **the value**  $p^\star$ , and also produce a near-optimal feasible point when possible.

* * *

1) Turn minimization into a yes/no decision problem (the “feasibility oracle”)
------------------------------------------------------------------------------

### 1.1 Sublevel feasibility set at level  $\alpha$ 

For any real number  $\alpha$ , define:

$$
S_\alpha := \{x:\ f_0(x)\le \alpha\}
$$

and the level-feasible set

$$
\mathcal F_\alpha := \mathcal F\cap S_\alpha = \{x\in\mathcal F:\ f_0(x)\le \alpha\}.
$$

### 1.2 The decision predicate  $\Phi(\alpha)$ 

Define:

$$
\Phi(\alpha) := \begin{cases} \text{true} & \text{if } \mathcal F_\alpha\neq \emptyset \\ \text{false} & \text{if } \mathcal F_\alpha= \emptyset \end{cases}
$$

Interpretation:  
 $\Phi(\alpha)$  answers the question:

> “Is there a feasible point whose objective value is  $\le \alpha$ ?”

This is the only “oracle” bisection needs.

### 1.3 Why  $\Phi(\alpha)$  is a convex feasibility problem (not optimization)

Because:

*    $\mathcal F$  is convex by assumption.
*    $S_\alpha$  is convex **by quasiconvexity** (definition).
*   intersection of convex sets is convex.

So  $\mathcal F_\alpha$  is convex. Checking  $\mathcal F_\alpha\neq\emptyset$  is a convex feasibility task.

In practice you’ll implement this feasibility check by solving a convex optimization that either finds a point or certifies infeasibility (solvers do that). But conceptually the object is feasibility.

* * *

2) The monotonicity lemma (this is the reason bisection is correct)
-------------------------------------------------------------------

This is the key logical engine.

### 2.1 Nesting of sublevel sets

If  $\alpha\le \beta$ , then:

$$
S_\alpha \subseteq S_\beta.
$$

Proof (one line, but let’s spell it out):

Take any  $x\in S_\alpha$ . That means  $f_0(x)\le \alpha$ . Since  $\alpha\le \beta$ , we have  $f_0(x)\le \beta$ , so  $x\in S_\beta$ . Therefore  $S_\alpha\subseteq S_\beta$ .

### 2.2 Nesting of level-feasible sets

Intersect with  $\mathcal F$ :

$$
\mathcal F_\alpha = \mathcal F\cap S_\alpha \subseteq \mathcal F\cap S_\beta = \mathcal F_\beta.
$$

### 2.3 Monotonicity of the predicate

From  $\mathcal F_\alpha\subseteq \mathcal F_\beta$ :

*   If  $\mathcal F_\alpha\neq\emptyset$  (true at  $\alpha$ ), then  $\mathcal F_\beta\neq\emptyset$  for all  $\beta\ge \alpha$ .
*   If  $\mathcal F_\beta=\emptyset$  (false at  $\beta$ ), then  $\mathcal F_\alpha=\emptyset$  for all  $\alpha\le \beta$ .

So:

$$
\boxed{\Phi(\alpha)=\text{true} \Rightarrow \Phi(\beta)=\text{true for all } \beta\ge \alpha}
$$
 
$$
\boxed{\Phi(\beta)=\text{false} \Rightarrow \Phi(\alpha)=\text{false for all } \alpha\le \beta}
$$

Meaning:  $\Phi$  is a monotone step-like function of  $\alpha$ .

### 2.4 Where the “step” happens (relationship to  $p^\star$ )

*   If  $\alpha < p^\star$ , then  $\Phi(\alpha)=$  false.  
    Why? Because  $p^\star$  is the infimum value; no feasible point can achieve value  $\le \alpha$  below it.
*   If  $\alpha > p^\star$ , then  $\Phi(\alpha)=$  true **under very mild conditions**: because by definition of infimum, for any  $\epsilon>0$  there exists  $x\in\mathcal F$  with  $f_0(x) < p^\star+\epsilon$ . Take  $\epsilon=\alpha-p^\star$ .

If the infimum is attained, then  $\Phi(p^\star)=$  true. If not attained,  $\Phi(p^\star)$  could be false but  $\Phi(\alpha)$  is true for all  $\alpha>p^\star$ . Either way, bisection still squeezes down to  $p^\star$ .

* * *

3) What bisection is solving, conceptually
------------------------------------------

You can view the original minimization as:

> Find the smallest  $\alpha$  such that  $\Phi(\alpha)=$  true.

Because:

*   “ $\Phi(\alpha)=$  true” means: there exists a feasible point with objective  $\le \alpha$ .
*   The smallest such  $\alpha$  is exactly the optimal value  $p^\star$  (or the limit of those values if not attained).

So bisection is not magic. It is simply searching for the boundary between infeasibility and feasibility in a monotone family of convex sets  $\mathcal F_\alpha$ .

* * *

4) The bisection algorithm, fully explicit
------------------------------------------

### 4.1 Inputs you must have

1.  A feasibility oracle for  $\Phi(\alpha)$ : given  $\alpha$ , determine feasibility of
    $$
    x\in\mathcal F,\quad f_0(x)\le \alpha,
    $$
    and if feasible, ideally return a witness point  $x$ .
2.  An initial bracket  $[L_0, U_0]$  such that:
    $$
    \Phi(L_0)=\text{false},\qquad \Phi(U_0)=\text{true}.
    $$
    So  $L_0$  is a valid lower bound and  $U_0$  is a valid upper bound.
3.  A stopping tolerance  $\varepsilon>0$  for the **value accuracy**.

### 4.2 The iteration rule

For  $k=0,1,2,\dots$ :

1.  Midpoint:
    $$
    \alpha_k := \frac{L_k + U_k}{2}.
    $$
2.  Evaluate  $\Phi(\alpha_k)$  by solving the feasibility problem.
    *   If feasible ( $\Phi(\alpha_k)=$  true), set:
    $$
    U_{k+1} := \alpha_k,\qquad L_{k+1}:=L_k.
    $$
    Interpretation: we found that the optimum is  $\le \alpha_k$ , so we can tighten the upper bound.
*   If infeasible ( $\Phi(\alpha_k)=$  false), set:
    $$
    L_{k+1} := \alpha_k,\qquad U_{k+1}:=U_k.
    $$
    Interpretation: nobody can achieve objective  $\le \alpha_k$ , so the optimum must be above  $\alpha_k$ .
    3.  Stop when:
    $$
    U_k - L_k \le \varepsilon.
    $$

### 4.3 What you output

*   A bracket:
    $$
    L_k < p^\star \le U_k
    $$
    with width at most  $\varepsilon$ .
*   A near-optimal feasible point: keep the best feasible witness you’ve seen (the one corresponding to the smallest feasible  $\alpha$ , typically the last feasible iterate). Call it  $\hat x$ . Then:
    $$
    f_0(\hat x)\le U_k,
    $$
    so its objective is within  $\varepsilon$  (in value) of the optimum lower bound.

* * *

5) Correctness proof (invariant + induction)
--------------------------------------------

This is the thing you may actually be asked to prove.

### 5.1 Invariant statement

For every iteration  $k$ :

$$
\boxed{\Phi(L_k)=\text{false} \quad\text{and}\quad \Phi(U_k)=\text{true}.}
$$

This implies:

$$
\boxed{L_k < p^\star \le U_k.}
$$

Why?

*   If  $\Phi(L_k)=$  false, then there is no feasible  $x$  with  $f_0(x)\le L_k$ , so the infimum must be strictly greater than  $L_k$ .
*   If  $\Phi(U_k)=$  true, there exists feasible  $x$  with  $f_0(x)\le U_k$ , so the infimum is  $\le U_k$ .

### 5.2 Base case

By assumption, your initial bracket  $[L_0,U_0]$  satisfies the invariant.

### 5.3 Inductive step

Assume the invariant holds at iteration  $k$ . Let  $\alpha_k=(L_k+U_k)/2$ .

Case 1:  $\Phi(\alpha_k)=$  true.

*   We set  $U_{k+1}=\alpha_k$ . Since  $\Phi(\alpha_k)$  is true,  $\Phi(U_{k+1})$  is true.
*   We keep  $L_{k+1}=L_k$ . Since  $\Phi(L_k)$  was false,  $\Phi(L_{k+1})$  is false.

Invariant holds.

Case 2:  $\Phi(\alpha_k)=$  false.

*   We set  $L_{k+1}=\alpha_k$ . Since  $\Phi(\alpha_k)$  is false,  $\Phi(L_{k+1})$  is false.
*   We keep  $U_{k+1}=U_k$ . Since  $\Phi(U_k)$  was true,  $\Phi(U_{k+1})$  is true.

Invariant holds.

Thus by induction it holds for all  $k$ . Therefore the bracket is always valid and always contains the true optimal value.

* * *

6) Convergence rate (how many feasibility solves)
-------------------------------------------------

At each step, the interval length halves.

Let  $W_k := U_k - L_k$ . Then:

$$
W_{k+1} = \frac{W_k}{2}.
$$

So:

$$
W_k = \frac{W_0}{2^k},\qquad W_0=U_0-L_0.
$$

To guarantee  $W_k\le \varepsilon$ , it suffices that

$$
\frac{U_0-L_0}{2^k}\le \varepsilon \quad\Longleftrightarrow\quad 2^k \ge \frac{U_0-L_0}{\varepsilon} \quad\Longleftrightarrow\quad k \ge \log_2\left(\frac{U_0-L_0}{\varepsilon}\right).
$$

So bisection takes  $O(\log(1/\varepsilon))$  feasibility checks. The heavy work is each feasibility solve (LP/SOCP/SDP).

* * *

7) The real work on problem sets: building the feasibility problem for a given  $\alpha$ 
-----------------------------------------------------------------------------------------

Everything above is “outer algorithm.” On PS sets you must be able to do the “inner modeling”:

Given  $\alpha$ , express

$$
x\in\mathcal F,\quad f_0(x)\le \alpha
$$

in a solver-ready convex form.

This is where Phase 5’s “LP/SOCP/SDP atoms” come back.

### 7.1 Linear-fractional objective (LP feasibility)

Suppose

$$
f_0(x)=\frac{a^\top x+b}{c^\top x+d}
$$

with domain constraint  $c^\top x+d>0$  (in practice  $c^\top x+d\ge \epsilon$ ).

Sublevel set:

$$
\frac{a^\top x+b}{c^\top x+d}\le \alpha.
$$

Because  $c^\top x+d>0$  on the domain, multiply without flipping inequality:

$$
a^\top x+b \le \alpha(c^\top x+d).
$$

Rearrange:

$$
(a-\alpha c)^\top x + (b-\alpha d)\le 0.
$$

That is an affine inequality in  $x$ . So if  $\mathcal F$  is polyhedral, the whole feasibility check is an LP feasibility problem.

**Critical domain trap:** if you do not enforce  $c^\top x+d>0$ , then the sublevel set is not what you think (multiplying can flip the inequality when the denominator is negative).

### 7.2 Norm-ratio objective (SOCP feasibility)

Suppose

$$
f_0(x)=\frac{\|Ax-b\|_2}{c^\top x+d},\qquad c^\top x+d>0.
$$

Sublevel:

$$
\frac{\|Ax-b\|_2}{c^\top x+d}\le \alpha \quad\Longleftrightarrow\quad \|Ax-b\|_2 \le \alpha(c^\top x+d),
$$

with  $c^\top x+d\ge 0$ .

For fixed  $\alpha$ , RHS is affine in  $x$ . So this is a standard SOC constraint (Phase 5.3):

$$
(\alpha(c^\top x+d),\ Ax-b)\in\mathcal Q.
$$

Thus each feasibility check is an SOCP.

### 7.3 “Max of things” objective (LP/SOCP/SDP feasibility depending on pieces)

If

$$
f_0(x)=\max_{i=1,\dots,r} g_i(x),
$$

then

$$
f_0(x)\le \alpha \iff g_i(x)\le \alpha\ \forall i.
$$

So you just add all those constraints. If each  $g_i(x)\le \alpha$  is LP/SOCP/SDP representable, so is the feasibility check.

* * *

8) How to find the initial bracket  $[L_0,U_0]$  (practical but essential)
--------------------------------------------------------------------------

Bisection cannot start without one infeasible point and one feasible point in  $\alpha$ \-space.

### 8.1 Finding an upper bound  $U_0$  (usually easy)

If you can find **any** feasible  $x_0\in\mathcal F$ , then

$$
U_0 := f_0(x_0)
$$

is automatically feasible:  $\Phi(U_0)=$  true (witness  $x_0$ ).

So “upper bound” is often “evaluate the objective at any feasible point.”

### 8.2 Finding a lower bound  $L_0$  (problem-dependent)

Common cases:

*   If you know  $f_0(x)\ge 0$  always (e.g., a norm ratio with positive denominator), then  $L_0=0$  is a valid lower bound (may or may not be infeasible, but it is a **lower** bound on the optimum value). For bisection you want  $L_0$  such that  $\Phi(L_0)$  is false; if  $L_0=0$  might be feasible, you need a smaller one.
*   A generic “expanding search” for a lower infeasible bound:
    *   Start with some candidate  $L$  (maybe 0 or  $-1$ ).
    *   If  $\Phi(L)$  is true, decrease it (e.g.,  $L\leftarrow L-2^j$ ).
    *   Keep going until  $\Phi(L)$  becomes false.  
        This uses monotonicity to guarantee you’ll eventually go below  $p^\star$  enough.

Similarly, if you lack a feasible upper bound, you can expand upward until feasibility appears.

On problem sets, you often don’t need to implement this; you just argue “choose  $L_0$  and  $U_0$  such that …” But you must know how it could be done.

* * *

9) Stopping criteria: what does “ $\varepsilon$ \-accurate” mean?
-----------------------------------------------------------------

### 9.1 Value accuracy (the standard theoretical guarantee)

If you stop when  $U_k-L_k\le \varepsilon$ , then you have a certified bracket:

$$
L_k < p^\star \le U_k,\qquad U_k-L_k\le \varepsilon.
$$

So  $U_k$  is at most  $\varepsilon$  above the best proven lower bound. That is a clean, deterministic guarantee.

### 9.2 Solution accuracy (what you can guarantee about  $\hat x$ )

Let  $\hat x$  be the best feasible point found (typically from the last feasible iterate, corresponding to  $U_k$ ). Then:

$$
f_0(\hat x)\le U_k.
$$

But you do **not** generally get a bound like  $\|\hat x-x^\star\|\le \delta$  from bisection alone. Bisection gives **objective value** accuracy, not necessarily variable accuracy, unless extra regularity holds (strong convexity-like properties, uniqueness, etc.).

* * *

10) Numerical reality: solver tolerances and “almost feasibility”
-----------------------------------------------------------------

In exact math,  $\Phi(\alpha)$  is a clean yes/no. In numerical solvers, you get:

*   “feasible” up to tolerance,
*   “infeasible” up to tolerance,
*   sometimes “inconclusive.”

Near the boundary  $p^\star$ , tiny numerical slack matters. Practical fixes:

*   Use a strict positivity margin in denominators:  $c^\top x+d \ge \epsilon$  with  $\epsilon>0$ .
*   Use conservative feasibility: treat “nearly infeasible” as infeasible to avoid reporting wrong feasibility.
*   Stop bisection before you push below numerical precision.

This isn’t handwavy: if feasibility decisions are noisy, bisection can jitter. The monotonic logic assumes exact oracle responses.

* * *

11) Common traps where students lose points
-------------------------------------------

1.  **You forgot to prove monotonicity / nesting**  
    Bisection is only justified because  $\Phi(\alpha)$  is monotone. If you don’t explicitly connect this to sublevel sets, your argument is incomplete.
2.  **You wrote a feasibility check that isn’t convex**  
    If your “ $f_0(x)\le \alpha$ ” constraint isn’t expressed in a convex representable form (LP/SOCP/SDP), then you haven’t shown the oracle is convex.
3.  **Fractional objectives without domain constraint**  
    The step
    $$
    \frac{p(x)}{q(x)}\le \alpha \iff p(x)\le \alpha q(x)
    $$
    is not valid unless you enforce a known sign for  $q(x)$ .
4.  **Confusing  $\le$  vs  $<$ **  
    Sublevel sets use  $\le$ . Many proofs (closedness, attainment, solver feasibility) depend on it.
5.  **Assuming attainment**  
    You don’t need attainment for bisection to approximate  $p^\star$ . But if you claim  $\Phi(p^\star)=$  true, that’s only true if the infimum is attained.

* * *

12) The mechanical PS-set template you should execute
-----------------------------------------------------

When given a quasiconvex minimization:

1.  **Declare the feasibility family**:
    $$
    \mathcal F_\alpha=\{x\in\mathcal F:\ f_0(x)\le \alpha\}.
    $$
2.  **Show convexity of  $\mathcal F_\alpha$ **:
    *    $\mathcal F$  convex by constraints,
    *    $f_0$  quasiconvex ⇒  $S_\alpha$  convex,
    *   intersection convex.
3.  **Show monotonicity**:
    $$
    \alpha\le\beta \Rightarrow \mathcal F_\alpha\subseteq\mathcal F_\beta.
    $$
4.  **Give bisection bracket**  $L_0<U_0$  with infeasible/feasible.
5.  **State bisection update rule** and stopping condition.
6.  **Give the iteration bound**:
    $$
    k \ge \log_2\!\left(\frac{U_0-L_0}{\varepsilon}\right).
    $$
7.  **Explain how each feasibility check is solved** (LP/SOCP/SDP) using Phase 5 modeling.

That is a complete, rigorous Phase 6.2 solution structure.

* * *

If you want to go one level deeper than most textbooks, the next step is to formalize “oracle returns a separating hyperplane / certificate of infeasibility” and connect bisection to dual certificates and cutting-plane logic. But for PS-style quasiconvex problems, the above is the core you must be able to execute mechanically.

## Response:
Phase 6.3 — Perspective transformation, from zero to hero (and why it’s the secret engine of “fractional tricks”)
-----------------------------------------------------------------------------------------------------------------

Phase 6.2 said: if the objective is quasiconvex, you can minimize it by bisection on sublevel sets.

Phase 6.3 is the upgrade: sometimes you can do **one** convex problem instead of many feasibility solves.

The big idea is not “a cute substitution.” It’s a **convex-analysis operation**: the _perspective_ of a function. It packages “divide by a positive scalar/affine thing” into a transformation that **preserves convexity**.

We’ll do this in layers:

1.  What the perspective is (definition and domain).
2.  Why it preserves convexity (a proof you can reproduce).
3.  The geometry (epigraph → conic scaling).
4.  The modeling mechanic: how ratios get converted by introducing  $t$  and scaling variables.
5.  Canonical worked templates: linear-fractional and norm-ratio, plus general convex constraints via perspectives.
6.  Failure modes: where people quietly break it.

* * *

0) Why fractions are annoying (and why quasiconvexity “almost” saves you)
-------------------------------------------------------------------------

You often see objectives like

$$
\min_x \ \frac{f(x)}{g(x)}, \qquad g(x)>0.
$$

Even if  $f$  is convex and  $g$  is affine positive, the ratio is generally **not convex**.

But its sublevel sets are often convex:

$$
\frac{f(x)}{g(x)}\le \alpha \quad\Longleftrightarrow\quad f(x)\le \alpha g(x),
$$

provided  $g(x)>0$  on the domain. That’s Phase 6.2 bisection land.

Perspective transformation tries to do something stronger:

> absorb the denominator into new variables so that the ratio becomes a convex expression **in one shot**.

When it works, you don’t bisection. You “compile” the whole fractional-looking problem into LP/SOCP/SDP directly.

* * *

1) The perspective: definition and what it really means
-------------------------------------------------------

Let  $f:\mathbb R^n\to \mathbb R\cup\{+\infty\}$  be an extended-valued function. (Extended-valued just means: we allow  $+\infty$  to encode domain restrictions.)

### 1.1 Definition (perspective of  $f$ )

Define  $\tilde f:\mathbb R^n\times \mathbb R\to \mathbb R\cup\{+\infty\}$  by

$$
\boxed{ \tilde f(x,t) := \begin{cases} t\, f(x/t) & t>0,\\ +\infty & t\le 0. \end{cases}}
$$

Key points you must internalize:

*   The _original_ variable is  $u\in\mathbb R^n$ .
*   The _perspective variables_ are  $(x,t)$  with  $t>0$ .
*   The relationship is  $u = x/t$ , i.e.  $x = t u$ .
*   The perspective is **not**  $f(x/t)$ . It’s  $t f(x/t)$ . The factor  $t$  is the whole point.

### 1.2 Why define  $+\infty$  for  $t\le 0$ ?

Because the perspective is conceptually “valid only when  $t>0$ .” Making it  $+\infty$  is the standard convex-analysis way to enforce the domain constraint as part of the function.

* * *

2) The fundamental theorem: convexity is preserved
--------------------------------------------------

### Theorem

If  $f$  is convex, then  $\tilde f$  is convex on the set  $\{(x,t): t>0\}$ .

$$
\boxed{f \text{ convex } \Rightarrow \tilde f(x,t)=t f(x/t)\text{ convex for }t>0.}
$$

This is one of the most important closure rules in BV.

### 2.1 Proof (fully explicit, no handwaving)

We must show: for any  $(x_1,t_1)$ ,  $(x_2,t_2)$  with  $t_1>0, t_2>0$ , and any  $\theta\in[0,1]$ ,

$$
\tilde f(\theta x_1+(1-\theta)x_2,\ \theta t_1+(1-\theta)t_2) \le \theta \tilde f(x_1,t_1) + (1-\theta)\tilde f(x_2,t_2).
$$

Define the convex combination:

$$
x_\theta := \theta x_1+(1-\theta)x_2,\qquad t_\theta := \theta t_1+(1-\theta)t_2.
$$

Since  $t_1,t_2>0$  and  $\theta\in[0,1]$ , we have  $t_\theta>0$ . So  $\tilde f(x_\theta,t_\theta)=t_\theta f(x_\theta/t_\theta)$  is well-defined.

Now comes the key trick: create weights that sum to 1, but incorporate  $t_1,t_2$ .

Define

$$
\lambda_1 := \frac{\theta t_1}{t_\theta},\qquad \lambda_2 := \frac{(1-\theta)t_2}{t_\theta}.
$$

Check the properties carefully:

*    $\lambda_1\ge 0$  and  $\lambda_2\ge 0$  because  $\theta,(1-\theta),t_1,t_2,t_\theta$  are nonnegative and  $t_\theta>0$ .
*    $\lambda_1+\lambda_2 = \frac{\theta t_1+(1-\theta)t_2}{t_\theta}=\frac{t_\theta}{t_\theta}=1$ .

Now rewrite the key quantity  $x_\theta/t_\theta$ :

$$
\frac{x_\theta}{t_\theta} = \frac{\theta x_1+(1-\theta)x_2}{t_\theta} = \frac{\theta t_1}{t_\theta}\frac{x_1}{t_1} + \frac{(1-\theta)t_2}{t_\theta}\frac{x_2}{t_2} = \lambda_1 \frac{x_1}{t_1} + \lambda_2 \frac{x_2}{t_2}.
$$

So  $x_\theta/t_\theta$  is a convex combination of  $x_1/t_1$  and  $x_2/t_2$ . Now apply convexity of  $f$ :

$$
f\!\left(\frac{x_\theta}{t_\theta}\right) = f\!\left(\lambda_1\frac{x_1}{t_1}+\lambda_2\frac{x_2}{t_2}\right) \le \lambda_1 f\!\left(\frac{x_1}{t_1}\right) + \lambda_2 f\!\left(\frac{x_2}{t_2}\right).
$$

Multiply both sides by  $t_\theta>0$  (safe: inequality direction doesn’t flip):

$$
t_\theta f\!\left(\frac{x_\theta}{t_\theta}\right) \le t_\theta\lambda_1 f\!\left(\frac{x_1}{t_1}\right) + t_\theta\lambda_2 f\!\left(\frac{x_2}{t_2}\right).
$$

But  $t_\theta\lambda_1=\theta t_1$  and  $t_\theta\lambda_2=(1-\theta)t_2$ , so:

$$
t_\theta f\!\left(\frac{x_\theta}{t_\theta}\right) \le \theta t_1 f\!\left(\frac{x_1}{t_1}\right) + (1-\theta) t_2 f\!\left(\frac{x_2}{t_2}\right).
$$

Recognize each side as a perspective:

$$
\tilde f(x_\theta,t_\theta) \le \theta \tilde f(x_1,t_1) + (1-\theta)\tilde f(x_2,t_2).
$$

That is exactly convexity of  $\tilde f$ . QED.

**What to remember:** the special weights  $\lambda_1,\lambda_2$  are the whole proof. This is why the factor  $t$  exists.

* * *

3) Geometry: perspective is “epigraph → conic scaling”
------------------------------------------------------

This is not optional intuition; it explains why the transformation is natural and why cones appear everywhere.

### 3.1 Epigraph of  $f$ 

$$
\operatorname{epi}(f) := \{(u,s): f(u)\le s\}.
$$

### 3.2 Epigraph of  $\tilde f$ 

Take  $(x,t)$  with  $t>0$ . The inequality  $\tilde f(x,t)\le s$  means:

$$
t f(x/t)\le s \quad\Longleftrightarrow\quad f(x/t)\le s/t.
$$

So:

$$
(x,t,s)\in \operatorname{epi}(\tilde f) \quad\Longleftrightarrow\quad t>0,\ (x/t,\ s/t)\in \operatorname{epi}(f).
$$

Interpretation:

*   pick a point  $(u,s)$  in epi $(f)$ ,
*   scale it by  $t>0$  to  $(x,s')=(tu, ts)$ ,
*   the collection of all such scaled points is essentially a **conic hull** of the epigraph.

That’s why the perspective is the algebraic counterpart of “turning an epigraph into a cone-like object.”

* * *

4) The modeling engine: removing denominators by scaling variables
------------------------------------------------------------------

Now we connect the convex-analysis object to the standard “fractional substitution” trick.

### 4.1 The common situation

You have a positive affine denominator

$$
g(x)=c^\top x + d,\qquad g(x)>0 \text{ on feasible set}.
$$

And your objective/constraints contain  $1/g(x)$  or ratios like  $f(x)/g(x)$ .

### 4.2 The canonical substitution

Define new variables

$$
t := \frac{1}{c^\top x + d},\qquad y := t x.
$$

Then  $t>0$  and  $x = y/t$ .

The key identity you always enforce is the “normalization”:

$$
c^\top y + d t = 1.
$$

Proof:

$$
c^\top y + d t = c^\top(tx)+dt = t(c^\top x+d)= t\cdot \frac{1}{t}=1.
$$

So instead of “denominator in the objective,” you impose a single linear constraint  $c^\top y + d t=1$ . That’s the move that makes the denominator disappear.

### 4.3 Where the perspective appears

Suppose your objective is

$$
\frac{f(x)}{c^\top x + d}.
$$

Using  $t=1/(c^\top x+d)$ , this equals

$$
t f(x).
$$

But  $x=y/t$ , so:

$$
t f(x) = t f(y/t) = \tilde f(y,t).
$$

So the ratio objective becomes a **perspective** of  $f$  evaluated at  $(y,t)$ .

Now the earlier theorem kicks in:

*   If  $f$  is convex,  $\tilde f$  is convex (for  $t>0$ ).

So the ratio objective turns into a convex objective in the lifted variables  $(y,t)$ , provided you add the linear normalization and  $t>0$ .

That’s the “engine” behind many fractional tricks.

* * *

5) The two flagship templates you must be fluent in
---------------------------------------------------

### 5.1 Linear-fractional programs become LPs

Problem:

$$
\min_x \ \frac{a^\top x + b}{c^\top x + d} \quad\text{s.t.}\quad Fx\le g,\ \ c^\top x + d > 0.
$$

Substitute:

$$
t=\frac{1}{c^\top x + d},\quad y=tx.
$$

Then the normalization:

$$
c^\top y + d t = 1,\quad t>0.
$$

Now rewrite everything:

**Objective**

$$
\frac{a^\top x + b}{c^\top x + d} = (a^\top x + b)t = a^\top (tx) + bt = a^\top y + bt,
$$

which is linear in  $(y,t)$ .

**Inequality constraints**

$$
Fx\le g \quad\Longleftrightarrow\quad F(y/t)\le g.
$$

Multiply by  $t>0$ :

$$
Fy \le g t.
$$

This is linear in  $(y,t)$  because  $g$  is constant data and  $t$  is scalar.

So the transformed problem is:

$$
\min_{y,t}\ a^\top y + bt \quad\text{s.t.}\quad Fy \le g t,\ \ c^\top y + d t = 1,\ \ t>0.
$$

That is an LP (or at worst a conic program if extra cones appear elsewhere).

**What to remember:** linear-fractional objectives do not need bisection. Perspective substitution collapses the whole thing into one LP.

* * *

### 5.2 Norm ratio becomes SOCP (often beautifully)

Problem:

$$
\min_x \ \frac{\|Ax-b\|_2}{c^\top x + d} \quad\text{s.t.}\quad x\in\mathcal F,\ \ c^\top x + d > 0.
$$

Same substitution:

$$
t=\frac{1}{c^\top x + d},\quad y=tx,\quad c^\top y + dt = 1.
$$

Now rewrite the numerator carefully. Start with:

$$
Ax-b = A(y/t) - b = \frac{Ay}{t} - b = \frac{Ay - bt}{t}.
$$

Take the norm:

$$
\|Ax-b\|_2 = \left\|\frac{Ay-bt}{t}\right\|_2 = \frac{1}{t}\|Ay-bt\|_2
$$

since  $t>0$ .

Now the ratio objective:

$$
\frac{\|Ax-b\|_2}{c^\top x + d} = \|Ax-b\|_2 \cdot t = \left(\frac{1}{t}\|Ay-bt\|_2\right)t = \|Ay-bt\|_2.
$$

So the transformed objective is just:

$$
\min_{y,t}\ \|Ay-bt\|_2
$$

with the linear constraint  $c^\top y + dt = 1$  and transformed feasible-set constraints.

That is SOCP-friendly by Phase 5.3 (epigraph + SOC):

$$
\min_{y,t,s}\ s \quad\text{s.t.}\quad \|Ay-bt\|_2 \le s,\ \ c^\top y + dt=1,\ \text{(other constraints)}.
$$

**This is the “wow” example:** the denominator literally vanishes and you get a clean norm minimization.

* * *

6) How general constraints transform (this is where people get sloppy)
----------------------------------------------------------------------

You can’t just replace  $x$  by  $y/t$  and “multiply by  $t$ ” randomly. You must use the correct convexity-preserving operation: the **perspective of the constraint function**.

### 6.1 If you have a convex constraint  $f(x)\le 0$ 

Replace  $x=y/t$ . You want an equivalent constraint in  $(y,t)$ .

A safe canonical way is:

$$
f(y/t)\le 0.
$$

But that is not in a standard convex form in  $(y,t)$  (it can be convex, but not always representable easily).

Instead, multiply by  $t>0$  and use the perspective:

$$
t f(y/t) \le 0 \quad\Longleftrightarrow\quad \tilde f(y,t)\le 0,
$$

where  $\tilde f$  is convex if  $f$  is convex.

So convex constraints transform into convex constraints via perspectives.

### 6.2 Linear equality constraints transform nicely

If  $Ax=b$ , then  $A(y/t)=b$ , multiply by  $t$ :

$$
Ay = bt,
$$

which is affine in  $(y,t)$ .

* * *

7) Relationship to bisection (when do you still need Phase 6.2?)
----------------------------------------------------------------

Perspective solves the whole problem directly when:

*   the denominator is (usually) **positive affine**, and
*   the rest of the problem transforms into a standard convex form (LP/SOCP/SDP) in  $(y,t)$ .

If the denominator is not affine, or positivity is not globally enforceable, or constraints don’t perspective-transform into representable cones, you fall back to:

*   use sublevel sets  $f_0(x)\le \alpha$  and bisection (Phase 6.2).

So perspective is “compile-time elimination of  $\alpha$ ”; bisection is “run-time search in  $\alpha$ .”

* * *

8) Domain and sign traps (the ones that silently kill correctness)
------------------------------------------------------------------

1.  **Denominator sign is nonnegotiable.**  
    If  $c^\top x + d$  can be negative, then:
    *   the ratio is not well-defined the same way,
*   cross-multiplication can flip inequalities,
*    $t=1/(c^\top x+d)$  may be negative,
*   the perspective’s domain  $t>0$  breaks.

So you must enforce  $c^\top x+d>0$ . In practice:  $c^\top x+d\ge \epsilon$ .

2.  **Forgetting  $t>0$ .**  
    Even if you have  $c^\top y + dt = 1$ , it does not automatically force  $t>0$  unless you know  $d\ge 0$  and  $c^\top y\ge 0$ \-type structure. Safer to explicitly include  $t\ge 0$  (or  $t>0$  conceptually).
3.  **Multiplying inequalities by  $t$  without stating  $t>0$ .**  
    Every time you multiply an inequality by  $t$ , you must note  $t>0$  so you don’t flip inequality.
4.  **Non-homogeneous terms.**  
    Some expressions don’t simplify nicely. When they don’t, you must use the perspective form  $t f(y/t)$ , not wishful algebra.

* * *

9) The mechanical PS-set recipe (do this without improvising)
-------------------------------------------------------------

When you see a ratio with positive affine denominator  $c^\top x+d$ :

1.  Declare the new variables:
    $$
    t=\frac{1}{c^\top x+d},\qquad y=tx.
    $$
2.  Add the normalization constraint:
    $$
    c^\top y + d t = 1,\qquad t>0.
    $$
3.  Rewrite every occurrence of  $x$  as  $y/t$ .
4.  Convert:
    *   affine  $a^\top x + b$  to  $a^\top y + bt$ ,
    *   norm  $\|Ax-b\|_2/(c^\top x+d)$  to  $\|Ay-bt\|_2$ ,
    *   general convex  $f(x)$  to its perspective  $\tilde f(y,t)=t f(y/t)$  if needed.
5.  Solve the resulting convex program once (LP/SOCP/SDP).

* * *

That’s Phase 6.3 in its fully operational form: a theorem-backed convexity-preserving transformation whose whole job is to turn “fractions” into “cones.”

If you continue to Phase 6.4/Phase 7 territory, the next conceptual cousin is the **log transform** in geometric programming: it’s like perspective’s multiplicative sibling, turning products/monomials into convex functions in log-space.

## Response:
Phase 7 — Geometric Programming (GP), zero-to-hero, fully unpacked
------------------------------------------------------------------

Geometric Programming is one of those “the universe is secretly linear in disguise” moments.

In the original variables it looks like a swamp of products, powers, and sums of products—usually nonconvex territory. GP is the special, carefully fenced-off region of that swamp where a single transformation makes everything convex:

> Work with **log-variables**  $y_i=\log x_i$ .  
> Then monomials become **affine**, and posynomials become **log-sum-exp**, which is **convex**.

Once you internalize that, GP stops being mystical and becomes as mechanical as “norm  $\to$  SOC.”

I’ll build it from absolute basics, prove the key convexity facts cleanly, show the conversion step-by-step, and end with a practical cookbook + common traps.

* * *

0) Why GP even exists (what structure it exploits)
--------------------------------------------------

Many models are naturally multiplicative:

*   “throughput” = product of factors,
*   “cost” = product of terms with elasticities,
*   constraints like “sum of several power-law terms ≤ budget,”
*   ratios of monomials, etc.

The algebra is multiplicative, and **logs** turn multiplicative algebra into additive algebra:

*   product  $\prod$  becomes sum  $\sum$ ,
*   power  $x^a$  becomes scalar multiple  $a\log x$ ,
*   sum of monomials becomes sum of exponentials in log-space,
*   log of that sum becomes **log-sum-exp** (convex).

GP is essentially: “optimize multiplicative expressions by moving to log-space where they become convex objects.”

* * *

1) Domain first: why  $x>0$  is not a technicality
--------------------------------------------------

GP lives on the **strictly positive orthant**

$$
\mathbb R^n_{++}=\{x\in\mathbb R^n: x_i>0\ \forall i\}.
$$

This is not optional:

*    $\log x_i$  only exists for  $x_i>0$ ,
*   monomials with negative or fractional exponents (e.g.,  $x^{-1}, x^{1/2}$ ) also require  $x>0$ ,
*   the transformation  $y=\log x$  is a bijection between  $\mathbb R^n_{++}$  and  $\mathbb R^n$ .

So anytime you see GP, you should mentally attach: **variables are strictly positive**.

* * *

2) The atoms: GP’s special meanings of “monomial” and “posynomial”
------------------------------------------------------------------

This is the first place people get wrecked, because “monomial” in GP does **not** mean polynomial monomial with integer exponents.

### 2.1 GP monomial

A **monomial** (in the GP sense) is

$$
\boxed{ m(x)=c\,x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n} }
$$

with:

*    $c>0$ ,
*   exponents  $a_i\in\mathbb R$  (any real: negative, fractional, whatever),
*   domain  $x\in\mathbb R^n_{++}$ .

Examples:

*    $2x_1^{1/2}x_2^{-3}$ 
*    $0.1x_1x_3^{0}$  (yes, exponent 0 is fine)
*    $x_1^{-1}x_2^{-1}$ 

Crucial fact (we’ll prove): monomials are **log-affine**.

### 2.2 Posynomial

A **posynomial** is a **positive sum of monomials**:

$$
\boxed{ p(x)=\sum_{k=1}^K c_k \prod_{i=1}^n x_i^{a_{ik}}, \qquad c_k>0. }
$$

Examples:

*    $x_1+x_2$  (each term is a monomial)
*    $3x_1^{-1}+2x_1^{1/2}x_2^{1/2}$ 
*    $0.5x_1^2x_2^{-1}+7x_2$ 

Not allowed:

*   subtraction (like  $x_1-x_2$ ),
*   negative coefficients.

“Posy” = positive sum.

* * *

3) The standard GP form (and why it’s written with  $\le 1$  and  $=1$ )
------------------------------------------------------------------------

A (primal) GP is typically presented as:

$$
\begin{aligned} \min_{x\in\mathbb R^n_{++}}\quad & p_0(x) \\ \text{s.t.}\quad & p_i(x)\le 1,\quad i=1,\dots,m\\ & m_j(x)=1,\quad j=1,\dots,r \end{aligned}
$$

where:

*    $p_0,p_i$  are posynomials,
*    $m_j$  are monomials.

Why RHS  $1$ ? Pure normalization convenience.

If you have  $p(x)\le b$  with  $b>0$ , then

$$
p(x)\le b \iff \frac{1}{b}p(x)\le 1,
$$

and  $\frac{1}{b}p$  is still a posynomial (positive scaling preserves posynomial-ness).

If you have  $m(x)=b$  with  $b>0$ , then

$$
m(x)=b \iff \frac{1}{b}m(x)=1,
$$

and  $\frac{1}{b}m$  is still a monomial.

So “ $\le 1$ ” and “ $=1$ ” are just the standard “canonical form.”

* * *

4) The log change of variables: the core move
---------------------------------------------

Define log-variables  $y\in\mathbb R^n$  by

$$
\boxed{y_i=\log x_i \quad\Longleftrightarrow\quad x_i=e^{y_i}.}
$$

This is a bijection:

*   every  $x>0$  corresponds to a unique  $y\in\mathbb R^n$ ,
*   every  $y\in\mathbb R^n$  corresponds to a unique  $x=e^y>0$ .

Now the entire GP story is: rewrite monomials/posynomials in terms of  $y$ , and take logs in the right places.

* * *

5) Monomials become affine in log-space (proof, fully explicit)
---------------------------------------------------------------

Take a monomial:

$$
m(x)=c\prod_{i=1}^n x_i^{a_i}.
$$

Substitute  $x_i=e^{y_i}$ :

$$
m(e^y)=c\prod_{i=1}^n (e^{y_i})^{a_i} =c\prod_{i=1}^n e^{a_i y_i} =c\,e^{\sum_{i=1}^n a_i y_i}.
$$

Now take log:

$$
\log m(e^y) =\log c + \sum_{i=1}^n a_i y_i.
$$

That is an affine function of  $y$ . Therefore:

$$
\boxed{\text{GP monomial } m(x)\ \Rightarrow\ \log m(e^y)\ \text{is affine in }y.}
$$

Immediate modeling consequence:

*   monomial equality  $m(x)=1$  becomes linear equality  $\log m(e^y)=0$ .

* * *

6) Posynomials become log-sum-exp in log-space (and log-sum-exp is convex)
--------------------------------------------------------------------------

Take a posynomial:

$$
p(x)=\sum_{k=1}^K c_k\prod_{i=1}^n x_i^{a_{ik}}.
$$

Substitute  $x=e^y$ . Each term becomes:

$$
c_k\prod_i (e^{y_i})^{a_{ik}} =c_k e^{\sum_i a_{ik}y_i} = e^{\log c_k + \sum_i a_{ik}y_i}.
$$

So

$$
p(e^y)=\sum_{k=1}^K \exp\left(\log c_k+\sum_i a_{ik}y_i\right).
$$

Define affine functions

$$
u_k(y)=\log c_k+\sum_{i=1}^n a_{ik}y_i.
$$

Then

$$
p(e^y)=\sum_{k=1}^K e^{u_k(y)} \quad\Rightarrow\quad \log p(e^y)=\log\left(\sum_{k=1}^K e^{u_k(y)}\right).
$$

The function

$$
\mathrm{lse}(u_1,\dots,u_K)=\log\left(\sum_{k=1}^K e^{u_k}\right)
$$

is called **log-sum-exp**.

### 6.1 Crucial fact: log-sum-exp is convex (rigorous proof)

There are multiple proofs; here’s one that’s clean and reproducible.

Let  $u,v\in\mathbb R^K$  and  $\theta\in[0,1]$ . We want:

$$
\mathrm{lse}(\theta u+(1-\theta)v)\le \theta\,\mathrm{lse}(u)+(1-\theta)\,\mathrm{lse}(v).
$$

Compute:

$$
\mathrm{lse}(\theta u+(1-\theta)v) =\log\left(\sum_{k=1}^K e^{\theta u_k+(1-\theta)v_k}\right) =\log\left(\sum_{k=1}^K (e^{u_k})^\theta (e^{v_k})^{1-\theta}\right).
$$

Now use **Hölder’s inequality** in the form:

$$
\sum_k a_k^\theta b_k^{1-\theta} \le \left(\sum_k a_k\right)^\theta \left(\sum_k b_k\right)^{1-\theta} \quad \text{for } a_k,b_k\ge 0.
$$

Set  $a_k=e^{u_k}$ ,  $b_k=e^{v_k}$  (all positive). Then:

$$
\sum_{k=1}^K (e^{u_k})^\theta (e^{v_k})^{1-\theta} \le \left(\sum_{k=1}^K e^{u_k}\right)^\theta \left(\sum_{k=1}^K e^{v_k}\right)^{1-\theta}.
$$

Take log of both sides (log is increasing):

$$
\log\left(\sum_k e^{\theta u_k+(1-\theta)v_k}\right) \le \theta\log\left(\sum_k e^{u_k}\right) +(1-\theta)\log\left(\sum_k e^{v_k}\right).
$$

That is exactly convexity of log-sum-exp.

So:

$$
\boxed{\log\left(\sum_{k=1}^K e^{u_k}\right)\ \text{is convex in }u.}
$$

Now since each  $u_k(y)$  is affine in  $y$ , the composition

$$
y \mapsto \log\left(\sum_k e^{u_k(y)}\right)
$$

is convex (convex function of affine map).

Therefore:

$$
\boxed{\text{posynomial } p(x)\ \Rightarrow\ \log p(e^y)\ \text{is convex in }y.}
$$

This is the heart of GP convexity.

* * *

7) Convert GP constraints into convex constraints in  $y$ 
----------------------------------------------------------

### 7.1 Posynomial inequality  $p(x)\le 1$ 

Start:

$$
p(x)\le 1,\quad x>0.
$$

Substitute  $x=e^y$ :

$$
p(e^y)\le 1.
$$

Take log (log is increasing, direction preserved):

$$
\log p(e^y)\le 0.
$$

We just proved  $\log p(e^y)$  is convex in  $y$ . So this is a convex inequality constraint.

So:

$$
\boxed{p(x)\le 1 \iff \log p(e^y)\le 0\quad (\text{convex in }y).}
$$

### 7.2 Monomial equality  $m(x)=1$ 

Start:

$$
m(x)=1.
$$

Substitute:

$$
m(e^y)=1.
$$

Take log:

$$
\log m(e^y)=0.
$$

But  $\log m(e^y)$  is affine in  $y$ . So this is a linear equality.

So:

$$
\boxed{m(x)=1 \iff \log m(e^y)=0\quad (\text{linear in }y).}
$$

* * *

8) Convert the objective (why we minimize  $\log p_0(e^y)$ )
------------------------------------------------------------

Original objective:

$$
\min_x p_0(x).
$$

After substitution  $x=e^y$ , that becomes  $\min_y p_0(e^y)$ .

But  $p_0(e^y)$  is a **sum of exponentials**, which is convex, right? Careful:  $p_0(e^y)$  is indeed convex in  $y$  if it’s a sum of exponentials of affine forms (which it is). So you _can_ minimize  $p_0(e^y)$  directly as a convex objective.

However, the “standard GP convex form” uses:

$$
\min_y \log p_0(e^y).
$$

Why does that preserve minimizers?

Because  $\log$  is strictly increasing, and  $p_0(e^y)>0$ . Therefore:

$$
p_0(e^{y_1}) < p_0(e^{y_2}) \iff \log p_0(e^{y_1}) < \log p_0(e^{y_2}).
$$

So the argmin set is unchanged.

Using  $\log$  is often numerically nicer and keeps everything in the “log-domain” family. It also aligns with the inequality transform  $p\le 1 \iff \log p\le 0$ .

Thus the standard convex “log-GP” is:

$$
\boxed{ \begin{aligned} \min_y\quad & \log p_0(e^y)\\ \text{s.t.}\quad & \log p_i(e^y)\le 0,\quad i=1,\dots,m\\ & \log m_j(e^y)=0,\quad j=1,\dots,r. \end{aligned}}
$$

Objective convex, inequalities convex, equalities affine ⇒ convex optimization problem.

Recover original variables at the end by:

$$
x_i=e^{y_i}.
$$

* * *

9) Why GP is “convex after transformation” in one sentence (but actually correct)
---------------------------------------------------------------------------------

Because after  $x=e^y$ :

*   monomial equality becomes affine equality,
*   posynomial inequality becomes  $\text{convex} \le 0$ ,
*   objective becomes convex (either  $p_0(e^y)$  or  $\log p_0(e^y)$ ).

That’s it. No magic beyond:

1.  log turns products/powers into affine,
2.  log of sum of exponentials is convex.

* * *

10) A fully worked example (mechanical conversion)
--------------------------------------------------

Consider:

$$
\begin{aligned} \min_{x_1,x_2>0}\quad & p_0(x)=x_1^{-1}x_2 + 2x_2^{-1}\\ \text{s.t.}\quad & p_1(x)=\frac{1}{3}x_1 x_2^2 \le 1\\ & p_2(x)=x_1^{-1}x_2 \le 1. \end{aligned}
$$

Step A: define  $y_1=\log x_1,\ y_2=\log x_2$ . Then:

*    $x_1^{-1}x_2 = e^{-y_1+y_2}$ ,
*    $x_2^{-1}=e^{-y_2}$ ,
*    $\frac{1}{3}x_1x_2^2=\exp(\log(1/3)+y_1+2y_2)$ .

Objective in  $y$ :

$$
p_0(e^y)=e^{-y_1+y_2}+2e^{-y_2}.
$$

Standard log-objective:

$$
\min_y\ \log\left(e^{-y_1+y_2}+2e^{-y_2}\right).
$$

That’s log-sum-exp of affine pieces ⇒ convex.

Constraint 1:

$$
\frac{1}{3}x_1x_2^2 \le 1 \iff \log\left(\frac{1}{3}e^{y_1+2y_2}\right)\le 0 \iff \log\frac{1}{3}+y_1+2y_2\le 0,
$$

linear.

Constraint 2:

$$
x_1^{-1}x_2 \le 1 \iff \log(e^{-y_1+y_2})\le 0 \iff -y_1+y_2\le 0,
$$

linear.

So the transformed problem is convex with a convex objective and linear constraints. Solve it, then  $x=e^y$ .

* * *

11) What GP is _not_ (common traps that look “almost GP”)
---------------------------------------------------------

1.  **Posynomial equalities are not allowed in standard GP.**  
    Constraint  $p(x)=1$  with  $p$  posynomial is generally nonconvex. Only monomial equalities are allowed, because in log-space they become linear.
2.  **Subtraction kills GP.**  
    Anything like  $x_1 + x_2 - 1$  is not a posynomial. Negative coefficients or differences break the log-sum-exp convexity structure.
3.  **Variables must be positive.**  
    If the problem allows  $x_i\le 0$ , it’s not a GP as stated. Sometimes you can reparameterize (like  $x_i = z_i^2$  if you need nonnegativity), but that’s extra modeling, not automatic GP.
4.  **Maximizing a posynomial is not GP-convex.**  
    Minimizing posynomial works. Maximizing generally becomes nonconvex after transformation.
5.  **Coefficients must be positive.**  
    Even if the algebra “looks similar,” a negative coefficient breaks the “sum of exponentials” representation.

* * *

12) GP as a strict “type system” (a practical recognition test)
---------------------------------------------------------------

To quickly recognize a GP:

*   Are all variables intended to be  $>0$ ?
*   Can every inequality be written as “posynomial  $\le 1$ ”?
*   Can every equality be written as “monomial  $=1$ ”?
*   Is the objective a posynomial to be minimized?

If yes, it’s GP.

If you have something like “posynomial  $\le$  monomial,” that’s also okay because dividing by a monomial keeps you in posynomials:

$$
p(x)\le m(x)\iff \frac{p(x)}{m(x)}\le 1,
$$

and  $p/m$  is still a posynomial (each monomial term divided by a monomial remains a monomial; sum remains posynomial).

That’s a very common manipulation.

* * *

13) The GP cookbook (what you literally do on problem sets)
-----------------------------------------------------------

1.  Ensure/declare  $x\in\mathbb R^n_{++}$ .
2.  Rewrite constraints into canonical form:
    *    $p(x)\le b$  ( $b>0$ ) →  $(1/b)p(x)\le 1$ .
*    $p(x)\le m(x)$  →  $p(x)/m(x)\le 1$ .
*    $m(x)=b$  ( $b>0$ ) →  $(1/b)m(x)=1$ .
    3.  Verify:
    *   LHS of “ $\le 1$ ” are posynomials,
*   LHS of “ $=1$ ” are monomials.
    4.  Transform:
    
$$
y_i=\log x_i.
$$
5.  Convert:
    *   each posynomial constraint  $p(x)\le 1$  becomes  $\log p(e^y)\le 0$  (convex),
*   each monomial equality  $m(x)=1$  becomes  $\log m(e^y)=0$  (linear),
*   objective becomes  $\min \log p_0(e^y)$  (convex).
    6.  Solve convex problem in  $y$ . Recover  $x=e^y$ .

* * *

14) How GP connects back to Phase 6.3 (perspective) conceptually
----------------------------------------------------------------

Perspective was about “divide by a positive affine thing.”  
GP is about “turn multiplication/powers into additive structure via logs.”

They’re cousins:

*   Perspective: scaling + convexity preservation.
*   GP: log-reparameterization turning posynomials into log-sum-exp.

If Phase 6.3 is “fractions become convex,” Phase 7 is “products become convex.”

* * *

If you want the next step in the same ultra-mechanical style, it’s usually: “Generalized GP / disciplined GP rules” and then “how to spot when a non-GP problem can be massaged into GP by introducing auxiliary variables and monomial bounds.” That’s where GP becomes a modeling language rather than a single template.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)