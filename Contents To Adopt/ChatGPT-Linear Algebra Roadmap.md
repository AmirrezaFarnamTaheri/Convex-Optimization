# Linear Algebra Roadmap

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 16:07:24  
**Updated:** 12/28/2025 23:49:49  
**Exported:** 12/29/2025 0:14:33  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/6951244d-6ee8-832b-ae58-5c56a819bb0a](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/6951244d-6ee8-832b-ae58-5c56a819bb0a)  

## Response:
Below is a **newcomer-safe, zero-to-hero roadmap** that treats linear algebra the way it actually works in optimization, data, and theory: as **geometry plus operators**, not symbol juggling.  
This is designed so that each concept earns its place, and nothing appears before the intuition that makes it necessary.

I’ll give you:  
• the **big picture structure**,  
• the **dependency graph** (what must come first),  
• and a **step-by-step learning path** with precise goals at each stage.

Think of this as a curriculum you could literally turn into a book or course.

* * *

The big picture (why these five topics belong together)
-------------------------------------------------------

Eigenvalues, kernels, bases, SVD, and the Schur complement are not separate ideas. They are **different lenses on the same object**:

> a linear map as geometry.

Every matrix is secretly:

*   stretching space,
*   squashing space,
*   rotating space,
*   or collapsing space onto lower dimensions.

Each concept answers a specific geometric question:

| Concept | Question it answers |
| --- | --- |
| Basis | What coordinate system are we using? |
| Kernel (null space) | Which directions get crushed to zero? |
| Eigenvalues/vectors | Which directions stay on their own axis? |
| SVD | How does the map act in _optimal_ coordinates? |
| Schur complement | What happens when part of the system is eliminated? |

* * *

Roadmap overview (high level)
-----------------------------

We proceed in **four layers**, each one unavoidable.

**Layer 0 — Foundations (what a matrix really is)**  
**Layer 1 — Subspaces & bases (where things live)**  
**Layer 2 — Spectral structure (eigen & SVD)**  
**Layer 3 — Block structure & Schur complement**

Each layer builds exactly one new mental move.

* * *

Layer 0 — Linear maps, not matrices (absolute ground floor)
-----------------------------------------------------------

Goal: stop thinking of matrices as tables of numbers.

You learn:

*   Vectors as **points and arrows**
*   Linear maps as **rules that preserve addition and scaling**
*   Matrices as **representations of linear maps in a basis**

Critical idea:

> A matrix depends on the basis.  
> The linear map does not.

This is the philosophical backbone for everything that follows.

