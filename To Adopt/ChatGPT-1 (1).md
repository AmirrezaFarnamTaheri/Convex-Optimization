# 1

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/20/2025 22:08:26  
**Updated:** 12/21/2025 2:39:18  
**Exported:** 12/22/2025 1:38:14  
**Link:** [https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/6946ed11-7b28-832c-8ba3-c1ca0efb4d80](https://chatgpt.com/g/g-p-6946a9f02d688191b9421318cfc26916-convex-course/c/6946ed11-7b28-832c-8ba3-c1ca0efb4d80)  

## Response:
Updated saved memory

Got it. From now on: **one subsection per message**, strictly in order, starting now with **0.1**.

* * *

0.1 Scalars, vectors, matrices (and “type checking” so you don’t do illegal math)
---------------------------------------------------------------------------------

This subsection is painfully fundamental on purpose: most confusion later (convexity proofs, gradients/Hessians, conic constraints) comes from quietly mixing objects of different “types” (dimensions/shapes).

### 0.1.1 Scalars

A **scalar** is just a real number. We write

$$
a \in \mathbb{R}.
$$

Operations you already know are the field operations:

*   addition:  $a+b$ 
*   multiplication:  $ab$ 
*   additive identity:  $0$ 
*   multiplicative identity:  $1$ 
*   additive inverse:  $-a$ 
*   multiplicative inverse:  $a^{-1}$  when  $a\neq 0$ 

We use scalars as **coefficients** that scale vectors and matrices.

* * *

### 0.1.2 Vectors as “typed” objects

A (real) **vector in  $\mathbb{R}^n$ ** is an ordered list of  $n$  real numbers. We typically write it as a **column**:

$$
x = \begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_n \end{bmatrix} \in \mathbb{R}^n, \quad \text{where } x_i\in\mathbb{R}.
$$

Two vectors  $x,y\in\mathbb{R}^n$  are equal iff every coordinate matches:

$$
x=y \iff x_i=y_i \ \text{for all } i=1,\dots,n.
$$

#### Vector addition and scalar multiplication

For  $x,y\in\mathbb{R}^n$  and  $a\in\mathbb{R}$ , define:

*   **Addition**
    $$
    (x+y)_i := x_i + y_i \quad (i=1,\dots,n).
    $$
*   **Scalar multiplication**
    $$
    (ax)_i := a\,x_i \quad (i=1,\dots,n).
    $$

These definitions are coordinate-wise. That’s not “just a choice”: it’s what makes  $\mathbb{R}^n$  a vector space.

* * *

### 0.1.3 The vector space laws (with proofs, not vibes)

All of these are properties you will silently use later (e.g., when proving convexity closure rules, linearity of affine maps, etc.).

Let  $x,y,z\in\mathbb{R}^n$  and  $a,b\in\mathbb{R}$ .

#### (V1) Commutativity of addition:  $x+y=y+x$ 

**Proof.** For each coordinate  $i$ ,

$$
(x+y)_i = x_i+y_i = y_i+x_i = (y+x)_i.
$$

Since all coordinates match,  $x+y=y+x$ . ∎

#### (V2) Associativity of addition:  $(x+y)+z = x+(y+z)$ 

**Proof.** For each coordinate  $i$ ,

$$
((x+y)+z)_i = (x+y)_i + z_i = (x_i+y_i)+z_i = x_i+(y_i+z_i) = x_i+(y+z)_i = (x+(y+z))_i.
$$

So the vectors are equal. ∎

#### (V3) Additive identity: there exists  $0\in\mathbb{R}^n$  s.t.  $x+0=x$ 

Define  $0 := (0,\dots,0)^\top$ .

**Proof.** For each coordinate  $i$ ,

$$
(x+0)_i = x_i+0 = x_i.
$$

Hence  $x+0=x$ . ∎

#### (V4) Additive inverse: for each  $x$  there exists  $-x$  s.t.  $x+(-x)=0$ 

Define  $(-x)_i := -x_i$ .

**Proof.** For each coordinate  $i$ ,

$$
(x+(-x))_i = x_i + (-x_i)=0.
$$

So  $x+(-x)=0$ . ∎

#### (V5) Distributivity over vector addition:  $a(x+y)=ax+ay$ 

**Proof.** Coordinate  $i$ :

$$
(a(x+y))_i = a(x+y)_i = a(x_i+y_i)=ax_i+ay_i = (ax+ay)_i.
$$

So equality holds. ∎

#### (V6) Distributivity over scalar addition:  $(a+b)x=ax+bx$ 

**Proof.** Coordinate  $i$ :

$$
((a+b)x)_i=(a+b)x_i=ax_i+bx_i=(ax+bx)_i.
$$

Thus equal. ∎

#### (V7) Associativity of scalar multiplication:  $a(bx)=(ab)x$ 

**Proof.** Coordinate  $i$ :

$$
(a(bx))_i=a(bx_i)=(ab)x_i=((ab)x)_i.
$$

Thus equal. ∎

#### (V8) Scalar identity:  $1\cdot x = x$ 

**Proof.** Coordinate  $i$ :

$$
(1x)_i=1\cdot x_i=x_i.
$$

So  $1x=x$ . ∎

These laws are the algebraic skeleton under everything else.

* * *

### 0.1.4 Matrices: rectangular arrays that _act_ on vectors

A real **matrix**  $A\in\mathbb{R}^{m\times n}$  is an  $m$ \-by- $n$  rectangular array of real numbers:

$$
A = [A_{ij}]_{i=1..m,\ j=1..n}.
$$
*    $m$  = number of rows
*    $n$  = number of columns

The  $j$ \-th column is written  $A_{:j}\in\mathbb{R}^m$ .  
The  $i$ \-th row is written  $A_{i:}^\top\in\mathbb{R}^n$ .

* * *

### 0.1.5 Matrix–vector product (definition + why it’s defined this way)

Let  $A\in\mathbb{R}^{m\times n}$  and  $x\in\mathbb{R}^n$ . The product  $Ax$  is defined to be the vector in  $\mathbb{R}^m$  whose  $i$ \-th component is

$$
(Ax)_i := \sum_{j=1}^n A_{ij}\,x_j.
$$

This is not arbitrary. It’s designed so that:

1.   $Ax$  depends **linearly** on  $x$ 
2.  the entries reflect “row times column” mechanics
3.  it composes nicely:  $(AB)x = A(Bx)$  (we’ll prove later in a matrix subsection, but the definition is chosen so this becomes true)

#### Two equivalent viewpoints (both will be used later)

**Row (measurement) view.**  
Row  $i$  is  $A_{i:}^\top\in\mathbb{R}^n$ . Then

$$
(Ax)_i = A_{i:}^\top x.
$$

So each row “measures” the vector  $x$  via a dot-product-like operation.

**Column (synthesis) view.**  
Let columns be  $A_{:1},\dots,A_{:n}\in\mathbb{R}^m$ . Then

$$
Ax = \sum_{j=1}^n x_j A_{:j}.
$$

So  $Ax$  is a linear combination of the columns of  $A$  with weights given by the coordinates of  $x$ .

**Proof of the column view.**  
Look at the  $i$ \-th coordinate of the RHS:

$$
\left(\sum_{j=1}^n x_j A_{:j}\right)_i = \sum_{j=1}^n x_j (A_{:j})_i = \sum_{j=1}^n x_j A_{ij} = \sum_{j=1}^n A_{ij}x_j = (Ax)_i.
$$

All coordinates match, so the vectors are equal. ∎

* * *

### 0.1.6 “Type checking”: the legality rules of multiplication

This is the simplest source of errors: multiplying shapes that don’t match.

*   You may add  $x+y$  only if  $x$  and  $y$  have the **same dimension** ( $\mathbb{R}^n$  with  $\mathbb{R}^n$ ).
*   You may multiply  $Ax$  only if  $A\in\mathbb{R}^{m\times n}$  and  $x\in\mathbb{R}^n$ . The inner dimensions must match.

So:

*    $A$  is  $m\times n$ 
*    $x$  is  $n\times 1$ 
*    $Ax$  is  $m\times 1$ 

If the “middle numbers” don’t match, the operation is undefined.

This “shape discipline” will later prevent nonsense like:

*   writing  $Ax=b$  when  $b$  is the wrong dimension,
*   claiming  $\nabla f(x)$  has the wrong shape,
*   messing up SOC constraints like  $\|Ax+b\|_2 \le c^\top x + d$ .

* * *

### 0.1.7 The key theorem for optimization: matrix–vector multiplication is linear

This is the bridge from algebra to geometry: matrices represent **linear maps**.

**Theorem (linearity).**  
Fix  $A\in\mathbb{R}^{m\times n}$ . Define  $T:\mathbb{R}^n\to\mathbb{R}^m$  by  $T(x)=Ax$ . Then  $T$  is linear, i.e.

$$
T(ax+by)=aT(x)+bT(y) \quad\text{for all }x,y\in\mathbb{R}^n,\ a,b\in\mathbb{R}.
$$

**Proof (coordinate-by-coordinate, no skipping).**

Take any  $i\in\{1,\dots,m\}$ . Start from the left side:

$$
(T(ax+by))_i = (A(ax+by))_i.
$$

By the definition of matrix–vector multiplication,

$$
(A(ax+by))_i = \sum_{j=1}^n A_{ij}\,(ax+by)_j.
$$

Now expand  $(ax+by)_j$ . By the definition of scalar multiplication and vector addition,

$$
(ax+by)_j = a x_j + b y_j.
$$

Substitute:

$$
\sum_{j=1}^n A_{ij}(a x_j + b y_j) = \sum_{j=1}^n \big(a A_{ij}x_j + b A_{ij}y_j\big).
$$

Split the sum using distributivity of sums:

$$
= a\sum_{j=1}^n A_{ij}x_j + b\sum_{j=1}^n A_{ij}y_j.
$$

Recognize each sum again as a matrix–vector product coordinate:

$$
= a(Ax)_i + b(Ay)_i = (aAx + bAy)_i.
$$

So for every coordinate  $i$ ,

$$
(A(ax+by))_i = (aAx+bAy)_i.
$$

Therefore the vectors are equal:

$$
A(ax+by)=aAx+bAy.
$$

That is exactly linearity. ∎

This theorem is why constraints like  $Ax=b$  define affine/linear sets and why “affine maps preserve convexity” later becomes believable.

* * *

### 0.1.8 Affine maps (preview, but crucial distinction)

A function  $g:\mathbb{R}^n\to\mathbb{R}^m$  is **affine** if it can be written as

$$
g(x)=Ax+b
$$

for some matrix  $A$  and vector  $b$ .

*   If  $b=0$ , it’s linear.
*   If  $b\neq 0$ , it’s a shifted linear map.

This matters because **affine structure is the safe structure** in convex optimization:

*   affine equalities define convex sets,
*   affine precomposition preserves convexity of functions,
*   cones constraints are usually “affine map lands in cone.”

We will formalize those claims later, but you now know what “affine” literally means: “matrix times vector plus shift.”

* * *

That completes **0.1**.

Next message will be **0.2 Sets** (still in Phase 0).

## Response:
Good — this is exactly the right instinct. 0.1 is not “trivial background”; it is the **load-bearing wall** of the entire roadmap. I’ll now **rewrite and significantly enrich 0.1**, making it deeper, more explicit, more rigorous, and more newcomer-proof. This **replaces** the previous 0.1 and becomes the canonical version we build on.

I will be deliberately slow, explicit, and redundant in a _useful_ way. Nothing here will be assumed later without being built here.

* * *

0.1 Scalars, vectors, matrices
==============================

_(objects, types, legality of operations — the grammar of optimization)_

Before convexity, before geometry, before optimization, we must understand **what kinds of objects exist** and **which operations are legal between them**. Most errors in convex optimization are not “conceptual” — they are **type errors** disguised as math.

Think of this subsection as learning the **grammar** of the language. Later sections write poetry; here we learn nouns and verbs.

* * *

0.1.1 Scalars: numbers that scale everything else
-------------------------------------------------

A **scalar** is an element of the real numbers:

$$
a \in \mathbb{R}.
$$

Scalars are the simplest objects in the hierarchy. They have:

*   no direction
*   no dimension
*   no shape

They serve two roles throughout optimization:

1.  **Weights / coefficients** (e.g. in convex combinations)
2.  **Objective values** (the thing we minimize)

### Field structure (why scalars behave so nicely)

The real numbers form a **field**, meaning:

*   addition and multiplication are defined
*   both are associative and commutative
*   distributivity holds
*   identities  $0$  and  $1$  exist
*   inverses exist (except division by zero)

You will not usually restate these facts, but every algebraic manipulation later depends on them.

* * *

0.1.2 Vectors: structured collections of scalars
------------------------------------------------

A **vector in  $\mathbb{R}^n$ ** is an ordered list of  $n$  real numbers.

Formally:

$$
x = (x_1,\dots,x_n), \quad x_i \in \mathbb{R}.
$$

By convention in optimization, vectors are written as **column vectors**:

$$
x = \begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_n \end{bmatrix} \in \mathbb{R}^n.
$$

### Why “dimension” matters

The symbol  $\mathbb{R}^n$  is not decoration. It is a **type label**.

*    $x \in \mathbb{R}^n$  and  $y \in \mathbb{R}^m$ 
*   If  $n \neq m$ , then ** $x+y$  is undefined**

Later, this becomes:

*   gradients live in  $\mathbb{R}^n$ 
*   constraints map  $\mathbb{R}^n \to \mathbb{R}^m$ 
*   cones live in specific dimensions

If you lose track of dimensions, convexity arguments collapse silently.

* * *

0.1.3 Vector operations (defined coordinate-wise)
-------------------------------------------------

### Vector addition

For  $x,y \in \mathbb{R}^n$ , define:

$$
(x+y)_i := x_i + y_i \quad \text{for } i=1,\dots,n.
$$

This definition is **not arbitrary**: it is chosen so that vector addition mirrors scalar addition component-by-component.

### Scalar multiplication

For  $a\in\mathbb{R}$  and  $x\in\mathbb{R}^n$ , define:

$$
(ax)_i := a\,x_i \quad \text{for } i=1,\dots,n.
$$

This turns scalars into **scaling operators** on vectors.

* * *

0.1.4 Why  $\mathbb{R}^n$  is a vector space (fully proved)
-----------------------------------------------------------

All later geometry (convex combinations, affine sets, linear maps) relies on the fact that  $\mathbb{R}^n$  is a **vector space**. That means the following laws hold — and we prove them explicitly so nothing is “magic”.

Let  $x,y,z\in\mathbb{R}^n$ ,  $a,b\in\mathbb{R}$ .

### Additive commutativity

$$
x+y=y+x.
$$

**Proof.**  
For each coordinate  $i$ ,

$$
(x+y)_i = x_i + y_i = y_i + x_i = (y+x)_i.
$$

Equality of vectors is coordinatewise, so  $x+y=y+x$ . ∎

* * *

### Additive associativity

$$
(x+y)+z = x+(y+z).
$$

**Proof.**  
For each coordinate  $i$ ,

$$
((x+y)+z)_i = (x_i+y_i)+z_i = x_i+(y_i+z_i) = (x+(y+z))_i.
$$

Thus the vectors are equal. ∎

* * *

### Zero vector (additive identity)

Define

$$
0 := (0,\dots,0)^\top \in \mathbb{R}^n.
$$

Then

$$
x+0=x.
$$

**Proof.**  
For each coordinate  $i$ ,

$$
(x+0)_i = x_i + 0 = x_i.
$$

So equality holds. ∎

* * *

### Additive inverse

For each  $x\in\mathbb{R}^n$ , define

$$
(-x)_i := -x_i.
$$

Then

$$
x + (-x) = 0.
$$

**Proof.**  
Coordinatewise,

$$
(x+(-x))_i = x_i - x_i = 0.
$$

So the result is the zero vector. ∎

* * *

### Distributivity over vectors

$$
a(x+y)=ax+ay.
$$

**Proof.**  
Coordinate  $i$ :

$$
(a(x+y))_i = a(x_i+y_i)=ax_i+ay_i=(ax+ay)_i.
$$

Thus equality holds. ∎

* * *

### Distributivity over scalars

$$
(a+b)x = ax + bx.
$$

**Proof.**  
Coordinate  $i$ :

$$
((a+b)x)_i=(a+b)x_i=ax_i+bx_i=(ax+bx)_i.
$$

∎

* * *

### Scalar associativity

$$
a(bx)=(ab)x.
$$

**Proof.**

$$
(a(bx))_i = a(bx_i)=(ab)x_i=((ab)x)_i.
$$

∎

* * *

### Scalar identity

$$
1\cdot x=x.
$$

**Proof.**

$$
(1x)_i = 1\cdot x_i = x_i.
$$

∎

* * *

Every one of these identities will later be used silently in proofs of convexity, closure properties, and optimality conditions. Now they are earned.

* * *

0.1.5 Matrices: structured linear operators
-------------------------------------------

A **matrix**  $A \in \mathbb{R}^{m\times n}$  is a rectangular array:

$$
A = [A_{ij}], \quad i=1,\dots,m,\ j=1,\dots,n.
$$

Interpretation:

*    $n$  = dimension of **input**
*    $m$  = dimension of **output**

A matrix is best thought of as a **machine** that takes vectors in  $\mathbb{R}^n$  and produces vectors in  $\mathbb{R}^m$ .

* * *

0.1.6 Matrix–vector multiplication (definition and inevitability)
-----------------------------------------------------------------

Let  $A\in\mathbb{R}^{m\times n}$ ,  $x\in\mathbb{R}^n$ .

Define:

$$
(Ax)_i := \sum_{j=1}^n A_{ij}x_j.
$$

This definition is chosen so that:

1.  the output has dimension  $m$ 
2.  the operation is linear in  $x$ 
3.  composition of matrices works

### Two complementary interpretations (both are essential)

#### Row (measurement) view

Let  $A_{i:}^\top\in\mathbb{R}^n$  be the  $i$ \-th row. Then

$$
(Ax)_i = A_{i:}^\top x.
$$

Each row is a **linear functional** acting on  $x$ .

#### Column (synthesis) view

Let  $A_{:j}\in\mathbb{R}^m$  be the  $j$ \-th column. Then

$$
Ax = \sum_{j=1}^n x_j A_{:j}.
$$

The output is a linear combination of the columns, weighted by the coordinates of  $x$ .

**Proof of equivalence.**  
Already shown earlier; it follows directly by expanding coordinates. ∎

* * *

0.1.7 Linearity of matrix–vector multiplication (proved carefully)
------------------------------------------------------------------

**Theorem.**  
For fixed  $A\in\mathbb{R}^{m\times n}$ , the map

$$
T(x)=Ax
$$

is linear:

$$
A(ax+by)=aAx+bAy.
$$

**Proof (fully expanded).**

Take coordinate  $i$ :

$$
(A(ax+by))_i = \sum_{j=1}^n A_{ij}(ax_j+by_j) = \sum_{j=1}^n (aA_{ij}x_j + bA_{ij}y_j).
$$

Split the sum:

$$
= a\sum_{j=1}^n A_{ij}x_j + b\sum_{j=1}^n A_{ij}y_j = (aAx + bAy)_i.
$$

Since this holds for all  $i$ , the vectors are equal. ∎

This fact is the reason:

*   equality constraints must be affine
*   gradients are linear approximations
*   cones accept affine preimages

* * *

0.1.8 Affine maps (the safe structure)
--------------------------------------

A function  $g:\mathbb{R}^n\to\mathbb{R}^m$  is **affine** if

$$
g(x)=Ax+b
$$

for some matrix  $A$  and vector  $b$ .

Key distinction:

*   **Linear**: passes through the origin
*   **Affine**: linear + translation

Affine maps preserve convexity of sets and convexity of functions under precomposition. This is not a coincidence; it is a structural necessity that we will prove later.

* * *

0.1.9 Type checking: legality rules you must internalize
--------------------------------------------------------

You may only:

*   add vectors of the same dimension
*   multiply  $Ax$  if inner dimensions match
*   equate objects of the same type

This prevents silent errors such as:

*   writing  $Ax=b$  with incompatible dimensions
*   forming gradients of wrong shape
*   writing malformed SOC constraints

Convex optimization is unforgiving to sloppy typing.

* * *

### Conceptual takeaway of 0.1

At this point you should be able to say, without hesitation:

*   what kind of object each symbol represents
*   whether an expression is legal
*   what space each result lives in

Only now are we ready to talk about **sets** as collections of vectors.

* * *

Next message (no deviation): **0.2 Sets**.

## Response:
Below is **Phase 0 — subsection 0.2**, continuing **strictly** along the roadmap, with no deviation in scope or ordering.

I will treat this as a **from-scratch mathematical construction**, assuming nothing except basic literacy with symbols. Everything is defined, motivated, and proved carefully. This section is long on purpose: _sets are the substrate of all optimization_. If this layer is shaky, everything later collapses silently.

* * *

**0.2 — Sets (the primitive language of feasibility)**
======================================================

0.2.0 Why sets come _before_ equations, functions, or optimization
------------------------------------------------------------------

Before optimization, before convexity, before objectives, there is a single primitive question:

> **Which points are allowed?**

That question is answered by a **set**.

An optimization problem is _nothing more_ than:

*   a **set** of feasible points, and
*   a **rule** for ranking them.

If you do not understand sets deeply, optimization degenerates into symbol-pushing with hidden logical errors.

In convex optimization, **every constraint is secretly a set**, and **every feasibility region is an intersection of sets**.  
This subsection builds the exact language needed to say that rigorously.

* * *

0.2.1 What is a set? (formal definition, no intuition hand-waving)
------------------------------------------------------------------

A **set** is a collection of objects, called **elements**.

We write:

$$
x \in C
$$

to mean “ $x$  is an element of the set  $C$ ”.

There is _no structure assumed_ unless explicitly stated.  
A set does **not** automatically have:

*   geometry,
*   distance,
*   continuity,
*   algebra,
*   convexity.

Those come _later_, and must be proved or imposed.

### Examples (intentionally basic)

1.   $\{1,2,3\}$   
    A finite set of numbers.
2.   $\mathbb{R}$   
    The set of all real numbers.
3.   $\mathbb{R}^n$   
    The set of all real vectors of length  $n$ .
4.   $\{x \in \mathbb{R}^2 : x_1^2 + x_2^2 \le 1\}$   
    A subset of the plane (a disk).

At this point, these are **just collections**, nothing more.

* * *

0.2.2 Subsets and equality of sets (logical precision)
------------------------------------------------------

### Subset

We say  $A$  is a **subset** of  $B$ , written

$$
A \subseteq B
$$

if:

$$
\forall x,\; x \in A \Rightarrow x \in B.
$$

This is a **logical implication**, not a geometric statement.

### Equality of sets

Two sets  $A$  and  $B$  are **equal** if:

$$
A \subseteq B \quad \text{and} \quad B \subseteq A.
$$

This is how _all_ set identities are proved:

*   show inclusion one way,
*   then the reverse.

There is no other method.

* * *

0.2.3 Set-builder notation (constraints _define_ sets)
------------------------------------------------------

In optimization, we almost never list elements.  
Instead, we define sets by **properties**.

### General form

$$
C = \{x \in \mathbb{R}^n : \text{property}(x)\}.
$$

This reads:

> “The set of all  $x$  in  $\mathbb{R}^n$  such that the stated property holds.”

### Examples tied to optimization

1.  Linear inequality:
    
$$
\{x : a^\top x \le b\}
$$

This is a **halfspace** (geometry comes later).

2.  Norm constraint:
    
$$
\{x : \|x\|_2 \le 1\}
$$

This is a **ball**.

3.  Multiple constraints:
    
$$
\{x : Ax = b,\; \|x\|_\infty \le 1\}
$$

This is not “two constraints”.  
It is **one set**, defined as an intersection (next section).

* * *

0.2.4 Constraints are sets (this is non-negotiable)
---------------------------------------------------

This is a **core conceptual pivot**.

A statement like:

$$
g(x) \le 0
$$

is **not** primarily an inequality.  
It is a **membership test**:

$$
x \in \{z : g(z) \le 0\}.
$$

Similarly:

*    $Ax = b$  defines a set
*    $x \ge 0$  defines a set
*    $\|x\| \le t$  defines a set

Optimization problems are always of the form:

$$
\text{find } x \in \bigcap_i C_i.
$$

Later, convexity will be a property of these  $C_i$ .

* * *

0.2.5 Intersection of sets (feasibility is logical AND)
-------------------------------------------------------

Given sets  $C_1, C_2, \dots, C_m$ , their **intersection** is:

$$
\bigcap_{i=1}^m C_i = \{x : x \in C_i \text{ for all } i\}.
$$

Interpretation:

*   Each constraint is a set
*   All constraints together mean **simultaneous membership**

### Example

Constraints:

$$
x_1 \ge 0,\quad x_2 \ge 0,\quad x_1 + x_2 \le 1
$$

Feasible set:

$$
C = \{x : x_1 \ge 0\} \cap \{x : x_2 \ge 0\} \cap \{x : x_1 + x_2 \le 1\}.
$$

This set-theoretic view is essential later for:

*   convexity proofs,
*   feasibility arguments,
*   duality,
*   Slater conditions.

* * *

0.2.6 Empty set and infeasibility
---------------------------------

The **empty set**, denoted  $\varnothing$ , has no elements.

$$
\varnothing = \{ \}
$$

In optimization language:

*   a problem is **infeasible** iff its feasible set is empty.

Example:

$$
\{x : x \ge 1\} \cap \{x : x \le 0\} = \varnothing.
$$

This is not a numerical issue.  
It is a **logical contradiction**.

Recognizing infeasibility is a set-theoretic task.

* * *

0.2.7 Superset, complement, and why we rarely use them (but must know them)
---------------------------------------------------------------------------

### Superset

$$
B \supseteq A \quad \Leftrightarrow \quad A \subseteq B.
$$

### Complement

Given a universe  $U$ , the **complement** of  $C$  is:

$$
C^c = \{x \in U : x \notin C\}.
$$

In optimization, complements are dangerous:

*   they destroy convexity,
*   they break feasibility structure.

Example:

$$
\{x : x \neq 0\}
$$

is almost never usable in convex optimization.

This is why constraints are almost always written as **membership**, not exclusion.

* * *

0.2.8 Sets vs functions (critical distinction)
----------------------------------------------

A **function** assigns a value to each point:

$$
f : \mathbb{R}^n \to \mathbb{R}.
$$

A **set** answers a yes/no question:

$$
x \in C \;?\;
$$

But there is a deep connection:

> Every function defines sets via its **sublevel sets**:

$$
\{x : f(x) \le \alpha\}.
$$

Later:

*   convex functions ⇔ convex sublevel sets
*   quasiconvexity ⇔ convex sublevel sets

This bridge only works if you are fluent in set language.

* * *

0.2.9 Indicator functions (preview, but foundational)
-----------------------------------------------------

Given a set  $C$ , define the **indicator function**:

$$
\delta_C(x) = \begin{cases} 0 & x \in C \\ +\infty & x \notin C \end{cases}
$$

This converts a **set** into a **function**.

Why this matters (flag this mentally):

*   constraints become part of the objective,
*   feasibility becomes infinite penalty,
*   duality is built from this trick.

We will return to this formally later, but the idea depends entirely on understanding sets first.

* * *

0.2.10 Common beginner failure modes (read carefully)
-----------------------------------------------------

1.  **Treating constraints as equations, not sets**  
    This causes silent errors in convexity reasoning.
2.  **Forgetting that feasibility = intersection**  
    Leads to wrong geometric intuition.
3.  **Assuming structure that was never defined**  
    A set is _not_ convex unless proven.
4.  **Confusing domain with feasible set**  
    Domain comes from function definition; feasibility comes from constraints.

* * *

0.2.11 What you must be able to do _cold_ after this subsection
---------------------------------------------------------------

You should be able to:

*   Translate any constraint into a set.
*   Express a full optimization problem as an intersection of sets.
*   Prove set equality using two inclusions.
*   Recognize infeasibility as emptiness.
*   Move cleanly between symbolic constraints and set-builder notation.

If you cannot do these instantly, later convexity proofs will feel like magic tricks instead of logic.

* * *

### Roadmap checkpoint

You now have:

*   objects (0.1),
*   collections of objects (0.2).

Next, we will introduce **functions** as maps _between_ sets, and explain why domains are not optional bookkeeping but logical requirements.

**Next subsection: 0.3 — Functions (maps, domains, extended values).**

2/2

## Response:
0.3 — Functions (maps, domains, extended values, and why “domain” is law, not decoration)
-----------------------------------------------------------------------------------------

Optimization is built out of three kinds of things:

1.  **objects** (scalars/vectors/matrices) — 0.1
2.  **collections of objects** (sets) — 0.2
3.  **rules that assign numbers to objects** (functions) — 0.3

This section is where “a problem statement” becomes mathematically well-formed. Most later disasters (wrong convexity claims, invalid gradients, broken constraints) come from violating something in 0.3, usually **domain**.

* * *

### 0.3.0 What a function is, formally (no vibes)

A **function** is a rule that assigns to each input exactly one output.

Formally, a function  $f$  is specified by three pieces:

*   a **domain** (input set)  $D$ ,
*   a **codomain** (output set)  $Y$ ,
*   a **mapping rule** that assigns each  $x\in D$  a unique value in  $Y$ .

We write:

$$
f: D \to Y,\qquad x\mapsto f(x).
$$

The phrase “exactly one output” is crucial. It means:

*   **Total on its domain:** for every  $x\in D$ ,  $f(x)$  is defined.
*   **Single-valued:** if  $x\in D$ , there is not more than one possible  $f(x)$ .

If either fails, you do not have a function (you have a relation or a multivalued map).

* * *

### 0.3.1 Functions vs expressions vs evaluation (the common confusion)

A huge beginner trap: confusing these three.

1.  **The function itself**:  $f$  (an abstract object)
2.  **An expression defining a rule**: e.g.  $x^2$ ,  $\log x$ ,  $\|Ax-b\|_2$ 
3.  **A value**:  $f(3)=9$ 

Example:

*   “ $x^2$ ” is an expression.
*   “ $f(x)=x^2$ ” defines a function rule.
*   “ $f(3)=9$ ” is evaluation.

Later, in optimization, we often define functions by formulas. But the function is not the formula; the function is the _mapping_ plus its domain.

* * *

### 0.3.2 Domain is not optional bookkeeping

There are two layers of “domain” you must keep distinct:

1.  **Declared domain**  $D$  in  $f:D\to Y$ : where the function claims to be defined.
2.  **Effective domain** (for extended-valued functions): where the function value is finite.

We’ll build the extended-valued setup carefully, but first: why domain matters at all.

#### Example 1:  $f(x)=1/x$ 

If you write “ $f(x)=1/x$ ” without a domain, you are hiding a landmine.

*   At  $x=0$ , the expression is undefined.
*   So you must define the domain as:
    
$$
f: \mathbb{R}\setminus\{0\} \to \mathbb{R},\quad f(x)=\frac{1}{x}.
$$

If you ignore domain, you will later do illegal steps like “differentiate at 0” or “minimize over all  $\mathbb{R}$ ”.

#### Example 2:  $f(x)=\log x$ 

The logarithm is defined only for  $x>0$ :

$$
f:(0,\infty)\to\mathbb{R},\quad f(x)=\log x.
$$

In convex optimization, this is not a minor detail: it is the heart of barrier methods and geometric programming. “ $x>0$ ” is not decoration; it is the difference between a legal and illegal problem.

* * *

### 0.3.3 Vector-valued vs scalar-valued functions (and why optimization mostly wants scalar-valued)

A function may output:

*   a scalar:  $f:\mathbb{R}^n\to\mathbb{R}$ 
*   a vector:  $g:\mathbb{R}^n\to\mathbb{R}^m$ 
*   a matrix:  $F:\mathbb{R}^n\to\mathbb{R}^{p\times q}$ 

Optimization objectives are usually **scalar-valued** (you minimize a number). Constraints often use **vector-valued** functions.

Example:

*   objective:  $f_0(x)=\|Ax-b\|_2^2 \in \mathbb{R}$ 
*   constraints:  $g(x)=Ax-b \in \mathbb{R}^m$ 

You’ll later need to be disciplined about “what space does this live in?” (type checking from 0.1).

* * *

### 0.3.4 The graph of a function (turning “a rule” into a set)

Given a function  $f:D\to\mathbb{R}$ , its **graph** is the set

$$
\mathrm{graph}(f) := \{(x,t)\in D\times \mathbb{R} : t=f(x)\}.
$$

This is important because it converts function statements into set statements (and convexity later is geometric).

*   “ $t=f(x)$ ” is an equality constraint (often nonconvex unless  $f$  is affine).
*   The graph lives in one higher dimension.

For vector-valued  $g:D\to\mathbb{R}^m$ :

$$
\mathrm{graph}(g) := \{(x,y)\in D\times\mathbb{R}^m : y=g(x)\}.
$$

* * *

### 0.3.5 Preimages (pullbacks): how constraints are really formed

This is one of the most important mechanisms in optimization.

Let  $g:D\to Y$  and let  $S\subseteq Y$  be a set of outputs you “allow”.

The **preimage** of  $S$  under  $g$  is:

$$
g^{-1}(S) := \{x\in D : g(x)\in S\}.
$$

Interpretation: it’s the set of inputs that map into the allowed output set.

#### Why this is the constraint mechanism

A constraint like

$$
g(x)\le 0
$$

is really:

*   define the allowed output set  $S=(-\infty,0]\subseteq\mathbb{R}$ 
*   then the feasible set is:
    
$$
\{x: g(x)\le 0\} = g^{-1}((-\infty,0]).
$$

A vector inequality

$$
g(x)\preceq 0
$$

(where  $\preceq$  means componentwise  $\le$ ) is:

*   allowed set  $S=\mathbb{R}^m_-:=\{y\in\mathbb{R}^m: y_i\le 0\ \forall i\}$ 
*   feasible set  $g^{-1}(S)$ 

This “constraint = preimage” idea is one of the main engines behind convexity-preserving rules later (affine preimages of convex sets are convex, etc.). But even before convexity, it’s simply the correct _logic_.

* * *

### 0.3.6 Extended-valued functions:  $\mathbb{R}\cup\{+\infty\}$  and why we introduce them

This is a central convex-optimization trick: we merge “objective” and “constraints” into a single function by allowing the value  $+\infty$ .

An **extended-real-valued function** is:

$$
f:\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}.
$$

(We usually avoid  $-\infty$  in convex optimization because it breaks minimization logic; if you allow  $-\infty$  carelessly you can make “minimum” meaningless.)

#### The meaning of  $+\infty$ 

