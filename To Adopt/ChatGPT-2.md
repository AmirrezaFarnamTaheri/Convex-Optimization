# 2

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/21/2025 0:41:59  
**Updated:** 12/21/2025 11:14:26  
**Exported:** 12/22/2025 1:39:01  
**Link:** [https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916/c/6947110d-b5d8-8328-934c-d4a702b9a348](https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916/c/6947110d-b5d8-8328-934c-d4a702b9a348)  

## Response:
Phase 3.1 — Norm axioms (the “rulers” that secretly power PS6)
--------------------------------------------------------------

You already know the roadmap text. Now we do the actual job: rebuild **what a norm is**, from first principles, in a way that makes later tricks (dual norms, robust constraints, SOCP modeling) feel inevitable instead of magical.

The key meta-fact you will keep using later is:

A **norm** is exactly the structure that makes “distance-like size” behave sanely under scaling and addition, and those sanity rules are _precisely_ what make norm balls convex sets and norm functions convex objectives. That’s why norms show up everywhere in convex optimization.

02-Slides

* * *

### 0) Where we are in the dependency graph

We’re in Phase 3 because Phase 2 gave you “convexity of functions = Jensen inequality / epigraph / supporting hyperplanes.” The moment we say “norms are convex,” we are feeding Phase 2 machinery with a new “safe objective/constraint generator.” (This is explicitly treated as a core example in your convex-functions material: “all norms are convex.”

03-Slides

Main Lecture 05

)

* * *

1) Definition: what is a norm?
------------------------------

A norm is a function

$$
\|\cdot\|:\mathbb{R}^n \to \mathbb{R}
$$

that assigns a nonnegative real number to each vector, intended to represent “size/length.”

It is defined by **three axioms**. They look simple, but each one is doing specific geometry work.

### Axiom (N1) Nonnegativity + definiteness

$$
\|x\|\ge 0 \quad \text{for all } x,\qquad \|x\|=0 \iff x=0.
$$

**Why we need it:**  
If  $\|x\|$  is “length,” negative length is nonsense, and the only vector of length  $0$  must be the zero vector. This axiom prevents pathological “size” functions that declare nonzero vectors to be “invisible.”

**Common failure mode:** seminorms.  
Sometimes you’ll see  $\|x\|=0$  for nonzero  $x$ . That’s a **seminorm**, not a norm. Example:  $\|x\|=|a^\top x|$  is zero for all vectors orthogonal to  $a$ .

### Axiom (N2) Positive homogeneity (scaling law)

$$
\|\alpha x\| = |\alpha|\,\|x\|\quad \text{for all } \alpha\in\mathbb{R},\ x\in\mathbb{R}^n.
$$

**Geometric meaning:** scaling the vector by  $\alpha$  scales its length by  $|\alpha|$ .  
The absolute value is crucial: flipping direction ( $\alpha<0$ ) doesn’t change length, it just reverses the arrow.

**Why optimization cares:**  
This axiom is what makes “unit ball + scaling” generate _all_ balls:

$$
\{x:\|x\|\le r\} = r\{x:\|x\|\le 1\}.
$$

So once you understand the unit ball, you understand every radius.

### Axiom (N3) Triangle inequality (additivity control)

$$
\|x+y\|\le \|x\|+\|y\|\quad \text{for all } x,y.
$$

**Meaning:** taking two steps can’t be shorter than taking the “best possible single step,” and conversely, the length of the combined step can’t exceed the sum of the lengths.

This is the axiom that forces convexity later. If you remember only one thing: **triangle inequality is convexity fuel**.

* * *

2) Immediate consequences (tiny lemmas you’ll use constantly)
-------------------------------------------------------------

### Lemma 1:  $\|x\|=\|-x\|$ 

Proof: by (N2) with  $\alpha=-1$ ,

$$
\|-x\|=\|(-1)x\|=|-1|\|x\|=\|x\|.
$$

### Lemma 2: Reverse triangle inequality

$$
\big|\|x\|-\|y\|\big|\le \|x-y\|.
$$

Proof (two lines, but each line is doing something):

1.  Triangle on  $x = (x-y)+y$ :
    
$$
\|x\| \le \|x-y\|+\|y\| \implies \|x\|-\|y\|\le \|x-y\|.
$$
2.  Swap  $x,y$ :
    
$$
\|y\|-\|x\|\le \|y-x\|=\|x-y\|.
$$

Combine:

$$
|\|x\|-\|y\||\le \|x-y\|.
$$

Interpretation: norms are “Lipschitz with constant 1” with respect to themselves. This is one of the reasons norm-based objectives behave nicely numerically.

### Lemma 3: Convex combinations shrink (the “two-point Jensen” for norms)

For  $0\le \theta\le 1$ ,

$$
\|\theta x + (1-\theta)y\| \le \theta\|x\| + (1-\theta)\|y\|.
$$

This is exactly the convexity inequality for the function  $f(x)=\|x\|$ , and it follows from triangle inequality + homogeneity (we’ll prove it cleanly in §4).

* * *

3) Examples of norms (and why each fits the axioms)
---------------------------------------------------

### 3.1 The  $\ell_2$  (Euclidean) norm

$$
\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}.
$$
*   (N1) obvious: squares are nonnegative; sum is zero iff each  $x_i=0$ .
*   (N2)  $\|\alpha x\|_2 = \sqrt{\sum (\alpha x_i)^2}=|\alpha|\sqrt{\sum x_i^2}=|\alpha|\|x\|_2$ .
*   (N3) is Cauchy–Schwarz-based; geometrically “straight line is shortest.”

### 3.2 The  $\ell_1$  norm

$$
\|x\|_1 = \sum_{i=1}^n |x_i|.
$$

Triangle inequality is componentwise:  $|a_i+b_i|\le |a_i|+|b_i|$ , then sum.

### 3.3 The  $\ell_\infty$  norm

$$
\|x\|_\infty=\max_i |x_i|.
$$

Triangle inequality: for each coordinate,

$$
|x_i+y_i|\le |x_i|+|y_i|\le \|x\|_\infty+\|y\|_\infty,
$$

then take max over  $i$ .

These three are the PS6 workhorses because:

*    $\ell_1$  and  $\ell_\infty$  often become **LP** constraints/objectives.
*    $\ell_2$  often becomes **SOCP** constraints/objectives.

Your materials explicitly treat norms as core convex examples.

03-Slides

Main Lecture 05

* * *

4) The key theorem: every norm is a convex function
---------------------------------------------------

This is not a slogan. You should be able to prove it on command.

### Theorem

The function  $f(x)=\|x\|$  is convex on  $\mathbb{R}^n$ .

#### Proof (from the definition of convexity)

We must show that for any  $x,y\in\mathbb{R}^n$  and any  $\theta\in[0,1]$ ,

$$
\|\theta x + (1-\theta)y\|\le \theta\|x\|+(1-\theta)\|y\|.
$$

**Step 1 (apply triangle inequality to a sum):**  
Write the convex combination as a sum:

$$
\theta x + (1-\theta)y = (\theta x) + ((1-\theta)y).
$$

Then by (N3),

$$
\|\theta x + (1-\theta)y\| \le \|\theta x\| + \|(1-\theta)y\|.
$$

**Step 2 (use homogeneity to pull out scalars):**  
Because  $\theta\ge 0$  and  $1-\theta\ge 0$ ,

$$
\|\theta x\| = \theta\|x\|,\qquad \|(1-\theta)y\|=(1-\theta)\|y\|
$$

by (N2).

**Step 3 (substitute back):**

$$
\|\theta x + (1-\theta)y\| \le \theta\|x\|+(1-\theta)\|y\|.
$$

Done.

This is exactly the style used in the course notes when proving “norms are convex.”

Main Lecture 05

**Why this matters for PS6:**  
Once a function is convex, its **sublevel sets** are convex, and constraints of the form  $\|Ax+b\|\le t$  become “safe” convex constraints. This is the gateway to SOCP modeling later.

* * *

5) Norm balls are convex sets (and this is the same proof in disguise)
----------------------------------------------------------------------

Define the norm ball of radius  $r\ge 0$  centered at  $c$ :

$$
B(c,r)=\{x:\|x-c\|\le r\}.
$$

### Claim

 $B(c,r)$  is convex.

**Proof (one-liner once you see it):**  
Take  $x_1,x_2\in B(c,r)$ . So  $\|x_1-c\|\le r$  and  $\|x_2-c\|\le r$ .  
For  $0\le\theta\le 1$ , consider  $x_\theta=\theta x_1+(1-\theta)x_2$ . Then

$$
x_\theta-c=\theta(x_1-c)+(1-\theta)(x_2-c).
$$

Apply convexity of the norm (proved above):

$$
\|x_\theta-c\|\le \theta\|x_1-c\|+(1-\theta)\|x_2-c\|\le \theta r+(1-\theta)r=r.
$$

So  $x_\theta\in B(c,r)$ . Hence convex.

This norm-ball convexity is emphasized as a core lemma in your convex-sets material (balls/ellipsoids/norm balls as canonical convex sets).

02-Slides

* * *

6) The “unit ball viewpoint” (this becomes huge later)
------------------------------------------------------

Let  $B=\{x:\|x\|\le 1\}$  be the unit ball.

From the axioms, you can reconstruct the norm from  $B$  via the **Minkowski functional (gauge)**:

$$
\|x\| = \inf\{t>0: x\in tB\}.
$$

(You don’t need to memorize the name yet. You do need to understand the idea: “how much do I have to scale the unit ball to catch  $x$ ?”)

Why this matters: later, dual norms and support functions basically come from “how do linear functionals touch this unit ball?” That’s the bridge into robust optimization and duality tricks.

* * *

7) Sanity checklist (what you should be able to do after 3.1)
-------------------------------------------------------------

You’re “done” with 3.1 when you can do these without looking anything up:

1.  Given a candidate  $\phi(x)$ , quickly test whether it satisfies (N1)-(N3).
2.  Prove, cleanly, that any norm is convex (triangle + homogeneity).
3.  Prove the norm ball is convex (either directly or by “sublevel set of convex function”).
4.  Instantly explain why  $\|Ax+b\|_2\le c^\top x + d$  smells like SOCP (because it’s “norm ≤ affine”).
5.  State and prove reverse triangle inequality.

* * *

That’s 3.1. Next, in **3.2**, we’ll go from “axioms” to **geometry**: unit balls, level sets, and why  $\ell_1$  balls have corners (sparsity),  $\ell_2$  balls are round (rotation-invariance), and  $\ell_\infty$  balls are boxes (worst-coordinate control). This is where the modeling instincts start to become automatic.

## Response:
3.2 — Geometry of norm balls (why norms _feel_ different, and why PS6 cares)
----------------------------------------------------------------------------

Phase 3.1 gave the axioms. Phase 3.2 is where those axioms turn into _pictures in your head_ that later become modeling reflexes: “this constraint makes a box,” “this objective prefers corners,” “this robust set is a ball in the dual norm,” etc.

A norm  $\|\cdot\|$  gives you a whole family of sets:

*   **Unit ball**:  $B = \{x\in\mathbb{R}^n : \|x\|\le 1\}$ 
*   **Radius- $r$  ball**:  $rB = \{x : \|x\|\le r\}$ 
*   **Sphere**:  $\{x : \|x\|=1\}$ 

Everything in 3.2 is basically: “what properties must  $B$  have if  $\|\cdot\|$  is a norm?” and “how do common norms differ by the _shape_ of  $B$ ?”

* * *

### 1) The unit ball completely characterizes the norm

This is not philosophy; it’s a precise statement.

Let  $B=\{x:\|x\|\le 1\}$ . For any  $x\neq 0$ ,

$$
\|x\| = \inf\{t>0 : x\in tB\}.
$$

Interpretation: “How much do I need to scale the unit ball until it just contains  $x$ ?”

Why it’s true (step-by-step, no handwaving):

*   If  $x\in tB$ , then by definition  $x=tb$  for some  $b$  with  $\|b\|\le 1$ .
*   Then  $\|x\|=\|tb\|=t\|b\|\le t$ . So any  $t$  that contains  $x$  must satisfy  $t\ge \|x\|$ . That means  $\|x\|$  is a lower bound on the set  $\{t: x\in tB\}$ .
*   Conversely, take  $t=\|x\|$ . If  $x\neq 0$ , define  $b=x/\|x\|$ . Then  $\|b\|=1$  by homogeneity, so  $b\in B$ . And  $x=\|x\|\,b\in \|x\|B$ . So  $t=\|x\|$  is feasible.
*   So the smallest feasible scaling is exactly  $\|x\|$ .

This matters later because “geometry of  $B$ ” becomes “algebra of  $\|\cdot\|$ ” and vice versa.

* * *

### 2) What _must_ a norm ball look like?

Let  $B=\{x:\|x\|\le 1\}$ . From the axioms:

#### (i) Convex

We proved in 3.1 that  $\|\cdot\|$  is convex, so its sublevel sets are convex. Concretely: if  $\|x\|\le 1$  and  $\|y\|\le 1$ , then for  $0\le\theta\le 1$ ,

$$
\|\theta x+(1-\theta)y\|\le \theta\|x\|+(1-\theta)\|y\|\le 1.
$$

#### (ii) Balanced (centrally symmetric)

“Balanced” means: if  $x\in B$ , then  $-x\in B$ .  
Reason:  $\|-x\|=\|x\|$ . So the ball is symmetric about the origin.

This is exactly why norm balls are “centered at 0” in a very strict sense; shifting the center produces sets like  $\{x:\|x-c\|\le r\}$ , still convex but no longer symmetric around 0.

#### (iii) Absorbing (it eventually contains any direction)

For any  $x$ , there exists  $t>0$  such that  $x\in tB$ . In fact  $t=\|x\|$  works because  $x\in\|x\|B$ .

Interpretation: the ball isn’t contained in a lower-dimensional subspace; it “spreads” in all directions enough to generate a full gauge.

#### (iv) Closed and bounded (in finite dimensions)

In  $\mathbb{R}^n$ , all norms are continuous and equivalent, so  $B$  is compact. You don’t need the full equivalence proof yet, but you should keep the intuition: no norm ball can be “infinitely spiky” or “unbounded” in finite dimensions.

* * *

### 3) Visual intuition in 2D:  $\ell_1, \ell_2, \ell_\infty$ 

Work in  $\mathbb{R}^2$ . Write  $x=(x_1,x_2)$ .

#### 3.1 The  $\ell_2$  unit ball: circle

$$
\|x\|_2 \le 1 \iff x_1^2+x_2^2 \le 1.
$$

This is the usual Euclidean disk.

Key geometric property: **rotation invariance**.  
If  $Q$  is orthogonal ( $Q^\top Q=I$ ), then  $\|Qx\|_2=\|x\|_2$ . So the ball looks the same from every angle.

Optimization consequence (foreshadowing):  $\ell_2$  penalizes magnitude uniformly in all directions; it doesn’t “prefer” axis-aligned solutions.

#### 3.2 The  $\ell_\infty$  unit ball: square (box)

$$
\|x\|_\infty \le 1 \iff \max(|x_1|,|x_2|)\le 1 \iff |x_1|\le 1,\ |x_2|\le 1.
$$

