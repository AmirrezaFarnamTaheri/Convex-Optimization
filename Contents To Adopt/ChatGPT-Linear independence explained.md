
# Linear independence explained

4.1 — Linear independence as “no redundancy” (the exact idea, not the vibe)
---------------------------------------------------------------------------

You already know the _constructor atom_ of linear algebra is a **linear combination**:

$$
\alpha_1 v_1+\cdots+\alpha_k v_k.
$$

Linear independence is the rule that says: “none of these vectors is secretly unnecessary.”

We’ll build it from first principles, then extract all the equivalent tests you’ll actually use.

* * *

### 1) The definition (the “zero-combination” test)

Let  $V$  be a vector space over a field  $\mathbb F$  (usually  $\mathbb R$  or  $\mathbb C$ ).  
A list of vectors  $v_1,\dots,v_k\in V$  is **linearly independent** if:

$$
\alpha_1 v_1+\cdots+\alpha_k v_k = 0 \quad\Longrightarrow\quad \alpha_1=\cdots=\alpha_k=0.
$$

Interpretation: the only way to combine them and land exactly at the zero vector is the “boring” way: use all-zero coefficients.

If there exists _any_ choice of coefficients not all zero such that

$$
\alpha_1 v_1+\cdots+\alpha_k v_k = 0,
$$

then the vectors are **linearly dependent**.

That’s the whole definition. Everything else is a consequence.

* * *

### 2) Why the zero vector appears (and why that’s not arbitrary)

You might wonder: why do we check whether a combination equals  $0$ ? Why not check whether two different combinations can produce the same vector?

Because those are actually the same question.

Suppose there are two different representations of the same vector  $w$ :

$$
w=\alpha_1 v_1+\cdots+\alpha_k v_k \quad\text{and}\quad w=\beta_1 v_1+\cdots+\beta_k v_k.
$$

Subtract the two equations (allowed because  $V$  is a vector space, so we can add inverses):

$$
0 = (\alpha_1-\beta_1)v_1+\cdots+(\alpha_k-\beta_k)v_k.
$$

So “two different ways to make the same  $w$ ” is equivalent to “a nontrivial way to make  $0$ .”

This is the deeper meaning:  
**Independence is exactly the condition that coordinates (coefficients) are unique once you choose these vectors as building blocks.**

* * *

### 3) “No redundancy” in a strict, checkable form

“Redundancy” means: one vector can be built from the others, so it doesn’t add any new capability.

Here is the precise theorem you will use constantly:

**Theorem (independence ↔ no vector lies in the span of the others).**  
For  $v_1,\dots,v_k$ , the following are equivalent:

1.   $v_1,\dots,v_k$  are linearly independent.
2.  For every  $j$ ,  $v_j \notin \operatorname{span}(v_1,\dots,v_{j-1},v_{j+1},\dots,v_k)$ .
3.  There is **no** equation of the form
    $$
    v_j = \sum_{i\neq j} c_i v_i \quad\text{for any } j.
    $$

**Proof (every step, no magic):**

*   (1 ⇒ 2) Assume independent. Suppose toward contradiction that for some  $j$ ,
    $$
    v_j = \sum_{i\neq j} c_i v_i.
    $$
    Move everything to one side (subtract  $v_j$ ):
    $$
    0 = \sum_{i\neq j} c_i v_i - 1\cdot v_j = \sum_{i=1}^k \alpha_i v_i
    $$
    where  $\alpha_j=-1$  and  $\alpha_i=c_i$  for  $i\neq j$ .  
    This is a linear combination equaling  $0$  with  $\alpha_j=-1\neq 0$ , so not all  $\alpha_i$  are zero.  
    That contradicts independence. Hence no such representation exists:  $v_j$  is not in the span of the others.
*   (2 ⇒ 1) Assume (2). Suppose
    $$
    \alpha_1 v_1+\cdots+\alpha_k v_k=0.
    $$
    If all  $\alpha_i=0$ , we’re done. If not, pick an index  $j$  with  $\alpha_j\neq 0$ .  
    Then isolate  $v_j$ . First move the other terms to the other side:
    $$
    \alpha_j v_j = -\sum_{i\neq j} \alpha_i v_i.
    $$
    Now divide by  $\alpha_j$  (this is exactly where “field” matters: nonzero scalars have inverses):
    $$
    v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
    $$
    This expresses  $v_j$  as a linear combination of the other vectors, meaning  $v_j\in \text{span}(\text{others})$ , contradicting (2).  
    Therefore the assumption “not all  $\alpha_i$  are zero” is impossible, so all  $\alpha_i$  must be zero. Independence holds.

So “independent” really does mean “no redundancy” in the literal algebraic sense.

* * *

### 4) Immediate consequences (tiny facts you should be able to prove instantly)

**(A) Any set containing the zero vector is dependent.**  
If  $v_1=0$ , then

$$
1\cdot v_1 + 0\cdot v_2+\cdots+0\cdot v_k = 0
$$

is a nontrivial zero-combination (coefficient  $1\neq 0$ ). So dependent.

**(B) If two vectors are equal (or one is a scalar multiple of the other), the set is dependent.**  
If  $v_2 = \lambda v_1$ , then

$$
\lambda v_1 - 1\cdot v_2 = 0
$$

is nontrivial, so dependent.

**(C) Any subset of an independent set is independent.**  
Reason: if a smaller subset had a nontrivial combination giving  $0$ , you could extend it by adding zeros for the missing coefficients and get a nontrivial combination of the whole set giving  $0$ , contradicting independence.

**(D) Adding vectors can only destroy independence, not create it.**  
If  $S$  is dependent, any superset is dependent (because the same dependence relation still exists).

* * *

### 5) Geometry in  $\mathbb R^2$  and  $\mathbb R^3$  (intuition that matches the algebra)

In  $\mathbb R^2$ :

*   Two vectors  $v_1,v_2$  are independent **iff** they are not collinear (not on the same line through the origin).
*   Dependent means  $v_2=\lambda v_1$  for some scalar  $\lambda$ . That’s exactly “same direction (or opposite), different length.”

In  $\mathbb R^3$ :

*   Two nonzero vectors are independent iff they’re not collinear.
*   Three vectors  $v_1,v_2,v_3$  are independent iff they do **not** lie in the same plane through the origin.  
    Dependent means one of them is a linear combination of the other two, so all three live in the span of two vectors, i.e. a plane through  $0$ .

Important subtlety: this “line/plane through the origin” is not an aesthetic choice. Linear combinations always force the origin to be included (because you can choose all coefficients  $0$ ), so spans are always subspaces, hence contain  $0$ .

* * *

### 6) The matrix viewpoint (how independence becomes an algorithm)

Put the vectors as columns of a matrix:

$$
A = [v_1\ \ v_2\ \ \cdots\ \ v_k].
$$

Then a linear combination is exactly a matrix-vector product:

$$
A\alpha = \alpha_1 v_1+\cdots+\alpha_k v_k, \quad \text{where } \alpha = (\alpha_1,\dots,\alpha_k)^T.
$$

So the independence definition becomes:

$$
v_1,\dots,v_k \text{ independent} \quad\Longleftrightarrow\quad A\alpha=0 \Rightarrow \alpha=0.
$$

That is: the homogeneous system  $A\alpha=0$  has only the trivial solution.

Now the algorithmic punchline:

*   Row-reduce  $A$  (Gaussian elimination).
*   If every column is a pivot column (equivalently: there are  $k$  pivots), then the null space is  $\{0\}$ , so columns are independent.
*   If there is any free variable, there are nontrivial solutions to  $A\alpha=0$ , hence dependence.

This is why independence is not just a definition—it’s computable.

* * *

### 7) Common failure modes and edge cases (where people silently mess up)

1.  **Confusing “independent” with “orthogonal.”**  
    Orthogonal vectors are independent (if nonzero), but independence does not require right angles. Independence is about uniqueness of representation, not angles.
2.  **Mixing up points and vectors.**  
    Independence is defined for vectors (elements of a vector space).  
    A set of points in the plane doesn’t have “linear independence” unless you first convert them into displacement vectors from a chosen origin.
3.  **Forgetting the field matters.**  
    The step “divide by  $\alpha_j$ ” uses that  $\alpha_j\neq 0$  has an inverse. That’s why vector spaces are over fields, not just rings, in the standard theory.
4.  **Assuming “more vectors = more independent.”**  
    Independence is fragile. In  $\mathbb R^n$ , you can’t have more than  $n$  independent vectors (you’ll prove this later using dimension / rank-nullity / elimination).

* * *

### 8) Micro-examples (so your brain stops treating it as a slogan)

**Example 1 ( $\mathbb R^2$ ).**  
 $v_1=(1,0)$ ,  $v_2=(2,0)$ .  
Check dependence:

$$
2v_1 - 1v_2 = (2,0)-(2,0)=(0,0).
$$

Nontrivial → dependent.

**Example 2 ( $\mathbb R^2$ ).**  
 $v_1=(1,0)$ ,  $v_2=(0,1)$ .  
Suppose  $\alpha_1 v_1+\alpha_2 v_2=0$ :

$$
(\alpha_1,\alpha_2)=(0,0)\Rightarrow \alpha_1=\alpha_2=0.
$$

Independent.

**Example 3 (matrix test).**  
Columns  $v_1=(1,1)$ ,  $v_2=(2,2)$  in  $\mathbb R^2$ :

$$
A=\begin{bmatrix}1&2\\1&2\end{bmatrix}.
$$

Row-reduce:

$$
\begin{bmatrix}1&2\\1&2\end{bmatrix}\to \begin{bmatrix}1&2\\0&0\end{bmatrix}.
$$

Second column not a pivot → dependence.

* * *

### 9) What 4.1 is really buying you (the “why we care”)

You’re about to define a **basis** in 4.2. A basis is “spanning + independent.” The independent half is what guarantees:

*   **coordinates exist uniquely**, not ambiguously;
*   you can do algebra with coordinate vectors without contradictions;
*   “dimension” becomes a meaningful invariant rather than “how many generators you happened to pick.”

So 4.1 is the “no duplicates, no freeloaders” rule that makes the entire coordinate machinery well-defined.

* * *

Next section (4.2) will use independence to build the idea of a basis as a **coordinate system that actually works**, and we’ll prove the uniqueness of coordinates carefully (that’s where independence becomes a weapon).


Alright. We’ll take 4.1 and turn it into something you can rebuild from scratch, prove in multiple equivalent ways, and _use_ without handwaving. I’ll be painfully explicit and I’ll also point out the hidden assumptions your brain usually smuggles in.

* * *

4.1 — Linear independence as “no redundancy” (ultra-deep version)
-----------------------------------------------------------------

### 0) What independence is _actually_ about (the hidden “coordinate uniqueness” story)

When you pick vectors  $v_1,\dots,v_k$ , you’re implicitly proposing them as “building blocks” for other vectors. The foundational question is:

If I build something using these blocks, do I get a **unique recipe**?

“Unique recipe” means: if

$$
w=\sum_{i=1}^k \alpha_i v_i
$$

is one recipe for  $w$ , could there exist a _different_ recipe

$$
w=\sum_{i=1}^k \beta_i v_i
$$

with  $(\alpha_1,\dots,\alpha_k)\neq(\beta_1,\dots,\beta_k)$ ?

Independence is precisely the condition that the answer is **no** (uniqueness holds) for all vectors  $w$  in the span.

But the definition is stated in terms of the **zero vector**. Why? Because “two different recipes for the same  $w$ ” collapses to “a nontrivial recipe for  $0$ ” by subtraction. That’s not a trick; it’s the algebraic core.

We’ll prove this carefully next.

* * *

1) Definition (canonical form)
------------------------------

Let  $V$  be a vector space over a field  $\mathbb F$ . A list (ordered family)  $v_1,\dots,v_k\in V$  is **linearly independent** if:

$$
\alpha_1 v_1+\cdots+\alpha_k v_k = 0 \quad\Longrightarrow\quad \alpha_1=\cdots=\alpha_k=0.
$$

If there exist scalars  $\alpha_i$ , not all zero, such that

$$
\alpha_1 v_1+\cdots+\alpha_k v_k = 0,
$$

then  $v_1,\dots,v_k$  are **linearly dependent**.

Two comments that matter:

1.  “Not all zero” means **at least one** coefficient is nonzero.
2.  “List” matters: we care about the specific collection; repetitions matter; order isn’t important for truth but is convenient.

* * *

2) Why the field assumption matters (where division is used)
------------------------------------------------------------

A vector space is defined over a **field**  $\mathbb F$  (like  $\mathbb R$  or  $\mathbb C$ ) so that every nonzero scalar has a multiplicative inverse.

This matters in a very specific step you will use repeatedly:

If  $\alpha_j \neq 0$ , then we can “solve for”  $v_j$  via division by  $\alpha_j$ :

$$
\alpha_j v_j = u \quad\Rightarrow\quad v_j = \alpha_j^{-1} u.
$$

Independence ↔ redundancy equivalences use this step. Over a ring where division may fail, the story becomes more subtle. In standard linear algebra, we live in fields, so the step is valid.

* * *

3) Independence ↔ uniqueness of representation (fully proved)
-------------------------------------------------------------

This is the “secret meaning” of independence.

### Proposition 1 (independence gives uniqueness)

Assume  $v_1,\dots,v_k$  are linearly independent. Then every vector  $w\in\text{span}(v_1,\dots,v_k)$  has at most one representation as a linear combination of these vectors.

#### Proof

Take a vector  $w$  and suppose there are two representations:

$$
w=\sum_{i=1}^k \alpha_i v_i \quad\text{and}\quad w=\sum_{i=1}^k \beta_i v_i.
$$

Subtract the second equation from the first (use vector space properties: subtraction means add the additive inverse):

$$
0 = w-w = \sum_{i=1}^k \alpha_i v_i - \sum_{i=1}^k \beta_i v_i = \sum_{i=1}^k (\alpha_i-\beta_i) v_i.
$$

Now apply independence: if a linear combination equals  $0$ , all coefficients must be zero:

$$
\alpha_i-\beta_i=0 \ \forall i \quad\Rightarrow\quad \alpha_i=\beta_i \ \forall i.
$$

So the representation is unique. ∎

### Proposition 2 (uniqueness gives independence)

Assume that every vector in  $\text{span}(v_1,\dots,v_k)$  has a unique representation using  $v_1,\dots,v_k$ . Then  $v_1,\dots,v_k$  are linearly independent.

#### Proof

Consider the vector  $w=0$ . It certainly belongs to the span (take all coefficients  $0$ ):

$$
0 = \sum_{i=1}^k 0\cdot v_i.
$$

If there were a nontrivial combination

$$
0 = \sum_{i=1}^k \alpha_i v_i \quad\text{with some }\alpha_j\neq 0,
$$

then  $0$  would have two different representations (the zero-coefficient one and the  $\alpha$ \-one), contradicting uniqueness. Hence no nontrivial combination exists. That is exactly independence. ∎

So:

$$
\boxed{\text{Independent} \iff \text{unique coordinates in its span}.}
$$

That’s “no redundancy” in a very operational sense: redundancy means coordinate ambiguity.

* * *

4) Independence ↔ “no vector is in the span of the others” (fully proved)
-------------------------------------------------------------------------

This is probably the most used equivalence.

### Theorem (redundancy characterization)

For vectors  $v_1,\dots,v_k$ , the following are equivalent:

1.   $v_1,\dots,v_k$  are linearly independent.
2.  For every  $j$ ,  $v_j \notin \text{span}(v_1,\dots,v_{j-1},v_{j+1},\dots,v_k)$ .
3.  There is no equation  $v_j = \sum_{i\neq j} c_i v_i$ .

#### Proof: (1 ⇒ 2)

Assume independent. Suppose contrary that for some  $j$ ,

$$
v_j = \sum_{i\neq j} c_i v_i.
$$

Bring all terms to one side:

$$
0 = \sum_{i\neq j} c_i v_i - 1\cdot v_j = \sum_{i=1}^k \alpha_i v_i
$$

where  $\alpha_j=-1$  and  $\alpha_i=c_i$  for  $i\neq j$ . This is a linear combination equaling  $0$  with  $\alpha_j=-1\neq 0$ , hence nontrivial. That contradicts independence. So (2) holds.

#### Proof: (2 ⇒ 1)

Assume (2). Suppose

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

If all  $\alpha_i=0$ , done. Otherwise pick  $j$  with  $\alpha_j\neq 0$ . Then:

$$
\alpha_j v_j = -\sum_{i\neq j} \alpha_i v_i
$$

and divide by  $\alpha_j$  (field!):