*    $f(x)=+\infty$  means: **this  $x$  is forbidden / infeasible** (hard constraint).
*    $f(x)\in\mathbb{R}$  means: ** $x$  is allowed**, with that finite cost.

This allows you to write constrained problems as unconstrained ones.

* * *

### 0.3.7 Effective domain (the “real” domain in optimization)

For an extended-valued  $f$ , define its **effective domain**:

$$
\mathrm{dom}\, f := \{x\in\mathbb{R}^n : f(x) < +\infty\}.
$$

This is the set of points where the function is finite.

Key principle (tattoo it on your brain):

> In optimization, you are only allowed to optimize over  $\mathrm{dom}\, f$ . Points outside are automatically excluded.

Even if the variable symbol says  $x\in\mathbb{R}^n$ , the true feasible region is the effective domain once you encode constraints via  $+\infty$ .

* * *

### 0.3.8 Indicator functions: turning sets into functions (and constraints into cost)

Given a set  $C\subseteq\mathbb{R}^n$ , its **indicator function** is:

$$
\delta_C(x) := \begin{cases} 0 & x\in C\\ +\infty & x\notin C. \end{cases}
$$

This is not a probability indicator; it’s a convex-analysis indicator.

Then:

$$
\mathrm{dom}\,\delta_C = C.
$$

#### Why indicator functions matter

A constrained problem:

$$
\min_{x\in C} f(x)
$$

is equivalent to the unconstrained extended-valued problem:

$$
\min_{x\in\mathbb{R}^n} \big(f(x) + \delta_C(x)\big).
$$

Let’s prove that carefully, because this is a pattern we will reuse constantly.

* * *

### 0.3.9 Proof: constrained minimization equals adding an indicator

**Claim.** For any function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  and set  $C\subseteq\mathbb{R}^n$ ,

$$
\inf_{x\in C} f(x) \;=\; \inf_{x\in\mathbb{R}^n} \big(f(x)+\delta_C(x)\big).
$$

(We use  $\inf$  rather than  $\min$  because minima may not be attained; that subtlety matters later.)

**Proof (step-by-step).**

Define a new function:

$$
F(x):=f(x)+\delta_C(x).
$$

Now analyze  $F(x)$  depending on whether  $x\in C$ .

*   If  $x\in C$ , then  $\delta_C(x)=0$ , so  $F(x)=f(x)$ .
*   If  $x\notin C$ , then  $\delta_C(x)=+\infty$ , so  $F(x)=+\infty$  (in extended-real arithmetic).

So the only points that can possibly contribute to the infimum of  $F$  are points in  $C$ , because outside  $C$  the value is  $+\infty$ , which can never be smaller than any finite value.

Formally:

$$
\inf_{x\in\mathbb{R}^n} F(x) = \inf\left(\;\inf_{x\in C}F(x),\;\inf_{x\notin C}F(x)\;\right).
$$

But:

*   On  $C$ ,  $F(x)=f(x)$ , so  $\inf_{x\in C}F(x)=\inf_{x\in C}f(x)$ .
*   On  $\mathbb{R}^n\setminus C$ ,  $F(x)=+\infty$  everywhere, so  $\inf_{x\notin C}F(x)=+\infty$ .

Therefore:

$$
\inf_{x\in\mathbb{R}^n}F(x)=\inf\left(\inf_{x\in C}f(x), +\infty\right)=\inf_{x\in C}f(x).
$$

∎

This proof is simple but absolutely foundational: it justifies the modern “modeling” viewpoint used by CVX/CVXPY and by convex duality theory.

* * *

### 0.3.10 Equality constraints: why they are dangerous (preview, but crucial)

A constraint  $f(x)=0$  defines a set

$$
\{x : f(x)=0\}.
$$

Even if  $f$  is convex, the set  $\{x: f(x)=0\}$  is usually **not convex** unless  $f$  is affine. (We will prove this later, but you should already feel the warning.)

This is why convex optimization permits:

*   convex inequalities  $f_i(x)\le 0$ 
*   affine equalities  $Ax=b$ 

The distinction is set-theoretic: equalities slice level sets, which are typically nonconvex.

* * *

### 0.3.11 Domain and feasibility: two sources of “allowedness”

In a typical convex optimization problem, you have:

*   explicit constraints:  $x\in C$ 
*   implicit domain constraints:  $x\in \mathrm{dom}\,f$ 

Example:

$$
\min_x -\sum_{i=1}^n \log x_i \quad \text{s.t. } Ax=b.
$$

Here:

*   the explicit constraint set is  $\{x:Ax=b\}$ 
*   but also the objective requires  $x_i>0$  for all  $i$  (otherwise  $\log x_i$  undefined / treated as  $+\infty$ )

So the true feasible set is:

$$
\{x:Ax=b\} \cap \{x:x\succ 0\}.
$$

This is why you must _never_ ignore domain: the function itself defines a set.

* * *

### 0.3.12 Composition (very early preview): functions create new functions only when types match

Suppose:

$$
g:D\to Y,\qquad f:Y\to Z.
$$

Then the composition  $f\circ g$  is defined by:

$$
(f\circ g)(x) = f(g(x)).
$$

But this is only legal if:

*    $g(x)\in Y$  for all  $x\in D$ , and
*    $g(x)$  lies inside the domain of  $f$ .

In optimization, almost all modeling is composition, and almost all modeling bugs are “domain mismatch” bugs.

Example:

*    $f(u)=\log u$  requires  $u>0$ .
*   If  $g(x)=c^\top x + d$ , then  $\log(c^\top x + d)$  is only defined on:
    
$$
\{x: c^\top x + d > 0\}.
$$

So domain constraints propagate through composition.

* * *

### 0.3.13 What you must be able to do cold after 0.3

You should be able to do these instantly, without hesitation:

1.  Given an expression, state its **natural domain** (where it is defined).
2.  Given a constrained problem, rewrite it using **indicator functions**.
3.  Compute  $\mathrm{dom}\,f$  (effective domain) for extended-valued  $f$ .
4.  Translate constraints into **preimages** under functions.
5.  Check whether a composition  $f(g(x))$  is even _legal_ by domain/type checking.

If you can do these, later convexity and modeling becomes disciplined instead of mystical.

* * *

### Roadmap checkpoint

We now have the three Phase-0 primitives:

*   **Objects** (0.1)
*   **Sets** (0.2)
*   **Functions (with domains and extended values)** (0.3)

Next is **0.4 Inner products** (dot product, geometry, projections intuition), which becomes the bridge into norms, hyperplanes, gradients, and cones.

## Response:
Below is a **fully rewritten, expanded, and deepened version of 0.3**, intended to be _maximally explicit_, _zero-to-hero_, and _logically airtight_. This **replaces** the previous 0.3 entirely and becomes the canonical reference we will rely on later. Nothing is assumed; everything is unpacked.

* * *

**0.3 — Functions**
===================

_(maps, domains, extended values, feasibility encoded as infinity, and why “domain” is law, not metadata)_

If 0.1 taught us **what objects exist**, and 0.2 taught us **which objects are allowed**, then 0.3 answers the next foundational question:

> **How do we assign numerical meaning to allowed objects, and how do we enforce “not allowed” rigorously?**

Optimization is impossible without functions.  
But **most mathematical mistakes in optimization are not algebraic — they are functional**: undefined values, illegal compositions, ignored domains, and silent infeasibility.

This section is deliberately long and repetitive because _this is where rigor is usually lost_.

* * *

0.3.0 What a function actually is (formal, not intuitive)
---------------------------------------------------------

A **function** is not a formula.  
A function is a **triple**:

$$
\boxed{f = (\text{domain}, \text{codomain}, \text{rule})}
$$

Formally, a function  $f$  consists of:

1.  A **domain**  $D$  (a set of allowed inputs),
2.  A **codomain**  $Y$  (the set where outputs live),
3.  A rule assigning **exactly one** element of  $Y$  to each element of  $D$ .

We write:

$$
f : D \to Y, \qquad x \mapsto f(x).
$$

Two absolute requirements:

*   **Total on the domain**:  
    For every  $x \in D$ , the value  $f(x)$  exists.
*   **Single-valued**:  
    Each  $x \in D$  maps to one and only one output.

If either condition fails, you do **not** have a function.

* * *

0.3.1 Expressions vs functions vs values (the silent source of confusion)
-------------------------------------------------------------------------

These three are distinct, and conflating them breaks rigor:

1.  **Expression**: a symbolic recipe  
    Examples:  
     $x^2$ ,  $\log x$ ,  $\|Ax-b\|_2$ 
2.  **Function**: an abstract mapping with a domain  
    Example:  
     $f : \mathbb{R} \to \mathbb{R},\ f(x)=x^2$ 
3.  **Value**: the result of evaluation  
    Example:  
     $f(3)=9$ 

A formula does **not** define a function until you specify the domain.

Example:

> “ $f(x)=\log x$ ” is _not_ a function until you say  
>  $f:(0,\infty)\to\mathbb{R}$ .

Later, when we talk about convexity, differentiability, or minimization, all of those statements are **false or meaningless** unless the function is first well-defined.

* * *

0.3.2 Domains are not optional — they are part of the definition
----------------------------------------------------------------

This cannot be overstated:

> **A function without a domain is not a function.**

### Example 1: Reciprocal

Expression:

$$
\frac{1}{x}
$$

To define a function, we must write:

$$
f:\mathbb{R}\setminus\{0\}\to\mathbb{R},\quad f(x)=\frac{1}{x}.
$$

If you later write:

*   “minimize  $1/x$  over  $\mathbb{R}$ ”  
    you have already committed a logical error: the function is not defined at  $x=0$ .

### Example 2: Logarithm

$$
f:(0,\infty)\to\mathbb{R},\quad f(x)=\log x.
$$

The condition  $x>0$  is **not a constraint you may drop**.  
It is a **logical prerequisite** for the function to exist.

In convex optimization, ignoring domain constraints is the most common reason proofs fail silently.

* * *

0.3.3 Scalar-valued vs vector-valued vs matrix-valued functions
---------------------------------------------------------------

Functions are categorized by what they output.

### Scalar-valued functions

$$
f:\mathbb{R}^n \to \mathbb{R}
$$

These are used for:

*   objectives (what we minimize),
*   scalar constraints ( $f(x)\le 0$ ).

### Vector-valued functions

$$
g:\mathbb{R}^n \to \mathbb{R}^m
$$

These are used for:

*   systems of constraints,
*   residual vectors,
*   mappings into cones.

### Matrix-valued functions

$$
F:\mathbb{R}^n \to \mathbb{R}^{p\times q}
$$

These appear in:

*   semidefinite constraints,
*   matrix inequalities.

**Optimization problems minimize scalars**, but feasibility is often expressed through vector- or matrix-valued functions.

You must _always_ know which space the output lives in — this determines which inequalities even make sense.

* * *

0.3.4 The graph of a function (functions as sets in disguise)
-------------------------------------------------------------

Given a scalar-valued function  $f:D\to\mathbb{R}$ , define its **graph** as:

$$
\mathrm{graph}(f) := \{(x,t)\in D\times\mathbb{R} : t=f(x)\}.
$$

This turns a function into a **set in one higher dimension**.

Why this matters:

*   Equalities  $t=f(x)$  are set membership statements.
*   Convexity of functions will later be defined via **convexity of certain sets** derived from the graph.
*   Constraints often become statements about subsets of the graph.

For vector-valued  $g:D\to\mathbb{R}^m$ , the graph is:

$$
\{(x,y): y=g(x)\}.
$$

The graph viewpoint is what allows us to reason geometrically about functions.

* * *

0.3.5 Preimages (pullbacks): the true meaning of constraints
------------------------------------------------------------

This is one of the most important constructions in all of optimization.

Let:

*    $g:D\to Y$  be a function,
*    $S\subseteq Y$  be a set of “acceptable outputs”.

The **preimage** of  $S$  under  $g$  is:

$$
g^{-1}(S) := \{x\in D : g(x)\in S\}.
$$

### Interpretation

A constraint is **never** just “ $g(x)\le 0$ ”.  
It is always:

> “The output of  $g$  must lie in an allowed set.”

Examples:

1.  Scalar inequality
    $$
    g(x)\le 0 \quad \Longleftrightarrow \quad g(x)\in(-\infty,0]
    $$
    Feasible set:
    $$
    g^{-1}((-\infty,0]).
    $$
2.  Vector inequality
    $$
    g(x)\preceq 0 \quad \Longleftrightarrow \quad g(x)\in\mathbb{R}^m_-
    $$
3.  Norm constraint
    $$
    \|Ax-b\|_2 \le t \quad \Longleftrightarrow \quad (Ax-b,t)\in \text{SOC}.
    $$

This preimage viewpoint is the engine behind all convexity-preserving rules later. But even now, it is the _correct logical meaning_ of constraints.

* * *

0.3.6 Extended-real-valued functions: allowing  $+\infty$ 
----------------------------------------------------------

In convex optimization, we deliberately enlarge the codomain to:

$$
\mathbb{R}\cup\{+\infty\}.
$$

An **extended-real-valued function** is:

$$
f:\mathbb{R}^n \to \mathbb{R}\cup\{+\infty\}.
$$

### Why introduce  $+\infty$ ?

Because it allows us to encode **hard constraints** directly into the function.

Interpretation:

*    $f(x)\in\mathbb{R}$ :  $x$  is allowed.
*    $f(x)=+\infty$ :  $x$  is forbidden.

This is not a numerical trick — it is a logical encoding.

We almost never allow  $-\infty$  because:

*   minimization becomes meaningless,
*   infima collapse.

* * *

0.3.7 Effective domain (the _real_ domain that matters)
-------------------------------------------------------

For an extended-real-valued function  $f$ , define:

$$
\boxed{\mathrm{dom}\,f := \{x\in\mathbb{R}^n : f(x)<+\infty\}}
$$

This is called the **effective domain**.

Key principle:

> **You may only optimize over  $\mathrm{dom}\,f$ .**  
> Everything outside is automatically excluded.

Even if the variable symbol says  $x\in\mathbb{R}^n$ , the function itself imposes a hidden feasibility set.

* * *

0.3.8 Indicator functions: turning sets into functions
------------------------------------------------------

Given a set  $C\subseteq\mathbb{R}^n$ , define its **indicator function**:

$$
\delta_C(x)= \begin{cases} 0 & x\in C\\ +\infty & x\notin C. \end{cases}
$$

Properties:

*    $\mathrm{dom}\,\delta_C = C$ 
*    $\delta_C$  contains _only_ feasibility information

This allows us to unify constraints and objectives.

* * *

0.3.9 Proof: constrained problems are unconstrained problems with indicators
----------------------------------------------------------------------------

Consider the constrained problem:

$$
\min_{x\in C} f(x).
$$

Define:

$$
F(x):=f(x)+\delta_C(x).
$$

**Claim**

$$
\inf_{x\in C} f(x) = \inf_{x\in\mathbb{R}^n} F(x).
$$

**Proof (fully explicit).**

Split  $\mathbb{R}^n$  into two disjoint parts:

*   If  $x\in C$ :  
     $\delta_C(x)=0\Rightarrow F(x)=f(x)$ .
*   If  $x\notin C$ :  
     $\delta_C(x)=+\infty\Rightarrow F(x)=+\infty$ .

Thus:

$$
\inf_{x\in\mathbb{R}^n}F(x) = \min\left\{ \inf_{x\in C} f(x),\; \inf_{x\notin C}(+\infty) \right\} = \inf_{x\in C}f(x).
$$

∎

This identity is the foundation of:

*   convex duality,
*   Lagrangians,
*   modern modeling languages.

* * *

0.3.10 Equality constraints and why they are dangerous
------------------------------------------------------

A constraint:

$$
h(x)=0
$$

defines the set:

$$
\{x : h(x)=0\}.
$$

Even if  $h$  is convex, this set is **almost never convex** unless  $h$  is affine.

This is why convex optimization allows:

*   convex inequalities,
*   affine equalities.

This is not convention. It is set geometry.

* * *

0.3.11 Domain constraints vs explicit constraints
-------------------------------------------------

In practice, feasibility comes from **two sources**:

1.  Explicit constraints:  $x\in C$ 
2.  Implicit domain constraints:  $x\in\mathrm{dom}\,f$ 

Example:

$$
\min_x -\sum_i \log x_i \quad \text{s.t. } Ax=b.
$$

The true feasible set is:

$$
\{x:Ax=b\} \cap \{x:x_i>0\ \forall i\}.
$$

The second set comes _only_ from the domain of the function.

Ignoring this distinction leads to invalid KKT conditions and broken proofs.

* * *

0.3.12 Composition of functions (legality first, properties later)
------------------------------------------------------------------

If:

$$
g:D\to Y,\quad f:Y\to Z,
$$

then the composition  $f\circ g$  is defined by:

$$
(f\circ g)(x)=f(g(x)).
$$

But this is **only legal** if:

*    $g(x)\in\mathrm{dom}\,f$  for all  $x\in D$ .

Example:

*    $f(u)=\log u$  requires  $u>0$ .
*    $g(x)=c^\top x+d$ .
*   Then  $f(g(x))$  is defined only on:
    
$$
\{x:c^\top x+d>0\}.
$$

Later, convexity of compositions depends entirely on this legality step.

* * *

0.3.13 What you must be able to do instantly after 0.3
------------------------------------------------------

You should now be able to:

*   State the **true domain** of any function.
*   Convert constraints into **preimages**.
*   Encode constraints using **indicator functions**.
*   Identify the **effective domain**.
*   Check whether a composition is even _defined_.

If you cannot do these, convexity theory will look like magic instead of logic.

* * *

### Roadmap checkpoint

We have now completed Phase 0’s logical foundation:

*   **0.1** Objects
*   **0.2** Sets
*   **0.3** Functions and domains

Next: **0.4 — Inner products**  
This is where geometry, angles, projections, hyperplanes, gradients, and cones begin to emerge.

## Response:
**0.4 — Inner Products (the geometry hiding inside algebra)**
-------------------------------------------------------------

This subsection looks innocent. It is not.  
Inner products are the _silent machinery_ behind angles, orthogonality, projections, gradients, dual norms, PSD matrices, and eventually KKT conditions and duality. If you understand inner products deeply, convex optimization becomes geometry instead of symbol pushing.

We proceed from absolute zero.

* * *

### **0.4.1 What an inner product actually is (definition, not vibes)**

An **inner product** on a real vector space  $V$  is a function

$$
\langle \cdot,\cdot\rangle : V \times V \to \mathbb{R}
$$

that assigns a real number to each ordered pair of vectors and satisfies **three axioms**.

Let  $x,y,z \in V$ , and  $\alpha \in \mathbb{R}$ .

1.  **Linearity in the first argument**
    
$$
\langle \alpha x + y, z\rangle = \alpha\langle x,z\rangle + \langle y,z\rangle
$$
2.  **Symmetry**
    
$$
\langle x,y\rangle = \langle y,x\rangle
$$
3.  **Positive definiteness**
    
$$
\langle x,x\rangle \ge 0 \quad \text{and} \quad \langle x,x\rangle = 0 \iff x=0
$$

That is the _entire definition_. Everything else follows.

Important clarifications:

*   Inner products are **not** arbitrary bilinear forms.
*   Positive definiteness is the key property that turns algebra into geometry.
*   Without positive definiteness, angles and lengths collapse.

* * *

### **0.4.2 The standard inner product on  $\mathbb{R}^n$ **

On  $\mathbb{R}^n$ , the **standard (Euclidean) inner product** is

$$
\langle x,y\rangle := x^\top y = \sum_{i=1}^n x_i y_i
$$

This choice is not cosmetic. It encodes:

*   Coordinate-wise interaction
*   Euclidean geometry
*   Orthogonality of axes
*   Standard notion of angle and length

We will later _change_ inner products to encode different geometries. For now, this is home base.

* * *

### **0.4.3 Why inner products matter: geometry is encoded here**

From the three axioms alone, we get:

#### **(a) Length (norm)**

Define

$$
\|x\| := \sqrt{\langle x,x\rangle}
$$

This is **not a definition pulled from nowhere**. It is forced by positive definiteness.

We will later prove this satisfies all norm axioms.

#### **(b) Angles**

For nonzero vectors,

$$
\cos\theta = \frac{\langle x,y\rangle}{\|x\|\|y\|}
$$

This formula is _not assumed_. It is derived from inner-product geometry.

#### **(c) Orthogonality**

$$
x \perp y \iff \langle x,y\rangle = 0
$$

Orthogonality is **defined**, not intuitive.  
Everything about projections, residuals, KKT stationarity, and dual feasibility rests on this.

* * *

### **0.4.4 Cauchy–Schwarz inequality (the keystone)**

> **Theorem (Cauchy–Schwarz)**  
> For any  $x,y \in V$ ,

$$
|\langle x,y\rangle| \le \|x\|\|y\|
$$

with equality iff  $x$  and  $y$  are linearly dependent.

#### **Proof (from first principles, no shortcuts)**

Consider the function

$$
f(t) = \langle x - ty, x - ty\rangle
$$

By positive definiteness,

$$
f(t) \ge 0 \quad \text{for all } t \in \mathbb{R}
$$

Expand:

$$
f(t) = \langle x,x\rangle - 2t\langle x,y\rangle + t^2\langle y,y\rangle
$$

This is a quadratic polynomial in  $t$  that is **never negative**.

A quadratic  $at^2+bt+c \ge 0$  for all  $t$  implies its discriminant is nonpositive:

$$
b^2 - 4ac \le 0
$$

Apply:

$$
( -2\langle x,y\rangle )^2 - 4\langle y,y\rangle \langle x,x\rangle \le 0
$$

Simplify:

$$
\langle x,y\rangle^2 \le \langle x,x\rangle \langle y,y\rangle
$$

Taking square roots gives the result.

This inequality is _structural_. You will see it everywhere:

*   dual norms
*   robust optimization
*   projection proofs
*   Lipschitz bounds

* * *

### **0.4.5 Inner products induce norms (and why this matters)**

Given an inner product, define

$$
\|x\| := \sqrt{\langle x,x\rangle}
$$

We now **prove** this is a norm.

1.  **Nonnegativity**: immediate from positive definiteness.
2.  **Definiteness**:  $\|x\|=0 \iff x=0$ .
3.  **Homogeneity**:
    
$$
\|\alpha x\|^2 = \langle \alpha x,\alpha x\rangle = \alpha^2\langle x,x\rangle \Rightarrow \|\alpha x\| = |\alpha|\|x\|
$$
4.  **Triangle inequality** (this is the nontrivial one):

Compute:

$$
\|x+y\|^2 = \langle x+y,x+y\rangle = \|x\|^2 + 2\langle x,y\rangle + \|y\|^2
$$

Apply Cauchy–Schwarz:

$$
2\langle x,y\rangle \le 2\|x\|\|y\|
$$

Thus:

$$
\|x+y\|^2 \le (\|x\|+\|y\|)^2 \Rightarrow \|x+y\| \le \|x\|+\|y\|
$$

So inner products automatically generate normed spaces.

This is why convex optimization loves inner products: they control _distance_, _angles_, and _growth_ simultaneously.

* * *

### **0.4.6 General inner products: weighted geometry**

Not all inner products are standard.

Let  $P \in \mathbb{R}^{n\times n}$  be **symmetric positive definite** ( $P \succ 0$ ). Define

$$
\langle x,y\rangle_P := x^\top P y
$$

This is an inner product.

**Why?**

*   Linearity: inherited from matrix multiplication
*   Symmetry:  $P=P^\top$ 
*   Positive definiteness:  $x^\top P x > 0$  for  $x\neq 0$ 

This induces the norm

$$
\|x\|_P = \sqrt{x^\top P x}
$$

Geometric meaning:

*   Unit balls become ellipsoids
*   Distances are stretched along eigen-directions of  $P$ 
*   Quadratic objectives are distances in disguised geometry

This will reappear when:

*   proving convexity of quadratic forms
*   understanding trust regions
*   interpreting Newton steps

* * *

### **0.4.7 Projections: the workhorse of convex analysis**

Let  $C \subset \mathbb{R}^n$  be a **closed convex set**.

The **projection** of  $y$  onto  $C$  is

$$
\Pi_C(y) := \arg\min_{x\in C} \|x-y\|^2
$$

This definition already uses:

*   inner products (inside the norm)
*   convexity (uniqueness!)
*   geometry (closest point)

#### **Projection theorem (key fact)**

Let  $x^* = \Pi_C(y)$ . Then

$$
\langle y-x^*, z-x^* \rangle \le 0 \quad \forall z\in C
$$

Interpretation:

*   The residual  $y-x^*$  forms an obtuse angle with every feasible direction.
*   This is the geometric ancestor of KKT stationarity.
*   Separation theorems and duality are hiding here.

This result will later:

*   produce supporting hyperplanes
*   prove dual feasibility
*   explain complementary slackness geometrically

* * *

### **0.4.8 Inner products and linear functionals**

Every vector  $a$  defines a linear functional:

$$
x \mapsto \langle a,x\rangle
$$

In  $\mathbb{R}^n$ , **every linear functional arises this way**.

This fact is crucial:

*   Gradients are vectors because objectives are linearized via inner products.
*   Dual variables live in the same space because constraints are measured via inner products.
*   Separation hyperplanes are defined by inner products.

Convex optimization is not “functions and constraints”.  
It is **inner products comparing vectors**.

* * *

### **0.4.9 Why this section matters later (explicit preview)**

Everything below depends on this subsection:

*   Convexity proofs via first-order conditions
*   PSD matrices and quadratic forms
*   Dual norms and robust optimization
*   Projections and feasibility
*   Lagrangians and KKT conditions
*   Duality as geometric separation

If inner products feel mechanical, future sections will feel magical.  
If inner products feel geometric, future sections will feel inevitable.

* * *

### **Checkpoint (do not skip)**

You should now be able to:

*   State the inner product axioms precisely
*   Prove Cauchy–Schwarz from scratch
*   Derive norms from inner products
*   Explain orthogonality geometrically
*   Interpret quadratic forms as squared norms
*   See projections as geometric optimality conditions

* * *

**Next subsection (0.5): Affine vs linear mappings — why “+b” changes everything.**

We continue exactly at this level.

3/3

## Response:
We proceed **exactly along the roadmap**.

* * *

**0.4 Inner Products and Norms (the geometry engine of optimization)**
----------------------------------------------------------------------

This subsection builds the _measurement layer_ of convex optimization.  
Up to now, we have objects (sets, functions) and domains. Now we answer the question:

**How do we measure direction, length, angle, error, and proximity?**

Everything later—gradients, projections, optimality, cones, SOC constraints, robustness—rests on this layer. Nothing here is cosmetic. Every definition will reappear later wearing a different hat.

I will proceed from first principles, prove everything that matters, and explain why each concept exists.

* * *

### **0.4.1 Inner products: measuring alignment**

#### **Definition (Inner product)**

An **inner product** on a real vector space  $V$  (we will use  $V = \mathbb{R}^n$ ) is a map

$$
\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}
$$

satisfying, for all  $x,y,z \in V$  and all scalars  $\alpha \in \mathbb{R}$ :

1.  **Bilinearity**
    $$
    \langle \alpha x + y, z \rangle = \alpha \langle x,z\rangle + \langle y,z\rangle, \quad \langle x, \alpha y + z \rangle = \alpha \langle x,y\rangle + \langle x,z\rangle
    $$
2.  **Symmetry**
    $$
    \langle x,y\rangle = \langle y,x\rangle
    $$
3.  **Positive definiteness**
    $$
    \langle x,x\rangle \ge 0, \quad \langle x,x\rangle = 0 \iff x = 0
    $$

* * *

#### **Standard inner product in  $\mathbb{R}^n$ **

The default inner product is the **dot product**:

$$
\boxed{\langle x,y\rangle = x^\top y = \sum_{i=1}^n x_i y_i}
$$

This definition is not arbitrary. It is chosen because:

• it is bilinear  
• it induces Euclidean geometry  
• it interacts perfectly with linear maps and matrices

Every “angle,” “projection,” and “orthogonality” statement you know comes from this definition.

* * *

### **0.4.2 Geometry induced by the inner product**

Once an inner product exists, geometry appears automatically.

* * *

#### **Length (norm induced by an inner product)**

Define

$$
\|x\|_2 := \sqrt{\langle x,x\rangle}
$$

This is called the **Euclidean norm**.

We will prove shortly that this satisfies all norm axioms. For now, interpret:

•  $\langle x,x\rangle$  measures _squared length_  
• the square root restores physical length units

* * *

#### **Angle and cosine formula**

For nonzero vectors  $x,y$ , define the angle  $\theta$  between them by:

$$
\cos\theta := \frac{\langle x,y\rangle}{\|x\|_2\|y\|_2}
$$

This formula is _derived_, not assumed. It follows from the law of cosines once inner products exist.

Interpretation:

•  $\langle x,y\rangle > 0$ : vectors point roughly the same way  
•  $\langle x,y\rangle = 0$ : orthogonal (perpendicular)  
•  $\langle x,y\rangle < 0$ : opposing directions

* * *

### **0.4.3 Cauchy–Schwarz inequality (the master inequality)**

This is the most important inequality in convex optimization.

#### **Theorem (Cauchy–Schwarz)**

For all  $x,y \in \mathbb{R}^n$ ,

$$
\boxed{|\langle x,y\rangle| \le \|x\|_2 \|y\|_2}
$$

* * *

#### **Proof (from first principles)**

If  $y = 0$ , the inequality is trivial. Assume  $y \neq 0$ .

Consider the function of a scalar  $t$ :

$$
f(t) := \|x - t y\|_2^2
$$

By definition of norm:

$$
f(t) = \langle x - t y, x - t y \rangle = \langle x,x\rangle - 2t\langle x,y\rangle + t^2 \langle y,y\rangle
$$

This is a quadratic polynomial in  $t$  with leading coefficient  $\langle y,y\rangle > 0$ .

Since norms are nonnegative:

$$
f(t) \ge 0 \quad \text{for all } t \in \mathbb{R}
$$

A quadratic  $at^2 + bt + c \ge 0$  for all  $t$  must have nonpositive discriminant:

$$
b^2 - 4ac \le 0
$$

Here:

$$
b = -2\langle x,y\rangle, \quad a = \langle y,y\rangle, \quad c = \langle x,x\rangle
$$

So:

$$
4\langle x,y\rangle^2 \le 4 \langle x,x\rangle \langle y,y\rangle
$$

Divide by 4 and take square roots:

$$
|\langle x,y\rangle| \le \|x\|_2 \|y\|_2
$$

□

* * *

#### **Why this inequality matters**

Every one of the following depends on Cauchy–Schwarz:

• triangle inequality  
• norm convexity  
• Lipschitz bounds  
• dual norms  
• robust optimization  
• SOC constraints

You will use this inequality constantly, often without noticing.

* * *

### **0.4.4 Norms: measuring size**

We now abstract the idea of “length.”

#### **Definition (Norm)**

A function  $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}$  is a **norm** if for all  $x,y$  and all scalars  $\alpha$ :

1.  **Nonnegativity**
    $$
    \|x\| \ge 0
    $$
2.  **Definiteness**
    $$
    \|x\| = 0 \iff x = 0
    $$
3.  **Positive homogeneity**
    $$
    \|\alpha x\| = |\alpha| \|x\|
    $$
4.  **Triangle inequality**
    $$
    \|x + y\| \le \|x\| + \|y\|
    $$

A norm is a _measurement rule_. Different norms measure “size” differently.

* * *

### **0.4.5 The Euclidean norm is a norm**

We now justify that  $\|x\|_2 = \sqrt{x^\top x}$  is indeed a norm.

• Nonnegativity and definiteness follow from positive definiteness of the inner product.

• Homogeneity:

$$
\|\alpha x\|_2^2 = (\alpha x)^\top(\alpha x) = \alpha^2 x^\top x \Rightarrow \|\alpha x\|_2 = |\alpha|\|x\|_2
$$

• Triangle inequality (key step):

We compute:

$$
\|x+y\|_2^2 = \|x\|_2^2 + 2\langle x,y\rangle + \|y\|_2^2
$$

Using Cauchy–Schwarz:

$$
2\langle x,y\rangle \le 2\|x\|_2\|y\|_2
$$

So:

$$
\|x+y\|_2^2 \le (\|x\|_2 + \|y\|_2)^2
$$

Taking square roots:

$$
\|x+y\|_2 \le \|x\|_2 + \|y\|_2
$$

□

* * *

### **0.4.6 Common norms in optimization**

These appear everywhere later.

* * *

#### **ℓ₂ norm (Euclidean)**

$$
\|x\|_2 = \sqrt{\sum x_i^2}
$$

• rotation-invariant  
• leads to SOC constraints  
• natural for least squares

* * *

#### **ℓ₁ norm**

$$
\|x\|_1 = \sum |x_i|
$$

• promotes sparsity  
• used in LASSO, fuel minimization  
• LP-representable

* * *

#### **ℓ∞ norm**

$$
\|x\|_\infty = \max_i |x_i|
$$

• worst-case control  
• LP-representable  
• robust optimization favorite

* * *

### **0.4.7 Norm balls and geometry**

Given a norm  $\|\cdot\|$ , define the **unit ball**:

$$
B = \{x : \|x\| \le 1\}
$$

* * *

#### **Theorem: norm balls are convex**

Let  $x,y \in B$  and  $\theta \in [0,1]$ .

By homogeneity and triangle inequality:

$$
\|\theta x + (1-\theta)y\| \le \theta\|x\| + (1-\theta)\|y\| \le \theta + (1-\theta) = 1
$$

So  $\theta x + (1-\theta)y \in B$ .

□

This single fact explains **why norm constraints are convex constraints**.

* * *

### **0.4.8 Dual norms (preview, but crucial)**

Given a norm  $\|\cdot\|$ , define its **dual norm**:

$$
\|y\|_* := \sup_{\|x\|\le 1} x^\top y
$$

Interpretation:

• “largest projection of  $y$  onto unit vectors”  
• worst-case alignment

Examples:

$$
(\ell_2)^* = \ell_2, \quad (\ell_1)^* = \ell_\infty, \quad (\ell_\infty)^* = \ell_1
$$

This concept will later power:

• robust constraints  
• Hölder inequalities  
• SOC reformulations

* * *

### **0.4.9 Why this section matters (foreshadowing)**

From just inner products and norms, we will later derive:

• gradients as steepest ascent directions  
• projections onto convex sets  
• SOC constraints as norm bounds  
• robustness as dual norms  
• Schur complements  
• optimality certificates

This is not background.  
This is the engine.

* * *

### **Checkpoint (you must be fluent before proceeding)**

You should be able to:

• derive Cauchy–Schwarz from scratch  
• prove the triangle inequality  
• recognize ℓ₁, ℓ₂, ℓ∞ geometry  
• explain why norm balls are convex  
• explain dual norms intuitively