That’s the axis-aligned square  $[-1,1]^2$ .

Optimization consequence:  $\ell_\infty$  is “control the worst coordinate.” Constraints become **two-sided bounds** componentwise. This is why  $\ell_\infty$ \-constraints often linearize nicely into LP form.

#### 3.3 The  $\ell_1$  unit ball: diamond

$$
\|x\|_1 \le 1 \iff |x_1|+|x_2|\le 1.
$$

That’s a diamond with corners on the axes:  $(\pm 1,0)$ ,  $(0,\pm 1)$ .

Optimization consequence (big one): corners on axes mean solutions under  $\ell_1$  penalties often “snap” to axes (sparsity intuition). In higher dimensions,  $\ell_1$  balls have lots of “sharp” extreme points aligned with coordinate axes.

You don’t need to worship the sparsity story yet—just store the geometric fact:  $\ell_1$  ball is pointy in coordinate directions;  $\ell_2$  is round;  $\ell_\infty$  is flat-faced.

* * *

### 4) “Which direction is expensive?” = supporting hyperplanes of the ball

This is where geometry starts turning into duality.

Take a direction vector  $u$ . Consider the linear functional  $x\mapsto u^\top x$ . Over the unit ball  $B$ , the maximum value

$$
\sup_{x\in B} u^\top x
$$

is achieved at a boundary point where a supporting hyperplane orthogonal to  $u$  touches  $B$ .

Geometric meaning:

*   The “most aligned” point of the ball with direction  $u$  tells you how large  $u^\top x$  can be when  $\|x\|\le 1$ .
*   If the ball has a **flat face** perpendicular to  $u$ , there are many maximizers (non-unique).
*   If the ball is **smooth** in that direction, the maximizer is typically unique.

This becomes the dual norm in 3.4–3.5:

$$
\|u\|_* = \sup_{\|x\|\le 1} u^\top x.
$$

I’m mentioning it now because the geometry is the whole point: dual norms are “support functions” of the primal unit ball.

* * *

### 5) Balls under linear maps: why ellipsoids show up

If  $A$  is invertible, look at the set

$$
\{x : \|Ax\|_2 \le 1\}.
$$

Let  $y=Ax$ . Then  $x=A^{-1}y$ , so this set is

$$
\{A^{-1}y : \|y\|_2\le 1\} = A^{-1}(\text{Euclidean ball}).
$$

A linear map sends the Euclidean ball to an **ellipsoid**.

This is exactly why quadratic forms and ellipsoids are welded together:

$$
\|Ax\|_2^2 = x^\top A^\top A x.
$$

So constraints like  $x^\top Px \le 1$  with  $P\succeq 0$  are “ellipsoid constraints.”

PS6 relevance: ellipsoids are convex;  $\|Ax+b\|_2\le t$  is a canonical SOCP pattern (and sometimes a disguised QCQP).

* * *

### 6) How radius and center work (translation vs scaling)

*   **Scaling**:  $\{x:\|x\|\le r\} = rB$ . This is purely from homogeneity.
*   **Translation**:  $\{x:\|x-c\|\le r\} = c + rB$ . This is just “move the ball.”

Why it matters: convex modeling often uses “affine image/preimage” closure rules. A norm-ball constraint is really:

$$
x \in c + rB,
$$

i.e., membership in an affine transformation of a canonical convex set. That is exactly the mindset PS6 wants.

* * *

### 7) Boundary structure: smooth vs pointy, and why optimization lands on corners

This is intuition you’ll see again with LP/QP/SOCP.

*    $\ell_2$  ball is smooth everywhere. When you minimize a linear functional over it, you typically get a unique tangency point.
*    $\ell_1$  and  $\ell_\infty$  balls have corners/edges. Minimizing linear functionals over polyhedral balls tends to hit **extreme points** (corners). That’s one geometric reason LP solutions hit vertices.

You don’t need simplex theory here; just the geometric truth: “linear objective + polyhedral feasible region → optimizer at an extreme point.”

* * *

### 8) Micro-drills (the exact skills 3.2 is building)

You should be able to do these instantly:

1.  In  $\mathbb{R}^2$ , sketch (mentally)  $\|x\|_1\le 1$ ,  $\|x\|_2\le 1$ ,  $\|x\|_\infty\le 1$ .
2.  Convert  $\|x\|_\infty\le 1$  into component inequalities.
3.  Explain why  $\|Ax+b\|_2\le t$  defines a convex set (composition of convex norm with affine map + sublevel set).
4.  Explain why  $x^\top Px \le 1$  with  $P\succeq 0$  is convex (ellipsoid / quadratic form).
5.  Given a direction  $u$ , describe the point on the unit ball that maximizes  $u^\top x$  (tangency/supporting hyperplane picture).

* * *

That’s 3.2: norms as _geometry engines_. Next in **3.3**, we’ll make the statement “norms are convex functions” operational for modeling (epigraphs, SOC representability of  $\ell_2$ , LP representability of  $\ell_1/\ell_\infty$ ), and we’ll start building the bridge to 3.4–3.5 (dual norms + “supremum over uncertainty = dual norm”), which is the robust-optimization magic used later in PS6.

## Response:
3.3 — Norms as convex functions (and how that becomes modeling “grammar”)
-------------------------------------------------------------------------

Phase 3.2 was “what the balls look like.” Phase 3.3 is “how to treat norms as first-class convex functions” so you can _systematically_ turn norm expressions into convex constraints and standard-form blocks (LP/SOCP/SDP later).

The big conceptual punchline is:

A norm is not just a geometry object. It is a convex function with a very special structure (positively homogeneous + subadditive). That structure gives you a toolbox: epigraphs, sublevel sets, composition rules, and representability patterns.

I’ll build this in layers, from definitions → theorems → modeling templates.

* * *

### 1) What does it mean for a norm to be “a convex function”?

A function  $f:\mathbb{R}^n\to\mathbb{R}$  is convex if for all  $x,y$  and  $\theta\in[0,1]$ ,

$$
f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y).
$$

In 3.1 we proved:

> For any norm  $\|\cdot\|$ , the function  $x\mapsto \|x\|$  is convex.

Let’s re-prove it, but this time as a modeling lemma you’ll actually invoke automatically.

#### Theorem 3.3.1 (Norm convexity from axioms)

For any norm  $\|\cdot\|$ ,

$$
\|\theta x+(1-\theta)y\|\le \theta\|x\|+(1-\theta)\|y\| \quad(\forall x,y,\ \forall\theta\in[0,1]).
$$

**Proof (each step tagged by axiom):**

1.  Write the convex combo as a sum:
    
$$
\theta x+(1-\theta)y = (\theta x) + ((1-\theta)y).
$$
2.  Apply triangle inequality (N3):
    
$$
\|\theta x+(1-\theta)y\| \le \|\theta x\|+\|(1-\theta)y\|.
$$
3.  Apply homogeneity (N2) with nonnegative scalars  $\theta$  and  $1-\theta$ :
    
$$
\|\theta x\|=\theta\|x\|,\quad \|(1-\theta)y\|=(1-\theta)\|y\|.
$$
4.  Substitute:
    
$$
\|\theta x+(1-\theta)y\|\le \theta\|x\|+(1-\theta)\|y\|.
$$

That’s convexity.

**Why this proof matters:** it’s “mechanical”: anytime you see a function with homogeneity + triangle-like inequality, you can suspect convexity. (This generalizes to gauges / Minkowski functionals later.)

* * *

### 2) Sublevel sets: why “norm ≤ constant” is always convex

If  $f$  is convex, then each **sublevel set**

$$
\{x: f(x)\le \alpha\}
$$

is convex. Proof is one line: take two feasible points, apply convexity inequality, conclude the convex combo is feasible.

Apply this to  $f(x)=\|x\|$ :

#### Corollary 3.3.2 (Norm balls are convex)

$$
\{x:\|x\|\le r\} \text{ is convex for any } r\ge 0.
$$

You already knew this in 3.2, but now you understand the modeling principle:

Whenever you can show some expression is a convex function of  $x$ , writing “that expression  $\le$  something” gives a convex constraint.

This is half of convex modeling.

* * *

### 3) The epigraph viewpoint: how norms become constraints without “mysticism”

The epigraph of  $f$  is

$$
\operatorname{epi}(f)=\{(x,t): f(x)\le t\}.
$$

Since  $\|\cdot\|$  is convex, its epigraph is a convex set:

$$
\operatorname{epi}(\|\cdot\|)=\{(x,t): \|x\|\le t\} \subset \mathbb{R}^{n+1}.
$$

This set is the canonical object you use when you do epigraph transformations:

*   If your objective is  $\min \|Ax+b\|$ , you can rewrite as
    $$
    \min t \quad \text{s.t.}\quad \|Ax+b\|\le t.
    $$
    Now it’s “minimize linear objective subject to a convex constraint” — the standard gateway to LP/SOCP.

So in your head, you should see the pattern:

> “minimize a norm” = “introduce  $t$ , constrain the norm by  $t$ , minimize  $t$ .”

This is the convex-optimization equivalent of “complete the square” in algebra: a standard move.

* * *

### 4) Composition rule you will use constantly: norm of affine map is convex

In Phase 2 you learned: if  $f$  is convex and  $g(x)=Ax+b$  is affine, then  $f\circ g$  is convex.

Let  $f(z)=\|z\|$ . It’s convex. Let  $g(x)=Ax+b$ . Affine.

Therefore:

#### Theorem 3.3.3

$$
x\mapsto \|Ax+b\| \text{ is convex (for any norm and any }A,b).
$$

This is one of the most used facts in modeling, because it converts “weird-looking expressions” into “safe convex constraints.”

Now immediately:

*   Constraint  $\|Ax+b\|\le c$  is convex if  $c$  is constant.
*   Constraint  $\|Ax+b\|\le \text{(affine in }x)$  can also be convex under conditions (more in a second).

* * *

### 5) When is “norm ≤ affine” convex?

This is subtle enough that people lose points on PS6-like tasks.

Consider a constraint

$$
\|Ax+b\| \le a^\top x + d.
$$

Left side is convex in  $x$ . Right side is affine in  $x$ .

The set  $\{x: \|Ax+b\|\le a^\top x + d\}$  is convex **if the right-hand side is not doing something illegal**. The typical legality condition is:

*   You must ensure  $a^\top x + d \ge 0$  on the feasible set, because norms are always  $\ge 0$ , and many standard-form cones (SOC) implicitly require a nonnegative “radius” coordinate.

Modeling-wise, the clean way is:

$$
\|Ax+b\| \le t,\quad t = a^\top x + d,\quad t\ge 0.
$$

Then you separate the convex epigraph constraint from the affine definition of  $t$ . This separation is how SOCP constraints are written:  $(t, Ax+b)\in \mathcal{Q}$  with  $t\ge 0$ .

Keep this in mind: you often need an extra  $t\ge 0$  line to make it a valid conic form.

* * *

### 6) Representability (the “languages” preview):  $\ell_1/\ell_\infty$  → LP,  $\ell_2$  → SOCP

3.3 is still “norms are convex,” but it’s the right time to connect to Phase 4/5 modeling patterns, because PS6 is mostly about landing in LP/SOCP/SDP.

#### 6.1  $\ell_\infty$  epigraph is linear (LP-friendly)

Constraint  $\|x\|_\infty \le t$  means:

$$
\max_i |x_i| \le t \iff |x_i|\le t\ \forall i \iff -t\le x_i\le t\ \forall i.
$$

That’s just linear inequalities. So the epigraph of  $\|\cdot\|_\infty$  is polyhedral.

More generally:  $\|Ax+b\|_\infty\le t$  becomes  $-t\mathbf{1}\le Ax+b\le t\mathbf{1}$ , still linear.

This is why  $\ell_\infty$  norms turn into LP constraints.

#### 6.2  $\ell_1$  epigraph is linear with auxiliary variables (LP-friendly)

 $\|x\|_1=\sum_i |x_i|$ . Constraint  $\|x\|_1\le t$  is not immediately linear because of absolute values. But we linearize each absolute value:

Introduce  $s_i\ge 0$  with

$$
-s_i \le x_i \le s_i,\quad \sum_i s_i \le t.
$$

Then  $\sum_i s_i$  upper bounds  $\sum_i |x_i|$ , and at optimum the bound tightens. This is the standard epigraph trick for  $\ell_1$ .

Therefore  $\ell_1$  also maps to LP.

#### 6.3  $\ell_2$  epigraph is second-order conic (SOCP-friendly)

Constraint  $\|x\|_2\le t$  defines the second-order cone:

$$
\mathcal{Q}^{n+1}=\{(t,x)\in\mathbb{R}\times\mathbb{R}^n: \|x\|_2\le t\}.
$$

So  $\|Ax+b\|_2\le t$  is exactly an SOCP constraint.

This is the core modeling block for SOCP: “Euclidean norm of affine expression bounded by affine scalar.”

3.3 takeaway: convexity tells you it’s legal; representability tells you which solver language it fits.

* * *

### 7) A deeper structural viewpoint: norms are sublinear functions

This is a powerful “classification theorem” that unifies a lot of later facts.

A function  $f:\mathbb{R}^n\to\mathbb{R}$  is called **sublinear** if:

1.  (Positive homogeneity)  $f(\alpha x)=\alpha f(x)$  for  $\alpha\ge 0$ 
2.  (Subadditivity)  $f(x+y)\le f(x)+f(y)$ 

A norm satisfies these (for  $\alpha\ge 0$ ) automatically by (N2) and (N3). It also satisfies definiteness, which sublinear functions don’t require.

Key theorem:

> Every sublinear function is convex.

Proof is basically the same as the norm convexity proof: write convex combos as sums and use homogeneity + subadditivity.

So you can store: **“norms are convex because they are sublinear.”**

This matters because later dual norms / support functions / robust constraints are all expressed in the language of sublinear functions.

* * *

### 8) Modeling checklist (the PS6-relevant reflexes you’re building)

After 3.3, you should be able to look at an expression and do these without blinking:

1.  See  $\|Ax+b\|$  and immediately say: “convex, because norm is convex + affine composition.”
2.  Convert  $\min \|Ax+b\|$  into  $\min t$  s.t.  $\|Ax+b\|\le t$ .
3.  Decide representability:
    *    $\ell_2$ : SOCP
    *    $\ell_1$ ,  $\ell_\infty$ : LP (with auxiliaries)
4.  When RHS is affine, add the missing guard:
    $$
    \|Ax+b\|\le t,\ t=a^\top x+d,\ t\ge 0.
    $$
5.  Recognize the difference between “convex constraint” and “conic representable constraint.” Convex is about truth; representable is about solver language.

* * *

That’s 3.3: norms as convex functions, and how to turn “norm expressions” into epigraph constraints and solver-friendly patterns.

Next is **3.4 (dual norms)**: we define them cleanly, then derive the specific pairs  $\ell_1\leftrightarrow \ell_\infty$ ,  $\ell_2\leftrightarrow \ell_2$ , and explain geometrically why the dual ball is the polar of the primal ball. Then 3.5 is the “supremum = dual norm” lemma that powers robust optimization rewrites.

## Response:
3.4 — Dual norms (the “shadow ruler” behind worst-case bounds)
--------------------------------------------------------------