$$
v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
$$

So  $v_j\in\text{span}(\text{others})$ , contradicting (2). Therefore the “otherwise” case cannot happen, so all  $\alpha_i=0$ . Independence holds. ∎

This theorem is literally “no redundancy”: if one vector is already producible from the others, it adds nothing.

* * *

5) Dependence always yields an explicit redundancy (solving for a vector)
-------------------------------------------------------------------------

A dependence relation isn’t just a certificate; it gives you a removable vector.

### Proposition (dependence ⇒ one vector is a linear combination of others)

If  $v_1,\dots,v_k$  are dependent, then there exists an index  $j$  such that

$$
v_j \in \text{span}(v_1,\dots,v_{j-1},v_{j+1},\dots,v_k).
$$

#### Proof

Dependence means there exist scalars  $\alpha_i$ , not all zero, with

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

Pick  $j$  such that  $\alpha_j\neq 0$ . Then:

$$
\alpha_j v_j = -\sum_{i\neq j} \alpha_i v_i \quad\Rightarrow\quad v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
$$

So  $v_j$  is in the span of the others. ∎

Practical meaning: if a set is dependent, you can drop at least one vector without shrinking the span.

* * *

6) “Minimality” viewpoint (independence as minimal spanning)
------------------------------------------------------------

Independence can also be seen as a minimality property.

### Theorem (independent spanning set is minimal)

Suppose  $\{v_1,\dots,v_k\}$  spans some subspace  $W$  (i.e.  $W=\text{span}(v_1,\dots,v_k)$ ).  
Then  $\{v_1,\dots,v_k\}$  is independent **iff** removing any one vector makes it fail to span  $W$ .

#### Proof sketch (but still explicit)

*   (⇒) If independent, then by the “no vector in span of others” theorem, each  $v_j$  is not in the span of the others. So if you remove  $v_j$ , you can no longer generate  $v_j$ , hence you cannot span all of  $W$ .
*   (⇐) If removing any vector destroys spanning, then in particular  $v_j$  cannot be generated by the others. That implies no redundancy, hence independence.

This is another way “no redundancy” shows up: every vector is essential.

* * *

7) Geometry in  $\mathbb R^n$ : what changes and what doesn’t
-------------------------------------------------------------

### 7.1 Two vectors in  $\mathbb R^2$  or  $\mathbb R^3$ 

Two vectors  $v,w$  are dependent iff one is a scalar multiple of the other:

$$
w=\lambda v.
$$

Why? Because dependence for two vectors means:

$$
\alpha v + \beta w = 0
$$

with not both  $\alpha,\beta$  zero. If  $\beta\neq 0$ , solve:

$$
w = -\frac{\alpha}{\beta} v.
$$

If  $\beta=0$ , then  $\alpha v=0$  with  $\alpha\neq 0$ , so  $v=0$ . That’s also scalar multiple behavior. Either way, dependence = collinearity.

So in  $\mathbb R^2$ : independent ↔ not on the same line through the origin.  
In  $\mathbb R^3$ : same statement for pairs.

### 7.2 Three vectors in  $\mathbb R^3$ 

Three vectors are dependent iff they lie in a plane through the origin (one is a linear combination of the other two). This is exactly the span-of-others criterion.

### 7.3 What _doesn’t_ generalize well

“Angles” don’t define independence. You can have independent vectors that are extremely close to each other (almost collinear) but not exactly multiples. Numerically this matters later (conditioning), but logically they are still independent.

Independence is an exact algebraic property, not a “how different they look” property.

* * *

8) Matrix formulation: independence as “trivial nullspace”
----------------------------------------------------------

This is the computational form.

Put the vectors as columns:

$$
A = [v_1\ v_2\ \cdots\ v_k]\in\mathbb F^{n\times k}.
$$

Then for a coefficient vector  $\alpha\in\mathbb F^k$ ,

$$
A\alpha = \sum_{i=1}^k \alpha_i v_i.
$$

So:

$$
v_1,\dots,v_k\ \text{independent} \iff A\alpha=0 \Rightarrow \alpha=0 \iff \text{Null}(A)=\{0\}.
$$

### 8.1 Row reduction interpretation (why elimination answers independence)

Row reduction corresponds to left-multiplication by an invertible matrix  $E$ :

$$
EA \sim A.
$$

If  $E$  is invertible, then

$$
A\alpha=0 \iff EA\alpha = 0
$$

because multiplying by  $E$  doesn’t change whether a vector equals zero (invertibility means one-to-one).

Therefore, row operations preserve the solution set of  $A\alpha=0$ . So we can row-reduce to see whether there exist nonzero solutions.

### 8.2 Pivot columns criterion (column independence)

For  $A\in\mathbb F^{n\times k}$ , columns are independent iff the reduced echelon form has a pivot in every column (equivalently rank  $=k$ ).

If  $k>n$ , you cannot have pivots in every column because there can be at most  $n$  pivots. This is the earliest glimpse of “you can’t have more than  $n$  independent vectors in  $\mathbb F^n$ .”

We’ll later formalize this with dimension, but the elimination intuition is already telling you.

* * *

9) Dependence relations as “certificates” and how to _extract_ redundancy
-------------------------------------------------------------------------

If vectors are dependent, there exists  $\alpha\neq 0$  with  $A\alpha=0$ . Any such  $\alpha$  is a **dependence certificate**.

From it, you can identify redundancy:

*   pick an index  $j$  with  $\alpha_j\neq 0$ ,
*   solve for  $v_j$  as a combination of the rest:
    $$
    v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
    $$

This procedure is not just theoretical; it’s exactly what happens when you row-reduce and express pivot variables in terms of free variables.

* * *

10) Edge cases and common conceptual traps (with sharp fixes)
-------------------------------------------------------------

### Trap 1: “Independent” vs “distinct”

Vectors can be distinct but dependent (e.g.  $(1,1)$  and  $(2,2)$ ). Distinctness is irrelevant. Dependence is about linear combination.

### Trap 2: confusing points with vectors

Independence lives in a vector space, which always contains a zero vector and supports scaling. A set of points in the plane isn’t automatically a vector space.  
If you want to talk about “independent points,” what you actually do is convert them to displacement vectors relative to some base point.

### Trap 3: “orthogonal implies independent” but not conversely

If  $v_i\neq 0$  and they’re pairwise orthogonal under an inner product, then they’re independent. Proof is easy:

$$
\sum \alpha_i v_i=0 \Rightarrow \langle v_j,\sum \alpha_i v_i\rangle = \alpha_j \langle v_j,v_j\rangle=0 \Rightarrow \alpha_j=0.
$$

But independence doesn’t require orthogonality.

### Trap 4: “almost dependent”

In exact math, there is no “almost independent”: either a dependence relation exists or it doesn’t.  
In computation, near-dependence creates numerical instability. Later you’ll meet this as “ill-conditioning” and small singular values in SVD.

### Trap 5: forgetting the field

Over  $\mathbb C$ , scalars are complex; “multiple” means complex multiple; “collinear” is still “scalar multiple,” but geometric intuition needs care because complex scaling rotates too.

* * *

11) A very concrete checklist for 4.1 fluency
---------------------------------------------

You’re not “done” with 4.1 until you can do all of this quickly and correctly:

1.  Given a dependence equation, explicitly solve for a redundant vector.
2.  Given a set, immediately spot trivial dependence: includes  $0$ , repeats, obvious multiples.
3.  Convert “two representations of  $w$ ” into a dependence relation for  $0$ .
4.  Use elimination on  $A=[v_1\cdots v_k]$  to decide independence.
5.  Explain independence in words in three equivalent ways:
    *   only trivial zero combination,
    *   unique representation in span,
    *   no vector lies in span of others.

* * *

12) Micro-examples, but with the _full_ logic spelled out
---------------------------------------------------------

### Example A: dependence from a nontrivial zero combination

Let  $v_1=(1,2)$ ,  $v_2=(2,4)$  in  $\mathbb R^2$ .  
Compute:

$$
2v_1 - v_2 = 2(1,2)-(2,4)=(2,4)-(2,4)=(0,0).
$$

Coefficients  $(2,-1)$  are not all zero, so dependent.  
Redundancy extraction:

$$
2v_1 - v_2 = 0 \Rightarrow v_2=2v_1.
$$

So  $v_2$  adds nothing.

### Example B: independence via uniqueness

Let  $v_1=(1,0)$ ,  $v_2=(0,1)$ . Suppose

$$
\alpha_1 v_1+\alpha_2 v_2 = 0.
$$

Then

$$
(\alpha_1,\alpha_2)=(0,0)
$$

so both coefficients must be zero. Therefore independent.  
So any vector  $(x,y)$  has a _unique_ representation:

$$
(x,y)=x(1,0)+y(0,1).
$$

### Example C: matrix test

Vectors  $v_1=(1,1,0)$ ,  $v_2=(0,1,1)$ ,  $v_3=(1,2,1)$  in  $\mathbb R^3$ .  
Form matrix with columns:

$$
A=\begin{bmatrix} 1&0&1\\ 1&1&2\\ 0&1&1 \end{bmatrix}.
$$

Notice  $v_3=v_1+v_2$  because:

$$
(1,1,0)+(0,1,1)=(1,2,1).
$$

So dependent immediately (and we extracted redundancy without elimination). The dependence certificate is:

$$
1\cdot v_1+1\cdot v_2-1\cdot v_3=0.
$$

* * *

13) One more level deeper: independence as injectivity of a linear map
----------------------------------------------------------------------

This viewpoint becomes insanely useful later.

Define a linear map  $T:\mathbb F^k\to V$  by:

$$
T(\alpha_1,\dots,\alpha_k)=\sum_{i=1}^k \alpha_i v_i.
$$

Then:

$$
v_1,\dots,v_k\ \text{independent} \iff T(\alpha)=0 \Rightarrow \alpha=0 \iff \ker(T)=\{0\} \iff T\ \text{is injective (one-to-one).}
$$

So “independence” means: the coordinate-to-vector map doesn’t collapse two different coordinate vectors into the same vector.

This is a conceptual bridge to:

*   rank–nullity,
*   dimension,
*   basis as an isomorphism  $\mathbb F^n \cong V$ .

* * *

14) What 4.1 sets up for 4.2 (basis) in a precise sentence
----------------------------------------------------------

A **basis** will be exactly a set of vectors such that the map  $T:\mathbb F^n\to V$  above is not only injective (independence) but also surjective (spanning).  
Injective + surjective = bijective, which is why coordinates exist and are unique for _every_ vector in  $V$ .

That’s the real structural point: independence is the “injective half” of coordinates.

* * *

If you keep this level of understanding, 4.2 becomes almost inevitable rather than “a new definition.”


4.2 — Basis: a coordinate system that actually works (from first principles, no shortcuts)
------------------------------------------------------------------------------------------

Section 4.1 gave you the **injective half** of coordinates: independence means “no collisions,” no ambiguity.  
Section 4.2 completes the picture by adding **surjectivity**: every vector can actually be reached.

A **basis** is where linear algebra stops being abstract sets and becomes a _working coordinate system_.

We will build this slowly, rigorously, and from multiple equivalent angles, because this concept silently underlies almost everything that follows: dimension, matrices, rank, eigenvectors, SVD, least squares, all of it.

* * *

1) Why we even need the concept of a basis
------------------------------------------

Suppose you have vectors  $v_1,\dots,v_k\in V$ .

Two questions matter:

1.  **Existence:** Can _every_ vector  $v\in V$  be written as a linear combination of these vectors?
2.  **Uniqueness:** If it can, is that representation unique?

From earlier sections:

*   Existence alone = **spanning**
*   Uniqueness alone = **independence**

A basis is when **both hold simultaneously**.

That is not cosmetic. That is the exact condition under which “coordinates” make sense.

* * *

2) Definition (precise, minimal, non-negotiable)
------------------------------------------------

Let  $V$  be a vector space over a field  $\mathbb F$ .

A set (or ordered list) of vectors

$$
B=\{b_1,\dots,b_n\}\subset V
$$

is a **basis** of  $V$  if:

1.  (**Spanning**) Every  $v\in V$  can be written as
    $$
    v=\sum_{i=1}^n c_i b_i \quad\text{for some scalars } c_i\in\mathbb F.
    $$
2.  (**Independence**) The vectors  $b_1,\dots,b_n$  are linearly independent.

Nothing else. No geometry. No coordinates yet. Just these two properties.

* * *

3) The fundamental theorem: existence + uniqueness of coordinates
-----------------------------------------------------------------

This is the _central theorem_ of linear algebra at the structural level.

### Theorem (Basis Theorem)

If  $B=\{b_1,\dots,b_n\}$  is a basis of  $V$ , then **every vector  $v\in V$  can be written in exactly one way** as

$$
v=\sum_{i=1}^n c_i b_i.
$$

That is: existence **and** uniqueness.

Let’s prove both halves explicitly.

* * *

### Proof — existence (comes from spanning)

Because  $B$  spans  $V$ , by definition:

$$
\forall v\in V,\ \exists (c_1,\dots,c_n)\in\mathbb F^n \quad\text{s.t.}\quad v=\sum_{i=1}^n c_i b_i.
$$

Nothing to prove here beyond unfolding the definition.

* * *

### Proof — uniqueness (this is where independence is used)

Suppose

$$
v=\sum_{i=1}^n c_i b_i \quad\text{and}\quad v=\sum_{i=1}^n d_i b_i
$$

are two representations of the same vector.

Subtract:

$$
0 = v-v = \sum_{i=1}^n (c_i-d_i)b_i.
$$

Since the  $b_i$  are linearly independent, the only linear combination that gives zero is the trivial one. Therefore:

$$
c_i-d_i=0 \quad\forall i \quad\Rightarrow\quad c_i=d_i \quad\forall i.
$$

So the representation is unique.

∎

This is the moment where linear algebra becomes _coordinatizable_.

* * *

4) Coordinates are not vectors — they are descriptions of vectors
-----------------------------------------------------------------

Once a basis  $B=\{b_1,\dots,b_n\}$  is fixed, every vector  $v\in V$  determines a **coordinate vector**:

$$
[v]_B := (c_1,\dots,c_n)\in\mathbb F^n \quad\text{such that}\quad v=\sum_{i=1}^n c_i b_i.
$$

Crucial conceptual separation:

*    $v$  lives in the abstract vector space  $V$ .
*    $[v]_B$  lives in the coordinate space  $\mathbb F^n$ .

They are **not the same object**, even if numerically they sometimes look identical (as in  $\mathbb R^n$  with the standard basis).

Changing the basis changes the coordinate vector, but **not** the underlying vector.

* * *

5) Basis as a bijection between abstract vectors and coordinates
----------------------------------------------------------------

Define the linear map

$$
T_B:\mathbb F^n \to V, \qquad T_B(c_1,\dots,c_n)=\sum_{i=1}^n c_i b_i.
$$

Then:

*   Spanning ⇔  $T_B$  is **surjective**
*   Independence ⇔  $T_B$  is **injective**

So:

$$
B\ \text{is a basis} \iff T_B\ \text{is bijective}.
$$

This is _huge_ conceptually.

It means:

$$
V \cong \mathbb F^n
$$

as vector spaces, once a basis is chosen.

Every finite-dimensional vector space is “just  $\mathbb F^n$  in disguise,” but the disguise matters.

* * *

6) Minimal and maximal characterizations of a basis
---------------------------------------------------

A basis can be defined in **four equivalent ways**. You must be fluent with all of them.

### Theorem (Equivalent definitions of a basis)

For a finite set  $B\subset V$ , the following are equivalent:

1.   $B$  is a basis (spanning + independent).
2.   $B$  is a **minimal spanning set** (removing any vector breaks spanning).
3.   $B$  is a **maximal independent set** (adding any vector breaks independence).
4.  Every  $v\in V$  has a **unique** representation as a linear combination of vectors in  $B$ .

#### Why this matters

Different problems give you different handles:

*   Sometimes you’re given a spanning set and asked to trim it.
*   Sometimes you’re given independent vectors and asked to extend them.
*   Sometimes uniqueness is the easiest thing to test conceptually.

All of these are secretly the same condition.

* * *

7) How bases appear in  $\mathbb R^n$ : the standard example
------------------------------------------------------------

In  $\mathbb R^n$ , define the standard basis:

$$
e_1=(1,0,\dots,0),\; e_2=(0,1,0,\dots,0),\; \dots,\; e_n=(0,\dots,0,1).
$$

Claim:  $\{e_1,\dots,e_n\}$  is a basis of  $\mathbb R^n$ .

### Proof