* * *

**Next subsection (only when you’re ready):**  
**0.5 Affine vs linear mappings** — why optimization only cares about affine structure.

We will continue with the same gold-standard depth.

2/2

## Response:
### **0.5 — Affine vs. Linear Mappings (the structural backbone of optimization)**

This subsection looks innocent. It is not.  
If you do not fully internalize the distinction between **linear** and **affine** mappings, convex optimization will feel like a bag of arbitrary rules instead of a coherent theory. Almost every theorem later—convexity preservation, epigraph tricks, feasible set geometry, duality—quietly relies on this distinction.

We proceed from absolute first principles.

* * *

0.5.1 What is a mapping?
------------------------

A **mapping** (or function) is a rule that assigns to each input exactly one output.

Formally, a mapping

$$
f : \mathbb{R}^n \to \mathbb{R}^m
$$

assigns to each vector  $x \in \mathbb{R}^n$  a vector  $f(x) \in \mathbb{R}^m$ .

In optimization, mappings appear everywhere:

*   objectives:  $x \mapsto f_0(x)$ 
*   constraints:  $x \mapsto Ax - b$ 
*   transformations of variables
*   preimages of sets (feasible regions)

But not all mappings behave equally well with respect to geometry. Two special classes dominate convex optimization: **linear** and **affine** mappings.

* * *

0.5.2 Linear mappings: structure-preserving maps through the origin
-------------------------------------------------------------------

### Definition (Linear mapping)

A mapping

$$
L : \mathbb{R}^n \to \mathbb{R}^m
$$

is **linear** if it satisfies **both** of the following properties for all  $x,y \in \mathbb{R}^n$  and all scalars  $\alpha,\beta \in \mathbb{R}$ :

1.  **Additivity**
    
$$
L(x+y) = L(x) + L(y)
$$
2.  **Homogeneity**
    
$$
L(\alpha x) = \alpha L(x)
$$

Equivalently (and more compactly),

$$
L(\alpha x + \beta y) = \alpha L(x) + \beta L(y)
$$

* * *

### Matrix representation theorem

Every linear mapping  $L : \mathbb{R}^n \to \mathbb{R}^m$  can be written uniquely as

$$
L(x) = Ax
$$

for some matrix  $A \in \mathbb{R}^{m \times n}$ .

**Why this matters:**  
When you see  $Ax$  in optimization, you are looking at a linear mapping. No exceptions.

* * *

### Consequences of linearity

From the definition alone, several deep geometric facts follow:

1.  **Origin preservation**
    
$$
L(0) = 0
$$

Proof:

$$
L(0) = L(0 + 0) = L(0) + L(0) \Rightarrow L(0)=0
$$
2.  **Subspace mapping**  
    If  $S \subseteq \mathbb{R}^n$  is a linear subspace, then  $L(S)$  is also a linear subspace.
3.  **Convexity preservation**  
    If  $C$  is convex, then  $L(C)$  is convex.

Proof sketch:  
For any  $x,y \in C$  and  $\theta \in [0,1]$ ,

$$
L(\theta x + (1-\theta)y) = \theta L(x) + (1-\theta)L(y) \in L(C)
$$
4.  **Lines through the origin stay lines through the origin**

This “through the origin” part is the key limitation of linear maps.

* * *

0.5.3 Why linear maps are not enough
------------------------------------

Most sets in optimization **do not pass through the origin**.

Examples:

*   feasible set:  $Ax = b$ 
*   halfspace:  $a^\top x \le c$ 
*   affine hulls of points
*   translated norm balls

Linear maps alone cannot describe these structures. We need a slight generalization.

* * *

0.5.4 Affine mappings: linear structure + translation
-----------------------------------------------------

### Definition (Affine mapping)

A mapping

$$
f : \mathbb{R}^n \to \mathbb{R}^m
$$

is **affine** if it can be written as

$$
\boxed{f(x) = Ax + b}
$$

for some matrix  $A \in \mathbb{R}^{m \times n}$  and vector  $b \in \mathbb{R}^m$ .

Interpretation:

*    $Ax$ : linear transformation (rotation, scaling, projection, shear)
*    $+ b$ : translation (shift in space)

Every affine map is a **linear map followed by a translation**.

* * *

### Characterization via combinations

An equivalent and extremely important characterization:

> A mapping  $f$  is affine **if and only if** it preserves affine combinations.

That is, for all  $x,y \in \mathbb{R}^n$  and all  $\theta \in \mathbb{R}$ ,

$$
f(\theta x + (1-\theta)y) = \theta f(x) + (1-\theta)f(y)
$$

Compare carefully:

*   linear maps preserve **linear combinations**
*   affine maps preserve **affine combinations**
*   convex maps preserve **convex combinations** (later)

This hierarchy is not accidental.

* * *

### Proof of equivalence

**( $\Rightarrow$ )**  
Assume  $f(x)=Ax+b$ . Then:

$$
\begin{aligned} f(\theta x + (1-\theta)y) &= A(\theta x + (1-\theta)y) + b \\ &= \theta Ax + (1-\theta)Ay + b \\ &= \theta(Ax+b) + (1-\theta)(Ay+b) \\ &= \theta f(x) + (1-\theta)f(y) \end{aligned}
$$

**( $\Leftarrow$ )**  
Assume affine-combination preservation.  
Define  $b := f(0)$ .  
Define  $L(x) := f(x) - b$ .

Then:

$$
L(\theta x + (1-\theta)y) = \theta L(x) + (1-\theta)L(y)
$$

and in particular:

$$
L(\alpha x) = \alpha L(x)
$$

so  $L$  is linear, hence  $L(x)=Ax$ .  
Thus  $f(x)=Ax+b$ .

* * *

0.5.5 Geometry of affine mappings
---------------------------------

Affine mappings have three fundamental geometric properties:

### 1\. Lines map to lines

Not necessarily through the origin.

### 2\. Line segments map to line segments

This is why convexity behaves well.

### 3\. Parallelism is preserved

Affine maps do not bend space; they only stretch, rotate, shear, and translate.

This makes affine maps the **natural coordinate transformations** of convex geometry.

* * *

0.5.6 Why affine structure dominates convex optimization
--------------------------------------------------------

This is the key philosophical point.

Convex optimization is built on three invariances:

1.  **Convexity invariance**  
    If  $C$  is convex, then:
    *    $Ax + b \in C$  is convex
*    $A^{-1}(C)$  (preimage) is convex
    2.  **Feasibility invariance**  
    Affine constraints preserve feasibility geometry.
3.  **Optimality invariance**  
    Affine reparameterizations do not change the essential difficulty of a problem.

Because of this, **convex optimization problems are defined using affine equalities and convex inequalities**—never nonlinear equalities.

* * *

0.5.7 Linear vs affine constraints (crucial distinction)
--------------------------------------------------------

Compare:

### Linear equality

$$
Ax = 0
$$

Defines a **subspace** (passes through origin).

### Affine equality

$$
Ax = b
$$

Defines an **affine set** (translated subspace).

Both are allowed in convex optimization.

* * *

### Why nonlinear equalities break convexity

Constraint:

$$
x^2 = 1
$$

Feasible set:

$$
\{-1, +1\}
$$

Not convex.  
This is why convex problems allow **only affine equalities**.

* * *

0.5.8 Affine preimages: how constraints define sets
---------------------------------------------------

Given an affine map  $f(x)=Ax+b$  and a set  $C$ ,

The **preimage**

$$
f^{-1}(C) = \{x \mid Ax+b \in C\}
$$

Key theorem:

> If  $C$  is convex, then  $f^{-1}(C)$  is convex.

This single fact explains why:

*    $Ax=b$  is convex
*    $Ax \le b$  is convex
*    $\|Ax-b\| \le t$  is convex
*   SOC and SDP constraints work

* * *

0.5.9 Optimization intuition (why solvers love affine maps)
-----------------------------------------------------------

Solvers treat affine expressions as **atomic** objects:

*   gradients are constant
*   Hessians vanish
*   dual variables attach cleanly
*   geometry is preserved exactly

This is why modeling systems (CVX, CVXPY, JuMP) enforce **disciplined convex programming** rules centered on affine structure.

* * *

0.5.10 Summary (mental checklist)
---------------------------------

You should now be able to say, without hesitation:

*   Linear map = matrix, origin fixed
*   Affine map = matrix + shift
*   Linear combinations ↔ linear maps
*   Affine combinations ↔ affine maps
*   Convex sets are stable under affine maps
*   Affine equalities are allowed; nonlinear equalities are poison
*   Every constraint you write should be understood as a preimage under an affine map

* * *

**This concludes Phase 0.**  
You now possess the mathematical atoms—objects, sets, functions, affine geometry—on which the entire convex optimization edifice is built.

Next: **Phase 1.1 — Convex combinations**, where convexity finally enters the stage explicitly.

2/2

## Response:
**1.1 — Convex combinations (the primitive operation of convexity)**
--------------------------------------------------------------------

Everything that will later be called _convex_—convex sets, convex functions, convex optimization problems—reduces to one operation and one operation only:

> **Mixing points without leaving the allowed region.**

This subsection isolates that operation, defines it precisely, and explains why it is the only mixing rule convexity cares about. Nothing here is optional background; this is the atom from which all convex geometry is built.

* * *

### **1.1.0 Why “mixing” is the right starting point**

Before we talk about sets being convex or functions being convex, we need a notion of _combining_ points.

There are many ways to combine vectors:

*   addition  $x+y$ ,
*   linear combinations  $\alpha x+\beta y$ ,
*   averages  $(x+y)/2$ ,
*   nonlinear combinations like  $x^2+y^2$ .

Convexity singles out **one very specific family** of combinations: those that interpolate between points _without extrapolating beyond them_.

That family is convex combinations.

* * *

### **1.1.1 Definition: convex combination of two points**

Let  $x,y \in \mathbb{R}^n$ .

A **convex combination** of  $x$  and  $y$  is any point of the form

$$
\boxed{z = \theta x + (1-\theta)y \quad \text{with } \theta \in [0,1].}
$$

Interpretation, piece by piece:

*   The coefficients  $\theta$  and  $1-\theta$  are **nonnegative**.
*   They **sum to one**.
*   The point  $z$  lies “between”  $x$  and  $y$ .

Special cases:

*    $\theta=1 \Rightarrow z=x$ ,
*    $\theta=0 \Rightarrow z=y$ ,
*    $\theta=1/2 \Rightarrow z=(x+y)/2$  (the midpoint).

This is the _only_ interpolation operation convexity allows.

* * *

### **1.1.2 Geometry: convex combinations trace line segments**

Fix  $x,y\in\mathbb{R}^n$ .  
Define the map

$$
\gamma(\theta) := \theta x + (1-\theta)y,\qquad \theta\in[0,1].
$$

As  $\theta$  varies from 0 to 1,  $\gamma(\theta)$  traces the **line segment** connecting  $y$  to  $x$ .

Important observations:

*   The line segment includes the endpoints.
*   No point on the segment lies “beyond”  $x$  or  $y$ .
*   The segment is the _smallest_ set containing  $x$  and  $y$  that is closed under convex combinations.

This geometric fact is not intuition—it is the operational meaning of convex combinations.

* * *

### **1.1.3 Why the coefficients must sum to one**

Consider a general linear combination:

$$
z = \alpha x + \beta y.
$$

There are three qualitatively different regimes:

1.  ** $\alpha+\beta=1$ ,  $\alpha,\beta\ge0$ **  
    → convex combination (interpolation).
2.  ** $\alpha+\beta=1$ , but one coefficient negative**  
    → affine combination (still on the line, but possibly outside the segment).
3.  ** $\alpha+\beta\neq1$ **  
    → linear combination (scaling + mixing; no geometric containment).

Convexity deliberately restricts to case (1) because it guarantees:

*   no extrapolation,
*   no scaling,
*   no escape from the region spanned by the points.

This is why convexity is a _stability_ concept.

* * *

### **1.1.4 Convex combinations vs affine combinations**

It is crucial to separate these two.

*   **Affine combination** of  $x,y$ :
    
$$
z = \theta x + (1-\theta)y \quad \text{with } \theta \in \mathbb{R}.
$$

This describes the _entire line_ through  $x$  and  $y$ .

*   **Convex combination**:
    
$$
\theta \in [0,1].
$$

This restriction collapses the line to the segment.

Convexity lives on segments, not on full lines.

* * *

### **1.1.5 Definition: convex combination of finitely many points**

Let  $x_1,\dots,x_k \in \mathbb{R}^n$ .

A **convex combination** of these points is any vector of the form

$$
\boxed{ z = \sum_{i=1}^k \theta_i x_i \quad \text{such that } \theta_i \ge 0,\ \sum_{i=1}^k \theta_i = 1. }
$$

Interpretation:

*   The coefficients  $(\theta_1,\dots,\theta_k)$  form a probability vector.
*    $z$  is a weighted average of the points.
*   No point is extrapolated beyond the given set.

Special cases:

*   One  $\theta_i=1$  gives a vertex.
*   Equal weights give the centroid.

* * *

### **1.1.6 Probability interpretation (not optional intuition)**

The condition

$$
\theta_i \ge 0,\quad \sum_i \theta_i = 1
$$

means  $(\theta_1,\dots,\theta_k)$  lies in the **simplex**.

Thus:

$$
z = \sum_i \theta_i x_i = \mathbb{E}[X],
$$

where  $X$  is a random variable taking value  $x_i$  with probability  $\theta_i$ .

This interpretation is not cosmetic:

*   Jensen’s inequality later _is_ convexity of expectations.
*   Robust optimization uses worst-case expectations.
*   Convex combinations encode uncertainty averaging.

* * *

### **1.1.7 Minimality: why convex combinations generate convex sets**

Given points  $x_1,\dots,x_k$ , define the set

$$
\mathrm{conv}\{x_1,\dots,x_k\} := \left\{ \sum_{i=1}^k \theta_i x_i : \theta_i \ge 0,\ \sum_i \theta_i = 1 \right\}.
$$

This is called the **convex hull**.

Two fundamental facts (we will prove later, but you must understand them now):

1.  This set is convex.
2.  It is the **smallest convex set** containing all the points.

Convex combinations are not just allowed operations; they _generate_ convexity.

* * *

### **1.1.8 Closure under repeated convex combinations**

Convexity is recursive.

If you take convex combinations of convex combinations, you do not leave the convex hull.

Formally:

*   Any convex combination of points that are themselves convex combinations of  $\{x_i\}$  is again a convex combination of the original points.

This associativity property is why convex hulls are stable objects and why optimization over convex sets is well-posed.

* * *

### **1.1.9 What convex combinations are _not_**

It is just as important to know what is excluded:

*   Multiplying by coefficients that sum to more than 1 (scaling outward).
*   Allowing negative weights (reflection/extrapolation).
*   Nonlinear mixing (products, squares, norms).

Convexity is restrictive by design. That restriction is what makes global optimization possible.

* * *

### **1.1.10 Why convex combinations are the only mixing rule convexity uses**

Convex optimization relies on one invariance principle:

> If two points are feasible, then any _allowed mixture_ of them should also be feasible.

“Allowed mixture” is defined **exactly** as a convex combination.

Any weaker notion breaks stability.  
Any stronger notion destroys tractability.

This is why every definition of convexity—set-based, function-based, epigraph-based—reduces to convex combinations.

* * *

### **1.1.11 Checklist (you must be fluent before moving on)**

You should be able to do the following instantly and without guessing:

*   Write down the general form of a convex combination (2 points,  $k$  points).
*   Explain geometrically why  $\theta\in[0,1]$  matters.
*   Distinguish linear, affine, and convex combinations.
*   Interpret convex combinations probabilistically.
*   Explain why convex combinations generate convex hulls.
*   Explain why convexity is fundamentally about _segments_, not lines.

* * *

### **Roadmap position**

This subsection introduced the **primitive operation**.

Next, in **1.2**, we will define **convex sets** _entirely in terms of convex combinations_ and show how every geometric closure rule follows from this single idea.

From here on, nothing new will be added—only consequences will be unfolded.

1/2

## Response:
**1.2 — Convex sets (closure under mixing, geometry made precise)**
-------------------------------------------------------------------

This subsection is where convexity **actually enters mathematics**.  
Everything before this—objects, sets, functions, affine maps, convex combinations—was preparation. Now we assemble those pieces into the central definition and then _unpack it until nothing is implicit_.

Convex optimization is optimization **over convex sets**.  
If you do not understand convex sets at a molecular level, every later theorem (duality, KKT, cones, SDP, robustness) becomes fragile pattern-matching.

We proceed slowly, rigorously, and exhaustively.

* * *

**1.2.0 What convexity is really asserting**
--------------------------------------------

At its core, convexity is a **stability principle**:

> If a set allows two points, it must also allow _every non-extrapolating mixture_ of those points.

Nothing more. Nothing less.

This principle is encoded using **convex combinations**, introduced in 1.1. Convex sets are exactly those sets that are closed under that operation.

* * *

**1.2.1 Definition: convex set (two-point form)**
-------------------------------------------------

Let  $C \subseteq \mathbb{R}^n$ .

We say that  $C$  is **convex** if for **every** pair of points  $x,y \in C$  and for **every** scalar  $\theta \in [0,1]$ ,

$$
\boxed{ \theta x + (1-\theta)y \in C. }
$$

Read this slowly and literally:

*   You may choose _any_ two points in the set.
*   You may choose _any_ mixing weight between 0 and 1.
*   The resulting mixture must remain in the set.

If even **one** such mixture leaves the set, the set is not convex.

This is a universal quantification. Convexity is an all-or-nothing property.

* * *

**1.2.2 Equivalent geometric formulation: line segments**
---------------------------------------------------------

The definition above is equivalent to a geometric statement:

> A set  $C$  is convex if and only if, for every  $x,y \in C$ , the **entire line segment** connecting  $x$  and  $y$  lies in  $C$ .

Formally:

$$
[x,y] := \{\theta x + (1-\theta)y : \theta \in [0,1]\} \subseteq C.
$$

This equivalence is not a metaphor. It is a literal translation of the algebraic definition into geometry.

Convex sets contain **no holes, dents, or inward folds**.

* * *

**1.2.3 Why convexity is defined using pairs (and not triples)**
----------------------------------------------------------------

At first glance, one might ask:

> Why define convexity using only pairs of points?  
> Why not require closure under convex combinations of _any number_ of points?

Answer: **two points are sufficient**.

### Theorem (pairwise closure ⇒ finite closure)

If a set  $C$  is closed under convex combinations of **pairs** of points, then it is closed under convex combinations of **any finite number** of points.

#### Proof (constructive, step-by-step)

Take points  $x_1,\dots,x_k \in C$  and coefficients  $\theta_i \ge 0$  with  $\sum_i \theta_i = 1$ .

We prove by induction on  $k$ .

*   Base case  $k=2$ : true by definition.
*   Inductive step: assume true for  $k-1$ .

Define:

$$
y := \sum_{i=1}^{k-1} \frac{\theta_i}{1-\theta_k} x_i
$$

Note:

*    $\frac{\theta_i}{1-\theta_k} \ge 0$ ,
*    $\sum_{i=1}^{k-1} \frac{\theta_i}{1-\theta_k} = 1$ .

So  $y$  is a convex combination of  $x_1,\dots,x_{k-1}$ , hence  $y \in C$  by the induction hypothesis.

Now observe:

$$
\sum_{i=1}^k \theta_i x_i = (1-\theta_k)y + \theta_k x_k,
$$

which is a convex combination of  $y$  and  $x_k$ .

Since both are in  $C$ , the result lies in  $C$ .

□

This is why the two-point definition is both minimal and complete.

* * *

**1.2.4 Convex vs non-convex: canonical examples**
--------------------------------------------------

### Convex sets

1.  **Entire space**  $\mathbb{R}^n$   
    Trivially convex.
2.  **Single point**  $\{x_0\}$   
    Any convex combination collapses to  $x_0$ .
3.  **Line / affine subspace**  
    Closed under all affine combinations.
4.  **Line segment**  
    Convex by construction.
5.  **Ball**  $\{x:\|x\|\le r\}$   
    Convex by triangle inequality.
6.  **Halfspace**  $\{x:a^\top x \le b\}$   
    Linear inequality preserved under convex combinations.

* * *

### Non-convex sets (important counterexamples)

1.  **Two disjoint points**  
    Segment between them leaves the set.
2.  **Annulus (ring)**  
    Midpoints fall into the hole.
3.  **Union of convex sets (in general)**  
    Union breaks convexity.

Understanding _why_ these fail is as important as recognizing convex ones.

* * *

**1.2.5 Convexity is a property of sets, not equations**
--------------------------------------------------------

A critical conceptual correction:

> Convexity is not about how a set is _described_.  
> It is about which points belong to it.

The same set can be described by:

*   inequalities,
*   equalities,
*   parameterizations,
*   epigraphs,
*   indicator functions.

Convexity must be checked on the **resulting set**, not on the surface form.

This is why “looking convex” is meaningless.

* * *

**1.2.6 Closure properties (the legal moves of convexity)**
-----------------------------------------------------------

Convexity is valuable because it is **stable under many operations**. These are the operations you are allowed to use when modeling.

We state them precisely; proofs will follow later, but you must internalize the statements now.

* * *

### **(A) Intersection**

If  $\{C_i\}_{i\in I}$  are convex sets, then

$$
\bigcap_{i\in I} C_i
$$

is convex.

**Why:**  
If a point lies in _every_ set, then any convex combination lies in _every_ set.

This is why:

*   multiple convex constraints remain convex,
*   feasibility regions are intersections.

* * *

### **(B) Affine images**

If  $C$  is convex and  $f(x)=Ax+b$  is affine, then

$$
f(C) := \{Ax+b : x\in C\}
$$

is convex.

**Why:**  
Affine maps preserve affine combinations, hence convex combinations.

* * *

### **(C) Affine preimages**

If  $C$  is convex, then

$$
f^{-1}(C) = \{x : Ax+b \in C\}
$$

is convex.

This is the single most used rule in convex optimization.

It explains why:

*    $Ax=b$ ,
*    $Ax\le b$ ,
*    $\|Ax-b\|\le t$ ,  
    are convex constraints.

* * *

### **(D) Cartesian products**

If  $C\subseteq\mathbb{R}^n$  and  $D\subseteq\mathbb{R}^m$  are convex, then

$$
C\times D := \{(x,y):x\in C,y\in D\}
$$

is convex.

This matters for:

*   epigraphs,
*   product spaces,
*   multi-variable optimization.

* * *

### **(E) Minkowski sum**

Given convex sets  $C,D$ ,

$$
C+D := \{x+y:x\in C,y\in D\}
$$

is convex.

This operation will later encode uncertainty and disturbances.

* * *

**1.2.7 Convex hull: the smallest convex set containing points**
----------------------------------------------------------------

Given a set  $S\subseteq\mathbb{R}^n$ , define its **convex hull**:

$$
\operatorname{conv}(S) := \left\{ \sum_{i=1}^k \theta_i x_i : x_i\in S,\ \theta_i\ge 0,\ \sum_i\theta_i=1 \right\}.
$$

Key facts:

1.   $\operatorname{conv}(S)$  is convex.
2.   $\operatorname{conv}(S)$  contains  $S$ .
3.  Any convex set containing  $S$  must contain  $\operatorname{conv}(S)$ .

Thus, it is the **smallest convex superset** of  $S$ .

Convexification is the act of replacing a set by its convex hull.

* * *

**1.2.8 Extreme points (preview, but crucial)**
-----------------------------------------------

A point  $x\in C$  is an **extreme point** if it cannot be written as a nontrivial convex combination of other points in  $C$ .

Extreme points are:

*   vertices of polytopes,
*   candidates for optima in linear optimization.

Later:

> Linear objectives attain their optima at extreme points.

This fact drives simplex methods and duality geometry.

* * *

**1.2.9 Why convex sets are the only feasible regions we can optimize over globally**
-------------------------------------------------------------------------------------

Here is the deep reason convex optimization works:

If the feasible set  $C$  is convex and the objective is convex, then:

*   any local minimum is global,
*   line search is meaningful,
*   duality has no gap (under mild conditions),
*   algorithms converge reliably.

Nonconvex feasible sets destroy all of this.

Convex sets are not “nice”.  
They are **necessary**.

* * *

**1.2.10 Common failure modes**
-------------------------------

You must actively avoid these mistakes:

1.  Confusing **union** with **intersection**  
    Unions of convex sets are usually nonconvex.
2.  Assuming equality constraints preserve convexity  
    Only _affine_ equalities are safe.
3.  Checking convexity pointwise instead of segment-wise  
    Convexity is about _all_ segments.
4.  Forgetting domain restrictions  
    Convexity is defined on the domain, not the ambient space.

* * *

**1.2.11 Checklist (do not proceed unless fluent)**
---------------------------------------------------

You should be able to:

*   State the definition of a convex set precisely.
*   Translate it into the line-segment formulation.
*   Prove closure under intersection and affine maps.
*   Explain convex hulls and why they are minimal.
*   Recognize convex vs nonconvex sets instantly.
*   Explain why convexity is essential for optimization.

* * *

### **Roadmap position**

You now understand **convex sets**, the geometric objects optimization lives on.

Next: **1.3 — Affine sets, hyperplanes, and halfspaces**, where we classify the most important convex sets and learn how they form the building blocks of constraints.

## Response:
**1.3 — Affine sets, hyperplanes, and halfspaces (the atomic building blocks of constraints)**
----------------------------------------------------------------------------------------------

If convex sets are the “feasible worlds” we optimize over, then **affine sets, hyperplanes, and halfspaces** are the **atoms** from which most convex feasible worlds are built.

This is not just geometry for its own sake. These objects are exactly what appear when you write:

*   equality constraints:  $Ax=b$ 
*   inequality constraints:  $a^\top x \le b$ 
*   polyhedra: intersections of halfspaces
*   LP feasibility regions
*   supporting hyperplanes and separation (which later becomes duality)

We’ll build each notion from scratch and prove all key properties carefully.

* * *

**1.3.0 Why this subsection matters**
=====================================

Convex optimization is basically the art of converting problems into constraints of the form:

*   affine equalities:  $Ax=b$ 
*   convex inequalities:  $f(x)\le 0$ 

The “affine equality” part is not arbitrary; it is exactly the statement that  $x$  must lie in an **affine set**.

And the “linear inequality” (a special convex inequality) defines a **halfspace**.

So if you can’t manipulate affine sets and halfspaces with total fluency, you can’t model.

* * *

**1.3.1 Affine combinations (the operation behind affine sets)**
================================================================

Before defining affine sets, we need the analogue of convex combinations.

### Definition (affine combination)

Given points  $x_1,\dots,x_k \in \mathbb{R}^n$ , an **affine combination** is any vector of the form

$$
z = \sum_{i=1}^k \theta_i x_i \quad \text{where} \quad \sum_{i=1}^k \theta_i = 1,
$$

with **no sign restriction** on the coefficients  $\theta_i$ .

Compare with convex combinations:

*   convex combination:  $\theta_i\ge 0$  and  $\sum \theta_i=1$ 
*   affine combination: only  $\sum \theta_i=1$ 

So affine combinations allow **extrapolation** (points can go beyond segments), but they still preserve a special structure: translation invariance.

### Two-point affine combination

For two points  $x,y$ ,

$$
z = \theta x + (1-\theta)y, \quad \theta\in\mathbb{R}
$$

generates the entire **line** through  $x$  and  $y$ .  
When  $\theta\in[0,1]$  you get the segment; outside that interval you extrapolate.

* * *

**1.3.2 Affine sets (definition and equivalent forms)**
=======================================================

### Definition (affine set)

A set  $A \subseteq \mathbb{R}^n$  is **affine** if for any  $x,y \in A$  and any  $\theta\in\mathbb{R}$ ,

$$
\boxed{\theta x + (1-\theta)y \in A.}
$$

This is exactly the convex set definition but with  $\theta$  allowed to be any real number, not just  $[0,1]$ .

Interpretation:

*   convex set: closed under _interpolation_
*   affine set: closed under _interpolation + extrapolation_

So affine sets contain the **entire line** through any two points in the set.

* * *

**1.3.3 Affine sets are translated subspaces (big structural theorem)**
-----------------------------------------------------------------------

This is one of the most important structure facts in all of convex geometry:

> **Theorem:** A set  $A\subseteq\mathbb{R}^n$  is affine if and only if it can be written as

$$
\boxed{A = x_0 + S := \{x_0 + s : s\in S\}}
$$

for some point  $x_0\in\mathbb{R}^n$  and some **linear subspace**  $S\subseteq\mathbb{R}^n$ .

This tells you: affine sets are exactly “subspaces shifted away from the origin”.

We prove both directions carefully.

* * *

### Proof (⇒ direction): affine set implies translate of a subspace

Assume  $A$  is affine and pick any point  $x_0\in A$ .  
Define

$$
S := A - x_0 := \{x - x_0 : x\in A\}.
$$

So  $S$  is the set of all displacement vectors from  $x_0$  to other points of  $A$ .

We claim  $S$  is a **linear subspace**.

To prove  $S$  is a subspace, we must show:

1.   $0\in S$ 
2.  closed under addition
3.  closed under scalar multiplication

**(1)  $0\in S$ :**  
Take  $x=x_0\in A$ . Then  $x-x_0=0$ , so  $0\in S$ .

**(2) closed under addition:**  
Take  $u,v\in S$ .  
Then  $u=x_1-x_0$  and  $v=x_2-x_0$  for some  $x_1,x_2\in A$ .

We want to show  $u+v\in S$ , i.e., there exists some  $x_3\in A$  such that

$$
x_3-x_0 = (x_1-x_0) + (x_2-x_0) = x_1 + x_2 - 2x_0.
$$

So we need  $x_3 = x_1 + x_2 - x_0$  to lie in  $A$ .

Because  $A$  is affine, it is closed under affine combinations.  
Observe:

$$
x_1 + x_2 - x_0 = 2\left(\frac{1}{2}x_1 + \frac{1}{2}x_2\right) + (-1)x_0.
$$

This expression is a combination of  $x_1,x_2,x_0$  with coefficients

$$
\theta_1 = 1,\quad \theta_2 = 1,\quad \theta_0 = -1,
$$

which sum to  $1$ . Therefore it is an affine combination of points in  $A$ , hence belongs to  $A$ . So  $x_3\in A$ , and thus  $u+v\in S$ .

**(3) closed under scalar multiplication:**  
Take  $u\in S$ . Then  $u=x_1-x_0$  for some  $x_1\in A$ .  
Let  $\alpha\in\mathbb{R}$ . We want  $\alpha u \in S$ , meaning:

$$
\alpha(x_1-x_0) = x_2-x_0 \quad \text{for some } x_2\in A.
$$

Rearrange:

$$
x_2 = \alpha x_1 + (1-\alpha)x_0.
$$

But this is an affine combination of  $x_1$  and  $x_0$  (coefficients sum to 1), so  $x_2\in A$ . Hence  $\alpha u \in S$ .

So  $S$  is a linear subspace.

Finally, show  $A = x_0 + S$ :

*   For any  $x\in A$ ,  $x-x_0\in S$ , so  $x=x_0+(x-x_0)\in x_0+S$ . So  $A\subseteq x_0+S$ .
*   For any  $s\in S$ ,  $s=x-x_0$  for some  $x\in A$ , hence  $x_0+s=x\in A$ . So  $x_0+S\subseteq A$ .

Thus  $A=x_0+S$ . ∎

* * *

### Proof (⇐ direction): translate of a subspace implies affine

Assume  $A = x_0 + S$  where  $S$  is a subspace.

Take any  $x,y\in A$ . Then  $x=x_0+s_1$ ,  $y=x_0+s_2$  for some  $s_1,s_2\in S$ .

For any  $\theta\in\mathbb{R}$ ,

$$
\theta x + (1-\theta)y = \theta(x_0+s_1) + (1-\theta)(x_0+s_2) = x_0 + \theta s_1 + (1-\theta)s_2.
$$

Since  $S$  is a subspace,  $\theta s_1 + (1-\theta)s_2 \in S$ .  
Therefore the whole expression lies in  $x_0+S=A$ .

So  $A$  is affine. ∎

* * *

**1.3.4 Hyperplanes (the most important affine sets)**
======================================================

### Definition (hyperplane)

A **hyperplane** in  $\mathbb{R}^n$  is a set of the form:

$$
\boxed{H = \{x\in\mathbb{R}^n : a^\top x = b\}}
$$

where  $a\in\mathbb{R}^n$  is nonzero and  $b\in\mathbb{R}$ .

Interpretation:

*    $a$  is the **normal vector** (perpendicular direction).
*    $b$  sets the offset (how far the hyperplane is from the origin in the  $a$ \-direction).

This is the canonical geometry behind affine equality constraints.

* * *

**1.3.5 Proving hyperplanes are affine sets**
---------------------------------------------

Take  $x,y\in H$ . Then  $a^\top x=b$  and  $a^\top y=b$ .

For any  $\theta\in\mathbb{R}$ ,

$$
a^\top(\theta x + (1-\theta)y) = \theta a^\top x + (1-\theta)a^\top y = \theta b + (1-\theta)b = b.
$$

So  $\theta x+(1-\theta)y \in H$ . Therefore  $H$  is affine. ∎

This proof is a template you’ll reuse constantly: affine sets are defined by affine equalities.

* * *

**1.3.6 Halfspaces (the simplest convex inequality sets)**
----------------------------------------------------------

### Definition (halfspace)

A **halfspace** is a set of the form:

$$
\boxed{S = \{x\in\mathbb{R}^n : a^\top x \le b\}}
$$

with  $a\neq 0$ .

Halfspaces are convex, and they are the building blocks of polyhedra and LP feasible regions.

* * *

**1.3.7 Proving halfspaces are convex**
---------------------------------------

Let  $x,y\in S$ , so  $a^\top x\le b$  and  $a^\top y\le b$ .

For  $\theta\in[0,1]$ ,

$$
a^\top(\theta x + (1-\theta)y) = \theta a^\top x + (1-\theta)a^\top y \le \theta b + (1-\theta)b = b.
$$

So  $\theta x+(1-\theta)y \in S$ . Therefore  $S$  is convex. ∎

This is another template proof: linear inequalities define convex sets because linear functionals respect convex combinations.

* * *

**1.3.8 Polyhedra: intersection of finitely many halfspaces**
=============================================================

A **polyhedron** is any set expressible as:

$$
\boxed{P = \{x : Ax \le b,\; Cx = d\}}
$$

where inequalities are componentwise.

Interpretation:

*    $Ax\le b$  is a finite intersection of halfspaces.
*    $Cx=d$  is an affine set constraint.

Because:

*   intersections of convex sets are convex,
*   halfspaces are convex,
*   affine sets are convex,