You now know: norms are convex, norm balls are convex sets, and “norm ≤ something” is a modeling primitive. Dual norms answer the next question:

When I care about the worst-case value of a dot product  $u^\top x$  over a norm ball, what number does it equal?

This is the precise mathematical engine behind robust optimization rewrites (PS6 ex 4.27 type moves) and behind many inequalities you’ve used informally (“Cauchy–Schwarz,” Hölder, etc.). Dual norms unify them.

We’ll do this in a “zero-to-hero” order:

1.  Define dual norm carefully (and prove it is a norm).
2.  Connect it to geometry (supporting hyperplanes; polar set).
3.  Compute important pairs:  $\ell_2\leftrightarrow \ell_2$ ,  $\ell_1\leftrightarrow \ell_\infty$ ,  $\ell_\infty\leftrightarrow \ell_1$ .
4.  Extract the key inequality (generalized Cauchy–Schwarz / Hölder).
5.  Explain why duality is exactly “how linear functionals see your ball.”

* * *

### 1) Setup: what is the dot product doing here?

We work in  $\mathbb{R}^n$  with the standard inner product

$$
\langle u,x\rangle = u^\top x.
$$

A linear functional  $x\mapsto u^\top x$  measures the component of  $x$  along direction  $u$ . Over a bounded convex set (like a norm ball), the maximum of a linear function occurs on the boundary, at a supporting hyperplane point. That’s the geometry from 3.2.

So: the dual norm will be the “maximum correlation with direction  $u$ ” subject to unit size in the primal norm.

* * *

2) Definition of the dual norm
------------------------------

Let  $\|\cdot\|$  be any norm on  $\mathbb{R}^n$ . Define  $\|\cdot\|_*$  on  $\mathbb{R}^n$  by

 $$
\boxed{\ \|u\|_* := \sup\{u^\top x : \|x\|\le 1\}\ } \quad (\star)
$$

This is: maximize the dot product with  $u$  over the primal unit ball.

A few immediate sanity points:

*   The feasible set  $\{x:\|x\|\le 1\}$  is compact in finite dimensions, and  $x\mapsto u^\top x$  is continuous, so the supremum is actually a maximum (achieved). But we don’t need attainment yet.
*   The value is finite because the unit ball is bounded.

Interpretation:  $\|u\|_*$  is “how big  $u^\top x$  can be when  $x$  has unit primal norm.”

* * *

3) The first big task: prove  $\|\cdot\|_*$  is indeed a norm
-------------------------------------------------------------

You must be able to do this cold. We verify the three axioms.

### Proposition 3.4.1

The function  $\|u\|_*=\sup_{\|x\|\le 1} u^\top x$  is a norm.

#### (N1) Nonnegativity and definiteness

**Nonnegativity:**  
For any  $u$ , the feasible set includes  $x=0$ , so

$$
\|u\|_*=\sup_{\|x\|\le 1} u^\top x \ge 0^\top u = 0.
$$

**Definiteness:** we show  $\|u\|_*=0 \iff u=0$ .

*   If  $u=0$ , then  $u^\top x = 0$  for all  $x$ , so the supremum is  $0$ .
*   Conversely, suppose  $\|u\|_*=0$ . That means  $u^\top x \le 0$  for all  $\|x\|\le 1$ .  
    But the unit ball is symmetric: if  $\|x\|\le 1$ , then  $\|-x\|\le 1$ . So also  $u^\top (-x)\le 0$ , i.e.  $-u^\top x\le 0$ , i.e.  $u^\top x\ge 0$ .  
    Combining:  $u^\top x = 0$  for all  $\|x\|\le 1$ .

Now use the “absorbing” property: for any vector  $y$ , we can scale it into the ball: let  $x=y/\|y\|$  (if  $y\neq 0$ ), then  $\|x\|=1$ . So  $u^\top x=0$  implies

$$
0 = u^\top \frac{y}{\|y\|} \quad \Rightarrow \quad u^\top y = 0
$$

for all  $y$ . The only vector orthogonal to all  $y$  is  $u=0$ . So definiteness holds.

#### (N2) Homogeneity

Take scalar  $\alpha\in\mathbb{R}$ . Then

$$
\|\alpha u\|_* = \sup_{\|x\|\le 1} (\alpha u)^\top x = \sup_{\|x\|\le 1} \alpha (u^\top x).
$$

If  $\alpha\ge 0$ ,  $\sup \alpha (u^\top x) = \alpha \sup (u^\top x) = \alpha \|u\|_*$ .  
If  $\alpha<0$ , then  $\sup \alpha(u^\top x) = |\alpha| \sup (-u^\top x)$ .  
But by symmetry of the ball,

$$
\sup_{\|x\|\le 1} (-u^\top x) = \sup_{\|x\|\le 1} u^\top (-x) = \sup_{\|x\|\le 1} u^\top x = \|u\|_*.
$$

So  $\|\alpha u\|_* = |\alpha|\|u\|_*$ .

#### (N3) Triangle inequality

We show  $\|u+v\|_* \le \|u\|_*+\|v\|_*$ .

By definition:

$$
\|u+v\|_* = \sup_{\|x\|\le 1} (u+v)^\top x = \sup_{\|x\|\le 1} \big(u^\top x + v^\top x\big).
$$

Now use the general inequality:  $\sup (a(x)+b(x)) \le \sup a(x) + \sup b(x)$ . (Because for every  $x$ ,  $a(x)+b(x)\le \sup a + \sup b$ , then taking sup over  $x$  keeps the inequality.)  
So

$$
\|u+v\|_* \le \sup_{\|x\|\le 1} u^\top x + \sup_{\|x\|\le 1} v^\top x = \|u\|_*+\|v\|_*.
$$

All axioms hold. So the dual norm is a norm.

* * *

4) The generalized Cauchy–Schwarz / Hölder inequality
-----------------------------------------------------

From the definition, a key inequality drops out instantly:

### Proposition 3.4.2 (Generalized Hölder inequality)

For any  $u,x\in\mathbb{R}^n$ ,

 $$
\boxed{\ u^\top x \le \|u\|_* \, \|x\|\ }.
$$

**Proof (mechanical):**

*   If  $x=0$ , trivial.
*   If  $x\neq 0$ , define  $z = x/\|x\|$ . Then  $\|z\|=1$ .
*   By definition of dual norm, for any vector  $z$  with  $\|z\|\le 1$ , we have  $u^\top z \le \|u\|_*$ . In particular  $u^\top z \le \|u\|_*$ .
*   Multiply by  $\|x\|$ :
    
$$
u^\top x = u^\top (\|x\|z) = \|x\|\,u^\top z \le \|x\|\,\|u\|_*.
$$

That is the whole inequality.

Special cases:

*   If  $\|\cdot\|=\|\cdot\|_2$ , then  $\|\cdot\|_*=\|\cdot\|_2$ , and this becomes the usual Cauchy–Schwarz:  $u^\top x\le \|u\|_2\|x\|_2$ .
*   If  $\|\cdot\|=\|\cdot\|_1$ , then dual is  $\|\cdot\|_\infty$ , giving the  $\ell_1$ \- $\ell_\infty$  Hölder bound.
*   If  $\|\cdot\|=\|\cdot\|_p$ , dual is  $\|\cdot\|_q$  with  $1/p+1/q=1$  (we’ll at least prove the key ones you need).

This inequality is the algebraic form of “dot product is bounded by product of primal and dual sizes.”

* * *

5) Geometry: dual ball is the polar of the primal ball
------------------------------------------------------

Let primal unit ball  $B=\{x:\|x\|\le 1\}$ .

Define its **polar set** (also called polar body) by

$$
B^\circ := \{u : u^\top x \le 1\ \text{for all }x\in B\}.
$$

This is a set of all directions  $u$  whose linear functional is bounded by 1 on  $B$ .

Now compute what  $B^\circ$  is in terms of the dual norm:

*   By definition of dual norm,  $\|u\|_* = \sup_{x\in B} u^\top x$ .
*   So the condition “ $u^\top x\le 1$  for all  $x\in B$ ” is exactly “the supremum over  $x\in B$  is  $\le 1$ .”
*   i.e.
    
$$
u\in B^\circ \iff \sup_{x\in B} u^\top x \le 1 \iff \|u\|_* \le 1.
$$

So:

 $$
\boxed{\ B^\circ = \{u:\|u\|_*\le 1\}\ }.
$$

Meaning: the **dual unit ball is the polar** of the primal unit ball. This is the cleanest geometric meaning of dual norm.

Visually in 2D:

*   The polar of a diamond ( $\ell_1$  ball) is a square ( $\ell_\infty$  ball).
*   The polar of a square is a diamond.
*   The polar of a circle is a circle.

That’s the  $\ell_1 \leftrightarrow \ell_\infty$ ,  $\ell_2 \leftrightarrow \ell_2$  fact in one picture.

* * *

6) Compute dual norms you absolutely need
-----------------------------------------

Now we do concrete computations. Each one is a maximization problem of the form

$$
\sup_{\|x\|\le 1} u^\top x.
$$

Because the constraint set is convex and the objective is linear, the optimum occurs on the boundary (extreme points / tangency), but we’ll do algebraic proofs.

### 6.1 Dual of  $\ell_2$  is  $\ell_2$ 

Claim:

$$
\|u\|_{2,*} = \|u\|_2.
$$

Proof:

We need to compute  $\sup_{\|x\|_2\le 1} u^\top x$ .

1.  Upper bound by Cauchy–Schwarz:
    
$$
u^\top x \le \|u\|_2\|x\|_2 \le \|u\|_2.
$$

So the supremum is  $\le \|u\|_2$ .

2.  Achieve this bound by choosing  $x$  aligned with  $u$ :
    *   If  $u=0$ , trivial.
*   If  $u\neq 0$ , let  $x = u/\|u\|_2$ . Then  $\|x\|_2=1$  and
    
$$
u^\top x = u^\top \frac{u}{\|u\|_2} = \frac{\|u\|_2^2}{\|u\|_2}=\|u\|_2.
$$

So supremum is exactly  $\|u\|_2$ . Hence dual is itself.

Geometric meaning: Euclidean ball is self-polar.

* * *

### 6.2 Dual of  $\ell_1$  is  $\ell_\infty$ 

Claim:

$$
\|u\|_{1,*} = \|u\|_\infty = \max_i |u_i|.
$$

We compute:

$$
\|u\|_{1,*} = \sup_{\|x\|_1\le 1} u^\top x.
$$

**Step 1: show  $\le \|u\|_\infty$ .**

For any  $x$ ,

$$
u^\top x = \sum_{i=1}^n u_i x_i \le \sum_{i=1}^n |u_i||x_i| \le \left(\max_i |u_i|\right)\sum_{i=1}^n |x_i| = \|u\|_\infty \|x\|_1.
$$

If  $\|x\|_1\le 1$ , then  $u^\top x \le \|u\|_\infty$ . Taking supremum:

$$
\sup_{\|x\|_1\le 1} u^\top x \le \|u\|_\infty.
$$

**Step 2: show  $\ge \|u\|_\infty$  by constructing an  $x$  that hits it.**

Let  $k$  be an index where  $|u_k|=\|u\|_\infty$ . Choose

$$
x_i = \begin{cases} \operatorname{sign}(u_k) & i=k,\\ 0 & i\neq k. \end{cases}
$$

Then  $\|x\|_1 = 1$  and

$$
u^\top x = u_k \operatorname{sign}(u_k) = |u_k|=\|u\|_\infty.
$$

So the supremum is at least  $\|u\|_\infty$ , and with the upper bound we conclude equality.

Geometric meaning:  $\ell_1$  ball has extreme points on coordinate axes; the maximizing dot product concentrates all mass on the coordinate with biggest  $|u_i|$ . That is why the dual is max-coordinate size.

* * *

### 6.3 Dual of  $\ell_\infty$  is  $\ell_1$ 

Claim:

$$
\|u\|_{\infty,*} = \|u\|_1 = \sum_i |u_i|.
$$

Compute:

$$
\|u\|_{\infty,*}=\sup_{\|x\|_\infty\le 1} u^\top x.
$$

Constraint  $\|x\|_\infty\le 1$  means  $|x_i|\le 1$  for all  $i$ .

**Upper bound:**

$$
u^\top x = \sum_i u_i x_i \le \sum_i |u_i||x_i|\le \sum_i |u_i|\cdot 1 = \|u\|_1.
$$

**Achieve it:**  
Choose  $x_i=\operatorname{sign}(u_i)$  for each  $i$ . Then  $|x_i|=1$  so  $\|x\|_\infty=1$ , and

$$
u^\top x = \sum_i u_i \operatorname{sign}(u_i)=\sum_i |u_i|=\|u\|_1.
$$

So equality holds.

Geometric meaning:  $\ell_\infty$  ball is a box; maximizing a linear functional over a box means pushing each coordinate to its extreme sign, producing the  $\ell_1$  sum.

* * *

7) The “dual of the dual” returns the primal
--------------------------------------------

In finite-dimensional spaces with the standard inner product, you get:

$$
\|x\|_{**} = \|x\|.
$$

Intuition: taking the polar twice returns the closed convex hull of the original set; since a norm ball is already closed, convex, balanced, and contains the origin appropriately, you get it back. You don’t need the full theorem proof right now, but remember the moral:

Duality is not arbitrary; it’s a geometric involution on balls.

* * *

8) Why PS6 cares: dual norm is how uncertainty becomes a norm term
------------------------------------------------------------------

The entire robust-constraint trick (you flagged it in your roadmap as “robust constraints → dual norm → SOCP”) is built on one single conceptual move:

When you see

$$
\sup_{\|u\|\le 1} u^\top x
$$

you should immediately think:

$$
= \|x\|_*.
$$

That exact equality is the next section (3.5). But 3.4 is where you internalize what  $\|x\|_*$  _means_ and how to compute it.

So 3.4 is the “definition and muscle,” 3.5 is the “magic lemma.”

* * *

### Micro-drills to verify you actually own 3.4

1.  Prove  $\|\cdot\|_*$  satisfies triangle inequality without skipping the “sup of sum ≤ sum of sups” step.
2.  For a given  $u$ , explicitly construct an optimizer  $x$  for the  $\ell_1$  and  $\ell_\infty$  cases (as we did).
3.  From the definition, re-derive the inequality  $u^\top x \le \|u\|_*\|x\|$  in 20 seconds.
4.  In 2D, explain (in words) why the polar of a diamond is a square.

* * *

Next is **3.5**, where we turn the definition into the robust-optimization identity you’ll use as a rewrite rule, and we’ll do it carefully enough that you can justify every equality sign on an exam.

## Response:
3.5 — The “supremum = dual norm” lemma (a.k.a. the robust-optimization magic step)
----------------------------------------------------------------------------------

This section is the hinge between “norm geometry” and “PS6 transformations.”

You already defined the dual norm in 3.4 as

$$
\|x\|_* := \sup_{\|u\|\le 1} u^\top x.
$$

So you might think 3.5 is trivial: “it’s true because it’s the definition.” That’s partly correct, but PS6-grade usage needs more:

1.  You must know exactly **which** norm is on the uncertainty set, and which becomes the **dual** in the result.
2.  You must be able to extend it from “unit ball” to “radius  $\rho$ ” and to “affine uncertainty.”
3.  You must know when the sup becomes an **absolute value**, a **norm term**, or a **support function**, and how to represent it as LP/SOCP/SDP constraints.

So 3.5 is: take the raw definition and turn it into a reliable rewrite rule + modeling templates.

* * *

1) The lemma in its cleanest form
=================================

Let  $\|\cdot\|$  be a norm on  $\mathbb{R}^n$ . Define its dual norm  $\|\cdot\|_*$  by

$$
\|x\|_*=\sup_{\|u\|\le 1} u^\top x.
$$

### Lemma 3.5.1 (Support function of the unit ball)

For every  $x\in\mathbb{R}^n$ ,

 $$
\boxed{\ \sup_{\|u\|\le 1} u^\top x = \|x\|_* \ }.
$$

Yes: this is literally the definition of dual norm, but you should interpret it as:

*   The left side is a **worst-case linear perturbation** over a norm-bounded uncertainty set.
*   The right side is a **deterministic norm** of  $x$  in the dual geometry.

This is the core robust rewrite.

* * *

2) The more useful versions (the ones you actually apply)
=========================================================

The unit-ball version is only step 0. Real problems have radii, absolute values, and affine maps.

2.1 Radius  $\rho$ : “ball of size  $\rho$ ” just scales the answer
-------------------------------------------------------------------

### Lemma 3.5.2 (Scaling)

For any  $\rho\ge 0$ ,

 $$
\boxed{\ \sup_{\|u\|\le \rho} u^\top x = \rho\,\|x\|_* \ }.
$$

**Proof (no skipped steps):**

Let  $U_\rho=\{u:\|u\|\le \rho\}$ . Use the change of variables  $u=\rho v$ .

*   If  $\|u\|\le \rho$ , then  $\|\rho v\|\le \rho \iff \rho\|v\|\le \rho \iff \|v\|\le 1$ . So  $u\in U_\rho$  iff  $v$  is in the unit ball.
*   Then
    
$$
\sup_{\|u\|\le \rho} u^\top x = \sup_{\|v\|\le 1} (\rho v)^\top x = \sup_{\|v\|\le 1} \rho (v^\top x) = \rho \sup_{\|v\|\le 1} v^\top x = \rho \|x\|_*.
$$

Done.

So “uncertainty radius” is just a scalar multiplier on the dual norm term.

* * *

2.2 Absolute value of a dot product: you get a symmetric sup
------------------------------------------------------------

Sometimes you see

$$
\sup_{\|u\|\le 1} |u^\top x|.
$$

### Lemma 3.5.3 (Absolute value)

 $$
\boxed{\ \sup_{\|u\|\le 1} |u^\top x| = \|x\|_* \ }.
$$

**Why?** Because the unit ball is symmetric:  $u$  feasible implies  $-u$  feasible.

Proof:

$$
\sup_{\|u\|\le 1} |u^\top x| = \sup_{\|u\|\le 1} \max\{u^\top x,\,-u^\top x\} = \max\left\{\sup_{\|u\|\le 1} u^\top x,\ \sup_{\|u\|\le 1} (-u^\top x)\right\}.
$$

But

$$
\sup_{\|u\|\le 1} (-u^\top x) = \sup_{\|u\|\le 1} u^\top (-x) = \| -x\|_* = \|x\|_*.
$$

And the first sup is  $\|x\|_*$  as well. So the max is  $\|x\|_*$ .

Practical takeaway: if the uncertainty set is a norm ball and the expression is linear in  $u$ , absolute values usually don’t change the answer (they just exploit symmetry).

* * *

2.3 Affine map inside the dot product: it becomes the dual norm of a transformed vector
---------------------------------------------------------------------------------------

You often see

$$
\sup_{\|u\|\le 1} u^\top (Ax+b).
$$

The uncertainty is in  $u$ , and your decision variable is  $x$ .

Since for fixed  $x$ , the quantity  $Ax+b$  is just some vector in  $\mathbb{R}^n$ , apply Lemma 3.5.1 with the vector  $y = Ax+b$ :

 $$
\boxed{\ \sup_{\|u\|\le 1} u^\top (Ax+b) = \|Ax+b\|_* \ }.
$$

And with radius  $\rho$ :

$$
\sup_{\|u\|\le \rho} u^\top (Ax+b) = \rho\,\|Ax+b\|_*.
$$

This is the exact step that turns “worst-case” into “norm of affine expression,” which then becomes LP/SOCP depending on which dual norm it is.

* * *

3) The robust-constraint template (this is the PS6 use case)
============================================================

A typical robust constraint looks like:

$$
a^\top x + \sup_{u\in \mathcal{U}} u^\top x \le c
$$

where  $\mathcal{U}$  is an uncertainty set.

If  $\mathcal{U}$  is a norm ball:

$$
\mathcal{U}=\{u:\|u\|\le \rho\},
$$

then by Lemma 3.5.2:

$$
\sup_{\|u\|\le \rho} u^\top x = \rho\|x\|_*.
$$

So the robust constraint becomes the deterministic convex constraint:

 $$
\boxed{\ a^\top x + \rho\|x\|_* \le c. \ }
$$

Now you have a standard modeling decision:

*   If  $\|\cdot\|_*$  is  $\ell_\infty$  or  $\ell_1$ : likely LP-representable.
*   If  $\|\cdot\|_*$  is  $\ell_2$ : SOCP-representable.

That is the “robust optimization magic step” you put in the roadmap.

* * *

4) Concrete examples you should be able to do instantly
=======================================================

These are the “muscle memory” versions.

Example A:  $\ell_2$  uncertainty ball gives an  $\ell_2$  norm term
--------------------------------------------------------------------

Let uncertainty be  $\|u\|_2\le \rho$ . Dual of  $\ell_2$  is  $\ell_2$ . Therefore

$$
\sup_{\|u\|_2\le \rho} u^\top x = \rho\|x\|_2.
$$

So a constraint like

$$
\sup_{\|u\|_2\le \rho} u^\top x \le t
$$

is equivalent to

$$
\rho\|x\|_2 \le t \iff \|x\|_2 \le t/\rho.
$$

That’s an SOCP constraint if  $t$  is a variable (with the usual  $t\ge 0$  guard).

Example B:  $\ell_\infty$  uncertainty ball gives an  $\ell_1$  norm term
-------------------------------------------------------------------------

Let  $\|u\|_\infty\le \rho$ . Dual of  $\ell_\infty$  is  $\ell_1$ . Hence

$$
\sup_{\|u\|_\infty\le \rho} u^\top x = \rho\|x\|_1.
$$

So robust box uncertainty becomes an  $\ell_1$  penalty/constraint, which is LP-friendly via auxiliary variables.

Example C:  $\ell_1$  uncertainty ball gives an  $\ell_\infty$  term
--------------------------------------------------------------------

If  $\|u\|_1\le \rho$ , dual is  $\ell_\infty$ :

$$
\sup_{\|u\|_1\le \rho} u^\top x = \rho\|x\|_\infty,
$$

which becomes linear inequalities:  $\|x\|_\infty\le t \iff -t\mathbf{1}\le x\le t\mathbf{1}$ .

* * *

5) Why this lemma is true geometrically (so you don’t forget it)
================================================================

The left side

$$
\sup_{\|u\|\le 1} u^\top x
$$

is the maximum value of the linear functional  $u\mapsto x^\top u$  over the primal unit ball in  $u$ \-space.

Geometrically:

*   Level sets of  $u\mapsto x^\top u$  are hyperplanes orthogonal to  $x$ .
*   Maximizing over a convex compact set slides a hyperplane outward until it just touches the set.
*   The maximum value equals the supporting hyperplane offset at the touching point.
*   That offset is exactly the **support function** of the set.
*   For a norm ball, the support function is the dual norm.

So: dual norm = “how far the unit ball extends in direction  $x$ ” (but measured via dot product support, not via the original norm itself).

This is the same “tangency to a ball” picture you already built in 3.2, now turned into a quantitative identity.

* * *

6) The one subtlety people mess up: which side gets dualized?
=============================================================

This is the most common PS6 mistake:

*   If uncertainty set is  $\|u\|\le 1$ , the answer is  $\|x\|_*$ .
*   Not  $\|x\|$ .
*   Not  $\|u\|_*$ .  
    The dual applies to the norm used to describe the uncertainty set.

Rule of thumb:

> “Uncertainty set norm” → “dual norm appears in the deterministic equivalent.”

So you must always identify: “What norm is bounding the uncertainty variable?”

* * *

7) Modeling consequences (preview of Phase 5 patterns)
======================================================

Once you rewrite the robust sup as a dual norm term, you immediately do one of:

*    $\|Ax+b\|_2 \le t$  → SOCP block.
*    $\|Ax+b\|_1 \le t$  → LP with auxiliaries.
*    $\|Ax+b\|_\infty \le t$  → LP with bounds.

So 3.5 is the bridge: “robust sup” → “norm” → “LP/SOCP.”

* * *

That’s 3.5: the exact rewrite rule, its scaled/absolute/affine variants, and the one big conceptual caution (dualize the uncertainty norm, not whatever feels convenient).

Next, when you’re ready, we move to Phase 4 (standard languages), starting with 4.1 epigraph standard form and then LP/QP/SOCP/SDP as target “landing zones.”

## Response:
4.1 — Epigraph standard form (the universal “translator” move)
--------------------------------------------------------------

Phase 4 is where you stop doing “convexity theory for its own sake” and start doing what PS6 actually tests: taking something that doesn’t look like a standard convex program and legally rewriting it into one of the solver languages (LP/QP/SOCP/SDP/GP) without changing the meaning.

The single most important rewrite in all of convex optimization is the epigraph trick. It is so fundamental that you should treat it like a compiler pass: whenever you see a weird objective, your first reflex is “can I epigraph it?”

### 1) What is an epigraph?

For a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  (extended-valued is important), the epigraph is the set

$$
\operatorname{epi}(f)=\{(x,t)\in\mathbb{R}^n\times\mathbb{R} : f(x)\le t\}.
$$

Interpretation: it’s the region in  $(x,t)$ \-space that lies “on or above the graph” of  $f$ .  
If  $f(x)=+\infty$  outside its domain, then the epigraph automatically enforces the domain, because “ $+\infty\le t$ ” is impossible.

Key fact you already met in Phase 2:

$$
f \text{ is convex } \iff \operatorname{epi}(f) \text{ is convex}.
$$

This is the bridge that turns “objective functions” into “constraints on sets.”

### 2) The epigraph transformation for objectives

Start with an optimization problem of the form

$$
\min_{x\in\mathcal{D}} f(x),
$$

where  $\mathcal{D}$  is whatever feasibility constraints you already have (equalities/inequalities, etc.).

Epigraph trick: introduce a new scalar variable  $t$  and rewrite as

$$
\min_{x,t}\ t \quad \text{s.t.}\quad f(x)\le t,\quad x\in\mathcal{D}.
$$

This is called putting the objective into “epigraph form,” because the constraint  $f(x)\le t$  says  $(x,t)\in\operatorname{epi}(f)$ .

The point is not cosmetic. It does two powerful things:

1.  The objective becomes linear: “minimize  $t$ ” (great for standard forms).
2.  All the nonlinearity is moved into constraints, where we can pattern-match it into LP/SOCP/SDP blocks.

### 3) Why this is _exactly_ equivalent (no handwaving)

You must be able to prove equivalence, because PS6-style grading often wants you to justify “this rewrite is legal.”

Let’s define two problems:

(P) Original:

$$
p^\star := \inf_{x\in\mathcal{D}} f(x).
$$

(E) Epigraph form:

$$
e^\star := \inf_{x,t}\ \{t : x\in\mathcal{D},\ f(x)\le t\}.
$$

Claim:  $e^\star = p^\star$ . Moreover, optimal  $x$ ’s correspond, and at optimum you can take  $t=f(x)$ .

Proof in two inequalities.

First show  $e^\star \le p^\star$ .  
Take any feasible  $x\in\mathcal{D}$  for (P). Choose  $t=f(x)$ . Then  $(x,t)$  is feasible for (E) because  $f(x)\le t$  holds with equality. The objective value in (E) is  $t=f(x)$ . Since this works for every feasible  $x$ ,

$$
e^\star \le \inf_{x\in\mathcal{D}} f(x) = p^\star.
$$

Now show  $e^\star \ge p^\star$ .  
Take any feasible  $(x,t)$  for (E). Then  $x\in\mathcal{D}$  and  $f(x)\le t$ . Since  $p^\star$  is the infimum of  $f(x)$  over  $\mathcal{D}$ , we have  $p^\star \le f(x)$ . Combine:

$$
p^\star \le f(x)\le t.
$$

So every feasible  $(x,t)$  in (E) has objective  $t\ge p^\star$ . Taking inf over feasible  $(x,t)$ ,

$$
e^\star \ge p^\star.
$$

Together:  $e^\star=p^\star$ .

Extra important conclusion: if  $(x^\star,t^\star)$  is optimal for (E), then necessarily  $t^\star=f(x^\star)$ .  
Reason: if  $t^\star>f(x^\star)$ , you could reduce  $t$  down to  $f(x^\star)$  and still satisfy  $f(x^\star)\le t$ , improving the objective. So optimum forces tightness.

That “tightness at optimum” is what makes the epigraph trick safe: it doesn’t change the minimizer  $x^\star$ ; it just adds a slack variable that becomes tight.

### 4) When is the epigraph-form problem convex?

The epigraph form

$$
\min t \ \text{s.t.}\ f(x)\le t,\ x\in\mathcal{D}
$$

is a convex optimization problem if:

*    $\mathcal{D}$  is a convex set (given by convex inequality constraints + affine equality constraints), and
*    $f$  is convex.

Because then the constraint set  $\{(x,t): f(x)\le t\}$  is exactly the epigraph of a convex function, hence convex, and intersecting with a convex  $\mathcal{D}$  keeps convexity.

So you can think of epigraph form as a “convexity-preserving compile step” when  $f$  is convex.

### 5) The modeling reason PS6 loves epigraphs: it exposes standard cones

The epigraph constraint  $f(x)\le t$  often has a known conic representation:

*   If  $f(x)=\|Ax+b\|_2$ , then  $f(x)\le t$  is SOC representable:  $\|Ax+b\|_2\le t$ .
*   If  $f(x)=\|Ax+b\|_1$ , then  $f(x)\le t$  is LP representable via auxiliary variables.
*   If  $f(x)=\|Ax+b\|_\infty$ , then  $f(x)\le t$  is linear bounds.
*   If  $f(x)=x^\top Px + q^\top x + r$  with  $P\succeq 0$ , then  $f(x)\le t$  becomes a convex quadratic inequality (QP/QCQP; sometimes SOCP/SDP via Schur complement tricks later).

So epigraph isn’t just “add  $t$ .” It’s “turn objective into a constraint whose shape I recognize.”

### 6) Epigraph of a maximum: the cleanest “split the max” trick

This is a huge practical pattern.

If

$$
f(x) = \max\{f_1(x), f_2(x), \dots, f_m(x)\},
$$

then