![https://mathigon.org/content/linear-algebra/images/transformations.svg](https://mathigon.org/content/linear-algebra/images/transformations.svg)

![https://ximera.osu.edu/la/LinearAlgebra/LTR-M-0080/main-figure0.svg](https://ximera.osu.edu/la/LinearAlgebra/LTR-M-0080/main-figure0.svg)

![https://www.3blue1brown.com/content/lessons/2016/3d-transformations/figures/three-dimensions/TransformMatrix.svg](https://www.3blue1brown.com/content/lessons/2016/3d-transformations/figures/three-dimensions/TransformMatrix.svg)

Only once this clicks does “changing basis” make sense later.

* * *

Layer 1 — Subspaces, span, basis, kernel
----------------------------------------

This layer answers: _what parts of space matter?_

### 1\. Span and subspaces

You learn:

*   Span as “everything you can build”
*   Subspace as “closed under addition and scaling”
*   Column space vs row space

Geometric rule:

> Subspaces are the _stable shapes_ of linear algebra.

### 2\. Basis (coordinate systems)

You learn:

*   A basis is **not special** — it’s a choice
*   Coordinates are bookkeeping, not geometry
*   Dimension = number of degrees of freedom

Key intuition:

> Choosing a basis is choosing how you look at the same object.

### 3\. Kernel (null space)

This is the first _structural_ concept.

You learn:

*   Kernel = directions that disappear
*   Rank–nullity theorem
*   Why non-invertibility is geometric

Critical sentence:

> The kernel is what the matrix destroys.

![https://pbs.twimg.com/media/F6fgLzDWgAAluOj.jpg](https://pbs.twimg.com/media/F6fgLzDWgAAluOj.jpg)

![https://boris-belousov.net/public/img/change_of_basis/basis-change.png](https://images.openai.com/thumbnails/url/FPPI13icu5mVUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7MNjItiihJdAlw9oh3dynItnAsNCpPdvLPDfcqcMz2NAx2tnAJM_GL8jUPT6wqTMw3VCsGAHBvJcQ)

![https://i.sstatic.net/10ein.jpg](https://images.openai.com/thumbnails/url/kxV5ZXicu5mZUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw5OzDJOiigwTylItvDMCjYqLDbzLAkuMUsOtYhMj8x0dC2zrIx3ybWINw22DPGLNy9WKwYAXN0l5g)

At the end of Layer 1, you can **see** why some systems have infinite solutions, none, or one.

* * *

Layer 2 — Eigenvalues and eigenvectors (fixed directions)
---------------------------------------------------------

Now we ask a deeper question:

> Are there directions that the transformation treats “cleanly”?

### 4\. Eigenvectors

You learn:

*   Definition from the equation  $Ax = \lambda x$ 
*   Why eigenvectors are **invariant directions**
*   Why most directions are mixtures of eigenvectors

Geometric meaning:

> Eigenvectors are axes the transformation respects.

### 5\. Eigenvalues

You learn:

*   Scaling factors along eigenvectors
*   Positive vs negative vs zero eigenvalues
*   Why zero eigenvalues link to the kernel

Crucial link:

> Kernel = eigenvalue 0.

### 6\. Diagonalization (when it works)

You learn:

*   What it means to diagonalize
*   Why diagonal matrices are trivial to understand
*   Why diagonalization sometimes fails

This naturally raises the question:

> What if eigenvectors are not enough?

That question **forces** SVD.

![https://www.geogebra.org/resource/Nkq8knZ9/hMg5Iq4qpGT7OVwW/material-Nkq8knZ9.png](https://www.geogebra.org/resource/Nkq8knZ9/hMg5Iq4qpGT7OVwW/material-Nkq8knZ9.png)

![https://media.geeksforgeeks.org/wp-content/uploads/20240719163402/Eigenvalues.png](https://media.geeksforgeeks.org/wp-content/uploads/20240719163402/Eigenvalues.png)

![https://understandinglinearalgebra.org/external/images/eigen-intro-A.svg](https://understandinglinearalgebra.org/external/images/eigen-intro-A.svg)

* * *

Layer 3 — Singular Value Decomposition (SVD): the universal answer
------------------------------------------------------------------

SVD is the most important idea here.

### 7\. Motivation for SVD

You learn:

*   Why eigenvalues fail for non-square or non-symmetric matrices
*   Why every matrix still has a clean geometric description

### 8\. The decomposition

You learn:

$$
A = U \Sigma V^T
$$

Meaning:

*    $V$ : rotate input space
*    $\Sigma$ : stretch/squash along orthogonal axes
*    $U$ : rotate output space

Key truth:

> Every linear map is “rotate → scale → rotate”.

### 9\. Singular values

You learn:

*   Singular values as magnitudes of action
*   Relation to eigenvalues of  $A^TA$ 
*   Rank, conditioning, stability

This explains:

*   PCA
*   least squares
*   low-rank approximation
*   numerical stability

![https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Singular-Value-Decomposition.svg/1200px-Singular-Value-Decomposition.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Singular-Value-Decomposition.svg/1200px-Singular-Value-Decomposition.svg.png)

![https://i.sstatic.net/pdZkU.png](https://images.openai.com/thumbnails/url/35y_l3icu5mVUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7xLQrKSk2OzChOqvQsKy6x8HApM6tIMnV18ii1KInyDays8nZ3DMyMLHVJCskzCK_wVSsGAKEaJzw)

![https://miro.medium.com/v2/resize%3Afit%3A1400/1%2A6wkgGgBy2NLVmRVOw8K86w.png](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2A6wkgGgBy2NLVmRVOw8K86w.png)

SVD unifies **kernel, rank, basis choice, and eigen-like behavior**.

* * *

Layer 4 — Block matrices and Schur complement
---------------------------------------------

Now comes the power tool used in optimization, statistics, and control.

### 10\. Block matrices

You learn:

*   Partitioning variables
*   Coupled systems
*   Why blocks appear naturally

### 11\. Schur complement

You learn:

*   Eliminating variables
*   When a block matrix is positive definite
*   Why it encodes conditional behavior

Core insight:

> The Schur complement is “what remains after solving part of the system”.

Geometric meaning:

*   Projecting out variables
*   Conditioning Gaussians
*   Feasibility of quadratic forms

This is why it appears everywhere in convex optimization and SDP.

![https://www.researchgate.net/publication/371337510/figure/fig1/AS%3A11431281165782765%401686072215518/Schematic-diagram-illustrating-the-block-LDU-decomposition-of-S-and-the-computation-of.png](https://tse1.mm.bing.net/th/id/OIP.I8QOn4ZeGVuAIALQGY1sYQHaD_?cb=ucfimg2&ucfimg=1&w=474&h=379&c=7&p=0)

![https://alecjacobson.com/weblog/media/schur-complement-trick-tilde.png](https://alecjacobson.com/weblog/media/schur-complement-trick-tilde.png)

![https://www.researchgate.net/publication/303759961/figure/fig1/AS%3A380420941205504%401467710828062/Computing-matrices-U-D-L-and-Schur-Complement-in-the-Backward-IJK-version-of.png](https://www.researchgate.net/publication/303759961/figure/fig1/AS%3A380420941205504%401467710828062/Computing-matrices-U-D-L-and-Schur-Complement-in-the-Backward-IJK-version-of.png)

* * *

Dependency graph (what depends on what)
---------------------------------------

```
Linear maps
   ↓
Subspaces & basis
   ↓
Kernel (null space)
   ↓
Eigenvectors & eigenvalues
   ↓
Diagonalization (partial)
   ↓
SVD (complete)
   ↓
Block matrices
   ↓
Schur complement
```

Nothing here is optional. Each concept solves a failure of the previous one.

* * *

How to _use_ this roadmap
-------------------------

If you follow this properly, you will:

*   never memorize eigenvalue formulas blindly,
*   understand why SVD is unavoidable,
*   see kernels instead of “rank deficiencies”,
*   treat Schur complements as geometry, not magic inequalities.

This is the same mental spine used in:

*   convex optimization (SDP, SOCP),
*   statistics (Gaussian conditioning),
*   numerical linear algebra,
*   modern machine learning.

Next natural continuation, if you want it:  
**turn this roadmap into a sequence of concrete problems**, where each idea is _forced_ to appear rather than introduced artificially.

## Response:
Alright. We start at **Layer 0: linear maps, not matrices**. This is the “if you skip this, everything later becomes memorization” layer.

I’ll build it from absolute basics, but rigorously: definitions → properties → consequences → how matrices arise → what changes when you change basis. Along the way I’ll keep a running geometric interpretation, because that’s what makes eigen/SVD/Schur feel inevitable instead of random.

* * *

0.0 What are we even studying?
------------------------------

### The object of study is a function, not a grid of numbers

A **matrix** is a way to _write down_ a particular kind of function.

The real object is a **linear map** (also called a linear transformation):

$$
T: V \to W
$$

where  $V$  and  $W$  are vector spaces (for now you can think  $V=\mathbb R^n$ ,  $W=\mathbb R^m$ ).

You should think:

*   Vectors live in  $V$  (inputs).
*    $T$  takes an input vector and outputs a vector in  $W$ .

The slogan:

> **A matrix is a coordinate representation of a linear map.**  
> The linear map is “basis-free reality”; the matrix is “how you describe it after choosing coordinates.”

Everything in eigenvalues/SVD/basis is just increasingly smart ways of choosing coordinates to reveal structure.

* * *

0.1 Vector spaces (minimal but real definitions)
------------------------------------------------

To be rigorous: a **real vector space**  $V$  is a set with two operations:

1.  vector addition  $+$ :  $V\times V\to V$ 
2.  scalar multiplication  $\cdot$ :  $\mathbb R\times V\to V$ 

satisfying the usual axioms (associativity, commutativity of addition, identity element, inverses, distributive laws, etc.).

For this roadmap, you can safely take  $V=\mathbb R^n$  and  $W=\mathbb R^m$ , where:

*   vectors are  $n$ \-tuples,
*   addition and scalar multiplication are componentwise.

But it’s important to know we’re not depending on coordinates yet.

* * *

0.2 Linear maps: the real definition
------------------------------------

A function  $T:V\to W$  is **linear** if for all  $x,y\in V$  and scalars  $\alpha,\beta\in\mathbb R$ ,

$$
T(\alpha x + \beta y)=\alpha T(x)+\beta T(y).
$$

Equivalent “two-rule” definition (often easier to check):

1.  **Additivity:**  $T(x+y)=T(x)+T(y)$ 
2.  **Homogeneity:**  $T(\alpha x)=\alpha T(x)$ 

These are equivalent because if both hold, then

$$
T(\alpha x+\beta y)=T(\alpha x)+T(\beta y)=\alpha T(x)+\beta T(y).
$$

Conversely, if the combined rule holds for all  $\alpha,\beta$ , then setting  $(\alpha,\beta)=(1,1)$  gives additivity and  $(\alpha,\beta)=(\alpha,0)$  gives homogeneity.

### Immediate consequences (tiny lemmas that matter later)

**Lemma 1:  $T(0)=0$ .**  
Proof:  $0 = 0\cdot x$ . Then  $T(0)=T(0\cdot x)=0\cdot T(x)=0$ .

**Lemma 2:  $T(-x)=-T(x)$ .**  
Proof:  $-x = (-1)x$ . Then  $T(-x)=T((-1)x)=(-1)T(x)=-T(x)$ .

**Lemma 3: linear maps preserve affine combinations through the origin.**  
If  $x=\sum_i \alpha_i x_i$ , then  $T(x)=\sum_i \alpha_i T(x_i)$ .  
Proof is repeated application of linearity.

This is the heart of why bases work: if you know what  $T$  does to building blocks, you know what it does to everything.

* * *

0.3 Geometry: what linearity “means” in pictures
------------------------------------------------

Even before coordinates:

*   Additivity means “parallelograms map to parallelograms.”
*   Homogeneity means “scaling a vector scales its image by the same amount.”

So linear maps:

*   keep the origin fixed (since  $T(0)=0$ ),
*   send lines through the origin to lines through the origin,
*   send subspaces to subspaces,
*   preserve “straightness” and “centered” combinations.

They do **not** generally preserve:

*   lengths,
*   angles,
*   areas/volumes (unless special types like orthogonal maps).

This is why later we care about eigenvalues (stretching factors) and SVD (optimal stretch directions).

* * *

0.4 The key idea: a basis lets you reduce everything to coordinates
-------------------------------------------------------------------

### What a basis is (no shortcuts)

A set of vectors  $\{v_1,\dots,v_n\}\subset V$  is a **basis** if:

1.  (Spanning) Every  $x\in V$  can be written as
    
$$
x = \sum_{i=1}^n c_i v_i
$$

for some scalars  $c_i$ .

2.  (Linear independence) The representation is unique:
    
$$
\sum_{i=1}^n c_i v_i = 0 \implies c_1=\cdots=c_n=0.
$$

Uniqueness is crucial: “coordinates” only make sense if one point corresponds to one coordinate vector.

If  $\{v_i\}$  is a basis, then the scalars  $(c_1,\dots,c_n)$  are called the **coordinates of  $x$  in that basis**.

We write:

$$
[x]_{\mathcal B} = \begin{bmatrix}c_1\\ \vdots \\ c_n\end{bmatrix}
$$

where  $\mathcal B=(v_1,\dots,v_n)$ .

This map  $x \mapsto [x]_{\mathcal B}$  is itself a bijection between the abstract vector space and  $\mathbb R^n$ .

* * *

0.5 How a matrix appears from a linear map (the core derivation)
----------------------------------------------------------------

Now the main theorem of Layer 0:

### Theorem (matrix representation)

Let  $T:V\to W$  be linear.  
Fix a basis  $\mathcal B=(v_1,\dots,v_n)$  for  $V$  and a basis  $\mathcal C=(w_1,\dots,w_m)$  for  $W$ .

Then there exists a unique matrix  $A\in\mathbb R^{m\times n}$  such that for every  $x\in V$ ,

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

This matrix  $A$  is called “the matrix of  $T$  in bases  $\mathcal B,\mathcal C$ .”

#### Proof (step-by-step, nothing hidden)

**Step 1: express any input using the domain basis.**  
Because  $\mathcal B$  is a basis, any  $x\in V$  can be written uniquely as

$$
x = \sum_{j=1}^n c_j v_j, \quad\text{so}\quad [x]_{\mathcal B} = \begin{bmatrix}c_1\\ \vdots \\ c_n\end{bmatrix}.
$$

**Step 2: apply  $T$  and use linearity.**

$$
T(x) = T\Big(\sum_{j=1}^n c_j v_j\Big) = \sum_{j=1}^n c_j T(v_j).
$$

**Step 3: express each  $T(v_j)$  in the codomain basis.**  
Since  $\mathcal C$  is a basis of  $W$ , each vector  $T(v_j)\in W$  has coordinates:

$$
[T(v_j)]_{\mathcal C} = \begin{bmatrix} a_{1j}\\ \vdots\\ a_{mj} \end{bmatrix}.
$$

These scalars  $a_{ij}$  are uniquely determined.

**Step 4: define the matrix by stacking these coordinate columns.**  
Let

$$
A := \begin{bmatrix} | & & | \\ [T(v_1)]_{\mathcal C} & \cdots & [T(v_n)]_{\mathcal C}\\ | & & | \end{bmatrix} \in\mathbb R^{m\times n}.
$$

So the  $j$ \-th column of  $A$  is exactly the coordinate vector of  $T(v_j)$ .

**Step 5: compute  $A[x]_{\mathcal B}$ .**  
Matrix multiplication by definition gives:

$$
A [x]_{\mathcal B} = A \begin{bmatrix}c_1\\ \vdots \\ c_n\end{bmatrix} = \sum_{j=1}^n c_j \, \text{(column }j\text{ of }A) = \sum_{j=1}^n c_j [T(v_j)]_{\mathcal C}.
$$

**Step 6: compare with coordinates of  $T(x)$ .**  
From Step 2,

$$
T(x)=\sum_{j=1}^n c_j T(v_j).
$$

Taking  $\mathcal C$ \-coordinates and using linearity of the coordinate map:

$$
[T(x)]_{\mathcal C} = \sum_{j=1}^n c_j [T(v_j)]_{\mathcal C}.
$$

But Step 5 showed that the right-hand side equals  $A[x]_{\mathcal B}$ . Therefore

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

**Uniqueness:** the columns of  $A$  are forced to be  $[T(v_j)]_{\mathcal C}$ . No other choice can satisfy the formula for all  $x$ .

That’s it. That’s the birth certificate of matrices.

* * *

0.6 The special case everyone starts with (standard coordinates)
----------------------------------------------------------------

Take:

*    $V=\mathbb R^n$ ,  $W=\mathbb R^m$ 
*   domain basis = standard basis  $e_1,\dots,e_n$ 
*   codomain basis = standard basis  $f_1,\dots,f_m$ 

Then the matrix  $A$  has columns:

$$
A_{:j} = T(e_j).
$$

And for any vector  $x=(x_1,\dots,x_n)$ ,

$$
x = \sum_{j=1}^n x_j e_j \quad\Rightarrow\quad T(x)=\sum_{j=1}^n x_j T(e_j)=\sum_{j=1}^n x_j A_{:j}=Ax.
$$

So the familiar formula  $T(x)=Ax$  is just the standard-basis version of the theorem.

* * *

0.7 The single most important warning: changing basis changes the matrix, not the map
-------------------------------------------------------------------------------------

Same map  $T$ . Different bases  $\mathcal B,\mathcal C$ . Different matrix.

This is why “the matrix” is not the real object. It’s a description.

### Change-of-basis matrix (exact meaning)

Let  $\mathcal B$  and  $\mathcal B'$  be two bases of  $V$ .  
There exists an invertible matrix  $P$  such that for all  $x\in V$ ,

$$
[x]_{\mathcal B} = P [x]_{\mathcal B'}.
$$

Interpretation:  $P$  converts coordinates from basis  $\mathcal B'$  to basis  $\mathcal B$ .

Similarly for  $W$ , bases  $\mathcal C,\mathcal C'$ , an invertible matrix  $Q$  satisfies

$$
[y]_{\mathcal C} = Q [y]_{\mathcal C'}.
$$

### Deriving how the matrix transforms

Suppose  $A$  represents  $T$  in  $(\mathcal B,\mathcal C)$ :

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

We want  $A'$  representing  $T$  in  $(\mathcal B',\mathcal C')$ :

$$
[T(x)]_{\mathcal C'} = A' [x]_{\mathcal B'}.
$$

Use the conversion relations:

$$
[T(x)]_{\mathcal C} = Q [T(x)]_{\mathcal C'}, \quad [x]_{\mathcal B} = P [x]_{\mathcal B'}.
$$

Plug into the first equation:

$$
Q [T(x)]_{\mathcal C'} = A \, P [x]_{\mathcal B'}.
$$

Multiply by  $Q^{-1}$ :

$$
[T(x)]_{\mathcal C'} = (Q^{-1} A P)\,[x]_{\mathcal B'}.
$$

So the new matrix is

$$
A' = Q^{-1} A P.
$$

This formula is not decoration. It is the mathematical statement of:

> “Same transformation, different coordinates.”

A famous special case: if  $V=W$  and you use the same basis change on both sides ( $\mathcal B'=\mathcal C'$ , and  $\mathcal B=\mathcal C$ ), then  $Q=P$  and:

$$
A' = P^{-1} A P,
$$

which is **similarity**—the backbone of eigenvalues.

So eigenvalues are really “things that don’t change under basis change.”

* * *

0.8 What you should be able to do after Layer 0
-----------------------------------------------

By the end of this layer, you should be fluent in these as _automatic_:

1.  Given a linear map  $T$  and a basis, you can build its matrix by computing  $T$  on basis vectors.
2.  You can explain why the  $j$ \-th column of  $A$  is  $T(e_j)$  (in standard coordinates).
3.  You understand: matrices multiply because it represents composition of linear maps.
4.  You can derive the change-of-basis relation  $A' = Q^{-1} A P$ , not memorize it.

These are the “atoms.” Everything later is compound molecules.

* * *

0.9 Preview: why this forces the next layer (subspaces/kernel)
--------------------------------------------------------------

Now that “matrix = linear map in coordinates” is settled, the next unavoidable question is:

A linear map doesn’t treat all directions equally. Some directions get:

*   preserved as a subspace,
*   sent to zero,
*   collapsed onto lower dimensions,
*   stretched more than others.

Those behaviors are described by **subspaces**:

*   image/column space,
*   kernel/null space,
*   rank-nullity.

So Layer 1 is: “what parts of space survive the map?”

That’s where kernel enters naturally.

* * *

If you want the strict roadmap progression: next message we go to **Layer 1.1** and start with **span, subspaces, and the idea of “solution sets are affine subspaces”**, then move to **basis** formally (again, but now as a tool), and then the **kernel** as the first structural invariant.

## Response:
Cool — we’ll zoom in and make Layer 0 _painfully_ clear and fully rigorous. The aim is that by the end, you can (i) derive the matrix representation theorem without “handwaving”, (ii) understand exactly what “coordinates” are as a linear isomorphism, (iii) prove why matrix multiplication corresponds to composition, and (iv) derive change-of-basis formulas from first principles, not memory.

I’ll proceed in small, logically sealed chunks: definition → lemma → proof → interpretation → (tiny example). No magic jumps.

* * *

Layer 0 (Deep Version): Linear maps are the reality; matrices are coordinates
-----------------------------------------------------------------------------

### 0.0 The “three-level” picture (this prevents 90% of confusion later)

There are three different things that people blur together:

1.  **Geometric vector** (basis-free object): an element  $x \in V$ .
2.  **Coordinates of a vector** in a chosen basis: a column  $[x]_{\mathcal B} \in \mathbb R^n$ .
3.  **A matrix**  $A$  that represents a linear map  $T$  _with respect to chosen bases_.

Key mantra (make this automatic):

*    $x$  is not the same as  $[x]_{\mathcal B}$ .
*    $T$  is not the same as the matrix  $A$ .
*   The only time you can write “ $T(x)=Ax$ ” without mental footnotes is when you silently identify  $x$  with its standard coordinates.

That identification is convenient, but it hides structure. We’ll expose it.

* * *

0.1 Vector spaces: what structure we truly need (minimal axioms)
----------------------------------------------------------------

Let  $V$  be a real vector space. That means:

*   You can add vectors:  $x+y\in V$ .
*   You can scale vectors:  $\alpha x \in V$ .

And the operations satisfy the axioms that make algebra behave: associativity, commutativity of addition, distributivity, existence of  $0$  and additive inverses, etc.

For now, you can picture  $V=\mathbb R^n$ , but our proofs won’t depend on coordinates.

* * *

0.2 Linear maps: definition and immediate consequences (proved, not asserted)
-----------------------------------------------------------------------------

### Definition (linearity)

A map  $T:V\to W$  is linear if for all  $x,y\in V$  and  $\alpha,\beta\in\mathbb R$ ,

$$
T(\alpha x+\beta y)=\alpha T(x)+\beta T(y).
$$

This is equivalent to the two axioms:

*   Additivity:  $T(x+y)=T(x)+T(y)$ 
*   Homogeneity:  $T(\alpha x)=\alpha T(x)$ 

#### Proof of equivalence (complete)

*   If the combined rule holds, set  $\alpha=\beta=1$  to get additivity, and set  $\beta=0$  to get homogeneity.
*   If additivity and homogeneity hold, then:
    $$
    T(\alpha x+\beta y)=T(\alpha x)+T(\beta y)=\alpha T(x)+\beta T(y).
    $$

### Lemma 0.2.1:  $T(0)=0$ .

Proof:

$$
0 = 0\cdot x \implies T(0)=T(0\cdot x)=0\cdot T(x)=0.
$$

### Lemma 0.2.2:  $T(-x)=-T(x)$ .

Proof:

$$
-x = (-1)x \implies T(-x)=T((-1)x)=(-1)T(x)=-T(x).
$$

### Lemma 0.2.3: linear maps preserve all finite linear combinations

If  $x=\sum_{j=1}^n c_j x_j$ , then  $T(x)=\sum_{j=1}^n c_j T(x_j)$ .

Proof by induction on  $n$ :

*   Base case  $n=1$  is homogeneity.
*   Step: write  $\sum_{j=1}^{n+1} c_j x_j = (\sum_{j=1}^n c_j x_j)+c_{n+1}x_{n+1}$ , apply additivity + induction + homogeneity.

This lemma is the engine of “knowing  $T$  on a basis determines it everywhere”.

* * *

0.3 “A linear map is determined by a basis” (precise theorem)
-------------------------------------------------------------

### Theorem 0.3.1 (determinacy by basis)

Let  $\mathcal B=(v_1,\dots,v_n)$  be a basis of  $V$ .  
If  $T,S:V\to W$  are linear and satisfy  $T(v_j)=S(v_j)$  for all basis vectors  $v_j$ , then  $T=S$  on all of  $V$ .

#### Proof (step-by-step)

Take any  $x\in V$ . Since  $\mathcal B$  is a basis, there exist unique scalars  $c_j$  such that  $x=\sum_{j=1}^n c_j v_j$ . Then:

$$
T(x)=T\Big(\sum_{j=1}^n c_j v_j\Big)=\sum_{j=1}^n c_j T(v_j)
$$

and similarly

$$
S(x)=\sum_{j=1}^n c_j S(v_j).
$$

But  $T(v_j)=S(v_j)$  for each  $j$ , so the sums are equal. Thus  $T(x)=S(x)$  for all  $x$ . QED.

Interpretation: **a linear map is fully specified by what it does to basis vectors.**

This is why matrices (columns) are enough.

* * *

0.4 Bases and coordinate maps (this is the real “coordinates” definition)
-------------------------------------------------------------------------

### Definition (basis)

A list  $\mathcal B=(v_1,\dots,v_n)$  is a basis if:

1.  (spanning) every  $x\in V$  can be written  $x=\sum_{j=1}^n c_j v_j$ ,
2.  (uniqueness) the coefficients are unique.

Uniqueness is equivalent to linear independence.

### Definition (coordinate map)

Fix a basis  $\mathcal B=(v_1,\dots,v_n)$ . Define the map

$$
\Phi_{\mathcal B}: V \to \mathbb R^n, \qquad \Phi_{\mathcal B}(x) = [x]_{\mathcal B}
$$

where  $[x]_{\mathcal B}$  is the unique coefficient vector  $c=(c_1,\dots,c_n)$  such that  $x=\sum_{j=1}^n c_j v_j$ .

So coordinates are not vague: they are **the output of a specific function**  $\Phi_{\mathcal B}$ .

Now we prove its critical properties.

### Lemma 0.4.1:  $\Phi_{\mathcal B}$  is linear.

Proof: Let  $x=\sum c_j v_j$  and  $y=\sum d_j v_j$ . Then

$$
\alpha x+\beta y=\sum_{j=1}^n (\alpha c_j+\beta d_j) v_j.
$$

By uniqueness of coordinates, the coordinate vector of  $\alpha x+\beta y$  is  $(\alpha c_j+\beta d_j)_j$ , i.e.

$$
[\alpha x+\beta y]_{\mathcal B} = \alpha [x]_{\mathcal B}+\beta [y]_{\mathcal B}.
$$

So  $\Phi_{\mathcal B}$  is linear. QED.

### Lemma 0.4.2:  $\Phi_{\mathcal B}$  is bijective (one-to-one and onto).

Proof:

*   Onto: given any  $c\in\mathbb R^n$ , define  $x=\sum c_j v_j$ . Then  $[x]_{\mathcal B}=c$ .
*   One-to-one: if  $[x]_{\mathcal B}=[y]_{\mathcal B}$ , then their coefficient vectors match, so  $x=y$  by uniqueness.

Thus  $\Phi_{\mathcal B}$  is a **linear isomorphism**.

### Definition (reconstruction map)

The inverse map  $\Psi_{\mathcal B} := \Phi_{\mathcal B}^{-1}$  sends coordinates back to the vector:

$$
\Psi_{\mathcal B}(c) = \sum_{j=1}^n c_j v_j.
$$

This is also linear.

So a basis gives you an explicit linear equivalence:

$$
V \;\cong\; \mathbb R^n
$$

but the isomorphism depends on the basis.

That’s what “choosing coordinates” _actually means_.

* * *

0.5 Matrix representation theorem (fully derived, no shortcuts)
---------------------------------------------------------------

Now we can state it cleanly.

### Theorem 0.5.1 (matrix of a linear map relative to bases)

Let  $T:V\to W$  be linear. Let  $\mathcal B=(v_1,\dots,v_n)$  be a basis for  $V$  and  $\mathcal C=(w_1,\dots,w_m)$  a basis for  $W$ .

Define the coordinate maps:

$$
\Phi_{\mathcal B}:V\to\mathbb R^n,\quad \Phi_{\mathcal C}:W\to\mathbb R^m.
$$

Then the composite map

$$
\mathbb R^n \xrightarrow{\;\Psi_{\mathcal B}\;} V \xrightarrow{\;T\;} W \xrightarrow{\;\Phi_{\mathcal C}\;} \mathbb R^m
$$

is a linear map from  $\mathbb R^n$  to  $\mathbb R^m$ , hence (and here is a known fact we can also prove) it must be multiplication by a unique matrix  $A\in\mathbb R^{m\times n}$ .

Concretely, for all  $x\in V$ :

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

#### Proof in two micro-steps

**Step 1: show the map from coordinates to coordinates is linear.**  
Define

$$
F := \Phi_{\mathcal C}\circ T \circ \Psi_{\mathcal B}:\mathbb R^n\to\mathbb R^m.
$$

Each piece is linear ( $\Psi_{\mathcal B}$  linear,  $T$  linear,  $\Phi_{\mathcal C}$  linear), and composition of linear maps is linear, so  $F$  is linear.

**Step 2: any linear map  $F:\mathbb R^n\to\mathbb R^m$  equals multiplication by a unique matrix.**  
We prove this from scratch:

Let  $e_1,\dots,e_n$  be the standard basis of  $\mathbb R^n$ . Any  $c\in\mathbb R^n$  can be written uniquely as  $c=\sum_{j=1}^n c_j e_j$ . Then by linearity:

$$
F(c)=F\Big(\sum_{j=1}^n c_j e_j\Big)=\sum_{j=1}^n c_j F(e_j).
$$

Now build a matrix  $A$  whose  $j$ \-th column is  $F(e_j)$ :

$$
A := \begin{bmatrix} | & & | \\ F(e_1) & \cdots & F(e_n) \\ | & & | \end{bmatrix}.
$$

Then by definition of matrix multiplication,

$$
Ac = \sum_{j=1}^n c_j A_{:j} = \sum_{j=1}^n c_j F(e_j)=F(c).
$$

So  $F(c)=Ac$  for all  $c$ . Uniqueness: if also  $F(c)=Bc$  for all  $c$ , then in particular  $F(e_j)=Be_j$  equals the  $j$ \-th column of  $B$ . But  $F(e_j)=Ae_j$  equals the  $j$ \-th column of  $A$ . Hence columns match, so  $A=B$ .

Now plug back:

$$
F([x]_{\mathcal B}) = [T(x)]_{\mathcal C}.
$$

But  $F(\cdot)=A(\cdot)$ . Therefore:

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

QED.

### What are the entries of  $A$ ?

They are literally the coordinates of  $T(v_j)$  in the codomain basis:

$$
A_{:j} = [T(v_j)]_{\mathcal C}.
$$

So “columns are images of basis vectors” is not a slogan; it’s a theorem.

* * *

0.6 Composition = matrix multiplication (proved, not asserted)
--------------------------------------------------------------

This is another foundational theorem that people memorize but rarely derive properly.

Let  $S:U\to V$ ,  $T:V\to W$  be linear maps. Choose bases:

*    $\mathcal A$  for  $U$ ,
*    $\mathcal B$  for  $V$ ,
*    $\mathcal C$  for  $W$ .

Let matrices represent them:

$$
[S(x)]_{\mathcal B} = B [x]_{\mathcal A}, \quad [T(y)]_{\mathcal C} = A [y]_{\mathcal B}.
$$

Then for  $x\in U$ ,

$$
[(T\circ S)(x)]_{\mathcal C} = [T(S(x))]_{\mathcal C} = A [S(x)]_{\mathcal B} = A (B [x]_{\mathcal A}) = (AB)[x]_{\mathcal A}.
$$

So the matrix of  $T\circ S$  is  $AB$ . That’s why multiplication is the right operation: it encodes composition.

* * *

0.7 Change of basis (constructed explicitly)
--------------------------------------------

Now we do change of basis with the same rigor: define the map, prove it’s invertible, derive formulas.

Let  $\mathcal B=(v_1,\dots,v_n)$  and  $\mathcal B'=(v'_1,\dots,v'_n)$  be two bases of  $V$ .

Define the **change-of-coordinates map** from  $\mathcal B'$ \-coordinates to  $\mathcal B$ \-coordinates:

$$
P := \Phi_{\mathcal B}\circ \Psi_{\mathcal B'} : \mathbb R^n \to \mathbb R^n.
$$

Interpretation:

*   Start with coordinates in  $\mathcal B'$ : a vector  $c' \in \mathbb R^n$ .
*   Reconstruct the actual vector:  $x=\Psi_{\mathcal B'}(c')$ .
*   Re-express it in basis  $\mathcal B$ :  $c=\Phi_{\mathcal B}(x)$ .  
    So  $c = Pc'$ .

### Lemma:  $P$  is linear and invertible.

*   Linear because it’s composition of linear maps.
*   Invertible because both  $\Phi_{\mathcal B},\Psi_{\mathcal B'}$  are invertible. In fact:
    
$$
P^{-1} = \Phi_{\mathcal B'}\circ \Psi_{\mathcal B}.
$$

### What are the columns of  $P$ ?

Take the standard basis  $e_j$  in  $\mathbb R^n$ . Then:

$$
P e_j = \Phi_{\mathcal B}(\Psi_{\mathcal B'}(e_j)).
$$

But  $\Psi_{\mathcal B'}(e_j)=v'_j$  (because  $e_j$  corresponds to “1 on  $v'_j$ , 0 on others”). So

$$
P e_j = [v'_j]_{\mathcal B}.
$$

So the  $j$ \-th column of  $P$  is “the coordinates of the new basis vector  $v'_j$  written in the old basis  $\mathcal B$ .”

This is how you compute  $P$  concretely.

* * *

0.8 How the matrix of a linear map transforms under basis change (derived cleanly)
----------------------------------------------------------------------------------

Let  $T:V\to W$ . Let  $\mathcal B,\mathcal B'$  be bases for  $V$  and  $\mathcal C,\mathcal C'$  bases for  $W$ .

Let:

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}
$$

and we want:

$$
[T(x)]_{\mathcal C'} = A' [x]_{\mathcal B'}.
$$

Define change-of-coordinates matrices:

$$
P := \Phi_{\mathcal B}\circ\Psi_{\mathcal B'} \quad\Rightarrow\quad [x]_{\mathcal B} = P [x]_{\mathcal B'},
$$
 
$$
Q := \Phi_{\mathcal C}\circ\Psi_{\mathcal C'} \quad\Rightarrow\quad [y]_{\mathcal C} = Q [y]_{\mathcal C'}.
$$

Now start from the known representation and substitute:

$$
[T(x)]_{\mathcal C} = A [x]_{\mathcal B}.
$$

Replace left side using  $[T(x)]_{\mathcal C} = Q [T(x)]_{\mathcal C'}$ , and right side using  $[x]_{\mathcal B} = P [x]_{\mathcal B'}$ :

$$
Q [T(x)]_{\mathcal C'} = A\, P [x]_{\mathcal B'}.
$$

Multiply by  $Q^{-1}$ :

$$
[T(x)]_{\mathcal C'} = (Q^{-1} A P) [x]_{\mathcal B'}.
$$

Therefore,

$$
A' = Q^{-1} A P.
$$

No memorization needed; it’s forced by definitions.

### Special case: similarity (why eigenvalues exist)

If  $V=W$  and you use the _same_ basis change on both sides (same space), then  $\mathcal C=\mathcal B$  and  $\mathcal C'=\mathcal B'$ , so  $Q=P$ . Then:

$$
A' = P^{-1} A P.
$$

This is similarity. Eigenvalues are quantities that stay invariant under this transformation.

So eigenvalues aren’t random: they’re “the numbers a linear map carries regardless of coordinates.”

* * *

0.9 Micro-examples (to anchor the abstraction)
----------------------------------------------

### Example 1: columns-as-images in standard basis

Let  $T:\mathbb R^2\to\mathbb R^2$  satisfy  $T(e_1)=(2,1)$ ,  $T(e_2)=(-1,3)$ .  
Then the matrix in standard basis is:

$$
A=\begin{bmatrix} 2 & -1 \\ 1 & 3\end{bmatrix}.
$$

For  $x = (x_1,x_2)=x_1 e_1 + x_2 e_2$ ,

$$
T(x)=x_1 T(e_1)+x_2 T(e_2)=x_1\binom{2}{1}+x_2\binom{-1}{3}=Ax.
$$

### Example 2: same map, different basis (matrix changes)

Let  $\mathcal B'=(v'_1,v'_2)$  with  $v'_1=(1,1)$ ,  $v'_2=(1,-1)$ .  
Compute change-of-basis matrix  $P$  from  $\mathcal B'$ \-coords to standard coords (standard =  $\mathcal B$ ):

Columns are  $[v'_1]_{\text{std}}=(1,1)$ ,  $[v'_2]_{\text{std}}=(1,-1)$ :

$$
P=\begin{bmatrix} 1 & 1\\ 1 & -1\end{bmatrix}.
$$

Then the new matrix is  $A' = P^{-1} A P$  (same space, same change both sides). The linear map didn’t change — only its coordinate description did.

This is the simplest “taste” of why choosing the _right_ basis can simplify  $A$  (diagonalize, SVD, etc.).

* * *

0.10 Checklist: what Layer 0 mastery actually means
---------------------------------------------------

You truly “have Layer 0” if you can do these from scratch:

1.  Given bases  $\mathcal B,\mathcal C$  and a linear map  $T$ , derive  $A_{:j}=[T(v_j)]_{\mathcal C}$ .
2.  Prove composition corresponds to multiplication.
3.  Define change-of-basis matrix via coordinate maps (not folklore) and compute its columns.
4.  Derive  $A' = Q^{-1}AP$ .
5.  Explain in one sentence why similarity is the right equivalence relation for “same linear map, different coordinates”.

* * *

Next, in Layer 1, we’ll make the map’s geometry explicit via subspaces: image, kernel, rank-nullity, and how solution sets to  $Ax=b$  are affine subspaces. That’s the bridge to eigen/SVD (because eigenvectors live inside invariant subspaces, and SVD is basically “pick orthonormal bases that expose image/kernel cleanly”).

## Response:
Thought for 10s

Layer 1 — Subspaces, span, bases, kernel (null space): “where things live”
--------------------------------------------------------------------------

Layer 0 gave you the core truth: **a matrix is a coordinate description of a linear map**.  
Layer 1 is where linear algebra stops being “arrays of numbers” and becomes **geometry of subspaces**.

The whole layer revolves around one meta-fact:

> Linear maps don’t act on individual vectors in isolation.  
> They act on whole _families of directions_ that form subspaces.

So we build, from scratch:

1.  linear combinations → span
2.  subspaces → why kernels/images are subspaces
3.  bases/dimension → how big these subspaces are
4.  solving  $Ax=b$  → affine sets + consistency
5.  rank–nullity → the size bookkeeping law that powers everything

I’ll go step-by-step and prove each nontrivial claim.

* * *

1.1 Linear combinations and span (the “construction rule”)
==========================================================

### Definition: linear combination

Given vectors  $v_1,\dots,v_k \in V$  and scalars  $c_1,\dots,c_k\in\mathbb R$ , the vector

$$
c_1 v_1 + \cdots + c_k v_k
$$

is a **linear combination** of the  $v_i$ .

This is the basic “allowed move” in a vector space.

### Definition: span

The **span** of a set  $S=\{v_1,\dots,v_k\}$  is the set of all linear combinations:

$$
\operatorname{span}(S) := \left\{\sum_{i=1}^k c_i v_i \;:\; c_i\in\mathbb R\right\}.
$$

Geometric intuition in  $\mathbb R^n$ :

*   one nonzero vector spans a line through the origin,
*   two non-collinear vectors span a plane through the origin,
*   etc.

### First key theorem: span is the smallest subspace containing the vectors

We haven’t defined subspace yet—good. We’ll define it next, then prove “span is the smallest one”.

* * *

1.2 Subspaces (the “stable shapes”)
===================================

### Definition: subspace

A subset  $U\subseteq V$  is a **subspace** if:

1.   $0\in U$  (contains the zero vector)
2.  closed under addition: if  $u_1,u_2\in U$  then  $u_1+u_2\in U$ 
3.  closed under scalar multiplication: if  $u\in U$  and  $\alpha\in\mathbb R$ , then  $\alpha u\in U$ 

These conditions are exactly what you need so that  $U$  itself behaves like a vector space (with the inherited operations).

### Lemma 1.2.1: If  $U$  is a subspace, then it is closed under all finite linear combinations.

If  $u_1,\dots,u_k\in U$  and  $c_1,\dots,c_k\in\mathbb R$ , then  $\sum c_i u_i\in U$ .

**Proof:**  
By closure under scalar multiplication, each  $c_i u_i\in U$ .  
By closure under addition, sums of elements of  $U$  stay in  $U$ . Induct on  $k$ . QED.

### Theorem 1.2.2:  $\operatorname{span}(S)$  is a subspace.

Let  $S=\{v_1,\dots,v_k\}$ . Then  $\operatorname{span}(S)\subseteq V$  is a subspace.

**Proof (check the three conditions):**

1.   $0\in \operatorname{span}(S)$  because  $0 = 0v_1+\cdots+0v_k$ .
2.  If  $x=\sum a_i v_i$  and  $y=\sum b_i v_i$ , then
    
$$
x+y=\sum (a_i+b_i)v_i \in \operatorname{span}(S).
$$
3.  If  $x=\sum a_i v_i$  and  $\alpha\in\mathbb R$ , then
    
$$
\alpha x = \sum (\alpha a_i) v_i \in \operatorname{span}(S).
$$

So it’s a subspace. QED.

### Theorem 1.2.3:  $\operatorname{span}(S)$  is the smallest subspace containing  $S$ .

Meaning:

*   it contains  $S$ , and
*   any subspace containing  $S$  must contain  $\operatorname{span}(S)$ .

**Proof:**  
Containment: each  $v_j\in S$  is in the span (take coefficient 1 for  $v_j$ , 0 for others).  
Minimality: if  $U$  is any subspace containing  $S$ , then by Lemma 1.2.1,  $U$  contains every linear combination of vectors in  $S$ . But that’s exactly  $\operatorname{span}(S)$ . QED.

This is why span is fundamental: it’s the “closure operator” under the allowed operations.

* * *

1.3 Linear independence, basis, and dimension (how big a subspace is)
=====================================================================

### Definition: linear independence

Vectors  $v_1,\dots,v_k$  are **linearly independent** if:

$$
c_1 v_1 + \cdots + c_k v_k = 0 \quad\Rightarrow\quad c_1=\cdots=c_k=0.
$$

If there exists a nontrivial combination giving 0, they are dependent.

Interpretation:

*   independent = none of them is “redundant”
*   dependent = at least one is a combination of the others (you can remove it without changing the span)

### Lemma 1.3.1: Dependence means one vector is in the span of the others.

If  $v_1,\dots,v_k$  are dependent, then for some  $j$ ,  $v_j \in \operatorname{span}(\{v_i:i\neq j\})$ .

**Proof:**  
Dependence gives scalars not all zero with  $\sum c_i v_i=0$ . Pick an index  $j$  with  $c_j\neq 0$ . Rearrange:

$$
c_j v_j = -\sum_{i\neq j} c_i v_i \quad\Rightarrow\quad v_j = \sum_{i\neq j} \left(-\frac{c_i}{c_j}\right)v_i.
$$

So  $v_j$  is in the span of the others. QED.

### Definition: basis (for a subspace too)

A list  $(b_1,\dots,b_r)$  is a **basis of a subspace**  $U\subseteq V$  if:

1.  it spans  $U$ :  $U=\operatorname{span}\{b_1,\dots,b_r\}$ ,
2.  it is linearly independent.

So a basis is a _minimal spanning set_ (no redundancy) and also a _maximal independent set_.

### Definition: dimension

The **dimension** of  $U$ , written  $\dim(U)$ , is the number of vectors in any basis of  $U$ .

Nontrivial fact: “any basis has the same size.” That requires a theorem (the Steinitz exchange lemma). I’ll give the core idea without drowning you yet:

*   Any independent set can be extended to a basis.
*   Any spanning set can be reduced to a basis.
*   Therefore, any two bases must have equal cardinality.

We’ll rely on this standard theorem when we do rank–nullity.

* * *

1.4 Kernel and image (the subspaces created by a linear map)
============================================================

Now we connect subspaces to linear maps. Let  $T:V\to W$  be linear.

### Definition: kernel (null space)

$$
\ker(T) := \{x\in V : T(x)=0\}.
$$

This is the set of directions that get sent to zero. It lives in the **domain**.

### Definition: image (range)

$$
\operatorname{im}(T) := \{T(x): x\in V\} \subseteq W.
$$

This is the set of outputs you can ever produce. It lives in the **codomain**.

### Theorem 1.4.1:  $\ker(T)$  is a subspace of  $V$ .

**Proof (three checks):**

1.   $0\in\ker(T)$  because  $T(0)=0$  (proved in Layer 0).
2.  If  $x,y\in\ker(T)$ , then  $T(x)=0$ ,  $T(y)=0$ . By linearity,
    
$$
T(x+y)=T(x)+T(y)=0+0=0,
$$

so  $x+y\in\ker(T)$ .  
3) If  $x\in\ker(T)$  and  $\alpha\in\mathbb R$ , then

$$
T(\alpha x)=\alpha T(x)=\alpha\cdot 0=0,
$$

so  $\alpha x\in\ker(T)$ . QED.

### Theorem 1.4.2:  $\operatorname{im}(T)$  is a subspace of  $W$ .

**Proof:**

1.   $0\in\operatorname{im}(T)$  because  $0=T(0)$ .
2.  If  $u=T(x)$  and  $v=T(y)$ , then
    
$$
u+v = T(x)+T(y)=T(x+y)\in\operatorname{im}(T).
$$
3.  If  $u=T(x)$ , then
    
$$
\alpha u = \alpha T(x)=T(\alpha x)\in\operatorname{im}(T).
$$

So it’s a subspace. QED.

### Coordinate-free invariance (important!)

Notice:  $\ker(T)$  and  $\operatorname{im}(T)$  are defined using only  $T$ , not any matrix.  
So they are **properties of the linear map**, not of a coordinate representation.

If you change basis and the matrix  $A$  changes to  $A'$ , the kernel as a set of geometric vectors is the same set; only its coordinate description changes.

* * *

1.5 Specializing to matrices: null space and column space
=========================================================

Now let’s set  $V=\mathbb R^n$ ,  $W=\mathbb R^m$  with standard bases, so  $T(x)=Ax$ .

Then:

*    $\ker(T)=\{x: Ax=0\}$  is the **null space** (or kernel) of  $A$ , often written  $N(A)$ .
*    $\operatorname{im}(T)=\{Ax: x\in\mathbb R^n\}$  is the **column space** of  $A$ , often written  $\operatorname{Col}(A)$ .

### Why “column space” literally means span of columns

Let the columns of  $A$  be  $a_1,\dots,a_n \in \mathbb R^m$ .  
Take any  $x\in\mathbb R^n$  with entries  $x_1,\dots,x_n$ . Then

$$
Ax = x_1 a_1 + \cdots + x_n a_n.
$$

So every output is a linear combination of columns, i.e.

$$
\operatorname{Col}(A) = \operatorname{span}\{a_1,\dots,a_n\}.
$$

This is a fully rigorous equality:

*   “ $\subseteq$ ” because any  $Ax$  is a combo of columns,
*   “ $\supseteq$ ” because any combo  $\sum x_i a_i$  equals  $Ax$  for  $x=(x_i)$ .

So image/range = span of columns.

* * *

1.6 Solving  $Ax=b$ : the solution set is affine, and kernel controls all freedom
=================================================================================

This is where kernel stops being abstract and becomes your daily bread.

Consider the linear system:

$$
Ax=b.
$$

### 1.6.1 Consistency criterion (when does a solution exist?)

A solution exists **iff**

$$
b \in \operatorname{Col}(A).
$$

Because  $\operatorname{Col}(A)$  is exactly the set of all achievable right-hand sides  $Ax$ .

This is the cleanest “existence” statement possible.

### 1.6.2 If a solution exists, describe all solutions

Assume  $x_0$  is one particular solution:  $Ax_0=b$ .

Claim:

$$
\{x: Ax=b\} = x_0 + N(A),
$$

where  $N(A)=\{z:Az=0\}$ .

**Proof (two inclusions):**

*   “ $\subseteq$ ”: Let  $x$  be any solution, so  $Ax=b$ . Then:
    $$
    A(x-x_0)=Ax-Ax_0=b-b=0,
    $$
    so  $x-x_0\in N(A)$ . Thus  $x=x_0+z$  for some  $z\in N(A)$ .
*   “ $\supseteq$ ”: If  $z\in N(A)$ , then:
    $$
    A(x_0+z)=Ax_0+Az=b+0=b,
    $$
    so  $x_0+z$  is a solution.

So solutions form a **translate of the kernel**. QED.

### What “affine” means (precisely)

A set is a **subspace** if it passes through the origin and is closed under linear combinations.  
A set like  $x_0+N(A)$  usually does **not** pass through the origin (unless  $x_0=0$ ), but it’s still “flat”: it’s a subspace shifted by  $x_0$ . That’s an **affine subspace**.

This fact is one of the main reasons optimization problems with linear equality constraints are geometrically clean: feasible sets are affine slices.

* * *

1.7 Rank and nullity (dimensions of image and kernel)
=====================================================

Now we quantify how “big” these subspaces are.

### Definitions

*   **Rank** of  $T$  (or  $A$ ):  $\operatorname{rank}(T) := \dim(\operatorname{im}(T))$ .  
    For a matrix,  $\operatorname{rank}(A)=\dim(\operatorname{Col}(A))$ .
*   **Nullity**:  $\operatorname{nullity}(T) := \dim(\ker(T))$ .  
    For a matrix,  $\operatorname{nullity}(A)=\dim(N(A))$ .

Rank = number of independent output directions achievable.  
Nullity = number of independent input directions that get killed.

### Theorem 1.7.1 (Rank–Nullity)

If  $T:V\to W$  is linear and  $V$  is finite-dimensional, then

$$
\dim(V) = \dim(\ker(T)) + \dim(\operatorname{im}(T)).
$$

For  $A\in\mathbb R^{m\times n}$ :

$$
n = \operatorname{nullity}(A) + \operatorname{rank}(A).
$$

#### Proof (constructed step-by-step from bases)

Let  $\ker(T)$  have a basis  $(k_1,\dots,k_r)$ . So  $r=\dim(\ker(T))$ .

**Step 1: extend kernel basis to a basis of all of  $V$ .**  
This is a standard theorem: any independent set can be extended to a basis. So we can find vectors  $v_{r+1},\dots,v_n$  such that

$$
(k_1,\dots,k_r, v_{r+1},\dots,v_n)
$$

is a basis of  $V$ . Here  $n=\dim(V)$ .

**Step 2: look at the images of the “extra” basis vectors.**  
Consider the set in  $W$ :

$$
T(v_{r+1}),\dots,T(v_n).
$$

We claim these span  $\operatorname{im}(T)$ .

Take any  $y\in\operatorname{im}(T)$ . Then  $y=T(x)$  for some  $x\in V$ .  
Write  $x$  in the basis of  $V$ :

$$
x = \sum_{i=1}^r a_i k_i + \sum_{j=r+1}^n b_j v_j.
$$

Apply  $T$ :

$$
T(x)=\sum_{i=1}^r a_i T(k_i) + \sum_{j=r+1}^n b_j T(v_j).
$$

But each  $k_i\in\ker(T)$ , so  $T(k_i)=0$ . Therefore:

$$
T(x)=\sum_{j=r+1}^n b_j T(v_j),
$$

a linear combination of  $T(v_{r+1}),\dots,T(v_n)$ . Hence these images span  $\operatorname{im}(T)$ .

So:

$$
\operatorname{im}(T)=\operatorname{span}\{T(v_{r+1}),\dots,T(v_n)\}.
$$

**Step 3: show these spanning vectors are independent.**  
Suppose

$$
\sum_{j=r+1}^n b_j T(v_j)=0.
$$

By linearity, that means:

$$
T\Big(\sum_{j=r+1}^n b_j v_j\Big)=0.
$$

So the vector  $u:=\sum_{j=r+1}^n b_j v_j$  lies in  $\ker(T)$ .

But  $\ker(T)$  is spanned by  $k_1,\dots,k_r$ . So we can also write:

$$
u=\sum_{i=1}^r a_i k_i
$$

for some  $a_i$ .

Thus:

$$
\sum_{j=r+1}^n b_j v_j - \sum_{i=1}^r a_i k_i = 0.
$$

This is a linear combination of the full basis  
 $(k_1,\dots,k_r,v_{r+1},\dots,v_n)$   
equal to zero. Since it’s a basis, it is linearly independent, so **all coefficients must be zero**:

$$
b_{r+1}=\cdots=b_n=0 \quad \text{and} \quad a_1=\cdots=a_r=0.
$$

Hence  $T(v_{r+1}),\dots,T(v_n)$  are linearly independent.

**Step 4: conclude dimension.**  
We have found  $(n-r)$  vectors in  $\operatorname{im}(T)$  that are:

*   spanning, and
*   independent.

So they form a basis of  $\operatorname{im}(T)$ . Therefore:

$$
\dim(\operatorname{im}(T)) = n-r.
$$

Rearrange:

$$
n = r + (n-r) = \dim(\ker(T)) + \dim(\operatorname{im}(T)).
$$

QED.

This proof is worth owning because it’s the first time you see “extend a basis” used as a weapon.

* * *

1.8 Consequences you should internalize (these power later layers)
==================================================================

### 1.8.1 Injective ⇔ trivial kernel

 $T$  is one-to-one (injective) iff  $\ker(T)=\{0\}$ .

**Proof sketch:**

*   If  $\ker(T)=\{0\}$  and  $T(x)=T(y)$ , then  $T(x-y)=0$ , so  $x-y=0$ , so  $x=y$ .
*   If  $T$  injective and  $T(x)=0=T(0)$ , injectivity gives  $x=0$ .

So “no direction collapses” means injective.

### 1.8.2 For square matrices: invertible ⇔ rank  $=n$  ⇔ nullity  $=0$ 

If  $A\in\mathbb R^{n\times n}$ :

*    $A$  invertible ⇔  $N(A)=\{0\}$  ⇔  $\operatorname{rank}(A)=n$ .

Because by rank–nullity:

$$
n = \operatorname{rank}(A) + \operatorname{nullity}(A).
$$

So nullity  $0$  forces rank  $n$ , and vice versa.

### 1.8.3 Why eigenvalue 0 is kernel (preview link to Layer 2)

If  $Ax=\lambda x$  and  $\lambda=0$ , then  $Ax=0$ .  
So the eigenvectors for eigenvalue  $0$  are exactly the nonzero kernel vectors.

That’s one of the bridges: kernel ↔ spectrum.

* * *

1.9 What you should be able to do after Layer 1 (sanity checklist)
==================================================================

You “own Layer 1” if you can do these without guessing:

1.  Prove that a given set is a subspace (or prove it’s not) by checking the 3 axioms.
2.  Given a matrix  $A$ , explain why  $\operatorname{Col}(A)=\operatorname{span}\{\text{columns}\}$ .
3.  Explain why  $Ax=b$  has a solution iff  $b\in\operatorname{Col}(A)$ .
4.  Derive the full solution set  $x_0+N(A)$  once you have one solution.
5.  Prove rank–nullity the way we did (kernel basis → extend → images give a basis of the image).

* * *

What comes next (Layer 2 preview, no work yet)
----------------------------------------------

Layer 1 told you: the map kills a whole subspace (kernel) and reaches only a subspace (image).  
Layer 2 asks: inside the domain, are there “special directions” that the map does not mix—directions  $x$  such that  $Ax$  stays on the same line?

That is exactly the eigenvector idea.

When you’re ready, we’ll start Layer 2 at the real beginning: **invariant subspaces**, then **eigenvectors as 1D invariant subspaces**, then eigenvalues as scaling factors, then diagonalization as choosing a basis made of eigenvectors (when possible).

## Response:
Thought for 20s

Got it. Let’s turn Layer 1 into something you can _derive, not remember_. I’m going to go deeper in three ways:

1.  I’ll prove the “hidden” theorems we relied on (basis extension, exchange lemma, “all bases have same size”).
2.  I’ll show multiple equivalent characterizations (so you can recognize the same idea in different disguises).
3.  I’ll connect the geometry to computation (Gaussian elimination / pivots / free variables), because that’s how rank/nullity stop being abstract.

I’ll assume we’re in finite-dimensional real spaces (ultimately  $\mathbb R^n$ ), because that’s the setting for eigen/SVD/Schur in optimization.

* * *

1.0 The meta-picture of Layer 1
-------------------------------

A linear map  $T:V\to W$  creates two canonical subspaces:

*   **Kernel**  $\ker(T)\subseteq V$ : all directions that get annihilated.
*   **Image**  $\operatorname{im}(T)\subseteq W$ : all outputs that are attainable.

Layer 1 is the machinery that lets you say, precisely and provably:

*   what it means to be a “direction family” (subspace),
*   how to describe a subspace minimally (basis),
*   how big it is (dimension),
*   how a linear system’s solution set is shaped (affine translate of the kernel),
*   why sizes must satisfy  $\dim V = \dim\ker(T)+\dim\operatorname{im}(T)$  (rank–nullity).

Everything later (eigenvectors, SVD) is “choose bases adapted to these subspaces.”

* * *

1.1 Subspaces: the clean definition and the “one-line” test (proved)
--------------------------------------------------------------------

### Definition (subspace)

A subset  $U\subseteq V$  is a subspace if:

1.   $0\in U$ 
2.   $u,v\in U \Rightarrow u+v\in U$ 
3.   $u\in U,\alpha\in\mathbb R \Rightarrow \alpha u\in U$ 

This is the axiomatic “closed under the operations” definition.

### Equivalent characterization (often easier)

A subset  $U\subseteq V$  is a subspace **iff** it is nonempty and closed under _all_ linear combinations of two vectors:

$$
(\forall u,v\in U)(\forall \alpha,\beta\in\mathbb R)\quad \alpha u+\beta v\in U.
$$

#### Proof (equivalence)

**( $\Rightarrow$ )** Assume the 3 axioms. Then  $\alpha u\in U$  and  $\beta v\in U$  by scalar closure, and their sum is in  $U$  by additivity closure. So  $\alpha u+\beta v\in U$ .

**( $\Leftarrow$ )** Assume  $U$  is nonempty and closed under  $\alpha u+\beta v$ .

*   Pick some  $u_0\in U$ . Then  $0u_0+0u_0=0\in U$ .
*   Additivity: take  $\alpha=\beta=1$ .
*   Scalar closure: take  $\beta=0$ ,  $v=u_0$ , then  $\alpha u+0u_0=\alpha u\in U$ .  
    So the 3 axioms hold. QED.

This matters because when you see constraints like “ $Ax=0$ ” or “ $x^Ty=0$ ” you can test subspace-ness quickly.

### Common failure modes (worth internalizing)

*   Sets defined by **nonhomogeneous** equations like  $Ax=b$  with  $b\neq 0$  are generally **not** subspaces (they don’t contain  $0$ ). They are affine sets.
*   Inequalities like  $\|x\|\le 1$  give convex sets, not subspaces (not closed under scaling by 2).

* * *

1.2 Span: “closure under allowed operations” made explicit
----------------------------------------------------------

### Definition (span)

Given  $S=\{v_1,\dots,v_k\}\subset V$ ,

$$
\operatorname{span}(S)=\left\{\sum_{i=1}^k c_i v_i : c_i\in\mathbb R\right\}.
$$

### Theorem:  $\operatorname{span}(S)$  is a subspace

Proof is direct closure checking (you saw it). The key point is: a span is literally “all linear combinations,” so it’s automatically stable under making more linear combinations.

### Theorem (minimality):  $\operatorname{span}(S)$  is the smallest subspace containing  $S$ 

Formally:

1.   $S\subseteq \operatorname{span}(S)$ 
2.  If  $U$  is a subspace and  $S\subseteq U$ , then  $\operatorname{span}(S)\subseteq U$ .

The second part is the important one: any subspace containing the generators must contain all linear combinations (closure), therefore it must contain the span.

So: **span is the subspace generated by a set.**

* * *

1.3 Linear independence, dependence, and redundancy (with precise equivalences)
-------------------------------------------------------------------------------

### Definition (linear independence)

 $v_1,\dots,v_k$  are linearly independent if

$$
\sum_{i=1}^k c_i v_i=0 \implies c_1=\cdots=c_k=0.
$$

If there exists a nontrivial solution  $(c_i)\neq 0$ , they are dependent.

### Lemma: dependence ⇔ one vector lies in the span of the others

You saw the standard proof: if  $\sum c_i v_i=0$  with some  $c_j\neq 0$ , rearrange to solve  $v_j$  as a combination of the rest.

This is the “redundancy detector.” Dependent sets contain extra vectors you can delete without shrinking the span.

* * *

1.4 Basis: spanning + independence ⇔ unique coordinates (proved both directions)
--------------------------------------------------------------------------------

This is a big conceptual hinge, so I’ll prove the equivalence carefully.

Let  $U\subseteq V$  be a subspace.

### Definition (basis of  $U$ )

A list  $(b_1,\dots,b_r)\subset U$  is a basis if:

1.  it spans  $U$ :  $U=\operatorname{span}\{b_1,\dots,b_r\}$ 
2.  it is independent.

### Theorem: “basis” is equivalent to “every vector has a unique representation”

Claim:  $(b_1,\dots,b_r)$  is a basis of  $U$  iff every  $u\in U$  can be written uniquely as

$$
u=\sum_{i=1}^r c_i b_i.
$$

#### Proof

**( $\Rightarrow$ )** If it’s a basis, spanning gives existence. For uniqueness: suppose

$$
\sum_{i=1}^r c_i b_i=\sum_{i=1}^r d_i b_i.
$$

Bring to one side:

$$
\sum_{i=1}^r (c_i-d_i)b_i=0.
$$

Independence forces  $c_i-d_i=0$  for all  $i$ , so  $c_i=d_i$ . Unique.

**( $\Leftarrow$ )** If every  $u\in U$  has a unique representation, then:

*   existence implies spanning;
*   uniqueness implies independence (because if  $\sum c_i b_i=0$  and not all  $c_i$  are zero, then  $0$  would have two distinct representations: all-zero coefficients and  $(c_i)$ ).  
    So it’s a basis. QED.

This is why bases are “coordinate systems.”

* * *

1.5 Dimension: why “number of basis vectors” is well-defined (Exchange Lemma)
-----------------------------------------------------------------------------

To use rank–nullity rigorously, we need the theorem: any two bases of the same finite-dimensional subspace have the same size. That is not trivial; it’s based on the **Steinitz Exchange Lemma**.

### Lemma (Steinitz Exchange / dimension inequality)

Let  $V$  be finite-dimensional. If

*    $L=\{\ell_1,\dots,\ell_k\}$  is linearly independent,
*    $S=\{s_1,\dots,s_m\}$  spans  $V$ ,

then  $k \le m$ .

This implies: any independent set can’t be larger than any spanning set.

#### Proof (constructive, finite-dimensional)

We’ll do a step-by-step “exchange” proof.

Start with spanning set  $S=(s_1,\dots,s_m)$ .

Because  $L$  is independent,  $\ell_1\neq 0$ . Since  $S$  spans  $V$ , we can write

$$
\ell_1 = \sum_{j=1}^m a_j s_j
$$

with not all  $a_j=0$ . Pick an index  $j_1$  with  $a_{j_1}\neq 0$ . Solve for  $s_{j_1}$ :

$$
s_{j_1}=\frac{1}{a_{j_1}}\left(\ell_1 - \sum_{j\neq j_1} a_j s_j\right).
$$

This shows  $s_{j_1}$  lies in the span of  $\ell_1$  and the other  $s_j$ ’s. Therefore, if we replace  $s_{j_1}$  by  $\ell_1$ , the new set still spans  $V$ . Concretely, define:

$$
S^{(1)} := \{\ell_1\}\cup (S\setminus\{s_{j_1}\}).
$$

Then  $S^{(1)}$  still spans  $V$ , and it still has size  $m$ .

Now repeat with  $\ell_2$ . Because  $S^{(1)}$  spans  $V$ , write  $\ell_2$  as a combination of  $S^{(1)}$ . If the coefficient of  $\ell_1$  in that combination is nonzero, it’s okay; the key is: there must be at least one element of  $S^{(1)}$  with nonzero coefficient that is not already “locked in” in a way that breaks independence. The exchange lemma guarantees you can always swap out some remaining  $s_j$ . Iterating, you can insert  $\ell_1,\dots,\ell_k$  one by one while keeping the set size at  $m$  and spanning.

But you cannot insert more than  $m$  independent vectors into a set of size  $m$  (once you’ve replaced all  $m$  elements, you’re done). Formally, after  $m$  swaps there is nothing left to swap. Hence  $k\le m$ . QED.

### Corollary: all bases have the same size

Let  $B$  and  $B'$  be bases of  $V$ .

*    $B$  is independent;  $B'$  spans. Exchange lemma gives  $|B|\le |B'|$ .
*   swap roles to get  $|B'|\le |B|$ .  
    So  $|B|=|B'|$ . This common number is  $\dim(V)$ .

Now dimension is genuinely well-defined.

* * *

1.6 Kernel and image: why they are subspaces (and why that’s structural)
------------------------------------------------------------------------

Let  $T:V\to W$  be linear.

### Kernel

$$
\ker(T)=\{x\in V:\;T(x)=0\}.
$$

#### Theorem:  $\ker(T)$  is a subspace of  $V$ 

Proof: already done, but note what’s really happening: the defining condition is a homogeneous linear equation  $T(x)=0$ . Homogeneous linear constraints always define subspaces.

### Image

$$
\operatorname{im}(T)=\{T(x):x\in V\}.
$$

#### Theorem:  $\operatorname{im}(T)$  is a subspace of  $W$ 

Proof: closure comes from linearity:

$$
T(\alpha x+\beta y)=\alpha T(x)+\beta T(y).
$$

So linear combinations of reachable outputs are reachable.

So kernel and image are not “random sets”: they are _the_ natural subspaces produced by a linear map.

* * *

1.7 Matrix specialization: column space, null space, row space
--------------------------------------------------------------

Let  $A\in\mathbb R^{m\times n}$  and  $T(x)=Ax$ .

*   Null space  $N(A)=\{x\in\mathbb R^n:Ax=0\}$  is  $\ker(T)$ .
*   Column space  $\operatorname{Col}(A)=\{Ax:x\in\mathbb R^n\}$  is  $\operatorname{im}(T)$ .

### Theorem:  $\operatorname{Col}(A)=\operatorname{span}\{\text{columns of }A\}$ 

Write columns  $a_1,\dots,a_n$ . For  $x=(x_1,\dots,x_n)$ ,

$$
Ax = x_1 a_1+\cdots+x_n a_n.
$$

So outputs are exactly linear combinations of columns.

### Row space (will matter for SVD)

The **row space** is the span of rows of  $A$ , a subspace of  $\mathbb R^n$ . Often written  $\operatorname{Row}(A)$ .

This is tied to constraints and orthogonality (next section).

* * *

1.8 Solving  $Ax=b$ : consistency, affine structure, and “all freedom = kernel”
-------------------------------------------------------------------------------

### Consistency criterion

$$
Ax=b \text{ has a solution } \iff b\in\operatorname{Col}(A).
$$

Because  $\operatorname{Col}(A)$  is exactly all attainable right-hand sides.

### Full solution set structure

Assume  $x_0$  is one solution ( $Ax_0=b$ ). Then:

$$
\{x:Ax=b\}=x_0+N(A).
$$

#### Proof (complete)

*   If  $Ax=b$ , then  $A(x-x_0)=Ax-Ax_0=b-b=0$ , so  $x-x_0\in N(A)$ , hence  $x=x_0+z$ .
*   If  $z\in N(A)$ , then  $A(x_0+z)=Ax_0+Az=b+0=b$ .

So feasible solutions form an affine subspace: a translated kernel.

### Definition (affine subspace)

A set  $S\subseteq \mathbb R^n$  is affine if it can be written as  $x_0+U$  where  $U$  is a subspace. Equivalently: for any  $x,y\in S$ , the whole line  $\{(1-t)x+ty:t\in\mathbb R\}\subseteq S$ .

(You can prove equivalence; it’s a useful exercise because it trains your “subspace vs affine” radar.)

* * *

1.9 Rank and nullity: dimensions of image and kernel
----------------------------------------------------

Define:

*    $\operatorname{rank}(T)=\dim(\operatorname{im}(T))$ 
*    $\operatorname{nullity}(T)=\dim(\ker(T))$ 

For matrices  $A\in\mathbb R^{m\times n}$ :

*    $\operatorname{rank}(A)=\dim(\operatorname{Col}(A))$ 
*    $\operatorname{nullity}(A)=\dim(N(A))$ 

Now the central law.

* * *

1.10 Rank–Nullity theorem: two rigorous proofs
----------------------------------------------

### Proof 1 (basis extension proof — structural)

Let  $V$  have dimension  $n$ . Let  $\ker(T)$  have basis  $(k_1,\dots,k_r)$ , so  $r=\dim\ker(T)$ .

1.  Extend this basis to a basis of  $V$ :  
    Using the basis extension theorem (which is a corollary of the exchange lemma), choose vectors  $v_{r+1},\dots,v_n$  such that
    $$
    (k_1,\dots,k_r,v_{r+1},\dots,v_n)
    $$
    is a basis of  $V$ .
2.  Claim:  $T(v_{r+1}),\dots,T(v_n)$  form a basis of  $\operatorname{im}(T)$ .
    *   Spanning: take any  $y\in\operatorname{im}(T)$ . Then  $y=T(x)$  for some  $x$ . Write  $x$  in that basis:
        $$
        x=\sum_{i=1}^r a_i k_i+\sum_{j=r+1}^n b_j v_j.
        $$
        Apply  $T$ :
        $$
        T(x)=\sum_{i=1}^r a_i T(k_i)+\sum_{j=r+1}^n b_j T(v_j)=\sum_{j=r+1}^n b_j T(v_j)
        $$
        because  $T(k_i)=0$ . So the images span.
    *   Independence: suppose  $\sum_{j=r+1}^n b_j T(v_j)=0$ . Then
        $$
        T\left(\sum_{j=r+1}^n b_j v_j\right)=0
        $$
        so  $u:=\sum_{j=r+1}^n b_j v_j\in\ker(T)$ . But  $\ker(T)=\operatorname{span}(k_1,\dots,k_r)$ , so  $u=\sum_{i=1}^r a_i k_i$ . Hence:
        $$
        \sum_{j=r+1}^n b_j v_j-\sum_{i=1}^r a_i k_i=0.
        $$
        Since the combined list is a basis (independent), all coefficients must be zero, so all  $b_j=0$ . Thus the images are independent.

Therefore  $\dim(\operatorname{im}(T)) = n-r$ . Rearranging:

$$
n = r + (n-r) = \dim(\ker(T))+\dim(\operatorname{im}(T)).
$$

QED.

### Proof 2 (Gaussian elimination / RREF proof — computational)

Let  $A\in\mathbb R^{m\times n}$ . Put  $A$  into reduced row echelon form (RREF). Row operations do not change the solution space of  $Ax=0$  (they produce an equivalent system).

In RREF:

*   Suppose there are  $r$  pivot columns. Then  $\operatorname{rank}(A)=r$ . (Pivot columns correspond to a basis of the column space; equivalently, nonzero rows correspond to basis of row space; both give the same  $r$ .)
*   The remaining  $n-r$  columns correspond to **free variables**. Each free variable introduces one degree of freedom, hence the null space has dimension  $n-r$ .

So  $\operatorname{nullity}(A)=n-r$ , hence

$$
n = \operatorname{rank}(A)+\operatorname{nullity}(A).
$$

QED.

This second proof is important because it ties rank/nullity to “pivots and free variables,” which is how you’ll actually compute kernels and ranks in practice.

* * *

1.11 Deeper structural view: First Isomorphism Theorem (optional, but powerful)
-------------------------------------------------------------------------------

This is the cleanest conceptual explanation of rank–nullity.

Define an equivalence relation on  $V$ :

$$
x \sim y \iff x-y\in\ker(T).
$$

Equivalence classes are cosets  $x+\ker(T)$ . The set of all cosets forms the quotient space  $V/\ker(T)$ .

Define a map:

$$
\tilde T: V/\ker(T)\to \operatorname{im}(T), \quad \tilde T([x]) = T(x).
$$

You must check it’s **well-defined**: if  $[x]=[y]$ , then  $x-y\in\ker(T)$ , so  $T(x-y)=0$ , hence  $T(x)=T(y)$ . Good.

Then:

*    $\tilde T$  is linear,
*    $\tilde T$  is injective (kernel becomes trivial in the quotient),
*    $\tilde T$  is surjective by definition of image.

So  $V/\ker(T) \cong \operatorname{im}(T)$  (isomorphic vector spaces), hence:

$$
\dim(V/\ker(T))=\dim(\operatorname{im}(T)).
$$

But  $\dim(V/\ker(T)) = \dim(V)-\dim(\ker(T))$ . Therefore rank–nullity follows.

This is the “algebraic skeleton” behind the geometric picture.

* * *

1.12 Fundamental subspaces and orthogonality (this sets up SVD)
---------------------------------------------------------------

Now we use the inner product on  $\mathbb R^n$ :  $u\cdot v = u^T v$ .

There are four fundamental subspaces for  $A\in\mathbb R^{m\times n}$ :

*    $\operatorname{Col}(A)\subseteq \mathbb R^m$ 
*    $N(A)\subseteq \mathbb R^n$ 
*    $\operatorname{Row}(A)\subseteq \mathbb R^n$ 
*    $N(A^T)\subseteq \mathbb R^m$  (left null space)

Key orthogonality relations:

$$
N(A) = \operatorname{Row}(A)^\perp,\qquad N(A^T)=\operatorname{Col}(A)^\perp.
$$

Let me prove the first one (the second is analogous).

### Theorem:  $N(A) = \operatorname{Row}(A)^\perp$ 

Let rows of  $A$  be  $r_1^T,\dots,r_m^T$  (each  $r_i\in\mathbb R^n$ ).

*   If  $x\in N(A)$ , then  $Ax=0$ . The  $i$ \-th component of  $Ax$  is  $r_i^T x = r_i\cdot x$ . So  $r_i\cdot x=0$  for every row  $r_i$ . Hence  $x$  is orthogonal to every row, i.e. orthogonal to their span:  $x\in \operatorname{Row}(A)^\perp$ .
*   Conversely, if  $x\in \operatorname{Row}(A)^\perp$ , then  $r_i\cdot x=0$  for all rows, so each entry of  $Ax$  is 0, hence  $Ax=0$ . So  $x\in N(A)$ .

Thus equality holds. QED.

Why this matters: SVD is basically the process of choosing orthonormal bases that split  $\mathbb R^n$  into  $\operatorname{Row}(A)\oplus N(A)$  and  $\mathbb R^m$  into  $\operatorname{Col}(A)\oplus N(A^T)$ , with clean scaling between the “active” parts. This is the deep bridge from Layer 1 → SVD.

* * *

1.13 Layer 1 “you actually own it” checklist
--------------------------------------------

You don’t “know” Layer 1 unless you can do these without black-boxing:

*   Given a set defined by equations, decide subspace vs affine vs neither, and prove it.
*   Prove span minimality (smallest subspace containing a set).
*   Prove basis ⇔ unique representation.
*   Prove exchange lemma (at least at the level of understanding the swap argument).
*   Derive rank–nullity by basis extension **and** explain its computational meaning (pivots/free variables).
*   Prove  $N(A)=\operatorname{Row}(A)^\perp$  and  $N(A^T)=\operatorname{Col}(A)^\perp$ .

* * *

If you say “next” again, we’ll start **Layer 2** the same way: not “here’s the eigenvalue equation,” but the real beginning: **invariant subspaces**, then **1D invariant subspaces (eigenvectors)**, then eigenvalues as scaling factors, then when diagonalization works/fails, which naturally forces SVD.

## Response:
Thought for 14s

Layer 2 — Eigenvalues, eigenvectors, invariant subspaces, diagonalization
-------------------------------------------------------------------------

_(the “find coordinates where the map stops mixing directions” layer)_

Layer 1 taught you that a linear map  $T$  creates big, structural subspaces:  $\ker(T)$  and  $\operatorname{im}(T)$ . Layer 2 zooms in on a different kind of structure:

> Are there directions (or subspaces) that the map sends back into themselves?

This is the precise mathematical idea behind “eigenvectors”.

* * *

### 2.0 The real motivation (why eigenvectors exist as a concept)

Take a linear map  $T:V\to V$  (square matrix case  $A:\mathbb R^n\to\mathbb R^n$ ). Generically,  $T$  **mixes** coordinates: an input direction gets sent to some other direction. That makes the dynamics of repeated application hard:

$$
x,\; Ax,\; A^2x,\; A^3x,\dots
$$

If we could find coordinates where  $A$  acts _independently_ on each coordinate axis (no mixing), analysis becomes trivial. The ideal case is: in some basis, the matrix is diagonal.

Diagonal matrices are “no-mixing” matrices. If

$$
D=\mathrm{diag}(\lambda_1,\dots,\lambda_n),
$$

then

$$
D x = (\lambda_1 x_1,\dots,\lambda_n x_n),
$$

so each coordinate just scales. No coordinate interacts with any other.

Eigenvectors are the mechanism for discovering whether such a basis exists (or at least partially exists).

* * *

2.1 Invariant subspaces (the concept that eigenvectors are a special case of)
-----------------------------------------------------------------------------

### Definition (invariant subspace)

Let  $T:V\to V$  be linear. A subspace  $U\subseteq V$  is ** $T$ \-invariant** if

$$
T(U)\subseteq U.
$$

Meaning: whenever  $u\in U$ , the image  $T(u)$  stays inside the same subspace  $U$ .

Why this matters: if you restrict attention to  $U$ , the transformation never leaves it. So you can analyze the map “locally” on  $U$ .

### Examples you already know (from Layer 1)

*    $\ker(T)$  is invariant: if  $u\in\ker(T)$ , then  $T(u)=0\in\ker(T)$ .
*    $\operatorname{im}(T)$  is invariant: if  $y\in\operatorname{im}(T)$ , then  $y=T(x)$  for some  $x$ , so  $T(y)=T(T(x))=T^2(x)\in\operatorname{im}(T)$ .

So invariant subspaces are not exotic; they are everywhere.

* * *

2.2 Eigenvectors are 1-dimensional invariant subspaces
------------------------------------------------------

A 1D subspace looks like a line through the origin:

$$
U=\operatorname{span}\{v\}=\{\alpha v:\alpha\in\mathbb R\}.
$$

### Key fact

A line  $U=\operatorname{span}\{v\}$  is invariant under  $T$  **iff**  $T(v)$  lies on the same line, i.e.  $T(v)\in\operatorname{span}\{v\}$ .

But “lying on the same line” means:

$$
T(v)=\lambda v
$$

for some scalar  $\lambda$ .

That scalar is the eigenvalue.

### Definition (eigenvalue/eigenvector)

A nonzero vector  $v\neq 0$  is an **eigenvector** of  $T$  with **eigenvalue**  $\lambda\in\mathbb R$  (or  $\mathbb C$  if we allow complex) if:

$$
T(v)=\lambda v.
$$

For a matrix  $A$ , this is

$$
Av=\lambda v.
$$

Interpretation: the direction  $v$  does not get rotated into a different direction; it only gets scaled (and possibly flipped if  $\lambda<0$ ).

* * *

2.3 The eigenvalue equation is a kernel equation (link to Layer 1)
------------------------------------------------------------------

Start from

$$
Av=\lambda v.
$$

Bring everything to one side:

$$
Av-\lambda v=0.
$$

Factor out  $v$  using  $Iv=v$ :

$$
(A-\lambda I)v=0.
$$

So:

>  $v$  is an eigenvector with eigenvalue  $\lambda$   
> **iff**  $v\neq 0$  is in the kernel of  $A-\lambda I$ .

### Definition (eigenspace)

For a given  $\lambda$ , the set of all eigenvectors (plus 0) is

$$
E_\lambda := \ker(A-\lambda I).
$$

This is a subspace (kernel of a linear map), so everything from Layer 1 applies.

### Immediate consequences

*    $\lambda$  is an eigenvalue **iff**  $\ker(A-\lambda I)\neq \{0\}$ .
*   The eigenspace dimension  $\dim(E_\lambda)$  is the number of independent eigenvectors you get for that eigenvalue (this is later called geometric multiplicity).

### Special case:  $\lambda=0$ 

$$
E_0=\ker(A-0I)=\ker(A).
$$

So the kernel is exactly the eigenspace for eigenvalue 0.

That’s the clean bridge: Layer 1’s kernel becomes Layer 2’s “zero-eigenvalue structure”.

* * *

2.4 Why eigenvectors diagonalize (when they exist in full)
----------------------------------------------------------

Suppose  $A\in\mathbb R^{n\times n}$  has  $n$  linearly independent eigenvectors  $v_1,\dots,v_n$  with eigenvalues  $\lambda_1,\dots,\lambda_n$ .

Form the matrix

$$
V := [v_1\;\;v_2\;\;\cdots\;\;v_n].
$$

Because the columns are independent,  $V$  is invertible.

Now define

$$
\Lambda := \mathrm{diag}(\lambda_1,\dots,\lambda_n).
$$

### Claim (the diagonalization formula)

$$
AV = V\Lambda \quad\Longrightarrow\quad A = V\Lambda V^{-1}.
$$

#### Proof (step-by-step)

Look at  $AV$ . Multiplying a matrix by  $V$  stacks the images of the columns:

$$
AV = [Av_1\;\;Av_2\;\;\cdots\;\;Av_n].
$$

Because each  $v_i$  is an eigenvector:

$$
Av_i=\lambda_i v_i.
$$

So

$$
AV = [\lambda_1 v_1\;\;\lambda_2 v_2\;\;\cdots\;\;\lambda_n v_n].
$$

Now look at  $V\Lambda$ . Multiplying  $V$  by a diagonal matrix scales each column:

$$
V\Lambda = [\lambda_1 v_1\;\;\lambda_2 v_2\;\;\cdots\;\;\lambda_n v_n].
$$

So indeed  $AV=V\Lambda$ .

Finally, multiply on the right by  $V^{-1}$ :

$$
AVV^{-1}=V\Lambda V^{-1}\quad\Rightarrow\quad A=V\Lambda V^{-1}.
$$

### Meaning

If you use the eigenvector basis, the matrix becomes diagonal. That is exactly “choose coordinates where the map doesn’t mix directions.”

So the whole diagonalization question reduces to:

> Does  $A$  have enough linearly independent eigenvectors to form a basis?

If yes: diagonalizable.  
If not: not diagonalizable (over the chosen field).

* * *

2.5 How to _find_ eigenvalues: the determinant condition
--------------------------------------------------------

We know:

$$
(A-\lambda I)v=0
$$

has a nonzero solution  $v\neq 0$  **iff** the linear map  $A-\lambda I$  is not injective.

In finite dimensions, a square linear map is injective **iff** it’s invertible **iff** its determinant is nonzero. So eigenvalues satisfy:

$$
\det(A-\lambda I)=0.
$$

### Why “nontrivial solution ⇔ det = 0” is true (rigorous)

Let  $M\in\mathbb R^{n\times n}$ .

Claim:

$$
\exists v\neq 0 \text{ with } Mv=0 \quad \Longleftrightarrow\quad \det(M)=0.
$$
*   ( $\Rightarrow$ ) If  $Mv=0$  for some  $v\neq 0$ , then  $M$  is not injective. A linear map on  $\mathbb R^n$  is invertible iff it’s injective, so  $M$  is not invertible. A square matrix is invertible iff  $\det(M)\neq 0$ . Therefore  $\det(M)=0$ .
*   ( $\Leftarrow$ ) If  $\det(M)=0$ , then  $M$  is not invertible, hence not injective. Not injective means there exist  $v\neq 0$  and  $w$  with  $Mv=Mw$ . Subtract:  $M(v-w)=0$  with  $v-w\neq 0$ . So a nonzero kernel vector exists.

Apply with  $M=A-\lambda I$ . Then eigenvalues are exactly roots of

$$
p_A(\lambda):=\det(A-\lambda I).
$$

This polynomial  $p_A$  is the **characteristic polynomial**.

* * *

2.6 Similarity invariance (why eigenvalues are “real properties” of the map)
----------------------------------------------------------------------------

From Layer 0, changing basis transforms a matrix by similarity:

$$
A' = P^{-1}AP.
$$

This is the same linear map, different coordinates.

Eigenvalues should not depend on coordinates. Let’s prove they don’t.

### Theorem: similar matrices have the same characteristic polynomial (hence same eigenvalues)

Compute:

$$
\det(A' - \lambda I) = \det(P^{-1}AP - \lambda I).
$$

Insert  $I = P^{-1}P$ :

$$
A' - \lambda I = P^{-1}AP - \lambda P^{-1}P = P^{-1}(A-\lambda I)P.
$$

Take determinant:

$$
\det(A'-\lambda I) = \det(P^{-1}(A-\lambda I)P) = \det(P^{-1})\det(A-\lambda I)\det(P).
$$

But  $\det(P^{-1})\det(P)=1$ . So:

$$
\det(A'-\lambda I)=\det(A-\lambda I).
$$

Therefore the characteristic polynomial is basis-invariant, and eigenvalues are genuine invariants of the linear map.

This is the deep reason eigenvalues matter: they survive coordinate changes.

* * *

2.7 Multiplicities and “why diagonalization can fail”
-----------------------------------------------------

Even if you find eigenvalues, you might not get enough eigenvectors.

For an eigenvalue  $\lambda$ , two numbers matter:

1.  **Algebraic multiplicity**: how many times  $\lambda$  appears as a root of  $p_A(\lambda)$ .
2.  **Geometric multiplicity**:  $\dim(E_\lambda)=\dim(\ker(A-\lambda I))$ , i.e. how many independent eigenvectors you actually get.

Facts (important and provable):

*    $1 \le \dim(E_\lambda) \le$  algebraic multiplicity of  $\lambda$ .
*    $A$  is diagonalizable iff the sum of geometric multiplicities across distinct eigenvalues equals  $n$  (equivalently: you can pick  $n$  independent eigenvectors).

Diagonalization fails when an eigenvalue has too few eigenvectors compared to how many times it repeats algebraically.

(When you later meet Jordan form, it’s precisely a controlled way to describe this failure. But SVD will sidestep it for many applications.)

* * *

2.8 Two instructive examples (to anchor geometry)
-------------------------------------------------

### Example A: a diagonal matrix (everything is eigen)

Let

$$
A=\begin{bmatrix}2&0\\0&3\end{bmatrix}.
$$

Then

$$
Ae_1=2e_1,\quad Ae_2=3e_2.
$$

So eigenpairs:  $(\lambda,v)=(2,e_1)$  and  $(3,e_2)$ . The eigenvectors are coordinate axes.

Characteristic polynomial:

$$
\det(A-\lambda I)=\det\begin{bmatrix}2-\lambda&0\\0&3-\lambda\end{bmatrix}=(2-\lambda)(3-\lambda).
$$

### Example B: a pure rotation in  $\mathbb R^2$  (no real eigenvectors)

Let

$$
R=\begin{bmatrix}0&-1\\1&0\end{bmatrix},
$$

rotation by  $90^\circ$ . Every nonzero vector gets rotated to a perpendicular direction. No real line through the origin is invariant, so there are **no real eigenvectors**.

Characteristic polynomial:

$$
\det(R-\lambda I)=\det\begin{bmatrix}-\lambda&-1\\1&-\lambda\end{bmatrix}=\lambda^2+1,
$$

roots  $\lambda=\pm i$  (complex). Over  $\mathbb C$ , eigenvectors exist; over  $\mathbb R$ , they don’t.

This is one of the reasons SVD becomes the “always works over  $\mathbb R$ ” tool.

* * *

2.9 What Layer 2 should leave you able to do (operational checklist)
--------------------------------------------------------------------

You should be able to derive, not quote:

1.  Eigenvector definition ⇔ kernel condition:  
     $Av=\lambda v \iff (A-\lambda I)v=0$  with  $v\neq 0$ .
2.  Eigenvalues ⇔ determinant condition:  
     $\ker(A-\lambda I)\neq\{0\} \iff \det(A-\lambda I)=0$ .
3.  Diagonalization formula:  
    If  $Av_i=\lambda_i v_i$  and  $V=[v_i]$ , then  $AV=V\Lambda\Rightarrow A=V\Lambda V^{-1}$ .
4.  Similarity invariance:  
     $A' = P^{-1}AP \Rightarrow \det(A'-\lambda I)=\det(A-\lambda I)$ .
5.  The failure mode: repeated eigenvalues may yield too few eigenvectors; diagonalization requires a full eigenbasis.

* * *

### Bridge to the next layer (SVD is forced by eigen failures)

Layer 2 gave you the dream: “find a basis of eigenvectors and diagonalize.” But we just saw two major failure modes:

*   Some matrices are not diagonalizable (not enough eigenvectors).
*   Some real matrices have no real eigenvectors (e.g., rotations).

SVD is the next layer because it gives you:

> an always-valid decomposition over  $\mathbb R$ , using orthonormal bases, that measures stretching directions even when eigenvectors don’t behave nicely.

When you say “next,” we’ll start SVD from the correct starting point: not the formula  $A=U\Sigma V^T$  as magic, but why orthonormal bases + “stretch factors” are the right invariant geometry, and how it comes from eigenvalues of  $A^TA$ .

## Response:
Layer 3 — SVD (Singular Value Decomposition)
--------------------------------------------

_(the “always works” spectral geometry: rotate → scale → rotate)_

Eigenvalues were the dream: “find a basis where the map doesn’t mix directions.” The problem was: eigenvectors can fail (non-diagonalizable) or leave the real numbers (rotations).

SVD is the fix. It works for **every** real matrix  $A\in\mathbb R^{m\times n}$ , square or rectangular, diagonalizable or not. It gives you the clean geometric truth:

> Any linear map    $\;x \mapsto Ax\;$  can be written as  
> **(orthogonal rotate/reflect)** → **(axis-aligned scaling)** → **(orthogonal rotate/reflect)**.

I’ll derive it from scratch, with all key lemmas proved.

* * *

### 3.0 What SVD is trying to measure (before definitions)

For any nonzero input direction  $x$ , consider the “gain”:

$$
\frac{\|Ax\|_2}{\|x\|_2}.
$$

This ratio answers: “how much does  $A$  stretch vectors in direction  $x$ ?”  
If we constrain  $\|x\|_2=1$ , then we’re looking at  $\|Ax\|_2$ .

SVD finds:

*   the directions  $v$  where  $\|Av\|_2$  is extremal (max, then next max orthogonal to previous, etc.),
*   and the corresponding stretch factors.

Those “best stretch directions” are the **right singular vectors**.  
The stretch factors are the **singular values**.  
The images  $Av$  (normalized) are the **left singular vectors**.

All of that will fall out of one key object:  $A^T A$ .

* * *

3.1 Start from the one object that is always nice:  $A^T A$ 
------------------------------------------------------------

Let  $A\in\mathbb R^{m\times n}$ . Define

$$
G := A^T A \in \mathbb R^{n\times n}.
$$

Two crucial properties:

1.  **Symmetric:**  $G^T = (A^T A)^T = A^T (A^T)^T = A^T A = G.$ 
2.  **Positive semidefinite (PSD):** for every  $x\in\mathbb R^n$ ,
    
$$
x^T G x = x^T A^T A x = (Ax)^T (Ax) = \|Ax\|_2^2 \ge 0.
$$

So  $A^T A$  is always symmetric PSD. That’s the jackpot, because symmetric matrices have a complete eigen-decomposition with orthonormal eigenvectors.

* * *

3.2 Spectral theorem (the engine we will use)
---------------------------------------------

### Theorem (Spectral theorem for real symmetric matrices)

If  $G\in\mathbb R^{n\times n}$  is symmetric, then there exists an orthogonal matrix  $V\in\mathbb R^{n\times n}$  and a real diagonal matrix  $\Lambda$  such that

$$
G = V\Lambda V^T,
$$

where:

*    $V^T V = I$  (columns of  $V$  are orthonormal eigenvectors),
*    $\Lambda = \mathrm{diag}(\lambda_1,\dots,\lambda_n)$  are real eigenvalues,
*    $G v_i = \lambda_i v_i$ .

Also, if  $G\succeq 0$  (PSD), then all  $\lambda_i \ge 0$ .

I won’t re-prove the full spectral theorem here (it’s a core linear algebra theorem), but I will prove the PSD ⇒ nonnegative eigenvalues claim since we need it.

### Lemma: If  $G\succeq 0$  and  $Gv=\lambda v$  with  $v\neq 0$ , then  $\lambda\ge 0$ .

Proof:

$$
v^T G v = v^T(\lambda v) = \lambda \, v^T v = \lambda \|v\|_2^2.
$$

Left side is  $\ge 0$  by PSD. Right side is  $\lambda\|v\|^2$  and  $\|v\|^2>0$ . Therefore  $\lambda\ge 0$ . QED.

Apply this to  $G=A^T A$ . So all eigenvalues of  $A^T A$  are nonnegative.

* * *

3.3 Singular values and right singular vectors (defined via  $A^T A$ )
----------------------------------------------------------------------

Let  $(\lambda_i, v_i)$  be eigenpairs of  $G=A^T A$ :

$$
A^T A v_i = \lambda_i v_i, \quad v_i^T v_i = 1, \quad \lambda_i \ge 0.
$$

Define the **singular values**:

$$
\sigma_i := \sqrt{\lambda_i} \;\ge\; 0.
$$

Define **right singular vectors** to be the eigenvectors  $v_i$  of  $A^T A$ .

At this point, “SVD” is not yet proved. We’ve only defined objects from something we know exists: the eigen-decomposition of a symmetric PSD matrix.

Now we extract geometric meaning.

* * *

3.4 Why these  $v_i$  are “principal stretching directions”
-----------------------------------------------------------

Take any unit vector  $x$  ( $\|x\|_2=1$ ). Then:

$$
\|Ax\|_2^2 = x^T A^T A x = x^T G x.
$$

So maximizing  $\|Ax\|^2$  over  $\|x\|=1$  is the same as maximizing the quadratic form  $x^T G x$  over the unit sphere.

There is a fundamental fact (Rayleigh quotient principle):

### Theorem (Rayleigh quotient extremum for symmetric matrices)

For symmetric  $G$ , the maximum of  $x^T G x$  subject to  $\|x\|=1$  equals the largest eigenvalue  $\lambda_{\max}$ , and it is attained at an eigenvector  $v_{\max}$ . Similarly, the minimum is  $\lambda_{\min}$ .

So the direction that maximizes  $\|Ax\|$  is the top eigenvector of  $A^T A$ . Its maximum stretch is:

$$
\max_{\|x\|=1} \|Ax\| = \sqrt{\lambda_{\max}} = \sigma_{\max}.
$$

Then, restricting to vectors orthogonal to the first direction, the next maximizer is the next eigenvector, etc. This is why singular vectors come in an orthonormal set.

So singular values are not arbitrary: they are exactly the “principal radii” of the ellipsoid  $A(\text{unit sphere})$ .

* * *

3.5 Left singular vectors: build them from  $Av_i$ 
---------------------------------------------------

Now define, for each  $i$  with  $\sigma_i>0$ :

$$
u_i := \frac{1}{\sigma_i} A v_i \in \mathbb R^m.
$$

This definition is motivated by:

*    $A v_i$  is the image of the principal direction  $v_i$ ,
*   we normalize it to unit length.

We need to prove two things:

1.   $\|u_i\|=1$ 
2.  the vectors  $u_i$  are orthonormal (for different  $i$ )

### Lemma 3.5.1: If  $\sigma_i>0$ , then  $\|u_i\|_2 = 1$ .

Proof:

$$
\|u_i\|_2^2 = \left\|\frac{1}{\sigma_i} A v_i\right\|^2 = \frac{1}{\sigma_i^2}\|A v_i\|^2 = \frac{1}{\sigma_i^2} v_i^T A^T A v_i = \frac{1}{\sigma_i^2} v_i^T (\lambda_i v_i) = \frac{\lambda_i}{\sigma_i^2} \|v_i\|^2.
$$

But  $\lambda_i = \sigma_i^2$  and  $\|v_i\|=1$ . So  $\|u_i\|^2=1$ . QED.

### Lemma 3.5.2: If  $i\neq j$  and  $\sigma_i,\sigma_j>0$ , then  $u_i^T u_j = 0$ .

Proof:

$$
u_i^T u_j = \left(\frac{1}{\sigma_i}A v_i\right)^T \left(\frac{1}{\sigma_j}A v_j\right) = \frac{1}{\sigma_i\sigma_j} v_i^T A^T A v_j = \frac{1}{\sigma_i\sigma_j} v_i^T (\lambda_j v_j) = \frac{\lambda_j}{\sigma_i\sigma_j} v_i^T v_j.
$$

But  $v_i^T v_j=0$  because eigenvectors of symmetric  $A^T A$  can be chosen orthonormal. Hence  $u_i^T u_j=0$ . QED.

So the nonzero-singular-value left singular vectors form an orthonormal set in  $\mathbb R^m$ .

* * *

3.6 The core pair of identities:  $Av_i = \sigma_i u_i$  and  $A^T u_i = \sigma_i v_i$ 
---------------------------------------------------------------------------------------

The first one is immediate from the definition:

$$
Av_i = \sigma_i u_i.
$$

The second one is the real structural symmetry:

### Lemma 3.6.1: If  $\sigma_i>0$ , then  $A^T u_i = \sigma_i v_i$ .

Proof:

$$
A^T u_i = A^T \left(\frac{1}{\sigma_i} A v_i\right) = \frac{1}{\sigma_i} A^T A v_i = \frac{1}{\sigma_i} \lambda_i v_i = \frac{\sigma_i^2}{\sigma_i} v_i = \sigma_i v_i.
$$

QED.

This shows  $u_i$  and  $v_i$  are paired:  $A$  maps  $v_i$  to  $\sigma_i u_i$ , and  $A^T$  maps  $u_i$  back to  $\sigma_i v_i$ .

* * *

3.7 Assemble the decomposition  $A = U\Sigma V^T$ 
--------------------------------------------------

Let  $r = \operatorname{rank}(A)$ . It turns out exactly  $r$  singular values are positive and the rest are zero; we’ll justify that in a moment.

Order the singular values:

$$
\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0,\quad \sigma_{r+1}=\cdots=0.
$$

Construct:

*    $V_r = [v_1\;\cdots\;v_r] \in \mathbb R^{n\times r}$ 
*    $U_r = [u_1\;\cdots\;u_r] \in \mathbb R^{m\times r}$ 
*    $\Sigma_r = \mathrm{diag}(\sigma_1,\dots,\sigma_r) \in \mathbb R^{r\times r}$ 

From  $Av_i = \sigma_i u_i$ , stacking columns gives:

$$
A V_r = U_r \Sigma_r.
$$

Now extend  $U_r$  to an orthonormal basis of  $\mathbb R^m$  (add columns  $u_{r+1},\dots,u_m$ ) to form an orthogonal matrix  $U\in\mathbb R^{m\times m}$ .  
Similarly extend  $V_r$  to an orthonormal basis of  $\mathbb R^n$  to form  $V\in\mathbb R^{n\times n}$ .

Define  $\Sigma\in\mathbb R^{m\times n}$  as the rectangular diagonal matrix with  $\sigma_1,\dots,\sigma_r$  on the diagonal and zeros elsewhere.

Then the full SVD statement is:

### Theorem (SVD)

For any  $A\in\mathbb R^{m\times n}$ , there exist orthogonal matrices  $U\in\mathbb R^{m\times m}$ ,  $V\in\mathbb R^{n\times n}$ , and a diagonal (rectangular)  $\Sigma\in\mathbb R^{m\times n}$  with nonnegative diagonal entries such that

$$
A = U \Sigma V^T.
$$

#### Proof idea (the only missing step)

We already built  $V$  from eigenvectors of  $A^T A$ , built  $U$  partially from  $Av_i$  for  $\sigma_i>0$ , then completed  $U$  orthogonally. The identity  $A=U\Sigma V^T$  is equivalent to  $AV=U\Sigma$ , and that holds because:

*   for  $i\le r$ ,  $Av_i = \sigma_i u_i$ ,
*   for  $i>r$ ,  $\sigma_i=0$  and  $v_i\in \ker(A)$  (we’ll prove in 3.8), so  $Av_i=0=\sigma_i u_i$ .

Thus  $A v_i = \sigma_i u_i$  holds for all  $i$ , which is exactly  $AV=U\Sigma$ . Multiply by  $V^T$  to get  $A=U\Sigma V^T$ . QED.

So the whole proof reduces to understanding the  $\sigma_i=0$  case carefully.

* * *

3.8 Rank, kernel, and the  $\sigma=0$  case (this is where Layer 1 returns)
---------------------------------------------------------------------------

### Fact 1:  $\sigma_i=0 \iff \lambda_i=0 \iff v_i \in \ker(A)$ .

Proof:

$$
A^T A v_i = \lambda_i v_i.
$$

If  $\lambda_i=0$ , then

$$
0 = v_i^T (A^T A) v_i = \|A v_i\|^2.
$$

So  $\|A v_i\|=0$ , hence  $A v_i=0$ , hence  $v_i\in\ker(A)$ .

Conversely, if  $v\in\ker(A)$ , then  $A v=0$  implies  $A^T A v=0$ , so  $v$  lies in the zero-eigenspace of  $A^T A$ , meaning  $\lambda=0$  and  $\sigma=0$ .

So:

*   the **right singular vectors with  $\sigma=0$ ** are exactly an orthonormal basis for  $\ker(A)$ .

This is huge: SVD literally splits the domain into

$$
\mathbb R^n = \operatorname{Row}(A) \;\oplus\; \ker(A)
$$

orthogonally (more on this in 3.10).

### Fact 2: number of positive singular values equals rank

Because:

*    $\operatorname{rank}(A) = \operatorname{rank}(A^T A)$ ,
*    $\operatorname{rank}(A^T A)$  equals the number of nonzero eigenvalues of  $A^T A$ ,
*   nonzero eigenvalues correspond to  $\sigma_i>0$ .

So  $r=\#\{i:\sigma_i>0\}=\operatorname{rank}(A)$ .

* * *

3.9 The geometric meaning: unit sphere goes to an ellipsoid
-----------------------------------------------------------

Consider the unit sphere in  $\mathbb R^n$ :

$$
S = \{x:\|x\|_2=1\}.
$$

Write  $x$  in the right singular basis:  $x=V y$  where  $\|y\|=\|x\|$  because  $V$  is orthogonal.

Then:

$$
Ax = U\Sigma V^T x = U\Sigma y.
$$

So the set  $A(S)$  equals:

$$
A(S) = \{U\Sigma y : \|y\|=1\}.
$$

Since  $U$  is just a rotation/reflect in  $\mathbb R^m$ , it doesn’t change lengths, only orientation. The shape is determined by  $\Sigma$ :

*    $\Sigma$  scales the coordinate axes by  $\sigma_1,\dots,\sigma_r$  and kills the rest.

So  $A(S)$  is an ellipsoid (possibly “flat” in some directions if rank  $<\min(m,n)$ ) with principal radii  $\sigma_i$ , oriented by  $U$ , and whose pre-image axes are  $V$ .

That’s why singular values are the “true stretching invariants” even when eigenvalues are useless.

* * *

3.10 The four fundamental subspaces, now cleanly visible (SVD as a subspace splitter)
-------------------------------------------------------------------------------------

Let  $A=U\Sigma V^T$ , with rank  $r$ .

Partition:

*    $V = [V_r\;\;V_0]$ , where  $V_0$  spans  $\ker(A)$ .
*    $U = [U_r\;\;U_0]$ , where  $U_0$  spans  $\ker(A^T)$ .

Then you get orthogonal direct sums:

*    $\operatorname{Row}(A) = \operatorname{span}(V_r)$ 
*    $\ker(A) = \operatorname{span}(V_0)$ 
*    $\operatorname{Col}(A) = \operatorname{span}(U_r)$ 
*    $\ker(A^T) = \operatorname{span}(U_0)$ 

And these are orthogonal complements exactly as in Layer 1:

$$
\ker(A)=\operatorname{Row}(A)^\perp,\quad \ker(A^T)=\operatorname{Col}(A)^\perp.
$$

SVD doesn’t just “factor a matrix.” It constructs orthonormal bases adapted to these four subspaces.

* * *

3.11 Practical consequences you should be able to derive
--------------------------------------------------------

### 3.11.1 Operator norm and condition number

The spectral norm (operator 2-norm) is:

$$
\|A\|_2 = \max_{\|x\|=1}\|Ax\| = \sigma_1.
$$

The smallest nonzero stretch is  $\sigma_r$ . If  $A$  is square invertible, then:

$$
\kappa_2(A)=\frac{\sigma_1}{\sigma_n}
$$

is the condition number (how sensitive solving  $Ax=b$  is).

### 3.11.2 Pseudoinverse (solving least squares cleanly)

For general  $m\times n$ , define  $\Sigma^+$  by inverting nonzero singular values:

*   replace each  $\sigma_i>0$  with  $1/\sigma_i$ ,
*   keep zeros as zeros,  
    and transpose the rectangle dimensions.

Then the Moore–Penrose pseudoinverse is:

$$
A^+ = V \Sigma^+ U^T.
$$

This gives:

*   minimum-norm solution to  $Ax=b$  when solutions exist,
*   least-squares solution when they don’t (projection onto column space).

### 3.11.3 Best rank- $k$  approximation (Eckart–Young)

If

$$
A=\sum_{i=1}^r \sigma_i u_i v_i^T,
$$

then the best rank- $k$  approximation in spectral or Frobenius norm is:

$$
A_k=\sum_{i=1}^k \sigma_i u_i v_i^T.
$$

This is the theorem behind PCA and compression. (Full proof is a bit longer; we can do it rigorously if you want—worth it.)

* * *

3.12 What “owning SVD” means (non-negotiable checklist)
-------------------------------------------------------

You truly have this layer if you can, from scratch:

1.  Prove  $A^T A$  is symmetric PSD.
2.  Use the spectral theorem on  $A^T A$  to define  $\sigma_i=\sqrt{\lambda_i}$ .
3.  Define  $u_i = Av_i/\sigma_i$  and prove  $\{u_i\}$  orthonormal for  $\sigma_i>0$ .
4.  Prove  $Av_i=\sigma_i u_i$  and  $A^T u_i=\sigma_i v_i$ .
5.  Handle the  $\sigma=0$  case and show it matches  $\ker(A)$ .
6.  Assemble  $A=U\Sigma V^T$  and interpret it geometrically.

* * *

### Bridge to the next layer (Schur complement)

SVD was “choose orthonormal bases to reveal stretching + subspace splitting.”

Schur complement is the next tool because it’s about **block structure** and **eliminating variables**, especially inside quadratic forms and PSD constraints (the heart of SDP and convex optimization). It tells you when a block matrix is PSD, and it’s basically “what remains after you solve part of the system.”

When you say “next,” we’ll do Schur complement from the same first-principles level: block matrices → quadratic forms → elimination → PSD equivalences → optimization interpretations.

## Response:
Thought for 14s

Layer 4 — Schur complement
--------------------------

_(block matrices, elimination, PSD tests, and why it’s the “hidden algebra” of SDP/convex optimization)_

You can think of the Schur complement as one idea wearing three different costumes:

1.  **Elimination (solve for part of the variables and substitute)**
2.  **Complete the square (quadratic forms in block variables)**
3.  **Block Gaussian elimination (factorization / determinant / inverse of block matrices)**

All three are literally the same algebra. We’ll derive it from first principles.

* * *

4.1 Start from the object: a block matrix and its quadratic form
================================================================

Let

$$
M=\begin{bmatrix} A & B\\ B^T & D \end{bmatrix}
$$

where  $A\in\mathbb R^{n\times n}$ ,  $D\in\mathbb R^{m\times m}$ ,  $B\in\mathbb R^{n\times m}$ . Assume  $M$  is symmetric, so  $A,D$  are symmetric.

Take a vector split into two blocks:

$$
z=\begin{bmatrix}x\\y\end{bmatrix},\quad x\in\mathbb R^n,\ y\in\mathbb R^m.
$$

Compute the quadratic form:

$$
z^T M z = \begin{bmatrix}x^T & y^T\end{bmatrix} \begin{bmatrix}A & B\\ B^T & D\end{bmatrix} \begin{bmatrix}x\\y\end{bmatrix} = x^T A x + 2x^T B y + y^T D y.
$$

This identity is basic but crucial: it shows exactly how  $x$  and  $y$  interact (the coupling term  $2x^TBy$ ).

* * *

4.2 The core maneuver: “complete the square” in block form
==========================================================

Assume first that  $D$  is invertible (later we handle singular  $D$ ).

We want to rewrite

$$
x^T A x + 2x^T B y + y^T D y
$$

in a form where the coupling disappears.

### Step 1: choose a shift that kills the cross term

Try substituting

$$
y = \tilde y - D^{-1}B^T x \quad\text{equivalently}\quad \tilde y = y + D^{-1}B^T x.
$$

Why this choice? Because it’s the multivariate analog of completing the square:

$$
y^T D y + 2 x^T B y
$$

should become

$$
(\tilde y)^T D (\tilde y) + \text{something in }x.
$$

### Step 2: expand after substitution

Compute  $y^T D y$ :

$$
y^T D y = (\tilde y - D^{-1}B^T x)^T D(\tilde y - D^{-1}B^T x).
$$

Expand carefully:

*   First term:
    
$$
\tilde y^T D \tilde y.
$$
*   Cross terms:
    
$$
-\tilde y^T D(D^{-1}B^T x) - (D^{-1}B^T x)^T D \tilde y = -\tilde y^T B^T x - x^T B \tilde y.
$$

Since these are scalars,  $\tilde y^T B^T x = x^T B \tilde y$ . So cross terms sum to

$$
-2x^T B\tilde y.
$$
*   Last term:
    
$$
(D^{-1}B^T x)^T D (D^{-1}B^T x) = x^T B D^{-1} B^T x.
$$

So:

$$
y^T D y = \tilde y^T D \tilde y - 2x^T B \tilde y + x^T B D^{-1}B^T x.
$$

Now compute the coupling term  $2x^TBy$ :

$$
2x^T B y = 2x^T B(\tilde y - D^{-1}B^T x) = 2x^T B\tilde y - 2x^T B D^{-1}B^T x.
$$

Add everything:

$$
x^T A x + 2x^TBy + y^T D y = x^T A x + \big(2x^T B\tilde y - 2x^T B D^{-1}B^T x\big) + \big(\tilde y^T D \tilde y - 2x^T B\tilde y + x^T B D^{-1}B^T x\big).
$$

The  $2x^T B\tilde y$  terms cancel. Combine the  $x$ \-only terms:

$$
-2x^T B D^{-1}B^T x + x^T B D^{-1}B^T x = -x^T B D^{-1}B^T x.
$$

So we get the clean decomposition:

$$
z^T M z = \tilde y^T D \tilde y + x^T\Big(A - B D^{-1}B^T\Big)x.
$$

### Definition (Schur complement of  $D$  in  $M$ )

$$
S_{/D}(M) := A - B D^{-1}B^T.
$$

So the quadratic form becomes:

$$
\begin{bmatrix}x\\y\end{bmatrix}^T \begin{bmatrix}A & B\\B^T & D\end{bmatrix} \begin{bmatrix}x\\y\end{bmatrix} = \big(y + D^{-1}B^T x\big)^T D \big(y + D^{-1}B^T x\big) + x^T S_{/D}(M) x.
$$

That identity is the beating heart of the Schur complement.

* * *

4.3 The first big theorem: PSD test via Schur complement (invertible case)
==========================================================================

Assume  $D \succ 0$  (symmetric positive definite, hence invertible).

### Theorem 4.3.1

$$
M=\begin{bmatrix}A & B\\B^T & D\end{bmatrix}\succeq 0 \quad\Longleftrightarrow\quad D\succ 0\ \text{and}\ S_{/D}(M)=A-BD^{-1}B^T\succeq 0.
$$

#### Proof (⇒)

Assume  $M\succeq 0$ . Then for all  $x,y$ ,

$$
z^T M z \ge 0.
$$
1.  Plug  $x=0$ . Then  $z^T M z = y^T D y \ge 0$  for all  $y$ . So  $D\succeq 0$ .  
    But we assumed  $D\succ 0$  for the equivalence statement (this assumption ensures invertibility and lets us complete the square cleanly).
2.  Use the completed-square identity:
    
$$
z^T M z = (y + D^{-1}B^T x)^T D (y + D^{-1}B^T x) + x^T S_{/D}(M)x.
$$

The first term is always  $\ge 0$  because  $D\succ 0$ . Therefore, for all  $x$  and  $y$ ,

$$
z^T M z \ge x^T S_{/D}(M)x.
$$

Now choose  $y = -D^{-1}B^T x$ , which makes the first term exactly 0. Then:

$$
0 \le z^T M z = x^T S_{/D}(M)x\quad \forall x.
$$

So  $S_{/D}(M)\succeq 0$ .

#### Proof (⇐)

Assume  $D\succ 0$  and  $S_{/D}(M)\succeq 0$ . Then for any  $x,y$ ,

$$
z^T M z = (y + D^{-1}B^T x)^T D (y + D^{-1}B^T x) + x^T S_{/D}(M)x.
$$

Each term is  $\ge 0$  for all  $x,y$ , so their sum is  $\ge 0$ . Hence  $M\succeq 0$ . QED.

This theorem is why Schur complements appear nonstop in SDP: they turn a block PSD constraint into a simpler PSD constraint plus  $D\succ 0$ .

* * *

4.4 Symmetry: the Schur complement of  $A$ 
===========================================

If instead  $A$  is invertible (or  $A\succ 0$ ), you can complete the square in the other variable.

Assume  $A\succ 0$ . Define:

$$
S_{/A}(M):= D - B^T A^{-1} B.
$$

Then you get the parallel theorem:

$$
M\succeq 0 \quad\Longleftrightarrow\quad A\succ 0\ \text{and}\ D - B^T A^{-1}B \succeq 0.
$$

Same proof, just swap roles.

* * *

4.5 Schur complement as elimination in optimization (the cleanest intuition)
============================================================================

Consider the quadratic function in  $y$ , with  $x$  fixed:

$$
q_x(y) := x^T A x + 2x^T B y + y^T D y.
$$

Assume  $D\succ 0$ . Then  $q_x(y)$  is a strictly convex quadratic in  $y$ , so it has a unique minimizer.

### Step 1: compute the minimizer

Differentiate w.r.t.  $y$ :

$$
\nabla_y q_x(y) = 2B^T x + 2D y.
$$

Set to zero:

$$
2B^T x + 2D y = 0 \quad\Rightarrow\quad Dy = -B^T x \quad\Rightarrow\quad y^*(x) = -D^{-1}B^T x.
$$

### Step 2: compute the minimized value

Plugging  $y^*(x)$  into the completed-square identity is fastest:

$$
q_x(y) = (y + D^{-1}B^T x)^T D (y + D^{-1}B^T x) + x^T(A - BD^{-1}B^T)x.
$$

At  $y=y^*(x)$ , the first term is 0. So:

$$
\min_y q_x(y) = x^T(A - BD^{-1}B^T)x.
$$

So the Schur complement is literally:

> “What remains in the quadratic form after you optimally eliminate  $y$ .”

This is the exact same algebra as in Gaussian elimination and in conditional Gaussians.

* * *

4.6 Determinant factorization (block determinant)
=================================================

Assume  $D$  is invertible. Then:

$$
\det\begin{bmatrix}A & B\\B^T & D\end{bmatrix} = \det(D)\,\det(A - BD^{-1}B^T).
$$

You can see this via block Gaussian elimination (a factorization):

Define the block lower-triangular matrix

$$
L=\begin{bmatrix} I & BD^{-1}\\ 0 & I \end{bmatrix}.
$$

Then

$$
L\begin{bmatrix}A & B\\B^T & D\end{bmatrix} = \begin{bmatrix} A - BD^{-1}B^T & B\\ B^T & D \end{bmatrix}.
$$

Now also multiply on the right by a matching block upper-triangular matrix to zero out the off-diagonal block. The determinant of triangular block matrices is the product of determinants of diagonal blocks, and  $\det(L)=1$ . Working this through yields the formula.

This identity explains why Schur complements show up in probabilistic normalization constants and log-det barriers.

* * *

4.7 Block inverse formula (when you need  $M^{-1}$ )
====================================================

Assume  $D$  invertible and also  $S:=A - BD^{-1}B^T$  invertible. Then

$$
M^{-1} = \begin{bmatrix} S^{-1} & -S^{-1}BD^{-1}\\ -D^{-1}B^T S^{-1} & D^{-1} + D^{-1}B^T S^{-1}BD^{-1} \end{bmatrix}.
$$

This is the matrix version of “solve the block system by eliminating one block, then back-substitute.”

(There’s a symmetric version using  $A^{-1}$  and  $D - B^T A^{-1} B$  if  $A$  is invertible.)

* * *

4.8 The semidefinite-but-singular case (the “generalized Schur complement”)
===========================================================================

Real optimization problems often have  $D\succeq 0$  but not invertible. Then  $D^{-1}$  doesn’t exist, and the simple formula breaks.

The right tool is the Moore–Penrose pseudoinverse  $D^+$  (from the SVD layer). There’s also an extra **range condition** that replaces invertibility.

### Key fact to remember

When  $D$  is singular, the expression  $BD^{-1}B^T$  is not defined. Even if you try  $BD^+B^T$ , you must ensure that the coupling  $B$  only “points into” directions where  $D$  has support.

Formally, the condition is:

$$
\operatorname{Range}(B^T) \subseteq \operatorname{Range}(D).
$$

Equivalent statement:

$$
(I - DD^+)B^T = 0.
$$

(Here  $DD^+$  is the orthogonal projector onto  $\operatorname{Range}(D)$ .)

### Theorem 4.8.1 (generalized PSD Schur condition)

For symmetric

$$
M=\begin{bmatrix}A & B\\B^T & D\end{bmatrix}
$$

with  $D\succeq 0$ , we have:

$$
M\succeq 0 \quad\Longleftrightarrow\quad \begin{cases} D\succeq 0,\\ (I - DD^+)B^T = 0 \quad(\text{range condition}),\\ A - B D^+ B^T \succeq 0. \end{cases}
$$

Intuition (why the extra condition exists):  
If  $D$  has a nontrivial kernel, then there are directions  $y\neq 0$  with  $y^T D y = 0$ . Along those directions, the only thing controlling the quadratic form is the coupling term  $2x^TBy$ . PSD forces that coupling to vanish in those “free” directions, which is exactly the range condition.

You don’t always need this version day-to-day, but if you do SDP theory seriously, you eventually hit it.

* * *

4.9 The classic modeling trick (why Schur complement is everywhere in convex optimization)
==========================================================================================

This is the standard “turn a quadratic inequality into an LMI” move.

Assume  $P\succ 0$ . Consider the constraint:

$$
x^T P^{-1} x \le t.
$$

This is not linear in  $(x,t)$  because of the inverse. But it is equivalent to a PSD constraint:

### Claim

For  $P\succ 0$ ,

$$
x^T P^{-1} x \le t \quad\Longleftrightarrow\quad \begin{bmatrix} P & x\\ x^T & t \end{bmatrix}\succeq 0.
$$

#### Proof

Apply the Schur complement with respect to  $P\succ 0$ . The Schur complement of  $P$  is:

$$
t - x^T P^{-1} x.
$$

So the block matrix is PSD iff  $P\succ 0$  and  $t - x^T P^{-1}x \ge 0$ , i.e.  $x^T P^{-1}x \le t$ . QED.

This is one of the core “translation rules” in SDP modeling (and it’s exactly why you wanted Schur complement in your roadmap).

* * *

4.10 What you should be able to do after this layer
===================================================

You “own” Schur complement if you can do these without pattern-matching:

1.  Start from  $x^TAx + 2x^TBy + y^TDy$  and complete the square to derive  $A - BD^{-1}B^T$ .
2.  Prove the PSD equivalence  $M\succeq 0 \iff D\succ 0$  and  $A - BD^{-1}B^T\succeq 0$ .
3.  Interpret Schur complement as “eliminate  $y$ ” by minimizing a quadratic.
4.  Derive the LMI equivalence  $\begin{bmatrix}P & x\\ x^T & t\end{bmatrix}\succeq 0 \iff x^T P^{-1}x\le t$  (with  $P\succ 0$ ).
5.  Know what breaks when  $D$  is singular and what the extra “range condition” is fixing.

* * *

If you want to continue the roadmap after this: the natural “next micro-layer” is the **kernel / nullspace viewpoint inside Schur complement** (how PSD plus singular blocks forces coupling to vanish on null directions), and then the **Schur complement ↔ Gaussian conditioning** equivalence (conditional covariance and precision matrices).

## Response:
Thought for 21s

Layer 5 — Orthogonality, projections, least squares, pseudoinverse
------------------------------------------------------------------

_(the “kernel + SVD become a working machine” layer, and Schur complement reappears as elimination)_

Up to now you have:

*   Layer 1: kernel/image are the two canonical subspaces of a linear map.
*   Layer 3: SVD gives orthonormal bases adapted to those subspaces.
*   Layer 4: Schur complement is elimination in block systems / quadratic forms.

This layer fuses them into one operational spine:

1.  **Orthogonality and orthogonal complements** (what “perpendicular subspace” means)
2.  **Orthogonal projection onto a subspace** (closest point theorem)
3.  **Least squares** as “project  $b$  onto the column space”
4.  **Pseudoinverse** as the clean formula for solutions, built from SVD
5.  **Projector identities** like  $AA^+$  and  $A^+A$  (the four fundamental subspaces made explicit)
6.  **Schur complement** shows up again when you eliminate variables in KKT systems.

I’ll do it from first principles, with full derivations.

* * *

### 5.1 Inner product, norm, and orthogonality

We work in  $\mathbb R^n$  with the standard inner product:

$$
\langle x,y\rangle := x^T y.
$$

From this, define the Euclidean norm:

$$
\|x\|_2 := \sqrt{\langle x,x\rangle} = \sqrt{x^T x}.
$$

Two vectors are orthogonal if

$$
x \perp y \quad\Longleftrightarrow\quad x^T y = 0.
$$

For a subspace  $U\subseteq \mathbb R^n$ , define its orthogonal complement:

$$
U^\perp := \{z\in\mathbb R^n : z^T u = 0 \ \forall u\in U\}.
$$

Facts you should be able to prove (they’re short, but fundamental):

1.   $U^\perp$  is a subspace.  
    Proof: check closure under addition/scalars directly from the defining dot-product equalities.
2.  If  $U\subseteq V$ , then  $V^\perp \subseteq U^\perp$ .  
    Proof: being orthogonal to “more vectors” is a stronger condition.
3.   $U \cap U^\perp = \{0\}$ .  
    Proof: if  $x\in U\cap U^\perp$ , then  $x\in U$  and  $x\perp x$ , so  $x^T x=0\Rightarrow x=0$ .
4.  In finite dimensions,  $\dim(U)+\dim(U^\perp)=n$ .  
    This is a core theorem (can be proved by taking an orthonormal basis of  $U$  and extending it to an orthonormal basis of  $\mathbb R^n$ ).

That last identity is the orthogonality version of rank–nullity and is the bridge to “four fundamental subspaces.”

* * *

### 5.2 Orthogonal projection: the closest point in a subspace

Let  $U\subseteq \mathbb R^n$  be a subspace, and let  $b\in\mathbb R^n$  be any vector.

We want the “closest point in  $U$  to  $b$ ”:

$$
\min_{u\in U} \|b-u\|_2.
$$

This is the definition of orthogonal projection, but we won’t assume existence/uniqueness; we prove it.

#### Theorem 5.2.1 (existence and uniqueness of orthogonal projection)

For any subspace  $U$  and any  $b$ , there exists a unique  $\hat u\in U$  such that

$$
\|b-\hat u\|_2 = \min_{u\in U} \|b-u\|_2.
$$

Moreover,  $\hat u$  is characterized by the orthogonality condition:

$$
b-\hat u \in U^\perp \quad\Longleftrightarrow\quad (b-\hat u)^T u = 0\ \forall u\in U.
$$

Proof, step-by-step:

1.  Pick an orthonormal basis of  $U$ :  $\{q_1,\dots,q_r\}$  with  $q_i^T q_j=\delta_{ij}$ . (This exists by Gram–Schmidt.)
2.  Consider candidates of the form  $u=\sum_{i=1}^r \alpha_i q_i$ . Every  $u\in U$  is exactly such a combination.
3.  Write the squared distance:
    
$$
\|b-u\|^2 = \|b-\sum \alpha_i q_i\|^2 = (b-\sum \alpha_i q_i)^T(b-\sum \alpha_i q_i).
$$

Expand using bilinearity and orthonormality:

$$
\|b-u\|^2 = b^T b - 2\sum_{i=1}^r \alpha_i q_i^T b + \sum_{i=1}^r \alpha_i^2,
$$

because cross terms  $\alpha_i\alpha_j q_i^T q_j$  vanish when  $i\neq j$ , and equal  $\alpha_i^2$  when  $i=j$ .

4.  This is now a separable quadratic in the coefficients  $\alpha_i$ . Minimize w.r.t. each  $\alpha_i$  by differentiation:
    
$$
\frac{\partial}{\partial \alpha_i}\Big( b^T b - 2\sum \alpha_k q_k^T b + \sum \alpha_k^2\Big) = -2 q_i^T b + 2\alpha_i.
$$

Set to zero:

$$
\alpha_i = q_i^T b.
$$
5.  So the unique minimizer is
    
$$
\hat u = \sum_{i=1}^r (q_i^T b)\, q_i.
$$
6.  Define the residual  $r := b-\hat u$ . Check orthogonality:  
    for any basis vector  $q_j$ ,
    
$$
q_j^T r = q_j^T b - q_j^T \sum_{i=1}^r (q_i^T b)q_i = q_j^T b - \sum_{i=1}^r (q_i^T b)(q_j^T q_i) = q_j^T b - (q_j^T b)=0.
$$

So  $r\perp q_j$  for all  $j$ , hence  $r\perp U$ , i.e.  $r\in U^\perp$ .

7.  Uniqueness: if two points  $\hat u_1,\hat u_2\in U$  both satisfy  $b-\hat u_k\in U^\perp$ , then subtract:
    
$$
(\hat u_1-\hat u_2) = (b-(b-\hat u_1))-(b-(b-\hat u_2)) \in U,
$$

and also

$$
\hat u_1-\hat u_2 = (b-\hat u_2) - (b-\hat u_1) \in U^\perp.
$$

So  $\hat u_1-\hat u_2 \in U\cap U^\perp=\{0\}$ , hence  $\hat u_1=\hat u_2$ .

That proves existence, formula, and uniqueness all at once.

So projection is not a definition you accept; it’s a theorem.

* * *

### 5.3 Projection matrix onto a subspace spanned by columns

Now specialize to a concrete subspace:

$$
U = \operatorname{Col}(A)\subseteq \mathbb R^m,\quad A\in\mathbb R^{m\times n}.
$$

We want the projection of  $b\in\mathbb R^m$  onto  $\operatorname{Col}(A)$ . Any vector in the column space looks like  $Ax$ . So the projection problem becomes:

$$
\min_{x\in\mathbb R^n} \|b-Ax\|_2.
$$

That is least squares. But the geometric meaning is: choose  $Ax$  to be the closest point to  $b$  in the column space.

* * *

### 5.4 Least squares and the normal equations (derived rigorously)

Define the objective:

$$
f(x) := \|b-Ax\|_2^2 = (b-Ax)^T(b-Ax).
$$

Expand:

$$
f(x)=b^T b - 2x^T A^T b + x^T A^T A x.
$$

This is a quadratic function in  $x$ . Its gradient is:

$$
\nabla f(x) = -2A^T b + 2A^T A x.
$$

(Reason: gradient of  $x^T Q x$  is  $(Q+Q^T)x$ , and for  $Q=A^T A$  symmetric, it’s  $2A^T A x$ ; gradient of  $-2x^T A^T b$  is  $-2A^T b$ .)

Set  $\nabla f(x)=0$  for optimality:

$$
A^T A x = A^T b.
$$

These are the **normal equations**.

Now connect this to geometry (projection condition):

Let  $r=b-Ax$  be the residual at a minimizer. The normal equations are equivalent to:

$$
A^T r = 0.
$$

Meaning:  $r\in \ker(A^T)$ . But  $\ker(A^T) = \operatorname{Col}(A)^\perp$ . Therefore:

$$
r \perp \operatorname{Col}(A).
$$

So the least squares solution is exactly the vector  $Ax$  whose residual is orthogonal to the column space — exactly the characterization of orthogonal projection from 5.2.

So the normal equations are not “a computational trick.” They are the algebraic form of the projection theorem.

* * *

### 5.5 Existence and uniqueness of least squares solutions

Existence: always. Because  $f(x)\ge 0$  and is convex quadratic; in finite dimensions it attains its minimum (can be argued via coercivity on  $\operatorname{Row}(A)$  directions and flatness on  $\ker(A)$ , or via SVD in a moment).

Uniqueness: depends on the kernel.

Key fact:

$$
f(x)=\|b-Ax\|^2 \text{ depends only on } Ax.
$$

If  $x$  and  $x+z$  with  $z\in \ker(A)$ , then  $A(x+z)=Ax$ , so they yield the same objective value. Therefore, if  $\ker(A)\neq\{0\}$ , minimizers are generally not unique.

More precisely:

*   If  $A$  has full column rank ( $\operatorname{rank}(A)=n$ ), then  $A^T A$  is invertible and the normal equations have a unique solution:
    $$
    x^*=(A^T A)^{-1}A^T b.
    $$
*   If  $\operatorname{rank}(A)<n$ , there are infinitely many minimizers, forming an affine set:
    $$
    x^* + \ker(A).
    $$

Among all minimizers, there is a unique one with smallest norm  $\|x\|$ . That is the “minimum-norm least squares” solution, and SVD gives it cleanly.

* * *

### 5.6 Pseudoinverse from SVD: the clean solution formula

Take the SVD:

$$
A = U\Sigma V^T,
$$

with singular values  $\sigma_1\ge\cdots\ge\sigma_r>0$  and the rest zero, where  $r=\operatorname{rank}(A)$ .

Write the “thin” parts:

*    $U_r = [u_1,\dots,u_r]$ ,
*    $V_r = [v_1,\dots,v_r]$ ,
*    $\Sigma_r=\mathrm{diag}(\sigma_1,\dots,\sigma_r)$ .

Then

$$
A = U_r \Sigma_r V_r^T.
$$

Define  $\Sigma_r^{-1}=\mathrm{diag}(1/\sigma_1,\dots,1/\sigma_r)$ . The Moore–Penrose pseudoinverse is:

$$
A^+ := V_r \Sigma_r^{-1} U_r^T.
$$

Now prove the core property for least squares:

#### Theorem 5.6.1 (minimum-norm least squares solution)

The vector

$$
x^\star = A^+ b
$$

is the unique solution that:

1.  minimizes  $\|b-Ax\|$  over all  $x$ , and
2.  among all minimizers, has minimum  $\|x\|$ .

Sketch of the derivation (but still tight):

Write  $x$  in the  $V$ \-basis:  $x = V y$ . Since  $V$  is orthogonal,  $\|x\|=\|y\|$ . Also:

$$
Ax = U\Sigma V^T V y = U\Sigma y.
$$

So the least squares problem becomes:

$$
\min_y \|b - U\Sigma y\|.
$$

Left-multiply by  $U^T$  (norm-preserving):

$$
\min_y \|U^T b - \Sigma y\|.
$$

Let  $c:=U^T b$ . Because  $\Sigma$  is diagonal-rectangular, this decouples into coordinates:

*   For  $i\le r$ : the term is  $(c_i - \sigma_i y_i)^2$ .
*   For  $i>r$ :  $\sigma_i=0$ , the term is  $c_i^2$  regardless of  $y_i$ .

So the minimizer must satisfy for  $i\le r$ :

$$
y_i = \frac{c_i}{\sigma_i}.
$$

For  $i>r$ ,  $y_i$  does not affect the residual, so to minimize  $\|y\|$  we choose  $y_i=0$ .

Thus

$$
y^\star = \begin{bmatrix}c_1/\sigma_1\\ \vdots \\ c_r/\sigma_r\\ 0\\ \vdots \\ 0\end{bmatrix}.
$$

Convert back:

$$
x^\star = V y^\star = V_r \Sigma_r^{-1} c_{1:r} = V_r\Sigma_r^{-1}U_r^T b = A^+ b.
$$

That gives both least squares optimality and minimum-norm selection in one shot.

* * *

### 5.7 Projection matrices appear automatically:  $AA^+$  and  $A^+A$ 

This is where kernel, image, and SVD become “one-line identities”.

Compute:

$$
AA^+ = (U_r\Sigma_r V_r^T)(V_r\Sigma_r^{-1}U_r^T) = U_r \Sigma_r (\Sigma_r^{-1}) U_r^T = U_r U_r^T.
$$

But  $U_r$  columns span  $\operatorname{Col}(A)$ . The matrix  $U_rU_r^T$  is the orthogonal projector onto that subspace. Therefore:

$$
P_{\operatorname{Col}(A)} = AA^+.
$$

Similarly:

$$
A^+A = (V_r\Sigma_r^{-1}U_r^T)(U_r\Sigma_r V_r^T) = V_rV_r^T,
$$

which is the orthogonal projector onto  $\operatorname{Row}(A)\subseteq \mathbb R^n$ .

Then automatically, projectors onto kernels are:

$$
P_{\ker(A)} = I - A^+A = I - V_rV_r^T = V_0 V_0^T,
$$
 
$$
P_{\ker(A^T)} = I - AA^+ = I - U_rU_r^T = U_0 U_0^T.
$$

This is the “four fundamental subspaces” turned into exact matrices.

* * *

### 5.8 Schur complement reappears: least squares as elimination in a block system

Here’s a very important viewpoint: least squares can be written as a constrained quadratic, whose KKT (optimality) conditions form a block linear system. Eliminating blocks is a Schur complement move.

Consider minimizing  $\frac12\|r\|^2$  subject to  $r=b-Ax$ . That is equivalent to least squares because  $r$  is exactly the residual.

Problem:

$$
\min_{x,r}\ \frac12 r^T r\quad\text{s.t.}\quad r + Ax = b.
$$

Form the Lagrangian with multiplier  $y$ :

$$
\mathcal L(x,r,y)=\frac12 r^T r + y^T(b - r - Ax).
$$

Stationarity:

*   w.r.t.  $r$ :  $\nabla_r \mathcal L = r - y = 0 \Rightarrow r=y$ .
*   w.r.t.  $x$ :  $\nabla_x \mathcal L = -A^T y = 0 \Rightarrow A^T y=0$ .  
    Primal feasibility:  $r+Ax=b$ .

Substitute  $r=y$ :

$$
y + Ax = b,\quad A^T y = 0.
$$

This is the block linear system:

$$
\begin{bmatrix} I & A\\ A^T & 0 \end{bmatrix} \begin{bmatrix} y\\ x \end{bmatrix} = \begin{bmatrix} b\\ 0 \end{bmatrix}.
$$

Now eliminate  $y$  using Schur complement. From the first block row:

$$
y = b - Ax.
$$

Plug into second:

$$
A^T(b - Ax)=0 \Rightarrow A^T A x = A^T b.
$$

Boom: the normal equations appear as the Schur complement elimination of  $y$ . This is exactly the same algebraic phenomenon as in Layer 4, now appearing inside least squares/KKT.

This perspective becomes critical in constrained least squares, ridge regression, and general quadratic programs, where the KKT matrix is block-structured and Schur complements are the standard method of reduction.

* * *

### 5.9 What you should be able to do after this layer

If you really own Layer 5, you can:

1.  Prove the projection theorem:  $\hat u\in U$  minimizes  $\|b-u\|$  iff  $b-\hat u\in U^\perp$ .
2.  Derive least squares normal equations as  $A^T(b-Ax)=0$ .
3.  Explain least squares geometrically as projecting  $b$  onto  $\operatorname{Col}(A)$ .
4.  Build  $A^+$  from SVD and prove  $x^\star=A^+b$  is minimum-norm least squares.
5.  Derive and interpret  $AA^+=U_rU_r^T$  and  $A^+A=V_rV_r^T$  as orthogonal projectors.
6.  Re-derive normal equations via the Schur complement of the KKT block matrix.

* * *

If you want to continue “next” beyond this, the natural Layer 6 is: **generalized eigenvalue problems and Rayleigh quotients**, which unify eigenvalues, PSD order, and Schur complements in one place and lead directly into SDP and trust-region duality (very Boyd–Vandenberghe flavored).

## Response:
Thought for 19s

Layer 6 — Rayleigh quotients and generalized eigenvalues
--------------------------------------------------------

_(the unifying “quadratic forms + PSD order + Schur complement” layer that powers SDP, trust-region duality, and stability)_

Everything you’ve built so far is pointing at one central object:

$$
x \mapsto x^T A x
$$

That’s a **quadratic form**. It’s the algebraic way to talk about “energy”, “curvature”, “variance”, and “ellipsoids”. Eigenvalues, SVD, Schur complements, least squares, and SDP all become the same story once you learn how to compare quadratic forms.

This layer has one main goal:

> Learn to convert “matrix inequalities” into “scalar inequalities for all vectors”, and then solve the resulting optimization problems via Rayleigh quotients.

* * *

### 6.1 Quadratic forms and PSD order (the “for all vectors” viewpoint)

Assume  $A\in\mathbb R^{n\times n}$  is symmetric. Define the quadratic form:

$$
q_A(x) := x^T A x.
$$

Now define PSD order.

**Definition (PSD / Loewner order).** For symmetric  $A,B$ ,

$$
A \succeq B \quad\Longleftrightarrow\quad A-B \succeq 0.
$$

And

$$
A \succeq 0 \quad\Longleftrightarrow\quad x^T A x \ge 0\ \ \forall x.
$$

That last equivalence is not a slogan; it’s the definition in many texts. The key is:

> A matrix inequality is a statement about a scalar inequality holding for **all vectors**.

Concretely:

$$
A \preceq tB \quad\Longleftrightarrow\quad x^T A x \le t\, x^T B x\ \ \forall x.
$$

This is the bridge to eigenvalues, because eigenvalues are exactly the “best constants”  $t$  in inequalities like that.

* * *

### 6.2 The Rayleigh quotient (why eigenvalues are optimization answers)

For symmetric  $A$ , define the Rayleigh quotient:

$$
R_A(x) := \frac{x^T A x}{x^T x},\quad x\neq 0.
$$

Two immediate facts (prove them once and own them forever):

1.  **Scale invariance:**  $R_A(\alpha x)=R_A(x)$  for  $\alpha\neq 0$ .  
    Proof:
    $$
    R_A(\alpha x)=\frac{(\alpha x)^T A(\alpha x)}{(\alpha x)^T(\alpha x)} =\frac{\alpha^2 x^T A x}{\alpha^2 x^T x}=R_A(x).
    $$
    So you can restrict to  $\|x\|=1$  without loss.
2.  **Rayleigh on an eigenvector:** if  $Ax=\lambda x$ , then  $R_A(x)=\lambda$ .  
    Proof:
    $$
    R_A(x)=\frac{x^T(\lambda x)}{x^T x}=\lambda.
    $$

So eigenvalues appear as Rayleigh quotients of special directions.

Now comes the big theorem: the _extreme_ Rayleigh quotients are exactly the extreme eigenvalues.

* * *

### 6.3 Variational characterization of eigenvalues (proved cleanly)

Let  $A$  be symmetric. By the spectral theorem,  $A$  has an orthonormal eigenbasis  $\{v_1,\dots,v_n\}$  with eigenvalues  $\lambda_1,\dots,\lambda_n$ . Assume sorted:

$$
\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n.
$$

Take any nonzero  $x$ . Expand it in the eigenbasis:

$$
x = \sum_{i=1}^n \alpha_i v_i.
$$

Because the basis is orthonormal:

$$
x^T x = \sum_{i=1}^n \alpha_i^2.
$$

Compute the quadratic form:

$$
x^T A x = \left(\sum_i \alpha_i v_i\right)^T A\left(\sum_j \alpha_j v_j\right) = \sum_{i,j} \alpha_i\alpha_j\, v_i^T A v_j.
$$

But  $Av_j=\lambda_j v_j$ , so  $v_i^T A v_j = \lambda_j v_i^T v_j = \lambda_j \delta_{ij}$ . Thus all cross terms vanish and:

$$
x^T A x = \sum_{j=1}^n \lambda_j \alpha_j^2.
$$

Therefore the Rayleigh quotient is:

$$
R_A(x)=\frac{\sum_{j=1}^n \lambda_j \alpha_j^2}{\sum_{j=1}^n \alpha_j^2}.
$$

Now stare at that expression: it is a **weighted average** of the eigenvalues, with weights

$$
w_j = \frac{\alpha_j^2}{\sum_{k=1}^n \alpha_k^2},
$$

and  $w_j\ge 0$ ,  $\sum_j w_j=1$ . So:

$$
R_A(x)=\sum_{j=1}^n w_j \lambda_j.
$$

A weighted average of numbers always lies between min and max. Therefore:

$$
\lambda_n \le R_A(x)\le \lambda_1\quad \forall x\neq 0.
$$

And the bounds are tight:

*   If  $x=v_1$ , then  $R_A(x)=\lambda_1$ .
*   If  $x=v_n$ , then  $R_A(x)=\lambda_n$ .

So we have proved:

**Theorem (Rayleigh extremum).**

$$
\max_{\|x\|=1} x^T A x = \lambda_1,\qquad \min_{\|x\|=1} x^T A x = \lambda_n.
$$

This is one of the most important “eigenvalues = optimization” identities in applied math.

* * *

### 6.4 Courant–Fischer (the “k-th eigenvalue = constrained max/min” principle)

The Rayleigh theorem gives only the top and bottom eigenvalues. What about the middle ones?

Define the k-th largest eigenvalue  $\lambda_k$  (with  $\lambda_1\ge\cdots\ge\lambda_n$ ).

A precise, powerful characterization is:

**Courant–Fischer min–max:**

$$
\lambda_k = \max_{\substack{S\subset\mathbb R^n\\ \dim(S)=k}}\ \ \min_{\substack{x\in S\\ \|x\|=1}} x^T A x.
$$

Interpretation: you choose a  $k$ \-dimensional subspace  $S$  to make the worst direction inside it as large as possible. The optimal value is  $\lambda_k$ .

Why it matters: it tells you eigenvalues are “best constants” under dimension constraints. This is the blueprint for many SDP relaxations and spectral bounds.

(If you want, we can do the full proof later; it’s a bit longer but fully doable with the eigenbasis expansion and subspace dimension counting.)

* * *

### 6.5 Generalized eigenvalues (A, B) and “whitening” (this is the main new object)

Now we level up.

Let  $A,B\in\mathbb R^{n\times n}$  be symmetric, and assume

$$
B \succ 0
$$

(symmetric positive definite). This is crucial: it means  $x^T B x>0$  for all  $x\neq 0$ .

**Definition (generalized eigenpair).** A scalar  $\lambda$  and nonzero vector  $x$  satisfy:

$$
A x = \lambda B x.
$$

This is not cosmetic. It’s what you get when your geometry uses the  $B$ \-inner product instead of the Euclidean one.

**Generalized Rayleigh quotient:**

$$
R_{A,B}(x) := \frac{x^T A x}{x^T B x},\quad x\neq 0.
$$

Exactly like before, it’s scale-invariant:

$$
R_{A,B}(\alpha x)=R_{A,B}(x).
$$

And if  $Ax=\lambda Bx$ , then:

$$
x^T A x = x^T(\lambda Bx)=\lambda x^T B x \Rightarrow R_{A,B}(x)=\lambda.
$$

So generalized eigenvalues are generalized Rayleigh quotients of special vectors.

Now we prove how to reduce the generalized problem to a standard eigenproblem using “whitening”.

#### Step 1: factor  $B$ 

Since  $B\succ 0$ , there exists an invertible  $B^{1/2}\succ 0$  with

$$
B^{1/2}B^{1/2}=B.
$$

(You can obtain  $B^{1/2}$  from the spectral theorem: diagonalize  $B=Q\Gamma Q^T$  with  $\Gamma>0$ , then  $B^{1/2}=Q\Gamma^{1/2}Q^T$ .)

#### Step 2: change variables

Let

$$
y := B^{1/2}x\quad \Longleftrightarrow\quad x = B^{-1/2}y.
$$

#### Step 3: transform the generalized eigen-equation

Start with:

$$
Ax=\lambda Bx.
$$

Substitute  $x=B^{-1/2}y$ :

$$
A B^{-1/2}y = \lambda B B^{-1/2}y = \lambda B^{1/2}y.
$$

Left-multiply by  $B^{-1/2}$ :

$$
B^{-1/2} A B^{-1/2}y = \lambda y.
$$

Define the “whitened” symmetric matrix:

$$
C := B^{-1/2} A B^{-1/2}.
$$

Then the generalized eigenproblem becomes an ordinary eigenproblem:

$$
C y = \lambda y.
$$

So:

> Generalized eigenvalues of  $(A,B)$  are ordinary eigenvalues of  $B^{-1/2}AB^{-1/2}$ .

This is the clean reduction that makes the whole theory work.

* * *

### 6.6 Variational characterization of generalized eigenvalues (proved)

Now use the transformation to prove the generalized Rayleigh extremum exactly like in 6.3.

Consider:

$$
R_{A,B}(x)=\frac{x^T A x}{x^T B x}.
$$

Substitute  $x=B^{-1/2}y$ . Compute numerator:

$$
x^T A x = y^T B^{-1/2} A B^{-1/2} y = y^T C y.
$$

Compute denominator:

$$
x^T B x = y^T B^{-1/2} B B^{-1/2} y = y^T I y = y^T y.
$$

Therefore:

$$
R_{A,B}(x)=\frac{y^T C y}{y^T y} = R_C(y).
$$

So maximizing the generalized Rayleigh quotient over  $x\neq 0$  is exactly maximizing the standard Rayleigh quotient of  $C$  over  $y\neq 0$ . By 6.3:

$$
\max_{x\neq 0} R_{A,B}(x) = \lambda_{\max}(C), \qquad \min_{x\neq 0} R_{A,B}(x) = \lambda_{\min}(C).
$$

Equivalently:

$$
\max_{\|x\|_B=1} x^T A x = \lambda_{\max}(A,B),
$$

where  $\|x\|_B^2 := x^T B x$ .

So generalized eigenvalues are again “best constants” in quadratic inequalities, but now measured in the geometry induced by  $B$ .

* * *

### 6.7 The “best constant” interpretation:  $A \preceq tB$  and  $\lambda_{\max}$ 

This is where PSD order and generalized eigenvalues fuse perfectly.

We want the smallest scalar  $t$  such that:

$$
A \preceq tB.
$$

Unpack the PSD inequality:

$$
A \preceq tB \quad\Longleftrightarrow\quad x^T A x \le t\, x^T B x\ \ \forall x.
$$

Assume  $B\succ 0$  so  $x^T B x>0$  for  $x\neq 0$ . Divide both sides by  $x^T B x$ :

$$
\frac{x^T A x}{x^T B x} \le t\quad \forall x\neq 0.
$$

That means:

$$
\sup_{x\neq 0} R_{A,B}(x) \le t.
$$

So the smallest such  $t$  is exactly:

$$
t^\star = \sup_{x\neq 0} R_{A,B}(x) = \lambda_{\max}(A,B).
$$

This is an extremely important identity:

>  $\lambda_{\max}(A,B)$  is the minimal scalar making  $tB - A \succeq 0$ .

In other words, generalized eigenvalues are the “tight PSD dominance constants.”

This exact statement is what turns into SDP constraints and dual certificates in convex optimization.

* * *

### 6.8 Where Schur complement sneaks back in (two key appearances)

#### (A) Turning quadratic inequalities into LMIs

From Layer 4 you already have:

$$
x^T P^{-1} x \le t \quad\Longleftrightarrow\quad \begin{bmatrix} P & x\\ x^T & t \end{bmatrix}\succeq 0 \quad (P\succ 0).
$$

This is a Schur complement equivalence. It’s the canonical way to express quadratic constraints as SDP constraints.

#### (B) Generalized eigenvalues as LMI feasibility in  $t$ 

Consider the scalar  $t$  and the constraint:

$$
tB - A \succeq 0.
$$

Feasibility depends on  $t$ . The smallest feasible  $t$  is  $\lambda_{\max}(A,B)$  as shown above. So generalized eigenvalue computation is literally:

> Find the smallest  $t$  such that an LMI holds.

That viewpoint is how generalized eigenvalues become a subroutine inside many convex optimization problems.

* * *

### 6.9 Edge cases and failure modes (don’t skip these)

1.  If  $A$  is not symmetric, the Rayleigh quotient story does not directly apply. You then use symmetric parts or move to singular values (SVD).
2.  If  $B\succeq 0$  but singular, the denominator  $x^T B x$  can be zero for nonzero  $x$ , and  $R_{A,B}(x)$  can blow up or be undefined. The correct generalized eigenproblem then lives on  $\operatorname{Range}(B)$  with additional consistency conditions (this is where pseudoinverses and range conditions appear, similar in spirit to generalized Schur complement).
3.  If  $B$  is indefinite, then  $x^T B x$  can be negative; the quotient is no longer bounded in general. The optimization interpretation changes completely.

For most convex optimization contexts (SDP, trust-region duality, ellipsoids), the safe and standard setting is  $B\succ 0$ .

* * *

### 6.10 What you should be able to do after this layer

You “own” this layer if you can derive these without memorization:

*   Prove  $\max_{\|x\|=1} x^T A x = \lambda_{\max}(A)$  for symmetric  $A$  via eigenbasis expansion.
*   Reduce  $Ax=\lambda Bx$  with  $B\succ 0$  to an ordinary eigenproblem via  $C=B^{-1/2}AB^{-1/2}$ .
*   Prove  $\max_{x\neq 0} \frac{x^T A x}{x^T B x} = \lambda_{\max}(A,B)$  using that reduction.
*   Prove the tight PSD dominance identity:
    $$
    \lambda_{\max}(A,B) = \min\{t:\ tB-A\succeq 0\}.
    $$
*   Explain how Schur complement turns quadratic forms and inverses into PSD block constraints.

* * *

If you keep going, the natural Layer 7 is the one that Boyd & Vandenberghe problems love: **KKT systems, block elimination, and trust-region duality**. That layer uses exactly: Schur complement + PSD order + generalized eigenvalues to explain why certain nonconvex quadratics still have exact duals.

## Response:
Thought for 10s

Layer 7 — Lagrangians, KKT conditions, block elimination, and why Schur complement is the algebra of optimality
---------------------------------------------------------------------------------------------------------------

_(this is where eigen/SVD/Schur stop being “linear algebra topics” and become the backbone of optimization)_

Up to now you built the _static geometry_ of linear maps (kernel/image), the _best coordinates_ (eigen/SVD), and the _block elimination rule_ (Schur complement). Layer 7 is where those fuse into one machine:

> Optimization optimality conditions are linear algebra statements about subspaces + block matrices.  
> Solving them is Schur complement elimination.  
> Spectral objects (eigenvalues/singular values) show up as “best constants” in feasibility/duality.

I’ll build it from the ground up.

* * *

7.1 Start from the most basic constrained optimization object: “minimize with constraints”
==========================================================================================

A general constrained problem looks like:

$$
\min_x \ f(x)\quad \text{s.t.}\quad h_i(x)=0\ (i=1,\dots,p),\quad g_j(x)\le 0\ (j=1,\dots,m).
$$

Three geometric facts:

1.  Equalities  $h(x)=0$  typically carve an **affine manifold** (locally a flat-ish slice).
2.  Inequalities  $g(x)\le 0$  carve a **region**; active constraints define the boundary.
3.  At optimum, the “direction of steepest descent” is blocked by the constraint geometry.

KKT formalizes “blocked descent” using linear algebra.

* * *

7.2 Lagrangian: turning constraints into algebra
================================================

Define the **Lagrangian**:

$$
\mathcal L(x,\nu,\lambda) := f(x) + \sum_{i=1}^p \nu_i h_i(x) + \sum_{j=1}^m \lambda_j g_j(x),
$$

where:

*    $\nu\in\mathbb R^p$  are equality multipliers (free sign),
*    $\lambda\in\mathbb R^m$  are inequality multipliers (must be  $\lambda\ge 0$ ).

Why this form? Because it’s the most general way to add constraint penalties while keeping linearity in multipliers. That linearity is what creates duality.

* * *

7.3 KKT conditions: the “optimality = orthogonality + complementarity” law
==========================================================================

Under standard regularity assumptions (constraint qualification; think “constraints meet nicely”), a primal optimum  $x^\star$  must satisfy KKT:

1.  **Primal feasibility**
    
$$
h_i(x^\star)=0,\quad g_j(x^\star)\le 0.
$$
2.  **Dual feasibility**
    
$$
\lambda^\star \ge 0.
$$
3.  **Stationarity** (gradient balance)
    
$$
\nabla f(x^\star) + \sum_{i=1}^p \nu_i^\star \nabla h_i(x^\star) + \sum_{j=1}^m \lambda_j^\star \nabla g_j(x^\star) =0.
$$
4.  **Complementary slackness**
    
$$
\lambda_j^\star\, g_j(x^\star)=0 \quad \forall j.
$$

The deepest meaning (connect to Layer 5 orthogonality):

*   The gradients  $\nabla h_i(x^\star)$  and active  $\nabla g_j(x^\star)$  span the **normal space** to the feasible set at  $x^\star$ .
*   Stationarity says  $-\nabla f(x^\star)$  lies in that normal cone: it has no feasible descent direction.

Complementary slackness is the “only active constraints matter” rule:  
if  $g_j(x^\star)<0$  (inactive), then  $\lambda_j^\star=0$ .

* * *

7.4 Equality-constrained quadratic minimization: the cleanest place to see KKT as a block linear system
=======================================================================================================

This is the canonical “linear algebra core” example.

Consider:

$$
\min_x \ \frac12 x^T Q x + c^T x \quad \text{s.t.}\quad A x = b,
$$

with  $Q=Q^T$  (not necessarily PD yet),  $A\in\mathbb R^{p\times n}$ .

### Step 1: Lagrangian

$$
\mathcal L(x,\nu) = \frac12 x^T Q x + c^T x + \nu^T(Ax-b).
$$

### Step 2: Stationarity w.r.t.  $x$ 

Compute gradient:

$$
\nabla_x \mathcal L = Qx + c + A^T\nu.
$$

Set to zero:

$$
Qx + A^T\nu = -c.
$$

### Step 3: Primal feasibility

$$
Ax=b.
$$

### Step 4: Assemble KKT linear system

Put the two vector equations together:

$$
\begin{bmatrix} Q & A^T\\ A & 0 \end{bmatrix} \begin{bmatrix} x\\ \nu \end{bmatrix} = \begin{bmatrix} -c\\ b \end{bmatrix}.
$$

This block matrix is called the **KKT matrix**.

Now the key point:

> Solving KKT is solving a block linear system.  
> Eliminating blocks is Schur complement.

* * *

7.5 Elimination via Schur complement: how you actually solve KKT
================================================================

Assume  $Q$  is invertible for the moment.

From stationarity:

$$
Qx = -c - A^T\nu \quad\Rightarrow\quad x = -Q^{-1}c - Q^{-1}A^T\nu.
$$

Plug into  $Ax=b$ :

$$
A(-Q^{-1}c - Q^{-1}A^T\nu)=b
$$
 
$$
- A Q^{-1}c - A Q^{-1}A^T \nu = b.
$$

So:

$$
(AQ^{-1}A^T)\nu = -(b + AQ^{-1}c).
$$

That matrix

$$
S := AQ^{-1}A^T
$$

is exactly the **Schur complement** of  $Q$  in the KKT matrix. You’ve literally just done block elimination.

Once you solve for  $\nu$ , recover  $x$  from the expression above.

This is why Schur complement is not “a trick”; it’s the algebraic content of “solve constraints + stationarity simultaneously.”

* * *

7.6 Inequality constraints: KKT becomes a _mixed_ linear–complementarity system
===============================================================================

Now add inequalities, simplest quadratic case:

$$
\min_x \ \frac12 x^T Q x + c^T x \quad \text{s.t.}\quad Gx \le h.
$$

Lagrangian:

$$
\mathcal L(x,\lambda)=\frac12 x^T Q x + c^T x + \lambda^T(Gx-h),\quad \lambda\ge 0.
$$

KKT:

*   Stationarity:  $Qx + c + G^T\lambda = 0$ 
*   Primal feasibility:  $Gx\le h$ 
*   Dual feasibility:  $\lambda\ge 0$ 
*   Complementary slackness:  $\lambda_i (Gx-h)_i = 0$ 

This is no longer a pure linear system because of the product constraints. But once you guess the active set (which inequalities are tight), it reduces to an equality-constrained system like 7.4–7.5. That’s why active-set methods exist.

* * *

7.7 Duality: why we “maximize a lower bound” (and where eigenvalues appear)
===========================================================================

Define the **dual function**:

$$
g(\nu,\lambda) := \inf_x \mathcal L(x,\nu,\lambda).
$$

General fact (always true, no convexity needed):

*    $g(\nu,\lambda)$  is a lower bound on the primal optimum for any  $\lambda\ge 0$ .
*   So maximizing  $g$  gives the best lower bound:
    
$$
\max_{\lambda\ge 0,\nu} g(\nu,\lambda).
$$

When  $f$  is convex and constraints are convex (plus Slater conditions), this lower bound becomes exact: **strong duality**.

But even in some nonconvex quadratic problems (trust-region), the dual can still be exact—this is where your earlier trust-region work fits.

* * *

7.8 Trust-region as the “spectral + Schur + KKT” showcase
=========================================================

Consider the trust-region subproblem (your Boyd-style friend):

$$
\min_x \ x^T A x + 2b^T x \quad \text{s.t.}\quad \|x\|_2^2 \le 1,
$$

with symmetric  $A$  (possibly indefinite).

### Step 1: Lagrangian

Constraint is  $x^Tx - 1 \le 0$ . Multiplier  $\lambda\ge 0$ .

$$
\mathcal L(x,\lambda)=x^T A x + 2b^T x + \lambda(x^Tx - 1) = x^T(A+\lambda I)x + 2b^T x - \lambda.
$$

### Step 2: Dual function  $g(\lambda)=\inf_x \mathcal L(x,\lambda)$ 

This infimum over  $x$  is a quadratic minimization. Two cases:

*   If  $A+\lambda I \not\succeq 0$ , then the quadratic in  $x$  is unbounded below (you can run off along a negative curvature direction), so:
    
$$
g(\lambda)=-\infty.
$$
*   If  $A+\lambda I \succ 0$ , then the quadratic is strictly convex and the minimizer solves:
    
$$
\nabla_x \mathcal L = 2(A+\lambda I)x + 2b = 0 \Rightarrow (A+\lambda I)x = -b \Rightarrow x(\lambda)=-(A+\lambda I)^{-1}b.
$$

Plug back to get the minimum value (complete the square):

$$
\inf_x \left[x^T(A+\lambda I)x + 2b^T x\right] = - b^T(A+\lambda I)^{-1}b.
$$

So:

$$
g(\lambda)= - b^T(A+\lambda I)^{-1}b - \lambda, \quad \text{valid when } A+\lambda I \succ 0.
$$

Thus the dual problem is:

$$
\max_{\lambda\ge 0}\ \ - b^T(A+\lambda I)^{-1}b - \lambda \quad \text{s.t.}\quad A+\lambda I \succeq 0.
$$

This is exactly where:

*   PSD order (Layer 6),
*   Schur complement (Layer 4),
*   and spectral properties (eigenvalues of  $A$ , because  $A+\lambda I\succeq 0 \iff \lambda \ge -\lambda_{\min}(A)$ )  
    all show up at once.

That last equivalence is a direct Rayleigh quotient fact:

$$
A+\lambda I\succeq 0 \iff x^T(A+\lambda I)x\ge 0\ \forall x \iff x^TAx \ge -\lambda \|x\|^2\ \forall x \iff \lambda \ge -\lambda_{\min}(A).
$$

So the _feasible set_ of the dual is spectral.

* * *

7.9 Schur complement reformulation: turning inverses into LMIs (again)
======================================================================

Dual constraints and objectives often involve terms like  $b^T(A+\lambda I)^{-1}b$ . In SDP modeling, you replace these with block LMIs.

For  $P\succ 0$ , you already proved:

$$
b^T P^{-1} b \le t \quad\Longleftrightarrow\quad \begin{bmatrix} P & b\\ b^T & t \end{bmatrix}\succeq 0.
$$

So if you introduce an auxiliary scalar  $t$  for the trust-region dual, you can rewrite parts of it as an LMI. That’s exactly how many quadratic duals become SDPs.

This is the universal pattern:

*   inverse inside scalar quadratic form  
    → Schur complement  
    → block PSD constraint.

* * *

7.10 What you should be able to do after Layer 7
================================================

You own this layer if you can do these cleanly:

1.  Write the Lagrangian for equality/inequality problems and state KKT without handwaving.
2.  Derive the KKT block matrix for equality-constrained QP and eliminate variables via Schur complement.
3.  Explain stationarity as an orthogonality / normal-cone statement.
4.  For trust-region, derive the dual function by analyzing when the quadratic infimum is finite, and compute the minimizing  $x(\lambda)$ .
5.  Translate “ $A+\lambda I\succeq 0$ ” into a condition on  $\lambda$  using eigenvalues / Rayleigh quotient.
6.  Use Schur complement to replace  $b^T P^{-1}b$  terms with block PSD constraints.

* * *

If you keep saying “Next,” the natural Layer 8 is: **Semidefinite programming modeling templates** (LMIs, Schur complement patterns, and how SVD/eigenvalue facts become convex constraints like  $\lambda_{\max}(X)\le t$ ,  $\|A\|_2\le t$ , ellipsoids, and robust constraints). That’s the “language” layer where all the previous math becomes a toolbox you can deploy on problems.

## Response:
Layer 8 — SDP and LMI modeling templates
----------------------------------------

_(the “language layer”: how eigenvalues/SVD/Schur become convex constraints you can actually write and solve)_

By now you’ve built the math. This layer is about becoming fluent in the _grammar_ of semidefinite programming: how to turn statements about norms, eigenvalues, inverses, quadratics, and robustness into **linear matrix inequalities (LMIs)**.

The core slogan is:

> In SDP, you don’t optimize over numbers.  
> You optimize over **matrices** with the constraint “this matrix is PSD”.

And Schur complement is the main translation rule.

* * *

### 8.1 The PSD cone and why it’s convex

Let  $\mathbb S^n$  be symmetric  $n\times n$  matrices.

Define the PSD cone:

$$
\mathbb S_+^n := \{X\in\mathbb S^n : X\succeq 0\} = \{X : x^T X x \ge 0\ \forall x\}.
$$

Convexity proof (fully explicit): take  $X,Y\succeq 0$ , and  $\theta\in[0,1]$ . For any  $x$ ,

$$
x^T(\theta X+(1-\theta)Y)x = \theta x^T X x + (1-\theta)x^T Y x \ge 0.
$$

So  $\theta X+(1-\theta)Y\succeq 0$ . Hence  $\mathbb S_+^n$  is convex.

This is why constraints like “ $X\succeq 0$ ” are convex constraints.

* * *

### 8.2 What an SDP is (and what an LMI is)

An SDP in standard primal form:

$$
\min_{X\in\mathbb S^n}\ \langle C,X\rangle \quad \text{s.t.}\quad \langle A_i,X\rangle = b_i\ (i=1,\dots,m),\quad X\succeq 0,
$$

where  $\langle C,X\rangle := \mathrm{tr}(C^T X)=\mathrm{tr}(CX)$  is the Frobenius/trace inner product.

An LMI (linear matrix inequality) is a constraint of the form:

$$
F(x) := F_0 + \sum_{k=1}^p x_k F_k \succeq 0
$$

where the matrix depends affinely on decision variables  $x$ .

So: **SDP = linear objective + affine equalities + an LMI**.

* * *

### 8.3 The master translation rule: Schur complement templates

This is the biggest “cookbook” you should memorize conceptually (not by rote):

1.  **Quadratic form with inverse**  
    For  $P\succ 0$ ,
    
$$
x^T P^{-1}x \le t \quad\Longleftrightarrow\quad \begin{bmatrix} P & x\\ x^T & t \end{bmatrix}\succeq 0.
$$
2.  **Norm bound (SOC as an LMI)**
    
$$
\|x\|_2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} tI & x\\ x^T & t \end{bmatrix}\succeq 0,\ \ t\ge 0.
$$

(Apply Schur complement: PSD iff  $tI\succeq 0$  and  $t - x^T(tI)^{-1}x = t - \|x\|^2/t \ge 0$ , i.e.  $\|x\|\le t$ .)

3.  **Bilinear-looking term made convex by lifting**  
    If you see  $xx^T$ , introduce a matrix variable  $X\succeq xx^T$ . Then:
    
$$
X \succeq xx^T \quad\Longleftrightarrow\quad \begin{bmatrix} X & x\\ x^T & 1 \end{bmatrix}\succeq 0.
$$

This is the “lift-and-relax” move behind many SDP relaxations.

* * *

### 8.4 Eigenvalue constraints become LMIs

This is where Layer 6 (Rayleigh quotient) becomes modeling.

Key equivalence:

$$
\lambda_{\max}(X) \le t \quad\Longleftrightarrow\quad X \preceq tI \quad\Longleftrightarrow\quad tI - X \succeq 0.
$$

Why it’s true:  $X\preceq tI$  means  $x^T X x \le t\|x\|^2$  for all  $x$ , and the smallest such  $t$  is exactly  $\lambda_{\max}(X)$ .

Similarly:

$$
\lambda_{\min}(X) \ge t \quad\Longleftrightarrow\quad X \succeq tI.
$$

So bounding eigenvalues is literally an LMI.

This single fact powers a ton of convex constraints: spectral radius bounds, stability, robust bounds, etc.

* * *

### 8.5 Spectral norm constraints via an LMI (SVD enters)

For a general (not necessarily symmetric) matrix  $A$ , the spectral norm is  $\|A\|_2=\sigma_{\max}(A)$ .

Template:

$$
\|A\|_2 \le t \quad\Longleftrightarrow\quad \begin{bmatrix} tI & A\\ A^T & tI \end{bmatrix}\succeq 0,\ \ t\ge 0.
$$

Derivation sketch (the real reason): that block matrix PSD is equivalent (by Schur complement) to

$$
tI - A(tI)^{-1}A^T \succeq 0 \ \Longleftrightarrow\ t^2 I - AA^T \succeq 0
$$

which means all eigenvalues of  $AA^T$  are  $\le t^2$ , i.e. all singular values of  $A$  are  $\le t$ .

So SVD  $\leftrightarrow$  Schur complement  $\leftrightarrow$  LMI.

* * *

### 8.6 Quadratic constraints and ellipsoids: SDP “sees” them cleanly

An ellipsoid constraint:

$$
(x-c)^T P^{-1} (x-c) \le 1,\quad P\succ 0
$$

is equivalent to:

$$
\begin{bmatrix} P & x-c\\ (x-c)^T & 1 \end{bmatrix}\succeq 0.
$$

This is the backbone of:

*   minimum-volume ellipsoids,
*   robust least squares with ellipsoidal uncertainty,
*   Mahalanobis distance constraints.

* * *

### 8.7 Robust optimization via the S-lemma / S-procedure (why SDP appears in “for all uncertainties”)

A very common robust constraint looks like:

$$
\text{for all } u \text{ with } u^T Q u \le 1,\quad (a+Bu)^T x \le c.
$$

“ $\forall u$ ” is scary. SDP often replaces it with an LMI using a multiplier (very Lagrange-duality flavored). The S-lemma says, under conditions, a quadratic implication is equivalent to existence of  $\lambda\ge 0$  such that a certain block matrix is PSD.

You don’t need the full theorem memorized yet—what you need is the pattern recognition:

> Robust quadratic constraints almost always become “there exists  $\lambda\ge 0$  such that an LMI holds”.

That’s the robust-optimization analog of KKT.

* * *

### 8.8 Lyapunov stability (a canonical “control” LMI)

For a linear system  $\dot x = Ax$ , a sufficient condition for asymptotic stability is: there exists  $P\succ 0$  such that

$$
A^T P + P A \prec 0.
$$

This is an LMI in  $P$ . It’s a pure SDP feasibility problem.

Why it’s convex:  $P\mapsto A^T P + P A$  is affine in  $P$ , and “ $\prec 0$ ” is just PSD order on  $-(\cdot)$ .

This is a great example where “eigenvalues of  $A$ ” are hard directly, but an LMI certificate is convex and computable.

* * *

### 8.9 The dual of an SDP (why certificates look like PSD matrices)

You don’t need full dual derivation every time, but you should know the shape:

Primal:

$$
\min_X \langle C,X\rangle\ \ \text{s.t.}\ \ \langle A_i,X\rangle=b_i,\ X\succeq 0.
$$

Dual:

$$
\max_y \ b^T y\ \ \text{s.t.}\ \ C - \sum_i y_i A_i \succeq 0.
$$

Interpretation: the dual variables build a matrix that must be PSD. That PSD matrix is the “certificate” that your lower bound is valid—same philosophy as Lagrange duality, but in matrix form.

* * *

### 8.10 The modeling “muscle memory” you want (core templates)

| If you see… | Try… |
| --- | --- |
|  $\lambda_{\max}(X)\le t$  |  $tI-X\succeq 0$  |
|  $\|A\|_2 \le t$  |  $\begin{bmatrix}tI&A\\A^T&tI\end{bmatrix}\succeq 0$  |
|  $x^T P^{-1}x \le t$  |  $\begin{bmatrix}P&x\\x^T&t\end{bmatrix}\succeq 0$  |
|  $X \succeq xx^T$  |  $\begin{bmatrix}X&x\\x^T&1\end{bmatrix}\succeq 0$  |
| Quadratic + elimination | form block matrix, take Schur complement |

(That table is the whole “SDP translation dictionary” in miniature.)

* * *

### 8.11 What “owning Layer 8” means

You own this layer if you can do all of the following without black-boxing:

1.  Prove  $X\succeq 0$  is convex from the definition  $x^T X x\ge 0\ \forall x$ .
2.  Convert eigenvalue bounds to LMIs using PSD order and Rayleigh quotient logic.
3.  Derive the spectral norm LMI  $\begin{bmatrix}tI&A\\A^T&tI\end{bmatrix}\succeq 0$  via Schur complement and  $AA^T$ .
4.  Convert inverse-quadratic constraints to block LMIs by Schur complement.
5.  Explain, at least qualitatively, why “robust for all  $u$ ” often introduces a multiplier  $\lambda$  and becomes an LMI.

* * *

If you want the next layer after this: it’s usually **(Layer 9) canonical cones and reductions** — how SOCP is a special case of SDP, how to recognize when SDP is overkill, and how to systematically reduce problems (norms, max-eigenvalue, log-det, nuclear norm) into standard conic forms.

## Response:
Thought for 40s

Below is a single self-contained HTML file (no libraries) that gives you **3 animated interactive demos**:

1.  **Eigen (symmetric 2×2)**: unit circle → ellipse, rotating vector, eigenvectors drawn, Rayleigh quotient shown.
2.  **SVD (general 2×2)**: animates the factorization  $A = U\Sigma V^T$  as **circle → (apply  $V^T$ ) → (apply  $\Sigma$ ) → (apply  $U$ )**.
3.  **Schur complement (2×2 quadratic form)**: visualizes  $q(x,y)=ax^2+2bxy+dy^2$ , completes the square, shows the minimizing  $y^\*(x)=-(b/d)x$ , and displays  $a-b^2/d$ .

Save as `linear_algebra_animations.html` and open in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Eigen / SVD / Schur — Animated Walkthrough</title>
  <style>
    :root { color-scheme: dark; }
    body { margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; background:#0b0f14; color:#d8e1ea; }
    .wrap { display:grid; grid-template-columns: 380px 1fr; gap: 12px; height:100vh; }
    .panel { padding:14px; border-right: 1px solid #17212b; overflow:auto; }
    .panel h1 { font-size:16px; margin:0 0 8px 0; }
    .panel h2 { font-size:13px; margin:14px 0 8px 0; color:#b7c7d8; }
    .row { display:flex; gap:10px; align-items:center; margin: 8px 0; }
    .row label { width:44px; color:#b7c7d8; font-size:12px; }
    input[type="range"] { width: 100%; }
    input[type="number"] { width:80px; background:#0f1620; border:1px solid #223244; color:#d8e1ea; padding:6px; border-radius:8px; }
    .seg { display:flex; gap:8px; flex-wrap:wrap; margin: 10px 0; }
    .btn, .pill {
      background:#0f1620; border:1px solid #223244; color:#d8e1ea;
      padding:8px 10px; border-radius:10px; cursor:pointer; user-select:none;
      font-size:12px;
    }
    .pill { display:flex; align-items:center; gap:8px; }
    .btn:hover, .pill:hover { border-color:#3a5872; }
    .btn.active { background:#142233; border-color:#6aa2d8; }
    .note { font-size:12px; color:#b7c7d8; line-height:1.35; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
    canvas { width:100%; height:100%; display:block; background: radial-gradient(1200px 700px at 60% 40%, #0f1620 0%, #0b0f14 55%, #070a0e 100%); }
    .footer { margin-top: 10px; padding-top: 10px; border-top: 1px solid #17212b; }
    .small { font-size:11px; color:#9fb0c2; }
  </style>
</head>
<body>
<div class="wrap">
  <div class="panel">
    <h1>Eigen / SVD / Schur — animations</h1>
    <div class="note">
      Pick a mode, move sliders, hit Play. This is a “see it happen” companion to the algebra:
      eigenvectors = invariant directions, SVD = rotate→scale→rotate, Schur = eliminate a block by completing the square.
    </div>

    <h2>Mode</h2>
    <div class="seg">
      <div id="modeEigen" class="btn active">Eigen (symmetric)</div>
      <div id="modeSVD" class="btn">SVD (general)</div>
      <div id="modeSchur" class="btn">Schur (quadratic)</div>
    </div>

    <h2>Controls</h2>
    <div class="seg">
      <div id="btnPlay" class="btn active">Play</div>
      <div id="btnStep" class="btn">Step</div>
      <div id="btnReset" class="btn">Reset phase</div>
    </div>

    <div class="row">
      <label>Speed</label>
      <input id="speed" type="range" min="0" max="100" value="45"/>
    </div>

    <h2>Matrix entries</h2>
    <div class="note small">
      Eigen + Schur use a symmetric 2×2: <span class="mono">[[a, b],[b, d]]</span>.<br/>
      SVD uses general 2×2: <span class="mono">[[a, b],[c, d]]</span>.
    </div>

    <div id="rowA" class="row">
      <label>a</label>
      <input id="a" type="range" min="-3" max="3" step="0.01" value="1.2"/>
      <input id="aN" type="number" step="0.01" value="1.2"/>
    </div>
    <div id="rowB" class="row">
      <label>b</label>
      <input id="b" type="range" min="-3" max="3" step="0.01" value="0.9"/>
      <input id="bN" type="number" step="0.01" value="0.9"/>
    </div>
    <div id="rowC" class="row">
      <label>c</label>
      <input id="c" type="range" min="-3" max="3" step="0.01" value="-0.6"/>
      <input id="cN" type="number" step="0.01" value="-0.6"/>
    </div>
    <div id="rowD" class="row">
      <label>d</label>
      <input id="d" type="range" min="-3" max="3" step="0.01" value="1.0"/>
      <input id="dN" type="number" step="0.01" value="1.0"/>
    </div>

    <h2>Readouts</h2>
    <div id="readout" class="note mono"></div>

    <div class="footer">
      <div class="small">
        Tip: In Eigen mode, set <span class="mono">b≈0</span> to see axes become eigenvectors. In SVD mode, try a shear
        (e.g. a=1, b=1.2, c=0, d=1). In Schur mode, watch how PSD needs <span class="mono">d&gt;0</span> and <span class="mono">a-b²/d ≥ 0</span>.
      </div>
    </div>
  </div>

  <div style="position:relative;">
    <canvas id="cv"></canvas>
  </div>
</div>

<script>
/* ============================
   Small linear algebra helpers
   ============================ */
const EPS = 1e-10;

function mat2(a,b,c,d){ return {a,b,c,d}; } // [[a,b],[c,d]]
function mat2T(M){ return mat2(M.a, M.c, M.b, M.d); }
function mat2Mul(A,B){
  return mat2(
    A.a*B.a + A.b*B.c,  A.a*B.b + A.b*B.d,
    A.c*B.a + A.d*B.c,  A.c*B.b + A.d*B.d
  );
}
function mat2Vec(M,x,y){ return [M.a*x + M.b*y, M.c*x + M.d*y]; }
function dot(x,y){ return x[0]*y[0] + x[1]*y[1]; }
function norm(x){ return Math.hypot(x[0], x[1]); }
function scale(v,s){ return [v[0]*s, v[1]*s]; }
function add(u,v){ return [u[0]+v[0], u[1]+v[1]]; }
function sub(u,v){ return [u[0]-v[0], u[1]-v[1]]; }
function normalize(v){
  const n = norm(v);
  if (n < EPS) return [1,0];
  return [v[0]/n, v[1]/n];
}
function ortho(v){ return [-v[1], v[0]]; } // rotate +90°
function clamp(x,lo,hi){ return Math.max(lo, Math.min(hi, x)); }

/* Eigen of symmetric 2x2 [[a,b],[b,d]]:
   eigenvalues: t±s, where t=(a+d)/2, s=sqrt(((a-d)/2)^2 + b^2)
   eigenvector for λ can be taken as [b, λ-a] (unless both ~0), else [λ-d, b]
*/
function eigSym2(a,b,d){
  const t = 0.5*(a+d);
  const delta = 0.5*(a-d);
  const s = Math.sqrt(delta*delta + b*b);
  const l1 = t + s;
  const l2 = t - s;

  function eigvec(lambda){
    let v = [b, lambda - a];
    if (norm(v) < EPS) v = [lambda - d, b];
    if (norm(v) < EPS) v = [1,0];
    return normalize(v);
  }
  const v1 = eigvec(l1);
  // For symmetric, v2 is orthogonal to v1 (can choose ortho)
  const v2 = normalize(ortho(v1));
  return { l1, l2, v1, v2 };
}

/* SVD for 2x2 via eigen of A^T A.
   Steps:
   - Compute G = A^T A (symmetric PSD).
   - Eigenpairs of G give v_i (right singular vectors) and λ_i=σ_i^2.
   - σ_i = sqrt(λ_i).
   - u_i = A v_i / σ_i for σ_i>0, else pick orthonormal completion.
*/
function svd2(A){
  const AT = mat2T(A);
  const G = mat2Mul(AT, A); // n=2 so 2x2
  // G is symmetric: [[g11,g12],[g12,g22]]
  const g11 = G.a, g12 = G.b, g22 = G.d;
  const { l1, l2, v1, v2 } = eigSym2(g11, g12, g22);

  let s1 = Math.sqrt(Math.max(0, l1));
  let s2 = Math.sqrt(Math.max(0, l2));

  // Ensure ordering s1 >= s2; if not, swap.
  let V1=v1, V2=v2;
  if (s2 > s1 + 1e-12){
    [s1,s2] = [s2,s1];
    [V1,V2] = [V2,V1];
  }

  // Left singulars
  let U1, U2;
  if (s1 > EPS){
    const Av1 = mat2Vec(A, V1[0], V1[1]);
    U1 = normalize(scale(Av1, 1/s1));
  } else {
    U1 = [1,0];
  }
  // For second, either compute or complete orthonormally
  if (s2 > EPS){
    const Av2 = mat2Vec(A, V2[0], V2[1]);
    U2 = normalize(scale(Av2, 1/s2));
    // Make sure orthonormal (numerical cleanup)
    // Orthogonalize U2 against U1
    const proj = dot(U2,U1);
    U2 = normalize(sub(U2, scale(U1, proj)));
  } else {
    U2 = normalize(ortho(U1));
  }

  // Build U and V with columns [u1 u2], [v1 v2]
  const U = mat2(U1[0], U2[0], U1[1], U2[1]);
  const V = mat2(V1[0], V2[0], V1[1], V2[1]);
  const VT = mat2T(V);
  const Sigma = mat2(s1,0,0,s2);

  return { U, Sigma, V, VT, s1, s2, u1:U1, u2:U2, v1:V1, v2:V2 };
}

/* ============================
   Canvas + rendering
   ============================ */
const canvas = document.getElementById('cv');
const ctx = canvas.getContext('2d');

function resize(){
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.floor(canvas.clientWidth * dpr);
  canvas.height = Math.floor(canvas.clientHeight * dpr);
  ctx.setTransform(dpr,0,0,dpr,0,0);
}
window.addEventListener('resize', resize);
resize();

function clear(){
  ctx.clearRect(0,0,canvas.clientWidth, canvas.clientHeight);
}

// Coordinate transform: world -> screen
function makeView(){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const cx = 0.52*w, cy = 0.52*h;
  const scalePx = Math.min(w,h)*0.23;
  return { w,h,cx,cy,scalePx };
}
function toScreen(view, p){
  return [view.cx + view.scalePx*p[0], view.cy - view.scalePx*p[1]];
}
function drawAxes(view){
  ctx.save();
  ctx.globalAlpha = 0.35;
  ctx.strokeStyle = "#9fb0c2";
  ctx.lineWidth = 1;
  // x axis
  ctx.beginPath();
  ctx.moveTo(0, view.cy);
  ctx.lineTo(view.w, view.cy);
  ctx.stroke();
  // y axis
  ctx.beginPath();
  ctx.moveTo(view.cx, 0);
  ctx.lineTo(view.cx, view.h);
  ctx.stroke();
  ctx.restore();
}
function drawGrid(view){
  ctx.save();
  ctx.globalAlpha = 0.12;
  ctx.strokeStyle = "#9fb0c2";
  ctx.lineWidth = 1;
  const step = view.scalePx/2;
  for(let x=view.cx%step; x<view.w; x+=step){
    ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,view.h); ctx.stroke();
  }
  for(let y=view.cy%step; y<view.h; y+=step){
    ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(view.w,y); ctx.stroke();
  }
  ctx.restore();
}

function drawPolyline(view, pts, stroke="#d8e1ea", alpha=1, lw=2){
  if (!pts.length) return;
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = stroke;
  ctx.lineWidth = lw;
  ctx.beginPath();
  const p0 = toScreen(view, pts[0]);
  ctx.moveTo(p0[0], p0[1]);
  for(let i=1;i<pts.length;i++){
    const p = toScreen(view, pts[i]);
    ctx.lineTo(p[0], p[1]);
  }
  ctx.closePath();
  ctx.stroke();
  ctx.restore();
}

function drawArrow(view, from, to, color="#d8e1ea", alpha=1, lw=2){
  const a = toScreen(view, from);
  const b = toScreen(view, to);
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = lw;
  ctx.beginPath();
  ctx.moveTo(a[0], a[1]);
  ctx.lineTo(b[0], b[1]);
  ctx.stroke();
  // arrowhead
  const dx = b[0]-a[0], dy = b[1]-a[1];
  const L = Math.hypot(dx,dy);
  if (L > 1e-6){
    const ux = dx/L, uy = dy/L;
    const size = 10;
    const left = [b[0] - size*(ux*0.9 - uy*0.4), b[1] - size*(uy*0.9 + ux*0.4)];
    const right= [b[0] - size*(ux*0.9 + uy*0.4), b[1] - size*(uy*0.9 - ux*0.4)];
    ctx.beginPath();
    ctx.moveTo(b[0], b[1]);
    ctx.lineTo(left[0], left[1]);
    ctx.lineTo(right[0], right[1]);
    ctx.closePath();
    ctx.fill();
  }
  ctx.restore();
}

function drawPoint(view, p, color="#d8e1ea", r=4, alpha=1){
  const s = toScreen(view, p);
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(s[0], s[1], r, 0, Math.PI*2);
  ctx.fill();
  ctx.restore();
}

function circlePoints(N=240){
  const pts = [];
  for(let i=0;i<N;i++){
    const t = (i/N)*Math.PI*2;
    pts.push([Math.cos(t), Math.sin(t)]);
  }
  return pts;
}

const UNIT = circlePoints();

/* ============================
   UI state
   ============================ */
let mode = "eigen"; // "eigen" | "svd" | "schur"
let playing = true;
let phase = 0; // animation phase in [0, 1) looped
let stepOnce = false;

const dom = {
  a: document.getElementById('a'), aN: document.getElementById('aN'),
  b: document.getElementById('b'), bN: document.getElementById('bN'),
  c: document.getElementById('c'), cN: document.getElementById('cN'),
  d: document.getElementById('d'), dN: document.getElementById('dN'),
  speed: document.getElementById('speed'),
  readout: document.getElementById('readout'),
  rowC: document.getElementById('rowC'),
  modeEigen: document.getElementById('modeEigen'),
  modeSVD: document.getElementById('modeSVD'),
  modeSchur: document.getElementById('modeSchur'),
  btnPlay: document.getElementById('btnPlay'),
  btnStep: document.getElementById('btnStep'),
  btnReset: document.getElementById('btnReset')
};

function setMode(m){
  mode = m;
  dom.modeEigen.classList.toggle('active', m==="eigen");
  dom.modeSVD.classList.toggle('active', m==="svd");
  dom.modeSchur.classList.toggle('active', m==="schur");
  // show/hide c row for non-general modes
  dom.rowC.style.display = (m==="svd") ? "flex" : "none";
  phase = 0;
  updateReadout();
}
dom.modeEigen.onclick = () => setMode("eigen");
dom.modeSVD.onclick   = () => setMode("svd");
dom.modeSchur.onclick = () => setMode("schur");

dom.btnPlay.onclick = () => {
  playing = !playing;
  dom.btnPlay.classList.toggle('active', playing);
  dom.btnPlay.textContent = playing ? "Play" : "Paused";
};
dom.btnStep.onclick = () => { stepOnce = true; };
dom.btnReset.onclick = () => { phase = 0; };

function linkSlider(sl, num){
  const syncFromSlider = () => { num.value = sl.value; updateReadout(); };
  const syncFromNum = () => {
    const v = clamp(parseFloat(num.value), parseFloat(sl.min), parseFloat(sl.max));
    sl.value = v; num.value = v; updateReadout();
  };
  sl.addEventListener('input', syncFromSlider);
  num.addEventListener('change', syncFromNum);
}
linkSlider(dom.a, dom.aN);
linkSlider(dom.b, dom.bN);
linkSlider(dom.c, dom.cN);
linkSlider(dom.d, dom.dN);

function currentA(){
  const a = parseFloat(dom.a.value);
  const b = parseFloat(dom.b.value);
  const c = parseFloat(dom.c.value);
  const d = parseFloat(dom.d.value);
  if (mode==="svd"){
    return mat2(a,b,c,d);
  } else {
    // symmetric
    return mat2(a,b,b,d);
  }
}

function fmt(x){
  if (!isFinite(x)) return "NaN";
  const s = x.toFixed(4);
  // trim trailing zeros
  return s.replace(/\.?0+$/,'');
}

function updateReadout(){
  const A = currentA();
  if (mode==="eigen"){
    const { l1, l2, v1, v2 } = eigSym2(A.a, A.b, A.d);
    dom.readout.innerHTML =
      `A = [[${fmt(A.a)}, ${fmt(A.b)}],[${fmt(A.b)}, ${fmt(A.d)}]]\n` +
      `eigenvalues: λ1=${fmt(l1)}, λ2=${fmt(l2)}\n` +
      `eigenvectors (unit): v1=(${fmt(v1[0])}, ${fmt(v1[1])}), v2=(${fmt(v2[0])}, ${fmt(v2[1])})\n` +
      `Rayleigh: R(x)= (xᵀAx)/(xᵀx)`;
  } else if (mode==="svd"){
    const { s1, s2, u1, u2, v1, v2 } = svd2(A);
    dom.readout.innerHTML =
      `A = [[${fmt(A.a)}, ${fmt(A.b)}],[${fmt(A.c)}, ${fmt(A.d)}]]\n` +
      `singular values: σ1=${fmt(s1)}, σ2=${fmt(s2)}\n` +
      `right (V) unit vectors: v1=(${fmt(v1[0])}, ${fmt(v1[1])}), v2=(${fmt(v2[0])}, ${fmt(v2[1])})\n` +
      `left (U) unit vectors:  u1=(${fmt(u1[0])}, ${fmt(u1[1])}), u2=(${fmt(u2[0])}, ${fmt(u2[1])})\n` +
      `A = U Σ Vᵀ  (animated as: Vᵀ → Σ → U)`;
  } else {
    // Schur: q(x,y)= a x^2 + 2 b x y + d y^2 ; Schur of d: s = a - b^2/d
    const a = A.a, b = A.b, d = A.d;
    const s = (Math.abs(d) < EPS) ? NaN : (a - (b*b)/d);
    const psdHint = (d > 0 && s >= -1e-12) ? "PSD (looks ≥0)" : "NOT PSD (has negative direction)";
    dom.readout.innerHTML =
      `q(x,y)= a x² + 2 b x y + d y²\n` +
      `a=${fmt(a)}, b=${fmt(b)}, d=${fmt(d)}\n` +
      `complete square: q = d ( y + (b/d) x )² + ( a - b²/d ) x²  (when d≠0)\n` +
      `Schur complement of d: s = a - b²/d = ${fmt(s)}\n` +
      `PSD test (when d>0): need d>0 and s≥0  ⇒  ${psdHint}`;
  }
}
updateReadout();

/* ============================
   Rendering per mode
   ============================ */

function drawEigen(view, A, t){
  // rotating unit vector x(t)
  const ang = 2*Math.PI*t;
  const x = [Math.cos(ang), Math.sin(ang)];
  const Ax = mat2Vec(A, x[0], x[1]);

  const { l1, l2, v1, v2 } = eigSym2(A.a, A.b, A.d);

  // Rayleigh quotient for current x
  const xAx = dot(x, mat2Vec(A, x[0], x[1]));
  const xx = dot(x,x);
  const R = xAx/xx;

  // Draw unit circle and ellipse A(circle)
  const ell = UNIT.map(p => mat2Vec(A, p[0], p[1]));

  drawGrid(view);
  drawAxes(view);

  drawPolyline(view, UNIT, "#9fb0c2", 0.35, 2); // unit circle
  drawPolyline(view, ell, "#6aa2d8", 0.75, 2.5); // mapped ellipse

  // Eigenvectors as lines (both directions)
  const evScale = 1.35;
  drawArrow(view, [0,0], scale(v1, evScale), "#ffd166", 0.95, 2.5);
  drawArrow(view, [0,0], scale(v2, evScale), "#06d6a0", 0.95, 2.5);

  // Rotating vector x and its image Ax
  drawArrow(view, [0,0], x, "#f1fa8c", 0.95, 2.5);
  drawPoint(view, x, "#f1fa8c", 4.5, 1);

  drawArrow(view, [0,0], Ax, "#ff6b6b", 0.9, 2.5);
  drawPoint(view, Ax, "#ff6b6b", 4.5, 1);

  // Show labels
  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.9;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`Eigen mode (symmetric): A maps circle → ellipse.`, 18, 22);
  ctx.fillText(`λ1=${fmt(l1)}, λ2=${fmt(l2)}   Rayleigh R(x)=${fmt(R)}`, 18, 40);
  ctx.fillText(`Yellow/Green = eigen-directions. Pale = x(t), Red = A x(t).`, 18, 58);
  ctx.restore();
}

function drawSVD(view, A, t){
  // Compute SVD
  const { U, Sigma, VT, s1, s2, u1, u2, v1, v2 } = svd2(A);

  // Stage timing: 3 segments: V^T, then Sigma, then U (each 1/3 of loop)
  const seg = 1/3;
  let stage = Math.floor(t/seg); // 0,1,2
  stage = clamp(stage, 0, 2);
  const local = (t - stage*seg)/seg; // [0,1)

  // Precompute shapes
  const X0 = UNIT;
  const X1 = UNIT.map(p => mat2Vec(VT, p[0], p[1]));
  const X2 = X1.map(p => mat2Vec(Sigma, p[0], p[1]));
  const X3 = X2.map(p => mat2Vec(U, p[0], p[1]));

  function lerpPts(P,Q,alpha){
    const out = [];
    for(let i=0;i<P.length;i++){
      out.push([ (1-alpha)*P[i][0] + alpha*Q[i][0], (1-alpha)*P[i][1] + alpha*Q[i][1] ]);
    }
    return out;
  }

  let shape;
  let title;
  if (stage===0){
    shape = lerpPts(X0, X1, local);
    title = "Apply Vᵀ (rotate/reflect in input space)";
  } else if (stage===1){
    shape = lerpPts(X1, X2, local);
    title = "Apply Σ (axis-aligned scaling by σ₁, σ₂)";
  } else {
    shape = lerpPts(X2, X3, local);
    title = "Apply U (rotate/reflect in output space)";
  }

  // Also animate a single tracked vector
  const ang = 2*Math.PI*t;
  const x0 = [Math.cos(ang), Math.sin(ang)];
  const x1 = mat2Vec(VT, x0[0], x0[1]);
  const x2 = mat2Vec(Sigma, x1[0], x1[1]);
  const x3 = mat2Vec(U, x2[0], x2[1]);
  let x;
  if (stage===0) x = add(scale(x0, 1-local), scale(x1, local));
  else if (stage===1) x = add(scale(x1, 1-local), scale(x2, local));
  else x = add(scale(x2, 1-local), scale(x3, local));

  drawGrid(view);
  drawAxes(view);

  // Draw base + current + final
  drawPolyline(view, X0, "#9fb0c2", 0.22, 2);
  drawPolyline(view, X3, "#6aa2d8", 0.35, 2.5);
  drawPolyline(view, shape, "#ffd166", 0.95, 3);

  // Draw singular vectors in input (v's) and output (u's)
  const vecScale = 1.1;
  drawArrow(view, [0,0], scale(v1, vecScale), "#f1fa8c", 0.9, 2.5);
  drawArrow(view, [0,0], scale(v2, vecScale), "#06d6a0", 0.9, 2.5);

  // On output side: show u's scaled by σ (to match A v = σ u)
  drawArrow(view, [0,0], scale(u1, vecScale), "#ff6b6b", 0.55, 2.5);
  drawArrow(view, [0,0], scale(u2, vecScale), "#ff6b6b", 0.35, 2.5);

  // tracked point
  drawArrow(view, [0,0], x, "#ffd166", 0.95, 2.5);
  drawPoint(view, x, "#ffd166", 4.5, 1);

  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.92;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`SVD mode: A = U Σ Vᵀ`, 18, 22);
  ctx.fillText(`${title}`, 18, 40);
  ctx.fillText(`σ₁=${fmt(s1)}, σ₂=${fmt(s2)} | v's: yellow/green, u's: red`, 18, 58);
  ctx.restore();
}

function drawSchur(view, A, t){
  // Quadratic q(x,y) = a x^2 + 2 b x y + d y^2
  const a = A.a, b = A.b, d = A.d;
  const s = (Math.abs(d) < EPS) ? NaN : (a - (b*b)/d);

  drawGrid(view);
  drawAxes(view);

  // Draw level sets of q as contours (approx)
  // We'll sample a grid and draw a few contour levels via marching squares-ish light approach:
  // simpler: draw many points whose q is near certain levels.
  const levels = [0.2, 0.6, 1.2, 2.0, 3.0];
  const w = view.w, h = view.h;
  const step = 10;
  ctx.save();
  ctx.globalAlpha = 0.85;
  ctx.lineWidth = 1;

  for (let li=0; li<levels.length; li++){
    const L = levels[li];
    // color gradient-ish by alpha only
    ctx.strokeStyle = "#6aa2d8";
    ctx.globalAlpha = 0.16 + 0.08*li;
    ctx.beginPath();
    let started = false;
    for (let px=0; px<w; px+=step){
      for (let py=0; py<h; py+=step){
        // inverse screen->world
        const xw = (px - view.cx)/view.scalePx;
        const yw = -(py - view.cy)/view.scalePx;
        const q = a*xw*xw + 2*b*xw*yw + d*yw*yw;

        // near level?
        if (Math.abs(q - L) < 0.04){
          if (!started){
            ctx.moveTo(px,py);
            started = true;
          } else {
            ctx.lineTo(px,py);
          }
        }
      }
    }
    if (started) ctx.stroke();
  }
  ctx.restore();

  // Show elimination: for each x, minimize over y => y*(x) = -(b/d)x (if d!=0)
  if (Math.abs(d) > EPS){
    const pts = [];
    for (let xw=-2.2; xw<=2.2; xw+=0.02){
      const ystar = -(b/d)*xw;
      pts.push([xw, ystar]);
    }
    drawPolyline(view, pts, "#ffd166", 0.95, 3); // minimizer line
  }

  // Animate a moving x and show y*(x) plus q_min = s x^2
  const xw = 2.0*Math.cos(2*Math.PI*t);
  let yw = 0;
  if (Math.abs(d) > EPS) yw = -(b/d)*xw;
  const qmin = (Math.abs(d) > EPS) ? (s * xw*xw) : NaN;

  drawPoint(view, [xw, yw], "#ffd166", 5, 1);
  drawArrow(view, [xw, 0], [xw, yw], "#ffd166", 0.8, 2);

  // PSD hint
  const psd = (d > 0 && isFinite(s) && s >= -1e-12);

  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.92;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`Schur mode: q(x,y)=a x² + 2 b x y + d y²`, 18, 22);
  ctx.fillText(`complete square: q = d (y + (b/d)x)² + (a - b²/d) x²`, 18, 40);
  ctx.fillText(`Schur s = a - b²/d = ${fmt(s)}  | d=${fmt(d)}  | PSD needs d>0 and s≥0`, 18, 58);
  ctx.fillText(`moving point is y*(x)=-(b/d)x, giving q_min(x)= s x² = ${fmt(qmin)}`, 18, 76);
  ctx.fillStyle = psd ? "#06d6a0" : "#ff6b6b";
  ctx.fillText(psd ? "PSD-like: contours are ellipses around 0" : "Not PSD: there exists a direction with q<0", 18, 94);
  ctx.restore();
}

/* ============================
   Main animation loop
   ============================ */
let last = performance.now();
function tick(now){
  const dt = Math.min(0.05, (now-last)/1000);
  last = now;

  const sp = parseFloat(dom.speed.value)/100; // 0..1
  const omega = 0.10 + 0.90*sp; // base speed

  if (playing){
    phase = (phase + omega*dt) % 1;
  } else if (stepOnce){
    phase = (phase + 0.02) % 1;
    stepOnce = false;
  }

  clear();
  const view = makeView();
  const A = currentA();

  if (mode==="eigen"){
    drawEigen(view, A, phase);
  } else if (mode==="svd"){
    drawSVD(view, A, phase);
  } else {
    drawSchur(view, A, phase);
  }

  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
</script>
</body>
</html>
```

If you want the “next-next” layer in code, the cleanest upgrade is a **3×3 version** (true 3D) with a WebGL-ish projection so you can literally watch an ellipsoid in 3D and see eigenvectors as principal axes. The math is the same; the visualization gets way more intuitive.

## Response:
Thought for 32s

Here’s **Batch 2**: a single self-contained HTML file (no libraries) with **4 new animated demos**:

1.  **Kernel + Column Space + Least Squares Projection** (uses SVD/pseudoinverse under the hood)
2.  **Gram–Schmidt (basis → orthonormal basis)** (animated “subtract projection” step)
3.  **Power Iteration** (see convergence to the dominant eigenvector for symmetric 2×2)
4.  **Rank-1 SVD Approximation (Eckart–Young intuition)** (circle→ellipse under  $A$  vs best rank-1)

Save as `linear_algebra_animations_batch2.html` and open in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Linear Algebra Animations — Batch 2</title>
  <style>
    :root { color-scheme: dark; }
    body { margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; background:#0b0f14; color:#d8e1ea; }
    .wrap { display:grid; grid-template-columns: 420px 1fr; gap: 12px; height:100vh; }
    .panel { padding:14px; border-right: 1px solid #17212b; overflow:auto; }
    .panel h1 { font-size:16px; margin:0 0 8px 0; }
    .panel h2 { font-size:13px; margin:14px 0 8px 0; color:#b7c7d8; }
    .row { display:flex; gap:10px; align-items:center; margin: 8px 0; }
    .row label { width:56px; color:#b7c7d8; font-size:12px; }
    input[type="range"] { width: 100%; }
    input[type="number"] { width:84px; background:#0f1620; border:1px solid #223244; color:#d8e1ea; padding:6px; border-radius:8px; }
    .seg { display:flex; gap:8px; flex-wrap:wrap; margin: 10px 0; }
    .btn {
      background:#0f1620; border:1px solid #223244; color:#d8e1ea;
      padding:8px 10px; border-radius:10px; cursor:pointer; user-select:none;
      font-size:12px;
    }
    .btn:hover { border-color:#3a5872; }
    .btn.active { background:#142233; border-color:#6aa2d8; }
    .note { font-size:12px; color:#b7c7d8; line-height:1.35; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; white-space: pre-wrap; }
    canvas { width:100%; height:100%; display:block; background: radial-gradient(1200px 700px at 60% 40%, #0f1620 0%, #0b0f14 55%, #070a0e 100%); }
    .small { font-size:11px; color:#9fb0c2; }
    .divider { margin: 10px 0; height:1px; background:#17212b; }
  </style>
</head>
<body>
<div class="wrap">
  <div class="panel">
    <h1>Linear Algebra Animations — Batch 2</h1>
    <div class="note">
      Four new visual machines: kernel/column space + projection, Gram–Schmidt, power iteration, and best rank-1 SVD approximation.
      Everything runs locally in one HTML file.
    </div>

    <h2>Mode</h2>
    <div class="seg">
      <div id="mKernel" class="btn active">Kernel + Projection</div>
      <div id="mGS" class="btn">Gram–Schmidt</div>
      <div id="mPower" class="btn">Power Iteration</div>
      <div id="mRank1" class="btn">Rank-1 SVD</div>
    </div>

    <h2>Playback</h2>
    <div class="seg">
      <div id="btnPlay" class="btn active">Play</div>
      <div id="btnStep" class="btn">Step</div>
      <div id="btnReset" class="btn">Reset</div>
    </div>
    <div class="row">
      <label>Speed</label>
      <input id="speed" type="range" min="0" max="100" value="45"/>
    </div>

    <div class="divider"></div>

    <h2>Parameters</h2>
    <div class="small">Matrix sliders are reused across modes. Some modes use symmetric \(A\).</div>

    <div id="rowA" class="row">
      <label>a</label>
      <input id="a" type="range" min="-3" max="3" step="0.01" value="1.2"/>
      <input id="aN" type="number" step="0.01" value="1.2"/>
    </div>
    <div id="rowB" class="row">
      <label>b</label>
      <input id="b" type="range" min="-3" max="3" step="0.01" value="0.9"/>
      <input id="bN" type="number" step="0.01" value="0.9"/>
    </div>
    <div id="rowC" class="row">
      <label>c</label>
      <input id="c" type="range" min="-3" max="3" step="0.01" value="-0.6"/>
      <input id="cN" type="number" step="0.01" value="-0.6"/>
    </div>
    <div id="rowD" class="row">
      <label>d</label>
      <input id="d" type="range" min="-3" max="3" step="0.01" value="1.0"/>
      <input id="dN" type="number" step="0.01" value="1.0"/>
    </div>

    <div id="gsControls" style="display:none;">
      <div class="divider"></div>
      <h2>Gram–Schmidt vectors</h2>
      <div class="row">
        <label>u₁</label>
        <input id="u1" type="range" min="-2" max="2" step="0.01" value="1.3"/>
        <input id="u1N" type="number" step="0.01" value="1.3"/>
      </div>
      <div class="row">
        <label>u₂</label>
        <input id="u2" type="range" min="-2" max="2" step="0.01" value="0.4"/>
        <input id="u2N" type="number" step="0.01" value="0.4"/>
      </div>
      <div class="row">
        <label>v₁</label>
        <input id="v1" type="range" min="-2" max="2" step="0.01" value="0.6"/>
        <input id="v1N" type="number" step="0.01" value="0.6"/>
      </div>
      <div class="row">
        <label>v₂</label>
        <input id="v2" type="range" min="-2" max="2" step="0.01" value="1.1"/>
        <input id="v2N" type="number" step="0.01" value="1.1"/>
      </div>
    </div>

    <h2>Readout</h2>
    <div id="readout" class="note mono"></div>

    <div class="divider"></div>
    <div class="small">
      Tips:
      <br/>• Kernel mode: make \(A\) rank-1 by setting rows proportional (e.g. c≈(a)*k and d≈(b)*k), then the nullspace line appears.
      <br/>• Power iteration: works best for symmetric \(A\) with \(|λ₁| &gt; |λ₂|\).
      <br/>• Rank-1: watch σ₂ and the error shrink when \(A\) is nearly rank-1.
    </div>
  </div>

  <div style="position:relative;">
    <canvas id="cv"></canvas>
  </div>
</div>

<script>
/* ============================
   Small linear algebra helpers
   ============================ */
const EPS = 1e-10;

function mat2(a,b,c,d){ return {a,b,c,d}; }              // [[a,b],[c,d]]
function mat2T(M){ return mat2(M.a, M.c, M.b, M.d); }    // transpose
function mat2Mul(A,B){
  return mat2(
    A.a*B.a + A.b*B.c,  A.a*B.b + A.b*B.d,
    A.c*B.a + A.d*B.c,  A.c*B.b + A.d*B.d
  );
}
function mat2Vec(M,x,y){ return [M.a*x + M.b*y, M.c*x + M.d*y]; }

function dot(u,v){ return u[0]*v[0] + u[1]*v[1]; }
function norm(v){ return Math.hypot(v[0], v[1]); }
function add(u,v){ return [u[0]+v[0], u[1]+v[1]]; }
function sub(u,v){ return [u[0]-v[0], u[1]-v[1]]; }
function scale(v,s){ return [v[0]*s, v[1]*s]; }
function ortho(v){ return [-v[1], v[0]]; }
function normalize(v){
  const n = norm(v);
  if (n < EPS) return [1,0];
  return [v[0]/n, v[1]/n];
}
function clamp(x,lo,hi){ return Math.max(lo, Math.min(hi, x)); }
function fmt(x){
  if (!isFinite(x)) return "NaN";
  const s = x.toFixed(4);
  return s.replace(/\.?0+$/,'');
}

/* Eigen for symmetric 2x2 [[a,b],[b,d]] */
function eigSym2(a,b,d){
  const t = 0.5*(a+d);
  const delta = 0.5*(a-d);
  const s = Math.sqrt(delta*delta + b*b);
  const l1 = t + s;
  const l2 = t - s;

  function eigvec(lambda){
    let v = [b, lambda - a];
    if (norm(v) < EPS) v = [lambda - d, b];
    if (norm(v) < EPS) v = [1,0];
    return normalize(v);
  }
  const v1 = eigvec(l1);
  const v2 = normalize(ortho(v1));
  return { l1, l2, v1, v2 };
}

/* SVD for 2x2 via eigen of A^T A */
function svd2(A){
  const AT = mat2T(A);
  const G = mat2Mul(AT, A); // symmetric PSD
  const g11 = G.a, g12 = G.b, g22 = G.d;
  const { l1, l2, v1, v2 } = eigSym2(g11, g12, g22);

  let s1 = Math.sqrt(Math.max(0, l1));
  let s2 = Math.sqrt(Math.max(0, l2));

  let V1=v1, V2=v2;
  if (s2 > s1 + 1e-12){
    [s1,s2] = [s2,s1];
    [V1,V2] = [V2,V1];
  }

  let U1, U2;
  if (s1 > EPS){
    const Av1 = mat2Vec(A, V1[0], V1[1]);
    U1 = normalize(scale(Av1, 1/s1));
  } else {
    U1 = [1,0];
  }

  if (s2 > EPS){
    const Av2 = mat2Vec(A, V2[0], V2[1]);
    U2 = normalize(scale(Av2, 1/s2));
    // orthonormalize
    const proj = dot(U2,U1);
    U2 = normalize(sub(U2, scale(U1, proj)));
  } else {
    U2 = normalize(ortho(U1));
  }

  const U = mat2(U1[0], U2[0], U1[1], U2[1]);    // cols u1,u2
  const V = mat2(V1[0], V2[0], V1[1], V2[1]);    // cols v1,v2
  const VT = mat2T(V);
  const Sigma = mat2(s1,0,0,s2);

  return { U, Sigma, V, VT, s1, s2, u1:U1, u2:U2, v1:V1, v2:V2 };
}

/* pseudoinverse from SVD: A^+ = V Σ^+ U^T */
function pinv2(A){
  const { U, V, s1, s2 } = svd2(A);
  const UT = mat2T(U);
  const Vmat = V;

  const inv1 = (s1 > 1e-8) ? 1/s1 : 0;
  const inv2 = (s2 > 1e-8) ? 1/s2 : 0;
  const SigPlus = mat2(inv1,0,0,inv2);

  // A+ = V * Σ+ * U^T
  return mat2Mul(mat2Mul(Vmat, SigPlus), UT);
}

/* ============================
   Canvas + drawing
   ============================ */
const canvas = document.getElementById('cv');
const ctx = canvas.getContext('2d');

function resize(){
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.floor(canvas.clientWidth * dpr);
  canvas.height = Math.floor(canvas.clientHeight * dpr);
  ctx.setTransform(dpr,0,0,dpr,0,0);
}
window.addEventListener('resize', resize);
resize();

function clear(){
  ctx.clearRect(0,0,canvas.clientWidth, canvas.clientHeight);
}

function makeView(cx, cy, scalePx){
  return { w: canvas.clientWidth, h: canvas.clientHeight, cx, cy, scalePx };
}
function toScreen(view, p){
  return [view.cx + view.scalePx*p[0], view.cy - view.scalePx*p[1]];
}
function drawGrid(view){
  ctx.save();
  ctx.globalAlpha = 0.10;
  ctx.strokeStyle = "#9fb0c2";
  ctx.lineWidth = 1;
  const step = view.scalePx/2;
  for(let x = view.cx % step; x < view.w; x += step){
    ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,view.h); ctx.stroke();
  }
  for(let y = view.cy % step; y < view.h; y += step){
    ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(view.w,y); ctx.stroke();
  }
  ctx.restore();
}
function drawAxes(view){
  ctx.save();
  ctx.globalAlpha = 0.35;
  ctx.strokeStyle = "#9fb0c2";
  ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(0, view.cy); ctx.lineTo(view.w, view.cy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(view.cx, 0); ctx.lineTo(view.cx, view.h); ctx.stroke();
  ctx.restore();
}
function drawArrow(view, from, to, color="#d8e1ea", alpha=1, lw=2){
  const a = toScreen(view, from);
  const b = toScreen(view, to);
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = lw;
  ctx.beginPath();
  ctx.moveTo(a[0], a[1]);
  ctx.lineTo(b[0], b[1]);
  ctx.stroke();
  const dx = b[0]-a[0], dy = b[1]-a[1];
  const L = Math.hypot(dx,dy);
  if (L > 1e-6){
    const ux = dx/L, uy = dy/L;
    const size = 10;
    const left = [b[0] - size*(ux*0.9 - uy*0.4), b[1] - size*(uy*0.9 + ux*0.4)];
    const right= [b[0] - size*(ux*0.9 + uy*0.4), b[1] - size*(uy*0.9 - ux*0.4)];
    ctx.beginPath();
    ctx.moveTo(b[0], b[1]);
    ctx.lineTo(left[0], left[1]);
    ctx.lineTo(right[0], right[1]);
    ctx.closePath();
    ctx.fill();
  }
  ctx.restore();
}
function drawPoint(view, p, color="#d8e1ea", r=4, alpha=1){
  const s = toScreen(view, p);
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(s[0], s[1], r, 0, Math.PI*2);
  ctx.fill();
  ctx.restore();
}
function drawLineThroughOrigin(view, dir, color, alpha=0.9, lw=2){
  const v = normalize(dir);
  const L = 3.0;
  drawArrow(view, [0,0], scale(v,  L), color, alpha, lw);
  drawArrow(view, [0,0], scale(v, -L), color, alpha, lw);
}
function drawPolyline(view, pts, stroke="#d8e1ea", alpha=1, lw=2, closed=true){
  if (!pts.length) return;
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = stroke;
  ctx.lineWidth = lw;
  ctx.beginPath();
  const p0 = toScreen(view, pts[0]);
  ctx.moveTo(p0[0], p0[1]);
  for(let i=1;i<pts.length;i++){
    const p = toScreen(view, pts[i]);
    ctx.lineTo(p[0], p[1]);
  }
  if (closed) ctx.closePath();
  ctx.stroke();
  ctx.restore();
}

function circlePoints(N=240){
  const pts = [];
  for(let i=0;i<N;i++){
    const t = (i/N)*Math.PI*2;
    pts.push([Math.cos(t), Math.sin(t)]);
  }
  return pts;
}
const UNIT = circlePoints();

/* ============================
   UI state
   ============================ */
let mode = "kernel"; // kernel | gs | power | rank1
let playing = true;
let phase = 0;
let stepOnce = false;

/* power iteration internal */
let powerX = normalize([0.7, 0.2]);
let powerTrail = [];
let powerAccum = 0;
let powerStepCount = 0;

/* ============================
   DOM wiring
   ============================ */
const dom = {
  cv: canvas,
  a: document.getElementById('a'), aN: document.getElementById('aN'),
  b: document.getElementById('b'), bN: document.getElementById('bN'),
  c: document.getElementById('c'), cN: document.getElementById('cN'),
  d: document.getElementById('d'), dN: document.getElementById('dN'),
  speed: document.getElementById('speed'),
  readout: document.getElementById('readout'),
  gsControls: document.getElementById('gsControls'),
  mKernel: document.getElementById('mKernel'),
  mGS: document.getElementById('mGS'),
  mPower: document.getElementById('mPower'),
  mRank1: document.getElementById('mRank1'),
  btnPlay: document.getElementById('btnPlay'),
  btnStep: document.getElementById('btnStep'),
  btnReset: document.getElementById('btnReset'),

  u1: document.getElementById('u1'), u1N: document.getElementById('u1N'),
  u2: document.getElementById('u2'), u2N: document.getElementById('u2N'),
  v1: document.getElementById('v1'), v1N: document.getElementById('v1N'),
  v2: document.getElementById('v2'), v2N: document.getElementById('v2N'),
};

function linkSlider(sl, num, onChange){
  const syncFromSlider = () => { num.value = sl.value; onChange?.(); };
  const syncFromNum = () => {
    const v = clamp(parseFloat(num.value), parseFloat(sl.min), parseFloat(sl.max));
    sl.value = v; num.value = v; onChange?.();
  };
  sl.addEventListener('input', syncFromSlider);
  num.addEventListener('change', syncFromNum);
}
function updateReadout(){ /* filled later */ }

linkSlider(dom.a, dom.aN, updateReadout);
linkSlider(dom.b, dom.bN, updateReadout);
linkSlider(dom.c, dom.cN, updateReadout);
linkSlider(dom.d, dom.dN, updateReadout);
linkSlider(dom.u1, dom.u1N, updateReadout);
linkSlider(dom.u2, dom.u2N, updateReadout);
linkSlider(dom.v1, dom.v1N, updateReadout);
linkSlider(dom.v2, dom.v2N, updateReadout);

function setMode(m){
  mode = m;
  dom.mKernel.classList.toggle('active', m==="kernel");
  dom.mGS.classList.toggle('active', m==="gs");
  dom.mPower.classList.toggle('active', m==="power");
  dom.mRank1.classList.toggle('active', m==="rank1");
  dom.gsControls.style.display = (m==="gs") ? "block" : "none";
  // c slider only meaningful for general matrix modes:
  // kernel + rank1 use general A; power uses symmetric; gs ignores A.
  document.getElementById('rowC').style.display = (m==="power") ? "none" : "flex";

  resetState();
  updateReadout();
}
dom.mKernel.onclick = () => setMode("kernel");
dom.mGS.onclick = () => setMode("gs");
dom.mPower.onclick = () => setMode("power");
dom.mRank1.onclick = () => setMode("rank1");

dom.btnPlay.onclick = () => {
  playing = !playing;
  dom.btnPlay.classList.toggle('active', playing);
  dom.btnPlay.textContent = playing ? "Play" : "Paused";
};
dom.btnStep.onclick = () => { stepOnce = true; };
dom.btnReset.onclick = () => { resetState(); };

function currentA(){
  const a = parseFloat(dom.a.value);
  const b = parseFloat(dom.b.value);
  const c = parseFloat(dom.c.value);
  const d = parseFloat(dom.d.value);
  if (mode==="power"){
    return mat2(a,b,b,d); // symmetric
  }
  return mat2(a,b,c,d);   // general
}
function gsVectors(){
  const u = [parseFloat(dom.u1.value), parseFloat(dom.u2.value)];
  const v = [parseFloat(dom.v1.value), parseFloat(dom.v2.value)];
  return {u, v};
}

function resetState(){
  phase = 0;
  // power iteration reset
  powerX = normalize([Math.random()*2-1, Math.random()*2-1]);
  powerTrail = [powerX];
  powerAccum = 0;
  powerStepCount = 0;
}

/* ============================
   Readout text
   ============================ */
function updateReadout(){
  if (mode==="kernel"){
    const A = currentA();
    const { s1, s2, u1, v1, v2 } = svd2(A);
    const rank = (s1>1e-8) + (s2>1e-8);
    const nDir = (s2 <= 1e-8) ? v2 : null; // nullspace direction when rank<2
    dom.readout.textContent =
      `Kernel + Projection mode\n` +
      `A = [[${fmt(A.a)}, ${fmt(A.b)}],[${fmt(A.c)}, ${fmt(A.d)}]]\n` +
      `σ1=${fmt(s1)}, σ2=${fmt(s2)}  (rank≈${rank})\n` +
      (nDir ? `null direction (≈ker A): v₂=(${fmt(nDir[0])}, ${fmt(nDir[1])})\n` : `null direction: none (full rank)\n`) +
      `Projection: p = AA⁺ b is orthogonal projection of b onto Col(A).\n` +
      `Least squares: x* = A⁺ b minimizes ||Ax - b||.`;
  } else if (mode==="gs"){
    const {u,v} = gsVectors();
    const q1 = normalize(u);
    const proj = dot(q1, v);
    const vperp = sub(v, scale(q1, proj));
    const vperpN = norm(vperp);
    const q2 = (vperpN > 1e-8) ? normalize(vperp) : normalize(ortho(q1));
    dom.readout.textContent =
      `Gram–Schmidt mode\n` +
      `u=(${fmt(u[0])}, ${fmt(u[1])}), v=(${fmt(v[0])}, ${fmt(v[1])})\n` +
      `q1 = u/||u|| = (${fmt(q1[0])}, ${fmt(q1[1])})\n` +
      `proj_{q1}(v) = (q1ᵀv) q1,  q1ᵀv = ${fmt(proj)}\n` +
      `v⊥ = v - proj = (${fmt(vperp[0])}, ${fmt(vperp[1])})\n` +
      `q2 = v⊥/||v⊥|| = (${fmt(q2[0])}, ${fmt(q2[1])})`;
  } else if (mode==="power"){
    const A = currentA();
    const { l1, l2, v1 } = eigSym2(A.a, A.b, A.d);
    dom.readout.textContent =
      `Power Iteration mode (symmetric A)\n` +
      `A = [[${fmt(A.a)}, ${fmt(A.b)}],[${fmt(A.b)}, ${fmt(A.d)}]]\n` +
      `eigs: λ1=${fmt(l1)}, λ2=${fmt(l2)}\n` +
      `dominant eigenvector direction v1≈(${fmt(v1[0])}, ${fmt(v1[1])})\n` +
      `iter: x_{k+1} = A x_k / ||A x_k||   (k=${powerStepCount})`;
  } else {
    const A = currentA();
    const { s1, s2, u1, v1 } = svd2(A);
    // best rank-1 approximation A1 = σ1 u1 v1^T
    const A1 = mat2(
      s1*u1[0]*v1[0], s1*u1[0]*v1[1],
      s1*u1[1]*v1[0], s1*u1[1]*v1[1]
    );
    // Frobenius error for 2x2: ||A-A1||_F
    const E = mat2(A.a-A1.a, A.b-A1.b, A.c-A1.c, A.d-A1.d);
    const fro = Math.sqrt(E.a*E.a + E.b*E.b + E.c*E.c + E.d*E.d);
    dom.readout.textContent =
      `Rank-1 SVD mode\n` +
      `A = [[${fmt(A.a)}, ${fmt(A.b)}],[${fmt(A.c)}, ${fmt(A.d)}]]\n` +
      `σ1=${fmt(s1)}, σ2=${fmt(s2)}\n` +
      `best rank-1: A1 = σ1 u1 v1ᵀ\n` +
      `||A - A1||_F ≈ ${fmt(fro)}  (for 2×2, equals σ2 up to norm conventions when A is rank-2)`;
  }
}

/* ============================
   Mode renderers
   ============================ */

function drawTitle(txt){
  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.92;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(txt, 18, 22);
  ctx.restore();
}

function drawKernelProjection(A, t){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const scalePx = Math.min(w,h)*0.22;

  // Two side-by-side coordinate systems
  const left  = makeView(0.30*w, 0.55*h, scalePx);
  const right = makeView(0.73*w, 0.55*h, scalePx);

  drawGrid(left); drawGrid(right);
  drawAxes(left); drawAxes(right);

  // Separator line
  ctx.save();
  ctx.strokeStyle = "#17212b";
  ctx.globalAlpha = 0.9;
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(0.515*w, 0);
  ctx.lineTo(0.515*w, h);
  ctx.stroke();
  ctx.restore();

  // rotating x in domain
  const ang = 2*Math.PI*t;
  const x = [Math.cos(ang), Math.sin(ang)];
  const Ax = mat2Vec(A, x[0], x[1]);

  // b in codomain (a moving target)
  const b = [1.2*Math.cos(2*Math.PI*(t+0.17)), 1.2*Math.sin(2*Math.PI*(t+0.17))];

  // pseudoinverse projection
  const Aplus = pinv2(A);
  const xStar = mat2Vec(Aplus, b[0], b[1]);      // x* = A+ b (min-norm LS)
  const p = mat2Vec(A, xStar[0], xStar[1]);      // p = A x* = AA+ b
  const r = sub(b, p);

  const { s1, s2, u1, u2, v1, v2 } = svd2(A);
  const rank = (s1>1e-8) + (s2>1e-8);
  const hasNull = (rank < 2);

  // Domain: show nullspace line if exists (v2)
  if (hasNull){
    drawLineThroughOrigin(left, v2, "#ffd166", 0.95, 2.5);
  }

  // Codomain: show column space line if rank=1 (u1)
  if (rank === 1){
    drawLineThroughOrigin(right, u1, "#06d6a0", 0.85, 2.5);
  }

  // Draw x and Ax
  drawArrow(left, [0,0], x, "#f1fa8c", 0.95, 2.5);
  drawPoint(left, x, "#f1fa8c", 4.5, 1);

  drawArrow(right, [0,0], Ax, "#ff6b6b", 0.9, 2.5);
  drawPoint(right, Ax, "#ff6b6b", 4.5, 1);

  // Draw b, projection p, and residual r = b-p
  drawArrow(right, [0,0], b, "#9fb0c2", 0.75, 2.2);
  drawPoint(right, b, "#9fb0c2", 4.2, 1);

  drawArrow(right, [0,0], p, "#6aa2d8", 0.95, 2.8);
  drawPoint(right, p, "#6aa2d8", 4.8, 1);

  drawArrow(right, p, b, "#ff6b6b", 0.65, 2.0); // residual
  drawPoint(right, add(p, scale(r, 0.5)), "#ff6b6b", 3.5, 0.5);

  // Show x* in domain
  drawArrow(left, [0,0], xStar, "#6aa2d8", 0.95, 2.8);
  drawPoint(left, xStar, "#6aa2d8", 4.8, 1);

  // Labels
  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.9;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`Domain (x)`, 18, 44);
  ctx.fillText(`Codomain (Ax)`, 0.56*w, 44);
  ctx.fillText(`x (yellow) → Ax (red)`, 18, 62);
  ctx.fillText(`b (gray), p=proj(b) (blue), r=b-p (red)`, 0.56*w, 62);
  ctx.fillText(`σ1=${fmt(s1)} σ2=${fmt(s2)} rank≈${rank}`, 18, 80);
  if (hasNull) ctx.fillText(`ker(A) shown as yellow line (≈ v₂)`, 18, 98);
  if (rank===1) ctx.fillText(`Col(A) shown as green line (≈ u₁)`, 0.56*w, 98);
  ctx.restore();
}

function drawGramSchmidt(t){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const view = makeView(0.52*w, 0.55*h, Math.min(w,h)*0.24);
  drawGrid(view); drawAxes(view);

  const {u,v} = gsVectors();

  const q1 = normalize(u);
  const alpha = dot(q1, v);
  const proj = scale(q1, alpha);
  const vperp = sub(v, proj);

  // Animate the subtraction v -> vperp
  // v(t) = v - s*proj where s goes 0..1 in part of the cycle
  const s = 0.5 - 0.5*Math.cos(2*Math.PI*t); // smooth 0..1..0
  const vAnim = sub(v, scale(proj, s));

  const vperpN = norm(vperp);
  const q2 = (vperpN > 1e-8) ? normalize(vperp) : normalize(ortho(q1));

  // Draw original vectors u, v
  drawArrow(view, [0,0], u, "#f1fa8c", 0.85, 2.5);
  drawArrow(view, [0,0], v, "#9fb0c2", 0.65, 2.5);

  // Draw proj component and the animated subtraction
  drawArrow(view, [0,0], proj, "#6aa2d8", 0.9, 2.5);
  drawArrow(view, [0,0], vAnim, "#ffd166", 0.95, 3.0);

  // Draw orthonormal basis directions q1, q2 as lines
  drawLineThroughOrigin(view, q1, "#f1fa8c", 0.55, 2.0);
  drawLineThroughOrigin(view, q2, "#06d6a0", 0.55, 2.0);

  // Draw vperp final (when s=1)
  drawArrow(view, [0,0], vperp, "#06d6a0", 0.65, 2.5);

  drawTitle("Gram–Schmidt: v⊥ = v − proj_{q1}(v), then q2 = v⊥/||v⊥||");
}

function stepPowerIteration(A){
  const y = mat2Vec(A, powerX[0], powerX[1]);
  const yn = norm(y);
  if (yn < EPS){
    powerX = normalize([Math.random()*2-1, Math.random()*2-1]);
  } else {
    powerX = scale(y, 1/yn);
  }
  powerTrail.push(powerX);
  if (powerTrail.length > 60) powerTrail.shift();
  powerStepCount += 1;
}

function drawPowerIteration(A, dt, t){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const view = makeView(0.52*w, 0.55*h, Math.min(w,h)*0.24);
  drawGrid(view); drawAxes(view);

  const { l1, l2, v1, v2 } = eigSym2(A.a, A.b, A.d);

  // Step the iteration periodically based on speed
  const sp = parseFloat(dom.speed.value)/100;
  const stepsPerSec = 1.0 + 6.0*sp; // 1..7 steps/sec
  powerAccum += dt;
  while (powerAccum >= 1/stepsPerSec){
    powerAccum -= 1/stepsPerSec;
    stepPowerIteration(A);
  }

  // Draw eigenvectors
  drawLineThroughOrigin(view, v1, "#ffd166", 0.9, 2.5);
  drawLineThroughOrigin(view, v2, "#06d6a0", 0.55, 2.0);

  // Draw trail of iterates
  for (let i=0;i<powerTrail.length;i++){
    const alpha = (i+1)/powerTrail.length;
    drawArrow(view, [0,0], scale(powerTrail[i], 1.6), "#6aa2d8", 0.12 + 0.65*alpha, 2);
  }

  // Current iterate
  drawArrow(view, [0,0], scale(powerX, 1.8), "#ff6b6b", 0.95, 3.0);
  drawPoint(view, scale(powerX, 1.8), "#ff6b6b", 4.5, 1);

  // Convergence hint
  const ratio = (Math.abs(l1) > EPS) ? (Math.abs(l2)/Math.abs(l1)) : NaN;

  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.92;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`Power iteration: x_{k+1} = A x_k / ||A x_k||`, 18, 22);
  ctx.fillText(`λ1=${fmt(l1)} λ2=${fmt(l2)}  | |λ2/λ1|≈${fmt(ratio)}`, 18, 40);
  ctx.fillText(`Yellow line = dominant eigenvector direction`, 18, 58);
  ctx.restore();
}

function drawRank1SVD(A, t){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  const view = makeView(0.52*w, 0.55*h, Math.min(w,h)*0.24);
  drawGrid(view); drawAxes(view);

  const { s1, s2, u1, v1 } = svd2(A);

  // Best rank-1 matrix A1 = σ1 u1 v1^T
  const A1 = mat2(
    s1*u1[0]*v1[0], s1*u1[0]*v1[1],
    s1*u1[1]*v1[0], s1*u1[1]*v1[1]
  );

  // Animate blend between A1 and A
  const s = 0.5 - 0.5*Math.cos(2*Math.PI*t); // 0..1..0
  const M = mat2(
    (1-s)*A1.a + s*A.a, (1-s)*A1.b + s*A.b,
    (1-s)*A1.c + s*A.c, (1-s)*A1.d + s*A.d
  );

  // Draw images of the unit circle
  const ellA  = UNIT.map(p => mat2Vec(A,  p[0], p[1]));
  const ellA1 = UNIT.map(p => mat2Vec(A1, p[0], p[1]));
  const ellM  = UNIT.map(p => mat2Vec(M,  p[0], p[1]));

  drawPolyline(view, UNIT, "#9fb0c2", 0.25, 2.0, true);
  drawPolyline(view, ellA,  "#6aa2d8", 0.35, 2.2, true);
  drawPolyline(view, ellA1, "#06d6a0", 0.45, 2.2, true);
  drawPolyline(view, ellM,  "#ffd166", 0.95, 3.0, true);

  // Track one vector
  const ang = 2*Math.PI*t;
  const x = [Math.cos(ang), Math.sin(ang)];
  const yA = mat2Vec(A,  x[0], x[1]);
  const y1 = mat2Vec(A1, x[0], x[1]);
  const yM = mat2Vec(M,  x[0], x[1]);

  drawArrow(view, [0,0], x,  "#f1fa8c", 0.8, 2.0);
  drawArrow(view, [0,0], yM, "#ffd166", 0.95, 3.0);
  drawPoint(view, yM, "#ffd166", 4.8, 1);

  ctx.save();
  ctx.fillStyle = "#d8e1ea";
  ctx.globalAlpha = 0.92;
  ctx.font = "12px ui-monospace, Menlo, Consolas, monospace";
  ctx.fillText(`Rank-1 SVD: A1 = σ1 u1 v1ᵀ`, 18, 22);
  ctx.fillText(`σ1=${fmt(s1)} σ2=${fmt(s2)}  (σ2 is the “leftover” rank-2 part)`, 18, 40);
  ctx.fillText(`Green ellipse: A1(circle)  | Blue ellipse: A(circle)  | Yellow: blend`, 18, 58);
  ctx.restore();
}

/* ============================
   Animation loop
   ============================ */
updateReadout();
let last = performance.now();

function tick(now){
  const dt = Math.min(0.05, (now-last)/1000);
  last = now;

  const sp = parseFloat(dom.speed.value)/100;
  const omega = 0.10 + 0.90*sp;

  if (playing){
    phase = (phase + omega*dt) % 1;
  } else if (stepOnce){
    phase = (phase + 0.02) % 1;
    stepOnce = false;
  }

  clear();

  const A = currentA();

  if (mode==="kernel"){
    drawKernelProjection(A, phase);
  } else if (mode==="gs"){
    drawGramSchmidt(phase);
  } else if (mode==="power"){
    drawPowerIteration(A, dt, phase);
  } else {
    drawRank1SVD(A, phase);
  }

  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);

/* Make sure mode starts consistent with UI */
setMode("kernel");
</script>
</body>
</html>
```

If you want Batch 3, the most satisfying next set is **true 3D**: (i) 3D ellipsoid principal axes (eigenvectors), (ii) SVD as “two rotations + scaling” in 3D, (iii) Schur complement as PSD of a 3×3 block with an interactive slider that literally shows the feasible region in parameter space.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)