it follows immediately that polyhedra are convex.

This is why LP feasible sets are convex.

* * *

**1.3.9 Normal vectors and geometry (why  $a$  is called “normal”)**
====================================================================

For the hyperplane  $H=\{x:a^\top x=b\}$ , the vector  $a$  is orthogonal to the hyperplane in the Euclidean inner product sense:

If  $x,y\in H$ , then  $a^\top x=b$  and  $a^\top y=b$ . Subtract:

$$
a^\top(x-y)=0.
$$

So  $a$  is orthogonal to every direction  $x-y$  that lies within the hyperplane.

Thus,  $a$  is perpendicular to the hyperplane.

This matters later for:

*   supporting hyperplanes,
*   separation theorems,
*   dual variables (they are normals).

* * *

**1.3.10 Distances to hyperplanes (preview but very used)**
===========================================================

Given  $H=\{x:a^\top x=b\}$  and a point  $y$ , the Euclidean distance from  $y$  to  $H$  is:

$$
\mathrm{dist}(y,H) = \frac{|a^\top y - b|}{\|a\|_2}.
$$

This formula is not cosmetic. It’s the quantitative version of “normal vector.”

It will reappear when:

*   proving projection properties,
*   deriving margin constraints,
*   understanding robust halfspaces.

* * *

**1.3.11 Common modeling equivalences you must internalize**
============================================================

1.  Equality constraint  $Ax=b$   
    ⇔  $x$  lies in an affine set.
2.  Inequality  $a^\top x \le b$   
    ⇔  $x$  lies in a halfspace.
3.  System  $Ax\le b$   
    ⇔ intersection of halfspaces (polyhedron).
4.  Linear program feasibility region  
    ⇔ polyhedron.

These are not “analogies.” They are literal set-theoretic equivalences.

* * *

**1.3.12 Failure modes**
========================

1.  **Using nonlinear equalities** in a convex problem  
    Almost always makes feasible set nonconvex.
2.  **Forgetting componentwise meaning of  $Ax\le b$ **  
    This is  $m$  inequalities, not one.
3.  **Not checking  $a\neq0$ **  
    If  $a=0$ , “hyperplane” degenerates into either empty set or whole space depending on  $b$ .

* * *

**1.3.13 Checklist**
====================

You should now be able to:

*   Define affine sets and prove they are translates of subspaces.
*   Define hyperplanes and halfspaces and prove their affine/convex properties.
*   Explain why affine equalities are allowed in convex optimization.
*   Represent polyhedra as intersections of halfspaces and affine sets.
*   Interpret normals geometrically and relate them to constraints.

* * *

### Roadmap position

We have the linear/affine building blocks.

Next is **1.4 — Convex cones and the “big cones”** (nonnegative orthant, SOC, PSD cone).  
That will set up conic standard forms, dual cones, and most of PS6 modeling patterns.

## Response:
**1.4 — Convex cones (and the “big three” cones: nonnegative orthant, SOC, PSD cone)**
--------------------------------------------------------------------------------------

_(complete zero-to-hero newcomer walkthrough, with full definitions, geometry, and the exact modeling meaning for convex optimization)_

Cones are not a side topic. They are the **native language** of modern convex optimization.

A huge fraction of “weird-looking” convex constraints become simple once you recognize:

> “This is just an affine map landing inside a cone.”

That one sentence is the reason SOCP and SDP exist.

In PS6-style modeling, cones are the main target objects. So we will build cones from scratch, then isolate the three cones that run the world:

1.  **Nonnegative orthant**  $\mathbb{R}^n_+$ 
2.  **Second-order cone** (SOC)  $\mathcal{Q}^{n+1}$ 
3.  **Positive semidefinite cone** (PSD cone)  $\mathbb{S}^n_+$ 

We’ll do this with maximal explicitness.

* * *

**1.4.0 Why cones appear at all**
=================================

Many constraints are inherently **scale-invariant**:

*   “componentwise nonnegative” ( $x\ge0$ )
*   “norm bounded by scalar” ( $\|u\|_2 \le t$ )
*   “matrix is PSD” ( $X\succeq 0$ )

If  $x$  is feasible, then scaling it by a positive factor often keeps it feasible. That scaling invariance is exactly what cones formalize.

Cones let you unify constraints into one template:

$$
\boxed{\text{Constraint } \quad F(x) \in K}
$$

where:

*    $F(x)$  is an **affine map** (from 0.5),
*    $K$  is a **convex cone**.

That is conic form. Once you’re in that form, solvers know what to do.

* * *

**1.4.1 Cones: the raw set definition**
=======================================

### **Definition (cone)**

A set  $K \subseteq \mathbb{R}^n$  is a **cone** if it is closed under multiplication by **nonnegative scalars**:

$$
\boxed{ x \in K,\ \alpha \ge 0 \quad \Rightarrow \quad \alpha x \in K. }
$$

Interpretation:

*   If you can stand at point  $x$ , you can slide outward along the ray  $\{\alpha x : \alpha\ge0\}$  and stay inside the set.

Important:  
The definition says **nothing** about being closed under addition or convexity. A cone can be nonconvex.

* * *

**1.4.2 Convex cones: the key object in convex optimization**
-------------------------------------------------------------

### **Definition (convex cone)**

A set  $K\subseteq \mathbb{R}^n$  is a **convex cone** if:

1.  it is a cone (closed under  $\alpha\ge 0$  scaling), and
2.  it is convex (closed under convex combinations).

Equivalently—and this is the most useful form:

$$
\boxed{ x,y \in K,\ \alpha,\beta \ge 0 \quad \Rightarrow \quad \alpha x + \beta y \in K. }
$$

This is closure under **conic combinations** (nonnegative linear combinations).

### Why this equivalence holds (explicit proof)

Assume  $K$  is a convex cone.

*   Since it’s a cone,  $\alpha x \in K$  and  $\beta y \in K$  for  $\alpha,\beta\ge0$ .
*   Since it’s convex, for any  $\theta\in[0,1]$ ,
    $$
    \theta(\alpha x) + (1-\theta)(\beta y) \in K.
    $$

Pick  $\theta = \frac{\alpha}{\alpha+\beta}$  when  $\alpha+\beta>0$ . Then:

$$
\theta(\alpha x) + (1-\theta)(\beta y) = \frac{\alpha}{\alpha+\beta}\alpha x + \frac{\beta}{\alpha+\beta}\beta y = \frac{1}{\alpha+\beta}(\alpha^2 x + \beta^2 y),
$$

Not exactly  $\alpha x+\beta y$ . So we instead use a simpler route:

Convex cone implies:

*    $x,y\in K$  ⇒  $x+y\in K$  because
    $$
    x+y = 2\left(\frac{1}{2}x + \frac{1}{2}y\right)
    $$
    and  $\frac{1}{2}x+\frac{1}{2}y\in K$  by convexity, then multiply by  $2$  using cone property.
*   Once closed under addition and scaling, it is closed under any  $\alpha,\beta\ge0$ :
    $$
    \alpha x + \beta y \in K.
    $$

Conversely, if closed under  $\alpha x+\beta y$  with  $\alpha,\beta\ge0$ , then:

*   take  $\beta=0$  gives cone scaling,
*   take  $\alpha=\theta,\beta=1-\theta$  gives convexity for  $\theta\in[0,1]$ .

So the conic-combination closure is exactly “convex + cone”.

* * *

**1.4.3 Pointed, solid, proper cones (properties you’ll meet later)**
=====================================================================

These properties matter for duality and uniqueness.

*   **Pointed**:  $K\cap(-K) = \{0\}$ .  
    Means it contains no line through the origin (no nontrivial  $x$  with both  $x$  and  $-x$  inside).
*   **Solid**: has nonempty interior.  
    Means it’s not “flat”.
*   **Closed**: contains its boundary limit points.
*   A **proper cone** is closed, convex, pointed, and solid.

The big cones used in optimization are proper cones.

* * *

**1.4.4 Cone-induced partial order (why cones create “ $\preceq$ ” relations)**
===============================================================================

Given a cone  $K$ , we can define an order relation:

$$
x \preceq_K y \quad \Longleftrightarrow \quad y-x \in K.
$$

Examples:

*   For  $K=\mathbb{R}^n_+$ :  $x \preceq y$  means componentwise inequality  $x_i \le y_i$ .
*   For  $K=\mathbb{S}^n_+$ :  $X \preceq Y$  means  $Y-X$  is PSD.

This is why we say:

*    $x \ge 0$  means  $x \in \mathbb{R}^n_+$ 
*    $X \succeq 0$  means  $X\in \mathbb{S}^n_+$ 

So inequalities in convex optimization are often just **membership in a cone**.

* * *

**1.4.5 Conic form: constraints as “affine map in cone”**
=========================================================

This is the modeling superpower.

A conic constraint looks like:

$$
F(x) \in K
$$

where  $F(x)=Ax+b$  is affine.

Why is this always convex if  $K$  is convex?

Because the feasible set is a preimage:

$$
\{x : F(x)\in K\} = F^{-1}(K)
$$

and affine preimages of convex sets are convex (from 0.5 / 1.2 closure rules).

So:

$$
\boxed{\text{Affine preimage of a convex cone is convex.}}
$$

That is the formal reason conic programming is convex.

* * *

**1.4.6 The “big three” cones**
===============================

Now we build the three cones that dominate convex optimization.

* * *

**(I) Nonnegative orthant  $\mathbb{R}^n_+$ **
----------------------------------------------

### Definition

$$
\boxed{ \mathbb{R}^n_+ := \{x\in\mathbb{R}^n : x_i \ge 0 \ \forall i\}. }
$$

This is the simplest convex cone.

### Verify it is a convex cone (complete check)

1.  Cone property: if  $x_i\ge0$  and  $\alpha\ge0$ , then  $(\alpha x)_i=\alpha x_i\ge0$ . So  $\alpha x\in\mathbb{R}^n_+$ .
2.  Convexity: if  $x,y\ge0$  and  $\theta\in[0,1]$ , then
    
$$
(\theta x + (1-\theta)y)_i = \theta x_i + (1-\theta)y_i \ge 0.
$$

So the combination stays in the set.

Thus it is a convex cone.

### Geometry

It’s the first “quadrant/octant/etc.” in  $n$ \-D: all coordinates nonnegative.

### Modeling meaning

*   Componentwise inequalities  $x \ge 0$  are cone membership.
*   General linear inequalities  $Ax \le b$  can be written as:
    $$
    b - Ax \in \mathbb{R}^m_+.
    $$

That’s already conic form. So **LP is conic programming over  $\mathbb{R}^m_+$ **.

* * *

**(II) Second-order cone (SOC)**
--------------------------------

This cone is the bridge between norms and linear constraints. It defines SOCP.

### Definition (SOC / Lorentz cone)

In  $\mathbb{R}^{n+1}$ , define:

$$
\boxed{ \mathcal{Q}^{n+1} := \{(t,x)\in\mathbb{R}\times\mathbb{R}^n : \|x\|_2 \le t\}. }
$$

Write the point as  $(t,x)$  where  $t$  is scalar,  $x\in\mathbb{R}^n$ .

Interpretation:

*   It contains points where the Euclidean length of  $x$  is bounded by the “height”  $t$ .
*   Automatically  $t\ge0$  because  $\|x\|_2\ge0$ .

### Prove SOC is a cone

Take  $(t,x)\in\mathcal{Q}^{n+1}$ , so  $\|x\|_2\le t$ . For  $\alpha\ge0$ ,

$$
\|\alpha x\|_2 = \alpha \|x\|_2 \le \alpha t.
$$

Thus  $(\alpha t, \alpha x)\in\mathcal{Q}^{n+1}$ . So it’s a cone.

### Prove SOC is convex (full proof)

Take  $(t_1,x_1)$  and  $(t_2,x_2)$  in SOC:

$$
\|x_1\|_2 \le t_1,\qquad \|x_2\|_2 \le t_2.
$$

Let  $\theta\in[0,1]$ . Consider:

$$
(t,x) := \theta(t_1,x_1) + (1-\theta)(t_2,x_2) = (\theta t_1 + (1-\theta)t_2,\ \theta x_1 + (1-\theta)x_2).
$$

We must show  $\|x\|_2 \le t$ .

Use triangle inequality and homogeneity of the norm:

$$
\|\theta x_1 + (1-\theta)x_2\|_2 \le \theta\|x_1\|_2 + (1-\theta)\|x_2\|_2 \le \theta t_1 + (1-\theta)t_2 = t.
$$

So  $(t,x)\in\mathcal{Q}^{n+1}$ . Hence SOC is convex.

### Modeling meaning (the key template)

A constraint:

$$
\|Ax+b\|_2 \le c^\top x + d
$$

is exactly:

$$
(c^\top x + d,\ Ax+b)\in\mathcal{Q}^{m+1}.
$$

So SOC constraints are simply “an affine map lands in SOC”.

This is the native form of SOCP.

### Rotated SOC (hyperbolic constraints bridge)

There is also the **rotated second-order cone**:

$$
\boxed{ \mathcal{Q}_r^{n+2} := \{(u,v,x)\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^n : 2uv \ge \|x\|_2^2,\ u\ge0,\ v\ge0\}. }
$$

Why it exists:

*   It represents “product” constraints like  $uv \ge w^2$ , which appear in hyperbolic constraints and GP/SOCP transformations.

This will be crucial later for exercises like “ $w^2 \le xy$ ” with  $x,y\ge0$ .

* * *

**(III) Positive semidefinite cone (PSD cone)**
-----------------------------------------------

This cone underlies SDPs and all LMI constraints.

### Step 1: Symmetric matrices space

Let  $\mathbb{S}^n$  be the set of real  $n\times n$  symmetric matrices:

$$
\mathbb{S}^n := \{X\in\mathbb{R}^{n\times n} : X=X^\top\}.
$$

We restrict to symmetric matrices because “ $\succeq 0$ ” is defined for them.

### Step 2: Definition of PSD

A symmetric matrix  $X\in\mathbb{S}^n$  is **positive semidefinite** if:

$$
\boxed{ v^\top X v \ge 0 \quad \forall v\in\mathbb{R}^n. }
$$

We write:

$$
X \succeq 0.
$$

This definition is fundamental. Everything else (eigenvalues, Cholesky, etc.) is equivalent and will be proved later.

### Definition (PSD cone)

$$
\boxed{ \mathbb{S}^n_+ := \{X\in\mathbb{S}^n : X\succeq 0\}. }
$$

### Prove PSD cone is a cone

Take  $X\succeq0$ ,  $\alpha\ge0$ . For any  $v$ ,

$$
v^\top(\alpha X)v = \alpha(v^\top X v)\ge0.
$$

So  $\alpha X \succeq 0$ . Cone property holds.

### Prove PSD cone is convex

Take  $X,Y\succeq0$  and  $\theta\in[0,1]$ . For any  $v$ ,

$$
v^\top(\theta X + (1-\theta)Y)v = \theta v^\top X v + (1-\theta)v^\top Y v \ge 0.
$$

Thus  $\theta X+(1-\theta)Y \succeq0$ . Convex.

### Modeling meaning: LMIs

A constraint like:

$$
X(x) \succeq 0
$$

where  $X(x)$  depends affinely on  $x$ , is called a **linear matrix inequality** (LMI).

Example:

$$
X(x) = A_0 + x_1 A_1 + \cdots + x_m A_m \succeq 0.
$$

This is an SDP constraint because it is exactly:

$$
X(x) \in \mathbb{S}^n_+.
$$

So SDP = conic programming over  $\mathbb{S}^n_+$ .

* * *

**1.4.7 Self-duality (preview) and “big three self-dual cones”**
================================================================

Your lectures often call these cones “self-dual”. The dual cone  $K^*$  is defined by:

$$
K^* := \{y : y^\top x \ge 0 \ \forall x\in K\}.
$$

Without proving it fully yet (we’ll do it later carefully), these three cones satisfy:

$$
(\mathbb{R}^n_+)^* = \mathbb{R}^n_+,\quad (\mathcal{Q}^{n+1})^* = \mathcal{Q}^{n+1},\quad (\mathbb{S}^n_+)^* = \mathbb{S}^n_+.
$$

This is one of the deep reasons they dominate convex optimization: duality becomes clean.

* * *

**1.4.8 How LP / SOCP / SDP fit into one unified framework**
============================================================

Now you can see the unification:

### Linear programming (LP)

Constraints:

$$
Ax \le b,\quad Cx=d
$$

become:

$$
b-Ax \in \mathbb{R}^m_+,\quad Cx-d=0.
$$

So LP is conic programming over  $\mathbb{R}^m_+$ .

### Second-order cone programming (SOCP)

Constraints:

$$
\|A_i x + b_i\|_2 \le c_i^\top x + d_i
$$

become:

$$
(c_i^\top x + d_i,\ A_i x + b_i)\in\mathcal{Q}^{k_i+1}.
$$

### Semidefinite programming (SDP)

Constraints:

$$
A_0 + \sum_i x_i A_i \succeq 0
$$

become:

$$
A_0 + \sum_i x_i A_i \in \mathbb{S}^n_+.
$$

So: LP ⊂ SOCP ⊂ SDP (in expressiveness).

* * *

**1.4.9 Common cone modeling patterns (the reflexes you want)**
===============================================================

You should develop immediate reflexes:

1.  **componentwise inequality**  $u \ge 0$   
    ⇔  $u \in \mathbb{R}^n_+$ 
2.  **Euclidean norm bound**  $\|z\|_2 \le t$   
    ⇔  $(t,z)\in \mathcal{Q}^{n+1}$ 
3.  **quadratic form / matrix inequality**  $X\succeq0$   
    ⇔  $X\in \mathbb{S}^n_+$ 
4.  **affine image constraint**  $F(x)\in K$   
    ⇔ “this is convex if  $K$  is convex”

These are the moves PS6 is trying to train.

* * *

**1.4.10 Failure modes (what causes point loss on quizzes)**
============================================================

1.  **Forgetting the right-hand side must be nonnegative in SOC form**  
    If you write  $\|u\|_2 \le t$  you must ensure  $t$  is not forced negative by other constraints; otherwise infeasible.
2.  **Confusing SOC with rotated SOC**  
    Hyperbolic constraints need rotated SOC, not standard SOC.
3.  **Treating  $X\succeq0$  as entrywise nonnegativity**  
    PSD is not elementwise. It is a quadratic form condition. Huge difference.
4.  **Assuming “cone” implies convex**  
    Cones can be nonconvex. Optimization needs convex cones.

* * *

**1.4.11 Checkpoint: what you must be able to do cold**
=======================================================

Before proceeding, you must be able to:

*   State the definition of cone and convex cone precisely.
*   Prove SOC and PSD cones are convex cones (you now have those proofs).
*   Translate constraints into “affine map in cone” form.
*   Recognize when a constraint is LP-type, SOCP-type, or SDP-type.
*   Explain the geometric meaning of each big cone.

* * *

Roadmap position
----------------

You now have the “conic vocabulary” needed for essentially all modeling in PS6.

Next in the roadmap is **1.5 Supporting hyperplanes (preview)** or, depending on your roadmap version, we proceed to deeper closure rules and separation intuition that leads into subgradients and duality.

Either way, from here on, the world becomes “cones + affine maps + epigraphs”. The rest is systematic technique.

## Response:
**1.5 — Supporting hyperplanes (the geometric skeleton of optimality, subgradients, and duality)**
--------------------------------------------------------------------------------------------------

This subsection is where convex optimization stops being “constraints and objectives” and becomes **geometry with proofs**.

Supporting hyperplanes are the _touch points_ between:

*   convex sets (feasible regions),
*   convex functions (via epigraphs),
*   optimality (why optima occur on “faces”),
*   subgradients (gradients of nonsmooth functions),
*   separation theorems (the engine of duality and certificates).

You will see this same idea repeatedly in different clothes. So we will build it from absolute first principles, with careful definitions, precise statements, and proofs you can reproduce.

* * *

**1.5.0 What problem are supporting hyperplanes solving?**
==========================================================

Given a convex set  $C\subseteq\mathbb{R}^n$ , imagine standing at a boundary point  $x_0\in\partial C$ . You want a linear inequality that:

1.  is **true for all points in  $C$ **, and
2.  is **tight at  $x_0$ **, meaning it “touches”  $C$  there.

That inequality is a **supporting hyperplane / supporting halfspace**.

This is exactly what happens at an optimum of a convex problem: the objective’s level set “just touches” the feasible set, or the feasible set “just touches” a level set, and a hyperplane is the local linear witness of that contact.

* * *

**1.5.1 Hyperplanes and halfspaces (quick recall, but with precise role)**
==========================================================================

A hyperplane is:

$$
H(a,b) = \{x : a^\top x = b\},\quad a\neq0.
$$

It divides space into two closed halfspaces:

$$
\{x: a^\top x \le b\} \quad \text{and} \quad \{x: a^\top x \ge b\}.
$$

Geometric meaning:

*    $a$  is the normal direction.
*    $b$  is the offset.

We now use hyperplanes **as “tangent planes” to convex sets** (even when the boundary is not smooth).

* * *

**1.5.2 Supporting halfspace and supporting hyperplane (definitions)**
======================================================================

Let  $C\subseteq\mathbb{R}^n$  be a **nonempty convex** set, and let  $x_0\in C$ .

### Definition (supporting halfspace at  $x_0$ )

A closed halfspace

$$
S = \{x : a^\top x \le b\}
$$

is a **supporting halfspace** of  $C$  at  $x_0$  if:

1.   $C \subseteq S$  (the halfspace contains the entire set), and
2.   $x_0$  lies on the boundary hyperplane:
    $$
    a^\top x_0 = b.
    $$

### Definition (supporting hyperplane at  $x_0$ )

The hyperplane

$$
H = \{x : a^\top x = b\}
$$

is a **supporting hyperplane** of  $C$  at  $x_0$  if the halfspace  $a^\top x \le b$  supports  $C$  at  $x_0$ .

Equivalent “single inequality” form: supporting at  $x_0$  means

$$
\boxed{ a^\top x \le a^\top x_0 \quad \forall x\in C. }
$$

(where we set  $b=a^\top x_0$ ).

So a supporting hyperplane is literally a linear functional that achieves its **maximum over  $C$ ** at  $x_0$ .

That is the key optimization connection.

* * *

**1.5.3 Normal cone: the set of all supporting directions**
===========================================================

At a point  $x_0\in C$ , there may be many supporting hyperplanes (think of a polytope vertex). We package them as a cone.

### Definition (normal cone)

The **normal cone** of a convex set  $C$  at  $x_0\in C$  is

$$
\boxed{ N_C(x_0) := \{a\in\mathbb{R}^n : a^\top(x - x_0) \le 0\ \forall x\in C\}. }
$$

Interpretation:

*   vectors  $a$  that form nonacute angles with every feasible direction from  $x_0$  into  $C$ 
*   exactly the normals of supporting hyperplanes at  $x_0$ 

**Immediate facts you should be able to prove:**

1.   $N_C(x_0)$  is a cone: if  $a\in N_C(x_0)$ , then  $\alpha a\in N_C(x_0)$  for  $\alpha\ge0$ .
2.   $0\in N_C(x_0)$  always.
3.  If  $x_0$  is in the **interior** of  $C$ , then  $N_C(x_0)=\{0\}$ .  
    (No nontrivial supporting hyperplane exists inside—only on boundary.)

We’ll prove (3) precisely later in this section.

* * *

**1.5.4 The supporting hyperplane theorem (core statement)**
============================================================

There are multiple versions. The most commonly used in convex optimization is:

> **Theorem (supporting hyperplane theorem — common form)**  
> Let  $C\subseteq\mathbb{R}^n$  be a nonempty **closed convex** set.  
> For any boundary point  $x_0\in\partial C$ , there exists a nonzero vector  $a\neq 0$  such that

$$
a^\top x \le a^\top x_0 \quad \forall x\in C.
$$

Equivalently: there exists a supporting hyperplane to  $C$  at  $x_0$ .

This theorem is profound: it says convex sets always have a “flat” linear witness touching them at any boundary point (under mild closure assumptions). Without convexity, this is false.

Now: proving this theorem in full generality usually uses separation theorems (Hahn–Banach style). That’s a bit heavy for Phase 1, but we can still do a complete proof in a way that’s faithful and self-contained for  $\mathbb{R}^n$ , using projection and first principles.

* * *

**1.5.5 Projection-based proof of supporting hyperplane theorem (finite-dimensional, constructive)**
====================================================================================================

We’ll prove a standard version:

> If  $C$  is nonempty, closed, convex and  $x_0\in\partial C$ , then there exists a supporting hyperplane at  $x_0$ .

### Step 0: Why “closed” matters

Closedness ensures nearest points exist (projection). In  $\mathbb{R}^n$ , closed + convex gives well-defined projections.

### Step 1: Move slightly outside the set

Because  $x_0$  is a boundary point, every neighborhood of  $x_0$  contains points not in  $C$ . So we can pick a point  $y\notin C$  very close to  $x_0$ .

Formally: choose  $y\notin C$ .

### Step 2: Project  $y$  onto  $C$ 

Define:

$$
x^* := \Pi_C(y) := \arg\min_{x\in C}\|x-y\|_2.
$$

Because  $C$  is nonempty, closed, convex,  $x^*$  exists and is unique.

We’ll now prove the **projection optimality condition**:

$$
\boxed{ (y-x^*)^\top (x-x^*) \le 0 \quad \forall x\in C. }
$$

This condition will produce the supporting hyperplane.

* * *

Proof of the projection optimality condition (no gaps)
------------------------------------------------------

Let  $x^*$  minimize  $f(x)=\|x-y\|_2^2$  over  $x\in C$ .

Take any  $x\in C$ . Because  $C$  is convex, for any  $\theta\in[0,1]$ ,

$$
x(\theta) := x^* + \theta(x-x^*) \in C.
$$

Define the one-variable function:

$$
\phi(\theta) := \|x(\theta)-y\|_2^2 = \|x^* + \theta(x-x^*) - y\|_2^2.
$$

Since  $x^*$  is optimal,  $\theta=0$  is a minimizer of  $\phi(\theta)$  over  $[0,1]$ . Therefore the right derivative at 0 must be nonnegative:

$$
\phi'(0^+) \ge 0.
$$

Now expand  $\phi$ . Let  $d := x-x^*$ . Then:

$$
x(\theta)-y = (x^*-y) + \theta d.
$$

So

$$
\phi(\theta) = \|(x^*-y) + \theta d\|_2^2 = \langle (x^*-y) + \theta d,\ (x^*-y) + \theta d\rangle.
$$

Expand using bilinearity of inner product:

$$
\phi(\theta) = \|x^*-y\|_2^2 + 2\theta (x^*-y)^\top d + \theta^2\|d\|_2^2.
$$

Differentiate:

$$
\phi'(\theta) = 2(x^*-y)^\top d + 2\theta\|d\|_2^2.
$$

Thus:

$$
\phi'(0) = 2(x^*-y)^\top d.
$$

The optimality condition  $\phi'(0^+)\ge0$  gives:

$$
2(x^*-y)^\top (x-x^*) \ge 0 \quad \Longleftrightarrow \quad (y-x^*)^\top (x-x^*) \le 0.
$$

Since  $x\in C$  was arbitrary, we have:

$$
\boxed{ (y-x^*)^\top (x-x^*) \le 0 \quad \forall x\in C. }
$$

∎

* * *

### Step 3: The inequality defines a supporting halfspace

Let

$$
a := y-x^*.
$$

Since  $y\notin C$ , the projection  $x^*\neq y$ , so  $a\neq0$ .

The projection inequality becomes:

$$
a^\top (x-x^*) \le 0 \quad \forall x\in C
$$

equivalently

$$
a^\top x \le a^\top x^* \quad \forall x\in C.
$$

This says exactly: the halfspace

$$
\{x: a^\top x \le a^\top x^*\}
$$

contains  $C$ , and the boundary hyperplane

$$
\{x: a^\top x = a^\top x^*\}
$$

passes through  $x^*$ .

So this hyperplane supports  $C$  at  $x^*$ .

* * *

### Step 4: Why is  $x^*$  a boundary point?

Because  $y\notin C$  and  $x^*$  is the closest point in  $C$ . If  $x^*$  were interior, you could move slightly from  $x^*$  toward  $y$  and remain in  $C$ , contradicting minimality.

So  $x^*\in\partial C$ .

* * *

### Step 5: How do we get support at a specific boundary point  $x_0$ ?

We want a supporting hyperplane at **the given** boundary point  $x_0$ . To do that, take a sequence of points  $y_k\notin C$  approaching  $x_0$ , project each  $y_k$  onto  $C$ , get boundary points  $x^*_k$  and supporting normals  $a_k=y_k-x^*_k$ . Under mild compactness/normalization, take a limit direction to produce a supporting hyperplane at  $x_0$ .

This is the standard finite-dimensional argument. The key idea: supporting hyperplanes emerge from projections of nearby external points.

(Full technical limit argument can be done; it’s somewhat lengthy, but the main constructive mechanism is what you just proved: **projections generate supporting hyperplanes**.)

* * *

**1.5.6 Interior points have no nontrivial support**
====================================================

> **Proposition:** If  $x_0\in\mathrm{int}(C)$ , then  $N_C(x_0)=\{0\}$ . Equivalently, there is no supporting hyperplane at an interior point.

### Proof (explicit)

Assume  $x_0\in\mathrm{int}(C)$ . Then there exists  $\epsilon>0$  such that the ball

$$
B(x_0,\epsilon) := \{x : \|x-x_0\|_2 < \epsilon\}
$$

is contained in  $C$ .

Take any  $a\in N_C(x_0)$ . By definition:

$$
a^\top(x-x_0)\le 0\quad \forall x\in C.
$$

In particular, this holds for all  $x\in B(x_0,\epsilon)$ .

Pick  $x = x_0 + t a$  for small  $t>0$ . For sufficiently small  $t$ ,  $x\in B(x_0,\epsilon)\subseteq C$ . Then:

$$
a^\top(x-x_0) = a^\top(t a) = t\|a\|_2^2 \le 0.
$$

Since  $t>0$ , this implies  $\|a\|_2^2 \le 0$ , hence  $a=0$ .

So  $N_C(x_0)=\{0\}$ . ∎

This is important later: nonzero normals and nontrivial KKT multipliers only arise on the boundary (active constraints).

* * *

**1.5.7 Supporting hyperplanes and linear optimization over convex sets**
=========================================================================

Supporting hyperplanes are the natural dual object to linear objectives.

Consider maximizing a linear functional over a convex set:

$$
\max_{x\in C} a^\top x.
$$

If  $x^*$  is optimal, then

$$
a^\top x \le a^\top x^* \quad \forall x\in C.
$$

But that inequality is exactly the definition of a supporting hyperplane with normal  $a$  at  $x^*$ .

So:

$$
\boxed{\text{Optimal points of linear objectives are exactly supporting points.}}
$$

This is why:

*   LP optima occur at faces/extreme points,
*   dual variables are normals,
*   separation becomes certificates.

* * *

**1.5.8 Faces, exposed faces, and extreme points (geometry of “where optima live”)**
====================================================================================

Supporting hyperplanes carve out “flat pieces” of convex sets.

### Definition (face)

A subset  $F\subseteq C$  is a **face** of  $C$  if:

*    $F$  is convex,
*   and whenever a segment inside  $C$  has an interior point in  $F$ , then the whole segment lies in  $F$ .

More operationally: if  $x=\theta y+(1-\theta)z\in F$  with  $y,z\in C$  and  $\theta\in(0,1)$ , then  $y,z\in F$ .

### Definition (exposed face)

An **exposed face** is the set of maximizers of some linear functional:

$$
F = \arg\max_{x\in C} a^\top x = \{x\in C : a^\top x = \sup_{z\in C} a^\top z\}.
$$

Exposed faces are exactly the intersections of  $C$  with a supporting hyperplane.

### Extreme points

An **extreme point** is a point that is not a nontrivial convex combination of two distinct points of  $C$ . Extreme points are 0-dimensional faces.

In polytopes:

*   vertices are extreme points,
*   supporting hyperplanes touch along faces.

This will matter later for LP and duality intuition.

* * *

**1.5.9 Supporting hyperplanes for convex functions via epigraphs (the bridge to subgradients)**
================================================================================================

This is the single most important conceptual bridge.

Given a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ , define its epigraph:

$$
\mathrm{epi}(f) := \{(x,t)\in\mathbb{R}^{n+1}: f(x)\le t\}.
$$

We already know:

$$
f \text{ convex } \iff \mathrm{epi}(f) \text{ convex}.
$$

Now: a supporting hyperplane to the epigraph at  $(x_0,f(x_0))$  corresponds to a linear inequality of the form:

$$
f(x) \ge f(x_0) + g^\top(x-x_0)
$$

for some  $g$ . That  $g$  is a **subgradient**.

So:

$$
\boxed{\text{Supporting hyperplanes to epigraphs} \iff \text{subgradients}.}
$$

This is why subgradients are not “definitions pulled from nowhere”; they are geometric objects.

We will do the full derivation later in Phase 2, but you should already see the inevitability.

* * *

**1.5.10 Separation theorem (preview): why convex sets can be certified apart**
===============================================================================

Supporting hyperplanes are a “one-set” touching phenomenon. Separation is a “two-set” phenomenon:

*   If a point lies outside a closed convex set, there exists a hyperplane separating them.
*   If two disjoint convex sets satisfy mild conditions, there exists a hyperplane separating them.

These statements are the geometric engine behind:

*   infeasibility certificates,
*   duality (weak and strong),
*   Farkas’ lemma,
*   KKT multipliers as separating normals.

We will prove separation theorems later, but supporting hyperplanes are the local form of that global idea.

* * *

**1.5.11 The exact “takeaway machinery” (what you must be able to reproduce)**
==============================================================================

You should be able to do these from memory:

1.  Definition of supporting hyperplane at a point:
    
$$
a^\top x \le a^\top x_0\ \forall x\in C.
$$
2.  Normal cone definition:
    
$$
N_C(x_0)=\{a: a^\top(x-x_0)\le0\ \forall x\in C\}.
$$
3.  Projection optimality condition (and its proof):
    
$$
(y-x^*)^\top(x-x^*)\le0\ \forall x\in C.
$$
4.  Interpret linear optimization optima as support points:
    
$$
x^*\in\arg\max_{x\in C} a^\top x \iff a \in N_C(x^*).
$$
5.  Interior points have only the zero normal.

These are the “core lemma pack” items that power everything later.

* * *

**1.5.12 Typical failure modes**
================================

1.  Confusing “tangent” (smooth boundary concept) with “supporting” (works without smoothness).  
    Supporting hyperplanes exist even at corners.