$$
f(x)\le t \iff f_i(x)\le t \ \forall i.
$$

Reason: “the max is ≤ t” exactly means “each term is ≤ t.”

So minimizing a max becomes:

$$
\min t \quad \text{s.t.}\quad f_i(x)\le t\ (i=1,\dots,m),\ x\in\mathcal{D}.
$$

This is the backbone of Chebyshev-center type problems, minimax formulations, and robust counterparts (before you convert sups to norms). It’s also how you linearize piecewise convex objectives.

### 7) Epigraph of a norm (connect to Phase 3)

You should see these instantly:

*   Minimize  $\|Ax+b\|_2$   
    becomes
    $$
    \min t \ \text{s.t.}\ \|Ax+b\|_2\le t.
    $$
    That’s SOCP.
*   Minimize  $\|Ax+b\|_1$   
    becomes
    $$
    \min t \ \text{s.t.}\ \|Ax+b\|_1\le t,
    $$
    then introduce  $s\ge 0$  and write  $-s \le Ax+b \le s,\ \mathbf{1}^\top s \le t$ . That’s LP.
*   Minimize  $\|Ax+b\|_\infty$   
    becomes
    $$
    \min t \ \text{s.t.}\ -t\mathbf{1}\le Ax+b \le t\mathbf{1}.
    $$
    That’s LP.

This is exactly how Phase 3 feeds Phase 4.

### 8) Domains and extended-valued functions (where people quietly lose points)

This matters a lot in PS sets: logs, barriers, ratios, GP, etc.

If  $f$  is extended-valued, say

$$
f(x)=\begin{cases} g(x), & x\in \mathrm{dom}\,g,\\ +\infty, & \text{otherwise}, \end{cases}
$$

then the constraint  $f(x)\le t$  automatically implies  $x\in\mathrm{dom}\,g$ . So you don’t “forget domain constraints” if you model the function as extended-valued correctly.

But if you write  $f(x)=g(x)$  and forget to say “with  $x$  in domain,” you can accidentally allow illegal  $x$  (like  $x\le 0$  inside  $\log x$ ). This is one of your listed failure modes, and epigraph thinking is one antidote: treat domain as part of the function definition, not an afterthought.

### 9) Epigraph vs hypograph: minimization vs maximization

For maximization you’d use the hypograph:

$$
\operatorname{hypo}(f)=\{(x,t): f(x)\ge t\}.
$$

Concave maximization problems often get rewritten similarly. For PS6 you mostly land in minimization convex programs, but you’ll sometimes flip signs: maximize concave  $f$  is equivalent to minimize convex  $-f$ , then epigraph.

### 10) The “epigraph checklist” (what you should do automatically)

Whenever you see an objective you want to “standard-form-ize,” run this mental procedure:

1.  Introduce  $t$ , rewrite objective as “minimize  $t$ .”
2.  Add constraint  $f(x)\le t$ .
3.  If  $f$  is a max/sum/norm/quadratic/log-sum-exp/etc., apply the known epigraph identity to break it into standard constraints.
4.  Add any missing domain constraints explicitly if you haven’t modeled  $f$  as extended-valued.
5.  Check: do constraints now match LP/QP/SOCP/SDP grammar?

That’s 4.1: epigraph standard form as the universal translator from “weird objective” to “linear objective + recognizable convex constraints.”

Next is 4.2 (LP) where we turn specific epigraph constraints—absolute values,  $\ell_1$ ,  $\ell_\infty$ , max of affine functions—into pure linear inequalities.

## Response:
4.2 — Linear Programs (LP): the “polyhedral language” and the core rewrite patterns
-----------------------------------------------------------------------------------

An LP is the simplest serious convex optimization language. It’s so simple that almost every modeling trick in PS6 is: “can I rewrite this thing until it becomes LP / SOCP / SDP?” LP is the first landing zone.

But to use LP like a pro, you need two skill layers:

1.  **Geometry truth layer:** LP feasible sets are polyhedra (intersections of halfspaces). Objectives are linear, so optima occur at extreme points (vertices) when bounded.
2.  **Engineering modeling layer:** you must know the small set of “legal rewrite atoms” that convert common expressions (absolute values, max,  $\ell_1$ ,  $\ell_\infty$ , piecewise-linear convex functions) into linear inequalities by introducing auxiliary variables.

We’ll build both, with rigorous equivalences.

* * *

1) What is an LP, exactly?
==========================

### Standard “inequality form”

$$
\begin{aligned} \min_x\quad & c^\top x\\ \text{s.t.}\quad & Ax \le b, \end{aligned}
$$

where:

*    $x\in\mathbb{R}^n$  is the decision variable,
*    $c\in\mathbb{R}^n$ ,
*    $A\in\mathbb{R}^{m\times n}$ ,
*    $b\in\mathbb{R}^m$ ,
*   and  $\le$  is componentwise.

You can also allow equalities  $Ex=h$  and variable bounds  $x\ge 0$ . All are linear constraints.

### Why it’s convex (and why it’s “the polyhedral language”)

*   Each inequality  $a_i^\top x \le b_i$  defines a **halfspace**, which is convex.
*   Intersection of convex sets is convex. So feasible region  $ \{x: Ax\le b\}$  is convex.
*   Linear objective  $c^\top x$  is convex (and concave), so minimizing it over a convex set is a convex optimization problem.

A region defined by finitely many linear inequalities/equalities is called a **polyhedron**. If it’s bounded, it’s a **polytope**.

* * *

2) The fundamental modeling principle of LP: “introduce slack variables”
========================================================================

LP modeling is mostly about replacing nonlinear expressions by new variables plus linear constraints that force those variables to behave as desired.

This is exactly the epigraph mindset from 4.1, specialized to functions whose epigraphs are polyhedra.

So the mantra is:

> If a function is convex and piecewise-linear, its epigraph is a polyhedron ⇒ it is LP-representable.

The biggest sources of convex piecewise-linear structure in PS6:

*   absolute value,
*   max of affine functions,
*    $\ell_1$ ,  $\ell_\infty$  norms,
*   hinge loss / ReLU type functions,
*   piecewise-linear penalties.

We now do each pattern as a precise equivalence.

* * *

3) Absolute value linearization (the most important LP atom)
============================================================

3.1 Scalar absolute value
-------------------------

Claim:

$$
|u|\le t \quad \Longleftrightarrow\quad -t\le u\le t,\ \ t\ge 0.
$$

**Proof (both directions):**

*   ( $\Rightarrow$ ) If  $|u|\le t$ , then by definition  $-t\le u\le t$ . Also  $|u|\ge 0$  implies  $t\ge 0$  (since  $t$  must be at least  $|u|$ ).
*   ( $\Leftarrow$ ) If  $-t\le u\le t$ , then  $u$  is within distance  $t$  of 0, which is exactly  $|u|\le t$ . (More formally:  $u\le t$  and  $-u\le t$  imply  $\max(u,-u)\le t$ , but  $\max(u,-u)=|u|$ .)

This is the simplest LP conversion: absolute value becomes two linear inequalities.

3.2 Modeling  $|u|$  itself (epigraph)
--------------------------------------

To represent  $s = |u|$  in an optimization where you minimize something involving  $|u|$ , you rarely enforce equality. Instead you enforce:

$$
s\ge u,\quad s\ge -u,\quad s\ge 0
$$

and then make  $s$  appear in an objective you are minimizing (or constraint you are tightening), which forces it to become tight at optimum.

Why these constraints work:

*   They imply  $s\ge \max(u,-u)=|u|$ .
*   If you minimize  $s$ , you’ll push it down until  $s=|u|$ .

That is a standard “epigraph tightness” argument (same logic as 4.1).

* * *

4) Max of affine functions (the second LP atom)
===============================================

Let  $f_i(x)=a_i^\top x + b_i$  be affine functions. Define

$$
f(x) = \max_{i=1,\dots,m} f_i(x).
$$

### Epigraph identity

$$
f(x)\le t \iff f_i(x)\le t\ \forall i.
$$

So to model  $t \ge \max_i (a_i^\top x+b_i)$ , you impose:

$$
t \ge a_i^\top x + b_i,\quad i=1,\dots,m.
$$

This is linear because each constraint is linear.

### The minimax LP template

A very common LP is:

$$
\min_x \max_i (a_i^\top x+b_i).
$$

Epigraph it:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad a_i^\top x + b_i \le t\ \forall i.
$$

This is the backbone of Chebyshev center (in  $\ell_\infty$ ), worst-case constraints, and many robust linear programs.

* * *

5)  $\ell_\infty$  norm as an LP constraint (box geometry)
==========================================================

Recall:

$$
\|z\|_\infty = \max_i |z_i|.
$$

Constraint  $\|z\|_\infty \le t$  is:

$$
|z_i|\le t \ \forall i \iff -t \le z_i \le t \ \forall i.
$$

So:

$$
\|Ax+b\|_\infty \le t \iff -t\mathbf{1} \le Ax+b \le t\mathbf{1}.
$$

This is _purely linear_. No extra auxiliary vector needed.

Why it’s LP-representable:  $\ell_\infty$  ball is a polyhedron (a box).

* * *

6)  $\ell_1$  norm as an LP constraint (needs auxiliary variables)
==================================================================

$$
\|z\|_1 = \sum_{i=1}^n |z_i|.
$$

Constraint  $\|z\|_1 \le t$  is not linear directly because of absolute values inside the sum. The standard move:

Introduce  $s\in\mathbb{R}^n$  with  $s\ge 0$  and enforce:

$$
-s \le z \le s,\qquad \mathbf{1}^\top s \le t.
$$

### Proposition 4.2.1 (Exact equivalence)

For any  $z$ ,

$$
\|z\|_1 \le t \quad\Longleftrightarrow\quad \exists s\ge 0:\ -s\le z\le s,\ \mathbf{1}^\top s\le t.
$$

**Proof:**

( $\Rightarrow$ ) Suppose  $\|z\|_1\le t$ . Let  $s_i=|z_i|$ . Then  $s\ge 0$ ,  $-s_i\le z_i\le s_i$  holds by definition of abs, and  $\mathbf{1}^\top s=\sum |z_i|=\|z\|_1\le t$ .

( $\Leftarrow$ ) Suppose there exists  $s\ge 0$  with  $-s\le z\le s$  and  $\mathbf{1}^\top s\le t$ . Then for each  $i$ ,  $|z_i|\le s_i$ . Summing:

$$
\|z\|_1=\sum_i |z_i| \le \sum_i s_i = \mathbf{1}^\top s \le t.
$$

So equivalence is exact. No relaxation.

Thus:

$$
\|Ax+b\|_1 \le t
$$

becomes:

$$
-s \le Ax+b \le s,\quad \mathbf{1}^\top s \le t,\quad s\ge 0.
$$

That’s LP.

* * *

7) Piecewise-linear convex penalties (hinge/ReLU) as LP
=======================================================

A common convex piecewise-linear function is:

$$
(u)_+ := \max(u,0).
$$

Epigraph representation:

$$
(u)_+ \le t \iff u\le t,\ 0\le t.
$$

More useful for objectives: to model  $t=(u)_+$  in minimization, impose

$$
t\ge u,\quad t\ge 0
$$

and minimize something increasing in  $t$ .

Similarly, a general convex piecewise-linear function can be expressed as max of finitely many affine functions:

$$
f(x) = \max_{j=1,\dots,k} (a_j^\top x + b_j),
$$

and therefore is LP-representable via the “max-of-affine” constraints.

This is a deep structural fact: **convex + piecewise-linear = max of affine**. You don’t need the full theorem proof yet, but you should recognize its modeling consequence: if you can rewrite something as a max of affine pieces, you are basically done (LP).

* * *

8) Equality constraints and free variables
==========================================

Two practical details that matter in actual LP standard forms:

### 8.1 Equality as two inequalities

$$
a^\top x = b \iff a^\top x \le b \ \text{and}\ a^\top x \ge b.
$$

The second is  $-a^\top x \le -b$ . So still linear.

### 8.2 Free variable to nonnegative variables

Some LP solvers require  $x\ge 0$ . If a variable  $x_j$  is free (can be negative), represent it as:

$$
x_j = x_j^+ - x_j^- ,\quad x_j^+\ge 0,\ x_j^-\ge 0.
$$

This is an exact reparameterization.

(You won’t always need this in PS6 writeups, but it’s part of “LP fluency.”)

* * *

9) The geometric fact that explains LP behavior: linear objective hits an extreme point
=======================================================================================

You don’t need simplex algorithm details, but you should understand the theorem-level picture:

*   Feasible set is a polyhedron (flat faces).
*   A linear objective has planar level sets.
*   Minimizing pushes the plane until it touches the feasible polyhedron.
*   Touching occurs at a face; if the optimum is unique, it’s at a vertex (extreme point).

This explains why LP solutions often “look combinatorial” (lots of constraints tight, sparse structure).

* * *

10) A mini “PS6 pattern book” for LP
====================================

These are the patterns you should recognize instantly:

1.  **Absolute value constraint/objective**  
     $|a^\top x + b|\le t$  → two inequalities.
2.  ** $\ell_\infty$  norm**  
     $\|Ax+b\|_\infty\le t$  → componentwise bounds.
3.  ** $\ell_1$  norm**  
     $\|Ax+b\|_1\le t$  → auxiliaries  $s\ge 0$ ,  $-s\le Ax+b\le s$ , sum  $s\le t$ .
4.  **Max of affine**  
     $\max_i (a_i^\top x+b_i)\le t$  →  $a_i^\top x+b_i\le t$  for all  $i$ .
5.  **Piecewise-linear convex penalties**  
    Hinge/ReLU style → “ $t\ge$  each piece,” minimize  $t$  or include  $t$  in objective.

These atoms are enough to solve a huge fraction of “turn this into LP” exercises.

* * *

If you want to keep the dependency ordering, the next natural section is **4.3 QP** (quadratic objectives with PSD matrices) and how they connect to ellipsoids and least squares, and then **4.5 SOCP**, where  $\ell_2$  norms become a first-class conic constraint.

## Response:
4.3 — Quadratic Programs (QP): convex quadratics, least squares, and why PSD is the whole game
----------------------------------------------------------------------------------------------

LP was the “polyhedral language.” QP is the next landing zone: you’re still optimizing over a convex feasible set (often polyhedral), but your objective (and sometimes constraints) can be **quadratic**.

A lot of PS6-style problems secretly reduce to “least squares with constraints,” and convex QP is exactly that.

We’ll do this in four layers:

1.  What a quadratic function is (algebra + geometry).
2.  When a quadratic is convex (PSD condition), with multiple equivalent characterizations.
3.  What a convex QP is, and how it relates to least squares.
4.  Modeling patterns: completing the square, epigraphs, and how to recognize QP structure.

* * *

1) Quadratic functions: the object we’re optimizing
===================================================

A general quadratic function on  $\mathbb{R}^n$  has the form

$$
q(x) = \frac{1}{2}x^\top P x + q^\top x + r,
$$

where:

*    $P\in\mathbb{R}^{n\times n}$  is a matrix,
*    $q\in\mathbb{R}^n$ ,
*    $r\in\mathbb{R}$ .

### 1.1 Symmetry matters (and you can assume it w.l.o.g.)