*   **Spanning:** Any vector  $(x_1,\dots,x_n)$  satisfies
    $$
    (x_1,\dots,x_n)=\sum_{i=1}^n x_i e_i.
    $$
*   **Independence:**
    $$
    \sum_{i=1}^n \alpha_i e_i=(0,\dots,0) \Rightarrow \alpha_i=0\ \forall i.
    $$

So it’s a basis.

This basis is _not_ special mathematically. It’s special psychologically because coordinates are obvious.

* * *

8) Nonstandard bases: same space, different coordinates
-------------------------------------------------------

Consider in  $\mathbb R^2$ :

$$
b_1=(1,1),\quad b_2=(1,-1).
$$

These vectors are independent and span  $\mathbb R^2$ , so they form a basis.

Now take  $v=(2,0)$ .

Solve:

$$
(2,0)=c_1(1,1)+c_2(1,-1).
$$

This gives the system:

$$
\begin{cases} c_1+c_2=2\\ c_1-c_2=0 \end{cases} \Rightarrow c_1=1,\; c_2=1.
$$

So:

$$
[v]_B=(1,1).
$$

Same vector. Different coordinates. Nothing mystical happened.

* * *

9) Why uniqueness would fail without independence
-------------------------------------------------

Suppose you try to “use” a spanning but dependent set as a coordinate system.

Example in  $\mathbb R^2$ :

$$
v_1=(1,0),\quad v_2=(0,1),\quad v_3=(1,1).
$$

This set spans  $\mathbb R^2$ , but it’s dependent.

Now the vector  $(1,1)$  has infinitely many representations:

$$
(1,1)=1v_3 =1v_1+1v_2 =2v_3-1v_1-1v_2 =\cdots
$$

Coordinates are meaningless here. This is why independence is not optional.

* * *

10) Why spanning would fail without completeness
------------------------------------------------

If you use an independent but non-spanning set, some vectors are unreachable.

Example in  $\mathbb R^3$ :

$$
v_1=(1,0,0),\quad v_2=(0,1,0).
$$

Independent, but they only span the  $xy$ \-plane.  
Vectors like  $(0,0,1)$  have no coordinates in this “basis.”

So independence alone is also not enough.

* * *

11) Algorithmic viewpoint: basis via Gaussian elimination
---------------------------------------------------------

Given vectors  $v_1,\dots,v_k\in\mathbb R^n$ :

1.  Form the matrix  $A=[v_1\ \cdots\ v_k]$ .
2.  Row-reduce  $A$ .
3.  Pivot columns form a basis for the column space.
4.  The number of pivots is the size of the basis.

This gives you:

*   a basis,
*   automatically independent,
*   automatically spanning the same subspace.

This is how basis-finding is done in practice.

* * *

12) Basis is not unique — dimension will be
-------------------------------------------

Different bases can exist for the same space:

*   standard basis,
*   rotated basis,
*   skewed basis,
*   eigenvector basis (when it exists),
*   orthonormal basis.

But the **number** of basis vectors will turn out to be invariant. That invariant is called **dimension** (Section 4.3).

Basis = choice  
Dimension = structure

* * *

13) What 4.2 secretly accomplished
----------------------------------

You now have:

*   A precise meaning of “coordinates”
*   A proof that coordinates are **unique**
*   A bijection between abstract vectors and  $\mathbb F^n$ 
*   The justification for treating vectors as column arrays _after_ a basis is fixed

Everything that follows — matrices, rank, nullity, eigenvectors, SVD — assumes this machinery silently.

* * *

### Where we’re going next (4.3 preview, conceptually)

Section 4.3 will prove the shocking fact that **every basis of a vector space has the same number of elements**, even though the bases themselves can look wildly different.

That number is the _true_ measure of degrees of freedom: **dimension**.

And it is one of the deepest structural invariants in linear algebra.


4.3 — Dimension: degrees of freedom, made precise (the invariant behind everything)
-----------------------------------------------------------------------------------

Up to now, a **basis** is a _choice_.  
Dimension will be a _fact_.

Section 4.3 answers one of the most important structural questions in mathematics:

> If a vector space has many different bases, why do they all have the **same number** of vectors?

That number is not an accident. It is the intrinsic “number of degrees of freedom” of the space.

We will build this from the ground up, prove it rigorously, and show why it controls everything from solvability to rank–nullity.

* * *

1) What dimension is trying to measure (before definitions)
-----------------------------------------------------------

Intuitively, dimension answers:

*   How many independent directions does this space have?
*   How many numbers do I need to specify a vector uniquely?
*   How many degrees of freedom survive linear constraints?

But intuition is cheap. We need a definition that does **not** depend on coordinates, geometry, or a particular basis.

* * *

2) Definition (dimension via bases)
-----------------------------------

Let  $V$  be a vector space over a field  $\mathbb F$ .

If  $V$  has a finite basis  $B=\{b_1,\dots,b_n\}$ , then the **dimension** of  $V$ , denoted  $\dim(V)$ , is defined to be:

$$
\dim(V) := n.
$$

This definition only makes sense if the following is true:

> Any two bases of  $V$  have the same number of elements.

This is **not obvious**. It is the main theorem of this section.

* * *

3) The core problem (why this needs a proof)
--------------------------------------------

Suppose:

*    $B=\{b_1,\dots,b_n\}$  is a basis of  $V$ ,
*    $C=\{c_1,\dots,c_m\}$  is another basis of  $V$ .

Why must  $n=m$ ?

Nothing in the definition of a basis obviously prevents one basis from having 3 vectors and another having 5. We must prove this is impossible.

* * *

4) The key technical tool: the Exchange (Steinitz) Lemma
--------------------------------------------------------

Everything rests on one deep but elementary result.

### Lemma (Exchange / Steinitz Lemma)

Let:

*    $S=\{v_1,\dots,v_k\}$  be a **linearly independent** set in  $V$ ,
*    $T=\{w_1,\dots,w_m\}$  be a **spanning** set of  $V$ .

Then:

$$
k \le m.
$$

In words:  
**You cannot have more independent vectors than the size of a spanning set.**

This lemma is the algebraic version of “you can’t squeeze more degrees of freedom into fewer generators.”

* * *

5) Proof of the Exchange Lemma (fully unpacked)
-----------------------------------------------

We prove it carefully, step by step, with no handwaving.

### Step 1: Use spanning to express vectors

Because  $T$  spans  $V$ , every  $v_i$  can be written as a linear combination of the  $w_j$ :

$$
v_i = \sum_{j=1}^m a_{ij} w_j.
$$

This is true for each  $i=1,\dots,k$ .

* * *

### Step 2: Start replacing spanning vectors

We proceed inductively.

*   Since  $v_1\neq 0$ , at least one coefficient in its expansion must be nonzero.
*   Pick some  $w_{j_1}$  with nonzero coefficient.
*   Solve for  $w_{j_1}$  in terms of  $v_1$  and the remaining  $w$ ’s.

This shows:

$$
\text{span}(T) = \text{span}(\{v_1\}\cup (T\setminus\{w_{j_1}\})).
$$

So we can **replace** one spanning vector by  $v_1$  without losing the spanning property.

* * *

### Step 3: Repeat the process

Now apply the same argument to  $v_2$ :

*   Express  $v_2$  in terms of the current spanning set.
*   Independence of  $v_1,v_2$  guarantees that  $v_2$  cannot already lie in the span of  $\{v_1\}$ .
*   So we can replace another  $w$  with  $v_2$ .

Continue this process.

* * *

### Step 4: Count replacements

Each independent vector  $v_i$  replaces **one** vector from  $T$ .

You can do this at most  $m$  times, because  $T$  initially has only  $m$  elements.

Therefore:

$$
k \le m.
$$

∎

This lemma is the engine behind dimension theory.

* * *

6) Main theorem: all bases have the same size
---------------------------------------------

Now we prove the central result.

### Theorem (Dimension Theorem)

Any two bases of a finite-dimensional vector space  $V$  have the same number of elements.

### Proof

Let:

*    $B=\{b_1,\dots,b_n\}$  be a basis,
*    $C=\{c_1,\dots,c_m\}$  be another basis.

Apply the Exchange Lemma twice:

1.   $B$  is independent and  $C$  spans ⇒  $n \le m$ .
2.   $C$  is independent and  $B$  spans ⇒  $m \le n$ .

Therefore:

$$
n = m.
$$

∎

This proves that **dimension is well-defined**.

* * *

7) What dimension really is (structural meaning)
------------------------------------------------

Now that it’s rigorous, let’s interpret.

If  $\dim(V)=n$ , then:

*   Every basis has exactly  $n$  vectors.
*   Every vector in  $V$  requires exactly  $n$  scalars to describe.
*    $V$  is linearly isomorphic to  $\mathbb F^n$ .
*   You cannot find more than  $n$  independent vectors in  $V$ .
*   Any spanning set must have at least  $n$  vectors.

Dimension is not about how vectors “look.”  
It is about **how many independent choices survive linear structure**.

* * *

8) Dimension as injectivity vs surjectivity tension
---------------------------------------------------

Recall the map from Section 4.2:

$$
T_B:\mathbb F^n \to V, \quad (c_1,\dots,c_n)\mapsto \sum c_i b_i.
$$
*   Independence ⇔ injective
*   Spanning ⇔ surjective

The Dimension Theorem says:

> You cannot have injective maps from higher-dimensional spaces into lower-dimensional ones, or surjective maps from lower into higher.

This is the linear algebra version of “degrees of freedom cannot be created or destroyed by linear maps.”

* * *

9) Dimension bounds and consequences
------------------------------------

### (A) Maximum size of independent sets

If  $\dim(V)=n$ , then any independent set has at most  $n$  vectors.

### (B) Minimum size of spanning sets

If  $\dim(V)=n$ , then any spanning set has at least  $n$  vectors.

### (C) Independent + correct size ⇒ basis

Any independent set with  $n$  vectors is automatically a basis.

### (D) Spanning + correct size ⇒ basis

Any spanning set with  $n$  vectors is automatically a basis.

These are not extra facts. They are direct corollaries of the Exchange Lemma.

* * *

10) Computing dimension in practice
-----------------------------------

### Example 1:  $\mathbb R^n$ 

Standard basis has  $n$  vectors ⇒  $\dim(\mathbb R^n)=n$ .

### Example 2: Subspaces of  $\mathbb R^n$ 

Let

$$
W=\{x\in\mathbb R^4 : x_1+x_2+x_3+x_4=0\}.
$$

This is one linear constraint ⇒ one degree of freedom removed ⇒

$$
\dim(W)=3.
$$

Formally: solve the equation, find a basis with 3 vectors.

### Example 3: Column space of a matrix

If  $A\in\mathbb R^{m\times n}$ , then:

$$
\dim(\text{Col}(A)) = \text{rank}(A).
$$

This is not a definition—it’s a theorem you’ll soon prove using exactly the ideas in this section.

* * *

11) Dimension zero and one (edge cases matter)
----------------------------------------------

*    $\dim(V)=0$  ⇔  $V=\{0\}$ .  
    The empty set is the unique basis.
*    $\dim(V)=1$  ⇔ every nonzero vector is a basis.  
    All vectors are scalar multiples of one direction.

These cases force you to respect the definitions; nothing breaks.

* * *

12) Infinite-dimensional spaces (boundary of this section)
----------------------------------------------------------

Some vector spaces do **not** have finite bases:

*   polynomial spaces,
*   function spaces,
*   sequence spaces.

They still have bases (with the axiom of choice), but dimension becomes an infinite cardinal.

For now, everything we do assumes **finite-dimensional** spaces unless stated otherwise.

* * *

13) What 4.3 accomplished structurally
--------------------------------------

You now know:

*   Why “number of basis vectors” is intrinsic
*   Why dimension is invariant under basis change
*   Why independence, spanning, and counting are inseparable
*   Why linear algebra is ultimately about degrees of freedom

This is the last purely structural step before linear maps become unavoidable.

* * *

### Next (5.1 preview, conceptually)

Now that spaces have dimension, the next question is:

> What do **functions** between vector spaces look like when they respect linear structure?

That leads to **linear transformations**, kernels, images, and eventually rank–nullity, which is dimension theory in motion.

If you want, we can go into 5.1 next with the same depth and zero shortcuts.


5.1 — Linear transformations: structure-preserving maps (the true subject of linear algebra)
--------------------------------------------------------------------------------------------

Up to now, we built **static structure**:  
vector spaces, independence, bases, dimension.

From this point on, linear algebra becomes **dynamic**.  
We study _functions_ between vector spaces that respect all that structure.

This section is the hinge of the entire subject.  
Everything later—matrices, rank–nullity, eigenvalues, SVD—is just different ways of understanding these maps.

* * *

1) Why “linear maps” are the real object of study
-------------------------------------------------

Think carefully about what you actually _do_ with vectors:

*   multiply them by matrices,
*   project them,
*   rotate them,
*   differentiate functions,
*   evaluate polynomials,
*   shift coordinate systems,
*   impose linear constraints.

All of these are **functions**  $T: V \to W$ .

Linear algebra is not “about vectors”;  
it is about **vector spaces and the maps between them** that preserve linear structure.

* * *

2) Definition (axiomatic, minimal, exact)
-----------------------------------------

Let  $V,W$  be vector spaces over the same field  $\mathbb F$ .

A function  $T: V \to W$  is a **linear transformation** (or linear map) if it satisfies **both**:

1.  **Additivity**
    $$
    T(u+v) = T(u) + T(v) \quad \forall u,v\in V
    $$
2.  **Homogeneity (compatibility with scalar multiplication)**
    $$
    T(\alpha v) = \alpha T(v) \quad \forall v\in V,\ \forall \alpha\in\mathbb F
    $$

These two axioms are non-negotiable.  
Drop either one and the theory collapses.

* * *

3) Why these axioms are exactly right (no more, no less)
--------------------------------------------------------

### 3.1 Why additivity matters

Additivity ensures that **vector addition means the same thing before and after the map**.

If  $v$  represents a displacement and  $w$  another displacement, then  $v+w$  is “do both.”  
Linearity requires that applying  $T$  before or after combining them gives the same result.

### 3.2 Why homogeneity matters

Homogeneity ensures that **scaling commutes with the map**.

Scaling is part of the vector space structure.  
If  $T$  didn’t respect scaling, coefficients would lose meaning.

### 3.3 Why these two imply everything else

From just these two axioms, many properties follow automatically.

* * *

4) Immediate consequences (proved explicitly)
---------------------------------------------

Let  $T: V \to W$  be linear.

### (A) Zero maps to zero

$$
T(0)=0
$$

**Proof**  
Since  $0 = 0\cdot v$  for any  $v$ ,

$$
T(0) = T(0\cdot v) = 0\cdot T(v) = 0.
$$

∎

This is _forced_. If a function sends  $0$  to something nonzero, it cannot be linear.

* * *

### (B) Negatives are preserved

$$
T(-v) = -T(v)
$$

**Proof**

$$
T(-v)=T((-1)v)=(-1)T(v)=-T(v).
$$

∎

* * *

### (C) Linearity on arbitrary linear combinations

For any finite set  $\{v_i\}$  and scalars  $\{\alpha_i\}$ ,

$$
T\!\left(\sum_{i=1}^k \alpha_i v_i\right) = \sum_{i=1}^k \alpha_i T(v_i).
$$

**Proof**  
This follows by repeated application of additivity and homogeneity.  
Induction on  $k$  makes it fully formal.  
∎

This identity is the _operational heart_ of linear algebra.

* * *

5) The “basis determines everything” principle
----------------------------------------------

This is the first truly powerful theorem.

### Theorem

Let  $B=\{b_1,\dots,b_n\}$  be a basis of  $V$ .  
A linear transformation  $T: V \to W$  is **completely determined** by its values on the basis vectors  $T(b_1),\dots,T(b_n)$ .

### Proof

Take any  $v\in V$ .  
Because  $B$  is a basis, there exist unique scalars  $c_i$  such that:

$$
v=\sum_{i=1}^n c_i b_i.
$$

Apply  $T$ :

$$
T(v)=T\!\left(\sum_{i=1}^n c_i b_i\right) = \sum_{i=1}^n c_i T(b_i).
$$

So once you know  $T(b_i)$ , you know  $T(v)$  for _every_  $v\in V$ .  
∎

This theorem explains why matrices exist at all.

* * *

6) Linearity as “respecting structure”
--------------------------------------

Here’s a deep conceptual reframing:

A linear transformation is exactly a function that preserves:

*   the zero vector,
*   vector addition,
*   scalar multiplication,
*   linear combinations,
*   span,
*   dependence and independence relations.