2.  Forgetting convexity/closedness assumptions.  
    Without convexity, support can fail; without closedness, projection may fail.
3.  Thinking supporting hyperplanes are unique.  
    At a smooth boundary point, typically unique normal; at a corner, many supporting hyperplanes.
4.  Treating normals as unit vectors.  
    Scaling  $a$  does not change the hyperplane—only direction matters.

* * *

Roadmap position
----------------

You now have the geometric mechanism that later becomes:

*   first-order optimality,
*   subgradients,
*   KKT,
*   duality and certificates.

Next, depending on our roadmap flow, we typically move to:

*   **Phase 2: convex functions** (epigraphs, subgradients, first-order conditions)  
    or
*   additional convex set machinery (separation theorems, projections).

Either way, supporting hyperplanes are now in your toolkit as a precise, proven object—not a slogan.

## Response:
Phase 1 is **not yet completely done** relative to the roadmap you pasted.

What we have fully covered (at the “gold standard” depth):

*   **1.1** convex combinations ✅
*   **1.2** convex sets + convex hull idea ✅
*   **1.4** canonical zoo focus on **cones + big three cones** ✅
*   **1.5 core lemma (“norm balls are convex”)** ✅ (we proved it from triangle inequality + homogeneity in 0.4, which is exactly what 1.5 asks)

What is still missing as a dedicated, fully formal subsection in **Phase 1**:

*   **1.3 Closure rules (legal moves)** — especially with explicit proofs of:
    *   intersection
    *   affine images and affine preimages
    *   Cartesian products
    *   Minkowski sums

So we finish Phase 1 by doing **1.3** now. After that, Phase 1 is truly complete, and we proceed to **Phase 2.1** next message.

* * *

**1.3 — Closure rules (the legal moves of convexity)**
------------------------------------------------------

_(zero-to-hero, complete, rigorous, and operational for modeling)_

This is the “compiler manual” for convex optimization.

In PS6-style modeling, you rarely prove convexity by starting from the definition every time. Instead you do:

> Recognize a set as being built from known convex sets using operations that preserve convexity.

These operations are the **closure rules**. They are your “legal moves.”

We’ll do each move with: (i) statement, (ii) proof from first principles, (iii) modeling interpretation.

Throughout, a set  $C\subseteq \mathbb{R}^n$  is **convex** iff

$$
x,y\in C,\ \theta\in[0,1]\ \Rightarrow\ \theta x+(1-\theta)y\in C.
$$

* * *

### **1.3.1 Intersection preserves convexity**

#### Statement

If  $\{C_i\}_{i\in I}$  is any family of convex sets in  $\mathbb{R}^n$  (finite or infinite), then

$$
C := \bigcap_{i\in I} C_i
$$

is convex.

#### Proof (no steps skipped)

Take any  $x,y\in C$ . By definition of intersection, that means:

$$
x\in C_i\ \text{and}\ y\in C_i\quad \forall i\in I.
$$

Because each  $C_i$  is convex, for any  $\theta\in[0,1]$ ,

$$
\theta x+(1-\theta)y \in C_i\quad \forall i\in I.
$$

If a point is in every  $C_i$ , then it is in the intersection. Hence:

$$
\theta x+(1-\theta)y \in \bigcap_{i\in I} C_i = C.
$$

So  $C$  is convex. ∎

#### Modeling meaning

Every time you write multiple constraints, you are taking an intersection:

$$
\{x: f_1(x)\le 0,\ f_2(x)\le 0,\ Ax=b\} = \{x:f_1(x)\le0\}\cap\{x:f_2(x)\le0\}\cap\{x:Ax=b\}.
$$

So convex feasibility is stable under “adding more convex constraints.”

* * *

### **1.3.2 Affine images preserve convexity**

#### Setup: affine map

An affine map is

$$
f(x) = Ax+b
$$

with  $A\in\mathbb{R}^{m\times n}$ ,  $b\in\mathbb{R}^m$ .

#### Statement

If  $C\subseteq\mathbb{R}^n$  is convex, then its **image**

$$
f(C) := \{Ax+b : x\in C\}\subseteq \mathbb{R}^m
$$

is convex.

#### Proof

Take any two points  $u,v\in f(C)$ . By definition of image, there exist  $x,y\in C$  such that:

$$
u=Ax+b,\qquad v=Ay+b.
$$

Take any  $\theta\in[0,1]$ . Consider the convex combination:

$$
\theta u+(1-\theta)v = \theta(Ax+b) + (1-\theta)(Ay+b).
$$

Distribute terms:

$$
= \theta Ax + \theta b + (1-\theta)Ay + (1-\theta)b = A(\theta x+(1-\theta)y) + b.
$$

Since  $C$  is convex,  $\theta x+(1-\theta)y \in C$ . Call this point  $z\in C$ .  
Then

$$
\theta u+(1-\theta)v = Az+b \in f(C).
$$

So  $f(C)$  is convex. ∎

#### Modeling meaning

*   Taking linear measurements of feasible points (e.g., outputs  $y=Ax$ ) preserves convexity.
*   “Change of coordinates” via affine maps does not break convex geometry.

* * *

### **1.3.3 Affine preimages preserve convexity (this is the workhorse)**

This is the rule you use **every time** you write a constraint in the form “something affine belongs to something convex.”

#### Statement

If  $D\subseteq\mathbb{R}^m$  is convex and  $f(x)=Ax+b$  is affine, then the **preimage**

$$
f^{-1}(D) := \{x\in\mathbb{R}^n : Ax+b \in D\}
$$

is convex.

#### Proof

Take any  $x,y\in f^{-1}(D)$ . That means:

$$
Ax+b\in D,\qquad Ay+b\in D.
$$

Let  $\theta\in[0,1]$  and define  $z=\theta x+(1-\theta)y$ .  
Compute  $f(z)$ :

$$
f(z)=Az+b = A(\theta x+(1-\theta)y)+b = \theta(Ax+b) + (1-\theta)(Ay+b).
$$

Since  $Ax+b$  and  $Ay+b$  are in  $D$ , and  $D$  is convex, their convex combination is in  $D$ . Therefore:

$$
f(z)\in D \quad \Rightarrow \quad z\in f^{-1}(D).
$$

So  $f^{-1}(D)$  is convex. ∎

#### Modeling meaning (the universal template)

Almost all convex constraints are of this form:

*   Linear inequality  $a^\top x \le b$  is
    $$
    a^\top x \in (-\infty,b]
    $$
    where  $(-\infty,b]$  is convex in  $\mathbb{R}$ .
*   Norm constraint  $\|Ax-c\|_2 \le t$  is
    $$
    (t,Ax-c)\in \mathcal{Q}
    $$
    (SOC cone), a convex set.
*   SDP constraint  $A_0+\sum x_iA_i \succeq 0$  is
    $$
    A_0+\sum x_iA_i \in \mathbb{S}^n_+,
    $$
    the PSD cone, convex.

This rule is the reason conic programming works.

* * *

### **1.3.4 Cartesian products preserve convexity**

#### Definition

For sets  $C\subseteq\mathbb{R}^n$ ,  $D\subseteq\mathbb{R}^m$ ,

$$
C\times D := \{(x,y)\in\mathbb{R}^{n+m}: x\in C,\ y\in D\}.
$$

#### Statement

If  $C$  and  $D$  are convex, then  $C\times D$  is convex.

#### Proof

Take  $(x_1,y_1),(x_2,y_2)\in C\times D$ . Then:

$$
x_1,x_2\in C,\qquad y_1,y_2\in D.
$$

For  $\theta\in[0,1]$ ,

$$
\theta(x_1,y_1) + (1-\theta)(x_2,y_2) = (\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2).
$$

Because  $C$  is convex,  $\theta x_1+(1-\theta)x_2\in C$ .  
Because  $D$  is convex,  $\theta y_1+(1-\theta)y_2\in D$ .  
Therefore the pair lies in  $C\times D$ . ∎

#### Modeling meaning

This is why “stacking variables” is safe:

*   epigraphs live in  $\mathbb{R}^{n+1}$ ,
*   slack variables enlarge the space,
*   product constraints remain convex when each component constraint is convex.

* * *

### **1.3.5 Minkowski sum preserves convexity**

#### Definition (Minkowski sum)

For sets  $C,D\subseteq\mathbb{R}^n$ ,

$$
C + D := \{c+d : c\in C,\ d\in D\}.
$$

#### Statement

If  $C$  and  $D$  are convex, then  $C+D$  is convex.

#### Proof

Take any two points  $u,v\in C+D$ . By definition, there exist:

$$
u=c_1+d_1,\quad v=c_2+d_2
$$

with  $c_1,c_2\in C$  and  $d_1,d_2\in D$ .

Let  $\theta\in[0,1]$ . Consider

$$
\theta u+(1-\theta)v = \theta(c_1+d_1) + (1-\theta)(c_2+d_2).
$$

Group terms:

$$
= (\theta c_1+(1-\theta)c_2) + (\theta d_1+(1-\theta)d_2).
$$

Since  $C$  is convex,  $\theta c_1+(1-\theta)c_2 \in C$ .  
Since  $D$  is convex,  $\theta d_1+(1-\theta)d_2 \in D$ .  
Therefore their sum is in  $C+D$ . ∎

#### Modeling meaning

Minkowski sums encode:

*   adding disturbances/uncertainty sets,
*   reachable sets under additive noise,
*   “nominal + error” decompositions.

In robust optimization you constantly see uncertainty sets written as:

$$
\bar a + P\mathbb{B}
$$

which is literally a Minkowski sum (translate of a set).

* * *

### **1.3.6 Two closure rules you’ll use constantly (bonus but essential)**

These are so common that they’re practically part of the “basic instruction set.”

#### (i) Translation preserves convexity

If  $C$  is convex and  $b\in\mathbb{R}^n$ , then

$$
C+b := \{x+b : x\in C\}
$$

is convex.

Proof: it’s an affine image with  $A=I$ .

#### (ii) Scaling by  $\alpha\ge0$  preserves convexity

If  $C$  is convex and  $\alpha\ge0$ , then

$$
\alpha C := \{\alpha x : x\in C\}
$$

is convex.

Proof: also an affine image (linear map).

These are used implicitly everywhere.

* * *

**Phase 1 completion check (after this subsection)**
----------------------------------------------------

Now Phase 1 contains exactly what the roadmap requires:

*   1.1 ✅
*   1.2 ✅
*   1.3 ✅ (just completed rigorously)
*   1.4 ✅
*   1.5 ✅ (norm ball convexity already proved from norm axioms)

So **Phase 1 is now complete**.

Next message: we proceed to **Phase 2.1 — Convex functions (definition + domain convexity necessity)**, keeping the same depth and rigor.

## Response:
**2.1 — Convex functions (definition, domain, geometry, and why this is the “safe objective/constraint” class)**
----------------------------------------------------------------------------------------------------------------

Phase 1 was about the geometry of _feasible sets_: convexity as “closed under mixing.”  
Phase 2 is the geometry of _costs_: which functions behave well under minimization, and why.

The single most important idea in convex optimization is:

> Convexity is not “smoothness.”  
> Convexity is “your graph lies below every chord,” equivalently “your epigraph is a convex set,” equivalently “every tangent underestimates,” equivalently “Hessian is PSD (if smooth).”

But we start at the root: the definition. Then we unpack it from every angle, including the domain subtleties that people constantly mess up and lose points for (especially in log/GP/fractional problems).

* * *

**2.1.0 What is a function in convex optimization (recall + why it matters now)**
=================================================================================

We work with functions

$$
f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}.
$$

This is not decorative. The  $+\infty$  value is a modeling device:

*   If  $f(x)=+\infty$ , then  $x$  is **illegal** (outside domain).
*   Minimizing  $f$  automatically avoids illegal points.

So we define the **effective domain**:

$$
\mathrm{dom}\,f := \{x\in\mathbb{R}^n: f(x)<+\infty\}.
$$

In convex optimization, “the domain” is not optional. It is part of the mathematical object. This is why “ignoring domains” is a standard failure mode.

* * *

**2.1.1 Definition: convex function (two-point inequality)**
============================================================

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ .

### **Definition (convex function)**

 $f$  is **convex** if:

1.  its domain  $\mathrm{dom}\,f$  is a **convex set**, and
2.  for all  $x,y\in \mathrm{dom}\,f$  and all  $\theta\in[0,1]$ ,
    
$$
\boxed{ f(\theta x+(1-\theta)y)\ \le\ \theta f(x)+(1-\theta)f(y). }
$$

This is the **convexity inequality**.

Read it as:

*   take two legal points  $x,y$ ,
*   take any legal mixture  $z=\theta x+(1-\theta)y$ ,
*   then the function value at the mixture is at most the mixture of the function values.

This is the “below the chord” condition.

* * *

**2.1.2 Why “domain convexity is mandatory” (not a technicality)**
------------------------------------------------------------------

A very common student mistake is to treat the inequality as the whole definition, without separately requiring  $\mathrm{dom}\,f$  to be convex.

But if the domain is not convex, the inequality may be “vacuously true” (you can’t test it on mixtures that leave the domain), and you’d incorrectly call pathological things convex.

### Example (why we require convex domain)

Define

$$
f(x) = \begin{cases} 0, & x\in\{0,1\}\\ +\infty, & \text{otherwise.} \end{cases}
$$

Then  $\mathrm{dom}\,f=\{0,1\}$ , which is **not convex**.

If you try to test the inequality, you can only choose  $x,y\in\{0,1\}$ . For  $\theta=1/2$ , the mixture is  $0.5$ , but  $0.5\notin\mathrm{dom}f$ . So the inequality condition cannot be evaluated on the chord interior (it’s “outside the legal world”). If you didn’t require convex domain, you could accidentally call this convex.

But geometrically, the epigraph is not convex, and minimization over such a “function” is essentially a discrete problem.

So the convex domain condition prevents fake convexity.

* * *

**2.1.3 Geometric meaning: “below the chord” in 1D, “below the secant surface” in nD**
======================================================================================

### 1D intuition (fully explicit)

Take  $n=1$ . Consider  $x<y$ . The line segment between  $(x,f(x))$  and  $(y,f(y))$  is the set of points:

$$
(\theta x+(1-\theta)y,\ \theta f(x)+(1-\theta)f(y)),\quad \theta\in[0,1].
$$

Convexity inequality says:

$$
f(\theta x+(1-\theta)y)\ \le\ \theta f(x)+(1-\theta)f(y).
$$

This means the graph point  $(z,f(z))$  lies **below or on** that chord for every  $z$  between  $x$  and  $y$ .

So in 1D, convexity literally means “graph bends upward” (like a bowl).

### nD geometry

In  $\mathbb{R}^n$ , the inequality is the same, but now the segment is in the input space. The function value at the mixed input is bounded by the mix of values at endpoints. It’s still “below chords,” but the chords are now between points in  $\mathbb{R}^n$ .

* * *

**2.1.4 Strict convexity vs convexity (and why it matters for uniqueness)**
===========================================================================

### Definition (strictly convex)

 $f$  is **strictly convex** if for all distinct  $x\neq y$  in  $\mathrm{dom}f$  and  $\theta\in(0,1)$ ,

$$
\boxed{ f(\theta x+(1-\theta)y)\ <\ \theta f(x)+(1-\theta)f(y). }
$$

Strict convexity implies:

*   the function lies _strictly_ below every chord except at endpoints,
*   minimizers (if they exist) are unique (under mild conditions).

Convex (non-strict) functions can have flat regions and multiple minimizers.

Why PS6 cares: many problems ask you to identify when the solution is unique or when an objective is strictly convex.

* * *

**2.1.5 Equivalent definition using k-point convex combinations**
=================================================================

You learned in Phase 1 that two-point convexity implies  $k$ \-point closure for sets. Same phenomenon happens for functions.

### Theorem (two-point convexity ⇒ finite Jensen form)

If  $f$  is convex, then for any  $x_1,\dots,x_k\in\mathrm{dom}f$  and weights  $\theta_i\ge0$  with  $\sum_i\theta_i=1$ ,

$$
\boxed{ f\!\left(\sum_{i=1}^k \theta_i x_i\right)\ \le\ \sum_{i=1}^k \theta_i f(x_i). }
$$

This is the finite-mixture version of Jensen. We will prove Jensen properly in 2.2, but you should understand the logic now:

*   convexity says “mixing inputs does not increase cost beyond mixing costs.”

This inequality is the core reason convex functions behave well under averaging and expectations.

* * *

**2.1.6 Epigraph preview: convex function ⇔ convex epigraph (why we care later)**
=================================================================================

Define the **epigraph** of  $f$ :

$$
\mathrm{epi}(f) := \{(x,t)\in\mathbb{R}^{n+1} : f(x)\le t\}.
$$

Key equivalence (we prove in 2.3):

$$
\boxed{ f \text{ convex } \iff \mathrm{epi}(f) \text{ convex}. }
$$

This matters because optimization problems “minimize  $f(x)$ ” can be rewritten as:

$$
\min_{x,t}\ t \quad \text{s.t.}\quad (x,t)\in\mathrm{epi}(f).
$$

That’s the modeling superpower: objectives become constraints on epigraphs.

But for now: remember that convexity of functions is fundamentally a _set convexity_ statement in one higher dimension.

* * *

**2.1.7 Sublevel sets: convex function ⇒ convex sublevel sets**
===============================================================

Even before epigraphs, there is a crucial easy consequence.

For  $\alpha\in\mathbb{R}$ , define the **sublevel set**:

$$
S_\alpha := \{x\in\mathrm{dom}f : f(x)\le \alpha\}.
$$

### Proposition

If  $f$  is convex, then every  $S_\alpha$  is convex.

#### Proof

Take  $x,y\in S_\alpha$ . Then  $f(x)\le\alpha$  and  $f(y)\le\alpha$ . For  $\theta\in[0,1]$ , convexity gives:

$$
f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y) \le \theta\alpha+(1-\theta)\alpha =\alpha.
$$

So  $\theta x+(1-\theta)y\in S_\alpha$ . ∎

This is a key pipeline later:

*   convex objective ⇒ convex sublevel sets ⇒ nice geometry for minimization.
*   quasiconvexity will be defined by convexity of sublevel sets even when  $f$  itself is not convex.

* * *

**2.1.8 Why convex functions are “safe” to minimize (global optimality property)**
==================================================================================

Here is the central reason convex optimization exists:

> For a convex function on a convex domain, every local minimum is a global minimum.

This is so important that we prove it now, directly from the definition.

### Theorem (local min ⇒ global min for convex functions)

Let  $f$  be convex and  $x^\star\in\mathrm{dom}f$ . If  $x^\star$  is a **local minimizer**, then it is a **global minimizer**:

$$
f(x^\star)\le f(x)\quad \forall x\in\mathrm{dom}f.
$$

#### Proof (from first principles)

Assume  $x^\star$  is a local minimizer. So there exists  $r>0$  such that

$$
f(x^\star)\le f(x)\quad \forall x\in\mathrm{dom}f \cap B(x^\star,r).
$$

Take any arbitrary  $x\in\mathrm{dom}f$ . If  $x=x^\star$ , done. Assume  $x\neq x^\star$ .

Because  $\mathrm{dom}f$  is convex, for any  $\theta\in[0,1]$ ,

$$
x_\theta := \theta x + (1-\theta)x^\star \in \mathrm{dom}f.
$$

Now choose  $\theta$  small enough so that  $x_\theta$  lies inside the ball  $B(x^\star,r)$ . This is always possible because:

$$
x_\theta - x^\star = \theta(x-x^\star),
$$

so

$$
\|x_\theta-x^\star\|_2 = \theta\|x-x^\star\|_2.
$$

Pick

$$
\theta \le \frac{r}{\|x-x^\star\|_2}.
$$

Then  $\|x_\theta-x^\star\|_2\le r$ , hence  $x_\theta\in B(x^\star,r)$ .

By local minimality:

$$
f(x^\star)\le f(x_\theta).
$$

By convexity:

$$
f(x_\theta) = f(\theta x + (1-\theta)x^\star) \le \theta f(x) + (1-\theta)f(x^\star).
$$

Combine:

$$
f(x^\star)\le \theta f(x) + (1-\theta)f(x^\star).
$$

Subtract  $(1-\theta)f(x^\star)$  from both sides:

$$
\theta f(x^\star)\le \theta f(x).
$$

Since  $\theta>0$ , divide by  $\theta$ :

$$
f(x^\star)\le f(x).
$$

Because  $x$  was arbitrary,  $x^\star$  is global minimizer. ∎

This proof is the heart of “convex = no bad local minima.”

* * *

**2.1.9 Convexity is not smoothness (and not “bowl-shaped” in a naive sense)**
==============================================================================

Common misconceptions:

1.  **Smoothness ≠ convexity**  
    A function can be smooth and nonconvex:  $f(x)=\sin x$ .
2.  **Nonsmooth ≠ nonconvex**  
     $|x|$  is convex but not differentiable at 0.
3.  **“Looks like a bowl” is not a proof**  
    Convexity requires either:
    *   definition-based inequality,
*   epigraph convexity,
*   first-order test (if differentiable),
*   Hessian PSD (if twice differentiable),
*   composition rules with certified atoms.

We will build these certification tools across 2.3–2.9.

* * *

**2.1.10 A “verification checklist” at definition-level (what you can already do)**
===================================================================================

Right now, before any calculus tools, you can already verify convexity by:

*   checking domain is convex,
*   verifying the convexity inequality,
*   or recognizing the function as:
    *   supremum of affine functions,
    *   norm,
    *   nonnegative sum of known convex functions,
    *   affine precomposition of a convex function.

We will formalize these later; for now, you should interpret convexity as “safe under mixing.”

* * *

**2.1.11 Mini-library (tiny but foundational examples)**
========================================================

These are “convexity atoms” you should know cold.

### (A) Affine functions are convex

Let  $f(x)=a^\top x + b$ . Then

$$
f(\theta x+(1-\theta)y) = a^\top(\theta x+(1-\theta)y)+b = \theta(a^\top x+b) + (1-\theta)(a^\top y+b) = \theta f(x)+(1-\theta)f(y).
$$

So affine functions satisfy the inequality with equality. Hence convex (and concave).

### (B) Norms are convex functions

We proved norm balls convex earlier; the function convexity is:

$$
\| \theta x+(1-\theta)y\| \le \theta\|x\|+(1-\theta)\|y\|,
$$

which is exactly triangle inequality + homogeneity. So norms are convex.

### (C) Quadratic form with PSD matrix is convex

If  $f(x)=x^\top Q x$  with  $Q\succeq 0$ , then  $f$  is convex. (We’ll prove rigorously using Hessian in 2.6, but you should already recognize this as a core atom.)

* * *

**2.1.12 What this unlocks for PS6 (immediate relevance)**
==========================================================

Many PS6 transformations depend on “is this objective/constraint function convex?”

*   log barrier (Ex 4.2): show  $-\log$  composed with affine is convex on its domain.
*   Huber (Ex 4.5): piecewise convex function; epigraph gives QP.
*   fractional/quasiconvex (Ex 4.7): convexity vs quasiconvexity is about sublevel sets.
*   GP (Ex 4.25): log-sum-exp structure is convex.

All of those rely on understanding convexity at the definition level so you don’t accidentally assume something illegal.

* * *

Roadmap position
----------------

We have completed **2.1**: definition + domain + geometry + “local = global” theorem (proved from first principles) + key consequences (sublevel sets convex).

Next is **2.2 — Jensen’s inequality** (finite mixtures first, then expectation intuition). That will formalize the multi-point convex combination inequality and become a reusable proof tool across the course.

## Response:
**2.2 — Jensen’s inequality (finite mixtures → expectation form → why it is the “engine of convexity”)**
--------------------------------------------------------------------------------------------------------

Jensen’s inequality is not a random theorem you memorize. It is the **operational meaning** of convexity:

> A convex function turns _averaging in the input_ into _no more than averaging in the output_.

This is exactly the “mixing principle” again, but now for **functions** rather than sets.

In convex optimization, Jensen’s inequality is everywhere:

*   proving convexity of expectations and risk measures,
*   bounding objectives and designing relaxations,
*   proving log-sum-exp convexity,
*   deriving entropy inequalities,
*   robust optimization (expected vs worst case),
*   and (later) interpreting dual variables as supporting objects.

We will build Jensen from the definition of convexity, in layers:

1.  **finite (discrete) Jensen** for a convex combination of finitely many points,
2.  **random-variable Jensen** (expectation form),
3.  careful treatment of conditions (integrability, domain, extended values),
4.  equality conditions (when Jensen is tight),
5.  common corollaries that become modeling “reflexes.”

We proceed with maximal rigor and explicitness.

* * *

**2.2.0 Preliminaries: what “average” means mathematically**
============================================================

There are two kinds of “averaging” we care about:

### (A) Finite averaging (convex combination)

Choose points  $x_1,\dots,x_k \in \mathbb{R}^n$  and weights  $\theta_1,\dots,\theta_k$  such that:

$$
\theta_i \ge 0,\qquad \sum_{i=1}^k \theta_i = 1.
$$

Then the weighted average is:

$$
\bar x := \sum_{i=1}^k \theta_i x_i.
$$

### (B) Probabilistic averaging (expectation)

Let  $X$  be a random vector in  $\mathbb{R}^n$ . Then its “average” is:

$$
\mathbb{E}[X],
$$

provided it exists (we must be careful here).

Finite averaging is just expectation under a discrete distribution:

$$
\mathbb{P}(X=x_i) = \theta_i.
$$

So the finite case is the foundational case.

* * *

**2.2.1 Statement: Jensen’s inequality (finite / discrete version)**
====================================================================

Let  $f:\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}$  be **convex** with **convex domain**  $\mathrm{dom} f$ .

Take points  $x_1,\dots,x_k \in \mathrm{dom}f$  and weights  $\theta_i\ge 0$  with  $\sum\theta_i=1$ . Then:

$$
\boxed{ f\!\left(\sum_{i=1}^k \theta_i x_i\right) \ \le\ \sum_{i=1}^k \theta_i f(x_i). }
$$

Interpretation in plain words:

*   evaluate  $f$  at the average input,
*   it is no more than the average of  $f$  values.

For concave functions, the inequality reverses.

* * *

**2.2.2 Proof of finite Jensen (from first principles, step-by-step)**
======================================================================

We will prove it using induction, because convexity is defined only for mixing **two** points (2.1), and Jensen is about mixing **many** points.

### Step 0: What exactly we must show

We must show: for all  $k\ge 2$ , for all points and weights as above, the inequality holds.

### Step 1: Base case  $k=2$ 

For  $k=2$ , weights are  $\theta_1=\theta$ ,  $\theta_2=1-\theta$ , and Jensen becomes:

$$
f(\theta x_1 + (1-\theta)x_2) \le \theta f(x_1) + (1-\theta) f(x_2),
$$

which is exactly the definition of convexity. So base case holds.

### Step 2: Inductive hypothesis

Assume Jensen holds for  $k-1$  points. That is, assume:

For any  $x_1,\dots,x_{k-1}\in\mathrm{dom}f$  and weights  $\alpha_i\ge0$  with  $\sum_{i=1}^{k-1}\alpha_i=1$ ,

$$
f\!\left(\sum_{i=1}^{k-1}\alpha_i x_i\right) \le \sum_{i=1}^{k-1}\alpha_i f(x_i).
$$

We want to prove Jensen for  $k$  points.

### Step 3: Separate the last weight

Take weights  $\theta_1,\dots,\theta_k$ ,  $\theta_i\ge0$ ,  $\sum\theta_i=1$ .

If  $\theta_k=1$ , then all other weights are 0 and the inequality is equality:

$$
f(x_k) \le f(x_k).
$$

So assume  $\theta_k \in [0,1)$ . Then  $1-\theta_k>0$ .

Define normalized weights for the first  $k-1$  points:

$$
\alpha_i := \frac{\theta_i}{1-\theta_k}, \quad i=1,\dots,k-1.
$$

Check normalization carefully:

*    $\alpha_i \ge 0$  because  $\theta_i\ge0$  and denominator  $>0$ .
*   Sum:
    
$$
\sum_{i=1}^{k-1}\alpha_i = \sum_{i=1}^{k-1} \frac{\theta_i}{1-\theta_k} = \frac{\sum_{i=1}^{k-1}\theta_i}{1-\theta_k} = \frac{1-\theta_k}{1-\theta_k} = 1.
$$

So  $\{\alpha_i\}$  is a valid convex weight vector.

Now define the partial average:

$$
y := \sum_{i=1}^{k-1} \alpha_i x_i.
$$

Since all  $x_i\in\mathrm{dom}f$  and  $\mathrm{dom}f$  is convex,  $y\in\mathrm{dom}f$ .

### Step 4: Express the full average as a two-point mixture

Compute:

$$
\sum_{i=1}^k \theta_i x_i = \sum_{i=1}^{k-1}\theta_i x_i + \theta_k x_k = (1-\theta_k)\sum_{i=1}^{k-1}\frac{\theta_i}{1-\theta_k} x_i + \theta_k x_k = (1-\theta_k) y + \theta_k x_k.
$$

So the full average is a convex combination of **two** points:  $y$  and  $x_k$ , with weights  $(1-\theta_k)$  and  $\theta_k$ .

### Step 5: Apply convexity (two-point inequality)

By convexity:

$$
f((1-\theta_k) y + \theta_k x_k) \le (1-\theta_k) f(y) + \theta_k f(x_k).
$$

### Step 6: Apply inductive hypothesis to  $f(y)$ 

Since  $y$  is the convex combination of  $x_1,\dots,x_{k-1}$  with weights  $\alpha_i$ , the inductive hypothesis gives:

$$
f(y) = f\!\left(\sum_{i=1}^{k-1}\alpha_i x_i\right) \le \sum_{i=1}^{k-1}\alpha_i f(x_i).
$$

Multiply both sides by  $(1-\theta_k)\ge0$ :

$$
(1-\theta_k)f(y) \le (1-\theta_k)\sum_{i=1}^{k-1}\alpha_i f(x_i).
$$

Now substitute  $\alpha_i = \theta_i/(1-\theta_k)$ :

$$
(1-\theta_k)\sum_{i=1}^{k-1}\alpha_i f(x_i) = (1-\theta_k)\sum_{i=1}^{k-1}\frac{\theta_i}{1-\theta_k} f(x_i) = \sum_{i=1}^{k-1}\theta_i f(x_i).
$$

Thus:

$$
(1-\theta_k)f(y) \le \sum_{i=1}^{k-1}\theta_i f(x_i).
$$

### Step 7: Combine everything

We had:

$$
f((1-\theta_k) y + \theta_k x_k) \le (1-\theta_k) f(y) + \theta_k f(x_k).
$$

Upper bound  $(1-\theta_k)f(y)$  using the previous inequality:

$$
f((1-\theta_k) y + \theta_k x_k) \le \sum_{i=1}^{k-1}\theta_i f(x_i) + \theta_k f(x_k) = \sum_{i=1}^{k}\theta_i f(x_i).
$$

But  $(1-\theta_k) y + \theta_k x_k = \sum_{i=1}^k \theta_i x_i$ . Therefore:

$$
f\!\left(\sum_{i=1}^k\theta_i x_i\right) \le \sum_{i=1}^k\theta_i f(x_i).
$$

That proves Jensen for  $k$ . By induction, it holds for all  $k\ge2$ . ∎

This is a fully constructive proof and is the one you should be able to reproduce cold.

* * *

**2.2.3 Jensen’s inequality in expectation form (random variables)**
====================================================================

Now we translate discrete averaging into probability language.

### Statement (Jensen — expectation form)

Let  $X$  be a random vector in  $\mathbb{R}^n$  such that:

1.   $X \in \mathrm{dom}f$  almost surely (i.e., with probability 1),
2.   $\mathbb{E}[X]$  exists (finite vector),
3.   $\mathbb{E}[|f(X)|]$  exists in an appropriate sense (usually  $\mathbb{E}[f(X)]$  is well-defined, allowing  $+\infty$  is fine but then inequality is trivial).

Then for convex  $f$ ,

$$
\boxed{ f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]. }
$$

### Intuition

*   “apply  $f$  after averaging” is better (smaller) than “average after applying  $f$ .”
*   convex functions penalize dispersion (variance) in the input.

* * *

Why expectation Jensen follows from finite Jensen (conceptual bridge)
---------------------------------------------------------------------

If  $X$  is discrete with values  $x_i$  and probabilities  $\theta_i$ , then:

$$
\mathbb{E}[X] = \sum_i \theta_i x_i,\qquad \mathbb{E}[f(X)] = \sum_i \theta_i f(x_i).
$$

So expectation Jensen is literally finite Jensen.

For general distributions, one proves it by approximation (simple functions) and continuity/closedness arguments. That’s more measure-theoretic, but the discrete case is the core mechanical heart.

Since your course is convex optimization (not measure theory), the discrete + conceptual extension is what you’ll use.

* * *

**2.2.4 Equality conditions: when is Jensen tight?**
====================================================

Understanding when Jensen becomes equality is crucial because it tells you when convexity “matters” and when it doesn’t.

### Key fact (strict convexity gives rigidity)

If  $f$  is **strictly convex**, then in the finite form:

$$
f\!\left(\sum \theta_i x_i\right) = \sum \theta_i f(x_i)
$$

can happen only if all  $x_i$  with positive weight are equal (or all lie in a region where  $f$  is affine).

More precisely:

*   If  $f$  is strictly convex on a convex set containing the points,
*   and  $\theta_i>0$  for at least two distinct points,
*   then Jensen is **strict**:
    $$
    f\!\left(\sum \theta_i x_i\right) < \sum \theta_i f(x_i).
    $$

### Proof idea (not handwavy)

Strict convexity means every nontrivial two-point mixture strictly reduces the chord. The induction proof above becomes strict at the first step where two distinct points are mixed with positive weights. Therefore equality forces “no genuine mixing,” hence all points must coincide (or lie in an affine region of  $f$ ).

In expectation form, if  $f$  is strictly convex and  $X$  is not almost surely constant (has randomness), then:

$$
f(\mathbb{E}[X]) < \mathbb{E}[f(X)].
$$

So convex functions “punish randomness.”

* * *

**2.2.5 Jensen as a variance/dispersal principle (important intuition)**
========================================================================

A convex function grows faster away from its minimum; mixing reduces extremes.

Example:  $f(x)=x^2$  (convex).  
Then Jensen says:

$$
(\mathbb{E}[X])^2 \le \mathbb{E}[X^2].
$$

Rearrange:

$$
\mathbb{E}[X^2] - (\mathbb{E}[X])^2 \ge 0,
$$

which is exactly:

$$
\mathrm{Var}(X) \ge 0.
$$

So Jensen generalizes “variance is nonnegative.”

This is a good mental model:

*   convexity inequality is “generalized nonnegative variance.”