Notice:

$$
x^\top P x = x^\top \left(\frac{P+P^\top}{2}\right) x
$$

because  $x^\top(P-P^\top)x = 0$  for any skew-symmetric matrix  $P-P^\top$ . (Reason:  $x^\top S x = (x^\top S x)^\top = x^\top S^\top x = -x^\top S x$  if  $S^\top=-S$ , so it must be 0.)

So only the symmetric part matters. Therefore we can always take  $P$  symmetric:

$$
P=P^\top.
$$

From now on, assume  $P$  is symmetric.

* * *

2) When is a quadratic function convex?
=======================================

This is the central truth of QP modeling:

$$
q(x) = \frac{1}{2}x^\top P x + q^\top x + r \text{ is convex } \iff P \succeq 0.
$$

Here  $P\succeq 0$  means  $P$  is **positive semidefinite (PSD)**:

$$
x^\top P x \ge 0 \quad \forall x.
$$

We’ll prove this in several complementary ways because each becomes useful later.

* * *

2.1 Hessian test (fast, standard)
---------------------------------

Compute gradient and Hessian.

For symmetric  $P$ ,

$$
\nabla q(x) = Px + q,
$$
 
$$
\nabla^2 q(x) = P.
$$

A twice-differentiable function is convex on a convex domain iff its Hessian is PSD everywhere. Here the Hessian is constant, so:

$$
q \text{ convex } \iff P\succeq 0.
$$

That’s the clean “calculus” route.

* * *

2.2 “Line restriction” proof (connects to Phase 2 principles)
-------------------------------------------------------------

Another way: a function is convex iff its restriction to any line is convex.

Take any  $x\in\mathbb{R}^n$  and any direction  $d\in\mathbb{R}^n$ . Consider the 1D function

$$
\phi(t) := q(x+td).
$$

Compute:

$$
\phi(t) = \frac{1}{2}(x+td)^\top P(x+td) + q^\top(x+td) + r.
$$

Expand:

$$
\phi(t)=\frac{1}{2}(x^\top Px + 2t d^\top Px + t^2 d^\top P d) + q^\top x + t q^\top d + r.
$$

Group by powers of  $t$ :

$$
\phi(t)=\underbrace{\left(\frac{1}{2}x^\top Px + q^\top x + r\right)}_{\text{constant}} + t\underbrace{(d^\top Px + q^\top d)}_{\text{linear}} + \frac{1}{2}t^2\underbrace{(d^\top P d)}_{\text{quadratic coefficient}}.
$$

A 1D quadratic  $\alpha t^2 + \beta t + \gamma$  is convex iff  $\alpha\ge 0$ . Here  $\alpha=\frac{1}{2}d^\top P d$ . So  $\phi$  is convex for every direction  $d$  iff  $d^\top P d\ge 0$  for all  $d$ , i.e.  $P\succeq 0$ .

This proof is important because later, for QCQPs and SOCP/SDP transformations, you often reduce to checking directional curvature.

* * *

2.3 “Completing the square” proof (geometric intuition)
-------------------------------------------------------

Assume  $P\succeq 0$ . If  $P$  is actually positive definite ( $\succ 0$ ), it is invertible and we can rewrite:

$$
q(x)=\frac{1}{2}(x+P^{-1}q)^\top P (x+P^{-1}q) + \left(r - \frac{1}{2}q^\top P^{-1}q\right).
$$

Derivation (step-by-step):

$$
\frac{1}{2}(x+P^{-1}q)^\top P (x+P^{-1}q) = \frac{1}{2}(x^\top P x + 2 q^\top x + q^\top P^{-1}q).
$$

Subtract the extra constant term  $\frac{1}{2}q^\top P^{-1}q$  and add  $r$ , you recover the original.

Geometric meaning:

*   A convex quadratic is “a bowl” whose level sets are ellipsoids (or cylinders if only semidefinite).
*   The minimizer (unconstrained) is where the gradient is zero:
    $$
    Px+q=0\Rightarrow x^\star=-P^{-1}q \quad (\text{if }P\succ 0).
    $$

If  $P\succeq 0$  but singular, you can still express  $x^\top Px$  as  $\|R x\|_2^2$  for some  $R$  (e.g., Cholesky on the range), and the function is convex but may have flat directions.

This viewpoint is very useful for “least squares = QP” below.

* * *

3) What is a (convex) Quadratic Program?
========================================

A **QP** is an optimization problem with a quadratic objective and linear constraints. The standard convex QP form:

$$
\begin{aligned} \min_x\quad & \frac{1}{2}x^\top P x + q^\top x + r \\ \text{s.t.}\quad & Ax \le b,\\ & Ex = h, \end{aligned}
$$

with the critical convexity requirement:

$$
P \succeq 0.
$$

Everything in the constraints is linear, so the feasible set is a polyhedron. You are minimizing a convex function over a convex set → convex optimization problem.

If  $P$  is not PSD (has a negative eigenvalue), the objective is nonconvex and the problem becomes much harder in general.

* * *

4) Least squares is the canonical convex QP
===========================================

This is not optional: you must be fluent here because half of convex modeling is “recognize least squares hiding in a corner.”

Consider

$$
\min_x \|Ax-b\|_2^2.
$$

Expand:

$$
\|Ax-b\|_2^2 = (Ax-b)^\top(Ax-b)=x^\top A^\top A x - 2 b^\top A x + b^\top b.
$$

So it is a quadratic objective with:

$$
P = 2A^\top A \succeq 0,\quad q = -2A^\top b,\quad r=b^\top b.
$$

(Depending on whether you include the  $\tfrac12$  convention, you’ll get  $P=A^\top A$  and  $q=-A^\top b$ . Both are the same optimization problem.)

Important:  $A^\top A$  is always PSD, because for any  $x$ ,

$$
x^\top A^\top A x = \|Ax\|_2^2 \ge 0.
$$

So least squares is always convex.

### Constrained least squares

$$
\min_x \|Ax-b\|_2^2 \quad \text{s.t. } Cx\le d
$$

is a convex QP (quadratic objective, linear constraints). Many “regularized regression with constraints” problems are exactly this.

* * *

5) Quadratic constraints vs QP vs QCQP (keep the taxonomy straight)
===================================================================

*   QP: quadratic objective + linear constraints.
*   QCQP: quadratic objective + quadratic constraints (can be convex if constraints are convex).
*   SOCP/SDP can represent many QCQPs with the right structure.

For 4.3 we stay in QP land, but it’s important to keep in mind that the moment a quadratic appears in constraints, you’re often in QCQP territory (Phase 4.4/4.5/4.6).

* * *

6) First-order optimality in unconstrained convex QP (you should know it)
=========================================================================

Consider unconstrained convex quadratic:

$$
\min_x \frac12 x^\top P x + q^\top x + r, \quad P\succeq 0.
$$
*   If  $P\succ 0$ : unique minimizer solves  $\nabla q(x)=0$ :
    $$
    Px+q=0 \Rightarrow x^\star=-P^{-1}q.
    $$
*   If  $P\succeq 0$  singular: minimizers may not be unique; you need feasibility of  $Px=-q$  in the range of  $P$ . If  $-q$  lies outside  $\mathrm{Range}(P)$ , the function is unbounded below along a null direction of  $P$  that has negative linear term. This is a real phenomenon; convexity alone doesn’t guarantee boundedness.

This matters for sanity checks: “convex” doesn’t automatically mean “has a finite minimum.”

* * *

7) Epigraph and auxiliary-variable patterns for quadratics
==========================================================

Even in QP, epigraph tricks matter because they connect to later conic forms.

### 7.1 Epigraph of a convex quadratic objective

$$
\min_x \left(\frac12 x^\top P x + q^\top x + r\right)
$$

epigraphs to

$$
\min_{x,t}\ t \quad \text{s.t.}\quad \frac12 x^\top P x + q^\top x + r \le t.
$$

This is not an LP (constraint is quadratic), but it’s a standard move when you want to combine objectives, maxima, or when turning things into SDP via Schur complements later.

### 7.2 “Square of a norm” vs “norm” (QP vs SOCP)

Be careful:

*    $\|Ax-b\|_2^2$  is quadratic → QP objective (or QCQP constraint).
*    $\|Ax-b\|_2$  is a norm → SOCP representable constraint/objective (via epigraph).

Sometimes you can choose either depending on the problem. Minimizing  $\|Ax-b\|_2$  and minimizing  $\|Ax-b\|_2^2$  have the same minimizers if unconstrained (monotone transform), but not always the same behavior with constraints and tradeoffs in multi-objective setups. In PS6, they might intentionally pick one to force you into SOCP vs QP.

* * *

8) How to recognize “is this a convex QP?” quickly (a checklist)
================================================================

Given an objective that looks quadratic, do:

1.  Put it into the canonical form  $\frac12 x^\top P x + q^\top x + r$ .
2.  Symmetrize  $P$ : replace by  $(P+P^\top)/2$ .
3.  Check convexity: is  $P\succeq 0$ ?
    *   If it is obviously  $A^\top A$  (least squares), yes.
    *   If diagonal with nonnegative entries, yes.
    *   Otherwise you’d check eigenvalues or principal minors (conceptually), but in modeling problems they usually design it to be recognizable.
4.  Confirm constraints are linear. If yes → convex QP.

* * *

9) Why QP is a “standard language” in Phase 4
=============================================

Because QP is:

*   expressive enough for least squares, ridge-like quadratic regularizers, portfolio variance minimization,
*   and still solvable efficiently with interior-point methods (and many specialized algorithms).

But in PS6, QP usually appears as an intermediate: you epigraph or transform and then it becomes SOCP/SDP if needed. So you must be bilingual: recognize QP structure and also know when to “lift” it.

* * *

If you want to keep the roadmap order, the next section is **4.4 QCQP** (quadratic constraints and when they’re convex), then **4.5 SOCP** where many QCQPs and norm constraints become a clean conic language.

## Response:
4.4 — QCQP: Quadratically Constrained Quadratic Programs (the “bridge language” to SOCP/SDP)
--------------------------------------------------------------------------------------------

A QCQP is where convex optimization starts to feel like wizardry to newcomers, because quadratics can be either perfectly convex and tame… or wildly nonconvex and evil. The difference is entirely about **PSD structure** and **which side of the inequality the quadratic sits on**.

Phase 4.4 has one goal: make you instantly recognize when a quadratic constraint is convex, and how to rewrite convex QCQPs into SOCP/SDP patterns later.

We’ll build:

1.  Definitions and taxonomy (QP vs QCQP).
2.  Exactly when a quadratic inequality defines a convex set.
3.  Geometric interpretation (ellipsoids, paraboloids, cylinders).
4.  Canonical convex QCQP forms: norm-squared constraints, trust regions, ellipsoids.
5.  Modeling moves that prepare for SOCP/SDP (lifting, Schur complement preview).
6.  Common failure modes.

* * *

1) Definition: what is a QCQP?
==============================

A **QCQP** has:

*   a quadratic objective, and
*   one or more quadratic constraints (plus possibly linear constraints).

General form:

$$
\begin{aligned} \min_x\quad & \frac12 x^\top P_0 x + q_0^\top x + r_0 \\ \text{s.t.}\quad & \frac12 x^\top P_i x + q_i^\top x + r_i \le 0,\quad i=1,\dots,m,\\ & Ax \le b,\quad Ex=h. \end{aligned}
$$

Here each  $P_i$  is symmetric WLOG (replace by  $(P_i+P_i^\top)/2$ ).

A QCQP is **convex** if:

*   the objective is convex:  $P_0\succeq 0$ ,
*   each inequality constraint function  $f_i(x)=\frac12 x^\top P_i x + q_i^\top x + r_i$  is convex:  $P_i\succeq 0$ ,
*   equalities are affine (not quadratic), and
*   linear constraints are fine.

So the first “truth rule” is:

> A quadratic inequality constraint is convex if it is of the form “convex quadratic  $\le 0$ .”

But you must be careful: “quadratic  $\le$  quadratic” can hide nonconvexity depending on how you rearrange it.

* * *

2) When does a quadratic inequality define a convex set?
========================================================

Consider a single constraint

$$
f(x) := \frac12 x^\top P x + q^\top x + r \le 0,
$$

with  $P=P^\top$ .

### Theorem 4.4.1 (Convexity of quadratic inequality)

The set  $\{x: f(x)\le 0\}$  is convex **iff**  $f$  is convex **iff**  $P\succeq 0$ .

Reason: sublevel sets of convex functions are convex. If  $P\succeq 0$ , then  $f$  is convex (same Hessian argument as 4.3). Hence its sublevel set is convex.

Conversely, if  $P$  has a negative eigenvalue,  $f$  is not convex, and its sublevel set is generically nonconvex (there are edge cases, but for modeling you treat it as nonconvex).

So the actionable rule is: check PSD of the quadratic form of each inequality.

### Why “ $\ge$ ” is usually nonconvex

If you had

$$
f(x)\ge 0
$$

with  $f$  convex, that is a **superlevel set** of a convex function, which is generally nonconvex. (Superlevel sets of concave functions are convex; sublevel sets of convex functions are convex.)

So:

*   convex quadratic  $\le$  constant → convex set
*   convex quadratic  $\ge$  constant → generally nonconvex set

This one sentence prevents a ton of mistakes.

* * *

3) Geometry: what does a convex quadratic constraint look like?
===============================================================

Assume  $P\succeq 0$ . Then  $x^\top Px$  is like a squared norm in a transformed coordinate system, because  $P$  can be factored as  $P=R^\top R$  (Cholesky / square root).

Then

$$
\frac12 x^\top P x = \frac12 \|Rx\|_2^2.
$$

So a typical convex quadratic inequality

$$
x^\top P x + q^\top x + r \le 0
$$

describes something like an ellipsoid or an “offset ellipsoid” (or cylinder) after completing the square.

### Completing the square (geometric form)

If  $P\succ 0$  (positive definite), we can rewrite:

$$
x^\top P x + 2q^\top x + 2r \le 0
$$

as

$$
(x + P^{-1}q)^\top P (x + P^{-1}q) \le q^\top P^{-1}q - 2r.
$$

So the feasible set is an ellipsoid (if the RHS is positive), a single point (if RHS = 0), empty (if RHS < 0).

If  $P\succeq 0$  but singular, you can have cylinders / slabs (flat directions).

This is why convex QCQP constraints are “ellipsoidal constraints” in general.

* * *

4) Canonical convex QCQP patterns you must recognize
====================================================

4.1 Norm-squared constraints (very common)
------------------------------------------

A form like

$$
\|Ax+b\|_2^2 \le t
$$

is a quadratic inequality.

Expand:

$$
\|Ax+b\|_2^2 = (Ax+b)^\top(Ax+b)=x^\top A^\top A x + 2b^\top A x + b^\top b.
$$

Here  $P=A^\top A\succeq 0$ , so it’s convex in  $x$ . Therefore the constraint is convex if  $t$  is constant, or if it appears on the right side as an affine variable appropriately (more on that soon).

Geometric meaning: it’s an ellipsoid in  $x$ \-space (possibly shifted).

4.2 Trust region constraint
---------------------------

Classic:

$$
\|x\|_2^2 \le \Delta^2.
$$