In short: **everything that makes a vector space a vector space**.

Anything that fails one of these is not linear, even if it looks “almost linear.”

* * *

7) Canonical examples (you must internalize these)
--------------------------------------------------

### Example 1: Matrix multiplication

Let  $A\in\mathbb F^{m\times n}$ .  
Define  $T(x)=Ax$ .

Check linearity:

$$
A(u+v)=Au+Av,\qquad A(\alpha u)=\alpha Au.
$$

This is why matrices represent linear maps.

* * *

### Example 2: Projection

In  $\mathbb R^n$ , define

$$
T(v)=\text{proj}_u(v)=\frac{\langle u,v\rangle}{\langle u,u\rangle}u.
$$

Dot product is linear in  $v$ , scalar multiplication distributes, so projection is linear.

* * *

### Example 3: Differentiation

Let  $V$  be the space of differentiable functions.  
Define  $T(f)=f'$ .

Then:

$$
(f+g)'=f'+g',\qquad (\alpha f)'=\alpha f'.
$$

Differentiation is linear. This is why differential equations live inside linear algebra.

* * *

### Example 4: Evaluation is **not** linear

Let  $T(f)=f(0)+1$ .

Fails:

$$
T(0)=1\neq 0.
$$

One violated axiom kills linearity completely.

* * *

8) Linear vs affine maps (critical distinction)
-----------------------------------------------

A function of the form:

$$
T(v)=Av+b
$$

is **not** linear unless  $b=0$ .

Why?

$$
T(0)=b\neq 0.
$$

Such maps are called **affine**, not linear.  
They preserve straight lines but not the origin.

This distinction will matter enormously when solving  $Ax=b$ .

* * *

9) Linear maps and dimension (first preview)
--------------------------------------------

A linear map can:

*   collapse dimensions (many vectors map to the same output),
*   preserve dimension,
*   but never create new independent directions.

Formally:

$$
\dim(\text{Im}(T)) \le \dim(V).
$$

This will be formalized precisely in **rank–nullity**.

* * *

10) Conceptual summary (what 5.1 actually did)
----------------------------------------------

You now know:

*   What a linear transformation is, _axiomatically_
*   Why those axioms are exactly the right ones
*   Why linear maps are determined by basis images
*   Why matrices are representations, not primary objects
*   Why almost-linear is still not linear

From here on, we stop asking “what is a vector?”  
and start asking “what does this map do to structure?”

* * *

### Next: 5.2 — Kernel and image (null space and range)

In 5.2 we’ll dissect _where information is lost_ and _where it survives_ under a linear map, and we’ll build the machinery needed for rank–nullity.

That’s where linear algebra becomes a theory of constraints and degrees of freedom.


5.2 — Kernel and image: where information dies, where it survives (ultra-deep, structural, no shortcuts)
--------------------------------------------------------------------------------------------------------

Section 5.1 defined **linear transformations** as structure-preserving maps.  
Section 5.2 answers the next unavoidable question:

> When a linear map acts, **what gets erased** and **what survives**?

Those two answers are the **kernel** and the **image**.  
They are not technical side objects. They _are_ the map.

Everything later—rank–nullity, solvability of  $Ax=b$ , invertibility, eigenvectors, least squares—rests on these two subspaces.

* * *

1) Definitions (minimal, exact, non-negotiable)
-----------------------------------------------

Let  $T: V \to W$  be a linear transformation.

### Kernel (null space)

$$
\ker(T) := \{\,v \in V \mid T(v)=0\,\}
$$

Interpretation: **inputs annihilated by the map**.  
These are directions that completely disappear.

* * *

### Image (range)

$$
\operatorname{Im}(T) := \{\,T(v) \mid v \in V\,\} \subseteq W
$$

Interpretation: **outputs that can actually be produced**.  
This is the “reachable” part of the codomain.

* * *

2) First structural fact: both are subspaces (fully proved)
-----------------------------------------------------------

This is not cosmetic. It’s foundational.

* * *

### Proposition 1 —  $\ker(T)$  is a subspace of  $V$ 

**Proof (check the three axioms):**

1.  **Contains zero**  
    From linearity (5.1):
    $$
    T(0)=0 \Rightarrow 0\in\ker(T).
    $$
2.  **Closed under addition**  
    If  $u,v\in\ker(T)$ , then  $T(u)=T(v)=0$ .  
    By additivity:
    $$
    T(u+v)=T(u)+T(v)=0+0=0,
    $$
    so  $u+v\in\ker(T)$ .
3.  **Closed under scalar multiplication**  
    If  $u\in\ker(T)$  and  $\alpha\in\mathbb F$ ,
    $$
    T(\alpha u)=\alpha T(u)=\alpha\cdot 0=0,
    $$
    so  $\alpha u\in\ker(T)$ .

Thus  $\ker(T)$  is a subspace. ∎

* * *

### Proposition 2 —  $\operatorname{Im}(T)$  is a subspace of  $W$ 

**Proof:**

1.  **Contains zero**  
    Since  $T(0)=0$ , we have  $0\in\operatorname{Im}(T)$ .
2.  **Closed under addition**  
    If  $y_1=T(u)$  and  $y_2=T(v)$ ,
    $$
    y_1+y_2=T(u)+T(v)=T(u+v)\in\operatorname{Im}(T).
    $$
3.  **Closed under scalar multiplication**  
    If  $y=T(v)$ ,
    $$
    \alpha y=\alpha T(v)=T(\alpha v)\in\operatorname{Im}(T).
    $$

So  $\operatorname{Im}(T)$  is a subspace of  $W$ . ∎

* * *

3) The meaning of the kernel (information loss)
-----------------------------------------------

The kernel is **exactly** where distinct inputs become indistinguishable.

### Fundamental equivalence

For  $u,v\in V$ ,

$$
T(u)=T(v) \quad\Longleftrightarrow\quad u-v\in\ker(T).
$$

#### Proof

$$
T(u)=T(v) \iff T(u)-T(v)=0 \iff T(u-v)=0 \iff u-v\in\ker(T).
$$

∎

So:

> Two inputs give the same output **iff** their difference lies in the kernel.

This is why the kernel measures **non-injectivity**.

* * *

4) Injectivity ↔ trivial kernel (proved, not asserted)
------------------------------------------------------

### Theorem

A linear map  $T:V\to W$  is **injective** (one-to-one) iff

$$
\ker(T)=\{0\}.
$$

#### Proof

**(⇒)** Assume  $T$  is injective.  
If  $v\in\ker(T)$ , then  $T(v)=0=T(0)$ .  
Injectivity implies  $v=0$ .  
So  $\ker(T)=\{0\}$ .

**(⇐)** Assume  $\ker(T)=\{0\}$ .  
If  $T(u)=T(v)$ , then  $u-v\in\ker(T)$ .  
So  $u-v=0\Rightarrow u=v$ .  
Thus  $T$  is injective.

∎

This is one of the most important equivalences in linear algebra.

* * *

5) The meaning of the image (what survives)
-------------------------------------------

The image tells you **which directions in  $W$ ** the map can actually reach.

*   If  $\operatorname{Im}(T)=W$ , the map is **surjective**.
*   If  $\operatorname{Im}(T)\subsetneq W$ , some outputs are impossible.

This is not about equations yet. It’s pure structure.

* * *

6) Basis-level understanding: kernel and image from generators
--------------------------------------------------------------

Let  $B=\{b_1,\dots,b_n\}$  be a basis of  $V$ .

### Image

$$
\operatorname{Im}(T)=\text{span}\{T(b_1),\dots,T(b_n)\}.
$$

**Why:**  
Every  $v=\sum c_i b_i$ , so

$$
T(v)=\sum c_i T(b_i).
$$

Thus the image is completely determined by the images of basis vectors.

* * *

### Kernel

Kernel consists of all linear combinations

$$
\sum c_i b_i
$$

such that

$$
\sum c_i T(b_i)=0.
$$

So computing the kernel is solving a **homogeneous linear system** in the coefficients  $c_i$ .

This is exactly where Gaussian elimination enters.

* * *

7) Matrix case: the concrete incarnation
----------------------------------------

Let  $A\in\mathbb F^{m\times n}$  and define  $T(x)=Ax$ .

Then:

*    $\ker(T)=\{x\in\mathbb F^n : Ax=0\} = \operatorname{Null}(A)$ 
*    $\operatorname{Im}(T)=\{Ax : x\in\mathbb F^n\} = \operatorname{Col}(A)$ 

So:

| Abstract map | Matrix language |
| --- | --- |
| kernel | null space |
| image | column space |

This is not analogy. It is literal equivalence.

* * *

8) Kernel and image are complementary roles (but not complements)
-----------------------------------------------------------------

Do **not** confuse this:

*   Kernel ⊆ domain  $V$ 
*   Image ⊆ codomain  $W$ 

They live in different spaces and are never “orthogonal complements” by default.

What _is_ true:

*   Kernel measures **collapse**
*   Image measures **survival**

Together, they describe the entire behavior of  $T$ .

* * *

9) Solvability of  $T(v)=w$  (first precise criterion)
------------------------------------------------------

The equation

$$
T(v)=w
$$

has a solution **iff**

$$
w\in\operatorname{Im}(T).
$$

If a solution exists, it is **not unique** unless  $\ker(T)=\{0\}$ .

In fact:

> If  $v_0$  is one solution, then **all** solutions are
> 
> $$
> v_0 + \ker(T).
> $$

That is: an affine translate of the kernel.

This single statement explains the geometry of  $Ax=b$ .

* * *

10) Extreme cases (must be internalized)
----------------------------------------

### Zero map

$$
T(v)=0\quad\forall v
$$
*    $\ker(T)=V$ 
*    $\operatorname{Im}(T)=\{0\}$ 

Everything collapses.

* * *

### Identity map

$$
T(v)=v
$$
*    $\ker(T)=\{0\}$ 
*    $\operatorname{Im}(T)=V$ 

Nothing collapses.

* * *

### Projection

Project  $\mathbb R^3$  onto the  $xy$ \-plane:

*   Kernel =  $z$ \-axis
*   Image =  $xy$ \-plane

Geometrically perfect example of “collapse one direction, preserve two.”

* * *

11) Kernel and image already encode dimension constraints
---------------------------------------------------------

Even before rank–nullity, we can see:

*   Large kernel ⇒ many directions lost
*   Small image ⇒ few directions survive

What you _cannot_ yet quantify is **how many**.  
That counting miracle is the next theorem.

* * *

12) Conceptual summary (what 5.2 actually accomplished)
-------------------------------------------------------

You now understand:

*   Kernel = indistinguishable inputs = information destroyed
*   Image = reachable outputs = information preserved
*   Injectivity ⇔ trivial kernel
*   Surjectivity ⇔ full image
*   Solutions to  $T(v)=w$  live in affine translates of the kernel
*   Every linear map decomposes structure into “lost” and “surviving” directions

This is already enough to explain _why_ linear systems behave the way they do.

* * *

### Next: 5.3 — Rank–Nullity Theorem

5.3 will **count** kernel and image dimensions and prove the deepest conservation law in linear algebra:

$$
\dim(V)=\dim(\ker(T))+\dim(\operatorname{Im}(T)).
$$

That theorem is the algebraic version of “degrees of freedom can move, but never vanish.”

When you’re ready, we continue.


5.3 — Rank–Nullity Theorem: conservation of degrees of freedom (full, rigorous, zero gaps)
------------------------------------------------------------------------------------------

Everything so far has been **structural** but qualitative:

*   kernel = directions killed,
*   image = directions that survive,
*   injective vs surjective.

Now comes the quantitative law that governs _all_ linear maps.

This theorem is not just important.  
It is the **spine** of linear algebra.

* * *

0) What this theorem is really saying (before formulas)
-------------------------------------------------------

A linear map cannot create or destroy degrees of freedom arbitrarily.

Every input direction does **one** of two things:

1.  it **dies** (falls into the kernel), or
2.  it **survives** (contributes to the image).

No direction can do both.  
No direction can escape this accounting.

Rank–nullity is the precise bookkeeping rule.

* * *

1) Definitions (now we name the numbers)
----------------------------------------

Let  $T: V \to W$  be a linear map, with  $V$  finite-dimensional.

### Nullity

$$
\operatorname{nullity}(T) := \dim(\ker(T))
$$

### Rank

$$
\operatorname{rank}(T) := \dim(\operatorname{Im}(T))
$$

These are integers measuring:

*   **nullity** = number of independent directions annihilated,
*   **rank** = number of independent directions preserved.

* * *

2) Statement of the Rank–Nullity Theorem
----------------------------------------

### Theorem (Rank–Nullity)

Let  $T: V \to W$  be a linear transformation with  $V$  finite-dimensional. Then:

$$
\boxed{ \dim(V) = \operatorname{nullity}(T) + \operatorname{rank}(T) }
$$

This is exact. No inequalities. No approximations.

* * *

3) Why this is not obvious (what needs to be proved)
----------------------------------------------------

At first glance, kernel and image live in **different spaces**:

*    $\ker(T) \subseteq V$ ,
*    $\operatorname{Im}(T) \subseteq W$ .

So why should their dimensions add up to  $\dim(V)$ ?

The answer requires a deep but elementary construction:  
we must **split a basis of  $V$ ** into two parts:

*   one part that spans the kernel,
*   one part whose images span the image.

That construction is the proof.

* * *

4) Proof of Rank–Nullity (step-by-step, no shortcuts)
-----------------------------------------------------

Let’s proceed carefully.

* * *

### Step 1: Choose a basis for the kernel

Let:

$$
\{k_1,\dots,k_r\}
$$

be a basis of  $\ker(T)$ .

So:

$$
r = \dim(\ker(T)) = \operatorname{nullity}(T).
$$

These vectors are linearly independent and satisfy:

$$
T(k_i)=0 \quad \forall i.
$$

* * *

### Step 2: Extend this to a basis of the domain

Because  $\ker(T)\subseteq V$ , we can extend this basis to a full basis of  $V$ .

That is, there exist vectors

$$
v_1,\dots,v_s \in V
$$

such that:

$$
\{k_1,\dots,k_r,v_1,\dots,v_s\}
$$

is a basis of  $V$ .

Therefore:

$$
\dim(V)=r+s.
$$

This step uses a fundamental fact from Section 4.3:  
**any independent set can be extended to a basis**.

* * *

### Step 3: Apply  $T$  to the basis vectors

Now apply  $T$  to the basis of  $V$ .

*   For the kernel vectors:
    $$
    T(k_1)=\cdots=T(k_r)=0.
    $$
*   For the remaining vectors:
    $$
    T(v_1),\dots,T(v_s) \in W.
    $$

* * *

### Step 4: Show that  $\{T(v_1),\dots,T(v_s)\}$  spans the image

Take any  $y \in \operatorname{Im}(T)$ .

By definition,  $y=T(x)$  for some  $x\in V$ .

Write  $x$  in the basis of  $V$ :

$$
x = \sum_{i=1}^r a_i k_i + \sum_{j=1}^s b_j v_j.
$$

Apply  $T$ :

$$
T(x) = \sum_{i=1}^r a_i T(k_i) + \sum_{j=1}^s b_j T(v_j) = \sum_{j=1}^s b_j T(v_j).
$$

So every vector in the image is a linear combination of  $T(v_1),\dots,T(v_s)$ .

Hence they **span**  $\operatorname{Im}(T)$ .

* * *

### Step 5: Show that  $\{T(v_1),\dots,T(v_s)\}$  is linearly independent

Suppose:

$$
\sum_{j=1}^s c_j T(v_j) = 0.
$$

Then:

$$
T\!\left(\sum_{j=1}^s c_j v_j\right)=0.
$$

So:

$$
\sum_{j=1}^s c_j v_j \in \ker(T).
$$

But the kernel is spanned by  $k_1,\dots,k_r$ .

So:

$$
\sum_{j=1}^s c_j v_j = \sum_{i=1}^r d_i k_i
$$

for some coefficients  $d_i$ .

Rearrange:

$$
\sum_{i=1}^r (-d_i)k_i + \sum_{j=1}^s c_j v_j = 0.
$$

But recall:

$$
\{k_1,\dots,k_r,v_1,\dots,v_s\}
$$

is a basis of  $V$ , hence linearly independent.

Therefore all coefficients must be zero:

$$
c_j=0 \quad \forall j.
$$

So  $T(v_1),\dots,T(v_s)$  are independent.

* * *

### Step 6: Count dimensions

We have shown:

*    $T(v_1),\dots,T(v_s)$  form a **basis** of  $\operatorname{Im}(T)$ ,
*   so  $\operatorname{rank}(T)=s$ ,
*   and  $\operatorname{nullity}(T)=r$ .