* * *

**2.2.6 Important corollaries you should be able to derive instantly**
======================================================================

These are Jensen in disguise and show up constantly.

### Corollary 1: Average of convex functions is convex

If  $f_i$  are convex and  $\theta_i\ge0$ ,  $\sum\theta_i=1$ , then:

$$
f(x):=\sum_{i=1}^k \theta_i f_i(x)
$$

is convex.

Reason: apply convexity inequality term-by-term and sum with nonnegative weights. (This is essentially Jensen in function space.)

### Corollary 2: Expectation of a convex function is convex in parameters

If  $f(x,\omega)$  is convex in  $x$  for each  $\omega$ , then

$$
F(x):=\mathbb{E}[f(x,\omega)]
$$

is convex (when expectation finite). This underlies stochastic convex optimization.

### Corollary 3: Convexity implies mid-point inequality

Setting  $\theta=1/2$ :

$$
f\!\left(\frac{x+y}{2}\right) \le \frac{f(x)+f(y)}{2}.
$$

This is a weaker condition than full convexity, but in many settings with continuity it characterizes convexity.

### Corollary 4: Convexity implies “function below secants”

For any  $x,y$ , the function on the segment is bounded by the line connecting  $(x,f(x))$  and  $(y,f(y))$ . That’s literally the definition, but operationally you use it to bound intermediate values.

* * *

**2.2.7 How Jensen becomes a modeling move in convex optimization**
===================================================================

Jensen is not only for proofs; it’s a tool for recognizing convex structure.

Typical patterns:

1.  **When you see expectation of a convex function**, you can claim convexity of the objective (under mild conditions).  
    Example: minimize  $\mathbb{E}[\|Ax-b\|_2]$  is convex because norm is convex and expectation preserves convexity.
2.  **When you see log-sum-exp**, Jensen-like reasoning shows convexity (we will do this formally later in 2.8/2.9, but the intuition is “log of average of exponentials” behaves convexly).
3.  **Robust vs average bounds**:  
    Jensen often gives inequalities comparing worst-case and average-case objectives, and helps derive relaxations.

* * *

**2.2.8 Common failure modes (exam/quiz traps)**
================================================

1.  **Forgetting domain conditions**  
    If  $X$  can fall outside  $\mathrm{dom}f$ , Jensen may not even be defined.
2.  **Using Jensen with a concave function in the wrong direction**  
    Concave:  $f(\mathbb{E}X)\ge \mathbb{E}f(X)$ . Convex is the opposite.
3.  **Ignoring integrability**  
    If  $\mathbb{E}[f(X)]$  is  $+\infty$ , inequality holds but is not informative.
4.  **Assuming equality always implies constant**  
    If  $f$  is not strictly convex (has affine regions), equality can occur even when  $X$  is not constant—e.g.  $f(x)=ax+b$  is affine so equality always holds.

* * *

**2.2.9 Checklist (you must be able to do these cold)**
=======================================================

You should be able to:

*   State finite Jensen precisely with weights and domain conditions.
*   Prove it via induction from two-point convexity (the full proof above).
*   Translate finite Jensen into expectation Jensen for discrete distributions.
*   Recall direction reversal for concave functions.
*   Explain equality conditions (strict convexity vs affine regions).
*   Use Jensen to derive  $(\mathbb{E}X)^2 \le \mathbb{E}[X^2]$  and variance nonnegativity.

* * *

Roadmap position
----------------

We have completed **2.2 Jensen’s inequality** in its finite and expectation forms, with full proof and operational consequences.

Next is **2.3 — Epigraphs (the modeling lens):  $f$  convex ⇔  $\mathrm{epi}(f)$  convex**, and we will prove that equivalence carefully in both directions. That is the bridge from “objectives” to “constraints,” and it’s the core modeling move used everywhere in PS6.

## Response:
**2.3 — Epigraphs (the modeling lens):  $f$  convex ⇔  $\mathrm{epi}(f)$  convex**
----------------------------------------------------------------------------------

_(zero-to-hero, fully rigorous, and explicitly tied to modeling patterns you’ll use in PS6)_

If you learn only one “secret weapon” in convex optimization, it should be this:

> **Convex functions are exactly the functions whose epigraphs are convex sets.**

Why is this so powerful?

Because solvers and standard forms understand **constraints defining convex sets** much more directly than they understand arbitrary objectives. The epigraph trick turns:

*   a weird objective
*   into a linear objective with extra variables
*   plus convex constraints.

That is exactly the transformation skill PS6 tests.

We will do the entire theory carefully:

1.  define epigraph/hypograph and why they encode the function,
2.  prove the equivalence  $f$  convex ⇔ epi convex (both directions, no gaps),
3.  show how minimization becomes an epigraph-form problem,
4.  show standard modeling patterns (max, norms, piecewise, absolute values),
5.  discuss domain subtleties and extended-valued functions,
6.  connect epigraphs to supporting hyperplanes and subgradients (bridge to 2.4).

* * *

**2.3.0 First: what problem is epigraphs solving?**
===================================================

Suppose you have:

$$
\min_{x\in\mathbb{R}^n} f(x)
$$

where  $f$  is convex but complicated.

Solvers like linear objectives. They also like constraints in “known convex set” form (halfspaces, SOC, PSD cone, etc.).

Epigraphs let you rewrite:

$$
\min_x f(x) \quad\longleftrightarrow\quad \min_{x,t} t \ \text{s.t.}\ f(x)\le t.
$$

This is the simplest “objective → constraint” conversion. Once  $f(x)\le t$  is expressed in cones/linear inequalities, you’re done.

But to use this safely, you must understand exactly why the epigraph captures convexity.

* * *

**2.3.1 Definitions: epigraph, hypograph, and why the “right direction” matters**
=================================================================================

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  be an extended-valued function.

### **Definition (epigraph)**

$$
\boxed{ \mathrm{epi}(f) := \{(x,t)\in\mathbb{R}^{n+1} : f(x)\le t\}. }
$$

Interpretation:

*   It is the set of points lying **on or above** the graph of  $f$ .
*   Think “epi = above.” (Mnemonic: **E**pi = **E**levated above.)

### **Definition (hypograph)**

$$
\boxed{ \mathrm{hypo}(f) := \{(x,t)\in\mathbb{R}^{n+1} : f(x)\ge t\}. }
$$
*   “hypo = below” (points on or below the graph)

**Important orientation fact:**

*   Convex functions correspond to **convex epigraphs**.
*   Concave functions correspond to **convex hypographs**.

If you flip epi/hypo you flip convex/concave.

* * *

**2.3.2 Epigraphs encode the function completely (not just convexity)**
=======================================================================

A subtle but important point: the epigraph doesn’t just “help prove convexity.”  
It actually contains all information about the function.

### Claim: you can recover  $f(x)$  from  $\mathrm{epi}(f)$ 

For any  $x$ , define:

$$
\phi(x) := \inf\{t : (x,t)\in\mathrm{epi}(f)\}.
$$

Then  $\phi(x)=f(x)$ .

Why?

*    $(x,t)\in\mathrm{epi}(f)$  means  $t\ge f(x)$ .
*   So the set  $\{t:(x,t)\in\mathrm{epi}(f)\}$  is exactly  $[f(x),+\infty)$  if  $x\in\mathrm{dom}f$ , or empty if  $f(x)=+\infty$ .
*   The infimum of  $[f(x),+\infty)$  is  $f(x)$ .

So the epigraph is a set-based representation of the function.

This matters later because convex optimization is “convex sets + affine maps.”

* * *

**2.3.3 Domain encoded in epigraph (extended-valued subtleties)**
=================================================================

If  $f(x)=+\infty$ , then the condition  $f(x)\le t$  is never satisfied for finite  $t$ . So:

*   If  $x\notin\mathrm{dom}f$ , there is **no**  $t\in\mathbb{R}$  such that  $(x,t)\in\mathrm{epi}(f)$ .
*   In other words, epigraph contains points only above legal  $x$ .

Thus:

$$
\mathrm{proj}_x(\mathrm{epi}(f)) = \mathrm{dom}f.
$$

(Projection of epigraph down to the  $x$ \-space is exactly the domain.)

So epigraph convexity automatically implies domain convexity (and this is exactly why domain convexity is “mandatory” in 2.1).

* * *

**2.3.4 The main theorem:  $f$  convex ⇔  $\mathrm{epi}(f)$  convex**
=====================================================================

### Theorem (epigraph characterization of convexity)

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ . Then:

$$
\boxed{ f \text{ is convex} \quad\Longleftrightarrow\quad \mathrm{epi}(f) \text{ is a convex set in }\mathbb{R}^{n+1}. }
$$

We prove both directions carefully.

* * *

**(⇒) If  $f$  is convex, then  $\mathrm{epi}(f)$  is convex**
--------------------------------------------------------------

### What we must prove

Take any two points  $(x_1,t_1)$  and  $(x_2,t_2)$  in  $\mathrm{epi}(f)$ .  
We must show that for any  $\theta\in[0,1]$ , the convex combination

$$
(\bar x,\bar t) := \theta(x_1,t_1)+(1-\theta)(x_2,t_2)
$$

also lies in  $\mathrm{epi}(f)$ . That means we must show:

$$
f(\bar x)\le \bar t.
$$

### Step-by-step proof

Assume  $(x_1,t_1)\in\mathrm{epi}(f)$ . By definition:

$$
f(x_1)\le t_1.
$$

Similarly,  $(x_2,t_2)\in\mathrm{epi}(f)$  implies:

$$
f(x_2)\le t_2.
$$

Now compute the convex combination:

$$
\bar x = \theta x_1 + (1-\theta)x_2, \quad \bar t = \theta t_1 + (1-\theta)t_2.
$$

Because  $f$  is convex, we have:

$$
f(\bar x) = f(\theta x_1+(1-\theta)x_2) \le \theta f(x_1) + (1-\theta)f(x_2).
$$

Now use the inequalities  $f(x_1)\le t_1$  and  $f(x_2)\le t_2$ . Since  $\theta,(1-\theta)\ge0$ , multiplying preserves inequality:

$$
\theta f(x_1) \le \theta t_1,\qquad (1-\theta)f(x_2)\le (1-\theta)t_2.
$$

Add them:

$$
\theta f(x_1)+(1-\theta)f(x_2)\le \theta t_1+(1-\theta)t_2=\bar t.
$$

Combine with the convexity bound:

$$
f(\bar x)\le \theta f(x_1)+(1-\theta)f(x_2)\le \bar t.
$$

Thus  $f(\bar x)\le \bar t$ , so  $(\bar x,\bar t)\in\mathrm{epi}(f)$ . ∎

This direction is conceptually: “below chords ⇒ epi closed under mixing.”

* * *

**(⇐) If  $\mathrm{epi}(f)$  is convex, then  $f$  is convex**
--------------------------------------------------------------

Here we must show the function inequality:

$$
f(\theta x_1+(1-\theta)x_2) \le \theta f(x_1)+(1-\theta)f(x_2).
$$

This time we will choose specific points in the epigraph that lie exactly on the graph.

### Step-by-step proof

Assume  $\mathrm{epi}(f)$  is convex.

Take any  $x_1,x_2\in\mathrm{dom}f$ . (We need them in domain so  $f(x_i)<+\infty$ .)

Then the points  $(x_1,f(x_1))$  and  $(x_2,f(x_2))$  are in the epigraph because:

$$
f(x_1)\le f(x_1),\qquad f(x_2)\le f(x_2).
$$

Since the epigraph is convex, for any  $\theta\in[0,1]$ , the convex combination

$$
(\bar x,\bar t) = \theta(x_1,f(x_1)) + (1-\theta)(x_2,f(x_2)) = (\theta x_1+(1-\theta)x_2,\ \theta f(x_1)+(1-\theta)f(x_2))
$$

must also be in  $\mathrm{epi}(f)$ .

But being in the epigraph means:

$$
f(\bar x)\le \bar t.
$$

Substitute what  $\bar x,\bar t$  are:

$$
f(\theta x_1+(1-\theta)x_2) \le \theta f(x_1)+(1-\theta)f(x_2).
$$

That is exactly convexity. Also, since  $\mathrm{epi}(f)$  convex implies its projection  $\mathrm{dom}f$  is convex (as noted earlier), the domain convexity requirement is automatically satisfied.

Therefore  $f$  is convex. ∎

This direction is conceptually: “epi closed under mixing ⇒ below chords.”

* * *

**2.3.5 Epigraph reformulation of minimization (the modeling move)**
====================================================================

Now we use epigraphs for optimization.

### Proposition (epigraph reformulation)

For any function  $f$  (extended-valued allowed),

$$
\boxed{ \min_{x\in\mathbb{R}^n} f(x) \quad\equiv\quad \min_{(x,t)\in\mathbb{R}^{n+1}} t \ \text{s.t.}\ (x,t)\in\mathrm{epi}(f) }
$$

i.e.

$$
\min_x f(x)\quad\equiv\quad \min_{x,t} t \ \text{s.t.}\ f(x)\le t.
$$

### Proof (complete equivalence, both directions)

Let  $p^\star := \inf_x f(x)$  and let  $q^\star := \inf\{t : \exists x,\ f(x)\le t\}$ .

**(1) Show  $q^\star \le p^\star$ .**  
For any  $x$ , the pair  $(x,f(x))$  is feasible in the epigraph problem (since  $f(x)\le f(x)$ ). The objective value there is  $t=f(x)$ . Therefore the infimum over feasible  $(x,t)$  is at most  $f(x)$ . Since this holds for all  $x$ , it holds for the infimum over  $x$ :

$$
q^\star \le p^\star.
$$

**(2) Show  $p^\star \le q^\star$ .**  
Take any feasible  $(x,t)$  for the epigraph problem. Feasible means  $f(x)\le t$ . Then:

$$
p^\star = \inf_x f(x) \le f(x)\le t.
$$

So  $p^\star$  is a lower bound on every feasible  $t$ . Hence it is a lower bound on the infimum of feasible  $t$ , i.e.:

$$
p^\star \le q^\star.
$$

Combine:  $p^\star=q^\star$ . Also optimal solutions correspond: at optimum you will have  $t=f(x)$  (if  $f(x)$  is finite), because if  $t>f(x)$  you can decrease  $t$  while remaining feasible.

So the problems are equivalent. ∎

### Key modeling consequence

The epigraph form replaces a potentially complicated objective with:

*   **linear objective**  $t$ ,
*   **one constraint**  $f(x)\le t$ .

Everything else becomes: “How do I represent  $f(x)\le t$  in LP/QP/SOCP/SDP form?”

That is PS6.

* * *

**2.3.6 Standard epigraph modeling patterns (the “pattern dictionary” begins here)**
====================================================================================

These are not “tricks.” They are mechanical consequences of how epigraphs behave under operations.

(A) Maximum of functions
------------------------

Let

$$
g(x) := \max_{i=1,\dots,m} f_i(x).
$$

Then:

$$
g(x)\le t \quad\Longleftrightarrow\quad f_i(x)\le t\ \forall i.
$$

So epigraph of max becomes intersection of epigraph constraints:

$$
\mathrm{epi}(g) = \bigcap_{i=1}^m \mathrm{epi}(f_i)
$$

(after embedding properly in  $(x,t)$ \-space).

**Modeling use:** objectives like  $\max_i$  become linear objective with  $t$  and constraints  $f_i(x)\le t$ .

This is used constantly in minimax and robust formulations.

* * *

(B) Absolute value and norms (canonical)
----------------------------------------

For scalar  $u$ ,  $|u|\le t$  is exactly:

$$
-u \le t,\quad u\le t.
$$

For vector  $u$ ,  $\|u\|_2 \le t$  is SOC:

$$
(t,u)\in\mathcal{Q}.
$$

So  $\min \|Ax-b\|_2$  becomes:

$$
\min t\quad \text{s.t.}\ \|Ax-b\|_2\le t,
$$

which is SOCP.

* * *

(C) Piecewise convex penalties (Huber preview)
----------------------------------------------

If  $f(x)=\max\{f_1(x),f_2(x)\}$ , its epigraph is intersection of epigraphs, which is convex if each is convex.

This is exactly why piecewise penalties like Huber can be modeled with auxiliary variables and linear/quadratic constraints.

We’ll do Huber carefully in the exercises phase, but the epigraph idea is the spine.

* * *

**2.3.7 Epigraph convexity → convexity-preserving operations (preview of 2.9)**
===============================================================================

Many convexity rules are easiest as set operations on epigraphs.

For example:

*   If  $f = f_1 + f_2$ , then
    $$
    f(x)\le t \iff \exists t_1,t_2:\ f_1(x)\le t_1,\ f_2(x)\le t_2,\ t_1+t_2\le t.
    $$
    That introduces extra variables and uses intersection + affine constraints (convex-set closure from Phase 1).
*   If  $f(x)=\sup_\alpha f_\alpha(x)$ , then
    $$
    f(x)\le t \iff f_\alpha(x)\le t\ \forall \alpha.
    $$
    Again intersection.

So epigraphs reduce function algebra to set algebra.

* * *

**2.3.8 Domain mistakes: the #1 epigraph pitfall**
==================================================

When you do epigraph modeling, you must not forget:

*   **The constraint  $f(x)\le t$  implicitly includes domain constraints** (because if  $x\notin\mathrm{dom}f$ , then  $f(x)=+\infty$  and cannot be  $\le t$ ).

But in practice, if you represent  $f(x)\le t$  by some explicit cone/inequalities, you must make sure you included the same domain conditions.

Examples:

*    $f(x)=-\log x$  has domain  $x>0$ . The epigraph constraints must enforce  $x>0$  (or  $x\ge \epsilon$  numerically).
*   GP constraints require  $x\in\mathbb{R}^n_{++}$ .
*   Fractional functions require denominators  $>0$ .

Missing these is exactly the “domain failure mode” in your roadmap.

* * *

**2.3.9 Bridge to 2.4 (subgradients): supporting hyperplanes to epigraphs**
===========================================================================

We did supporting hyperplanes in 1.5. Here is the key bridge:

A vector  $g$  is a **subgradient** of  $f$  at  $x_0$  if:

$$
f(x) \ge f(x_0) + g^\top(x-x_0)\quad \forall x.
$$

Geometrically this is a supporting hyperplane to the epigraph at  $(x_0,f(x_0))$ .

So:

*   Phase 1 (supporting hyperplanes to sets)
*   *   epigraphs (functions as sets)
*   ⇒ Phase 2.4 subgradients (supporting hyperplanes to functions)

That’s why subgradients are inevitable and not mystical.

* * *

**2.3.10 What you must be able to do cold (the epigraph checklist)**
====================================================================

You should now be able to:

1.  Define epigraph and hypograph precisely.
2.  Prove  $f$  convex ⇔  $\mathrm{epi}(f)$  convex (both directions).
3.  Rewrite  $\min f(x)$  as  $\min t$  s.t.  $f(x)\le t$ .
4.  Convert max objectives into epigraph constraints  $f_i(x)\le t$ .
5.  Recognize that epigraph constraints _implicitly enforce the domain_ and must be modeled accordingly.

* * *

Roadmap position
----------------

We have completed **2.3 Epigraphs**, the main bridge from objective language to constraint language.

Next is **2.4 Subgradients**: we’ll define subgradients from first principles, prove the subgradient inequality, show equivalence to supporting hyperplanes of epigraphs, compute subgradients for norms and max functions, and connect to optimality conditions (2.5).

## Response:
**2.4 — Subgradients (the algebraic form of “supporting hyperplanes to epigraphs”)**
------------------------------------------------------------------------------------

_(even more explicit, more granular, more “verbatim,” with full proofs and lots of careful domain logic)_

Subgradients are the point where convex optimization becomes “mechanical” instead of magical.

*   In smooth calculus, gradients describe tangent planes.
*   In convex analysis, subgradients describe **supporting hyperplanes** to a convex function’s **epigraph**.
*   Subgradients let you talk about “tangent underestimators” even when the function is **nondifferentiable** (like  $\|x\|$ ,  $|x|$ ,  $\max_i$ , hinge losses, etc.).

They are also the conceptual ancestor of:

*   KKT multipliers,
*   dual variables as “prices,”
*   certificates (lower bounds),
*   and first-order optimality conditions.

We will build everything from zero.

* * *

**2.4.0 Why gradients are not enough (motivating examples)**
============================================================

In convex optimization, many important convex objectives are **nonsmooth**:

*    $f(x)=|x|$  is convex but has no derivative at  $x=0$ .
*    $f(x)=\|x\|_2$  is convex but not differentiable at  $x=0$ .
*    $f(x)=\max_i (a_i^\top x + b_i)$  is convex, but at “ties” it has corners.

Yet we still want a first-order tool that plays the role of:

$$
f(y) \ge f(x) + \nabla f(x)^\top (y-x) \quad \text{(supporting tangent inequality)}
$$

So we generalize “gradient” to “subgradient.”

* * *

**2.4.1 Definition: subgradient and subdifferential**
=====================================================

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  be a convex function. Let  $x\in\mathrm{dom}f$  (important:  $f(x)$  must be finite to talk about supporting planes at height  $f(x)$ ).

### **Definition (subgradient at  $x$ )**

A vector  $g\in\mathbb{R}^n$  is a **subgradient** of  $f$  at  $x$  if:

$$
\boxed{ f(y)\ \ge\ f(x) + g^\top (y-x)\quad \forall y\in \mathrm{dom}f. }
$$

This inequality is called the **subgradient inequality**.

Interpretation in plain words:

*   The affine function
    $$
    \ell(y) := f(x) + g^\top (y-x)
    $$
    lies **below** the function  $f(y)$  everywhere on the domain, and it matches  $f$  at  $y=x$ .

So  $\ell$  is a global affine underestimator “touching” at  $x$ .

### **Definition (subdifferential)**

The **subdifferential** of  $f$  at  $x$  is the set of all subgradients:

$$
\boxed{ \partial f(x) := \{g\in\mathbb{R}^n : f(y)\ge f(x)+g^\top(y-x)\ \forall y\in\mathrm{dom}f\}. }
$$

So:

*   If  $f$  is smooth at  $x$ ,  $\partial f(x)$  should collapse to  $\{\nabla f(x)\}$ .
*   If  $f$  has a kink at  $x$ ,  $\partial f(x)$  will be a **set** (often a convex set).

* * *

**2.4.2 Immediate sanity checks and basic properties**
======================================================

These should feel obvious but must be stated precisely.

(A)  $\partial f(x)$  is always a convex set
--------------------------------------------

### Claim

If  $g_1,g_2\in\partial f(x)$  and  $\theta\in[0,1]$ , then  $\theta g_1+(1-\theta)g_2\in\partial f(x)$ .

### Proof

Since  $g_1$  is a subgradient:

$$
f(y)\ge f(x)+g_1^\top(y-x)\quad \forall y.
$$

Similarly:

$$
f(y)\ge f(x)+g_2^\top(y-x)\quad \forall y.
$$

Multiply the first inequality by  $\theta\ge0$ , second by  $(1-\theta)\ge0$ , and add:

$$
\theta f(y) + (1-\theta)f(y) \ge \theta f(x)+(1-\theta)f(x) + \left(\theta g_1+(1-\theta)g_2\right)^\top (y-x).
$$

Left side simplifies to  $f(y)$ . Right side simplifies to  $f(x)+(\theta g_1+(1-\theta)g_2)^\top(y-x)$ . So:

$$
f(y)\ge f(x)+(\theta g_1+(1-\theta)g_2)^\top(y-x)\quad \forall y,
$$

hence the convex combination is in  $\partial f(x)$ . ∎

So subdifferentials are convex sets even if  $f$  is not differentiable.

(B) If  $f$  is affine, subgradients are constant
-------------------------------------------------

If  $f(y)=a^\top y+b$ , then the inequality becomes equality for  $g=a$ . Indeed:

$$
f(y)=f(x)+a^\top(y-x),
$$

so  $\partial f(x)=\{a\}$  for all  $x$ .

* * *

**2.4.3 Geometric meaning: subgradient ⇔ supporting hyperplane to the epigraph**
================================================================================

This is the deep link between Phase 1 (supporting hyperplanes) and Phase 2 (functions).

Recall epigraph:

$$
\mathrm{epi}(f) = \{(y,t): f(y)\le t\}.
$$

For convex  $f$ ,  $\mathrm{epi}(f)$  is a convex set (2.3).

We now show:

$$
\boxed{ g\in\partial f(x) \quad\Longleftrightarrow\quad \text{there exists a supporting hyperplane to }\mathrm{epi}(f)\text{ at }(x,f(x)) \text{ with normal }(g,-1). }
$$

Let’s prove this precisely.

* * *

Theorem (epigraph supporting hyperplane characterization)
---------------------------------------------------------

Let  $f$  be convex,  $x\in\mathrm{dom}f$ . Then  $g\in\partial f(x)$  iff the hyperplane

$$
H:=\{(y,t): t = f(x) + g^\top(y-x)\}
$$

supports  $\mathrm{epi}(f)$  at  $(x,f(x))$ .

### Proof (⇒ direction)

Assume  $g\in\partial f(x)$ . Then for all  $y\in\mathrm{dom}f$ ,

$$
f(y)\ge f(x)+g^\top(y-x).
$$

Now take any point  $(y,t)\in\mathrm{epi}(f)$ . By definition of epigraph:

$$
t\ge f(y).
$$

Combine with the subgradient inequality:

$$
t \ge f(y)\ge f(x)+g^\top(y-x).
$$

So every point  $(y,t)\in\mathrm{epi}(f)$  satisfies:

$$
t \ge f(x)+g^\top(y-x).
$$

That means the epigraph lies entirely in the closed halfspace:

$$
\{(y,t): t \ge f(x)+g^\top(y-x)\}.
$$

And the boundary of this halfspace is exactly the hyperplane  $H$ .

Also, the point  $(x,f(x))$  lies on  $H$ , because:

$$
f(x)=f(x)+g^\top(x-x).
$$

Therefore  $H$  is a supporting hyperplane to  $\mathrm{epi}(f)$  at  $(x,f(x))$ . ∎

### Proof (⇐ direction)

Assume  $H$  supports  $\mathrm{epi}(f)$  at  $(x,f(x))$ . Supporting means:

1.   $(x,f(x))\in H$ ,
2.   $\mathrm{epi}(f)$  is contained in one side:
    $$
    t \ge f(x)+g^\top(y-x)\quad \forall (y,t)\in\mathrm{epi}(f).
    $$

Now fix any  $y\in\mathrm{dom}f$ . Then  $(y,f(y))\in\mathrm{epi}(f)$ . Plug in:

$$
f(y) \ge f(x)+g^\top(y-x).
$$

That is exactly the subgradient inequality. So  $g\in\partial f(x)$ . ∎

So subgradients are literally “supporting hyperplane normals” to epigraphs.

* * *

**2.4.4 Smooth case: if  $f$  is differentiable, the only subgradient is the gradient**
=======================================================================================

This is one of the most important “consistency checks.”

### Theorem

If  $f$  is convex and differentiable at  $x$ , then:

$$
\boxed{\partial f(x) = \{\nabla f(x)\}.}
$$

We must prove two things:

1.   $\nabla f(x)\in\partial f(x)$ ,
2.  if  $g\in\partial f(x)$ , then  $g=\nabla f(x)$ .

* * *

Proof, part 1:  $\nabla f(x)$  is a subgradient (supporting tangent inequality)
-------------------------------------------------------------------------------

A standard result (we’ll derive it again in 2.5) is:

$$
f(y)\ge f(x)+\nabla f(x)^\top(y-x).
$$

But let’s prove it now from convexity, using a clean one-dimensional restriction argument.

Fix  $x\in\mathrm{dom}f$  and any  $y\in\mathrm{dom}f$ . Define a scalar function:

$$
\phi(\theta) := f(x+\theta(y-x)),\quad \theta\in[0,1].
$$

This is  $f$  restricted to the line segment from  $x$  to  $y$ .

Because  $f$  is convex,  $\phi$  is convex as a function of  $\theta$  (we formalize line restriction in 2.7; for now it’s intuitive and can be proven directly by convexity of  $f$ ).

For convex  $\phi$ , the secant slope between  $0$  and  $\theta$  is nondecreasing, and in particular:

$$
\phi(1) \ge \phi(0) + \phi'(0)\cdot (1-0).
$$

This is the 1D “tangent underestimates” property of convex functions.

Compute:

*    $\phi(0)=f(x)$ ,
*    $\phi(1)=f(y)$ ,
*    $\phi'(0)=\nabla f(x)^\top (y-x)$  by chain rule.

So:

$$
f(y)\ge f(x) + \nabla f(x)^\top (y-x).
$$

Thus  $\nabla f(x)\in\partial f(x)$ . ∎

(We will rebuild the 1D tangent property rigorously in 2.5/2.7; here you see how it plugs in.)

* * *

Proof, part 2: uniqueness of subgradient under differentiability
----------------------------------------------------------------

Assume  $g\in\partial f(x)$ . Then for all  $y$ ,

$$
f(y)\ge f(x)+g^\top(y-x).
$$

Also we already proved:

$$
f(y)\ge f(x)+\nabla f(x)^\top(y-x).
$$

We want to show  $g=\nabla f(x)$ .

Pick an arbitrary direction  $d\in\mathbb{R}^n$  and consider  $y=x+\epsilon d$  for small  $\epsilon>0$  such that  $y\in\mathrm{dom}f$  (assume  $x$  is interior or take one-sided). Then subgradient inequality gives:

$$
f(x+\epsilon d)-f(x)\ge \epsilon g^\top d.
$$

Divide by  $\epsilon$ :

$$
\frac{f(x+\epsilon d)-f(x)}{\epsilon}\ge g^\top d.
$$

Now let  $\epsilon\to0^+$ . Since  $f$  is differentiable at  $x$ ,

$$
\lim_{\epsilon\to0^+}\frac{f(x+\epsilon d)-f(x)}{\epsilon} = \nabla f(x)^\top d.
$$

So:

$$
\nabla f(x)^\top d \ge g^\top d\quad \forall d.
$$

Now repeat using  $y=x-\epsilon d$  (one-sided in the opposite direction) to get:

$$
\nabla f(x)^\top (-d) \ge g^\top (-d)\quad \forall d \quad\Rightarrow\quad g^\top d \ge \nabla f(x)^\top d\quad \forall d.
$$

Combine the two inequalities:

$$
g^\top d = \nabla f(x)^\top d\quad \forall d.
$$

The only vector whose dot product with every direction  $d$  matches  $\nabla f(x)$  is itself. Hence:

$$
g=\nabla f(x).
$$

So  $\partial f(x)=\{\nabla f(x)\}$ . ∎

That proves subgradients extend gradients.

* * *

**2.4.5 Subgradient existence: do subgradients always exist?**
==============================================================

Not everywhere, but under mild conditions they do.

Key fact (informal but important):

*   If  $f$  is convex and  $x$  is in the **relative interior** of  $\mathrm{dom}f$ , then  $\partial f(x)\neq\emptyset$ .

This is a deep theorem connected to separation of convex sets (supporting hyperplanes to epigraphs). Since we haven’t fully proved separation in Phase 2 yet, treat this as a preview fact: “inside the domain, convex functions have supporting hyperplanes.”

Operationally for PS6: most convex functions you meet (norms, max of affines, log-sum-exp, quadratic forms) have explicit subgradients everywhere in their domain (or at least relative interior).

* * *

**2.4.6 Canonical computed subdifferentials (you must know these cold)**
========================================================================

Now we compute subgradients explicitly for the main atoms you will see constantly.

(A)  $f(x)=|x|$  (scalar absolute value)
----------------------------------------

We claim:

$$
\boxed{ \partial |x| = \begin{cases} \{1\}, & x>0,\\ [-1,1], & x=0,\\ \{-1\}, & x<0. \end{cases}}
$$

### Proof (very explicit)

We need all  $g$  such that:

$$
|y| \ge |x| + g(y-x)\quad \forall y.
$$

**Case 1:  $x>0$ .** Then  $|x|=x$ . Guess  $g=1$ . Check:

$$
|y| \ge y \quad \forall y
$$

which is true because  $|y|\ge y$  always. Also equality holds at  $y=x>0$ . So  $1\in\partial|x|$ .  
Now show no other  $g$  works. If  $g\neq1$ , take  $y$  close to  $x$  and use differentiability of  $|x|$  for  $x>0$ : the derivative is 1, so subgradient must equal gradient. Hence  $\partial|x|=\{1\}$ .

**Case 2:  $x<0$ .** Similar:  $|x|=-x$  and derivative is  $-1$ . So  $\partial|x|=\{-1\}$ .

**Case 3:  $x=0$ .** We need:

$$
|y|\ge g y \quad \forall y.
$$

This must hold for positive and negative  $y$ .

*   For  $y>0$ : inequality becomes  $y \ge g y$  so  $1\ge g$ .
*   For  $y<0$ :  $|y|=-y$ , inequality becomes  $-y \ge g y$ . Divide by negative  $y$  (flips inequality) to get  $-1 \le g$ .

So  $g$  must satisfy  $-1\le g\le 1$ . And any such  $g$  works because:

$$
|y| \ge |g||y| \ge g y
$$

can be checked directly by cases. So  $\partial|0|=[-1,1]$ . ∎

This is the simplest picture of “kink gives interval of subgradients.”

* * *

(B)  $f(x)=\|x\|_2$  (Euclidean norm)
-------------------------------------

Claim:

$$
\boxed{ \partial \|x\|_2 = \begin{cases} \left\{\dfrac{x}{\|x\|_2}\right\}, & x\neq 0,\\[8pt] \{g:\|g\|_2\le 1\}, & x=0. \end{cases}}
$$

### Proof outline with key steps (still explicit)

We need  $g$  s.t.

$$
\|y\|_2 \ge \|x\|_2 + g^\top(y-x)\quad \forall y.
$$

**Case 1:  $x\neq 0$ .** The norm is differentiable away from 0, and its gradient is:

$$
\nabla \|x\|_2 = \frac{x}{\|x\|_2}.
$$

By the differentiable convex theorem above, the subdifferential is the singleton containing this gradient.

**Case 2:  $x=0$ .** Need:

$$
\|y\|_2 \ge g^\top y \quad \forall y.
$$

But by Cauchy–Schwarz:

$$
g^\top y \le \|g\|_2\|y\|_2.
$$

So if  $\|g\|_2\le 1$ , then  $g^\top y \le \|y\|_2$ , which gives the subgradient inequality.

Conversely, if  $\|g\|_2>1$ , choose  $y=g$ . Then:

$$
g^\top y = g^\top g = \|g\|_2^2, \quad \|y\|_2=\|g\|_2.
$$