That is  $x^\top x \le \Delta^2$  with  $P=I\succeq 0$ . Convex.

If the objective is quadratic too, you get a “trust region subproblem,” which is a famous QCQP. It’s convex if the objective Hessian is PSD (but in numerical optimization trust region often has indefinite objective; then it’s nonconvex but still solvable by special methods—outside our convex scope).

4.3 Ellipsoid constraint in matrix form
---------------------------------------

$$
(x-c)^\top P (x-c)\le 1,\quad P\succeq 0.
$$

Expanding gives a convex quadratic inequality. This is basically “membership in an ellipsoid.”

This appears constantly in robust optimization and control.

* * *

5) “Quadratic ≤ affine” vs “norm ≤ affine”: prepare for SOCP
============================================================

Here is a modeling subtlety that PS6 often tests.

### 5.1 Norm constraint:  $\|Ax+b\|_2 \le a^\top x + d$ 

This is SOCP-friendly (if  $a^\top x + d\ge 0$  enforced). It is convex because LHS is convex and RHS is affine, and the set  $\{(x,t): \|Ax+b\|_2 \le t\}$  is convex (SOC).

### 5.2 Squared norm constraint:  $\|Ax+b\|_2^2 \le a^\top x + d$ 

This is **not** automatically SOCP. It’s a convex quadratic constraint if the RHS is constant. If the RHS is affine in  $x$ , the set

$$
\{x : \|Ax+b\|_2^2 \le a^\top x + d\}
$$

is still convex if the function  $g(x)=\|Ax+b\|_2^2 - a^\top x - d$  is convex (it is, because  $\|Ax+b\|_2^2$  is convex and subtracting an affine term preserves convexity). So convexity is okay.

But representability: turning “square” constraints into SOCP needs special tricks (rotated SOC) and typically requires nonnegativity structure. This is where Phase 5.4 (hyperbolic / rotated SOC) comes in. So at this stage, you should separate:

*   Is it convex? (truth track)
*   Can I represent it as LP/QP/SOCP/SDP? (engineering track)

A convex QCQP may be left as QCQP in some frameworks, but many solvers prefer SOCP/SDP forms.

* * *

6) A central modeling trick: lifting to a matrix variable (preview of SDP)
==========================================================================

This is the conceptual bridge: quadratic forms are linear in the outer product  $X = xx^\top$ .

Because:

$$
x^\top P x = \operatorname{tr}(P xx^\top) = \operatorname{tr}(P X).
$$

So if you define  $X=xx^\top$ , quadratic terms become linear in  $(X,x)$ . But the relation  $X=xx^\top$  is nonconvex (rank-1 constraint). Dropping rank gives an SDP relaxation.

You don’t need to use this for basic PS6 transformations unless they explicitly ask for SDP relaxation, but it’s crucial conceptual glue: “quadratic” is “linear in a lifted PSD matrix.”

We’ll do it rigorously in the SDP section (4.6) with Schur complements and LMIs.

* * *

7) Convex QCQP ↔ SOCP/SDP representability (what to remember now)
=================================================================

Not every convex QCQP is an SOCP, but many important ones are:

*   Any constraint  $\|Ax+b\|_2 \le t$  is SOCP.
*   Any constraint of the form  $x^\top Px \le t$  with  $P\succeq 0$  can often be written as  $\|R x\|_2 \le \sqrt{t}$  if  $t$  is constant, where  $R^\top R = P$ . But if  $t$  is variable, the square root makes it non-linear; then you typically use rotated SOC or SDP.

So “quadratic constraints” are a bridge: sometimes they map cleanly to SOCP (especially when they’re norms), and otherwise SDP is the universal conic umbrella.

* * *

8) The most common QCQP failure modes (PS6 traps)
=================================================

1.  **Wrong inequality direction:** writing  $x^\top Px \ge 1$  and calling it convex.  
    If  $P\succeq 0$ , that’s generally nonconvex.
2.  **Indefinite quadratic disguised as difference of PSD terms:**  
    If you see  $x^\top(P_1-P_2)x\le c$  with  $P_1,P_2\succeq 0$ , the difference may be indefinite → not convex.
3.  **Forgetting to symmetrize  $P$ :**  
    Always replace with  $(P+P^\top)/2$  before checking PSD.
4.  **Assuming “quadratic” implies “QP”:**  
    If constraints are quadratic, you’re in QCQP land, not QP.
5.  **Confusing convexity with representability:**  
    Something can be convex but not obviously LP/QP/SOCP without extra modeling.

* * *

9) What you should be able to do after 4.4 (skills checklist)
=============================================================

Given any constraint that looks quadratic, you should be able to:

*   Rewrite it as  $\frac12 x^\top P x + q^\top x + r \le 0$ .
*   Identify  $P$  and decide whether  $P\succeq 0$ .
*   Conclude convexity (or nonconvexity) based on that.
*   Recognize standard geometries: ball/ellipsoid/trust region.
*   Decide whether it’s naturally QP/QCQP or whether a norm form exists that points to SOCP.

* * *

Next is **4.5 SOCP**, where we stop “guessing” and learn the precise conic grammar: what the second-order cone is, how to express norm constraints and rotated hyperbolic constraints, and how a large fraction of convex QCQPs become SOCPs by the right transformation.

## Response:
4.5 — SOCP: Second-Order Cone Programming (the “norm + geometry” language)
--------------------------------------------------------------------------

SOCP is the workhorse language for PS6-style modeling because it captures “Euclidean norm constraints” and a surprisingly large family of convex quadratic constraints, robust constraints, and hyperbolic constraints. It’s the sweet spot: much richer than LP/QP, much simpler than SDP.

You should leave 4.5 with one superpower:

> When you see something like “ $\|(\text{affine})\|_2 \le (\text{affine})$ ” or “ $w^2 \le xy$ ” or “a convex quadratic inequality with PSD structure,” you can _mechanically_ rewrite it as an SOCP.

We’ll proceed in a careful order:

1.  Define the second-order cone and what “conic form” means.
2.  Show why  $\|x\|_2 \le t$  is exactly membership in that cone.
3.  Show closure rules: affine images/preimages.
4.  Rotated SOC and hyperbolic constraints (the  $w^2\le xy$  magic).
5.  How SOC captures many convex QCQPs.
6.  Common modeling patterns and failure modes.

* * *

1) Conic programs: what does “SOCP” mean structurally?
======================================================

A **cone**  $K\subseteq\mathbb{R}^m$  is a set closed under scaling by nonnegative scalars:

$$
z\in K,\ \alpha\ge 0 \ \Rightarrow\ \alpha z\in K.
$$

A **conic program** has the form

$$
\begin{aligned} \min_x\quad & c^\top x\\ \text{s.t.}\quad & Ax + b \in K, \end{aligned}
$$

possibly with multiple cones and affine equality constraints.

SOCP is the special case where  $K$  is a product of **second-order cones** (and maybe  $\mathbb{R}^p_+$  and equalities, which are cones too).

This matters because your modeling goal becomes:

*   rewrite constraints into “affine expression ∈ cone.”

That’s a very crisp grammar.

* * *

2) The second-order cone (SOC): definition and basic meaning
============================================================

The (standard) second-order cone in dimension  $n+1$  is

 $$
\boxed{\ \mathcal{Q}^{n+1} := \{(t,x)\in\mathbb{R}\times\mathbb{R}^n : \|x\|_2 \le t\}\ }.
$$

A few immediate facts:

*   It is a cone: if  $\|x\|_2\le t$  and  $\alpha\ge 0$ , then  $\|\alpha x\|_2 = \alpha\|x\|_2\le \alpha t$ , so  $(\alpha t,\alpha x)\in \mathcal{Q}$ .
*   It is convex: because  $\|\cdot\|_2$  is convex and  $\{(t,x):\|x\|_2\le t\}$  is an epigraph of a convex function.
*   It is closed and pointed (no lines through the origin except 0).
*   It is “ice-cream cone” shaped in 3D:  $\sqrt{x_1^2+x_2^2}\le t$ .

So the SOC is nothing more and nothing less than the epigraph of the Euclidean norm.

**Core equivalence (SOCP atom #1):**

$$
\|x\|_2 \le t \quad\Longleftrightarrow\quad (t,x)\in \mathcal{Q}^{n+1}.
$$

This is why SOCP is “the norm language.”

* * *

3) Affine maps into the SOC: the key closure rule
=================================================

In Phase 1 you learned: if  $C$  is convex, then an affine preimage  $\{x: Ax+b\in C\}$  is convex.

Apply that to  $C=\mathcal{Q}$ . Then any constraint of the form

$$
(Ax+b,\ Cx+d)\in \mathcal{Q}
$$

is convex. In the more common “norm” syntax, this is:

 $$
\boxed{\ \|Cx+d\|_2 \le Ax+b\ }.
$$

But to be a proper SOC constraint, the scalar on the right must be a scalar (or a 1D affine expression), and you typically must ensure it’s nonnegative on feasibility, because  $\|Cx+d\|_2\ge 0$ .

**SOCP atom #2 (most common PS6 pattern):**

$$
\|Fx+g\|_2 \le a^\top x + b,\quad \text{plus } a^\top x+b\ge 0.
$$

Then define  $t=a^\top x+b$  and write  $(t,Fx+g)\in \mathcal{Q}$ .

This is the canonical “ $\ell_2$  norm bounded by affine” constraint.

* * *

4) What is an SOCP formally?
============================

A standard SOCP can be written as

$$
\begin{aligned} \min_x\quad & c^\top x\\ \text{s.t.}\quad & \|A_i x + b_i\|_2 \le c_i^\top x + d_i,\quad i=1,\dots,m,\\ & Fx = g,\\ & Gx \le h. \end{aligned}
$$

Each norm inequality is an SOC membership constraint; linear equalities/inequalities can be included as well.

SOCP is convex because each SOC constraint is convex and everything else is affine.

* * *

5) Rotated second-order cone (RSOC): the hyperbola-to-cone trick
================================================================

The standard SOC handles  $\|x\|_2 \le t$ . The **rotated SOC** handles constraints like  $w^2\le xy$  with  $x,y\ge 0$ , and more generally “quadratic-over-linear” types.

One common definition (dimension  $n+2$ ):

 $$
\boxed{\ \mathcal{Q}_r^{n+2} := \{(u,v,z)\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^n : 2uv \ge \|z\|_2^2,\ u\ge 0,\ v\ge 0\}\ }.
$$

This set is convex (it’s a cone and can be mapped to standard SOC by a linear transform; also it’s well-known as a convex cone).

### 5.1 The scalar hyperbolic constraint as RSOC

Take  $n=1$  and  $z=w$ . Then

$$
(u,v,w)\in \mathcal{Q}_r^{3} \iff 2uv \ge w^2,\ u\ge 0,\ v\ge 0.
$$

If your constraint is  $w^2 \le xy,\ x\ge 0,\ y\ge 0$ , just set  $u=x$ ,  $v=y/2$ , or  $u=x/2, v=y$  depending on convention, to match  $2uv\ge w^2$ .

So the robust rewrite is:

 $$
\boxed{\ w^2 \le xy,\ x\ge 0,\ y\ge 0 \iff (x,y,w)\in \text{RSOC up to a factor of 2}. }
$$

This is exactly the “hyperbolic constraints → rotated SOC” item you listed in the roadmap (Ex 4.26). The factor-of-2 is just convention; what matters is the template: product ≥ square.

### 5.2 Quadratic-over-linear is convex and RSOC-representable

A famous convex function is the quadratic-over-linear:

$$
f(z,t)=\frac{\|z\|_2^2}{t},\quad t>0.
$$

Constraint  $\frac{\|z\|_2^2}{t}\le u$  is equivalent (for  $t>0$ ) to  $\|z\|_2^2 \le ut$ , which is hyperbolic in  $(u,t)$  and becomes RSOC:

$$
2u\cdot \frac{t}{2} \ge \|z\|_2^2,\ u\ge 0,\ t\ge 0 \quad\Longleftrightarrow\quad (u,t/2,z)\in \mathcal{Q}_r.
$$

This appears in many control/estimation problems and in some QCQP-to-SOCP conversions.

* * *

6) How SOCP captures many convex QCQPs
======================================

This is where Phase 4.4 connects.

A convex quadratic constraint often looks like:

$$
x^\top P x + q^\top x + r \le 0,\quad P\succeq 0.
$$

If  $P$  factors as  $P=R^\top R$ , then

$$
x^\top P x = \|Rx\|_2^2.
$$

So the constraint becomes

$$
\|Rx\|_2^2 + q^\top x + r \le 0.
$$

This is not yet SOC because of the square and the linear term together. But many common cases simplify:

### Case A: Pure ellipsoid / norm-squared bound

$$
x^\top P x \le \alpha,\quad P\succeq 0,\ \alpha\ge 0.
$$

Then  $\|Rx\|_2^2\le \alpha$ , equivalently  $\|Rx\|_2 \le \sqrt{\alpha}$ . If  $\alpha$  is constant, that is SOC.

If  $\alpha$  is a variable,  $\sqrt{\alpha}$  is not affine, so you instead use RSOC:

$$
\|Rx\|_2^2 \le \alpha \iff 2\alpha\cdot \frac12 \ge \|Rx\|_2^2,\ \alpha\ge 0 \iff (\alpha,1/2,Rx)\in \mathcal{Q}_r.
$$

So it becomes RSOC with a constant “1/2” as one of the two positive scalars.

### Case B: Norm ≤ affine is directly SOC

If you can rewrite the constraint as

$$
\|Fx+g\|_2 \le a^\top x + b,
$$

you are done (SOC), provided you include  $a^\top x+b\ge 0$ .

This is why so many convex QCQPs are better rewritten as norm constraints than expanded quadratics.

* * *

7) The SOCP modeling cookbook (PS6-grade patterns)
==================================================

These are the patterns you should recognize in the wild.

### Pattern 1: Euclidean norm in objective

$$
\min_x \|Ax-b\|_2
$$

Epigraph:

$$
\min_{x,t} t\ \text{s.t.}\ \|Ax-b\|_2 \le t.
$$

SOCP.

### Pattern 2: “least squares” turned into SOCP (alternative to QP)

Sometimes they prefer SOCP even for squared norms:

$$
\min \|Ax-b\|_2^2
$$

You can do QP, or you can introduce  $y=Ax-b$ , minimize  $\|y\|_2^2$  (still QP). If they want SOCP, they usually phrase it as  $\min \|Ax-b\|_2$ , not squared.

### Pattern 3: Robust linear constraint with  $\ell_2$  uncertainty

$$
a^\top x + \sup_{\|u\|_2\le \rho} u^\top x \le b
$$

Use 3.5: supremum becomes  $\rho\|x\|_2$ . Then:

$$
a^\top x + \rho\|x\|_2 \le b \iff \|x\|_2 \le \frac{b-a^\top x}{\rho},\quad b-a^\top x\ge 0.
$$

This is SOC.

### Pattern 4: Hyperbolic constraint (rotated SOC)

$$
w^2 \le xy,\ x\ge 0,\ y\ge 0
$$

→ RSOC.

### Pattern 5: Quadratic-over-linear