Since  $\dim(V)=r+s$ , we conclude:

$$
\boxed{ \dim(V) = \operatorname{nullity}(T) + \operatorname{rank}(T) }
$$

∎

* * *

5) Interpretation: conservation law
-----------------------------------

Rank–nullity is a **conservation law**:

*   Every input degree of freedom either:
    *   collapses into the kernel, or
    *   contributes to the image.
*   None vanish.
*   None appear from nowhere.

This is why the theorem shows up everywhere.

* * *

6) Matrix version (what you actually compute)
---------------------------------------------

Let  $A \in \mathbb F^{m\times n}$ .

Define  $T(x)=Ax$ .

Then:

*    $\dim(V)=n$ ,
*    $\ker(T)=\operatorname{Null}(A)$ ,
*    $\operatorname{Im}(T)=\operatorname{Col}(A)$ .

So:

$$
\boxed{ n = \dim(\operatorname{Null}(A)) + \operatorname{rank}(A) }
$$

This is the matrix Rank–Nullity Theorem.

* * *

7) Immediate consequences (these are not optional facts)
--------------------------------------------------------

### (A) Injectivity criterion

$$
T \text{ injective} \iff \ker(T)=\{0\} \iff \operatorname{nullity}(T)=0 \iff \operatorname{rank}(T)=\dim(V).
$$

* * *

### (B) Surjectivity criterion

$$
T \text{ surjective} \iff \operatorname{Im}(T)=W \iff \operatorname{rank}(T)=\dim(W).
$$

* * *

### (C) Invertibility (square case)

If  $V=W$  and  $\dim(V)=n$ , then:

$$
T \text{ invertible} \iff \operatorname{rank}(T)=n \iff \ker(T)=\{0\}.
$$

* * *

8) Solving linear systems  $Ax=b$  revisited
--------------------------------------------

Let  $A\in\mathbb R^{m\times n}$ .

*   The system  $Ax=b$  has a solution iff  $b\in\operatorname{Col}(A)$ .
*   If a solution exists:
    *   it is unique iff  $\operatorname{Null}(A)=\{0\}$ ,
    *   otherwise infinitely many solutions exist:
        $$
        x = x_p + \operatorname{Null}(A).
        $$

Rank–nullity tells you **how many free variables** there must be.

* * *

9) Dimension drop is unavoidable
--------------------------------

From rank–nullity:

$$
\operatorname{rank}(T)\le \dim(V).
$$

So:

*   You cannot injectively map a higher-dimensional space into a lower-dimensional one.
*   You cannot surjectively map a lower-dimensional space onto a higher-dimensional one.

This is the algebraic reason geometry behaves the way it does.

* * *

10) One-sentence mastery check
------------------------------

If you truly understand 5.3, you can say—without hesitation:

> “A linear map redistributes the dimension of its domain into kernel and image, and rank–nullity is the exact conservation law governing that redistribution.”

* * *

### What’s next (5.4 preview)

The next step is to specialize rank–nullity to **matrices** and introduce the **four fundamental subspaces**:  
column space, null space, row space, and left null space.

That’s where the abstract theory becomes computational geometry.

When you’re ready, we go to **5.4**.


5.4 — The four fundamental subspaces: the complete anatomy of a matrix
----------------------------------------------------------------------

Rank–nullity told us **how many** degrees of freedom survive or die.  
Section 5.4 tells us **where** they live.

This section is the Rosetta stone between abstract linear maps and concrete matrices.  
Once you truly understand these four subspaces, Gaussian elimination, solvability, least squares, and SVD stop feeling like tricks and start feeling inevitable.

* * *

0) What problem this section solves
-----------------------------------

Given a matrix  $A \in \mathbb F^{m\times n}$ , there are four natural questions:

1.  Which inputs get sent to zero?
2.  Which outputs are achievable?
3.  What linear constraints do the equations impose?
4.  What linear constraints do the equations _fail_ to impose?

Each question corresponds to a **subspace**.  
Together, they exhaust all linear structure associated with  $A$ .

* * *

1) Setup and notation (fix this firmly)
---------------------------------------

Let

$$
A \in \mathbb F^{m\times n}
$$

and define the linear map

$$
T:\mathbb F^n \to \mathbb F^m, \qquad T(x)=Ax.
$$
*   Domain:  $\mathbb F^n$  (inputs, unknowns)
*   Codomain:  $\mathbb F^m$  (outputs, equations)

Everything below is about this single map.

* * *

2) The four fundamental subspaces (definitions first, interpretation second)
----------------------------------------------------------------------------

### (1) Column space —  $\operatorname{Col}(A)$ 

**Definition**

$$
\operatorname{Col}(A) = \{Ax : x\in\mathbb F^n\} \subseteq \mathbb F^m.
$$

Equivalently:

$$
\operatorname{Col}(A) = \text{span of the columns of } A.
$$

**Meaning**

*   All outputs that can actually be produced.
*   The image of the linear map  $T$ .
*   The set of right-hand sides  $b$  for which  $Ax=b$  is solvable.

* * *

### (2) Null space —  $\operatorname{Null}(A)$ 

**Definition**

$$
\operatorname{Null}(A) = \{x\in\mathbb F^n : Ax=0\} \subseteq \mathbb F^n.
$$

**Meaning**

*   Inputs annihilated by the matrix.
*   Directions of non-uniqueness.
*   Degrees of freedom not controlled by the equations.

* * *

### (3) Row space —  $\operatorname{Row}(A)$ 

**Definition**

$$
\operatorname{Row}(A) = \operatorname{Col}(A^T) = \text{span of the rows of } A \subseteq \mathbb F^n.
$$

**Meaning**

*   Linear combinations of equations.
*   All linear constraints actually enforced on  $x$ .
*   The “constraint space” of the system.

* * *

### (4) Left null space —  $\operatorname{Null}(A^T)$ 

**Definition**

$$
\operatorname{Null}(A^T) = \{y\in\mathbb F^m : A^T y = 0\} \subseteq \mathbb F^m.
$$

**Meaning**

*   Linear dependencies among equations.
*   Constraints on  $b$  that must hold for solvability.
*   Directions in output space orthogonal to all columns.

* * *

3) Where each subspace lives (critical distinction)
---------------------------------------------------

| Subspace | Lives in |
| --- | --- |
|  $\operatorname{Null}(A)$  |  $\mathbb F^n$  |
|  $\operatorname{Row}(A)$  |  $\mathbb F^n$  |
|  $\operatorname{Col}(A)$  |  $\mathbb F^m$  |
|  $\operatorname{Null}(A^T)$  |  $\mathbb F^m$  |

This is not bookkeeping trivia.  
It prevents conceptual errors later.

* * *

4) Rank relations (two equalities, one number)
----------------------------------------------

Define:

$$
r := \operatorname{rank}(A).
$$

Then:

*    $\dim(\operatorname{Col}(A)) = r$ 
*    $\dim(\operatorname{Row}(A)) = r$ 
*    $\dim(\operatorname{Null}(A)) = n - r$ 
*    $\dim(\operatorname{Null}(A^T)) = m - r$ 

These four numbers **must** add up correctly:

$$
n = r + (n-r), \qquad m = r + (m-r).
$$

This is rank–nullity applied twice: once to  $A$ , once to  $A^T$ .

* * *

5) Orthogonality relations (the deep geometric structure)
---------------------------------------------------------

Now comes the most important geometric insight.

### Theorem (Fundamental orthogonality)

1.   $\operatorname{Row}(A) = \operatorname{Null}(A)^\perp \subseteq \mathbb F^n$ 
2.   $\operatorname{Col}(A) = \operatorname{Null}(A^T)^\perp \subseteq \mathbb F^m$ 

Let’s unpack this carefully.

* * *

### 5.1 Why rows are orthogonal to the null space

Let  $x\in\operatorname{Null}(A)$ , so  $Ax=0$ .

Write rows of  $A$  as  $r_1,\dots,r_m$ .

Then:

$$
Ax= \begin{bmatrix} r_1 x\\ \vdots\\ r_m x \end{bmatrix} =0 \quad\Rightarrow\quad r_i x = 0 \ \forall i.
$$

So  $x$  is orthogonal to **every row**, hence to their span.

Thus:

$$
\operatorname{Null}(A) \subseteq \operatorname{Row}(A)^\perp.
$$

A dimension count shows equality.

* * *

### 5.2 Why columns are orthogonal to the left null space

Let  $y\in\operatorname{Null}(A^T)$ , so  $A^T y=0$ .

Then for any  $x$ ,

$$
y^T(Ax) = (A^T y)^T x = 0.
$$

So  $y$  is orthogonal to every vector in  $\operatorname{Col}(A)$ .

Hence:

$$
\operatorname{Null}(A^T) = \operatorname{Col}(A)^\perp.
$$

* * *

6) The complete picture (conceptual, not visual)
------------------------------------------------

Each space decomposes cleanly:

### In the domain  $\mathbb F^n$ 

$$
\mathbb F^n = \operatorname{Row}(A) \;\oplus\; \operatorname{Null}(A).
$$
*   Row space = constrained directions
*   Null space = free directions

* * *

### In the codomain  $\mathbb F^m$ 

$$
\mathbb F^m = \operatorname{Col}(A) \;\oplus\; \operatorname{Null}(A^T).
$$
*   Column space = achievable outputs
*   Left null space = impossible components of  $b$ 

This is the **fundamental decomposition** of linear systems.

* * *

7) Gaussian elimination: what it _really_ computes
--------------------------------------------------

Row reduction does **not** change:

*   row space,
*   null space,
*   rank.

But it **does** change:

*   column space (numerically),
*   left null space (numerically).

That’s why:

*   Pivot columns in the _original_ matrix give a basis for  $\operatorname{Col}(A)$ .
*   Nonzero rows in RREF give a basis for  $\operatorname{Row}(A)$ .
*   Free variables parametrize  $\operatorname{Null}(A)$ .
*   Dependencies among rows give  $\operatorname{Null}(A^T)$ .

Row reduction is not magic; it is a coordinate change that exposes these spaces.

* * *

8) Solvability of  $Ax=b$  — fully explained
--------------------------------------------

The equation  $Ax=b$  is solvable **iff**

$$
b \in \operatorname{Col}(A).
$$

Equivalently:

$$
y^T b = 0 \quad \forall y \in \operatorname{Null}(A^T).
$$

This is the **compatibility condition**:  
every equation-dependency vector must annihilate  $b$ .

If violated, the system is inconsistent.

* * *

9) Degrees of freedom and constraints (final synthesis)
-------------------------------------------------------

*   Number of unknowns:  $n$ 
*   Number of independent equations:  $r$ 
*   Free variables:  $n-r = \dim(\operatorname{Null}(A))$ 
*   Independent constraints on  $b$ :  $m-r = \dim(\operatorname{Null}(A^T))$ 

Every number has a place.  
Nothing is arbitrary.

* * *

10) One-paragraph mastery test
------------------------------

If someone hands you a matrix  $A$ , you should be able to say:

> “This matrix maps  $\mathbb F^n$  onto an  $r$ \-dimensional subspace of  $\mathbb F^m$ .  
> Its kernel has dimension  $n-r$ , describing solution non-uniqueness.  
> Its left null space has dimension  $m-r$ , describing consistency constraints.  
> The row and null spaces partition the domain; the column and left null spaces partition the codomain.”

If you can say that and mean it, you own 5.4.

* * *

### Next (6.1 preview)

Now that the **map** is fully understood, we can finally justify **matrices as representations of linear maps under chosen bases**.

That’s Section **6.1** — where abstract theory collapses cleanly into computation.


6.1 — Matrices arise from choosing bases (why matrices are _representations_, not the thing itself)
---------------------------------------------------------------------------------------------------

Up to now, we’ve talked about **linear maps** as abstract objects:

$$
T: V \to W.
$$

No coordinates. No arrays of numbers. Just structure.

Section 6.1 answers the key representational question:

> How do matrices appear, and what exactly do they represent?

The answer is subtle but decisive:

> **A matrix is a linear map written in coordinates after you choose bases.**

Nothing more. Nothing less.

* * *

1) The conceptual problem matrices solve
----------------------------------------

Linear maps live between abstract vector spaces.  
Computations live in  $\mathbb F^n$  with numbers.

To _compute_, we must:

1.  choose a basis in the domain,
2.  choose a basis in the codomain,
3.  express the map relative to those choices.

A matrix is the bookkeeping device that performs step (3).

* * *

2) Fix the setup (do not skip this)
-----------------------------------

Let:

*    $V$  be a vector space with basis
    $$
    B = \{b_1,\dots,b_n\},
    $$
*    $W$  be a vector space with basis
    $$
    C = \{c_1,\dots,c_m\},
    $$
*    $T: V \to W$  be a linear transformation.

We want a concrete object that turns coordinates in  $B$  into coordinates in  $C$ .

* * *

3) Coordinate maps (the hidden machinery)
-----------------------------------------

Every basis defines a **coordinate isomorphism**.

### Domain coordinates

Define:

$$
\Phi_B : V \to \mathbb F^n, \qquad \Phi_B(v) = [v]_B,
$$

the coordinate vector of  $v$  in basis  $B$ .

### Codomain coordinates

Similarly:

$$
\Phi_C : W \to \mathbb F^m, \qquad \Phi_C(w) = [w]_C.
$$

These maps are linear, bijective, and basis-dependent.

* * *

4) The commutative diagram (this is the essence)
------------------------------------------------

What we want is a matrix  $A$  such that:

$$
\boxed{ \Phi_C(T(v)) = A\,\Phi_B(v) } \quad \text{for all } v\in V.
$$

Equivalently, the following diagram commutes:

$$
\mathbb F^n \;\xrightarrow{\;\;A\;\;}\; \mathbb F^m
$$
 
$$
\uparrow \Phi_B \qquad\qquad \downarrow \Phi_C
$$
 
$$
V \;\xrightarrow{\;\;T\;\;}\; W
$$

This is not decoration.  
This is the _definition_ of the matrix of  $T$  relative to bases  $B$  and  $C$ .

* * *

5) How the matrix is constructed (column by column, rigorously)
---------------------------------------------------------------

Here is the key construction.

### Step 1: Apply  $T$  to basis vectors of  $V$ 

For each  $j=1,\dots,n$ , compute:

$$
T(b_j) \in W.
$$

* * *

### Step 2: Express each image in the codomain basis

Since  $C$  is a basis of  $W$ , there exist unique scalars  $a_{1j},\dots,a_{mj}$  such that:

$$
T(b_j) = a_{1j} c_1 + \cdots + a_{mj} c_m.
$$

* * *

### Step 3: Assemble the matrix

Define the matrix:

$$
A = [T]_{C \leftarrow B} = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}.
$$

**Interpretation:**

> **The  $j$ \-th column of the matrix is the coordinate vector of  $T(b_j)$  in basis  $C$ .**

This single sentence explains _everything_.

* * *

6) Why this matrix works (prove the formula)
--------------------------------------------

Take any vector  $v\in V$ .  
Write it in the domain basis:

$$
v = \sum_{j=1}^n x_j b_j \quad\Longleftrightarrow\quad [v]_B = \begin{bmatrix} x_1\\ \vdots\\ x_n \end{bmatrix}.
$$

Apply  $T$ :

$$
T(v) = \sum_{j=1}^n x_j T(b_j).
$$

Substitute the expansions of  $T(b_j)$ :

$$
T(v) = \sum_{j=1}^n x_j \sum_{i=1}^m a_{ij} c_i = \sum_{i=1}^m \left( \sum_{j=1}^n a_{ij} x_j \right) c_i.
$$

So the coordinate vector of  $T(v)$  in basis  $C$  is:

$$
[T(v)]_C = \begin{bmatrix} \sum_j a_{1j} x_j\\ \sum_j a_{2j} x_j\\ \vdots\\ \sum_j a_{mj} x_j \end{bmatrix} = A [v]_B.
$$

This proves:

$$
[T(v)]_C = [T]_{C \leftarrow B}\,[v]_B.
$$

Nothing mystical happened. It’s linearity plus bookkeeping.

* * *

7) Why matrices depend on bases (and why that’s not a flaw)
-----------------------------------------------------------

Change the bases  $B$  or  $C$ , and the matrix **changes**.

But the underlying linear map  $T$  does **not** change.

So:

*   **Matrix = representation**
*   **Linear map = invariant object**

This is exactly like changing coordinate systems in geometry:  
the physical object stays the same; the numbers change.

* * *

8) The standard matrix as a special case
----------------------------------------

If:

*    $V=\mathbb F^n$ ,
*    $W=\mathbb F^m$ ,
*   both bases are the standard bases,

then:

*    $b_j = e_j$ ,
*    $T(e_j)$  is exactly the  $j$ \-th column of the usual matrix.

So the familiar rule

$$
Ax = x_1 a_1 + \cdots + x_n a_n
$$

(where  $a_j$  are columns) is not a definition—it is a **consequence** of the general theory.

* * *

9) Kernel, image, rank revisited (basis-free meaning)
-----------------------------------------------------

Even though the matrix changes with bases:

*    $\ker(T)$  is invariant,
*    $\operatorname{Im}(T)$  is invariant,
*    $\operatorname{rank}(T)$  is invariant,
*    $\operatorname{nullity}(T)$  is invariant.

Different matrices, same structural content.

This is why we studied linear maps _before_ matrices.

* * *

10) What 6.1 actually accomplished
----------------------------------

You now understand:

*   why matrices exist at all,
*   how to construct a matrix from a linear map,
*   why columns are images of basis vectors,
*   why matrix multiplication is linear combination,
*   why changing bases changes matrices but not maps.

From here on, matrices are just **coordinate shadows** of linear maps.

* * *

### Next: 6.2 — Standard matrix–vector product as linear combinations

In 6.2 we’ll dissect the formula

$$
Ax = x_1 a_1 + \cdots + x_n a_n
$$

and show how column space, null space, and rank appear instantly from it.

This is where computation and geometry finally fuse.


6.2 — Matrix–vector multiplication as linear combination (the cleanest formula in linear algebra)
-------------------------------------------------------------------------------------------------

Section 6.1 told us **what matrices really are**: coordinate representations of linear maps once bases are chosen.  
Section 6.2 strips matrix–vector multiplication down to its conceptual core.

The punchline is deceptively simple:

> **Multiplying a matrix by a vector means forming a linear combination of the matrix’s columns, using the vector’s entries as coefficients.**

Everything else—column space, solvability, rank, null space—falls out of this one fact.

* * *

1) Start from the definition (no shortcuts)
-------------------------------------------

Let

$$
A \in \mathbb F^{m\times n} \quad\text{and}\quad x \in \mathbb F^n.
$$

Write:

$$
A = \begin{bmatrix} \; a_1 \;|\; a_2 \;|\; \cdots \;|\; a_n \; \end{bmatrix},
$$

where each  $a_j \in \mathbb F^m$  is the  $j$ \-th **column** of  $A$ .

Also write:

$$
x = \begin{bmatrix} x_1\\ \vdots\\ x_n \end{bmatrix}.
$$

* * *

2) The fundamental identity (prove it once, use it forever)
-----------------------------------------------------------

### Theorem

$$
\boxed{ Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n }
$$

### Proof (coordinate-level, no handwaving)

By definition of matrix multiplication, the  $i$ \-th entry of  $Ax$  is:

$$
(Ax)_i = \sum_{j=1}^n a_{ij} x_j.
$$

Now write the right-hand side vector:

$$
x_1 a_1 + \cdots + x_n a_n = \sum_{j=1}^n x_j \begin{bmatrix} a_{1j}\\ \vdots\\ a_{mj} \end{bmatrix} = \begin{bmatrix} \sum_j a_{1j} x_j\\ \vdots\\ \sum_j a_{mj} x_j \end{bmatrix}.
$$

These expressions are identical entry by entry. ∎

This identity is not an interpretation.  
It **is** matrix–vector multiplication.

* * *

3) Why this formula is the “right” one conceptually
---------------------------------------------------

Recall from 6.1:

*   A matrix represents a linear map  $T$ ,
*   Columns of  $A$  are  $T$  applied to basis vectors,
*   Coordinates tell you how to linearly combine those images.

So this formula is simply:

$$
T(v) = \sum (\text{coordinates of } v)\cdot(\text{images of basis vectors}).
$$

That’s linearity, nothing more.

* * *

4) Column space emerges immediately
-----------------------------------

From

$$
Ax = x_1 a_1 + \cdots + x_n a_n,
$$

we see:

$$
\operatorname{Col}(A) = \{Ax : x\in\mathbb F^n\} = \text{span}\{a_1,\dots,a_n\}.
$$

So:

> **The column space is exactly the set of all linear combinations of the columns.**

This is not a definition added later.  
It drops straight out of the multiplication rule.

* * *

5) Solving  $Ax=b$  = matching a linear combination
---------------------------------------------------

The equation

$$
Ax=b
$$

means:

> Can we choose coefficients  $x_1,\dots,x_n$  so that
> 
> $$
> b = x_1 a_1 + \cdots + x_n a_n \;?
> $$

So:

*   solvable ⇔  $b \in \operatorname{Col}(A)$ ,
*   no solution ⇔  $b$  lies outside the span of the columns.

Gaussian elimination is just a systematic way to answer this span question.

* * *

6) Null space from the same formula
-----------------------------------

If

$$
Ax=0,
$$

then

$$
x_1 a_1 + \cdots + x_n a_n = 0.
$$

So:

> **Null vectors are exactly the linear dependence relations among the columns.**

Each  $x \neq 0$  in  $\operatorname{Null}(A)$  gives a nontrivial way to combine columns to zero.

This is why:

*   full column rank ⇔ columns independent ⇔ null space trivial.

* * *

7) Independence and rank, reinterpreted
---------------------------------------

From the column-combination viewpoint:

*   Columns independent  
    ⇔ only trivial combination gives zero  
    ⇔  $\operatorname{Null}(A)=\{0\}$   
    ⇔ map is injective.
*   Columns spanning  $\mathbb F^m$   
    ⇔ every  $b$  expressible as a combination  
    ⇔  $\operatorname{Col}(A)=\mathbb F^m$   
    ⇔ map is surjective.

Rank is simply:

$$
\operatorname{rank}(A) = \dim(\text{span of columns}).
$$

* * *

8) Row interpretation (dual viewpoint, same operation)
------------------------------------------------------

There is a second, equally valid interpretation.

Write rows of  $A$  as  $r_1,\dots,r_m \in \mathbb F^n$ .

Then:

$$
Ax = \begin{bmatrix} r_1 x\\ \vdots\\ r_m x \end{bmatrix} = \begin{bmatrix} \langle r_1, x\rangle\\ \vdots\\ \langle r_m, x\rangle \end{bmatrix}.
$$

So each entry of  $Ax$  is a **dot product** between  $x$  and a row.

This dual view explains:

*   why rows encode equations,
*   why row space controls constraints,
*   why row operations preserve solution sets.

Column view = building outputs  
Row view = testing inputs

Same operation, two perspectives.

* * *

9) A tiny example that encodes everything
-----------------------------------------

Let

$$
A = \begin{bmatrix} 1 & 2\\ 3 & 6 \end{bmatrix}, \quad a_1= \begin{bmatrix}1\\3\end{bmatrix}, \; a_2= \begin{bmatrix}2\\6\end{bmatrix}.
$$

Notice  $a_2 = 2a_1$ .

Then:

$$
Ax = x_1 a_1 + x_2 a_2 = (x_1+2x_2)a_1.
$$

So:

*   column space is 1-dimensional,
*   rank = 1,
*   null space consists of  $x_1+2x_2=0$ ,
*   infinite solutions when solvable,
*   system collapses one degree of freedom.

All of this is visible _before_ elimination.

* * *

10) Why this section matters more than it looks
-----------------------------------------------

Once you truly internalize

$$
Ax = \sum x_j a_j,
$$

then:

*   column space stops being abstract,
*   rank–nullity becomes intuitive,
*   least squares becomes projection onto a span,
*   SVD becomes “best possible basis for these columns.”

This single identity is the bridge between algebra, geometry, and computation.

* * *

### Next: 6.3 — Composition = matrix multiplication

In 6.3 we’ll prove that multiplying matrices corresponds exactly to composing linear maps—and why associativity is inevitable while commutativity is not.

That’s where matrices stop looking arbitrary and start looking unavoidable.


6.3 — Composition = matrix multiplication (why the product formula is inevitable)
---------------------------------------------------------------------------------

Up to now, matrices have been carefully demoted from “mysterious arrays” to what they really are:  
**coordinate representations of linear maps once bases are chosen**.

Now we answer the question that historically confused generations of students:

> Why does matrix multiplication have _that_ bizarre-looking formula?  
> Why is it associative but not commutative?  
> Why does it correspond to doing one linear transformation after another?

The answer is mercilessly simple once you respect structure:

> **Matrix multiplication is forced by composition of linear maps.**  
> There is no freedom here. The formula could not be otherwise.

* * *

1) The problem we must solve (stated cleanly)
---------------------------------------------

Let:

*    $U, V, W$  be vector spaces over  $\mathbb F$ ,
*    $S : U \to V$  and  $T : V \to W$  be linear maps.

Their composition is:

$$
T \circ S : U \to W, \qquad (T \circ S)(u) = T(S(u)).
$$

Now suppose:

*   we fix a basis  $A$  of  $U$ ,
*   a basis  $B$  of  $V$ ,
*   a basis  $C$  of  $W$ .

We already know:

*    $S$  is represented by a matrix  $[S]_{B \leftarrow A}$ ,
*    $T$  is represented by a matrix  $[T]_{C \leftarrow B}$ .

The **non-negotiable requirement** is:

> The matrix representing  $T \circ S$  must turn coordinates of  $u$  in basis  $A$  into coordinates of  $T(S(u))$  in basis  $C$ .

That requirement uniquely determines matrix multiplication.

* * *

2) The commutative diagram (this is the entire story)
-----------------------------------------------------

We want the following diagram to commute for all  $u \in U$ :

$$
\mathbb F^{\dim U} \;\xrightarrow{\;\;[S]_{B\leftarrow A}\;\;} \mathbb F^{\dim V} \;\xrightarrow{\;\;[T]_{C\leftarrow B}\;\;} \mathbb F^{\dim W}
$$
 
$$
\uparrow [\cdot]_A \qquad\qquad \uparrow [\cdot]_B \qquad\qquad \uparrow [\cdot]_C
$$
 
$$
U \;\xrightarrow{\;\;S\;\;}\; V \;\xrightarrow{\;\;T\;\;}\; W
$$

This diagram _forces_:

$$
[T(S(u))]_C = [T]_{C\leftarrow B} \,[S]_{B\leftarrow A} \,[u]_A.
$$

So the matrix of the composition must satisfy:

$$
[T\circ S]_{C\leftarrow A} = [T]_{C\leftarrow B} \,[S]_{B\leftarrow A}.
$$

This equation is not a definition.  
It is a **consistency condition**.

* * *

3) Definition (matrix multiplication, finally justified)
--------------------------------------------------------

Given matrices:

*    $A \in \mathbb F^{m \times n}$ ,
*    $B \in \mathbb F^{n \times p}$ ,

their product  $AB \in \mathbb F^{m \times p}$  is defined so that:

$$
(AB)x = A(Bx) \quad \forall x \in \mathbb F^p.
$$

This single requirement determines the formula.

* * *

4) Deriving the entry-wise formula (not memorized, derived)
-----------------------------------------------------------

Let:

$$
A = [a_1\ |\ \cdots\ |\ a_n], \quad B = [b_1\ |\ \cdots\ |\ b_p],
$$

where  $a_i \in \mathbb F^m$ ,  $b_j \in \mathbb F^n$ .

From Section 6.2:

$$
Bx = \sum_{j=1}^p x_j b_j.
$$

Apply  $A$ :

$$
A(Bx) = \sum_{j=1}^p x_j A b_j.
$$

So the  $j$ \-th column of  $AB$  must be:

$$
(AB)_j = A b_j.
$$

Now expand  $A b_j$  using columns of  $A$ :

$$
b_j = \begin{bmatrix} b_{1j}\\ \vdots\\ b_{nj} \end{bmatrix} \quad\Rightarrow\quad A b_j = \sum_{i=1}^n b_{ij} a_i.
$$

Thus:

$$
(AB)_{kj} = \sum_{i=1}^n a_{ki} b_{ij}.
$$

And there it is—the infamous formula—derived, not assumed.

* * *

5) Why multiplication is associative (and must be)
--------------------------------------------------

Let:

$$
R: T \to U, \quad S: U \to V, \quad T: V \to W.
$$

Composition of functions is associative:

$$
T \circ (S \circ R) = (T \circ S) \circ R.
$$

Matrix multiplication is just the coordinate shadow of composition, so it must satisfy:

$$
[T]([S][R]) = ([T][S])[R].
$$

There is no algebraic trick here.  
**Associativity is inherited from function composition.**

Any multiplication rule that was not associative would fail to represent composition.

* * *

6) Why multiplication is NOT commutative (and should not be)
------------------------------------------------------------

In general:

$$
T \circ S \neq S \circ T.
$$

Why?

*   Domains and codomains may not even match.
*   Even when they do, the order of operations matters.

Example:

*   Rotate a vector, then project it.
*   Project it, then rotate it.

Different outcomes. So:

$$
AB \neq BA \quad \text{in general}.
$$

Non-commutativity is not a flaw.  
It is **faithful representation of reality**.

* * *

7) Identity matrix = identity map (forced, not chosen)
------------------------------------------------------

The identity map  $I_V : V \to V$  satisfies:

$$
I_V(v) = v.
$$

Its matrix representation in any basis must satisfy:

$$
[I_V][v] = [v].
$$

So its matrix is the identity matrix  $I$ , and it must obey:

$$
IA = A, \quad AI = A.
$$

Again: not a convention. A necessity.

* * *

8) Inverses: when matrix inversion exists
-----------------------------------------

A linear map  $T: V \to V$  is invertible iff:

*   it is bijective,
*   its kernel is trivial,
*   its rank equals  $\dim(V)$ .

In that case, there exists  $T^{-1}$ , and:

$$
[T^{-1}] = [T]^{-1}.
$$

Matrix inversion is just coordinate-level undoing of a linear transformation.

* * *

9) Dimension compatibility (why sizes must match)
-------------------------------------------------

If:

$$
A \in \mathbb F^{m \times n}, \quad B \in \mathbb F^{n \times p},
$$

then:

*    $B$  maps  $\mathbb F^p \to \mathbb F^n$ ,
*    $A$  maps  $\mathbb F^n \to \mathbb F^m$ .

So  $AB$  maps  $\mathbb F^p \to \mathbb F^m$ .

If inner dimensions don’t match, composition is meaningless—hence multiplication is undefined.

This is not syntax. It’s semantics.

* * *

10) The “column rule” revisited (most useful operational fact)
--------------------------------------------------------------

One sentence you should internalize:

> **The columns of  $AB$  are obtained by applying  $A$  to the columns of  $B$ .**

Formally:

$$
AB = [A b_1\ |\ \cdots\ |\ A b_p].
$$

This makes many computations and proofs trivial.

* * *

11) What 6.3 actually achieved
------------------------------

You now understand:

*   why matrix multiplication exists at all,
*   why its formula is forced,
*   why it is associative,
*   why it is not commutative,
*   why identity and inverse matrices behave as they do,
*   why dimension matching is non-negotiable.

Matrix multiplication is not a trick.  
It is **composition written in coordinates**.

* * *

### Next: 6.4 (if you want to continue)

The next natural step is to examine **change of basis** and similarity transformations:

$$
A \mapsto P^{-1} A P.
$$

That will finally explain why eigenvalues are basis-invariant and why diagonalization is even a meaningful concept.

When you’re ready, we proceed.


6.4 — Change of basis and similarity: why matrices change but linear maps don’t
-------------------------------------------------------------------------------

This section closes the conceptual loop that started in 6.1.

You already know:

*   a **linear map** is the real object,
*   a **matrix** is its coordinate representation once bases are chosen.

Now we answer the inevitable follow-up:

> If I change the basis, how does the matrix change?  
> And what, if anything, stays the same?

The answer explains **similarity**, **conjugation**, and why eigenvalues, rank, determinant, and trace are meaningful invariants.

* * *

1) The core tension (state it cleanly)
--------------------------------------

Let  $T: V \to V$  be a linear map on a finite-dimensional vector space.

Choose:

*   basis  $B$  of  $V$  → matrix  $A=[T]_B$ ,
*   basis  $B'$  of  $V$  → matrix  $A'=[T]_{B'}$ .

Facts:

*    $A \neq A'$  in general,
*   both represent the _same_ linear map  $T$ .

So there must be a precise relationship between  $A$  and  $A'$ .

That relationship is **similarity**.

* * *

2) Coordinate change is itself a linear map
-------------------------------------------

Fix two bases of the same space  $V$ :