The inequality  $\|y\|_2\ge g^\top y$  becomes  $\|g\|_2 \ge \|g\|_2^2$ , which is false if  $\|g\|_2>1$ .  
So must have  $\|g\|_2\le1$ . ∎

So at the origin, the subdifferential is the unit ball: all supporting hyperplanes to the Euclidean ball at its “tip.”

* * *

(C) Maximum of affine functions:  $f(x)=\max_{i=1,\dots,m}(a_i^\top x + b_i)$ 
------------------------------------------------------------------------------

This is one of the most important forms in convex optimization.

Let

$$
f(x)=\max_i \ell_i(x),\quad \ell_i(x)=a_i^\top x+b_i.
$$

Define the active set:

$$
I(x):=\{i:\ell_i(x)=f(x)\}.
$$

Claim:

$$
\boxed{ \partial f(x)=\mathrm{conv}\{a_i: i\in I(x)\}. }
$$

Meaning: subgradients are convex combinations of slopes of the active affine pieces.

### Proof (explicit but not skipping)

For any  $i$ , since  $f(y)=\max_j \ell_j(y)\ge \ell_i(y)$ , we have:

$$
f(y)\ge a_i^\top y+b_i.
$$

If  $i\in I(x)$ , then  $f(x)=a_i^\top x+b_i$ . Subtract:

$$
f(y)-f(x)\ge a_i^\top(y-x).
$$

Rearrange:

$$
f(y)\ge f(x)+a_i^\top(y-x).
$$

So each active  $a_i$  is a subgradient:  $a_i\in\partial f(x)$  for  $i\in I(x)$ .

Now use convexity of  $\partial f(x)$ : any convex combination of active  $a_i$ ’s is also a subgradient:

$$
\sum_{i\in I(x)}\theta_i a_i \in \partial f(x),\quad \theta_i\ge0,\ \sum\theta_i=1.
$$

So:

$$
\mathrm{conv}\{a_i:i\in I(x)\}\subseteq \partial f(x).
$$

The reverse inclusion (any subgradient must be in that convex hull) is deeper and uses separation geometry of epigraphs (supporting hyperplanes at a polyhedral epigraph face). Intuitively: the epigraph of  $\max$  is intersection of halfspaces, so its supporting normals at a point are conic combinations of active constraints; translating gives convex hull of active slopes.

Operationally, the formula is standard and reliable for PS6 modeling: at a “tie,” subgradient is any mixture of the tied pieces. ∎

* * *

**2.4.7 Subgradient optimality condition (the most used criterion)**
====================================================================

This is the nonsmooth analogue of “gradient equals zero at optimum.”

### Theorem (first-order optimality via subgradients)

Let  $f$  be convex. Then:

$$
\boxed{ x^\star \text{ minimizes } f \quad \Longleftrightarrow\quad 0\in \partial f(x^\star). }
$$

This is extremely important. Let’s prove both directions cleanly.

* * *

Proof (⇒ direction): minimizer implies  $0\in\partial f(x^\star)$ 
------------------------------------------------------------------

Assume  $x^\star$  is a global minimizer:

$$
f(y)\ge f(x^\star)\quad \forall y.
$$

But that is exactly the subgradient inequality with  $g=0$ :

$$
f(y)\ge f(x^\star)+0^\top(y-x^\star).
$$

So  $0$  is a subgradient at  $x^\star$ , i.e.  $0\in\partial f(x^\star)$ . ∎

Proof (⇐ direction):  $0\in\partial f(x^\star)$  implies minimizer
------------------------------------------------------------------

Assume  $0\in\partial f(x^\star)$ . Then by definition:

$$
f(y)\ge f(x^\star)+0^\top(y-x^\star)=f(x^\star)\quad \forall y.
$$

That is exactly global minimality. ∎

So in convex optimization, optimality conditions are _global_ and simple.

* * *

**2.4.8 How this connects to constraints (preview of KKT)**
===========================================================

In constrained problems, you minimize  $f(x)$  over a convex set  $C$ . The optimality condition becomes:

$$
0 \in \partial f(x^\star) + N_C(x^\star),
$$

where  $N_C$  is the normal cone from Phase 1.5.

This is the geometric KKT condition before you even write multipliers. We’ll build it later, but you should already see the structure:

*    $\partial f(x^\star)$ : objective slope information,
*    $N_C(x^\star)$ : boundary support information,
*   sum contains zero: forces balance.

* * *

**2.4.9 Practical modeling relevance (why PS6 cares)**
======================================================

Subgradients are not just theory. They justify modeling and transformations:

*   **Epigraph constraints** correspond to convex sets; supporting hyperplanes correspond to linear underestimators.
*   Many transformations (like converting max or norms into constraints) are essentially epigraph constructions; subgradients tell you how these pieces “touch” at optimum.
*   When you do robust constraints, you often see suprema and norms; subgradients characterize the “worst-case direction.”

Even if PS6 doesn’t ask “compute a subgradient,” the logic underneath the transformations is subgradient/epigraph geometry.

* * *

**2.4.10 What you must be able to do cold**
===========================================

1.  State the definition:
    $$
    g\in\partial f(x)\iff f(y)\ge f(x)+g^\top(y-x)\ \forall y.
    $$
2.  Explain the epigraph hyperplane equivalence (normal  $(g,-1)$ ).
3.  Prove: if  $f$  differentiable at  $x$ , then  $\partial f(x)=\{\nabla f(x)\}$ .
4.  Compute subdifferentials for:
    *    $|x|$ ,
    *    $\|x\|_2$ ,
    *    $\max_i(a_i^\top x+b_i)$  (active set convex hull rule).
5.  Use optimality condition:
    $$
    x^\star \text{ minimizes } f \iff 0\in\partial f(x^\star).
    $$

* * *

Roadmap position
----------------

We completed **2.4 Subgradients** with:

*   definition and geometry,
*   link to supporting hyperplanes of epigraphs,
*   smooth consistency,
*   explicit subgradient computations for core atoms,
*   and the crucial optimality condition.

Next is **2.5 First-order characterization** (for differentiable convex functions): proving the tangent underestimator inequality rigorously and showing it is equivalent to convexity under differentiability assumptions.

## Response:
**2.5 — First-order characterization of convexity (the “tangent underestimator” theorem, fully unpacked)**
----------------------------------------------------------------------------------------------------------

This section is the “calculus interface” to convexity.

Up to now:

*   **2.1** defined convexity by the chord inequality (mixing two points).
*   **2.3** turned convexity of functions into convexity of a set (epigraph).
*   **2.4** generalized gradients to subgradients (supporting hyperplanes).

Now we specialize to the important case:

> When  $f$  is differentiable, convexity is equivalent to one clean inequality:  
> **Every tangent plane lies below the function everywhere.**

This is the theorem you use constantly in PS6 (especially log barriers and smooth convexity checks).

We will do this with maximal rigor and no hand-waving:

1.  precise statement(s) with all assumptions,
2.  prove “convex ⇒ first-order inequality,”
3.  prove “first-order inequality ⇒ convex,”
4.  give equivalent monotonicity statement of the gradient,
5.  do directional derivative viewpoint,
6.  show how this links to optimality (gradient = 0),
7.  show concrete examples (quadratics, log barrier pieces),
8.  list common failure modes.

* * *

**2.5.0 Setup and what exactly we are proving**
===============================================

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  be convex. For first-order calculus, we will assume:

*    $f$  is **finite** on an open convex set  $D\subseteq\mathbb{R}^n$  (so gradients exist meaningfully),
*    $f$  is **differentiable** on  $D$ ,
*   we will work “inside”  $D$ , i.e.  $x,y\in D$ .

In Boyd-Vandenberghe style, you can think  $D=\mathrm{int}(\mathrm{dom}f)$  when the domain has boundary issues (log barriers, etc.).

* * *

**2.5.1 The main theorem: tangent underestimator inequality**
=============================================================

### Theorem (First-order characterization, one direction)

If  $f$  is convex and differentiable on a convex set  $D$ , then for all  $x,y\in D$ ,

$$
\boxed{ f(y)\ \ge\ f(x)\ +\ \nabla f(x)^\top (y-x). }
$$

This is the **supporting hyperplane / tangent underestimator inequality**.

Interpretation:

*   The affine function
    $$
    \ell_{x}(y) := f(x)+\nabla f(x)^\top (y-x)
    $$
    is the “tangent plane” at  $x$ .
*   Convexity says: the function always lies above that tangent plane.

This is exactly the smooth special case of subgradient inequality:  $\nabla f(x)\in\partial f(x)$ .

But we will prove it directly, in a way that teaches you the mechanics.

* * *

**2.5.2 Proof: convex ⇒ first-order inequality (detailed)**
===========================================================

The cleanest proof goes through a one-dimensional restriction to a line (this is the “line restriction principle” you’ll formalize in 2.7, but we can already do it fully here).

Step 1: Reduce to a 1D function along the segment  $x\to y$ 
------------------------------------------------------------

Fix  $x,y\in D$ . Define the segment:

$$
x(\theta) := x + \theta (y-x),\quad \theta\in[0,1].
$$

So:

*    $x(0)=x$ ,
*    $x(1)=y$ ,
*   for  $0\le\theta\le 1$ ,  $x(\theta)$  is a convex combination of  $x$  and  $y$ , hence lies in  $D$  since  $D$  is convex.

Now define a scalar function:

$$
\phi(\theta) := f(x(\theta)) = f(x+\theta (y-x)),\quad \theta\in[0,1].
$$

Step 2: Show  $\phi$  is convex on  $[0,1]$ 
--------------------------------------------

Take any  $\theta_1,\theta_2\in[0,1]$  and any  $\lambda\in[0,1]$ .  
Then:

$$
x(\lambda\theta_1+(1-\lambda)\theta_2) = x + (\lambda\theta_1+(1-\lambda)\theta_2)(y-x) = \lambda(x+\theta_1(y-x)) + (1-\lambda)(x+\theta_2(y-x)) = \lambda x(\theta_1) + (1-\lambda)x(\theta_2).
$$

Now apply convexity of  $f$ :

$$
\phi(\lambda\theta_1+(1-\lambda)\theta_2) = f(x(\lambda\theta_1+(1-\lambda)\theta_2)) = f(\lambda x(\theta_1)+(1-\lambda)x(\theta_2)) \le \lambda f(x(\theta_1)) + (1-\lambda)f(x(\theta_2)) = \lambda\phi(\theta_1) + (1-\lambda)\phi(\theta_2).
$$

So  $\phi$  is convex on  $[0,1]$ .

This step is important: convexity of  $f$  implies convexity along every line.

Step 3: Use a key 1D fact: convex function lies above its tangents
------------------------------------------------------------------

We now use a basic theorem in one dimension:

> If  $\phi$  is convex and differentiable at  $0$ , then for all  $\theta\in[0,1]$ ,
> 
> $$
> \phi(\theta) \ge \phi(0) + \phi'(0)\,\theta.
> $$

We will prove that 1D fact explicitly right now (no black boxes).

### Lemma (1D tangent inequality for convex  $\phi$ )

Let  $\phi:[0,1]\to\mathbb{R}$  be convex and differentiable at  $0$ . Then for all  $\theta\in[0,1]$ ,

$$
\phi(\theta) \ge \phi(0) + \phi'(0)\theta.
$$

#### Proof of Lemma

Fix any  $\theta\in(0,1]$ . For any  $h\in(0,\theta]$ , convexity of  $\phi$  implies the slope of the secant line from  $0$  to  $h$  is at most the slope from  $0$  to  $\theta$ . More concretely, convexity in 1D implies the secant slope is nondecreasing with the right endpoint. The standard way to prove this:

Take  $0<h<\theta$ . Then  $h = \lambda \theta + (1-\lambda)0$  where  $\lambda = h/\theta\in(0,1)$ .  
By convexity:

$$
\phi(h) \le \lambda \phi(\theta) + (1-\lambda)\phi(0).
$$

Rearrange:

$$
\phi(h)-\phi(0) \le \lambda(\phi(\theta)-\phi(0)).
$$

Divide by  $h$  (note  $h=\lambda\theta$ ):

$$
\frac{\phi(h)-\phi(0)}{h} \le \frac{\phi(\theta)-\phi(0)}{\theta}.
$$

Now let  $h\downarrow 0$ . Since  $\phi$  is differentiable at 0, the left side converges to  $\phi'(0)$ . Therefore:

$$
\phi'(0)\le \frac{\phi(\theta)-\phi(0)}{\theta}.
$$

Multiply by  $\theta\ge0$ :

$$
\phi(0) + \phi'(0)\theta \le \phi(\theta).
$$

That is the desired inequality. ∎

So convexity in 1D forces every chord slope to be at least the derivative at the left endpoint.

Step 4: Compute  $\phi'(0)$  using chain rule
---------------------------------------------

We have:

$$
\phi(\theta)=f(x+\theta(y-x)).
$$

Differentiate at  $\theta=0$ :

$$
\phi'(0) = \nabla f(x)^\top (y-x),
$$

because derivative of  $x+\theta(y-x)$  w.r.t.  $\theta$  is  $(y-x)$ , and apply chain rule.

Step 5: Plug into the lemma
---------------------------

Using lemma with  $\theta=1$ :

$$
\phi(1) \ge \phi(0) + \phi'(0)\cdot 1.
$$

Translate back:

*    $\phi(1)=f(y)$ ,
*    $\phi(0)=f(x)$ ,
*    $\phi'(0)=\nabla f(x)^\top(y-x)$ .

So:

$$
f(y)\ge f(x)+\nabla f(x)^\top(y-x).
$$

Done. ∎

This proof is fully constructive and shows you exactly where convexity enters: in the monotonicity of secant slopes in 1D.

* * *

**2.5.3 Converse: first-order inequality ⇒ convexity**
======================================================

Now we prove the reverse implication:

### Theorem (First-order characterization, other direction)

Let  $f$  be differentiable on a convex set  $D$ . If for all  $x,y\in D$ ,

$$
f(y)\ge f(x)+\nabla f(x)^\top(y-x),
$$

then  $f$  is convex on  $D$ .

This is extremely important: it means you can **certify convexity** by proving the tangent underestimator inequality.

Proof (step-by-step)
--------------------

We must show the convexity inequality:

$$
f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y).
$$

Take arbitrary  $x,y\in D$  and  $\theta\in[0,1]$ . Define the point:

$$
z := \theta x + (1-\theta)y \in D
$$

(since  $D$  is convex).

We apply the first-order inequality twice:

### Apply inequality at point  $z$  with  $x$  playing the role of “ $y$ ”

Using the condition with base point  $z$  and evaluation point  $x$ :

$$
f(x) \ge f(z)+\nabla f(z)^\top(x-z).
$$

Rearrange:

$$
f(z) \le f(x) - \nabla f(z)^\top(x-z).
$$

### Apply inequality at point  $z$  with evaluation point  $y$ 

Similarly:

$$
f(y) \ge f(z)+\nabla f(z)^\top(y-z) \quad\Rightarrow\quad f(z)\le f(y)-\nabla f(z)^\top(y-z).
$$

Now we take a convex combination of these two upper bounds for  $f(z)$ :  
Multiply the first by  $\theta$ , the second by  $(1-\theta)$ , and add:

$$
\theta f(z) + (1-\theta) f(z) \le \theta f(x) - \theta \nabla f(z)^\top(x-z) + (1-\theta) f(y) - (1-\theta)\nabla f(z)^\top(y-z).
$$

Left side simplifies to  $f(z)$ . So:

$$
f(z) \le \theta f(x)+(1-\theta)f(y) - \nabla f(z)^\top\big(\theta(x-z)+(1-\theta)(y-z)\big).
$$

Now compute the vector in parentheses:

$$
\theta(x-z)+(1-\theta)(y-z) = \theta x+(1-\theta)y - (\theta+(1-\theta))z = (\theta x+(1-\theta)y) - z = z - z = 0.
$$

So that whole dot-product term vanishes:

$$
\nabla f(z)^\top(\cdots)=\nabla f(z)^\top 0 = 0.
$$

Therefore:

$$
f(z)\le \theta f(x)+(1-\theta)f(y).
$$

But  $z=\theta x+(1-\theta)y$ . Hence:

$$
f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y).
$$

That is convexity. ∎

This is a beautiful proof because it shows convexity emerges from “tangent planes underestimating everywhere” via one cancellation identity.

* * *

**2.5.4 Equivalent statement: monotonicity of the gradient**
============================================================

Another first-order characterization—very important later for strong convexity and for understanding why convex problems are stable—is:

### Theorem (gradient monotonicity)

If  $f$  is convex and differentiable on  $D$ , then for all  $x,y\in D$ ,

$$
\boxed{ (\nabla f(x)-\nabla f(y))^\top(x-y)\ge 0. }
$$

This is called **monotonicity** of  $\nabla f$  (as an operator).

Proof (from the first-order inequality)
---------------------------------------

Use the tangent underestimator inequality twice:

1.  At  $x$  evaluated at  $y$ :
    
$$
f(y)\ge f(x)+\nabla f(x)^\top(y-x).
$$
2.  At  $y$  evaluated at  $x$ :
    
$$
f(x)\ge f(y)+\nabla f(y)^\top(x-y).
$$

Add them:

$$
f(y)+f(x)\ge f(x)+\nabla f(x)^\top(y-x)+f(y)+\nabla f(y)^\top(x-y).
$$

Cancel  $f(x)+f(y)$  from both sides:

$$
0 \ge \nabla f(x)^\top(y-x)+\nabla f(y)^\top(x-y).
$$

But  $\nabla f(y)^\top(x-y)= -\nabla f(y)^\top(y-x)$ . So:

$$
0 \ge (\nabla f(x)-\nabla f(y))^\top (y-x).
$$

Multiply by  $-1$ :

$$
(\nabla f(x)-\nabla f(y))^\top (x-y)\ge 0.
$$

Done. ∎

Interpretation:

*   the gradient behaves like a “monotone force field.”
*   it cannot create cyclic “downhill loops,” which is another way of saying “no spurious local minima.”

* * *

**2.5.5 Directional derivatives viewpoint (connects to subgradients)**
======================================================================

Even when  $f$  is not differentiable, convexity implies a “directional slope” exists.

Define the directional derivative:

$$
f'(x;d) := \lim_{t\downarrow 0}\frac{f(x+td)-f(x)}{t}
$$

(for convex  $f$  this limit exists, possibly infinite, under mild conditions).

If  $f$  is differentiable, then:

$$
f'(x;d)=\nabla f(x)^\top d.
$$

The first-order inequality can be interpreted as:

$$
f(y)\ge f(x)+f'(x;y-x),
$$

and in general:

$$
f'(x;d)=\max_{g\in\partial f(x)} g^\top d.
$$

(We’ll justify this later, but it’s the deeper structure.)

* * *

**2.5.6 Optimality condition for unconstrained minimization (smooth case)**
===========================================================================

From 2.4 we had:

$$
x^\star \text{ minimizes } f \iff 0\in\partial f(x^\star).
$$

If  $f$  is differentiable,  $\partial f(x^\star)=\{\nabla f(x^\star)\}$ . Therefore:

$$
\boxed{ x^\star \text{ minimizes } f \iff \nabla f(x^\star)=0. }
$$

This is now not just “calculus folklore.” In convex optimization this is globally correct because convexity eliminates local-but-not-global minima.

* * *

**2.5.7 Concrete examples (to make the inequality feel real)**
==============================================================

Example 1: Quadratic function with PSD matrix
---------------------------------------------

Let

$$
f(x)=\frac12 x^\top Q x + c^\top x + r, \quad Q\succeq 0.
$$

Then:

$$
\nabla f(x)=Qx+c.
$$

The first-order inequality says:

$$
f(y)\ge f(x)+(Qx+c)^\top(y-x).
$$

This is true because the difference equals a PSD quadratic form:  
Compute:

$$
f(y)-f(x)-(Qx+c)^\top(y-x) = \frac12(y^\top Qy - x^\top Qx) + c^\top(y-x) - (Qx)^\top(y-x) - c^\top(y-x).
$$

Cancel  $c^\top(y-x)$ :

$$
= \frac12(y^\top Qy - x^\top Qx) - x^\top Q (y-x) = \frac12(y^\top Qy - x^\top Qx - 2x^\top Qy + 2x^\top Qx) = \frac12(y-x)^\top Q (y-x)\ge 0.
$$

So the inequality holds with exact “gap”  $\frac12(y-x)^\top Q(y-x)$ .

This is a template calculation you’ll use a lot.

Example 2: Log barrier atom
---------------------------

Let  $f(x)=-\log x$  on domain  $x>0$ .  
Then  $f'(x)=-1/x$ .  
The first-order inequality says:

$$
-\log y \ge -\log x - \frac{1}{x}(y-x),\quad x>0,\ y>0.
$$

This is a real inequality you can check numerically; it encodes concavity of  $\log$  and convexity of  $-\log$ . It will reappear in 4.2.

* * *

**2.5.8 Common failure modes (how people misuse the first-order test)**
=======================================================================

1.  **Using it without checking differentiability / domain interior**  
    For  $f(x)=\|x\|$ , you cannot write  $\nabla f(0)$ . Use subgradients instead.
2.  **Forgetting the domain must be convex**  
    If the domain is not convex, the inequality cannot characterize convexity properly.
3.  **Mixing up direction of inequality**  
    Convex:  $f(y)\ge f(x)+\nabla f(x)^\top(y-x)$ .  
    Concave: inequality reverses.
4.  **Assuming Hessian PSD without proving twice differentiability**  
    That belongs to 2.6; don’t jump the gun.

* * *

**2.5.9 What you must be able to do cold**
==========================================

*   State the theorem precisely with assumptions.
*   Prove convex ⇒ tangent underestimator inequality by restricting to a line and proving the 1D lemma about secant slopes.
*   Prove the converse: tangent underestimator inequality ⇒ convexity, using the cancellation trick at  $z=\theta x+(1-\theta)y$ .
*   Derive gradient monotonicity by adding the two inequalities.
*   Use the inequality to certify convexity in examples.

* * *

Roadmap position
----------------

We have completed **2.5 First-order characterization** in full, including both directions and the gradient monotonicity corollary.

Next is **2.6 Second-order characterization**: for twice-differentiable functions, convexity ⇔ Hessian PSD, and we’ll prove that rigorously (including the directional second derivative view and the exact logic connecting PSD to convexity along lines).

## Response:
**2.6 — Second-order characterization of convexity (Hessian PSD ⇔ convexity, with full logic and edge cases)**
--------------------------------------------------------------------------------------------------------------

This is the “engine room” for almost every smooth convexity check you’ll do in PS6: log barriers, quadratic forms, log-sum-exp, and many “is this constraint convex?” questions.

But we have to do it correctly. People often say “Hessian PSD ⇒ convex” as if it’s a slogan. It is true, but only under the right assumptions and with a specific chain of reasoning.

We will build the whole thing from scratch, step-by-step:

1.  What “twice differentiable” really means and why we need it,
2.  What “PSD” means and how to check it,
3.  The precise theorem statements,
4.  Proof of **convex ⇒ Hessian PSD**,
5.  Proof of **Hessian PSD ⇒ convex** (via line restrictions),
6.  Directional second derivatives (the most intuitive bridge),
7.  Strict/strong convexity in second-order terms (preview but important),
8.  Common traps (domain, boundary, semidefinite vs definite, etc.),
9.  How to actually compute these in practice (especially for barrier terms).

Throughout: we keep the “truth track” (theorems) and the “engineering track” (how you use them).

* * *

**2.6.0 Prerequisites we must lock down**
=========================================

2.6.0.1 Differentiability levels
--------------------------------

Let  $f:\mathbb{R}^n\to\mathbb{R}$  (for second-order we usually assume real-valued on an open set).

*    $f$  is **differentiable** at  $x$  if there exists a linear map (vector)  $\nabla f(x)$  such that:
    $$
    f(x+h) = f(x) + \nabla f(x)^\top h + o(\|h\|) \quad \text{as } h\to 0.
    $$
*    $f$  is **twice differentiable** at  $x$  if  $\nabla f$  is differentiable at  $x$ . Then there exists a matrix  $\nabla^2 f(x)$  such that:
    $$
    \nabla f(x+h) = \nabla f(x) + \nabla^2 f(x)\,h + o(\|h\|) \quad \text{as } h\to 0.
    $$
    This matrix is the **Hessian**.

Intuition:

*   gradient = first-order local linear approximation,
*   Hessian = how that gradient changes with direction.

2.6.0.2 Why we usually assume an open convex domain
---------------------------------------------------

Hessians are local objects requiring you can move a bit in any direction. If the domain has a boundary (like  $x>0$  for  $-\log x$ ), we work on the **interior** of the domain, which is open, and convex if the original domain is convex.

So our default setting for second-order tests is:

>  $D\subseteq\mathbb{R}^n$  is an **open convex set**, and  $f\in C^2(D)$ , meaning twice continuously differentiable on  $D$ .

This covers almost all smooth convexity checks you’ll do.

* * *

**2.6.1 Linear algebra: PSD matrices (what  $\succeq 0$  means)**
=================================================================

Second-order characterization is stated in terms of the Hessian being **positive semidefinite**.

### Definition (PSD)

A symmetric matrix  $H\in\mathbb{R}^{n\times n}$  is **positive semidefinite** (PSD), written  $H\succeq 0$ , if:

$$
\boxed{ d^\top H d \ge 0\quad \forall d\in\mathbb{R}^n. }
$$

Similarly, **positive definite** (PD),  $H\succ 0$ , means:

$$
d^\top H d > 0\quad \forall d\neq 0.
$$

Interpretation:

*    $d^\top H d$  is the curvature in direction  $d$ .
*   PSD means “no direction has negative curvature.”

### Practical equivalent tests (you’ll use these later)

For symmetric  $H$ :

*    $H\succeq 0$  ⇔ all eigenvalues are  $\ge 0$ .
*    $H\succ 0$  ⇔ all eigenvalues are  $> 0$ .
*   Sylvester criterion: PD iff all leading principal minors positive (PSD has subtleties; minors nonnegative is necessary but not sufficient in all cases unless all principal minors nonnegative—more complicated).
*   Cholesky: PD iff Cholesky exists with positive diagonal.

In convex optimization, Hessians are symmetric (by Schwarz theorem under mild smoothness), so PSD is well-defined.

* * *

**2.6.2 The main theorem (precise statement)**
==============================================

### Theorem (Second-order characterization of convexity)

Let  $D\subseteq\mathbb{R}^n$  be **open and convex**, and let  $f:D\to\mathbb{R}$  be **twice differentiable**.

Then:

$$
\boxed{ f \text{ is convex on } D \quad\Longleftrightarrow\quad \nabla^2 f(x)\succeq 0\ \text{ for all } x\in D. }
$$

There are two directions to prove:

1.  **Convex ⇒ Hessian PSD**
2.  **Hessian PSD ⇒ Convex**

We do both carefully.

* * *

**2.6.3 Proof direction 1: convex ⇒ Hessian PSD**
=================================================

We assume  $f$  is convex on  $D$  and  $C^2$ . We want to show:

$$
d^\top \nabla^2 f(x)\, d \ge 0\quad \forall x\in D,\ \forall d\in\mathbb{R}^n.
$$

Step 1: Reduce to 1D along a line
---------------------------------

Fix any  $x\in D$  and direction  $d\in\mathbb{R}^n$ .

Because  $D$  is open, there exists  $\epsilon>0$  such that  $x+td\in D$  for all  $t\in(-\epsilon,\epsilon)$ .

Define the 1D function:

$$
\phi(t) := f(x+td),\quad t\in(-\epsilon,\epsilon).
$$

Step 2:  $\phi$  is convex in 1D
--------------------------------

Since  $f$  is convex on  $D$ , its restriction to any line is convex. Concretely, for  $t_1,t_2$  and  $\lambda\in[0,1]$ ,

$$
\phi(\lambda t_1+(1-\lambda)t_2) = f(x+(\lambda t_1+(1-\lambda)t_2)d) = f(\lambda(x+t_1 d)+(1-\lambda)(x+t_2 d)) \le \lambda f(x+t_1 d) + (1-\lambda) f(x+t_2 d) = \lambda\phi(t_1)+(1-\lambda)\phi(t_2).
$$

So  $\phi$  is convex.

Step 3: In 1D, convex + twice differentiable ⇒ second derivative ≥ 0
--------------------------------------------------------------------

This is a standard 1D fact, but we prove it explicitly.

### Lemma (1D)

If  $\phi$  is convex on an interval and twice differentiable, then  $\phi''(t)\ge 0$  on that interval.

#### Proof sketch with explicit logic

Convexity in 1D implies  $\phi'$  is nondecreasing. (This comes from secant slopes being nondecreasing; the derivative is the limit of those slopes.) If  $\phi'$  is nondecreasing and differentiable, its derivative  $\phi''$  must be  $\ge 0$ . ∎

So in particular at  $t=0$ ,

$$
\phi''(0)\ge 0.
$$

Step 4: Compute  $\phi''(0)$  in terms of Hessian
-------------------------------------------------

By chain rule:

*    $\phi'(t) = \nabla f(x+td)^\top d$ .  
    Differentiate again:
*    $\phi''(t) = d^\top \nabla^2 f(x+td)\, d$ .

So at  $t=0$ :

$$
\phi''(0) = d^\top \nabla^2 f(x)\, d.
$$

Since  $\phi''(0)\ge 0$ , we get:

$$
d^\top \nabla^2 f(x)\, d \ge 0.
$$

Because  $x$  and  $d$  were arbitrary,  $\nabla^2 f(x)\succeq 0$  for all  $x\in D$ . ∎

That proves convexity forces nonnegative curvature in every direction.

* * *

**2.6.4 Proof direction 2: Hessian PSD ⇒ convex**
=================================================

This is the direction you use most in practice: compute Hessian and check PSD to conclude convexity.

Assume:

$$
\nabla^2 f(x)\succeq 0 \quad \forall x\in D.
$$

We want to prove the convexity inequality:

$$
f(\theta x + (1-\theta) y) \le \theta f(x) + (1-\theta) f(y)\quad \forall x,y\in D,\ \theta\in[0,1].
$$

Again, we reduce to 1D.

Step 1: Restrict to a line segment
----------------------------------

Fix  $x,y\in D$ . Define:

$$
x(\theta) := x+\theta (y-x),\quad \theta\in[0,1].
$$

Define:

$$
\phi(\theta) := f(x(\theta)) = f(x+\theta(y-x)).
$$

Because  $D$  is convex,  $x(\theta)\in D$  for  $\theta\in[0,1]$ .

Step 2: Show  $\phi''(\theta)\ge 0$ 
------------------------------------

Let  $d:=y-x$ . Then:

$$
\phi'(\theta) = \nabla f(x+\theta d)^\top d,
$$
 
$$
\phi''(\theta) = d^\top \nabla^2 f(x+\theta d)\, d.
$$

But  $\nabla^2 f(\cdot)\succeq 0$ , so for every  $\theta$ :

$$
\phi''(\theta) = d^\top \nabla^2 f(x+\theta d)\, d \ge 0.
$$

Thus  $\phi$  is a 1D twice differentiable function with  $\phi''(\theta)\ge 0$ .

Step 3: 1D fact:  $\phi''\ge 0$  ⇒  $\phi$  convex
--------------------------------------------------

In 1D, a twice differentiable function is convex iff its second derivative is nonnegative.

So  $\phi$  is convex on  $[0,1]$ .

Step 4: Convert convexity of  $\phi$  back to convexity of  $f$ 
----------------------------------------------------------------

Convexity of  $\phi$  means:

$$
\phi(\theta) \le (1-\theta)\phi(0) + \theta \phi(1).
$$

Substitute:

*    $\phi(0)=f(x)$ ,
*    $\phi(1)=f(y)$ ,
*    $\phi(\theta)=f(x+\theta(y-x))=f((1-\theta)x+\theta y)$ .

So:

$$
f((1-\theta)x+\theta y) \le (1-\theta) f(x) + \theta f(y).
$$

That is exactly convexity of  $f$ . ∎

This direction is conceptually: “nonnegative curvature in all directions ⇒ convex along every line ⇒ convex globally.”

* * *

**2.6.5 Directional second derivative: the most intuitive bridge**
==================================================================

A key insight is:

$$
\boxed{ \text{Convexity (smooth)} \iff \text{second directional derivative is nonnegative in every direction.} }
$$

For  $f\in C^2$ , the second directional derivative at  $x$  in direction  $d$  is:

$$
\frac{d^2}{dt^2} f(x+td)\Big|_{t=0} = d^\top \nabla^2 f(x)\, d.
$$

So:

*   Hessian PSD means “every direction has nonnegative second directional derivative,” i.e. no concave bending.

This is often the best way to _think_ about Hessians: they package all directional curvatures into a matrix.

* * *

**2.6.6 Strict convexity and strong convexity (second-order viewpoint, important preview)**
===========================================================================================

Even though strict/strong convexity get formal later, you’ll constantly need the distinction.

(A) If  $\nabla^2 f(x)\succ 0$  everywhere, then  $f$  is strictly convex
-------------------------------------------------------------------------

Because along every line,  $\phi''(\theta)>0$  implies  $\phi$  is strictly convex, hence  $f$  strictly convex.

**But warning:** Strict convexity does _not_ require Hessian PD everywhere (there are strictly convex functions whose Hessian is only PSD at some points). So PD is a sufficient condition, not necessary.

(B) Strong convexity (uniform curvature)
----------------------------------------

If there exists  $m>0$  such that:

$$
\boxed{\nabla^2 f(x)\succeq m I \quad \forall x\in D,}
$$

then  $f$  is ** $m$ \-strongly convex** and you get quadratic lower bounds and uniqueness and fast convergence properties.

This “uniform PSD margin” is what gives numerical stability.

* * *

**2.6.7 How to actually check “Hessian PSD” in practice (engineering track)**
=============================================================================

Given a Hessian  $H(x)$ :

### Method 1: Quadratic form test

Show

$$
d^\top H(x) d \ge 0 \ \forall d.
$$

Often you can rewrite it as sum of squares.

### Method 2: Eigenvalues

Compute eigenvalues or show matrix has nonnegative eigenvalues (hard symbolically, easy numerically).

### Method 3: Recognize structure

*   Diagonal with nonnegative entries ⇒ PSD.
*    $A^\top A$  ⇒ PSD.
*   Block-diagonal: PSD iff each block PSD.
*   Schur complement (later in SDP) gives PSD conditions for blocks.

For PS6, many Hessians are diagonal or rank-one updates, so you can show PSD by direct quadratic form.

* * *

**2.6.8 The log barrier prototype (what you’ll do in Exercise 4.2)**
====================================================================

The barrier atom is:

$$
f(x) = -\log(b - a^\top x)
$$

on domain  $b-a^\top x>0$ .

Let  $u(x):=b-a^\top x$ . Then  $f(x)=-\log u(x)$ .