$$
\frac{\|Fx+g\|_2^2}{a^\top x+b} \le t,\quad a^\top x+b>0
$$

Multiply both sides:

$$
\|Fx+g\|_2^2 \le t(a^\top x+b)
$$

→ RSOC in  $(t,\ a^\top x+b,\ Fx+g)$  with positivity constraints.

* * *

8) The most common SOCP failure modes (PS6 traps)
=================================================

1.  **Right-hand side not affine / not scalar.**  
    SOC needs  $\| \cdot \|_2 \le \text{scalar}$ . If the RHS is nonlinear, you’re not in SOC (unless you introduce variables to linearize it).
2.  **Forgetting nonnegativity of the RHS scalar.**  
    Even if mathematically redundant sometimes, conic form needs it:  $t\ge 0$ .
3.  **Confusing  $\|z\|_2^2 \le t$  with  $\|z\|_2 \le t$ .**  
    The square changes representability (SOC vs RSOC). Don’t casually take square roots if  $t$  is variable.
4.  **Dropping domain constraints in quadratic-over-linear.**  
    You must enforce denominator  $>0$  (or  $\ge 0$  with care). Otherwise equivalence fails.
5.  **Mismatched dimensions in cone membership.**  
     $(t,x)\in \mathcal{Q}^{n+1}$  means  $t$  is scalar and  $x$  is  $n$ \-vector.

* * *

9) What you should be able to do after 4.5
==========================================

If you’re actually “SOCP fluent,” you can:

*   Spot SOC constraints:  $\|Ax+b\|_2 \le c^\top x + d$ .
*   Introduce epigraph variables to convert norm objectives to SOC constraints.
*   Recognize when you need RSOC (products / squares / quadratic-over-linear).
*   Convert robust sups to dual norms, then to SOC when the dual norm is  $\ell_2$ .
*   State clearly the extra conditions (nonnegativity, domain positivity) that make transformations exact.

* * *

Next is **4.6 SDP**, where the cone is the PSD cone, constraints are LMIs, and the Schur complement becomes your main “translation rule” (the SDP analogue of the SOC norm epigraph).

## Response:
4.6 — SDP: Semidefinite Programming (the “PSD cone + matrix inequality” language)
---------------------------------------------------------------------------------

SOCP was “norm constraints.” SDP is “matrix-norm / eigenvalue / quadratic form constraints.” It’s the most expressive of the standard convex cones you’ll meet in Boyd–Vandenberghe land, and PS6-style problems use it when the geometry is fundamentally about **positive semidefinite (PSD) matrices**.

Your mission in 4.6 is to become fluent in three things:

1.  What the **PSD cone** is and why “ $X\succeq 0$ ” is a convex constraint.
2.  What an **LMI** (linear matrix inequality) is and why it’s the canonical SDP constraint.
3.  The **Schur complement** trick: the main translation rule that turns many quadratic / norm / inverse / eigenvalue statements into LMIs.

We’ll build them from first principles and then show the modeling templates you’ll actually use.

* * *

1) The objects: symmetric matrices and the PSD order
====================================================

1.1 Symmetric matrices as a vector space
----------------------------------------

Let  $\mathbb{S}^n$  be the set of real symmetric  $n\times n$  matrices:

$$
\mathbb{S}^n=\{X\in\mathbb{R}^{n\times n} : X=X^\top\}.
$$

This is a real vector space of dimension  $n(n+1)/2$ .

We will optimize over  $\mathbb{S}^n$  a lot in SDP.

1.2 Positive semidefinite (PSD) matrices
----------------------------------------

A symmetric matrix  $X\in\mathbb{S}^n$  is PSD, written  $X\succeq 0$ , if

 $$
\boxed{\ x^\top X x \ge 0\quad \forall x\in\mathbb{R}^n\ }.
$$

Equivalent characterizations (you should know at least the first three):

*   **Eigenvalue characterization:**  $X\succeq 0$  iff all eigenvalues of  $X$  are  $\ge 0$ .
*   **Cholesky / square-root factorization:**  $X\succeq 0$  iff there exists  $R$  such that  $X=R^\top R$ .
*   **Principal minors:**  $X\succeq 0$  iff all principal minors are nonnegative (practically useful for small  $n$ ).

These are not just trivia: they explain why PSD constraints are convex and how they encode “squared norms.”

1.3 PSD defines a partial order (Loewner order)
-----------------------------------------------

For symmetric matrices, define:

$$
A \preceq B \quad \Longleftrightarrow\quad B-A \succeq 0.
$$

This is the **PSD order**. It’s how you say “ $B$  is bigger than  $A$  in all quadratic directions.”

This order shows up in “bounds” problems (like your roadmap’s ex 4.40), eigenvalue constraints, and matrix inequalities.

* * *

2) The PSD cone is convex (you must be able to prove this)
==========================================================

Define the PSD cone:

$$
\mathbb{S}^n_+ := \{X\in\mathbb{S}^n: X\succeq 0\}.
$$

### Proposition 4.6.1

 $\mathbb{S}^n_+$  is a convex cone.

**Cone proof:** If  $X\succeq 0$  and  $\alpha\ge 0$ , then for all  $x$ ,

$$
x^\top (\alpha X)x = \alpha(x^\top X x)\ge 0,
$$

so  $\alpha X\succeq 0$ .

**Convexity proof:** If  $X\succeq 0$  and  $Y\succeq 0$  and  $0\le \theta\le 1$ , then for all  $x$ ,

$$
x^\top(\theta X+(1-\theta)Y)x = \theta x^\top X x + (1-\theta)x^\top Y x \ge 0.
$$

So  $\theta X+(1-\theta)Y\succeq 0$ .

This is the simplest and most important “truth track” fact: PSD constraints define convex feasible sets.

* * *

3) What is an SDP?
==================

A **semidefinite program** is a convex optimization problem with a linear objective and constraints that are affine slices of the PSD cone.

A common canonical form:

$$
\begin{aligned} \min_{X\in\mathbb{S}^n}\quad & \langle C, X\rangle \\ \text{s.t.}\quad & \langle A_i, X\rangle = b_i,\quad i=1,\dots,m,\\ & X\succeq 0, \end{aligned}
$$

where  $\langle A,X\rangle := \operatorname{tr}(A^\top X)=\operatorname{tr}(AX)$  is the Frobenius/trace inner product (for symmetric matrices).

More generally, you can have vector variables  $x$  and an affine matrix expression:

$$
F(x)=F_0+\sum_{i=1}^k x_i F_i.
$$

Then the constraint

$$
F(x)\succeq 0
$$

is a linear matrix inequality (LMI). That’s the standard SDP constraint.

So:

> **SDP = linear objective + LMIs.**

* * *

4) LMIs: linear matrix inequalities (the real modeling primitive)
=================================================================

An LMI is a constraint of the form

$$
F_0 + x_1 F_1 + \cdots + x_k F_k \succeq 0,
$$

where  $F_i\in\mathbb{S}^n$  are fixed symmetric matrices and  $x\in\mathbb{R}^k$  are decision variables.

Why “linear”? Because each entry of  $F(x)$  is an affine function of  $x$ . The PSD constraint is nonlinear in entries, but convex because it’s membership in the PSD cone.

This is the exact analogue of SOC constraints  $(t,Ax+b)\in \mathcal{Q}$ , but in matrix space.

* * *

5) The Schur complement: the SDP “translation rule”
===================================================

This is the one you must master. It’s like the absolute value trick for LP, or the norm-epigraph trick for SOCP.

5.1 Statement (two-block case)
------------------------------

Consider a symmetric block matrix:

$$
M = \begin{pmatrix} A & B\\ B^\top & C \end{pmatrix},
$$

where  $A\in\mathbb{S}^p$ ,  $C\in\mathbb{S}^q$ ,  $B\in\mathbb{R}^{p\times q}$ .

Assume  $C\succ 0$  (positive definite). Then:

 $$
\boxed{\ M\succeq 0 \quad \Longleftrightarrow\quad C\succ 0\ \text{and}\ A - B C^{-1} B^\top \succeq 0 \ }.
$$

The matrix

$$
A - B C^{-1}B^\top
$$

is called the **Schur complement of  $C$  in  $M$ **.

There is a symmetric alternative: if  $A\succ 0$ , then

$$
M\succeq 0 \iff A\succ 0 \ \text{and}\ C - B^\top A^{-1} B \succeq 0.
$$

5.2 Proof idea (enough detail to trust every step)
--------------------------------------------------

I’ll prove the  $C\succ 0$  version carefully.

Assume  $C\succ 0$ . Consider the block factorization:

$$
\begin{pmatrix} I & BC^{-1}\\ 0 & I \end{pmatrix} \begin{pmatrix} A-BC^{-1}B^\top & 0\\ 0 & C \end{pmatrix} \begin{pmatrix} I & 0\\ C^{-1}B^\top & I \end{pmatrix} = \begin{pmatrix} A & B\\ B^\top & C \end{pmatrix}.
$$

You can verify by multiplying the right two factors first:

$$
\begin{pmatrix} A-BC^{-1}B^\top & 0\\ 0 & C \end{pmatrix} \begin{pmatrix} I & 0\\ C^{-1}B^\top & I \end{pmatrix} = \begin{pmatrix} A-BC^{-1}B^\top & 0\\ B^\top & C \end{pmatrix}.
$$

Then multiply on the left:

$$
\begin{pmatrix} I & BC^{-1}\\ 0 & I \end{pmatrix} \begin{pmatrix} A-BC^{-1}B^\top & 0\\ B^\top & C \end{pmatrix} = \begin{pmatrix} A-BC^{-1}B^\top + BC^{-1}B^\top & BC^{-1}C\\ B^\top & C \end{pmatrix} = \begin{pmatrix} A & B\\ B^\top & C \end{pmatrix}.
$$

Now the key PSD fact: if  $T$  is invertible, then

$$
M\succeq 0 \iff T^\top M T \succeq 0.
$$

Congruence transformations preserve PSD.

In our factorization, the outer matrices are invertible, so  $M\succeq 0$  iff the middle block-diagonal matrix is PSD:

$$
\begin{pmatrix} A-BC^{-1}B^\top & 0\\ 0 & C \end{pmatrix}\succeq 0 \iff A-BC^{-1}B^\top \succeq 0\ \text{and}\ C\succeq 0.
$$

With  $C\succ 0$  assumed, you get the equivalence.

That’s the whole Schur complement logic: PSD of a block matrix is equivalent to PSD of a simpler expression involving an inverse.

This is why SDP can represent inverse-looking constraints linearly.

* * *

6) The most important SDP modeling templates
============================================

Now we cash out the Schur complement into specific “rewrite atoms.”

6.1 Quadratic form bound as an LMI
----------------------------------

A classic constraint:

$$
x^\top P x \le t,\quad P\succeq 0
$$

is not linear. But it can be written as an LMI if  $P\succ 0$  (or with care using pseudoinverse).

Let  $P\succ 0$ . Consider:

$$
\begin{pmatrix} t & x^\top\\ x & P^{-1} \end{pmatrix}\succeq 0.
$$

Apply Schur complement with  $C=P^{-1}\succ 0$ :

$$
t - x^\top (P^{-1})^{-1} x = t - x^\top P x \ge 0 \iff x^\top P x \le t.
$$

So:

 $$
\boxed{\ x^\top P x \le t \iff \begin{pmatrix} t & x^\top\\ x & P^{-1} \end{pmatrix}\succeq 0 \quad (P\succ 0)\ }.
$$

This is a huge deal: quadratic constraints become LMIs.

(If  $P$  is only semidefinite, you can still represent related constraints with extra variables or factor  $P=R^\top R$  and use SOC/RSOC; SDP is the more general umbrella.)

6.2 Norm bound as an LMI (connect SOC ↔ SDP)
--------------------------------------------

Constraint  $\|x\|_2 \le t$  is SOC. It also has an SDP representation:

$$
\|x\|_2 \le t \iff \begin{pmatrix} t & x^\top\\ x & tI \end{pmatrix}\succeq 0.
$$

Check via Schur complement with  $C=tI$ . If  $t>0$ ,

$$
t - x^\top (tI)^{-1} x = t - \frac{1}{t}\|x\|_2^2 \ge 0 \iff \|x\|_2^2 \le t^2 \iff \|x\|_2 \le t,
$$

and PSD also implies  $t\ge 0$ . So SOC ⊂ SDP representable. (SDP generalizes SOCP.)

6.3 Eigenvalue constraints as LMIs (why SDP handles eigenvalues)
----------------------------------------------------------------

For symmetric  $X$ , the largest eigenvalue  $\lambda_{\max}(X)\le t$  is equivalent to:

$$
X \preceq tI \iff tI - X \succeq 0.
$$

That is an LMI.

Similarly,  $\lambda_{\min}(X)\ge t$  means  $X\succeq tI$ , also an LMI.

This is exactly why “eigenvalue optimization” problems land in SDP (your roadmap’s ex 4.38 type items).

* * *

7) Why SDP is the “universal convex quadratic language”
=======================================================

Two deep reasons:

1.  Quadratic forms are linear in  $xx^\top$ :  
     $x^\top P x = \operatorname{tr}(P xx^\top)$ .  
    The PSD constraint naturally controls objects like  $xx^\top$ .
2.  Schur complements turn inverse-like expressions into PSD block constraints:  
    That’s how you represent things like  $x^\top P^{-1}x$ , or matrix fractional constraints.

So SDP is the right landing zone when:

*   your constraint talks about matrix PSD order,
*   eigenvalues,
*   Schur complement structure,
*   “matrix norm” variants (spectral norm, nuclear norm—though those are advanced).

* * *

8) Failure modes (the SDP version of “forgetting t≥0”)
======================================================

1.  **Non-symmetric matrices inside PSD constraint.**  
    PSD is only defined for symmetric matrices. Always symmetrize or ensure symmetry.
2.  **Applying Schur complement without definiteness.**  
    The clean equivalence needs  $A\succ 0$  or  $C\succ 0$ . If it’s only semidefinite, the equivalence becomes more subtle (involves range conditions). In PS6 problems they usually ensure strict PD or give a form that avoids the issue.
3.  **Wrong block placement.**  
    If you swap blocks, you change which complement you’re taking. Keep track of dimensions.
4.  **Forgetting domain/positivity constraints hidden in PSD.**  
    For example,  $\begin{pmatrix} t & x^\top\\ x & tI\end{pmatrix}\succeq 0$  implies  $t\ge 0$ . Don’t separately add it if you don’t need it, but be aware it’s implied.

* * *

9) What you should be able to do after 4.6 (skills checklist)
=============================================================

*   Define PSD and prove PSD cone is convex.
*   Recognize an LMI: “affine in variables, PSD constraint.”
*   Use Schur complement to convert:
    *    $x^\top P x \le t$  into an LMI,
    *    $\|x\|_2\le t$  into an LMI,
    *   eigenvalue bounds into LMIs.
*   Explain, in words, why SDP generalizes SOCP and handles eigenvalues naturally.

* * *

Next, in Phase 5 (modeling transformations), you’ll repeatedly use the 4.x “languages” as landing zones. In particular, the Schur complement becomes a main tool for turning odd-looking inequalities into SDPs (exactly like absolute values → LP and norms → SOCP).



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)