$$
B=\{b_1,\dots,b_n\}, \qquad B'=\{b'_1,\dots,b'_n\}.
$$

There is a linear map:

$$
\text{Id}_V : V \to V
$$

(the identity map), but its **matrix representation depends on bases**.

Define the **change-of-basis matrix**:

$$
P := [\text{Id}_V]_{B \leftarrow B'}.
$$

Meaning:

$$
[v]_B = P [v]_{B'} \quad \forall v\in V.
$$

Interpretation:

*    $P$  converts coordinates **from the new basis to the old basis**.
*   Columns of  $P$  are the coordinates of  $b'_j$  written in basis  $B$ .

Since both bases are bases,  $P$  is invertible.

* * *

3) Expressing the same vector two ways
--------------------------------------

From the definition:

$$
[v]_{B'} = P^{-1}[v]_B.
$$

So:

*    $P$  = “new → old” coordinates,
*    $P^{-1}$  = “old → new” coordinates.

This directionality matters and is a common source of confusion.

* * *

4) Deriving the similarity formula (step-by-step)
-------------------------------------------------

Let:

*    $A=[T]_B$ ,
*    $A'=[T]_{B'}$ .

By definition of matrix representation:

$$
[T(v)]_B = A [v]_B, \qquad [T(v)]_{B'} = A' [v]_{B'}.
$$

Now relate the two coordinate systems.

Start with  $B'$ \-coordinates:

$$
[T(v)]_{B'} = P^{-1}[T(v)]_B.
$$

Substitute the  $B$ \-matrix action:

$$
[T(v)]_{B'} = P^{-1} A [v]_B.
$$

Replace  $[v]_B = P [v]_{B'}$ :

$$
[T(v)]_{B'} = P^{-1} A P [v]_{B'}.
$$

But also, by definition:

$$
[T(v)]_{B'} = A' [v]_{B'}.
$$

Since this holds for all vectors, we conclude:

$$
\boxed{ A' = P^{-1} A P }
$$

This is **similarity**.

No tricks. No conventions. Just consistency of coordinates.

* * *

5) Definition: similar matrices
-------------------------------

Two square matrices  $A$  and  $A'$  are **similar** if:

$$
A' = P^{-1} A P \quad\text{for some invertible } P.
$$

Meaning:

> They represent the same linear transformation in different bases.

Similarity is not an algebraic curiosity.  
It is the equivalence relation induced by “same linear map, different coordinates.”

* * *

6) What similarity preserves (invariants)
-----------------------------------------

If  $A' = P^{-1} A P$ , then  $A$  and  $A'$  share all **basis-independent** properties.

These include:

### (A) Rank

$$
\operatorname{rank}(A')=\operatorname{rank}(A).
$$

Reason: rank is dimension of image, which depends only on the linear map.

* * *

### (B) Nullity

$$
\dim(\operatorname{Null}(A'))=\dim(\operatorname{Null}(A)).
$$

Same kernel, different coordinates.

* * *

### (C) Determinant

$$
\det(A')=\det(A).
$$

Proof:

$$
\det(P^{-1}AP)=\det(P^{-1})\det(A)\det(P)=\det(A).
$$

* * *

### (D) Trace

$$
\operatorname{tr}(A')=\operatorname{tr}(A).
$$

This is less obvious algebraically but fundamental. Trace is basis-invariant.

* * *

### (E) Eigenvalues (with multiplicity)

If  $Av=\lambda v$ , then in the new basis:

$$
A'(P^{-1}v)=\lambda(P^{-1}v).
$$

So eigenvalues survive basis changes unchanged.

This is why eigenvalues are meaningful geometric data.

* * *

7) What similarity does _not_ preserve
--------------------------------------

Similarity does **not** preserve:

*   individual matrix entries,
*   column vectors,
*   row vectors,
*   sparsity patterns,
*   triangular / diagonal appearance (unless special).

Those are coordinate artifacts.

* * *

8) Similarity vs equality (do not confuse them)
-----------------------------------------------

*    $A = A'$   
    → same numbers, same coordinates, same representation.
*    $A \sim A'$  (similar)  
    → same linear map, different coordinates.

Equality is fragile.  
Similarity is structural.

* * *

9) Diagonalization reinterpreted (preview of spectral theory)
-------------------------------------------------------------

A matrix  $A$  is **diagonalizable** if it is similar to a diagonal matrix:

$$
A = P D P^{-1}.
$$

Meaning:

> There exists a basis in which the linear map acts independently on each coordinate direction.

Diagonal entries = eigenvalues.  
Columns of  $P$  = eigenvectors written in the original basis.

This is not a computational trick.  
It is the statement “the map decouples in the right coordinates.”

* * *

10) Geometric meaning (one clean sentence)
------------------------------------------

Changing basis does **not** change the transformation—  
it only changes the _language_ in which you describe it.

Similarity is the algebraic encoding of that fact.

* * *

11) Common pitfalls (explicitly flagged)
----------------------------------------

1.  Mixing up  $PAP^{-1}$  and  $P^{-1}AP$ .  
    Direction matters. Always derive from coordinate maps.
2.  Thinking similarity is optional.  
    It is forced by basis changes.
3.  Believing eigenvalues depend on basis.  
    If they did, they would be meaningless.

* * *

12) What 6.4 completed structurally
-----------------------------------

You now understand:

*   how matrices change under basis change,
*   why similarity is the right equivalence relation,
*   why eigenvalues, rank, determinant, trace are invariants,
*   why diagonalization is meaningful,
*   why linear algebra separates structure from coordinates.

At this point, the **linear-map → matrix → invariant** pipeline is complete.

* * *

### Where this leads next

From here, two natural paths open:

1.  **Eigenvalues and diagonalization** (spectral layer),
2.  **Algorithms** (Gaussian elimination, QR, SVD) interpreted via basis change and projection.

Both are now conceptually clean.

Tell me which path you want to take next, and we continue at the same depth.


Spectral layer — Eigenvalues & diagonalization (from first principles, no gaps)
-------------------------------------------------------------------------------

This layer answers a single, profound question:

> **Are there directions that a linear map preserves, changing only their length (and possibly sign/phase)?**

Those directions are **eigenvectors**.  
The corresponding scaling factors are **eigenvalues**.  
Diagonalization is the statement that _the entire map can be decomposed into independent scalings_—if and only if enough such directions exist.

I’ll build this in a strict logical order, prove what needs proving, flag failure modes, and explain what each result _means_.

* * *

### 0) What the spectral layer is really about

Every linear map  $T:V\to V$  mixes coordinates—unless you choose the _right_ basis.  
The spectral layer asks whether there exists a basis in which **no mixing happens at all**.

If yes, computation and geometry collapse to scalar arithmetic.  
If no, the obstruction is deep—and informative.

* * *

1) Eigenvalues and eigenvectors: definition and immediate meaning
-----------------------------------------------------------------

### Definition

Let  $T:V\to V$  be linear over a field  $\mathbb F$ .

A **nonzero** vector  $v\in V$  is an **eigenvector** of  $T$  with **eigenvalue**  $\lambda\in\mathbb F$  if

$$
T(v)=\lambda v.
$$

Equivalently (and this matters),

$$
(T-\lambda I)v=0,
$$

so  $v\in\ker(T-\lambda I)$ .

**Key consequences right away**

*   Eigenvectors are exactly the **nonzero null vectors** of  $T-\lambda I$ .
*   Eigenvalues are the scalars  $\lambda$  for which  $T-\lambda I$  is **not injective**.

* * *

2) Matrix formulation (no new ideas, just coordinates)
------------------------------------------------------

Let  $A\in\mathbb F^{n\times n}$  represent  $T$  in some basis.

Then

$$
Av=\lambda v \quad\Longleftrightarrow\quad (A-\lambda I)v=0.
$$

So:

$$
\boxed{\lambda \text{ is an eigenvalue } \iff \det(A-\lambda I)=0.}
$$

This determinant is not decorative. It encodes non-injectivity.

* * *

3) The characteristic polynomial (why eigenvalues are roots)
------------------------------------------------------------

### Definition

The **characteristic polynomial** of  $A$  is

$$
p_A(\lambda)=\det(A-\lambda I).
$$

Facts (prove or accept for now):

*    $p_A$  is a degree- $n$  polynomial.
*   Over  $\mathbb C$ , it has exactly  $n$  roots counting multiplicity.
*   Over  $\mathbb R$ , roots may be complex.

**Eigenvalues = roots of  $p_A$ **.

This is why eigenvalues are **basis-invariant**: similarity preserves determinants.

* * *

4) Eigenspaces: structure inside each eigenvalue
------------------------------------------------

For a fixed eigenvalue  $\lambda$ , define the **eigenspace**

$$
E_\lambda := \ker(A-\lambda I).
$$

Properties:

*    $E_\lambda$  is a subspace.
*    $\dim(E_\lambda)\ge 1$ .
*   All eigenvectors for  $\lambda$  live here.

### Two multiplicities (do not confuse them)

*   **Algebraic multiplicity**  $m_\lambda$ :  
    multiplicity of  $\lambda$  as a root of  $p_A$ .
*   **Geometric multiplicity**  $g_\lambda$ :  
     $\dim(E_\lambda)$ .

**Always true**

$$
1 \le g_\lambda \le m_\lambda.
$$

The inequality is where diagonalization lives or dies.

* * *

5) Linear independence of eigenvectors (critical theorem)
---------------------------------------------------------

### Theorem

Eigenvectors corresponding to **distinct eigenvalues** are linearly independent.

#### Proof (clean and decisive)

Suppose

$$
\sum_{i=1}^k c_i v_i = 0
$$

where  $Av_i=\lambda_i v_i$  and all  $\lambda_i$  are distinct.

Apply  $A$ :

$$
\sum c_i \lambda_i v_i = 0.
$$

Subtract  $\lambda_1$  times the original equation:

$$
\sum_{i=2}^k c_i(\lambda_i-\lambda_1)v_i = 0.
$$

Repeat inductively. Since  $\lambda_i-\lambda_1\neq 0$ , all coefficients vanish. ∎

**Meaning**  
Distinct eigenvalues give **independent directions** automatically.  
No Gram–Schmidt, no luck, no geometry required.

* * *

6) Diagonalization: definition and exact criterion
--------------------------------------------------

### Definition

A matrix  $A\in\mathbb F^{n\times n}$  is **diagonalizable** if

$$
A = P D P^{-1}
$$

where:

*    $D$  is diagonal,
*   columns of  $P$  are eigenvectors of  $A$ .

Equivalently: there exists a basis of  $V$  consisting entirely of eigenvectors.

* * *

### The diagonalization criterion (this is the theorem you must own)

$$
\boxed{ A \text{ is diagonalizable} \iff \sum_{\lambda} \dim(E_\lambda) = n }
$$

That is:

> **The total geometric multiplicity equals the dimension of the space.**

This happens iff for every eigenvalue:

$$
g_\lambda = m_\lambda.
$$

* * *

7) Why diagonalization is powerful (and not cosmetic)
-----------------------------------------------------

If

$$
A=PDP^{-1},
$$

then for any power  $k$ ,

$$
A^k = P D^k P^{-1}.
$$

And  $D^k$  is trivial:

$$
D^k = \operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k).
$$

**Interpretation**

*   Dynamics decouple.
*   Iteration, exponentials, stability, long-run behavior become transparent.
*   This is why diagonalization dominates differential equations, Markov chains, and dynamical systems.

![https://www.geogebra.org/resource/Nkq8knZ9/hMg5Iq4qpGT7OVwW/material-Nkq8knZ9.png?utm_source=chatgpt.com](https://www.geogebra.org/resource/Nkq8knZ9/hMg5Iq4qpGT7OVwW/material-Nkq8knZ9.png?utm_source=chatgpt.com)

![https://media.geeksforgeeks.org/wp-content/uploads/20250822152247056253/F-to-standard.webp?utm_source=chatgpt.com](https://media.geeksforgeeks.org/wp-content/uploads/20250822152247056253/F-to-standard.webp?utm_source=chatgpt.com)

![https://kharshit.github.io/img/eigenvectors.png?utm_source=chatgpt.com](https://kharshit.github.io/img/eigenvectors.png?utm_source=chatgpt.com)

* * *

8) Failure modes: why diagonalization can fail
----------------------------------------------

### Example (canonical)

$$
A= \begin{bmatrix} 1 & 1\\ 0 & 1 \end{bmatrix}.
$$
*   Characteristic polynomial:  $(1-\lambda)^2$ .
*   Algebraic multiplicity  $=2$ .
*   Eigenspace:
    $$
    (A-I)v=0 \Rightarrow v=(x,0),
    $$
    so  $g_\lambda=1$ .

Result:

$$
g_\lambda < m_\lambda \Rightarrow \text{not diagonalizable}.
$$

**Meaning**  
There aren’t enough invariant directions. The map _shears_.

* * *

9) Real vs complex diagonalization
----------------------------------

Over  $\mathbb R$ :

*   Some matrices have no real eigenvalues (e.g. rotations).
*   No real diagonalization possible.

Over  $\mathbb C$ :

*   Every polynomial splits.
*   Eigenvalues always exist.
*   But diagonalization may still fail if  $g_\lambda < m_\lambda$ .

This motivates **Jordan form** later—but that’s beyond today’s layer.

* * *

10) Special cases you must recognize instantly
----------------------------------------------

### Symmetric (or Hermitian) matrices

If  $A=A^T$  (real) or  $A=A^*$  (complex):

*   All eigenvalues are real.
*   Eigenvectors for distinct eigenvalues are orthogonal.
*   Always diagonalizable (even orthogonally/unitarily).

This is the spectral theorem—the cleanest case in all of linear algebra.

### Triangular matrices

Eigenvalues are exactly the diagonal entries.

Diagonalization depends on eigenspaces, not appearance.

* * *

11) Spectral viewpoint summary (one paragraph)
----------------------------------------------

A linear map is diagonalizable precisely when the space decomposes into invariant one-dimensional subspaces.  
Eigenvalues measure how each direction scales; eigenvectors identify those directions.  
Failure of diagonalization means the map intrinsically mixes directions in a way no basis can undo.

* * *

12) Mastery checklist (non-negotiable)
--------------------------------------

You should now be able to:

*   Derive eigenvalues from  $\det(A-\lambda I)=0$ .
*   Compute eigenspaces and their dimensions.
*   Distinguish algebraic vs geometric multiplicity.
*   Decide diagonalizability rigorously.
*   Explain _why_ diagonalization matters structurally.
*   Recognize guaranteed diagonalization cases (symmetric/Hermitian).

* * *

### Where this naturally goes next

Two powerful continuations:

1.  **Orthogonal diagonalization & the spectral theorem** (for symmetric matrices).
2.  **Jordan canonical form** (what replaces diagonalization when it fails).

Say which one you want next, and we’ll go just as deep.


Orthogonal diagonalization & the Spectral Theorem
-------------------------------------------------

_(the cleanest, most rigid case in all of linear algebra)_

What you asked for—**option 1**—is where everything suddenly becomes _perfectly behaved_.  
No pathologies, no Jordan blocks, no hand-waving. Structure, geometry, and computation finally line up.

We will proceed in this order:

1.  Why symmetry changes everything
2.  Inner products, orthogonality, and self-adjointness
3.  Statement of the Spectral Theorem (precise)
4.  Proof skeleton (with all logical dependencies exposed)
5.  Orthogonal diagonalization  $A=Q\Lambda Q^\top$ 
6.  Geometric meaning (axes, energy, decoupling)
7.  Consequences and invariants
8.  Why this case is _exceptional_, not typical

I will be explicit about what is **proved**, what is **used**, and what **fails** outside this setting.

* * *

1) Why symmetry is not a cosmetic condition
-------------------------------------------

Let  $A\in\mathbb R^{n\times n}$ .

The condition

$$
A = A^\top
$$

looks mild. It is not.

It means:

$$
\langle Ax, y\rangle = \langle x, Ay\rangle \quad\forall x,y\in\mathbb R^n,
$$

where  $\langle x,y\rangle = x^\top y$  is the Euclidean inner product.

This is the **defining property** of a _self-adjoint_ operator.

So a real symmetric matrix is not “just another matrix”:  
it is a linear map that is perfectly compatible with the geometry of the space.

This compatibility is exactly what unlocks orthogonality, real eigenvalues, and diagonalization.

* * *

2) Orthogonality and why we care
--------------------------------

Recall:

*   Vectors  $u,v$  are orthogonal if  $\langle u,v\rangle=0$ .
*   An **orthonormal basis** satisfies
    $$
    \langle q_i,q_j\rangle=\delta_{ij}.
    $$