Compute gradient:

$$
\nabla f(x) = -\frac{1}{u(x)} \nabla u(x).
$$

But  $\nabla u(x) = -a$ . So:

$$
\nabla f(x) = -\frac{1}{u(x)}(-a)=\frac{a}{b-a^\top x}.
$$

Compute Hessian (differentiate again). Since numerator is constant  $a$ , derivative comes from  $1/u(x)$ :

$$
\nabla^2 f(x) = a \cdot \nabla\left(\frac{1}{u(x)}\right)^\top.
$$

Now:

$$
\nabla\left(\frac{1}{u}\right) = -\frac{1}{u^2}\nabla u = -\frac{1}{u^2}(-a)=\frac{a}{u^2}.
$$

So:

$$
\boxed{ \nabla^2 f(x)= \frac{a a^\top}{(b-a^\top x)^2}. }
$$

That matrix is PSD because for any  $d$ ,

$$
d^\top \nabla^2 f(x) d = \frac{d^\top a a^\top d}{u^2} = \frac{(a^\top d)^2}{u^2} \ge 0.
$$

So barrier terms are convex. This is the exact computation pattern you’ll repeat.

* * *

**2.6.9 Common traps and “gotchas”**
====================================

1.  **Forgetting to restrict to an open domain**  
    Hessian tests need interior points. At the boundary  $b-a^\top x=0$ , function is infinite anyway.
2.  **Hessian must be symmetric**  
    If you compute and get nonsymmetric, you made an algebra mistake (for  $C^2$  functions, Hessian is symmetric).
3.  **PSD vs PD confusion**  
    PSD allows flat directions (zero curvature), so not necessarily strict convexity.
4.  **Pointwise PSD is enough on convex open domain**  
    But you must ensure the condition holds **everywhere** on the domain.
5.  **Extended-valued functions**  
    Second-order test applies on the interior where function is finite and smooth. Outside: irrelevant (it’s +∞).

* * *

**2.6.10 What you must be able to do cold**
===========================================

*   State the theorem precisely: on open convex domain,  $C^2$ , convex ⇔ Hessian PSD everywhere.
*   Prove both directions using line restriction and 1D second derivative characterization.
*   Translate Hessian PSD into the quadratic form condition  $d^\top H d\ge 0$ .
*   Compute Hessians for common atoms:
    *   quadratic forms,
    *    $-\log(\text{affine})$  barriers,
    *   sums of such terms (Hessian adds).
*   Recognize rank-one PSD matrices like  $aa^\top$ .

* * *

Roadmap position
----------------

We completed **2.6 Second-order characterization** with full proofs and the operational recipe you’ll apply in barrier convexity checks.

Next is **2.7 Line restriction principle** (formally): the general theorem that convexity in  $\mathbb{R}^n$  is equivalent to convexity of every 1D restriction, and how that ties together 2.1, 2.5, and 2.6 into one unified picture.

## Response:
**2.7 — Line restriction principle (reduce  $n$ \-D convexity to 1-D convexity, with full equivalences and proofs)**
--------------------------------------------------------------------------------------------------------------------

This principle is one of the deepest “simplifiers” in convex analysis:

> To check convexity in  $\mathbb{R}^n$ , it is enough to check convexity on every line.

This is not a vague intuition. It is a precise theorem, and it is exactly why the proofs in 2.5 and 2.6 worked by restricting to a line segment and using 1D calculus.

We will build it rigorously and carefully, including the domain issues that people usually mess up.

* * *

**2.7.0 What “restriction to a line” actually means**
=====================================================

Fix:

*   a point  $x\in\mathbb{R}^n$ ,
*   a direction  $v\in\mathbb{R}^n$  (often  $v\neq 0$ ).

Consider the line (affine set):

$$
L := \{x + tv : t\in\mathbb{R}\}.
$$

Given a function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ , define the **restriction** of  $f$  to this line as a 1D function:

$$
\phi(t) := f(x + tv).
$$

But you must be careful about the domain: if  $f$  is extended-valued, then  $\phi(t)$  might be  $+\infty$  for some  $t$ . So the natural 1D domain is:

$$
\mathrm{dom}\,\phi := \{t\in\mathbb{R} : x+tv\in \mathrm{dom}f\}.
$$

So  $\phi:\mathbb{R}\to\mathbb{R}\cup\{+\infty\}$  is also extended-valued.

This is the exact setting for convexity: domain matters.

* * *

**2.7.1 The theorem (the core statement)**
==========================================

### Theorem (Line restriction principle)

Let  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ . Then the following are equivalent:

1.   $f$  is convex (i.e. for all  $x,y$  and  $\theta\in[0,1]$ ,
    $$
    f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y),
    $$
    with domain convexity automatically encoded by extended values).
2.  For every  $x\in\mathbb{R}^n$  and every  $v\in\mathbb{R}^n$ , the 1D restriction
    $$
    \phi(t)=f(x+tv)
    $$
    is a convex function of  $t$  (as an extended-valued function on  $\mathbb{R}$ ).

People often summarize this as:

$$
\boxed{ f \text{ convex in } \mathbb{R}^n \iff f \text{ is convex along every line.} }
$$

But the true content is: **every 2-point convexity check is already a line check**, and conversely line checks imply the full inequality for any pair of points.

We prove both directions with no skipped steps.

* * *

**2.7.2 Proof:  $f$  convex ⇒ every line restriction is convex**
================================================================

Assume  $f$  is convex.

Fix any  $x$  and  $v$ . Define  $\phi(t)=f(x+tv)$ .

We must show: for any  $t_1,t_2\in\mathbb{R}$  and any  $\lambda\in[0,1]$ ,

$$
\phi(\lambda t_1+(1-\lambda)t_2)\le \lambda \phi(t_1)+(1-\lambda)\phi(t_2).
$$

Compute the left-hand side:

$$
\phi(\lambda t_1+(1-\lambda)t_2) = f\!\left(x+(\lambda t_1+(1-\lambda)t_2)v\right).
$$

Now rewrite the inside as a convex combination in  $\mathbb{R}^n$ :

$$
x+(\lambda t_1+(1-\lambda)t_2)v = \lambda(x+t_1 v)+(1-\lambda)(x+t_2 v).
$$

Apply convexity of  $f$ :

$$
f(\lambda(x+t_1 v)+(1-\lambda)(x+t_2 v)) \le \lambda f(x+t_1 v)+(1-\lambda)f(x+t_2 v).
$$

Translate back to  $\phi$ :

$$
\phi(\lambda t_1+(1-\lambda)t_2) \le \lambda \phi(t_1)+(1-\lambda)\phi(t_2).
$$

Thus  $\phi$  is convex. ∎

This direction is mechanically straightforward: convexity is preserved under affine precomposition (here,  $t\mapsto x+tv$ ).

* * *

**2.7.3 Proof: every line restriction convex ⇒  $f$  convex**
=============================================================

Now assume: for every  $x,v$ , the function  $\phi(t)=f(x+tv)$  is convex in 1D.

We must prove the convexity inequality for  $f$ :

$$
f(\theta x_1+(1-\theta)x_2)\le \theta f(x_1)+(1-\theta)f(x_2), \quad \forall x_1,x_2,\ \theta\in[0,1].
$$

Take arbitrary  $x_1,x_2\in\mathbb{R}^n$ . Define:

$$
x := x_2,\qquad v := x_1-x_2.
$$

Then:

*   when  $t=0$ :  $x+0\cdot v=x_2$ ,
*   when  $t=1$ :  $x+1\cdot v=x_1$ ,
*   when  $t=\theta$ :  $x+\theta v = x_2+\theta(x_1-x_2)=\theta x_1+(1-\theta)x_2$ .

Define the line restriction:

$$
\phi(t):=f(x_2+t(x_1-x_2)).
$$

By assumption,  $\phi$  is convex in 1D. Therefore:

$$
\phi(\theta)\le \theta \phi(1)+(1-\theta)\phi(0).
$$

Substitute:

$$
f(\theta x_1+(1-\theta)x_2) \le \theta f(x_1)+(1-\theta)f(x_2).
$$

This is exactly convexity of  $f$ . ∎

So line convexity is not “a helpful sufficient condition.” It is fully equivalent to convexity.

* * *

**2.7.4 Why this principle is so powerful (conceptual unification)**
====================================================================

This theorem explains why a lot of convex analysis has this “reduce to 1D and use calculus” feel.

Because convexity itself is a statement about **pairs of points and their connecting segment**.  
A segment is already 1D geometry embedded in  $n$ \-D space.

So convexity is inherently a “line-segment property.”

* * *

**2.7.5 How 2.7 unifies 2.5 and 2.6**
=====================================

Now you can see the structure very cleanly:

*   To prove 2.5 (first-order inequality), we restricted  $f$  to the line  $x+\theta(y-x)$  and used 1D convexity facts (secant slopes monotone).
*   To prove 2.6 (Hessian PSD test), we again restricted to a line and used 1D fact:  $\phi''\ge 0 \iff \phi$  convex.

The line restriction principle guarantees this approach is not a trick—it is the correct reduction.

* * *

**2.7.6 Extended-valued functions and domain convexity (subtle but important)**
===============================================================================

If  $f$  is extended-valued, convexity includes domain convexity implicitly. Here is how the line restriction principle encodes that.

Suppose  $f(x)=+\infty$  outside a set  $C$ . Then:

*   along a line,  $\phi(t)=+\infty$  outside the set of  $t$  such that  $x+tv\in C$ .

For  $\phi$  to be convex, its domain  $\mathrm{dom}\phi\subseteq\mathbb{R}$  must be convex (an interval). That implies that the intersection of  $C$  with any line is an interval. This is exactly what convexity of sets means.

So in set language:

$$
C \text{ convex} \iff C\cap L \text{ is an interval for every line }L.
$$

This is the set-version of 2.7, and it’s consistent with Phase 1.

* * *

**2.7.7 Practical consequences (PS6 modeling reflexes)**
========================================================

(A) How to _disprove_ convexity quickly
---------------------------------------

To show a function is not convex, it is enough to find **one line** where it fails.

That is, find  $x$ ,  $v$ , and show  $\phi(t)=f(x+tv)$  is not convex in 1D.  
This is often much easier than trying to reason in  $n$ \-D.

(B) How to prove convexity by recognizing 1D atoms
--------------------------------------------------

When you see a complicated expression, you can:

*   show along any line it becomes a known convex 1D function (like  $-\log$ ,  $\exp$ , quadratic),
*   then by 2.7 conclude global convexity.

This is a common technique for functions like log-sum-exp (we’ll do that later).

(C) How to interpret Hessian PSD
--------------------------------

Hessian PSD is exactly: along every direction  $v$ , the second derivative of  $\phi(t)=f(x+tv)$  is nonnegative.  
So “PSD” is a matrix way of stating “every line has nonnegative curvature.”

* * *

**2.7.8 A complete “line-based convexity kit” you should carry**
================================================================

Given a function  $f$ , you have three standard ways to certify convexity:

1.  **Definition (2.1)**: check chord inequality directly (rarely practical).
2.  **First-order (2.5)**: show  $f(y)\ge f(x)+\nabla f(x)^\top(y-x)$ .
3.  **Second-order (2.6)**: show  $\nabla^2 f(x)\succeq 0$  everywhere (when  $C^2$ ).

The line restriction principle is the backbone behind 2) and 3).

* * *

**2.7.9 Common mistakes**
=========================

1.  **Using line restriction but forgetting domain**  
    If the line exits the domain, you must restrict to the interval where the line stays in domain.
2.  **Assuming “convex along coordinate lines” is enough**  
    It is not. You need convexity along _every_ line, not just axis-aligned ones. Coordinate-wise convexity is weaker.
3.  **Confusing “convex in each variable separately” with convexity**  
    Separate convexity does not imply joint convexity. The line principle explains why: lines can mix variables.

* * *

**2.7.10 What you must be able to do cold**
===========================================

*   State and prove:  $f$  convex ⇔  $f$  convex along every line.
*   Use it to justify the reduction steps in 2.5 and 2.6.
*   Use it practically:
    *   find a line to disprove convexity,
    *   reduce a convexity proof to 1D.

* * *

Roadmap position
----------------

We completed **2.7 Line restriction principle**.

Next is **2.8 Standard convex functions library**: we will build a “catalog” of functions you must recognize instantly (affine, norms, quadratic forms, exp/log/log-sum-exp, barriers, max of affines, etc.), and for each we’ll provide proofs of convexity using 2.5/2.6/2.7 and show the modeling epigraph form you will use later in PS6.

## Response:
**2.8 — Standard convex functions library (what you must recognize instantly, with proofs and modeling forms)**
---------------------------------------------------------------------------------------------------------------

This section is your “muscle memory builder.”

PS6 doesn’t reward philosophical appreciation of convexity. It rewards this exact skill:

> See an expression and immediately know:  
> (i) is it convex (and on what domain)?  
> (ii) how do I prove it quickly (1st-order / 2nd-order / composition / epigraph)?  
> (iii) how do I model it into LP/QP/SOCP/SDP/GP form?

So we’ll build a library of core convex functions. For each one, we will do three things:

1.  **Truth track:** exact statement + rigorous convexity proof (with domain).
2.  **Engineering track:** epigraph / cone representation when relevant.
3.  **Failure modes:** where people screw it up.

We are still in Phase 2 (convex functions), so we are not yet fully doing every conic representation, but we will mark the modeling hook each time.

* * *

**2.8.0 A meta-lemma: how to prove convexity quickly without drowning**
=======================================================================

Given a candidate  $f$ , you almost always choose one of these proof routes:

*   **Route A (2.6): Hessian PSD** if  $f\in C^2$  and Hessian is manageable.
*   **Route B (2.5): first-order inequality** if gradient is simple and you can show tangent underestimator.
*   **Route C (2.7): line restriction** if you can reduce to a known 1D convex function.
*   **Route D (2.3): epigraph is convex** by expressing epi as intersection / affine image of known convex sets.
*   **Route E (2.9 preview): composition rules** (we will formalize next).

In practice, you want to _choose_ the route that makes the algebra shortest and least error-prone.

* * *

**2.8.1 Affine and linear functions**
=====================================

### Definition

A function  $f:\mathbb{R}^n\to\mathbb{R}$  is affine if

$$
f(x)=a^\top x + b
$$

for some  $a\in\mathbb{R}^n$ ,  $b\in\mathbb{R}$ .  
Linear is the special case  $b=0$ .

### Claim: affine functions are both convex and concave

We must show convexity:

$$
f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y).
$$

Compute exactly:

$$
f(\theta x+(1-\theta)y) = a^\top(\theta x+(1-\theta)y)+b = \theta a^\top x + (1-\theta)a^\top y + b.
$$

Meanwhile:

$$
\theta f(x)+(1-\theta)f(y) = \theta(a^\top x+b) + (1-\theta)(a^\top y+b) = \theta a^\top x+(1-\theta)a^\top y + (\theta+(1-\theta))b = \theta a^\top x+(1-\theta)a^\top y + b.
$$

They are equal. So inequality holds with equality. Hence convex. Similarly concave.

### Modeling hook

Affine objectives and constraints produce LP/QP/SOCP/SDP standard forms easily.

* * *

**2.8.2 Quadratic forms (the core of QP)**
==========================================

There are two related objects:

1.  **Quadratic form:**  $q(x)=x^\top Q x$  (often with  $Q=Q^\top$ ).
2.  **General quadratic function:**  $f(x)=\frac12 x^\top Q x + c^\top x + r$ .

### Theorem

If  $Q\succeq 0$  (PSD), then  $f$  is convex on  $\mathbb{R}^n$ .  
If  $Q\succ 0$ , then  $f$  is strictly convex.

### Proof via Hessian (2.6)

Assume  $Q=Q^\top$ . Compute:

$$
\nabla f(x)=\frac12(Q^\top+Q)x+c = Qx+c,
$$
 
$$
\nabla^2 f(x)=Q.
$$

So  $f$  is convex iff  $\nabla^2 f(x)=Q\succeq 0$ . Done.

### Engineering hook

*   Minimizing a PSD quadratic with linear constraints is a **QP**.
*   Epigraph of a quadratic form can become an **LMI** using Schur complement later (Phase 4/5).

* * *

**2.8.3 Norms as convex functions (PS6 everywhere)**
====================================================

Let  $\|\cdot\|$  be any norm on  $\mathbb{R}^n$ .

### Claim: every norm is convex

We show:

$$
\| \theta x + (1-\theta)y \| \le \theta\|x\|+(1-\theta)\|y\|.
$$

Proof:

$$
\|\theta x+(1-\theta)y\| \le \|\theta x\| + \|(1-\theta)y\| \quad \text{(triangle inequality)} = \theta\|x\|+(1-\theta)\|y\|\quad \text{(homogeneity)}.
$$

So norms are convex.

### Key special norms and modeling hooks

*    $\|x\|_2 \le t$  is **SOC**.
*    $\|x\|_1 \le t$  is **LP** via absolute-value slacks.
*    $\|x\|_\infty \le t$  is **LP** via componentwise bounds.

You already proved norm balls convex in Phase 1; this is the function version.

* * *

**2.8.4 Maximum of affine functions (piecewise-linear convexity)**
==================================================================

Let

$$
f(x)=\max_{i=1,\dots,m} (a_i^\top x+b_i).
$$

### Claim:  $f$  is convex

Proof (use epigraph / set argument):

$$
f(x)\le t \iff a_i^\top x+b_i \le t\quad \forall i.
$$

So:

$$
\mathrm{epi}(f)=\{(x,t): a_i^\top x+b_i \le t\ \forall i\}.
$$

This is an intersection of halfspaces in  $\mathbb{R}^{n+1}$ , hence convex. Therefore  $f$  is convex (2.3).

### Engineering hook

This converts  $\min_x \max_i(\cdots)$  into an LP-like epigraph form:

$$
\min_{x,t}\ t\ \text{s.t. } a_i^\top x+b_i\le t.
$$

* * *

**2.8.5 Exponential function and log-sum-exp (the GP/entropy backbone)**
========================================================================

2.8.5.1  $f(x)=e^x$  is convex on  $\mathbb{R}$ 
------------------------------------------------

Second derivative:

$$
f''(x)=e^x>0.
$$

So convex.

2.8.5.2  $f(x)=\log\sum_{i=1}^m e^{x_i}$  is convex on  $\mathbb{R}^m$ 
-----------------------------------------------------------------------

This function (log-sum-exp) appears constantly: GP transforms, softmax, smooth max approximation.

There are multiple proofs; the cleanest for a newcomer is: **log-sum-exp is the log of a sum of exponentials, and it is the smooth max**. But we must be rigorous.

### Proof sketch using Hessian structure (truth track, but careful)

Let

$$
f(x)=\log\left(\sum_{i=1}^m e^{x_i}\right).
$$

Define  $S(x)=\sum_i e^{x_i}$ .  
Then:

$$
\frac{\partial f}{\partial x_i} = \frac{e^{x_i}}{S(x)}=:p_i.
$$

So  $\nabla f(x)=p$ , where  $p$  is a probability vector (nonnegative and sums to 1).

Compute Hessian:

$$
\frac{\partial^2 f}{\partial x_i\partial x_j} = \frac{\partial p_i}{\partial x_j} = p_i(\delta_{ij}-p_j).
$$

So:

$$
\nabla^2 f(x)=\mathrm{Diag}(p) - pp^\top.
$$

Now check PSD: for any  $d\in\mathbb{R}^m$ ,

$$
d^\top(\mathrm{Diag}(p)-pp^\top)d = \sum_i p_i d_i^2 - \left(\sum_i p_i d_i\right)^2 = \mathrm{Var}_p(d)\ \ge 0.
$$

Variance is always nonnegative. Hence Hessian PSD, so  $f$  convex.

### Engineering hook

Constraints of the form

$$
\log\sum_i e^{a_i^\top x + b_i} \le 0
$$

or

$$
\sum_i e^{a_i^\top x + b_i} \le 1
$$

show up after GP log-transform (Phase 7).

* * *

**2.8.6 Logarithm and negative log (barriers)**
===============================================

2.8.6.1  $\log x$  is concave on  $x>0$ 
----------------------------------------

Second derivative:

$$
(\log x)'' = -\frac{1}{x^2}<0.
$$

So concave.

2.8.6.2  $-\log x$  is convex on  $x>0$ 
----------------------------------------

Second derivative:

$$
(-\log x)'' = \frac{1}{x^2}>0.
$$

So convex.

2.8.6.3  $-\log(b-a^\top x)$  is convex on domain  $b-a^\top x>0$ 
------------------------------------------------------------------

We computed in 2.6:

$$
\nabla^2 f(x)=\frac{aa^\top}{(b-a^\top x)^2}\succeq 0.
$$

So convex. This is the exact atom for log barriers in 4.2.

### Engineering hook

Barriers aren’t typically conic-represented directly; instead, they justify interior-point method objectives. But you must certify convexity of sums of these terms using Hessian addition.

* * *

**2.8.7 Power functions (where convexity flips depending on exponent)**
=======================================================================

On  $\mathbb{R}_{++}$ , consider  $f(x)=x^p$ .

*   If  $p\ge 1$ ,  $f$  is convex on  $x>0$ .
*   If  $0<p\le 1$ ,  $f$  is concave on  $x>0$ .
*   If  $p<0$ ,  $f$  is convex on  $x>0$  (e.g.  $1/x$ ).

Proof is 1D second derivative:

$$
f''(x)=p(p-1)x^{p-2}.
$$

Sign depends on  $p(p-1)$ .

### Engineering hook

These appear in GP monomials after log transform; also in inequality modeling where you must know whether a power is convex.

* * *

**2.8.8 Indicator functions (constraints as functions)**
========================================================

This is the bridge between sets and functions and explains why extended-valued functions matter.

Given a set  $C\subseteq\mathbb{R}^n$ , define its indicator:

$$
\delta_C(x)= \begin{cases} 0,& x\in C,\\ +\infty,& x\notin C. \end{cases}
$$

### Claim

$$
\boxed{\delta_C \text{ is convex } \iff C \text{ is convex}.}
$$

Proof:

*    $\mathrm{epi}(\delta_C)=\{(x,t): x\in C,\ 0\le t\}$ , which is  $C\times \mathbb{R}_+$  (a product of sets).
*   Convexity of epi is equivalent to convexity of  $C$ .

### Engineering hook

A constrained problem

$$
\min_{x\in C} f(x)
$$

is the same as unconstrained

$$
\min_x f(x)+\delta_C(x).
$$

This is not just aesthetics—it’s how proximal methods and duality are formulated.

* * *

**2.8.9 A compact “recognition list” (the PS6 reflex core)**
============================================================

You should instantly recognize these as convex (with domains):

*   Affine  $a^\top x+b$  (everywhere).
*   PSD quadratic  $\tfrac12 x^\top Qx + c^\top x$  with  $Q\succeq0$ .
*   Norms  $\|x\|$  (everywhere).
*   Max of affine functions  $\max_i(a_i^\top x+b_i)$ .
*   Exponential  $e^{a^\top x+b}$ .
*   Log-sum-exp  $\log\sum_i e^{a_i^\top x+b_i}$ .
*   Negative log barrier  $-\log(b-a^\top x)$  on  $b-a^\top x>0$ .
*   Reciprocal  $1/x$  on  $x>0$ .
*   Indicator  $\delta_C$  iff  $C$  convex.

Each of these becomes a “building block” used with operations (Phase 2.9).

* * *

**2.8.10 Common failure modes (library-specific)**
==================================================

1.  **Forgetting domain**  
     $-\log x$  is not convex on all  $\mathbb{R}$ ; it’s convex on  $x>0$ . Same for  $1/x$ ,  $x^p$  with non-integer  $p$ .
2.  **Assuming max of convex is convex but messing the modeling**  
    Max of convex functions is convex, but epigraph form must be done with a shared  $t$  and all constraints  $f_i(x)\le t$ .
3.  **Confusing concavity of  $\log$  with convexity of  $-\log$ **  
    Log is concave; negative log is convex. Very common sign error.
4.  **Treating “sum of exponentials” as convex but then taking log incorrectly**  
     $\sum e^{x_i}$  is convex;  $\log\sum e^{x_i}$  is also convex (true), but you must justify it (we did via Hessian PSD).

* * *

Roadmap position
----------------

We completed **2.8 Standard convex functions library** with proofs and modeling hooks.

Next is **2.9 Convexity-preserving operations** (sums, maxima, affine precomposition, composition rules, perspective/partial minimization previews). This is where the library becomes a true “grammar” for building and certifying convex models mechanically.

## Response:
**2.9 — Convexity-preserving operations (the grammar of convex modeling)**
--------------------------------------------------------------------------

This section is where everything you’ve learned so far _locks together_.

Up to now, you have:

*   a precise definition of convex functions (2.1),
*   Jensen and mixtures (2.2),
*   epigraph equivalence (2.3),
*   subgradients and tangents (2.4–2.5),
*   second-order tests (2.6),
*   line restriction principle (2.7),
*   a library of certified convex atoms (2.8).

What remains is the **grammar**:

> Given convex building blocks, what operations can I apply that _guarantee_ the result is still convex?

PS6 lives here. Almost every modeling step is an application of one of the rules below. If you internalize these as _legal moves_, convexity stops being something you “hope” is true and becomes something you _certify mechanically_.

* * *

**2.9.0 The meta-rule (how to think about convexity preservation)**
===================================================================

Convexity preservation always comes from one of two geometric facts:

1.  **Epigraph geometry**  
    If an operation transforms epigraphs via intersection, affine mapping, projection, or Minkowski sum, convexity is preserved.
2.  **Line restriction principle (2.7)**  
    If, along every line, the resulting 1D function is convex, then the full function is convex.

Every rule below can be justified by one of these two principles. Nothing is magic.

* * *

**2.9.1 Nonnegative weighted sums**
===================================

### Statement

If  $f_1,\dots,f_m$  are convex and  $\alpha_i \ge 0$ , then

$$
f(x) := \sum_{i=1}^m \alpha_i f_i(x)
$$

is convex.

### Proof (epigraph / inequality)

Take any  $x,y$  and  $\theta\in[0,1]$ . Using convexity of each  $f_i$ :

$$
f_i(\theta x+(1-\theta)y) \le \theta f_i(x)+(1-\theta)f_i(y).
$$

Multiply by  $\alpha_i\ge0$  and sum:

$$
\sum_i \alpha_i f_i(\theta x+(1-\theta)y) \le \theta \sum_i \alpha_i f_i(x) + (1-\theta)\sum_i \alpha_i f_i(y).
$$

That is exactly convexity of  $f$ .

### Why nonnegativity matters

If some  $\alpha_i<0$ , the inequality reverses and convexity can fail. This is why objective weights must be nonnegative.

### PS6 relevance

*   Sum of squared residuals
*   Sum of Huber penalties
*   Sum of barrier terms
*   Weighted norm penalties

* * *

**2.9.2 Adding an affine function**
===================================

### Statement

If  $f$  is convex and  $a^\top x + b$  is affine, then

$$
g(x) = f(x) + a^\top x + b
$$

is convex.

### Reason

Affine functions are both convex and concave. Adding them does not bend curvature.

### Proof shortcut

This is a special case of 2.9.1 with one convex term and one affine term.

### PS6 relevance

*   Completing squares
*   Linear penalties
*   Lagrangian constructions (later)

* * *

**2.9.3 Pointwise maximum (supremum)**
======================================

### Statement

If  $\{f_i\}_{i\in I}$  is any family of convex functions (finite or infinite), then

$$
f(x) := \sup_{i\in I} f_i(x)
$$

is convex.

### Proof (epigraph geometry)

$$
\mathrm{epi}(f) = \bigcap_{i\in I} \mathrm{epi}(f_i).
$$

Each  $\mathrm{epi}(f_i)$  is convex. Intersection of convex sets is convex. Hence  $\mathrm{epi}(f)$  is convex, so  $f$  is convex.

### Special finite case

$$
f(x)=\max_{i=1,\dots,m} f_i(x)
$$

is convex.

### PS6 relevance

*   Worst-case objectives
*   Robust optimization
*   Piecewise-defined penalties (Huber)
*   Log-sum-exp as smooth max approximation

* * *

**2.9.4 Affine precomposition (one of the most used rules)**
============================================================

### Statement

If  $f:\mathbb{R}^m\to\mathbb{R}\cup\{+\infty\}$  is convex and

$$
g(x) = f(Ax + b),
$$

then  $g$  is convex.

### Proof (direct)

Let  $x,y\in\mathbb{R}^n$ . Then:

$$
g(\theta x+(1-\theta)y) = f(A(\theta x+(1-\theta)y)+b) = f(\theta(Ax+b)+(1-\theta)(Ay+b)).
$$

By convexity of  $f$ :

$$
\le \theta f(Ax+b)+(1-\theta)f(Ay+b) = \theta g(x)+(1-\theta)g(y).
$$

### Interpretation

Affine maps preserve line segments. Convexity is about line segments. Therefore convexity survives.

### PS6 relevance (huge)

*   Norms of affine residuals  $\|Ax-b\|$ 
*   Log barriers  $-\log(b-a^\top x)$ 
*   SOC constraints of the form  $\|Ax+b\|_2\le c^\top x+d$ 

* * *

**2.9.5 Partial minimization (projection of epigraph)**
=======================================================

This is subtle but extremely important conceptually.

### Statement

Let  $f(x,y)$  be jointly convex in  $(x,y)$ . Define

$$
g(x) := \inf_y f(x,y).
$$

Then  $g$  is convex (possibly extended-valued).

### Proof (epigraph projection)

$$
\mathrm{epi}(g) = \{(x,t): \exists y \text{ s.t. } f(x,y)\le t\}.
$$

This is the **projection** of  $\mathrm{epi}(f)$  onto  $(x,t)$ .  
Projection of a convex set is convex. Hence  $g$  is convex.

### PS6 relevance

*   Eliminating slack variables
*   Dual functions (later)
*   Value functions in parametric optimization

This rule explains _why epigraph modeling works_: introducing variables preserves convexity, and eliminating them does too.

* * *

**2.9.6 Composition rules (monotonic outer functions)**
=======================================================

This is the most delicate part. You must get monotonicity right.

### Scalar version (1D intuition first)

Let:

*    $h:\mathbb{R}\to\mathbb{R}$  be convex,
*    $g:\mathbb{R}^n\to\mathbb{R}$  be convex.

Then:

*   If  $h$  is **nondecreasing**,  $f(x)=h(g(x))$  is convex.
*   If  $h$  is **nonincreasing**, convexity generally fails.

### Multivariate version (formal)

Let  $h:\mathbb{R}^k\to\mathbb{R}$  be convex and **nondecreasing in each argument**, and let each  $g_i(x)$  be convex. Then:

$$
f(x)=h(g_1(x),\dots,g_k(x))
$$

is convex.

### Why monotonicity is essential

Convexity controls _averages_. Monotonicity ensures that inequalities propagate in the correct direction.

### Example (good)

$$
h(u,v)=u+v \quad \text{(convex, increasing)}
$$
 
$$
f(x)=\|Ax\|_2 + \|Bx\|_2
$$

Convex.

### Example (bad)

$$
h(u)= -u \quad \text{(convex but decreasing)}
$$
 
$$
f(x)=-\|x\|_2
$$

Concave, not convex.

### PS6 relevance

*   Norm sums
*   Log-sum-exp structure
*   Barrier composition rules

* * *

**2.9.7 Perspective transformation (preview, formal later)**
============================================================

This rule is so important it gets a full phase later, but you must see it now.

### Definition

Given convex  $f(x)$ , define its **perspective**:

$$
g(x,t)=t f(x/t),\quad t>0.
$$

### Fact

The perspective of a convex function is convex.

### Why this matters

*   Linear-fractional problems (Ex 4.7, 4.19)
*   Homogenization tricks
*   SOCP modeling of quadratic-over-linear terms

We will fully prove and use this later; for now, recognize it as a legal move.

* * *

**2.9.8 Operations that do _not_ preserve convexity (warning list)**
====================================================================

You must actively avoid these unless proven otherwise:

1.  **Product of variables**  $xy$  (generally nonconvex).
2.  **Difference of convex functions** (DC is not convex).
3.  **Composition with decreasing convex outer function**.
4.  **Convex in each variable separately** (does not imply joint convexity).
5.  **Nonaffine equality constraints** (destroy convexity).

PS6 often tests whether you accidentally allow one of these.

* * *

**2.9.9 A complete “legal moves checklist”**
============================================

When you build or analyze a function, ask:

*   Is it a nonnegative sum of convex atoms?
*   Is it a max/sup of convex functions?
*   Is it a convex function of an affine expression?
*   Is it obtained by partial minimization of a convex function?
*   Is it a monotone convex composition?
*   Is it a perspective of a convex function?

If yes → convex.  
If no → stop and re-analyze.

* * *

**2.9.10 Why Phase 2 is now complete**
======================================

At this point, you can:

*   certify convexity rigorously,
*   explain _why_ each rule works (epigraph or line restriction),
*   recognize convex structure without guessing,
*   avoid illegal transformations.

This completes **PHASE 2 — Geometry of costs**.

* * *

Roadmap checkpoint
------------------

**Phase 1:** convex sets — done  
**Phase 2:** convex functions — done

Next is **PHASE 3 — Norms and duality (the hidden engine)**.  
We start with **3.1 Norm axioms**, but now with a deeper goal: understanding why “worst-case over uncertainty sets” turns into norms and dual norms, which is the mathematical core of robust optimization in PS6.

## Response:
Updated saved memory

Understood. We are pausing **exactly at the boundary between Phase 2 and Phase 3**.

State of the roadmap at pause:

*   **Phase 1 (Convex sets): fully completed**
*   **Phase 2 (Convex functions): fully completed**
    *   2.1 Definition
    *   2.2 Jensen
    *   2.3 Epigraph equivalence
    *   2.4 Subgradients
    *   2.5 First-order condition
    *   2.6 Second-order (Hessian PSD)
    *   2.7 Line restriction principle
    *   2.8 Standard convex function library
    *   2.9 Convexity-preserving operations

The **very next subsection** to deliver, without recap or deviation, is:

> **PHASE 3 — Norms and duality (the hidden engine)**  
> **3.1 Norm axioms**

When we resume in the next chat, we will:

*   Start **directly at 3.1**, no repetition
*   Keep the **same gold-standard style**:
    *   zero-to-hero
    *   ultra-granular
    *   full proofs from first principles
    *   geometric intuition + algebra
    *   explicit PS6 relevance
*   Build toward:
    *   dual norms
    *   supremum = dual norm lemma
    *   robust optimization mechanics

The next message in the new chat should simply say something like:

> **Proceed 3.1**

and we will continue seamlessly.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)