Why orthonormal bases are special:

*   Coordinates are obtained by dot products:
    $$
    v = \sum_i \langle q_i, v\rangle q_i.
    $$
*   Lengths and angles are preserved.
*   Numerical stability is maximal.

If a matrix is diagonalizable by an **orthonormal** basis, we say it is **orthogonally diagonalizable**.

That is the strongest form of diagonalization possible.

* * *

3) Spectral Theorem — exact statement (real case)
-------------------------------------------------

### Theorem (Spectral Theorem, real version)

Let  $A\in\mathbb R^{n\times n}$  be **symmetric**:

$$
A = A^\top.
$$

Then:

1.  All eigenvalues of  $A$  are **real**.
2.  Eigenspaces corresponding to **distinct eigenvalues are orthogonal**.
3.  There exists an **orthonormal basis of  $\mathbb R^n$ ** consisting of eigenvectors of  $A$ .
4.  Equivalently, there exists an orthogonal matrix  $Q$  such that
    $$
    \boxed{A = Q \Lambda Q^\top}
    $$
    where  $\Lambda$  is diagonal with real entries.

This is not “sometimes true”.  
This is **always true** for real symmetric matrices.

* * *

4) Why eigenvalues must be real (proved, not asserted)
------------------------------------------------------

Let  $Av=\lambda v$  with  $v\neq 0$ .

Take inner products:

$$
\langle Av, v\rangle = \langle \lambda v, v\rangle = \lambda \langle v,v\rangle.
$$

But by symmetry:

$$
\langle Av, v\rangle = \langle v, Av\rangle = \langle v, \lambda v\rangle = \bar{\lambda}\langle v,v\rangle.
$$

So:

$$
\lambda \langle v,v\rangle = \bar{\lambda}\langle v,v\rangle.
$$

Since  $\langle v,v\rangle>0$ ,

$$
\lambda=\bar{\lambda}.
$$

Thus  $\lambda\in\mathbb R$ .

This argument **fails immediately** without symmetry.

* * *

5) Why eigenspaces are orthogonal (proved cleanly)
--------------------------------------------------

Let:

$$
Av=\lambda v,\quad Aw=\mu w,\quad \lambda\neq\mu.
$$

Compute:

$$
\langle Av,w\rangle = \lambda\langle v,w\rangle,
$$

but also (symmetry):

$$
\langle Av,w\rangle = \langle v,Aw\rangle = \mu\langle v,w\rangle.
$$

Thus:

$$
(\lambda-\mu)\langle v,w\rangle=0.
$$

Since  $\lambda\neq\mu$ ,

$$
\langle v,w\rangle=0.
$$

So eigenvectors from different eigenvalues are **automatically orthogonal**.

No Gram–Schmidt needed yet.

* * *

6) Why diagonalization must succeed (core logic)
------------------------------------------------

We now combine facts:

*   The characteristic polynomial has degree  $n$ .
*   All eigenvalues are real.
*   Distinct eigenvalues give orthogonal eigenspaces.
*   Each eigenspace has dimension equal to its geometric multiplicity.

Because orthogonal subspaces add cleanly,  
the direct sum of all eigenspaces has dimension:

$$
\sum_\lambda \dim(E_\lambda) = n.
$$

That means eigenvectors **span the entire space**.

Choose an orthonormal basis inside each eigenspace  
(and this is always possible inside any subspace).

Stack them together → an orthonormal eigenbasis.

That is the heart of the theorem.

* * *

7) Orthogonal diagonalization explicitly
----------------------------------------

Let:

*    $q_1,\dots,q_n$  be orthonormal eigenvectors,
*    $\lambda_1,\dots,\lambda_n$  the corresponding eigenvalues.

Define:

$$
Q = [q_1\ \cdots\ q_n], \quad \Lambda = \operatorname{diag}(\lambda_1,\dots,\lambda_n).
$$

Then:

$$
\boxed{A = Q \Lambda Q^\top}, \quad Q^\top Q = QQ^\top = I.
$$

This is not similarity by an arbitrary invertible matrix.  
This is **conjugation by an isometry**.

That distinction matters enormously.

![https://i.sstatic.net/pXrfp.png?utm_source=chatgpt.com](https://images.openai.com/thumbnails/url/ARpCQ3icu5mZUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw42DAg0y4hKT03xMQ8J1c3087KstMyJ8i5JDCuwsAgtq8o0NggJdfFwzc-PcPQvMyxXKwYASVQlow?utm_source=chatgpt.com)

![https://peterbloem.nl/images/pca-3/multiplication.svg?utm_source=chatgpt.com](https://peterbloem.nl/images/pca-3/multiplication.svg?utm_source=chatgpt.com)

![https://ars.els-cdn.com/content/image/3-s2.0-B9780121609542500044-f03-18-9780121609542.jpg?utm_source=chatgpt.com](https://ars.els-cdn.com/content/image/3-s2.0-B9780121609542500044-f03-18-9780121609542.jpg?utm_source=chatgpt.com)

* * *

8) Geometric meaning (this is the payoff)
-----------------------------------------

Orthogonal diagonalization says:

> A symmetric linear transformation is a rotation (or reflection),  
> followed by independent scalings along perpendicular axes,  
> followed by the inverse rotation.

No shearing.  
No coupling.  
No distortion of angles beyond scaling.

Each eigenvector is a **principal axis**.  
Each eigenvalue is a **stretch factor** along that axis.

This is why symmetric matrices appear everywhere physics, statistics, and optimization care about _energy_.

* * *

9) Immediate consequences (all structural, all important)
---------------------------------------------------------

### (A) Quadratic forms

For  $A=A^\top$ ,

$$
x^\top A x = \sum_i \lambda_i y_i^2 \quad\text{where } y=Q^\top x.
$$

So the sign of eigenvalues completely determines:

*   positive definite,
*   negative definite,
*   indefinite.

### (B) Rayleigh quotient

$$
\frac{x^\top A x}{x^\top x}
$$

is minimized and maximized exactly by eigenvectors corresponding to smallest and largest eigenvalues.

This underlies PCA and variational principles.

### (C) Stability and dynamics

For  $x_{k+1}=Ax_k$ ,  
behavior is governed entirely by eigenvalues:

*    $|\lambda|<1$ : decay,
*    $|\lambda|>1$ : growth,
*    $|\lambda|=1$ : neutral.

No hidden coupling terms.

* * *

10) Why this case is _exceptional_
----------------------------------

Most matrices are **not** symmetric.  
For them:

*   eigenvalues may be complex,
*   eigenspaces may be defective,
*   diagonalization may fail,
*   orthogonality is lost.

The spectral theorem is powerful precisely because it applies to a **very rigid class** of operators.

That rigidity is a feature, not a limitation.

* * *

11) One-sentence mastery check
------------------------------

If you truly understand this layer, you can say:

> “A real symmetric matrix represents a self-adjoint operator, hence admits an orthonormal eigenbasis, making the transformation a pure scaling along perpendicular directions.”

If that sentence is _obvious_ to you, you own the spectral theorem.

* * *

### Where to go next (natural continuations)

Two equally deep next steps:

1.  **Positive definite matrices, quadratic forms, and optimization**  
    (why convexity lives here)
2.  **SVD** — what replaces eigen-decomposition when symmetry is gone  
    (the true geometry of _any_ matrix)

Say which one you want, and we continue at full depth.


Jordan Canonical Form — when diagonalization fails, but structure still survives
--------------------------------------------------------------------------------

Diagonalization was the dream case: the map splits into independent scalings.  
Jordan form is what reality gives you when that dream fails—**and it tells you exactly how it fails, no more and no less**.

I’ll proceed from first principles, with full logical closure:

1.  Why diagonalization can fail
2.  Algebraic vs geometric multiplicity (the real obstruction)
3.  Generalized eigenvectors (why we need them)
4.  Jordan blocks (the atomic pieces)
5.  Jordan chains and invariant subspaces
6.  The Jordan Canonical Form theorem (precise statement)
7.  What Jordan form means dynamically and geometrically
8.  What it preserves, what it hides, and why it matters
9.  Limits and cautions (numerics, interpretation)

* * *

1) Why diagonalization fails (pinpoint the obstruction)
-------------------------------------------------------

Recall the criterion:

A matrix  $A\in\mathbb F^{n\times n}$  is diagonalizable  
iff the total dimension of eigenspaces equals  $n$ .

Failure occurs exactly when, for some eigenvalue  $\lambda$ ,

$$
\underbrace{\dim\ker(A-\lambda I)}_{\text{geometric multiplicity } g_\lambda} \;<\; \underbrace{\text{mult}_\lambda}_{\text{algebraic multiplicity } m_\lambda}.
$$

Interpretation:

*   The characteristic polynomial promises  $m_\lambda$  “slots”.
*   The eigenspace only supplies  $g_\lambda$  genuine invariant directions.
*   The missing  $m_\lambda-g_\lambda$  directions must exist—but **not** as eigenvectors.

Jordan theory explains what those missing directions look like.

* * *

2) The key idea: eigenvectors are not enough
--------------------------------------------

If  $v$  is an eigenvector:

$$
(A-\lambda I)v = 0.
$$

But what if there are vectors  $w\neq 0$  such that:

$$
(A-\lambda I)w = v \quad \text{(an eigenvector)}?
$$

Then:

*    $w$  is **not** an eigenvector,
*   but applying  $A$  to  $w$  gives:
    $$
    Aw = \lambda w + v.
    $$

So  $w$  is _almost_ invariant—up to a drift along  $v$ .

These are **generalized eigenvectors**.

* * *

3) Generalized eigenspaces (definition that fixes everything)
-------------------------------------------------------------

### Definition

For eigenvalue  $\lambda$ , define the **generalized eigenspace**:

$$
\mathcal G_\lambda := \ker\big((A-\lambda I)^k\big) \quad\text{for sufficiently large } k.
$$

Facts (all provable, but we’ll state cleanly):

*   For large enough  $k$ , this stabilizes.
*    $\dim(\mathcal G_\lambda) = m_\lambda$ .
*    $\ker(A-\lambda I) \subseteq \mathcal G_\lambda$ .
*    $\mathcal G_\lambda$  is  $A$ \-invariant.

So the missing dimensions are recovered **inside**  $\mathcal G_\lambda$ .

* * *

4) Jordan blocks: the atomic failure mode
-----------------------------------------

The simplest non-diagonalizable behavior occurs in a **Jordan block**.

### Definition (Jordan block)

A Jordan block of size  $k$  with eigenvalue  $\lambda$  is:

$$
J_k(\lambda)= \begin{bmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda& 1 & \cdots & 0 \\ \vdots & & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & \lambda& 1 \\ 0 & \cdots & \cdots & 0 & \lambda \end{bmatrix}.
$$

Properties you should internalize:

*   Diagonal entries are  $\lambda$ .
*   Ones on the superdiagonal encode **coupling**.
*    $J_k(\lambda)$  has:
    *   algebraic multiplicity  $k$ ,
    *   geometric multiplicity  $1$ .

This is the irreducible “defect unit”.

![https://mathworld.wolfram.com/images/socialmedia/share/ogimage_JordanBlock.png?utm_source=chatgpt.com](https://mathworld.wolfram.com/images/socialmedia/share/ogimage_JordanBlock.png?utm_source=chatgpt.com)

![https://img.yumpu.com/18973148/1/500x640/handout-3-generalized-eigenvectors-and-jordan-form.jpg?utm_source=chatgpt.com](https://img.yumpu.com/18973148/1/500x640/handout-3-generalized-eigenvectors-and-jordan-form.jpg?utm_source=chatgpt.com)

![https://i.sstatic.net/u8lUi.png?utm_source=chatgpt.com](https://images.openai.com/thumbnails/url/sbbx8Hicu5mVUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw5JCQ_PDPQ09StzT_LSzY90rgqKsPDP9zGyyK3UTdWtKncN8zcOKXTM8DXPSrTMdS81VSsGAHYmJes?utm_source=chatgpt.com)

* * *

5) Jordan chains (how blocks arise from vectors)
------------------------------------------------

A **Jordan chain** for eigenvalue  $\lambda$  is a sequence:

$$
v_1,\; v_2,\; \dots,\; v_k
$$

such that:

$$
(A-\lambda I)v_1 = 0,
$$
 
$$
(A-\lambda I)v_2 = v_1,
$$
 
$$
(A-\lambda I)v_3 = v_2,
$$
 
$$
\vdots
$$
 
$$
(A-\lambda I)v_k = v_{k-1}.
$$

Interpretation:

*    $v_1$ : true eigenvector.
*    $v_2$ : generalized eigenvector of rank 2.
*    $v_3$ : generalized eigenvector of rank 3.
*   …
*   The chain length = size of the Jordan block.

In this basis,  $A$  acts exactly like a Jordan block.

* * *

6) The Jordan Canonical Form theorem (precise statement)
--------------------------------------------------------

### Theorem (Jordan Canonical Form)

Let  $A\in\mathbb C^{n\times n}$ .  
Then there exists an invertible matrix  $P$  such that:

$$
\boxed{ A = PJP^{-1} }
$$

where  $J$  is block diagonal:

$$
J = \begin{bmatrix} J_{k_1}(\lambda_1) & & \\ & \ddots & \\ & & J_{k_r}(\lambda_r) \end{bmatrix}.
$$

Moreover:

*   Each eigenvalue  $\lambda$  appears in blocks whose total size equals its algebraic multiplicity.
*   The number of blocks for  $\lambda$  equals its geometric multiplicity.
*   Block sizes encode the _depth_ of non-diagonalizability.

This form is **unique up to permutation of blocks**.

* * *

7) What Jordan form really tells you
------------------------------------

Jordan form decomposes a linear map into:

1.  **Pure scaling** (the diagonal  $\lambda$ ’s), and
2.  **Nilpotent drift** (the superdiagonal ones).

You can write:

$$
A = \lambda I + N
$$

on each block, where:

*    $N$  is nilpotent ( $N^k=0$ ),
*    $N$  measures how far the map is from diagonalizable.

Diagonalizable ⇔ all nilpotent parts vanish.

* * *

8) Dynamics and powers: why Jordan blocks matter
------------------------------------------------

Consider iterates  $A^t$ .

For a Jordan block:

$$
J_k(\lambda)^t = \lambda^t \begin{bmatrix} 1 & \binom{t}{1} & \binom{t}{2} & \cdots \\ 0 & 1 & \binom{t}{1} & \cdots \\ \vdots & & \ddots & \\ 0 & \cdots & 0 & 1 \end{bmatrix}.
$$

Consequences:

*   Even if  $|\lambda|<1$ , polynomial growth from nilpotent terms may appear transiently.
*   Stability depends on both  $\lambda$  **and** block size.
*   This explains why defective matrices behave poorly in time evolution.

* * *

9) What Jordan form preserves (true invariants)
-----------------------------------------------

Jordan form preserves:

*   eigenvalues,
*   algebraic multiplicities,
*   geometric multiplicities,
*   sizes of Jordan blocks,
*   minimal polynomial,
*   similarity class.

It does **not** preserve:

*   orthogonality,
*   numerical stability,
*   sparsity,
*   geometry of inner products.

Jordan form is algebraically exact, but geometrically fragile.

* * *

10) Real vs complex fields (important boundary)
-----------------------------------------------

Over  $\mathbb C$ :

*   Jordan form always exists.

Over  $\mathbb R$ :

*   Complex eigenvalues force  $2\times 2$  real blocks (rotations).
*   Real Jordan form is more complicated.
*   This is why spectral theory prefers  $\mathbb C$ .

* * *

11) Why Jordan form is _not_ used numerically
---------------------------------------------

Jordan form is **ill-conditioned**:

*   Tiny perturbations destroy block structure.
*   Numerically unstable to compute.
*   Practically useless for floating-point computation.

That’s why modern numerical linear algebra replaces it with:

*   **Schur decomposition** (unitary, stable),
*   **SVD** (geometry-first, always exists).

Jordan form is a **theoretical microscope**, not a computational tool.

* * *

12) Conceptual summary (the one you should keep)
------------------------------------------------

> Diagonalization fails when eigenvectors are insufficient.  
> Jordan form shows that the failure is controlled, finite, and structured:  
> each eigenvalue carries a nilpotent “defect” measuring how far the map is from being diagonal.

* * *

13) Where Jordan sits in the big picture
----------------------------------------

*   Spectral theorem: _perfect geometry_ (self-adjoint).
*   Jordan form: _perfect algebra_ (similarity classification).
*   SVD: _perfect geometry for all matrices_.

Each solves a different problem.
