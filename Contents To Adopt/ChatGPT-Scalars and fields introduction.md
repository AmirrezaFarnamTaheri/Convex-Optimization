
# Scalars and fields introduction

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/21/2025 12:31:37  
**Updated:** 12/21/2025 15:20:36  
**Exported:** 12/21/2025 15:20:52  
**Link:** [https://chatgpt.com/g/g-p-6947b657693c81918d50611efd43d5fe-linalg/c/6947b761-8b38-8322-ac58-aab577937cf6](https://chatgpt.com/g/g-p-6947b657693c81918d50611efd43d5fe-linalg/c/6947b761-8b38-8322-ac58-aab577937cf6)  

## Response:
0.1 Scalars and fields — what “numbers are allowed,” and why linear algebra cares
---------------------------------------------------------------------------------

Before “vectors” exist, linear algebra is already quietly assuming something about the _numbers_ you’re allowed to use as coefficients. Those numbers are the scalars. A _field_ is the rulebook that tells you how those scalars behave.

You can think of a field as: “a number system where you can add, subtract, multiply, and divide (except by 0), and the usual algebra works.”

Most linear algebra courses live over:

*   **ℝ** (real numbers), or
*   **ℂ** (complex numbers).

But the _definitions_ are built to work over any field 𝔽.

* * *

### 1) What is a scalar?

A **scalar** is just an element of some chosen set of “numbers” 𝔽 that we use to _scale_ things later.

Examples:

*   If 𝔽 = ℝ, scalars are real numbers like  $-3, 0, 2.7, \sqrt{2}$ .
*   If 𝔽 = ℂ, scalars are complex numbers like  $1+2i$ .

In linear algebra, scalars will become the coefficients  $\alpha_i$  in linear combinations like

$$
\alpha_1 v_1 + \cdots + \alpha_k v_k.
$$

So 0.1 is basically: what properties must the coefficients  $\alpha$  have for the whole theory to work cleanly?

* * *

### 2) Field axioms, from scratch (no hand-waving)

A **field** is a set  $\mathbb{F}$  together with two operations:

*   addition:  $+ : \mathbb{F}\times\mathbb{F}\to\mathbb{F}$ 
*   multiplication:  $\cdot : \mathbb{F}\times\mathbb{F}\to\mathbb{F}$ 

We write  $ab$  for  $a\cdot b$ .

Axioms come in three bundles: “addition behaves,” “multiplication behaves,” and “they interact nicely.”

#### A) Addition behaves like an abelian group

For all  $a,b,c \in \mathbb{F}$ :

1.  **Closure (addition)**:  $a+b \in \mathbb{F}$ .
2.  **Associativity**:  $(a+b)+c = a+(b+c)$ .
3.  **Commutativity**:  $a+b = b+a$ .
4.  **Additive identity**: there exists an element  $0\in\mathbb{F}$  such that  $a+0=a$ .
5.  **Additive inverse**: for each  $a$ , there exists  $-a$  such that  $a+(-a)=0$ .

This means you can always subtract:  $a-b := a+(-b)$ .

#### B) Multiplication behaves like an abelian group on nonzero elements

For all  $a,b,c \in \mathbb{F}$ :

6.  **Closure (multiplication)**:  $ab \in \mathbb{F}$ .
7.  **Associativity**:  $(ab)c = a(bc)$ .
8.  **Commutativity**:  $ab = ba$ .
9.  **Multiplicative identity**: there exists  $1\in\mathbb{F}$ ,  $1\neq 0$ , such that  $a\cdot 1 = a$ .
10.  **Multiplicative inverse**: for each  $a\neq 0$ , there exists  $a^{-1}\in\mathbb{F}$  such that  $a a^{-1}=1$ .

This is the “division works” axiom:  $a/b := a\cdot b^{-1}$  is defined whenever  $b\neq 0$ .

#### C) Addition and multiplication cooperate (distributive law)

11.  **Distributivity**:
    
$$
a(b+c) = ab + ac.
$$

(And it implies  $(a+b)c = ac + bc$  too, given commutativity of multiplication.)

That’s it. That’s the field contract.

* * *

### 3) Why linear algebra needs a field (not just any number system)

Linear algebra is about _linear combinations_, like:

$$
\alpha_1 v_1 + \cdots + \alpha_k v_k.
$$

To make this algebra sane, the scalars must allow:

*   **scaling** by any  $\alpha \in \mathbb{F}$ ,
*   **undoing a nonzero scale** by multiplying with  $\alpha^{-1}$ ,
*   **distribution** so scaling respects addition, i.e.  $\alpha(v+w)=\alpha v + \alpha w$ ,
*   solving equations like  $\alpha x = y$  when  $\alpha\neq 0$ .

That last one is _the_ hidden reason: linear algebra constantly reduces to equations of the form

$$
\alpha x = 0 \quad \Rightarrow \quad x = 0 \ \text{(when } \alpha\neq 0\text{)}.
$$

This implication uses inverses:

$$
\alpha x = 0,\ \alpha\neq 0 \ \Rightarrow\ \alpha^{-1}(\alpha x)=\alpha^{-1}0 \ \Rightarrow\ ( \alpha^{-1}\alpha)x = 0 \ \Rightarrow\ 1\cdot x = 0 \ \Rightarrow\ x=0.
$$

If inverses fail, a lot of “basic” linear algebra facts fail too.

* * *

### 4) Concrete examples: what counts, what doesn’t

#### Fields (good citizens)

*   **ℚ** (rationals): field.
*   **ℝ**: field.
*   **ℂ**: field.
*   **Finite fields**  $\mathbb{F}_p$  where  $p$  is prime: field (arithmetic mod  $p$ ).

#### Not fields (important non-examples)

*   **ℤ** (integers) is _not_ a field: 2 has no multiplicative inverse in ℤ (since  $1/2\notin \mathbb{Z}$ ).
*   ** $\mathbb{Z}_n$ ** (integers mod  $n$ ) is a field **only if  $n$  is prime**.  
    Example: mod 6,  $2\neq 0$  but  $2\cdot 3 = 0 \ (\text{mod }6)$ . That means nonzero things can multiply to zero (“zero divisors”), and inverses break.
*   **Matrices** are not a field under usual multiplication: not commutative, and most nonzero matrices are not invertible.

This matters because “linear algebra over ℤ” becomes a different subject (modules, Smith normal form), and many familiar theorems need modification.

* * *

### 5) The “minimal mental model” made precise

You wrote: scalars are “units of measurement” that stretch/shrink objects. That intuition is solid, but let’s pin down what the field axioms guarantee about “stretching.”

In any vector space (later), scalar multiplication is supposed to satisfy (among other things):

*    $1\cdot v = v$  (scaling by 1 changes nothing)
*    $0\cdot v = 0$  (scaling by 0 collapses to the zero vector)
*    $(\alpha\beta)\cdot v = \alpha\cdot(\beta\cdot v)$  (scales compose)
*    $(\alpha+\beta)\cdot v = \alpha\cdot v + \beta\cdot v$  (splitting coefficients works)

But these identities _lean on_ the scalar side behaving like a field, especially distributivity and inverses.

* * *

### 6) Tiny but crucial “field consequences” you’ll use constantly (proved cleanly)

These are not extra axioms; they follow from the field axioms. I’m proving them now because they become reflexes later.

#### Fact 1:  $0\cdot a = 0$  for all  $a\in\mathbb{F}$ 

Proof:

$$
0\cdot a = (0+0)\cdot a \quad \text{(since }0=0+0\text{)}
$$

Using distributivity:

$$
(0+0)\cdot a = 0\cdot a + 0\cdot a.
$$

So

$$
0\cdot a = 0\cdot a + 0\cdot a.
$$

Add the additive inverse of  $0\cdot a$  to both sides:

$$
0 = 0\cdot a.
$$

Done.

#### Fact 2: If  $a\neq 0$  and  $ab=0$ , then  $b=0$ 

Proof:  
If  $a\neq 0$ , then  $a^{-1}$  exists. Multiply both sides of  $ab=0$  by  $a^{-1}$ :

$$
a^{-1}(ab) = a^{-1}0.
$$

Associativity gives:

$$
(a^{-1}a)b = 0.
$$

But  $a^{-1}a=1$ , so:

$$
1\cdot b = 0 \Rightarrow b=0.
$$

Done.

This is the formal reason you can “divide by  $a$ ” in linear algebra proofs.

#### Fact 3: The multiplicative identity is unique; the additive identity is unique

Sketch (since it’s conceptually important, but repetitive):  
If  $1$  and  $1'$  are both multiplicative identities, then  $1 = 1\cdot 1' = 1'$ . Same idea for  $0$ .

Uniqueness matters because it prevents weird “multiple zeros” nonsense; the algebra is well-posed.

* * *

### 7) What you should be able to do after 0.1 (competency checklist)

You’re good on 0.1 when you can do these without vibes-based reasoning:

*   State exactly what a field is (set + two operations + axioms).
*   Explain why “division by nonzero scalars” is structurally required in linear algebra.
*   Give examples/non-examples and say _which axiom fails_ (e.g., ℤ fails inverses).
*   Use distributivity to prove small identities like  $0a=0$ ,  $(-1)a=-a$  (you can try proving this next), and the “no zero divisors” property above.

* * *

### 8) Bridge to 0.2 (so you see the arc)

0.1 built the coefficient universe  $\mathbb{F}$ . Next, 0.2 will build the idea of “structure + maps that respect structure.” Linear algebra will then be: a set  $V$  with operations compatible with  $\mathbb{F}$ , plus the maps  $T:V\to W$  that preserve those operations.

That’s the whole game: pick your scalars (0.1), define the structured objects (vector spaces), then study the structure-preserving maps (linear maps).

## Response:
Alright. We’ll take 0.1 and stretch it until it squeaks. The goal is not “I can repeat the definition of a field,” but “I can see exactly which later linear-algebra moves are secretly field moves, and which would break if we weakened the number system.”

I’ll proceed in a dependency-clean way:

1.  What “scalars” are (formally and operationally)
2.  Exact definition of a field, axiom by axiom, with “what this axiom buys you”
3.  Immediate derived laws (proved in full) that you will use constantly later
4.  Why “field” specifically (what breaks in rings, semirings, mod n with n composite, etc.)
5.  How ℝ and ℂ fit, and what changes over ℂ (conjugation / inner products later)
6.  Mental model: scaling, units, and “linearity” as “coefficient bookkeeping”
7.  A mini “failure museum” with explicit counterexamples

No web browsing is needed here; this is stable math.

* * *

0.1 — Scalars and fields (the coefficient universe)
---------------------------------------------------

### 0.1.0 What is a “scalar” really?

A “scalar” is not a magical kind of number. It’s simply:

*   an element of a chosen set  $\mathbb F$ ,
*   equipped with operations  $+$  and  $\cdot$ ,
*   that will act as _coefficients_ in expressions of the form
    $$
    \alpha_1 v_1 + \cdots + \alpha_k v_k,
    $$
    and will also define “scaling”:
    $$
    \alpha v.
    $$

So in linear algebra, “scalar” means “coefficient from the base number system.”

The key is: if your coefficient system is too weak, you can’t do many of the standard algebraic manipulations that power linear algebra (solving linear equations, Gaussian elimination, dimension arguments, etc.).

So we need to specify what properties  $\mathbb F$  must have.

* * *

0.1.1 The formal definition of a field
--------------------------------------

A **field**  $\mathbb F$  is a set with two binary operations:

*   addition:  $+\colon \mathbb F\times \mathbb F \to \mathbb F$ ,
*   multiplication:  $\cdot\colon \mathbb F\times \mathbb F \to \mathbb F$ ,

such that certain axioms hold. These axioms ensure that algebra behaves like the familiar arithmetic of rationals/reals/complex numbers.

It’s helpful to group axioms into three layers:

1.   $(\mathbb F, +)$  behaves like “numbers under addition.”
2.   $(\mathbb F\setminus\{0\}, \cdot)$  behaves like “nonzero numbers under multiplication.”
3.  multiplication distributes over addition (the bridge law).

Let’s state everything precisely.

* * *

### A) Additive structure:  $(\mathbb F,+)$  is an abelian group

For all  $a,b,c\in\mathbb F$ :

**(A1) Closure under addition.**  
 $a+b \in \mathbb F$ .

This prevents the operation from “escaping” the universe.

**(A2) Associativity of addition.**  
 $(a+b)+c = a+(b+c)$ .

This is what allows you to write  $a+b+c$  without parentheses ambiguity.

**(A3) Commutativity of addition.**  
 $a+b=b+a$ .

Order doesn’t matter for adding coefficients.

**(A4) Additive identity exists.**  
There exists  $0\in\mathbb F$  such that  $a+0=a$  for all  $a$ .

This gives a neutral element; later this becomes the scalar “0” used in linear combinations.

**(A5) Additive inverses exist.**  
For each  $a\in\mathbb F$ , there exists an element  $-a \in \mathbb F$  such that

$$
a+(-a) = 0.
$$

This is what makes subtraction legitimate:

$$
a-b := a+(-b).
$$

So: add/subtract is always allowed.

* * *

### B) Multiplicative structure:  $(\mathbb F\setminus\{0\},\cdot)$  is an abelian group

For all  $a,b,c\in\mathbb F$ :

**(M1) Closure under multiplication.**  
 $ab\in\mathbb F$ .

**(M2) Associativity of multiplication.**  
 $(ab)c = a(bc)$ .

This is what allows  $abc$  without parentheses ambiguity.

**(M3) Commutativity of multiplication.**  
 $ab=ba$ .

This is not strictly needed for _all_ of linear algebra (you can do linear algebra over division rings / skew fields), but standard linear algebra assumes commutative scalars. We’ll stick to fields, meaning commutative multiplication.

**(M4) Multiplicative identity exists.**  
There exists  $1\in\mathbb F$ , with  $1\neq 0$ , such that  $a\cdot 1 = a$  for all  $a$ .

**(M5) Multiplicative inverses exist for all nonzero elements.**  
For each  $a\in\mathbb F$  with  $a\neq 0$ , there exists  $a^{-1}\in\mathbb F$  such that

$$
a a^{-1} = 1.
$$

This is the core “division is possible” property:

$$
\frac{a}{b} := a b^{-1} \quad \text{(defined when }b\neq 0\text{).}
$$

So: multiply/divide by nonzero is always allowed.

* * *

### C) The bridge axiom: distributivity

**(D) Distributive law.**  
For all  $a,b,c\in\mathbb F$ :

$$
a(b+c) = ab + ac.
$$

Because multiplication is commutative, you also get  $(a+b)c = ac + bc$ , but the field definition typically states only one direction; the other follows.

Distributivity is what allows coefficient algebra to be consistent with “expanding linear combinations.”

* * *

0.1.2 What each axiom buys you later (in linear algebra terms)
--------------------------------------------------------------

This is the “why do we care” part, but I’ll make it mechanistic.

*   **Additive inverses** let you do elimination steps like “subtract row 2 from row 1.”
*   **Multiplicative inverses** let you normalize pivots: if pivot is  $p\neq 0$ , you can divide a row by  $p$  to make the pivot 1.
*   **Distributivity** is what makes matrix-vector multiplication behave like “linear combination of columns.”
*   **Associativity/commutativity** let you rearrange and regroup coefficients without changing meaning.

If you remove just one of these, you often still have some algebraic structure, but standard theorems become false or need heavy modification.

* * *

0.1.3 Derived laws you will use constantly (with full proofs)
-------------------------------------------------------------

These are “lemmas” you’ll use without thinking later. We’ll prove them now cleanly.

### Lemma 1:  $0\cdot a = 0$  for all  $a\in\mathbb F$ 

**Proof.**

Start from the fact that  $0$  is additive identity, so  $0 = 0+0$ .

Multiply both sides by  $a$ :

$$
0\cdot a = (0+0)\cdot a.
$$

Apply distributivity:

$$
(0+0)\cdot a = 0\cdot a + 0\cdot a.
$$

So

$$
0\cdot a = 0\cdot a + 0\cdot a.
$$

Now add the additive inverse of  $0\cdot a$  to both sides. Let  $x=0\cdot a$ . Then the equation is  $x = x + x$ .

Add  $-x$  to both sides:

$$
x + (-x) = (x+x)+(-x).
$$

Left side becomes  $0$ . Right side: use associativity:

$$
(x+x)+(-x) = x + (x + (-x)) = x + 0 = x.
$$

So  $0 = x$ . That is,  $0 = 0\cdot a$ . ∎

* * *

### Lemma 2:  $a\cdot 0 = 0$  for all  $a\in\mathbb F$ 

Same idea, or use commutativity:  $a\cdot 0 = 0\cdot a = 0$ . ∎

* * *

### Lemma 3:  $(-1)\cdot a = -a$  for all  $a\in\mathbb F$ 

This one is extremely useful later (it’s what makes “minus” behave normally).

**Proof.**

We know  $1 + (-1) = 0$  by definition of additive inverse of 1.

Multiply both sides by  $a$ :

$$
(1+(-1))a = 0a.
$$

Apply distributivity to left side:

$$
1a + (-1)a = 0a.
$$

But  $1a=a$  (multiplicative identity), and  $0a=0$  (Lemma 1). So:

$$
a + (-1)a = 0.
$$

But the definition of  $-a$  is: the unique element satisfying  $a + (-a) = 0$ .  
So  $(-1)a$  plays the role of  $-a$ . Hence  $(-1)a=-a$ . ∎

* * *

### Lemma 4: Cancellation law for addition

If  $a+c = b+c$ , then  $a=b$ .

**Proof.**

Add  $-c$  to both sides:

$$
(a+c)+(-c) = (b+c)+(-c).
$$

By associativity:

$$
a + (c+(-c)) = b + (c+(-c)).
$$

But  $c+(-c)=0$ , so:

$$
a+0 = b+0 \Rightarrow a=b.
$$

∎

You will use this constantly when simplifying coefficient equations.

* * *

### Lemma 5: Cancellation law for multiplication (nonzero factor)

If  $a\neq 0$  and  $ab=ac$ , then  $b=c$ .

**Proof.**

Since  $a\neq 0$ ,  $a^{-1}$  exists. Multiply both sides by  $a^{-1}$ :

$$
a^{-1}(ab) = a^{-1}(ac).
$$

Associativity gives:

$$
(a^{-1}a)b = (a^{-1}a)c.
$$

But  $a^{-1}a=1$ , so:

$$
1\cdot b = 1\cdot c \Rightarrow b=c.
$$

∎

This is exactly why you can “divide by a nonzero scalar.”

* * *

### Lemma 6: No zero divisors in a field

If  $ab=0$ , then  $a=0$  or  $b=0$ .

**Proof.**

Assume  $a\neq 0$ . Then  $a^{-1}$  exists. Multiply  $ab=0$  by  $a^{-1}$ :

$$
a^{-1}(ab)=a^{-1}0 \Rightarrow (a^{-1}a)b=0 \Rightarrow 1\cdot b=0 \Rightarrow b=0.
$$

So if  $a\neq 0$ , then  $b=0$ . Contrapositive gives the stated “either-or.” ∎

This “no zero divisors” property is why linear equations behave well.

* * *

### Lemma 7: Uniqueness of 0 and 1

If  $0$  and  $0'$  are both additive identities, then  $0=0'$ . Similarly for  $1$ .

**Proof for 0.**  
Because  $0$  is identity,  $0+0'=0'$ . Because  $0'$  is identity,  $0+0'=0$ . So  $0'=0$ . ∎

Same pattern for  $1$ . ∎

This matters because it ensures your algebra doesn’t depend on arbitrary choices.

* * *

0.1.4 Why fields, specifically? (what breaks if you weaken the scalars)
-----------------------------------------------------------------------

Many algebraic systems look “almost like” fields, but missing one feature. Here’s how linear algebra reacts.

### Case 1: Scalars are a ring but not a field (example:  $\mathbb Z$ )

 $\mathbb Z$  has addition/subtraction/multiplication with distributivity, but **no inverses for nonzero elements**.

What breaks?

*   You can’t divide a pivot by 2 during Gaussian elimination and stay in integers.
*   Equations like  $2x=1$  have no solution in  $\mathbb Z$ , even though  $2\neq 0$ .
*   Many dimension/rank arguments still exist but become subtler (module theory, not vector spaces).

So “linear algebra over  $\mathbb Z$ ” becomes “module theory,” not vector spaces.

### Case 2: Modulo arithmetic  $\mathbb Z_n$ 

*   If  $n$  is prime,  $\mathbb Z_n$  is a field  $\mathbb F_p$ . Great. Linear algebra works.
*   If  $n$  is composite,  $\mathbb Z_n$  is not a field: some nonzero elements have no inverses, and you get zero divisors.

Example in  $\mathbb Z_6$ :

$$
2\neq 0,\quad 3\neq 0,\quad 2\cdot 3 = 6 \equiv 0\ (\text{mod }6).
$$

So you have  $ab=0$  with  $a,b\neq 0$ . This destroys Lemma 6.

What does that do to linear algebra?

*   Elimination can fail because a nonzero pivot might not be invertible.
*   Equations can behave strangely; “rank” needs care.

### Case 3: Semirings (no subtraction), like  $\mathbb N$  with  $+$  and  $\cdot$ 

No additive inverses. So you can’t even do elimination steps that require subtraction. This is an entirely different world (tropical algebra, etc.).

So: for standard linear algebra, fields are the sweet spot where coefficient manipulation is clean.

* * *

0.1.5 ℝ vs ℂ: what changes later (important forward reference)
--------------------------------------------------------------

Both  $\mathbb R$  and  $\mathbb C$  are fields. So all algebra above holds.

But one big thing changes later when we talk about “dot products” / “inner products.”

Over  $\mathbb R$ , the usual inner product is:

$$
\langle x,y\rangle = x^\top y.
$$

Over  $\mathbb C$ , if you used  $x^\top y$  you get problems with positivity. The correct inner product uses **complex conjugation**:

$$
\langle x,y\rangle = x^* y = \sum_i \overline{x_i} y_i,
$$

where  $x^*$  is conjugate transpose.

That’s not part of 0.1 (fields), but it’s why linear algebra over ℂ has “Hermitian” instead of “symmetric,” etc.

So: 0.1 sets the scalar field; later geometry depends on the field too.

* * *

0.1.6 “Scaling” as the algebra of measurement units (making the intuition precise)
----------------------------------------------------------------------------------

Your mental model (“scalars are units that stretch/shrink”) is good, but let’s sharpen it:

When we later define vector spaces, scalar multiplication  $\alpha v$  must satisfy rules that mirror field rules. In fact, vector space axioms include:

*    $(\alpha+\beta)v = \alpha v + \beta v$  (distributivity over scalar addition)
*    $\alpha(u+v) = \alpha u + \alpha v$  (distributivity over vector addition)
*    $(\alpha\beta)v = \alpha(\beta v)$  (associativity of scaling)
*    $1v=v$  (identity scale)
*    $0v=0$  (collapse)

Notice: these are “field distributivity/associativity” mirrored into how scalars act on vectors.

So the field axioms are exactly what make “coefficient bookkeeping” consistent.

* * *

0.1.7 A “failure museum” (explicitly showing what breaks)
---------------------------------------------------------

Here are concrete mini-experiments that show why inverses and no-zero-divisors matter.

### Exhibit A: “Nonzero scalar times nonzero can equal zero” (zero divisors)

In  $\mathbb Z_6$ :

$$
2\cdot 3 \equiv 0.
$$

So the equation

$$
2x = 0
$$

has a nonzero solution:  $x=3$ .

In a field, Lemma 6 forbids this: if  $2\neq 0$ , then  $2x=0\Rightarrow x=0$ .

This property (that “scaling by nonzero never collapses something nonzero to zero”) is essential to many linear algebra proofs about independence and dimension.

### Exhibit B: “Pivot not invertible” breaks elimination

Try solving  $2x = 1$  in  $\mathbb Z_6$ . There is no  $x$  because 2 has no inverse mod 6 (since gcd(2,6)=2).

In a field, every nonzero pivot is invertible, so elimination always has a legal “divide by pivot” step.

* * *

0.1.8 The real punchline (what to internalize)
----------------------------------------------

When you later see statements like:

*   “Assume  $\alpha \neq 0$ , divide both sides by  $\alpha$ .”
*   “Scale a row to make the pivot 1.”
*   “If  $\sum \alpha_i v_i = 0$  and vectors are independent, conclude  $\alpha_i=0$ .”
*   “Multiply by inverse matrix / inverse scalar.”

You should hear a tiny voice: “field axiom M5 is being used here.”

That’s why 0.1 exists. It’s not ceremony; it’s the warranty that the algebraic moves you’re about to do are legal.

* * *

Micro-checklist (0.1 mastery)
-----------------------------

You truly “own” 0.1 when you can do these from memory:

1.  State the field definition (set + operations + axioms).
2.  Prove  $0a=0$ ,  $(-1)a=-a$ , cancellation, and “no zero divisors.”
3.  Explain exactly why  $\mathbb Z$  is not a field (missing inverses), and why  $\mathbb Z_p$  is a field iff  $p$  prime.
4.  Explain in one sentence: “Linear algebra needs division by nonzero scalars to make elimination and uniqueness arguments work.”

* * *

When you’re ready to continue, 0.2 will formalize the “structure + structure-preserving maps” viewpoint (groups → homomorphisms → vector spaces → linear maps). That’s where “linear” starts to mean something before pictures show up.

## Response:
Let’s drill deeper in a way that pays dividends later. The “field” layer is the hidden skeleton under: linear combinations, solving systems, rank/dimension, eigenvalues, determinants, orthogonality. If you really internalize 0.1, later topics stop feeling like a pile of tricks and start feeling inevitable.

I’ll expand in five directions:

1.  What a “structure” is, formally, and why axioms matter (meta-level clarity)
2.  Fields vs. near-misses: rings, integral domains, division rings (and exactly what each lets you do)
3.  A deeper set of “field consequences” you’ll repeatedly use (proved carefully)
4.  Concrete examples (ℚ, ℝ, ℂ, finite fields) plus “characteristic” and why it matters
5.  How the choice of field changes linear algebra (what statements remain true, what changes)

No vibes. Just clean logical plumbing.

* * *

0.1.A What axioms really are: “the rules of the game”
-----------------------------------------------------

Axioms are not “facts about numbers.” They’re the _definition_ of what we mean by a certain kind of system.

When we say “ $\mathbb F$  is a field,” we are not claiming we discovered a property of  $\mathbb F$ . We are declaring: “ $\mathbb F$  has operations  $+$  and  $\cdot$  satisfying these rules.”

Why do this? Because then every theorem you prove using only those rules automatically applies to:

*    $\mathbb R$ ,  $\mathbb C$ ,  $\mathbb Q$ ,
*   finite fields  $\mathbb F_p$ ,
*   any other field you meet later.

This is the “abstraction economy” of math: pay once (prove theorem from axioms), reuse forever.

* * *

0.1.B Field definition again, but with “what could go wrong” attached
---------------------------------------------------------------------

A field is a set  $\mathbb F$  with two operations  $+$  and  $\cdot$ .

The axioms are precisely the ones needed to make these two operations behave like arithmetic and to make “solving linear equations” behave predictably.

Key: there are two layers of invertibility.

*   Addition: every element has an additive inverse. So subtraction always works.
*   Multiplication: every **nonzero** element has a multiplicative inverse. So division by nonzero works.

The “nonzero” exception is not cosmetic: if 0 had a multiplicative inverse, you’d get a contradiction (I’ll prove that in a second).

* * *

0.1.C Foundational derived facts (deeper list, fully proved)
------------------------------------------------------------

Earlier we proved a few. Now I’ll build a richer “toolbox” of consequences that will quietly power later linear algebra manipulations.

### Lemma C1:  $0 \neq 1$  is necessary (not optional)

In the definition of a field we require  $0 \neq 1$ . Why?

If  $0 = 1$ , then for any  $a\in\mathbb F$ ,

$$
a = a\cdot 1 = a\cdot 0 = 0,
$$

so the entire set collapses to a single element. That “degenerate field” is useless; it destroys everything (no distinct scalars).

So we explicitly exclude it.

* * *

### Lemma C2: 0 cannot have a multiplicative inverse in any nontrivial ring/field

Assume for contradiction that there exists  $x$  with  $0\cdot x = 1$ . But we proved  $0\cdot x = 0$ . So  $0=1$ , contradicting nontriviality. Done.

So “divide by 0” is not merely disallowed by convention; it is structurally impossible if you want consistent algebra.

* * *

### Lemma C3: Additive inverse is unique; multiplicative inverse is unique

This matters later when you talk about “the” inverse, not “an” inverse.

Additive inverse uniqueness:  
Suppose  $b$  and  $c$  both satisfy  $a+b=0$  and  $a+c=0$ .  
Then:

$$
b = b + 0 = b + (a+c) = (b+a)+c = (a+b)+c = 0+c = c.
$$

So  $b=c$ .

Multiplicative inverse uniqueness (for  $a\neq 0$ ):  
If  $ab=1$  and  $ac=1$ , then

$$
b = b\cdot 1 = b(ac) = (ba)c = 1\cdot c = c,
$$

using associativity and commutativity (or just associativity plus careful ordering). So unique.

* * *

### Lemma C4:  $-(-a) = a$ 

Proof:  
By definition,  $-a$  satisfies  $a+(-a)=0$ .  
Now  $-(-a)$  is defined as the additive inverse of  $(-a)$ , so:

$$
(-a) + (-(-a)) = 0.
$$

But also  $ (-a) + a = 0$  (since addition is commutative and  $a+(-a)=0$ ).  
By uniqueness of additive inverse of  $(-a)$ , we must have  $-(-a)=a$ .

* * *

### Lemma C5:  $-(a+b) = (-a)+(-b)$ 

Proof:  
We must show  $(a+b) + [(-a)+(-b)] = 0$ .  
Compute:

$$
(a+b)+((-a)+(-b)) = (a+(-a)) + (b+(-b)) = 0+0=0,
$$

using associativity and commutativity. Then uniqueness of additive inverse gives the claim.

This is one of the algebraic moves behind simplifying linear combinations later.

* * *

### Lemma C6:  $(-a)b = -(ab)$  and  $a(-b)=-(ab)$ 

Proof:  
We show  $(-a)b$  is the additive inverse of  $ab$ .  
Compute:

$$
ab + (-a)b = (a+(-a))b = 0\cdot b = 0,
$$

where we used distributivity and Lemma  $0\cdot b=0$ .  
So indeed  $(-a)b = -(ab)$ . Similarly for  $a(-b)$ .

* * *

### Lemma C7:  $(-a)(-b)=ab$ 

Proof:  
Using Lemma C6 twice:

$$
(-a)(-b) = -\big(a(-b)\big) = -\big(-(ab)\big) = ab,
$$

because  $-(-x)=x$  (Lemma C4).

* * *

### Lemma C8: If  $a\neq 0$ , then  $a^{-1}\neq 0$ 

Proof:  
If  $a^{-1}=0$ , then  $1 = aa^{-1} = a\cdot 0 = 0$ , contradiction. So  $a^{-1}\neq 0$ .

* * *

### Lemma C9: Solving a one-variable linear equation is always possible and unique

Take  $a,b\in\mathbb F$  with  $a\neq 0$ . Consider:

$$
ax=b.
$$

Existence: Let  $x = a^{-1}b$ . Then:

$$
a(a^{-1}b) = (aa^{-1})b = 1\cdot b = b.
$$

Uniqueness: If  $ax=b$  and  $ay=b$ , then  $ax=ay$ . Since  $a\neq 0$ , cancellation (multiply by  $a^{-1}$ ) gives  $x=y$ .

So: in a field, every nonzero coefficient equation  $ax=b$  has a unique solution.

This is the microscopic engine behind Gaussian elimination.

* * *

0.1.D Why “field” is exactly the right strength for standard linear algebra
---------------------------------------------------------------------------

Now let’s classify “nearby” structures and spell out exactly what breaks when you weaken.

### 1) Ring

A ring has  $+$  like an abelian group, and multiplication associative + distributive, and usually has 1, but not every nonzero element is invertible.

Example:  $\mathbb Z$ .

What you can still do:

*   Add/subtract freely.
*   Multiply and distribute.

What you cannot guarantee:

*   Division by nonzero.
*   Pivot normalization in elimination while staying inside the ring.
*   Certain dimension arguments that rely on “if  $\alpha\neq 0$  then  $\alpha v=0 \Rightarrow v=0$ ” (this can fail in rings with zero divisors).

So “vector spaces over a ring” are not vector spaces; they’re modules. Beautiful, but different.

### 2) Integral domain

A commutative ring with 1 and **no zero divisors**.

Example:  $\mathbb Z$  is an integral domain.

Good news:

*   If  $ab=0$ , then  $a=0$  or  $b=0$ . So you regain the “no collapsing by nonzero multiplication” property.

Bad news:

*   Still no division by arbitrary nonzero elements. You can’t solve  $2x=1$  in  $\mathbb Z$ .

So you get a partial linear algebra, but elimination isn’t “always legal.”

### 3) Division ring (skew field)

Every nonzero element is invertible, but multiplication may be noncommutative.

Example: quaternions  $\mathbb H$ .

Linear algebra can be done over division rings, but:

*   you must distinguish left vs right scalar multiplication,
*   determinants/eigenvalues get subtler.

Standard introductory linear algebra avoids this and assumes commutativity, i.e., fields.

So: **fields** are the clean “just enough structure” so linear algebra is robust and uniform.

* * *

0.1.E Deeper examples: finite fields, characteristic, and why it matters
------------------------------------------------------------------------

Most people only see  $\mathbb R$  and  $\mathbb C$ , but linear algebra over finite fields is a huge part of coding theory, cryptography, combinatorics, algorithms. And it reveals which theorems are truly “field theorems” vs “real-geometry theorems.”

### E1: Finite fields  $\mathbb F_p$  for prime  $p$ 

Define  $\mathbb F_p = \{0,1,2,\dots,p-1\}$  with addition and multiplication mod  $p$ .

Why is it a field when  $p$  is prime?

The key is: every nonzero element has an inverse mod  $p$ . Concretely, for any  $a\in\{1,\dots,p-1\}$ , there exists  $b$  with:

$$
ab \equiv 1 \pmod p.
$$

Sketch of why (core idea):

*   Consider the multiples  $a,2a,3a,\dots,(p-1)a$  mod  $p$ .
*   If  $ia \equiv ja \pmod p$  with  $i\neq j$ , then  $p\mid (i-j)a$ .
*   Since  $p$  is prime and  $a\neq 0$ ,  $p\nmid a$ , so  $p\mid (i-j)$ , impossible for  $1\le i-j\le p-2$ .
*   So the multiples are all distinct nonzero residues, hence they form a permutation of  $\{1,\dots,p-1\}$ .
*   In particular,  $1$  appears among them:  $ka\equiv 1$ . Then  $k$  is  $a^{-1}$ .

That argument is the “finite field inverse existence” engine.

When  $n$  is composite, this fails because you can have zero divisors.

### E2: Characteristic of a field

This is conceptually important because it changes certain identities.

In a field  $\mathbb F$ , consider:

$$
1,\quad 1+1,\quad 1+1+1,\quad \dots
$$

If there exists a smallest positive integer  $p$  such that

$$
\underbrace{1+1+\cdots+1}_{p\text{ times}} = 0,
$$

then the field has **characteristic  $p$ **.

If no such  $p$  exists, the field has characteristic 0.

Facts (very important, and true):

*    $\mathbb Q,\mathbb R,\mathbb C$  have characteristic 0.
*    $\mathbb F_p$  has characteristic  $p$ .
*   The characteristic of a field is either 0 or a prime.

Why must it be prime? If char is  $n$  and  $n=ab$  composite, then:

$$
0 = n\cdot 1 = (ab)\cdot 1 = (a\cdot 1)(b\cdot 1),
$$

but neither  $a\cdot 1$  nor  $b\cdot 1$  is 0 if  $n$  is minimal, giving zero divisors—impossible in a field. So  $n$  must be prime.

Why this matters for linear algebra:

*   Over char  $p$ , you have  $p=0$  inside the scalar system. So coefficients behave differently (e.g.,  $2=-1$  in  $\mathbb F_3$ ).
*   Geometry-based intuitions from  $\mathbb R$  can mislead (no ordering, no “positive” notion).

But algebraic linear algebra (span, dimension, rank-nullity) still works beautifully because it’s field-based, not order-based.

* * *

0.1.F How the choice of field changes linear algebra (a precise separation)
---------------------------------------------------------------------------

There are two “flavors” of linear algebra statements:

1.  Purely algebraic statements: depend only on field axioms.
2.  Geometric/analytic statements: require extra structure like an order (ℝ) or completeness, or an inner product.

Let me be explicit.

### F1: Statements true over any field (pure field-linear algebra)

These rely only on addition, multiplication, inverses, distributivity.

*   Definition and properties of vector spaces (once defined over a field)
*   Subspaces, span, linear independence
*   Basis existence, uniqueness of coordinates relative to a basis
*   Dimension is well-defined; all bases have same size
*   Rank-nullity theorem
*   Gaussian elimination works (over a field) and yields RREF
*   Determinant can be defined and has multiplicativity (for commutative fields)
*   Eigenvalues exist in an algebraic closure sometimes; but diagonalization statements depend on polynomial splitting

These are the “field-native” theorems.

### F2: Statements that depend on ℝ (order / positivity) or ℂ with conjugation

*   Inequalities like “ $\|x\|\ge 0$ ” require a notion of positivity (over ℝ), or at least a _positive definite inner product_ (over ℂ uses conjugate).
*   “Angles” and “orthogonality” require an inner product structure, not just a field.
*   Concepts like “length,” “distance,” “least squares minimization” need norms/inner products and often completeness/analysis for deeper results.

So: 0.1 sets the algebraic bedrock; 2.x sets the geometric bedrock.

This separation is crucial. It prevents you from mixing “algebra truths” with “real-geometry intuitions” accidentally.

* * *

0.1.G A more precise mental model of “scalars as measurement units”
-------------------------------------------------------------------

“Scalar as unit” is a metaphor; here’s the exact mathematical content behind it.

A scalar  $\alpha$  is something you can:

*   add with other scalars to combine coefficients,
*   multiply with scalars to compose rescalings,
*   invert (if nonzero) to undo a rescaling,
*   distribute over sums to keep “linear” behavior coherent.

That’s exactly what “units” do in measurement:

*   multiplying by 2 doubles,
*   multiplying by 1/2 halves,
*   multiplying by 0 annihilates,
*   multiplication composes: doubling then tripling equals multiplying by 6.

The field axioms are the abstract statement that “rescaling behaves consistently.”

Later, the axioms of a vector space essentially say:  
“Vectors form an additive abelian group, and scalars act on vectors in a way compatible with the scalar field laws.”

So 0.1 is: define the coefficient universe.  
Then 1.x is: define the objects the scalars act on.

* * *

0.1.H A clean “why division matters” argument, tied directly to linear independence
-----------------------------------------------------------------------------------

One of the earliest deep uses of “fieldness” is the idea that scaling by a nonzero scalar is injective.

### Proposition H1: In a field, the map  $m_\alpha:\mathbb F\to\mathbb F$  given by  $m_\alpha(x)=\alpha x$  is injective if  $\alpha\neq 0$ 

Proof:  
Assume  $\alpha x=\alpha y$ . Then  $\alpha(x-y)=0$ . Since  $\alpha\neq 0$ , Lemma “no zero divisors” implies  $x-y=0$ , so  $x=y$ .

This injectivity is what makes “unique coordinates” and “independence” behave properly later.

If you lose inverses or get zero divisors, this injectivity can fail, and independence becomes weird.

* * *

0.1.I Failure museum, expanded (more explicit and instructive)
--------------------------------------------------------------

### Exhibit I1: In  $\mathbb Z_6$ , nonzero scaling can kill a nonzero element

We saw:

$$
2\cdot 3 \equiv 0 \pmod 6.
$$

So the equation  $2x=0$  has a nonzero solution  $x=3$ . This means the “scaling map”  $m_2(x)=2x$  is not injective. That breaks many proofs that assume injectivity of nonzero scaling.

### Exhibit I2: Elimination step “divide by pivot” can be illegal

Over  $\mathbb Z$ , try solving  $2x=1$ . Elimination would say “divide by 2,” but  $1/2\notin \mathbb Z$ . So you can’t stay inside  $\mathbb Z$ .

Over  $\mathbb F_5$ , you can. Because 2 has an inverse mod 5, which is 3 (since  $2\cdot 3=6\equiv 1$ ).

So whether elimination is universally legal depends on the field axiom “every nonzero has inverse.”

* * *

0.1.J What you should memorize vs what you should _understand_
--------------------------------------------------------------

Memorize:

*   “Field = commutative ring with 1 where every nonzero element is invertible.”
*   The list of axioms (at least conceptually grouped).

Understand deeply (this is the point):

*   Every time you “divide by a coefficient,” “normalize a pivot,” or argue uniqueness by cancellation, you are using multiplicative inverses.
*   Every time you expand  $\alpha(u+v)$  into  $\alpha u + \alpha v$ , you’re using distributivity.
*   The clean behavior of “linear combinations” depends on this coefficient algebra being well-behaved.

* * *

0.1.K Super-short forward hook to 0.2 (to keep the roadmap coherent)
--------------------------------------------------------------------

0.1 gave us the coefficient universe  $\mathbb F$ .

0.2 will formalize the pattern:

*   You have a set with some operations = “structure.”
*   You care about maps that preserve those operations.

Then “linear algebra” becomes:

*   vector spaces = sets with addition + scalar multiplication compatible with  $\mathbb F$ ,
*   linear maps = functions that preserve those operations.

So 0.1 is: define the scalar structure.  
0.2 is: define “structure-preserving maps” in general, so “linear map” later feels like a special case of a universal idea.

If you want to make 0.2 feel inevitable, 0.1 is the “choose your scalars” step.

That’s the deeper story.

## Response:
0.2 Functions and structure-preserving maps (proto–linear algebra)
------------------------------------------------------------------

0.1 chose the **scalar universe**  $\mathbb F$ .  
0.2 explains the _meta-pattern_ that will generate linear algebra:

You don’t study sets as raw piles of elements. You study sets **with structure**, and the functions that **respect** that structure.

Linear algebra is just one instance of this general idea:

*   the structured sets are **vector spaces**,
*   the structure-preserving functions are **linear maps**.

We’ll build that pattern from absolute basics.

* * *

### 0.2.1 What is a “set with structure”?

A **set**  $S$  by itself is just “things.” No operations, no rules.

A **structure** on a set is typically given by specifying one or more operations, relations, or distinguished elements that you promise satisfy certain axioms.

The most common kind of structure (and the one we need) is **algebraic structure**: operations that take elements of the set and return elements of the set.

#### A) Operations (the main kind we care about)

An ** $n$ \-ary operation** on a set  $S$  is a function

$$
\omega : S^n \to S.
$$

Examples:

*   Binary operation:  $S\times S\to S$  (like  $+$  or  $\cdot$ ).
*   Unary operation:  $S\to S$  (like  $x\mapsto -x$ ).
*   Nullary operation: a chosen element (like identity  $e$  or  $0$ ); formally it’s a function from a one-point set  $\{\ast\}\to S$ .

So “a set with structure” often means:

*   a set  $S$ ,
*   plus one or more operations  $\omega_1,\dots,\omega_k$ ,
*   plus axioms those operations satisfy.

#### B) Relations (less central for now)

A relation is something like  $\le$  on  $\mathbb R$ . That’s structure too, but linear algebra’s core is about operations, not order.

* * *

### 0.2.2 Homomorphisms: the core idea of “preserving structure”

Once you have structure, the natural next question is:

Which functions between structured sets **respect** the structure?

That’s the birth of “homomorphism.”

#### Definition (informal but accurate)

A function  $f:S\to T$  is structure-preserving if applying the structure then mapping equals mapping then applying the structure.

Concretely: if  $S$  and  $T$  both have a binary operation  $\star$ , then we want

$$
f(x\star_S y) = f(x)\star_T f(y) \quad \forall x,y\in S.
$$

That equation is the _prototype_ of linearity.

You should see it as a commuting diagram idea:

*   Combine inside  $S$ , then map to  $T$ ,
*   or map each piece to  $T$ , then combine inside  $T$ ,
*   same result.

This is the “don’t mess up the algebra” constraint.

* * *

### 0.2.3 First real example: groups and group homomorphisms

We’re not doing group theory for its own sake. We’re using it as the simplest “structure + structure-preserving maps” template.

#### Definition: group

A **group**  $(G,\circ)$  is a set  $G$  with a binary operation  $\circ : G\times G\to G$  such that:

1.  Associativity:  $(a\circ b)\circ c = a\circ(b\circ c)$ 
2.  Identity:  $\exists e\in G$  s.t.  $e\circ a=a\circ e=a$ 
3.  Inverses:  $\forall a\in G$ ,  $\exists a^{-1}$  s.t.  $a\circ a^{-1}=a^{-1}\circ a=e$ 

If also  $a\circ b=b\circ a$ , it’s an **abelian group**.

Examples:

*    $(\mathbb Z,+)$  is an abelian group.
*    $(\mathbb R,+)$  is an abelian group.
*   Nonzero reals  $(\mathbb R\setminus\{0\},\cdot)$  is an abelian group.

#### Definition: group homomorphism

A function  $\varphi:(G,\circ)\to(H,\bullet)$  is a **group homomorphism** if

$$
\varphi(a\circ b)=\varphi(a)\bullet\varphi(b)\quad \forall a,b\in G.
$$

That single equation is the whole definition.

##### What does it force?

A lot. For example:

**Proposition 1: homomorphisms send identity to identity.**  
If  $\varphi:G\to H$  is a group homomorphism, then  $\varphi(e_G)=e_H$ .

Proof:

$$
\varphi(e_G)=\varphi(e_G\circ e_G)=\varphi(e_G)\bullet \varphi(e_G).
$$

Now “cancel”  $\varphi(e_G)$  on the left in the group  $H$ : multiply by  $\varphi(e_G)^{-1}$  to get  $e_H=\varphi(e_G)$ . (Cancellation is valid because  $H$  is a group.) ∎

**Proposition 2: homomorphisms send inverses to inverses.**

$$
\varphi(a^{-1})=\varphi(a)^{-1}.
$$

Proof:

$$
e_H = \varphi(e_G)=\varphi(a\circ a^{-1})=\varphi(a)\bullet\varphi(a^{-1}),
$$

so  $\varphi(a^{-1})$  is the inverse of  $\varphi(a)$ . ∎

So one structural equation gives strong consequences.

This is exactly what will happen with linear maps later: from two equations you’ll get dozens of useful identities “for free.”

* * *

### 0.2.4 The pattern you should extract (this is the whole point)

A “good” map is defined by preserving the operations.

*   Group: 1 operation  $\circ$  → homomorphism preserves  $\circ$ .
*   Ring: two operations  $+$ ,  $\cdot$  → ring homomorphism preserves both.
*   Vector space: operations  $+$  and “scalar multiplication by  $\alpha$ ” → linear map preserves both.

So linear maps are not random. They’re _the homomorphisms of vector spaces._

* * *

### 0.2.5 From fields to vector spaces: why we needed 0.1 first

A vector space  $V$  (later) has:

*   addition  $V\times V\to V$ ,
*   scalar multiplication  $\mathbb F\times V\to V$ .

So we must already know what  $\mathbb F$  is and how it behaves. That was 0.1.

You can already guess the “structure-preserving map” definition now:

A function  $T:V\to W$  is linear if it preserves:

1.  addition in  $V$ ,
2.  scalar multiplication by any  $\alpha\in\mathbb F$ .

That becomes:

$$
T(u+v)=T(u)+T(v),\qquad T(\alpha v)=\alpha T(v).
$$

That is exactly the homomorphism pattern.

* * *

### 0.2.6 Linearity can be compressed into one master rule

The two rules above imply a stronger “finite linear combination” rule, and it’s worth proving now because it will become your reflex.

#### Proposition (linearity ⇔ preserving all finite linear combinations)

If  $T:V\to W$  satisfies

$$
T(u+v)=T(u)+T(v),\qquad T(\alpha v)=\alpha T(v),
$$

then for any vectors  $v_1,\dots,v_k\in V$  and scalars  $\alpha_1,\dots,\alpha_k\in\mathbb F$ ,

$$
T\Big(\sum_{i=1}^k \alpha_i v_i\Big)=\sum_{i=1}^k \alpha_i T(v_i).
$$

Proof (fully explicit):  
We prove by induction on  $k$ .

Base  $k=1$ :

$$
T(\alpha_1 v_1)=\alpha_1 T(v_1)
$$

holds by scalar rule.

Inductive step: assume true for  $k-1$ . Consider  $k$ :

$$
T\Big(\sum_{i=1}^k \alpha_i v_i\Big) = T\Big(\big(\sum_{i=1}^{k-1}\alpha_i v_i\big) + \alpha_k v_k\Big).
$$

Apply additivity:

$$
= T\Big(\sum_{i=1}^{k-1}\alpha_i v_i\Big) + T(\alpha_k v_k).
$$

Apply induction hypothesis to the first term, and scalar rule to the second:

$$
= \sum_{i=1}^{k-1}\alpha_i T(v_i) + \alpha_k T(v_k) = \sum_{i=1}^{k}\alpha_i T(v_i).
$$

Done. ∎

This tells you what linear maps _really do_: they “pull through” linear combinations.

* * *

### 0.2.7 Two common traps (and why 0.2 prevents them)

#### Trap A: confusing “any function” with “structure-respecting function”

Most functions  $f:\mathbb R^n\to\mathbb R^m$  are not linear.

Example:  $f(x)=x^2$  (componentwise) fails additivity:

$$
(1+1)^2 = 4 \neq 2 = 1^2+1^2.
$$

So “linear” is a very specific constraint: it says the function respects the algebra of combination.

#### Trap B: thinking linear algebra is “about matrices”

Matrices come later as _representations_ of linear maps after choosing bases.

The real objects are:

*   vector spaces (structured sets),
*   linear maps (structure-preserving maps).

0.2 is the conceptual move that makes that feel natural instead of philosophical fluff.

* * *

### 0.2.8 What you must be able to do after 0.2

You’ve mastered 0.2 when you can:

*   Define “structure” as operations/axioms on a set.
*   Define “structure-preserving” map as “operation commutes with mapping.”
*   Give the group example and derive: identity maps to identity; inverses map to inverses.
*   State linearity as the vector-space homomorphism condition:
    $$
    T(u+v)=T(u)+T(v),\quad T(\alpha v)=\alpha T(v).
    $$
*   Prove the “preserves any finite linear combination” identity via induction.

* * *

That completes 0.2 in the same “no gaps” style. The next step in your roadmap is 1.1 (construct  $\mathbb R^n$  explicitly and prove it behaves like a vector space), where we finally introduce vectors—but now “linear” already has a meaning: “preserves the operations.”

## Response:
1.1 Start with  $\mathbb R^n$  as a concrete model (and prove it is a vector space)
-----------------------------------------------------------------------------------

We’re going to build  $\mathbb R^n$  from the ground up, define its operations with zero ambiguity, then verify every vector-space axiom carefully. This is the “training ground” where everything is explicit and calculable. Later, when we define _abstract_ vector spaces, you’ll recognize the same pattern.

I’ll be annoyingly precise about: what the set is, what the operations are, what equality means, what needs to be proved, and where we use properties of  $\mathbb R$  from 0.1.

* * *

### 1.1.0 What is  $\mathbb R^n$ , really?

Fix a positive integer  $n\in\mathbb N$  (so  $n=1,2,3,\dots$ ).

#### Definition (as a set of functions)

A very clean, foundational definition is:

$$
\mathbb R^n := \{x \mid x:\{1,2,\dots,n\}\to \mathbb R\}.
$$

That is: an element  $x\in\mathbb R^n$  is a function that assigns to each index  $i\in\{1,\dots,n\}$  a real number  $x(i)$ .

We usually write  $x_i$  instead of  $x(i)$ , so an  $x\in\mathbb R^n$  can be written as an  $n$ \-tuple:

$$
x=(x_1,\dots,x_n).
$$

This definition matters because it makes it obvious how to define operations **componentwise**: do the scalar operation in  $\mathbb R$  at each index.

#### Equality in  $\mathbb R^n$ 

Two vectors  $x,y\in\mathbb R^n$  are equal iff they are equal as functions:

$$
x=y \quad \Longleftrightarrow\quad \forall i\in\{1,\dots,n\},\ x_i=y_i.
$$

This is a crucial “how you prove equality” rule: **show all components match**.

* * *

### 1.1.1 Define the operations on  $\mathbb R^n$ 

To make  $\mathbb R^n$  into a vector space over  $\mathbb R$ , we need:

1.  vector addition:  $\mathbb R^n\times \mathbb R^n\to\mathbb R^n$ 
2.  scalar multiplication:  $\mathbb R\times\mathbb R^n\to\mathbb R^n$ 

We define both componentwise using the field operations of  $\mathbb R$ .

#### Definition: Addition

For  $x=(x_1,\dots,x_n)$  and  $y=(y_1,\dots,y_n)$ , define  $x+y\in\mathbb R^n$  by:

$$
(x+y)_i := x_i + y_i \quad \text{for each } i=1,\dots,n.
$$

We must check this is well-defined: the right-hand side  $x_i+y_i$  is a real number, and  $\mathbb R$  is closed under addition, so  $(x+y)_i\in\mathbb R$  for each  $i$ , hence  $x+y\in\mathbb R^n$ .

#### Definition: Scalar multiplication

For  $\alpha\in\mathbb R$  and  $x\in\mathbb R^n$ , define  $\alpha x\in\mathbb R^n$  by:

$$
(\alpha x)_i := \alpha x_i \quad \text{for each } i=1,\dots,n.
$$

Again well-defined because  $\mathbb R$  is closed under multiplication.

So the rule is: **everything is done coordinate-by-coordinate inside the field  $\mathbb R$ **.

* * *

1.1.2 The goal: prove  $\mathbb R^n$  is a vector space over  $\mathbb R$ 
--------------------------------------------------------------------------

Now we need the formal axioms. A vector space  $V$  over a field  $\mathbb F$  is a set with two operations satisfying 8 axioms. Here  $V=\mathbb R^n$  and  $\mathbb F=\mathbb R$ .

I’ll list the axioms first, then prove each one in a componentwise way, explicitly saying what property of  $\mathbb R$  we use.

### Vector space axioms (over  $\mathbb R$ )

For all  $x,y,z\in\mathbb R^n$  and all scalars  $\alpha,\beta\in\mathbb R$ :

**(V1) Closure under addition:**  $x+y\in\mathbb R^n$ .  
**(V2) Commutativity of addition:**  $x+y=y+x$ .  
**(V3) Associativity of addition:**  $(x+y)+z=x+(y+z)$ .  
**(V4) Additive identity exists:** there exists  $0\in\mathbb R^n$  s.t.  $x+0=x$ .  
**(V5) Additive inverses exist:** for each  $x$ , there exists  $-x$  s.t.  $x+(-x)=0$ .  
**(V6) Compatibility of scalar multiplication:**  $\alpha(\beta x)=(\alpha\beta)x$ .  
**(V7) Identity scalar:**  $1x=x$ .  
**(V8) Distributive laws:**

*    $\alpha(x+y)=\alpha x+\alpha y$ 
*    $(\alpha+\beta)x=\alpha x+\beta x$ 

We will prove all eight.

The structure of all proofs will be:

To prove two vectors are equal, prove their components are equal for each  $i$ .

* * *

1.1.3 Proofs of axioms (full, explicit)
---------------------------------------

### (V1) Closure under addition

Take any  $x,y\in\mathbb R^n$ . By definition,  $(x+y)_i=x_i+y_i\in\mathbb R$  because  $\mathbb R$  is closed under addition. So every component of  $x+y$  is real, hence  $x+y\in\mathbb R^n$ . ∎

(You can think: addition is defined so closure is basically built in.)

* * *

### (V2) Commutativity of addition

We want to show  $x+y=y+x$ . By componentwise equality, it suffices to show:

$$
(x+y)_i=(y+x)_i\quad \forall i.
$$

Compute:

$$
(x+y)_i=x_i+y_i,\qquad (y+x)_i=y_i+x_i.
$$

But addition in  $\mathbb R$  is commutative:  $x_i+y_i=y_i+x_i$ . So components match, so vectors are equal. ∎

* * *

### (V3) Associativity of addition

We want  $(x+y)+z=x+(y+z)$ . Check component  $i$ :

$$
((x+y)+z)_i=(x+y)_i+z_i=(x_i+y_i)+z_i.
$$

Also,

$$
(x+(y+z))_i=x_i+(y+z)_i=x_i+(y_i+z_i).
$$

But addition in  $\mathbb R$  is associative:

$$
(x_i+y_i)+z_i = x_i+(y_i+z_i).
$$

So all components match; hence the vectors are equal. ∎

* * *

### (V4) Additive identity exists

We must exhibit a vector  $0\in\mathbb R^n$  such that  $x+0=x$  for all  $x$ .

Define:

$$
0 := (0,0,\dots,0)\in\mathbb R^n,
$$

where each component is the real number  $0\in\mathbb R$ .

Now check:

$$
(x+0)_i = x_i + 0.
$$

In  $\mathbb R$ ,  $x_i+0=x_i$  (additive identity property). Hence  $(x+0)_i=x_i$  for all  $i$ , so  $x+0=x$ . ∎

Note: we also get  $0+x=x$  automatically by commutativity.

* * *

### (V5) Additive inverses exist

Given  $x\in\mathbb R^n$ , we must find a vector  $-x$  such that  $x+(-x)=0$ .

Define:

$$
-x := (-x_1,\dots,-x_n).
$$

This is in  $\mathbb R^n$  because each  $-x_i\in\mathbb R$ .

Now check:

$$
(x+(-x))_i = x_i + (-x_i) = 0
$$

because  $-x_i$  is the additive inverse of  $x_i$  in  $\mathbb R$ .

So  $x+(-x)$  has every component equal to 0, hence  $x+(-x)=0$ . ∎

* * *

### (V6) Compatibility of scalar multiplication

We want:

$$
\alpha(\beta x) = (\alpha\beta)x.
$$

Check component  $i$ :

$$
(\alpha(\beta x))_i = \alpha(\beta x)_i = \alpha(\beta x_i).
$$

On the other hand:

$$
((\alpha\beta)x)_i = (\alpha\beta)x_i.
$$

But multiplication in  $\mathbb R$  is associative:

$$
\alpha(\beta x_i) = (\alpha\beta)x_i.
$$

So all components match. ∎

* * *

### (V7) Identity scalar

We want  $1x=x$ .

Check component  $i$ :

$$
(1x)_i = 1\cdot x_i = x_i
$$

because 1 is multiplicative identity in  $\mathbb R$ . Hence  $1x=x$ . ∎

* * *

### (V8a) Distributivity over vector addition

We want:

$$
\alpha(x+y)=\alpha x+\alpha y.
$$

Check component  $i$ :

Left side:

$$
(\alpha(x+y))_i = \alpha(x+y)_i = \alpha(x_i+y_i).
$$

Right side:

$$
(\alpha x+\alpha y)_i = (\alpha x)_i + (\alpha y)_i = \alpha x_i + \alpha y_i.
$$

But distributivity in  $\mathbb R$  says:

$$
\alpha(x_i+y_i)=\alpha x_i + \alpha y_i.
$$

So components match; vectors equal. ∎

* * *

### (V8b) Distributivity over scalar addition

We want:

$$
(\alpha+\beta)x=\alpha x+\beta x.
$$

Check component  $i$ :

Left:

$$
((\alpha+\beta)x)_i = (\alpha+\beta)x_i.
$$

Right:

$$
(\alpha x+\beta x)_i = \alpha x_i + \beta x_i.
$$

Distributivity in  $\mathbb R$  says:

$$
(\alpha+\beta)x_i=\alpha x_i+\beta x_i.
$$

So vectors equal. ∎

* * *

### Conclusion

We verified all axioms, so:

$$
\boxed{\mathbb R^n\ \text{with componentwise addition and scalar multiplication is a vector space over }\mathbb R.}
$$

* * *

1.1.4 Important “derived facts” in  $\mathbb R^n$  (proved, not assumed)
------------------------------------------------------------------------

Now that we have axioms, there are consequences you will use constantly. These are worth proving now because they become “automatic moves” later.

### Fact A: The zero vector is unique

Suppose  $0$  and  $0'$  both satisfy  $x+0=x$  and  $x+0'=x$  for all  $x$ . Take  $x=0'$ :

$$
0' + 0 = 0' \quad \text{(by identity property of }0),
$$

but also:

$$
0' + 0 = 0 \quad \text{(because }0'\text{ is identity, so }0'+0=0).
$$

Thus  $0'=0$ . ∎

So “the” zero vector is well-defined.

### Fact B: Additive inverse is unique

If  $y$  and  $z$  both satisfy  $x+y=0$  and  $x+z=0$ , then:

$$
y = y + 0 = y + (x+z) = (y+x)+z = (x+y)+z = 0+z = z.
$$

So inverse is unique. ∎

So “ $-x$ ” is unambiguous.

### Fact C:  $0\cdot x = 0$  for all  $x\in\mathbb R^n$ 

This is a vector-space-level analog of the scalar lemma.

Proof:

$$
0x = (0+0)x = 0x + 0x
$$

by distributivity over scalar addition. Add  $-(0x)$  to both sides to get  $0=0x$ . ∎

### Fact D:  $(-1)x = -x$ 

Proof:

$$
(1+(-1))x = 0x = 0.
$$

Left side:

$$
1x + (-1)x = x + (-1)x.
$$

So  $x + (-1)x = 0$ , meaning  $(-1)x$  is the additive inverse of  $x$ . By uniqueness,  $(-1)x=-x$ . ∎

These facts matter because later you’ll do them without thinking, but they come from axioms.

* * *

1.1.5 “Sanity checks” you listed, but now explained at proof-level
------------------------------------------------------------------

### Sanity check 1: If  $\alpha=0$ , then  $\alpha x = 0$ 

This is exactly Fact C.

### Sanity check 2:  $x+(-x)=0$ 

That’s exactly axiom (V5), and we constructed  $-x$  componentwise.

* * *

1.1.6 Why this “explicit model” matters (deep conceptual payoff)
----------------------------------------------------------------

 $\mathbb R^n$  is not just a convenient place to do computations. It’s the canonical example of a vector space because:

*   You can **see** linear combinations explicitly:
    $$
    \sum_{i=1}^k \alpha_i v^{(i)} = \Big(\sum_{i=1}^k \alpha_i v^{(i)}_1,\ \dots,\ \sum_{i=1}^k \alpha_i v^{(i)}_n\Big).
    $$
    This formula is going to be the template for almost every proof later.
*   Many abstract objects become “ $\mathbb R^n$  in disguise” once you choose a basis.

So 1.1 is the place where you first learn what the axioms _mean_ by seeing them hold in a concrete universe.

* * *

1.1.7 Mini-preview: the standard basis (because it will be used constantly)
---------------------------------------------------------------------------

Even though basis is formally later, we can already define the “coordinate axes vectors” in  $\mathbb R^n$ .

Define  $e_j \in \mathbb R^n$  by:

$$
(e_j)_i = \begin{cases} 1 & i=j\\ 0 & i\neq j. \end{cases}
$$

These are the vectors:

*    $e_1=(1,0,0,\dots,0)$ ,
*    $e_2=(0,1,0,\dots,0)$ ,
*   …
*    $e_n=(0,0,\dots,1)$ .

Then any  $x=(x_1,\dots,x_n)$  can be written (and this is crucial):

$$
x = x_1 e_1 + x_2 e_2 + \cdots + x_n e_n.
$$

Proof (componentwise):  
The  $i$ \-th component of the RHS is

$$
\sum_{j=1}^n x_j (e_j)_i.
$$

But  $(e_j)_i$  is 1 only when  $j=i$ , and 0 otherwise, so the sum equals  $x_i$ . Hence equality.

This shows: coordinates are literally coefficients in a linear combination.

* * *

1.1.8 What you must be fluent at after 1.1
------------------------------------------

You should be able to do, instantly and correctly:

*   Use the “componentwise equality” principle: prove vector identities by checking each index.
*   Expand definitions:  
     $(x+y)_i=x_i+y_i$ ,  $(\alpha x)_i=\alpha x_i$ .
*   Prove any vector space axiom for  $\mathbb R^n$  without skipping steps.
*   Derive and use:  
     $0x=0$ ,  $(-1)x=-x$ , uniqueness of  $0$ , uniqueness of inverses.
*   Decompose any  $x$  using standard basis:  
     $x=\sum x_i e_i$ .

* * *

If you want maximum continuity with the roadmap, the next step is 1.2 (geometry as representation, not definition). But 1.1 is now fully nailed:  $\mathbb R^n$  is a vector space because its operations are inherited componentwise from the field  $\mathbb R$ , and every axiom reduces to the corresponding scalar axiom at each coordinate.

## Response:
1.2 Geometry as a representation, not a definition (points vs vectors, affine structure, and why this distinction is non-negotiable)
------------------------------------------------------------------------------------------------------------------------------------

In 1.1 we treated  $\mathbb R^n$  as a set of  $n$ \-tuples with operations. That was purely algebraic.

Now 1.2 is about something subtle but foundational:

*   In  $\mathbb R^n$ , we _often_ draw vectors as arrows in space, and we _often_ treat a vector like a point.
*   This is convenient, but it hides a conceptual distinction that becomes critical the moment you study:
    *   solution sets  $Ax=b$  (affine sets),
    *   translations,
    *   convexity and “affine combinations,”
    *   gradients (as covectors / linear functionals),
    *   change of origin,
    *   anything involving “locations” vs “displacements.”

So this section is about building a clean mental model:

> A **point** is a location.  
> A **vector** is a displacement (difference between two points).  
> You can add vectors to vectors.  
> You can add vectors to points.  
> You cannot add points to points (not intrinsically).

In  $\mathbb R^n$  we can _identify_ points with vectors once we choose an origin, but that identification is a _choice_, not a law of nature.

We will formalize this properly.

* * *

### 1.2.0 What the “picture” usually does (and why it can mislead)

In  $\mathbb R^2$ , you draw an arrow from the origin to  $(x_1,x_2)$  and call that the vector  $x$ . You also plot the point  $(x_1,x_2)$  and call that the point  $x$ .

You get used to writing:

*   “the point  $x$ ” and “the vector  $x$ ” interchangeably,
*   “ $x+y$ ” as “add two points,”
*   “ $2x$ ” as “double a point.”

This works only because we are quietly using the origin  $0$  as a distinguished reference point and converting points into displacement vectors from that origin.

The danger: when you later change origin or talk about sets defined by equations  $Ax=b$ , you’ll accidentally use vector-space rules on things that are not vector subspaces.

So we’ll separate the concepts cleanly.

* * *

1.2.1 Two different kinds of objects: a set of points vs a vector space of displacements
----------------------------------------------------------------------------------------

### A) Vectors: elements of a vector space  $V$ 

From 1.1,  $V=\mathbb R^n$  is a vector space. That means we can do:

*   vector + vector  $\to$  vector,
*   scalar  $\cdot$  vector  $\to$  vector,

and the axioms hold.

So it makes perfect sense to talk about:

$$
v+w,\quad \alpha v,\quad \sum_i \alpha_i v_i.
$$

### B) Points: elements of an affine space  $A$ 

A “space of points” (locations) is typically modeled as an **affine space**. An affine space is not a vector space because it has no distinguished “zero point” (no canonical origin).

The structure is:

*   There is a set  $A$  of points.
*   There is a vector space  $V$  of displacement vectors.
*   You can subtract points to get a vector:
    $$
    A\times A \to V,\quad (p,q)\mapsto q-p.
    $$
*   You can add a vector to a point to get a point:
    $$
    A\times V \to A,\quad (p,v)\mapsto p+v.
    $$

This “point + vector” operation is sometimes called a **translation**.

Crucial: there is _no_ natural operation  $A\times A\to A$  that would be “point + point.” Points don’t add.

That’s not philosophy; it’s about invariance under change of origin. If point addition were intrinsic, it would have to not depend on any chosen origin. But it does.

* * *

1.2.2 The minimum axioms of an affine space (rigorous)
------------------------------------------------------

Let  $V$  be a vector space over  $\mathbb R$ . An **affine space modeled on  $V$ ** is a nonempty set  $A$  with an action  $A\times V\to A$ , written  $(p,v)\mapsto p+v$ , such that:

1.  **Identity translation:**
    $$
    p+0 = p \quad \forall p\in A.
    $$
2.  **Compatibility with vector addition (associativity of translating):**
    $$
    (p+v)+w = p+(v+w) \quad \forall p\in A,\ \forall v,w\in V.
    $$
3.  **Transitivity and freeness (unique displacement between points):**  
    For any  $p,q\in A$ , there exists a **unique**  $v\in V$  such that
    $$
    q = p+v.
    $$
    That unique vector is denoted  $q-p$ .

This axiom is the real “points vs vectors” bridge:

*   any two points determine exactly one displacement vector from one to the other.

From this axiom, subtraction of points is well-defined:

$$
q-p := \text{the unique } v\in V \text{ such that } q=p+v.
$$

* * *

1.2.3 Derived identities in affine spaces (proved)
--------------------------------------------------

These are the rules you will use constantly when reasoning about affine sets.

### Proposition 1:  $(q-p) + (r-q) = r-p$ 

Interpretation: displacements add along a path.

**Proof.**  
Let  $v=q-p$ , so  $q=p+v$ .  
Let  $w=r-q$ , so  $r=q+w$ .

Substitute  $q=p+v$  into  $r=q+w$ :

$$
r = (p+v)+w = p+(v+w)
$$

by affine compatibility.

By uniqueness of displacement from  $p$  to  $r$ , we must have:

$$
r-p = v+w = (q-p)+(r-q).
$$

∎

This is the rigorous content behind “head-to-tail” arrow addition in diagrams.

* * *

### Proposition 2:  $p+(q-p)=q$ 

**Proof.**  
By definition,  $q-p$  is the unique vector  $v$  such that  $q=p+v$ . Therefore  $p+(q-p)=q$ . ∎

* * *

### Proposition 3:  $q - (p+v) = (q-p) - v$ 

This is a “translation invariance” identity.

**Proof.**  
Let  $u=q-p$ , so  $q=p+u$ . Then:

$$
q = p+u = (p+v) + (u-v)
$$

because  $(p+v)+(u-v)=p+(v+u-v)=p+u$ .

So the displacement from  $(p+v)$  to  $q$  is  $(u-v)$ . Hence

$$
q-(p+v)=u-v=(q-p)-v.
$$

∎

This is a typical affine manipulation used in geometry and optimization.

* * *

1.2.4 How  $\mathbb R^n$  hides the distinction (origin identification)
-----------------------------------------------------------------------

Now the subtle part: in  $\mathbb R^n$ , we often take the set of points  $A$  to be “the same underlying set” as the vector space  $V=\mathbb R^n$ . That is, a point is an  $n$ \-tuple and a vector is also an  $n$ \-tuple.

But **the operations are conceptually different**:

*   As vectors:  $x+y$  means vector addition (displacement composition).
*   As points:  $p+v$  means translate point  $p$  by displacement  $v$ .

Where does “point + point” come from in standard coordinate geometry? From choosing an origin  $o$ .

If you choose an origin  $o\in A$ , you can identify each point  $p\in A$  with the vector:

$$
\vec p := p-o \in V.
$$

This vector  $\vec p$  is “the displacement from the origin to the point.”

Then if you have two points  $p,q$ , you can define a coordinate-dependent “sum of points” by:

$$
p \oplus q := o + ((p-o)+(q-o)).
$$

This depends on  $o$ . Change  $o$ , and the result changes.

That’s the rigorous reason “adding points” is not intrinsic.

In everyday  $\mathbb R^n$  with origin  $0$ , we silently use  $o=0$ , so:

$$
p \oplus q = 0 + (p+q) = p+q.
$$

So the usual coordinate addition of  $n$ \-tuples is really “add their displacement vectors from the origin, then convert back to a point.”

The origin is doing hidden work.

* * *

1.2.5 Why this matters: subspaces vs affine sets (Ax=0 vs Ax=b)
---------------------------------------------------------------

This is where the distinction becomes operationally necessary.

### A) Subspace: must contain the origin (vector identity)

A subset  $W\subseteq V$  is a subspace if:

*    $0\in W$ ,
*   closed under vector addition,
*   closed under scalar multiplication.

So the “zero vector” is central. Subspaces are “worlds anchored at 0.”

Example:

$$
\{x\in\mathbb R^n : Ax=0\}
$$

is always a subspace (a linear system through the origin).

### B) Affine set: translation of a subspace (does NOT need to contain the origin)

A typical solution set

$$
\{x\in\mathbb R^n : Ax=b\}
$$

when  $b\neq 0$ , is generally **not** a subspace because it usually does not contain  $0$ .

But it is an **affine subspace**:  
If  $x_p$  is one particular solution to  $Ax=b$ , then the full solution set is:

$$
x_p + \{x : Ax=0\} = \{x_p + z : z\in \mathrm{Null}(A)\}.
$$

That is: “one point” + “all displacements in the null space.”

This decomposition is literally point + vector-subspace. It is not vector-space closure in the original set.

This is why you must keep point-vs-vector clear: the solution set is a set of points; the nullspace is a set of vectors (displacements). You translate the nullspace by a particular point to get the affine solution set.

* * *

1.2.6 Affine combinations vs linear combinations (the algebraic version of points vs vectors)
---------------------------------------------------------------------------------------------

This is a huge conceptual bridge to convexity later.

### Linear combination (vectors)

A linear combination is:

$$
\sum_{i=1}^k \alpha_i v_i.
$$

No constraint on  $\sum \alpha_i$ . This always lives in the vector space.

### Affine combination (points)

If  $p_1,\dots,p_k$  are **points**, an affine combination is:

$$
\sum_{i=1}^k \alpha_i p_i \quad \text{with the constraint } \sum_{i=1}^k \alpha_i = 1.
$$

Why the constraint? Because it makes the expression independent of the choice of origin.

Let’s prove that cleanly.

#### Proposition: Affine combinations are origin-independent; general linear combinations of points are origin-dependent

Take points  $p_i \in A$ . Choose an origin  $o\in A$  and represent each point as a vector  $v_i := p_i - o \in V$ .

Define the “computed point”:

$$
p := o + \sum_{i=1}^k \alpha_i v_i.
$$

This is how you would compute  $\sum \alpha_i p_i$  in coordinates relative to origin  $o$ .

Now choose a different origin  $o' = o + t$  for some  $t\in V$ .  
Then the coordinate vectors change:

$$
v_i' := p_i - o' = p_i - (o+t) = (p_i-o) - t = v_i - t.
$$

Now compute the same formula using  $o'$ :

$$
p' := o' + \sum_{i=1}^k \alpha_i v_i' = (o+t) + \sum_{i=1}^k \alpha_i (v_i - t)
$$

Expand:

$$
p' = o+t + \sum_{i=1}^k \alpha_i v_i - \Big(\sum_{i=1}^k \alpha_i\Big)t.
$$

Group terms:

$$
p' = o + \sum_{i=1}^k \alpha_i v_i + \Big(1-\sum_{i=1}^k \alpha_i\Big)t.
$$

But  $o + \sum \alpha_i v_i$  is exactly  $p$ . So:

$$
p' = p + \Big(1-\sum_{i=1}^k \alpha_i\Big)t.
$$

Therefore:

*   If  $\sum \alpha_i = 1$ , then  $p' = p$ . Independence of origin.
*   If  $\sum \alpha_i \neq 1$ , then  $p'$  changes when you change origin. So it’s not intrinsic.

That’s the deep reason affine combinations have the “sum coefficients = 1” constraint.

This becomes the backbone of affine geometry and convexity:

*   convex combinations are affine combinations with  $\alpha_i\ge 0$ .

* * *

1.2.7 Translation invariance: what geometry cares about, not absolute coordinates
---------------------------------------------------------------------------------

In physics terms:

*   Points are “where you are.”
*   Vectors are “how you move.”

Many statements in geometry and optimization are translation-invariant: they should not depend on where you decide the origin is.

Examples:

*   “these points are collinear”
*   “this set is an affine subspace”
*   “this set is convex”
*   “the distance between two points” (requires a norm too, later)

All these should survive shifting the coordinate system.

This is why point+point is suspicious: if your notion depends on the coordinate origin, it is not geometrically natural.

* * *

1.2.8 Practical consequences (things you must NOT do)
-----------------------------------------------------

Here are common illegal moves that happen when you blur points and vectors:

1.  Treating solution sets  $Ax=b$  as subspaces when  $b\neq 0$ .  
    Subspaces must contain  $0$ . Affine sets need not.
2.  Taking “midpoint” of two points without realizing it is an affine combination:
    $$
    m = \frac12 p + \frac12 q.
    $$
    This is fine because coefficients sum to 1. It’s intrinsic.
3.  Trying to interpret “ $2p$ ” for a point  $p$  as meaningful without an origin.  
    It is origin-dependent. You can only scale vectors intrinsically.
4.  Confusing “vector from  $p$  to  $q$ ” with “the point  $q-p$ .”  
     $q-p$  is a vector. It does not live in the point set  $A$ .

* * *

1.2.9 Concrete sanity pictures (verbal but exact)
-------------------------------------------------

*   **Vector addition**: place arrow  $v$  head-to-tail with arrow  $w$ . The resulting displacement is  $v+w$ . This corresponds to Proposition 1:  $(q-p)+(r-q)=r-p$ .
*   **Point + vector**: take point  $p$ . Move by displacement  $v$  to get a new point  $p+v$ . This is translation.
*   **Point difference**:  $q-p$  is “the unique displacement that takes you from  $p$  to  $q$ .”

These three operations are the complete correct geometry.

* * *

1.2.10 Mastery checklist for 1.2
--------------------------------

You fully own 1.2 when you can do all of these cleanly:

*   Explain why points don’t add intrinsically (dependence on origin).
*   Define an affine space as “points + displacement vectors” with the translation axioms.
*   Prove  $(q-p)+(r-q)=r-p$ .
*   Show that  $Ax=b$  solution set is  $x_p + \mathrm{Null}(A)$  and therefore affine, not a subspace (unless  $b=0$ ).
*   Prove affine combinations are exactly the origin-independent linear combinations of points (sum coefficients = 1).
*   Distinguish linear combinations of vectors vs affine combinations of points vs convex combinations.

* * *

This nails 1.2 at a foundational level. Next in the roadmap is 1.3 (linear combinations as the fundamental constructor). That’s where everything in linear algebra starts to compress into one atomic operation: “take linear combinations,” and you’ll see why matrices are just “machines for linear combinations.”

## Response:
1.3 Linear combinations — the fundamental constructor (everything is built out of this)
---------------------------------------------------------------------------------------

Up to now, we have done three things, very deliberately and in the correct dependency order:

*   **0.1** fixed the scalar universe (a field): what coefficients are allowed and why division must work.
*   **0.2** taught us what it means to _preserve structure_ and why linear maps are not arbitrary functions.
*   **1.1–1.2** built the concrete model  $\mathbb R^n$  and separated **vectors (displacements)** from **points (locations)**.

Now we arrive at the atomic operation of all linear algebra:

> **Linear combinations are the only way vectors are ever constructed, compared, generated, or transformed.**

If you deeply understand linear combinations, everything else—span, subspaces, bases, column spaces, matrix multiplication, projections, least squares—becomes a controlled elaboration of this single idea.

This section will:

1.  Define linear combinations with full precision
2.  Show why they are the _minimal closure operation_ compatible with vector space axioms
3.  Introduce span rigorously (as a closure, not a slogan)
4.  Prove fundamental properties of span
5.  Explain linear dependence/independence as _statements about linear combinations_
6.  Show how matrices are nothing but “linear-combination machines” (preview, not hand-wavy)

No shortcuts.

* * *

1.3.1 Definition: linear combination (fully explicit)
-----------------------------------------------------

Let  $V$  be a vector space over a field  $\mathbb F$  (for now, think  $V=\mathbb R^n$ ,  $\mathbb F=\mathbb R$ ).

Let  $v_1,\dots,v_k \in V$  be vectors.  
Let  $\alpha_1,\dots,\alpha_k \in \mathbb F$  be scalars.

### Definition (linear combination)

A **linear combination** of  $v_1,\dots,v_k$  is any vector of the form

$$
\sum_{i=1}^k \alpha_i v_i = \alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_k v_k.
$$

This is not notation fluff. It encodes exactly two allowed operations:

*   scalar multiplication ( $\alpha_i v_i$ ),
*   vector addition (summing the results).

Nothing else is allowed.

* * *

1.3.2 Why linear combinations are the _only_ reasonable constructor
-------------------------------------------------------------------

This is a deep point that often goes unstated.

A vector space is defined by:

*   closure under **addition**,
*   closure under **scalar multiplication**.

So suppose you start with a set of vectors  $S=\{v_1,\dots,v_k\}$ .

Ask: _what vectors must exist if the space is to respect the axioms?_

*   You must be able to scale each  $v_i$  by any scalar.
*   You must be able to add the results.
*   You must be able to repeat this finitely many times.

That forces you to include **all finite linear combinations**.

There is no other operation sanctioned by the axioms.

> **Therefore: linear combinations are not one tool among many.  
> They are the closure operation dictated by the axioms themselves.**

This is why linear algebra reduces everything to questions about linear combinations.

* * *

1.3.3 Linear combinations in  $\mathbb R^n$ : componentwise anatomy
-------------------------------------------------------------------

Let’s unpack a linear combination _completely_ in  $\mathbb R^n$ .

Let

$$
v^{(1)},\dots,v^{(k)} \in \mathbb R^n, \quad v^{(j)} = (v^{(j)}_1,\dots,v^{(j)}_n).
$$

Then

$$
x = \sum_{j=1}^k \alpha_j v^{(j)}
$$

means, **component by component**:

$$
x_i = \sum_{j=1}^k \alpha_j v^{(j)}_i \quad \text{for each } i=1,\dots,n.
$$

So a linear combination is literally:

*   for each coordinate  $i$ ,
*   take a scalar-weighted sum of the corresponding coordinates.

This matters because:

*   every proof later reduces to this formula,
*   matrices, dot products, projections, norms all act coordinatewise on these sums.

* * *

1.3.4 Definition: span (as a closure, not a buzzword)
-----------------------------------------------------

Now we formalize the idea of “all vectors you can build from these.”

### Definition (span)

Let  $S=\{v_1,\dots,v_k\}\subset V$ .

The **span** of  $S$ , denoted  $\mathrm{span}(S)$ , is:

$$
\mathrm{span}(S) := \left\{ \sum_{i=1}^k \alpha_i v_i \;\middle|\; \alpha_1,\dots,\alpha_k \in \mathbb F \right\}.
$$

That is: the set of _all_ linear combinations of vectors in  $S$ .

No more, no less.

* * *

1.3.5 Span is the smallest subspace containing  $S$  (proved rigorously)
------------------------------------------------------------------------

This theorem is not cosmetic. It is the structural reason “span” matters.

### Theorem

 $\mathrm{span}(S)$  is:

1.  a subspace of  $V$ ,
2.  the **smallest** subspace of  $V$  that contains  $S$ .

#### Proof, Part 1:  $\mathrm{span}(S)$  is a subspace

We verify the subspace criteria.

**(i) Contains the zero vector**

Take all coefficients  $\alpha_i = 0$ . Then

$$
\sum_{i=1}^k 0\cdot v_i = 0.
$$

So  $0\in\mathrm{span}(S)$ .

**(ii) Closed under addition**

Let

$$
x=\sum_{i=1}^k \alpha_i v_i, \quad y=\sum_{i=1}^k \beta_i v_i
$$

be in  $\mathrm{span}(S)$ .

Then:

$$
x+y = \sum_{i=1}^k (\alpha_i v_i + \beta_i v_i) = \sum_{i=1}^k (\alpha_i+\beta_i) v_i,
$$

which is again a linear combination of vectors in  $S$ .  
So  $x+y\in\mathrm{span}(S)$ .

**(iii) Closed under scalar multiplication**

For any  $\gamma\in\mathbb F$ ,

$$
\gamma x = \gamma \sum_{i=1}^k \alpha_i v_i = \sum_{i=1}^k (\gamma\alpha_i) v_i,
$$

which is again a linear combination of vectors in  $S$ .

Thus  $\mathrm{span}(S)$  is a subspace.

* * *

#### Proof, Part 2: Minimality

Let  $W\subseteq V$  be **any** subspace such that  $S\subseteq W$ .

Because  $W$  is a subspace:

*   it contains each  $v_i$ ,
*   it is closed under scalar multiplication,
*   it is closed under addition.

Therefore, for any scalars  $\alpha_i$ ,

$$
\sum_{i=1}^k \alpha_i v_i \in W.
$$

So every element of  $\mathrm{span}(S)$  lies in  $W$ , i.e.

$$
\mathrm{span}(S)\subseteq W.
$$

Thus  $\mathrm{span}(S)$  is the smallest subspace containing  $S$ .

∎

* * *

1.3.6 Membership problem: “is  $x$  in the span?”
-------------------------------------------------

This is the first _algorithmic_ linear algebra question.

Given:

*   vectors  $v_1,\dots,v_k$ ,
*   a vector  $x$ ,

the question

$$
x \in \mathrm{span}(v_1,\dots,v_k)\ ?
$$

means:

> Do there exist scalars  $\alpha_1,\dots,\alpha_k$  such that
> 
> $$
> \sum_{i=1}^k \alpha_i v_i = x\ ?
> $$

In  $\mathbb R^n$ , this is equivalent to a **system of linear equations**.

Explicitly, writing components:

$$
\sum_{i=1}^k \alpha_i v^{(i)}_j = x_j \quad \text{for each } j=1,\dots,n.
$$

That is:

*   unknowns:  $\alpha_1,\dots,\alpha_k$ ,
*   equations: one per coordinate.

This is why solving systems  $Ax=b$  is _not_ a separate topic—it is literally the question “is  $b$  in the span of the columns of  $A$ ?”

* * *

1.3.7 Linear dependence and independence (as statements about linear combinations)
----------------------------------------------------------------------------------

Now we introduce a crucial dichotomy.

### Definition: linear dependence

Vectors  $v_1,\dots,v_k$  are **linearly dependent** if there exist scalars  $\alpha_1,\dots,\alpha_k$ , **not all zero**, such that

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

### Definition: linear independence

Vectors  $v_1,\dots,v_k$  are **linearly independent** if the only solution to

$$
\sum_{i=1}^k \alpha_i v_i = 0
$$

is

$$
\alpha_1=\cdots=\alpha_k=0.
$$

This definition is entirely about linear combinations. Nothing geometric yet.

* * *

1.3.8 What dependence really means (not intuition—logic)
--------------------------------------------------------

### Proposition

If  $v_1,\dots,v_k$  are linearly dependent, then **at least one vector can be written as a linear combination of the others**.

#### Proof

Because the vectors are dependent, there exist scalars  $\alpha_i$ , not all zero, such that

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

Pick an index  $j$  with  $\alpha_j\neq 0$ .

Rearrange:

$$
\alpha_j v_j = -\sum_{i\neq j} \alpha_i v_i.
$$

Because  $\alpha_j\neq 0$  and we are over a field, divide:

$$
v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
$$

So  $v_j$  is a linear combination of the others.

∎

This proof **uses the field axiom** (division by nonzero scalar). That’s why dependence behaves cleanly only over fields.

* * *

1.3.9 Independence as uniqueness of linear combinations
-------------------------------------------------------

There is a second, equally important interpretation.

### Proposition

Vectors  $v_1,\dots,v_k$  are linearly independent **if and only if** every vector in their span has a **unique** representation as a linear combination of them.

#### Proof (⇐ direction)

Assume representations are unique.

Suppose

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

But  $0$  also has the representation

$$
0 = \sum_{i=1}^k 0\cdot v_i.
$$

By uniqueness,  $\alpha_i=0$  for all  $i$ .  
So vectors are independent.

#### Proof (⇒ direction)

Assume vectors are independent.

Suppose

$$
\sum_{i=1}^k \alpha_i v_i = \sum_{i=1}^k \beta_i v_i.
$$

Subtract:

$$
\sum_{i=1}^k (\alpha_i-\beta_i) v_i = 0.
$$

By independence,  $\alpha_i-\beta_i=0$ , so  $\alpha_i=\beta_i$ .  
Thus representation is unique.

∎

This proposition is the bridge to **bases** and **coordinates** later.

* * *

1.3.10 Matrices are linear-combination machines (conceptual preview)
--------------------------------------------------------------------

This is not yet formal matrix theory, but the idea belongs here.

Let  $A\in\mathbb R^{m\times n}$  have columns:

$$
A = [a_1\ a_2\ \cdots\ a_n], \quad a_j\in\mathbb R^m.
$$

Then for any  $x=(x_1,\dots,x_n)\in\mathbb R^n$ ,

$$
Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n.
$$

That is:

*   matrix–vector multiplication **is** a linear combination of the columns,
*   the coefficients come from the input vector.

So:

*   column space = span of columns,
*   solving  $Ax=b$  = asking whether  $b$  is in that span,
*   rank = dimension of that span.

This is why 1.3 is not optional. It _is_ matrix theory, in embryonic form.

* * *

1.3.11 Mastery checklist for 1.3
--------------------------------

You truly own this section when you can, without hesitation:

*   Define linear combinations and expand them componentwise.
*   Define span and prove it is the smallest subspace containing a set.
*   Reduce “membership in span” to a linear system.
*   Use the dependence definition to explicitly solve for one vector in terms of others.
*   Explain independence as uniqueness of representation.
*   Interpret matrix–vector multiplication as a linear combination of columns.

* * *

### Final meta-point (important)

From here on, **every** object in linear algebra will be characterized by one question:

> “What linear combinations does this allow or forbid?”

*   Subspace: closed under all linear combinations.
*   Basis: allows all linear combinations _uniquely_.
*   Linear map: preserves linear combinations.
*   Matrix: encodes linear combinations.
*   Rank: how many independent directions of linear combination survive.
*   Projection: best linear combination approximation.

So 1.3 is not a chapter.  
It is the atom.

Next in the roadmap is **1.4 (geometry of linear combinations)** or directly **2.x (dot product)**, depending on how you want to branch.

## Response:
1.4 The geometry of linear combinations
---------------------------------------

_(how algebra turns into shape, dimension, and degrees of freedom)_

Up to 1.3, everything was algebraic: coefficients, sums, closure.  
Now we cash that algebra out into **geometry**, but carefully—without confusing geometry for definition.

The guiding principle of this section is:

> **Geometry is not an extra structure added to linear algebra.  
> Geometry is what linear combinations look like when the field is  $\mathbb R$ .**

So 1.4 answers:  
_What shapes do linear combinations produce, and why do those shapes encode dimension, freedom, and constraint?_

We will proceed in layers:

1.  Single vector: one degree of freedom → a line
2.  Two vectors: cases → line or plane
3.   $k$  vectors: span as a geometric object
4.  Linear vs affine geometry (again, but now operationally)
5.  Dimension as “number of independent directions”
6.  Why geometry never contradicts algebra—only reveals it

No pictures needed; everything will be proved symbolically and interpreted geometrically.

* * *

1.4.1 One vector: span as a line through the origin
---------------------------------------------------

Let  $v\in\mathbb R^n$ ,  $v\neq 0$ .

### Algebraic object

$$
\mathrm{span}\{v\} = \{\alpha v : \alpha\in\mathbb R\}.
$$

### Geometric interpretation

This set is a **line through the origin** in the direction of  $v$ .

Why “line”?

*   One free scalar parameter  $\alpha$ .
*   As  $\alpha$  varies over  $\mathbb R$ , you move continuously in both directions.

Why “through the origin”?

*   When  $\alpha=0$ ,  $\alpha v = 0$ .

### Rigorous characterization

Define the map

$$
f:\mathbb R \to \mathbb R^n, \quad f(\alpha)=\alpha v.
$$
*    $f$  is linear.
*    $f$  is injective because  $v\neq 0$ :
    $$
    \alpha v = \beta v \Rightarrow (\alpha-\beta)v=0 \Rightarrow \alpha=\beta.
    $$

So  $\mathrm{span}\{v\}$  is a 1-dimensional linear subspace.

> **One nonzero vector gives exactly one direction of freedom.**

This is the prototype of “dimension = number of independent scalars.”

* * *

1.4.2 Two vectors: three fundamentally different cases
------------------------------------------------------

Let  $v_1,v_2\in\mathbb R^n$ , both nonzero.

We study:

$$
\mathrm{span}\{v_1,v_2\} = \{\alpha v_1+\beta v_2 : \alpha,\beta\in\mathbb R\}.
$$

Everything depends on **linear dependence vs independence**.

* * *

### Case A:  $v_2$  is a scalar multiple of  $v_1$ 

That is,  $v_2 = \lambda v_1$  for some  $\lambda\in\mathbb R$ .

Then:

$$
\alpha v_1 + \beta v_2 = \alpha v_1 + \beta(\lambda v_1) = (\alpha+\lambda\beta)v_1.
$$

So:

$$
\mathrm{span}\{v_1,v_2\} = \mathrm{span}\{v_1\}.
$$

### Geometry

*   Still a **line through the origin**.
*   Second vector adds _no new direction_.

This is the geometric meaning of linear dependence:

> **Dependent vectors do not increase geometric dimension.**

* * *

### Case B:  $v_1,v_2$  are linearly independent

Then:

$$
\alpha v_1 + \beta v_2 = 0 \Rightarrow \alpha=\beta=0.
$$

Now the map

$$
(\alpha,\beta)\mapsto \alpha v_1+\beta v_2
$$

is injective from  $\mathbb R^2$  into  $\mathbb R^n$ .

### Geometry

*   The span is a **plane through the origin**.
*   Two independent degrees of freedom.
*   Every point in the plane has a _unique_ coordinate pair  $(\alpha,\beta)$ .

This is the first appearance of **coordinate systems**.

* * *

### Case C: Degenerate dimensions (why  $\mathbb R^1$  and  $\mathbb R^2$  behave differently)

If  $n=1$ :

*   Any two nonzero vectors are dependent.
*   You cannot form a plane.

If  $n\ge 2$ :

*   Independence is possible.
*   Geometry reflects ambient dimension.

This foreshadows a crucial principle:

> **A subspace cannot have dimension larger than the ambient space.**

* * *

1.4.3 General case: span of  $k$  vectors
-----------------------------------------

Let  $v_1,\dots,v_k\in\mathbb R^n$ .

### Algebraic object

$$
\mathrm{span}\{v_1,\dots,v_k\} = \left\{ \sum_{i=1}^k \alpha_i v_i : \alpha_i\in\mathbb R \right\}.
$$

### Geometric meaning

*   Each independent vector adds **one independent direction**.
*   Dependent vectors add **no new geometry**.
*   The span is a **flat object through the origin**:
    *   line (1D),
    *   plane (2D),
    *   3D subspace,
    *   …
    *   up to dimension  $\le n$ .

This object is called a **linear subspace**.

* * *

### Dimension = number of independent directions

Let  $\{v_1,\dots,v_k\}$  have maximal independent subset of size  $d$ .

Then:

$$
\dim(\mathrm{span}\{v_1,\dots,v_k\}) = d.
$$

This is not definition—it is consequence of:

*   uniqueness of linear combinations (1.3),
*   injectivity of coefficient maps.

Geometrically:

*   You need  $d$  real numbers to describe a general point in the span.
*   No fewer will do.
*   More would be redundant.

* * *

1.4.4 Linear combinations vs affine combinations (geometry version)
-------------------------------------------------------------------

Recall from 1.2:

*   Linear combinations → vectors → anchored at origin.
*   Affine combinations → points → origin-free.

### Linear combinations

$$
\sum_{i=1}^k \alpha_i v_i
$$
*   always pass through 0,
*   describe linear subspaces.

### Affine combinations

$$
\sum_{i=1}^k \alpha_i p_i, \quad \sum \alpha_i = 1
$$
*   describe **affine flats** (lines, planes, hyperplanes),
*   need not pass through origin.

### Example: line through two points  $p,q$ 

Affine description:

$$
\ell = \{(1-t)p + tq : t\in\mathbb R\}.
$$

Rewrite:

$$
(1-t)p + tq = p + t(q-p).
$$
*    $q-p$  is a vector (direction).
*    $p$  is a base point.

So geometrically:

> **Affine objects = point + linear subspace.**

This decomposition is canonical and will recur constantly.

* * *

1.4.5 Convex geometry as a restriction of linear geometry (preview)
-------------------------------------------------------------------

If we impose constraints on coefficients, geometry changes:

### Convex combinations

$$
\sum_{i=1}^k \alpha_i p_i, \quad \alpha_i \ge 0, \quad \sum \alpha_i = 1.
$$

Geometrically:

*   You get the **filled-in shape** between points:
    *   line segment,
    *   triangle,
    *   polygon,
    *   polytope.

Linear algebra underlies this:

*   convexity is affine geometry + inequality constraints.

This is why linear algebra is prerequisite for convex optimization.

* * *

1.4.6 Why geometry never contradicts algebra
--------------------------------------------

A common beginner fear:

> “The picture says one thing; the algebra says another.”

This never happens if you are precise.

Why?

*   Geometry is just the _real-number instantiation_ of algebraic definitions.
*   Every geometric statement corresponds to a rank, independence, or span statement.

Examples:

*   “These vectors lie in a plane”  
    ↔ span has dimension 2.
*   “This line doesn’t pass through origin”  
    ↔ affine, not linear.
*   “This direction adds nothing new”  
    ↔ linear dependence.

So geometry is a _sanity check_, not an alternative theory.

* * *

1.4.7 The deep invariant: translation vs linear structure
---------------------------------------------------------

One final conceptual tightening.

Linear geometry:

*   distinguished origin,
*   scaling meaningful,
*   subspaces.

Affine geometry:

*   no origin,
*   no intrinsic scaling,
*   only differences matter.

The moment you see:

*    $Ax=0$  → linear,
*    $Ax=b$  → affine,

you should mentally translate:

*   “vector subspace” vs “translated vector subspace.”

This distinction is not optional. It is the backbone of:

*   solution sets,
*   regression,
*   feasible regions,
*   constraint qualifications.

* * *

1.4.8 Mastery checklist for 1.4
-------------------------------

You have _fully_ internalized 1.4 if you can:

*   Predict the geometry of a span from independence alone.
*   Explain dimension as number of free scalar parameters.
*   Translate between:
    *   algebraic span,
    *   geometric flat,
    *   degrees of freedom.
*   Decompose any affine set as:
    $$
    \text{point} + \text{linear subspace}.
    $$
*   Explain why linear combinations pass through the origin and affine ones do not.
*   See convex geometry as constrained affine geometry.

* * *

### Where this leaves us

At this point, you have:

*   scalars (0.1),
*   structure-preserving maps (0.2),
*   concrete vector spaces (1.1),
*   points vs vectors (1.2),
*   linear combinations as atoms (1.3),
*   geometry of those atoms (1.4).

You are now ready to move into **inner products (2.x)**, where geometry gains _metric meaning_ (lengths, angles, projections). That is the next qualitative leap.

If you want, we proceed to **2.1 (dot product as an inner product)** with the same depth.

## Response:
2.1 Dot product as an inner product on  $\mathbb R^n$ 
------------------------------------------------------

_(where linear algebra acquires metric meaning: length, angle, orthogonality)_

Up to 1.4, linear algebra was **purely algebraic + affine geometry**:

*   vectors as displacements,
*   linear combinations,
*   span and dimension,
*   flats through the origin or translated.

What was _missing_ was any notion of:

*   length,
*   angle,
*   perpendicularity,
*   closeness,
*   projection.

Those are not automatic in a vector space. They require **extra structure**.

Section 2.1 is the precise moment where geometry becomes _metric geometry_.

The dot product is not “just a formula.” It is:

> a symmetric, bilinear, positive-definite pairing that turns linear structure into measurable geometry.

We will:

1.  Define the dot product rigorously
2.  Prove each inner-product axiom from the definition
3.  Explain what each axiom _means_ geometrically and algebraically
4.  Derive foundational consequences (orthogonality, zero detection)
5.  Show why this structure is special to  $\mathbb R^n$  (and how it generalizes)

No intuition without proof. No pictures without algebra.

* * *

2.1.1 What an inner product is supposed to do (before definition)
-----------------------------------------------------------------

Before writing a formula, we must be clear about the _job description_.

An inner product  $\langle \cdot,\cdot\rangle$  on a real vector space should:

1.  Take **two vectors** and return a **real number**.
2.  Behave linearly in each argument (up to symmetry).
3.  Be symmetric: swapping inputs does nothing.
4.  Detect zero vectors via positivity:
    $$
    \langle x,x\rangle \ge 0,\quad \langle x,x\rangle=0 \iff x=0.
    $$

Why these requirements?

*   Linearity ensures compatibility with linear combinations.
*   Symmetry ensures “angle” is mutual.
*   Positive definiteness ensures  $\langle x,x\rangle$  can represent squared length.

Everything later—norms, projections, least squares—depends exactly on these properties and on nothing else.

* * *

2.1.2 Definition of the dot product on  $\mathbb R^n$ 
------------------------------------------------------

Let  $x=(x_1,\dots,x_n)$ ,  $y=(y_1,\dots,y_n)$  be vectors in  $\mathbb R^n$ .

### Definition (dot product)

$$
\boxed{ \langle x,y\rangle := x^\top y := \sum_{i=1}^n x_i y_i }
$$

This is a _definition_, not a theorem.

We now verify that this operation satisfies the inner product axioms.

* * *

2.1.3 Axiom 1: symmetry
-----------------------

### Statement

$$
\langle x,y\rangle = \langle y,x\rangle \quad \forall x,y\in\mathbb R^n.
$$

### Proof

By definition:

$$
\langle x,y\rangle = \sum_{i=1}^n x_i y_i.
$$

Because multiplication in  $\mathbb R$  is commutative:

$$
x_i y_i = y_i x_i.
$$

Therefore:

$$
\sum_{i=1}^n x_i y_i = \sum_{i=1}^n y_i x_i = \langle y,x\rangle.
$$

∎

### Meaning

Symmetry is what allows us to interpret the dot product as “mutual alignment.”  
There is no notion of “directional bias” between the arguments.

* * *

2.1.4 Axiom 2: linearity in the first argument
----------------------------------------------

We prove linearity in the first argument; symmetry then implies linearity in the second.

### Statement

For all  $x,y,z\in\mathbb R^n$  and scalars  $a,b\in\mathbb R$ :

$$
\langle ax+by,\,z\rangle = a\langle x,z\rangle + b\langle y,z\rangle.
$$

### Proof

Start from the definition:

$$
\langle ax+by,\,z\rangle = \sum_{i=1}^n (ax_i + by_i) z_i.
$$

Distribute multiplication:

$$
= \sum_{i=1}^n (a x_i z_i + b y_i z_i).
$$

Use linearity of summation:

$$
= a\sum_{i=1}^n x_i z_i + b\sum_{i=1}^n y_i z_i.
$$

Recognize dot products:

$$
= a\langle x,z\rangle + b\langle y,z\rangle.
$$

∎

### Meaning

This axiom ensures the dot product respects **linear combinations**.  
It is exactly what makes the dot product compatible with vector space structure.

Without linearity, projection and least squares collapse.

* * *

2.1.5 Axiom 3: positive definiteness
------------------------------------

### Statement

For all  $x\in\mathbb R^n$ :

$$
\langle x,x\rangle \ge 0, \quad\text{and}\quad \langle x,x\rangle = 0 \iff x=0.
$$

### Proof

Compute:

$$
\langle x,x\rangle = \sum_{i=1}^n x_i^2.
$$
*   Each term  $x_i^2 \ge 0$  because squares of real numbers are nonnegative.
*   Therefore the sum is nonnegative.

Now suppose:

$$
\langle x,x\rangle = 0.
$$

Then:

$$
\sum_{i=1}^n x_i^2 = 0.
$$

A sum of nonnegative numbers is zero **if and only if** every term is zero. Hence:

$$
x_i^2 = 0 \quad \forall i \Rightarrow x_i=0 \quad \forall i.
$$

Thus  $x=0$ .

Conversely, if  $x=0$ , then clearly  $\langle x,x\rangle=0$ .

∎

### Meaning

This is the axiom that turns algebra into geometry.

*    $\langle x,x\rangle$  behaves like “squared length.”
*   Zero is detected _exactly_.
*   No nonzero vector has zero “length.”

This property fails over many other fields (e.g., finite fields), which is why Euclidean geometry is special to  $\mathbb R$ .

* * *

2.1.6 Consequence: linearity in the second argument
---------------------------------------------------

Because the dot product is symmetric:

$$
\langle x, ay+bz\rangle = \langle ay+bz, x\rangle = a\langle y,x\rangle + b\langle z,x\rangle = a\langle x,y\rangle + b\langle x,z\rangle.
$$

So the dot product is **bilinear**:

*   linear in each argument separately.

This fact will be used constantly.

* * *

2.1.7 The dot product as a bilinear form
----------------------------------------

At this point, we can reframe the dot product abstractly.

Define:

$$
\langle \cdot,\cdot\rangle : \mathbb R^n \times \mathbb R^n \to \mathbb R.
$$

This map is:

*   bilinear,
*   symmetric,
*   positive definite.

Such an object is called a **(real) inner product**.

So:

> The dot product is not _an example_ of an inner product on  $\mathbb R^n$ .  
> It is _the canonical inner product_ inherited from coordinates.

Later, we will see that:

*   different inner products correspond to different geometries,
*   the dot product corresponds to standard Euclidean geometry.

* * *

2.1.8 Orthogonality emerges immediately
---------------------------------------

### Definition

Vectors  $x,y\in\mathbb R^n$  are **orthogonal** if:

$$
\langle x,y\rangle = 0.
$$

This definition is **purely algebraic**.

Yet it captures exactly the geometric notion of perpendicularity.

Key properties (proved algebraically):

*   If  $x\perp y$ , then for all scalars  $\alpha,\beta$ ,
    $$
    \alpha x \perp \beta y.
    $$
*   If  $x\perp y$ , then:
    $$
    \langle x+y, x-y\rangle = \langle x,x\rangle - \langle y,y\rangle.
    $$

Proof of the second:

$$
\langle x+y, x-y\rangle = \langle x,x\rangle - \langle x,y\rangle + \langle y,x\rangle - \langle y,y\rangle = \langle x,x\rangle - \langle y,y\rangle,
$$

since  $\langle x,y\rangle=\langle y,x\rangle=0$ .

This algebraic identity underlies right-triangle geometry later.

* * *

2.1.9 The dot product as “measuring alignment”
----------------------------------------------

A crucial interpretation—proved later formally via Cauchy–Schwarz—is:

*    $\langle x,y\rangle > 0$ : vectors point in roughly the same direction.
*    $\langle x,y\rangle = 0$ : vectors are orthogonal.
*    $\langle x,y\rangle < 0$ : vectors point in opposite directions.

But note carefully:

> This interpretation is **derived**, not assumed.

Right now, we only know:

*   dot product is bilinear,
*   symmetric,
*   positive definite.

Everything geometric must be proved from these properties.

* * *

2.1.10 Why inner products are extra structure (not automatic)
-------------------------------------------------------------

Important conceptual checkpoint:

*   A vector space **does not** automatically have an inner product.
*   Inner products are **choices**.

Example:

*    $\mathbb R^n$  can carry infinitely many inner products.
*   The dot product is the standard one, but others exist:
    $$
    \langle x,y\rangle_M := x^\top M y
    $$
    where  $M$  is symmetric positive definite.

Each such choice gives a different notion of length, angle, and orthogonality.

So:

> Linear algebra = vector spaces + linear maps  
> Euclidean geometry = vector spaces + inner product

This distinction becomes critical in optimization and numerical analysis.

* * *

2.1.11 Mastery checklist for 2.1
--------------------------------

You fully understand 2.1 if you can:

*   State the dot product definition and expand it componentwise.
*   Prove symmetry, bilinearity, and positive definiteness _from the definition_.
*   Explain why positive definiteness detects the zero vector.
*   Explain why the dot product is additional structure, not part of the vector space axioms.
*   Define orthogonality algebraically and manipulate it using bilinearity.

* * *

### Where this leads next

With the dot product in place, we can now **derive**:

*   norms (lengths) rigorously → **2.2**,
*   Cauchy–Schwarz inequality,
*   triangle inequality,
*   projections and least squares → **2.3**.

Everything geometric from here on is a theorem, not a picture.

If you’re ready, the next step is **2.2: the norm induced by the inner product**, where length, distance, and inequality structure appear for the first time.

## Response:
Got it. Let’s take 2.1 and do it “from bedrock”: not just _prove the axioms from the formula_, but also (i) explain why these axioms are exactly what you need, (ii) show how the dot product is the unique “coordinatewise” such object up to a change of basis, (iii) connect it to linear functionals and matrices, and (iv) lay down the lemmas you’ll repeatedly use in 2.2–2.3 (Cauchy–Schwarz, projections) without yet proving what belongs to 2.2–2.3.

I’ll keep the scope strictly inside 2.1 (inner product + basic consequences), but I’ll be richer and more systematic.

* * *

2.1 Dot product as an inner product on  $\mathbb R^n$ 
------------------------------------------------------

### 2.1.0 What new structure are we adding, exactly?

A vector space gives you:

*   addition  $x+y$ ,
*   scalar multiplication  $\alpha x$ ,

and nothing else. That is enough to talk about:

*   linear combinations,
*   span,
*   subspaces,
*   dimension,
*   linear maps.

But it is **not** enough to talk about:

*   lengths,
*   angles,
*   perpendicularity,
*   distance,
*   “closest point” problems.

Those require a way to **compare** vectors numerically. An inner product is precisely such a comparison device: it produces a real number from a pair of vectors in a way that is compatible with linear structure.

So in 2.1 we are doing an extension:

$$
(\mathbb R^n,\; +,\; \cdot)\quad \longrightarrow \quad (\mathbb R^n,\; +,\; \cdot,\; \langle \cdot,\cdot\rangle).
$$

The inner product is extra structure. You choose it.

* * *

2.1.1 The abstract definition: inner product (real case)
--------------------------------------------------------

Let  $V$  be a real vector space. An **inner product** on  $V$  is a function

$$
\langle \cdot,\cdot\rangle : V\times V \to \mathbb R
$$

satisfying, for all  $x,y,z\in V$  and  $a,b\in\mathbb R$ :

1.  **Linearity in the first argument** (additivity + homogeneity):
    
$$
\langle ax+by,\; z\rangle = a\langle x,z\rangle + b\langle y,z\rangle.
$$
2.  **Symmetry**:
    
$$
\langle x,y\rangle = \langle y,x\rangle.
$$
3.  **Positive definiteness**:
    
$$
\langle x,x\rangle \ge 0,\qquad \langle x,x\rangle = 0 \iff x=0.
$$

A few meta-notes that matter:

*   In the **real** case, symmetry + linearity in first argument implies linearity in second argument as a theorem (we’ll prove it).
*   In the **complex** case, symmetry is replaced by conjugate symmetry; we’ll flag that precisely later.

* * *

2.1.2 The concrete definition: dot product on  $\mathbb R^n$ 
-------------------------------------------------------------

Let  $x=(x_1,\dots,x_n)$ ,  $y=(y_1,\dots,y_n)\in\mathbb R^n$ .

### Definition (dot product)

$$
\boxed{ \langle x,y\rangle := x^\top y := \sum_{i=1}^n x_i y_i. }
$$

This is a map  $\mathbb R^n\times\mathbb R^n \to \mathbb R$  because the sum of real numbers is real.

Now we prove it satisfies the inner product axioms.

* * *

2.1.3 Proof that the dot product is an inner product (fully expanded)
---------------------------------------------------------------------

### Axiom 1: symmetry

**Claim.**  $\langle x,y\rangle=\langle y,x\rangle$ .

**Proof.**  
By definition:

$$
\langle x,y\rangle = \sum_{i=1}^n x_i y_i.
$$

In  $\mathbb R$ , multiplication is commutative:  $x_i y_i = y_i x_i$ . Substitute:

$$
\sum_{i=1}^n x_i y_i = \sum_{i=1}^n y_i x_i = \langle y,x\rangle.
$$

∎

**What this buys later.**  
Symmetry ensures “orthogonality” is mutual and makes the geometry undirected.

* * *

### Axiom 2: linearity in the first argument

We prove both additivity and homogeneity (then combine).

#### (a) Additivity:  $\langle x+y, z\rangle = \langle x,z\rangle + \langle y,z\rangle$ 

**Proof.**

$$
\langle x+y, z\rangle = \sum_{i=1}^n (x+y)_i z_i.
$$

But by definition of vector addition in  $\mathbb R^n$ ,  $(x+y)_i = x_i + y_i$ . So:

$$
= \sum_{i=1}^n (x_i+y_i) z_i.
$$

Distribute multiplication over addition in  $\mathbb R$ :

$$
(x_i+y_i)z_i = x_i z_i + y_i z_i.
$$

So:

$$
\langle x+y, z\rangle = \sum_{i=1}^n (x_i z_i + y_i z_i).
$$

Split the sum (property of finite sums):

$$
= \sum_{i=1}^n x_i z_i + \sum_{i=1}^n y_i z_i = \langle x,z\rangle + \langle y,z\rangle.
$$

∎

#### (b) Homogeneity:  $\langle a x, z\rangle = a\langle x,z\rangle$ 

**Proof.**

$$
\langle ax, z\rangle = \sum_{i=1}^n (ax)_i z_i.
$$

By definition of scalar multiplication,  $(ax)_i = a x_i$ . So:

$$
= \sum_{i=1}^n (a x_i) z_i = \sum_{i=1}^n a(x_i z_i).
$$

Factor out the constant  $a$  from a finite sum:

$$
= a \sum_{i=1}^n x_i z_i = a\langle x,z\rangle.
$$

∎

#### (c) Combine:  $\langle ax+by, z\rangle = a\langle x,z\rangle+b\langle y,z\rangle$ 

Use additivity + homogeneity:

$$
\langle ax+by, z\rangle = \langle ax, z\rangle + \langle by, z\rangle = a\langle x,z\rangle + b\langle y,z\rangle.
$$

∎

**What this buys later.**  
This is the key “pull linear combinations through” rule. It will turn dot products into algebraic tools.

* * *

### Axiom 3: positive definiteness

**Claim.**  $\langle x,x\rangle \ge 0$ , and equality holds iff  $x=0$ .

**Proof (nonnegativity).**

$$
\langle x,x\rangle = \sum_{i=1}^n x_i x_i = \sum_{i=1}^n x_i^2.
$$

Each term  $x_i^2 \ge 0$  for real  $x_i$ . Sum of nonnegative numbers is nonnegative. Hence  $\langle x,x\rangle \ge 0$ .

**Proof (zero iff  $x=0$ ).**  
Assume  $\langle x,x\rangle = 0$ . Then:

$$
\sum_{i=1}^n x_i^2 = 0.
$$

Each  $x_i^2 \ge 0$ . A finite sum of nonnegative reals equals 0 **only if** each term is 0:

$$
x_i^2 = 0 \quad \forall i.
$$

But  $x_i^2=0$  implies  $x_i=0$  in  $\mathbb R$ . Therefore all components are zero, so  $x=0$ .

Conversely, if  $x=0$  then all  $x_i=0$ , so  $\langle x,x\rangle=0$ .  
∎

**What this buys later.**  
This is the mechanism for defining a norm by  $\|x\|=\sqrt{\langle x,x\rangle}$ . Positive definiteness is what makes it a genuine length (no nonzero vector has zero length).

* * *

2.1.4 Immediate theorem: bilinearity (linearity in the second argument too)
---------------------------------------------------------------------------

In the real case, symmetry converts linearity in the first argument into linearity in the second.

### Proposition (linearity in second argument)

For all  $x,y,z\in\mathbb R^n$  and  $a,b\in\mathbb R$ ,

$$
\langle x, ay+bz\rangle = a\langle x,y\rangle + b\langle x,z\rangle.
$$

**Proof.**  
Using symmetry:

$$
\langle x, ay+bz\rangle = \langle ay+bz, x\rangle.
$$

Apply linearity in the first argument:

$$
\langle ay+bz, x\rangle = a\langle y,x\rangle + b\langle z,x\rangle.
$$

Apply symmetry again:

$$
\langle y,x\rangle = \langle x,y\rangle,\quad \langle z,x\rangle = \langle x,z\rangle.
$$

So:

$$
\langle x, ay+bz\rangle = a\langle x,y\rangle + b\langle x,z\rangle.
$$

∎

So the dot product is **bilinear** + symmetric + positive definite.

* * *

2.1.5 Inner products produce linear functionals (a key structural viewpoint)
----------------------------------------------------------------------------

Fix a vector  $y\in\mathbb R^n$ . Define a function:

$$
\varphi_y : \mathbb R^n \to \mathbb R,\qquad \varphi_y(x) := \langle x,y\rangle.
$$

### Proposition

 $\varphi_y$  is a **linear map** (a linear functional).

**Proof.**  
For any  $x_1,x_2$  and scalars  $a,b$ :

$$
\varphi_y(ax_1+bx_2) = \langle ax_1+bx_2,\; y\rangle = a\langle x_1,y\rangle + b\langle x_2,y\rangle = a\varphi_y(x_1)+b\varphi_y(x_2).
$$

∎

Interpretation (very important later):

*   An inner product lets you convert a vector  $y$  into a linear measurement device  $x\mapsto\langle x,y\rangle$ .
*   In more advanced language: it identifies  $V$  with its dual space  $V^*$  (Riesz representation), but we won’t assume that yet—this is the seed.

* * *

2.1.6 Orthogonality: definition and basic algebraic properties
--------------------------------------------------------------

### Definition

 $x$  and  $y$  are **orthogonal**, written  $x\perp y$ , if:

$$
\langle x,y\rangle = 0.
$$

This definition is purely algebraic. Geometry comes later via theorems.

#### Proposition 1: scaling preserves orthogonality

If  $x\perp y$ , then for all scalars  $a,b$ ,

$$
(ax)\perp(by).
$$

**Proof.**

$$
\langle ax, by\rangle = ab\langle x,y\rangle = ab\cdot 0 = 0.
$$

∎

#### Proposition 2: orthogonality with a sum is a linear constraint

For fixed  $y$ , the set

$$
H_y := \{x\in\mathbb R^n : \langle x,y\rangle=0\}
$$

is a subspace (and when  $y\neq 0$ , it is a hyperplane through the origin).

**Proof (subspace).**

*    $0\in H_y$  because  $\langle 0,y\rangle=0$ .
*   If  $x_1,x_2\in H_y$ , then:
    $$
    \langle x_1+x_2, y\rangle = \langle x_1,y\rangle + \langle x_2,y\rangle = 0+0=0.
    $$
*   If  $x\in H_y$  and  $a\in\mathbb R$ , then:
    $$
    \langle ax, y\rangle = a\langle x,y\rangle = a\cdot 0 = 0.
    $$

So it’s a subspace. ∎

This is a key bridge to optimization constraints like  $a^\top x = b$ : dot products define linear equations.

* * *

2.1.7 Matrix viewpoint: dot product as a special bilinear form
--------------------------------------------------------------

The dot product is the bilinear form associated with the identity matrix.

For  $x,y\in\mathbb R^n$ ,

$$
\langle x,y\rangle = x^\top y = x^\top I y.
$$

More generally, for any symmetric matrix  $M$ ,

$$
\langle x,y\rangle_M := x^\top M y
$$

is bilinear and symmetric. It is an inner product **iff**  $M$  is **symmetric positive definite** (SPD):

$$
x^\top M x > 0 \quad \forall x\neq 0.
$$

This matters because it tells you:

*   inner products correspond to SPD matrices (in coordinates),
*   choosing an inner product is choosing a geometry.

We won’t prove the full “iff” classification yet, but the direction “SPD ⇒ inner product” is straightforward:

*   bilinear: matrix multiplication distributes
*   symmetric:  $M=M^\top$ 
*   positive definite: definition of SPD

This is the first taste that “geometry” is encoded by matrices.

* * *

2.1.8 Why the dot product is special in  $\mathbb R^n$ 
-------------------------------------------------------

Two reasons:

### (A) It is coordinatewise and canonical once you choose the standard basis

In the standard basis  $e_1,\dots,e_n$ ,

$$
\langle e_i,e_j\rangle = \delta_{ij} = \begin{cases} 1 & i=j\\ 0 & i\neq j. \end{cases}
$$

This property encodes “axes are perpendicular and unit length.”

You can verify it directly:

$$
\langle e_i,e_j\rangle = \sum_{k=1}^n (e_i)_k (e_j)_k.
$$

But  $(e_i)_k$  is 1 if  $k=i$  else 0. The product is 1 exactly when  $i=j=k$ , else 0, so the sum is  $\delta_{ij}$ .

### (B) It makes the standard coordinates orthonormal

This is the core of Euclidean geometry: coordinates behave like perpendicular unit directions.

Later, Gram–Schmidt will construct such bases in general.

* * *

2.1.9 Complex warning (so you don’t get ambushed later)
-------------------------------------------------------

Over  $\mathbb C^n$ , if you define  $\sum x_i y_i$ , you do **not** get positive definiteness because  $x_i^2$  can be complex and sums don’t compare to 0.

The correct complex inner product is:

$$
\langle x,y\rangle := \sum_{i=1}^n \overline{x_i}\, y_i = x^* y,
$$

which is:

*   linear in the second argument,
*   conjugate-linear in the first,
*   conjugate-symmetric:  $\langle x,y\rangle=\overline{\langle y,x\rangle}$ ,
*   positive definite:  $\langle x,x\rangle = \sum |x_i|^2 \ge 0$ .

For now we are purely in  $\mathbb R^n$ , but it’s worth seeing why the real case was “simpler.”

* * *

2.1.10 The key identities you should be fluent with (all proved from bilinearity)
---------------------------------------------------------------------------------

These are used constantly later; I’ll derive them now.

### Identity 1:  $\langle x,0\rangle = 0$  and  $\langle 0,y\rangle=0$ 

Proof:

$$
\langle x,0\rangle = \langle x, 0\cdot 0\rangle = 0\langle x,0\rangle = 0
$$

is a bit circular, so do it cleanly using additivity:

$$
\langle x,0\rangle = \langle x,0+0\rangle = \langle x,0\rangle + \langle x,0\rangle.
$$

Subtract  $\langle x,0\rangle$  from both sides (allowed in  $\mathbb R$ ):

$$
0 = \langle x,0\rangle.
$$

Similarly for  $\langle 0,y\rangle$ . ∎

### Identity 2:  $\langle x,-y\rangle = -\langle x,y\rangle$ 

Proof:

$$
\langle x,-y\rangle = \langle x, (-1)y\rangle = (-1)\langle x,y\rangle = -\langle x,y\rangle.
$$

∎

### Identity 3: Polarization (real case preview)

You can recover the dot product from “squared lengths”:

$$
\langle x,y\rangle = \frac{1}{2}\big(\langle x+y,x+y\rangle - \langle x,x\rangle - \langle y,y\rangle\big).
$$

Proof is just expanding using bilinearity:

$$
\langle x+y,x+y\rangle = \langle x,x\rangle + 2\langle x,y\rangle + \langle y,y\rangle.
$$

Rearrange. ∎

This matters later: the inner product is encoded by the norm it induces.

* * *

2.1.11 What you should mentally conclude (the “compressed meaning”)
-------------------------------------------------------------------

After this richer 2.1, you should have these truths locked in:

1.  The dot product is a **specific inner product** on  $\mathbb R^n$ .
2.  An inner product is exactly: symmetric + bilinear + positive definite.
3.  Fixing one argument gives a **linear functional** in the other.
4.  Orthogonality is just the equation  $\langle x,y\rangle=0$ , and its solution set is a subspace (hyperplane when  $y\neq0$ ).
5.  Dot product is  $x^\top I y$ ; more general inner products are  $x^\top M y$  with  $M$  SPD.
6.  All geometric facts (angles, projections, least squares) are **theorems** derived from these axioms.

* * *

2.1.12 Mastery checklist (stronger)
-----------------------------------

You’re genuinely fluent with 2.1 if you can do all of this without guessing:

*   Prove symmetry, bilinearity, positive definiteness from  $\sum x_i y_i$ .
*   Prove linearity in the second argument using symmetry.
*   Show  $x\mapsto \langle x,y\rangle$  is a linear map and compute it explicitly.
*   Show  $\{x:\langle x,y\rangle=0\}$  is a subspace and say why it’s codimension 1 when  $y\neq0$  (we’ll formalize codimension later, but you should see the idea).
*   Expand  $\langle x+y,x+y\rangle$  correctly and derive polarization.

* * *

If you want the strict roadmap continuation, the next item is **2.2: the norm induced by an inner product**, and there we will (i) define  $\|x\|=\sqrt{\langle x,x\rangle}$ , (ii) prove norm axioms, and (iii) prove Cauchy–Schwarz and triangle inequality rigorously from scratch.

## Response:
2.2 Norm induced by an inner product
------------------------------------

_(length, distance, and inequality — all derived, nothing assumed)_

In 2.1 we introduced an **inner product** as extra structure on a vector space, and we proved—from the coordinate formula—that the dot product on  $\mathbb R^n$  is symmetric, bilinear, and positive definite.

Now we do something very precise and very important:

> **We derive a notion of length from the inner product, and we prove—rigorously—that it satisfies exactly the axioms required of a norm.**

Nothing about “length” is assumed.  
Everything comes from the inner product axioms plus field properties of  $\mathbb R$ .

This section has four logical blocks:

1.  Definition of the induced norm
2.  Proof of the norm axioms (with all dependencies explicit)
3.  Cauchy–Schwarz inequality (proved from scratch)
4.  Triangle inequality (derived, not guessed)

* * *

2.2.0 Why norms are not automatic
---------------------------------

A vector space by itself has **no canonical notion of size**.

*   You can add vectors.
*   You can scale vectors.
*   But there is no intrinsic meaning to “this vector is longer than that one.”

An inner product changes that by assigning a real number  $\langle x,x\rangle$  to each vector  $x$ , which:

*   is nonnegative,
*   vanishes only at zero.

This suggests interpreting  $\langle x,x\rangle$  as a _squared length_.  
The square root then gives length.

This is not an intuition—it’s a construction.

* * *

2.2.1 Definition: norm induced by an inner product
--------------------------------------------------

Let  $(V,\langle\cdot,\cdot\rangle)$  be a real inner product space.  
(In particular, take  $V=\mathbb R^n$  with the dot product.)

### Definition (induced norm)

For any  $x\in V$ , define:

$$
\boxed{ \|x\| := \sqrt{\langle x,x\rangle}. }
$$

This is well-defined because:

*    $\langle x,x\rangle \ge 0$  by positive definiteness,
*   the square root of a nonnegative real number exists and is unique in  $\mathbb R$ .

We now prove that this function  $\|\cdot\|$  satisfies the **norm axioms**.

* * *

2.2.2 Norm axioms (what we must prove)
--------------------------------------

A function  $\|\cdot\|:V\to\mathbb R$  is a **norm** if for all  $x,y\in V$  and all scalars  $\alpha\in\mathbb R$ :

1.  **Nonnegativity and definiteness**
    
$$
\|x\|\ge 0, \quad \|x\|=0 \iff x=0.
$$
2.  **Absolute homogeneity**
    
$$
\|\alpha x\| = |\alpha|\,\|x\|.
$$
3.  **Triangle inequality**
    
$$
\|x+y\| \le \|x\| + \|y\|.
$$

We will prove each, but note carefully:

*   (1) and (2) are straightforward consequences of inner product axioms.
*   (3) is not trivial. It requires a deep inequality: **Cauchy–Schwarz**.

So the logical dependency is:

$$
\text{Inner product} \Rightarrow \text{Cauchy–Schwarz} \Rightarrow \text{Triangle inequality}.
$$

We will respect that order.

* * *

2.2.3 Norm axiom 1: nonnegativity and definiteness
--------------------------------------------------

### Claim

$$
\|x\| \ge 0, \quad \|x\| = 0 \iff x=0.
$$

### Proof

By definition:

$$
\|x\| = \sqrt{\langle x,x\rangle}.
$$
*   Since  $\langle x,x\rangle \ge 0$ , its square root is  $\ge 0$ .  
    So  $\|x\|\ge 0$ .
*    $\|x\| = 0 \iff \sqrt{\langle x,x\rangle}=0 \iff \langle x,x\rangle=0$ .

By **positive definiteness** of the inner product:

$$
\langle x,x\rangle=0 \iff x=0.
$$

Hence:

$$
\|x\|=0 \iff x=0.
$$

∎

This axiom is where positive definiteness does its real work.

* * *

2.2.4 Norm axiom 2: absolute homogeneity
----------------------------------------

### Claim

$$
\|\alpha x\| = |\alpha|\,\|x\| \quad \forall \alpha\in\mathbb R.
$$

### Proof

Start from the definition:

$$
\|\alpha x\| = \sqrt{\langle \alpha x,\alpha x\rangle}.
$$

Use bilinearity of the inner product:

$$
\langle \alpha x,\alpha x\rangle = \alpha^2 \langle x,x\rangle.
$$

Thus:

$$
\|\alpha x\| = \sqrt{\alpha^2 \langle x,x\rangle} = \sqrt{\alpha^2}\,\sqrt{\langle x,x\rangle}.
$$

Now, in  $\mathbb R$ ,

$$
\sqrt{\alpha^2} = |\alpha|.
$$

Therefore:

$$
\|\alpha x\| = |\alpha|\,\|x\|.
$$

∎

This is why the absolute value appears: lengths are insensitive to direction.

* * *

2.2.5 Interlude: why the triangle inequality is hard
----------------------------------------------------

At this point, we **cannot yet** prove:

$$
\|x+y\| \le \|x\| + \|y\|.
$$

Why? Because expanding:

$$
\|x+y\|^2 = \langle x+y,x+y\rangle = \langle x,x\rangle + 2\langle x,y\rangle + \langle y,y\rangle,
$$

we get a cross term  $\langle x,y\rangle$ .

To control that term, we need a bound of the form:

$$
|\langle x,y\rangle| \le \|x\|\,\|y\|.
$$

This inequality is **not obvious** and must be proved.

That inequality is the **Cauchy–Schwarz inequality**, and it is the mathematical hinge of Euclidean geometry.

* * *

2.2.6 Cauchy–Schwarz inequality (full proof)
--------------------------------------------

### Theorem (Cauchy–Schwarz)

For all  $x,y\in V$ ,

$$
\boxed{ |\langle x,y\rangle| \le \|x\|\,\|y\|. }
$$

Moreover, equality holds **if and only if**  $x$  and  $y$  are linearly dependent.

* * *

### Proof (standard, but fully unpacked)

If  $y=0$ , then:

$$
\langle x,y\rangle = 0, \quad \|y\|=0,
$$

so the inequality becomes  $0 \le 0$ , which holds.  
So assume  $y\neq 0$ .

Consider the function:

$$
f(t) := \|x - t y\|^2 = \langle x - t y,\; x - t y\rangle, \quad t\in\mathbb R.
$$

#### Step 1: expand  $f(t)$ 

Using bilinearity and symmetry:

$$
\begin{aligned} f(t) &= \langle x,x\rangle - 2t\langle x,y\rangle + t^2 \langle y,y\rangle. \end{aligned}
$$

So  $f(t)$  is a quadratic polynomial in  $t$ :

$$
f(t) = \|y\|^2 t^2 - 2\langle x,y\rangle t + \|x\|^2.
$$

#### Step 2: use nonnegativity

By definition of norm:

$$
f(t) = \|x - ty\|^2 \ge 0 \quad \text{for all } t\in\mathbb R.
$$

A quadratic polynomial  $at^2 + bt + c$  with  $a>0$  is nonnegative for all  $t$  **if and only if** its discriminant is  $\le 0$ .

Here:

*    $a = \|y\|^2 > 0$ ,
*    $b = -2\langle x,y\rangle$ ,
*    $c = \|x\|^2$ .

So we must have:

$$
b^2 - 4ac \le 0.
$$

#### Step 3: compute the discriminant

$$
(-2\langle x,y\rangle)^2 - 4(\|y\|^2)(\|x\|^2) \le 0.
$$

Simplify:

$$
4\langle x,y\rangle^2 \le 4\|x\|^2\|y\|^2.
$$

Divide by 4:

$$
\langle x,y\rangle^2 \le \|x\|^2\|y\|^2.
$$

Take square roots:

$$
|\langle x,y\rangle| \le \|x\|\,\|y\|.
$$

This proves the inequality.

* * *

### Equality condition

Equality holds iff the discriminant is exactly zero, i.e.

$$
x - t y = 0 \quad \text{for some } t\in\mathbb R.
$$

That means:

$$
x = ty,
$$

so  $x$  and  $y$  are linearly dependent.

∎

* * *

2.2.7 Norm axiom 3: triangle inequality
---------------------------------------

Now we can finally prove the triangle inequality.

### Claim

$$
\|x+y\| \le \|x\| + \|y\|.
$$

### Proof

Start from:

$$
\|x+y\|^2 = \langle x+y,x+y\rangle.
$$

Expand:

$$
= \langle x,x\rangle + 2\langle x,y\rangle + \langle y,y\rangle = \|x\|^2 + 2\langle x,y\rangle + \|y\|^2.
$$

Apply Cauchy–Schwarz:

$$
\langle x,y\rangle \le |\langle x,y\rangle| \le \|x\|\,\|y\|.
$$

So:

$$
\|x+y\|^2 \le \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\|+\|y\|)^2.
$$

Both sides are nonnegative, so taking square roots preserves inequality:

$$
\|x+y\| \le \|x\| + \|y\|.
$$

∎

This completes the proof that  $\|\cdot\|$  is a norm.

* * *

2.2.8 Distance induced by the norm (derived, not defined)
---------------------------------------------------------

Once you have a norm, you automatically get a notion of **distance**:

$$
d(x,y) := \|x-y\|.
$$

This satisfies:

*    $d(x,y)\ge 0$ ,
*    $d(x,y)=0 \iff x=y$ ,
*    $d(x,y)=d(y,x)$ ,
*   triangle inequality:
    $$
    d(x,z)\le d(x,y)+d(y,z).
    $$

So Euclidean distance is **not primitive**.  
It is induced from the inner product via the norm.

* * *

2.2.9 What really happened conceptually
---------------------------------------

Let’s compress the logic chain:

1.  Inner product gives a quadratic form  $x\mapsto\langle x,x\rangle$ .
2.  Positive definiteness makes it behave like squared length.
3.  Square root gives a norm.
4.  Cauchy–Schwarz controls cross terms.
5.  Triangle inequality follows.
6.  Distance follows automatically.

Nothing geometric was assumed.  
Everything was _forced_ by algebra.

* * *

2.2.10 Mastery checklist for 2.2
--------------------------------

You truly understand this section if you can:

*   Prove norm axioms (1) and (2) directly from inner product axioms.
*   Prove Cauchy–Schwarz _from scratch_ using the quadratic argument.
*   Identify exactly where positivity and bilinearity are used.
*   Derive triangle inequality cleanly from Cauchy–Schwarz.
*   Explain why the norm and distance are not additional structure but consequences.

* * *

At this point, you now have:

*   linear structure (Phase 1),
*   metric structure (2.1–2.2).

The next step, **2.3**, is where this machinery becomes _constructive_:  
**orthogonality and projection**, which is the conceptual core of least squares, regression, and optimization.

When ready, we proceed to **2.3 Orthogonality and projection** with the same rigor.

## Response:
2.3 Orthogonality and projection
--------------------------------

_(how inner products turn geometry into computation, and why least squares is inevitable)_

By the end of 2.2, we achieved something very strong:

*   From an inner product, we **derived** a norm.
*   From the norm, we **derived** distance.
*   From distance, we obtained a precise notion of “closeness.”

But all of this is still _passive_.  
We can measure lengths and distances, but we haven’t yet **constructed optimal vectors**.

Section 2.3 is where linear algebra becomes _active_:

> Given a vector and a subspace, how do we find the **closest vector in the subspace**?

This question is not cosmetic. It is the mathematical core of:

*   orthogonal decomposition,
*   least squares,
*   regression,
*   projections,
*   normal equations,
*   optimization with quadratic objectives.

We will proceed with extreme care and full rigor.

* * *

2.3.0 What new problem are we solving?
--------------------------------------

Fix:

*   a real inner product space  $(V,\langle\cdot,\cdot\rangle)$ ,
*   a subspace  $W \subset V$ ,
*   a vector  $x \in V$  (not necessarily in  $W$ ).

We ask:

> Among all vectors  $w \in W$ , which one minimizes the distance  $\|x - w\|$ ?

This is a **well-posed optimization problem**:

*   objective: minimize  $\|x - w\|^2$ ,
*   feasible set: a linear subspace  $W$ .

We will show:

1.  A minimizer exists.
2.  It is unique.
3.  It is characterized by **orthogonality**.
4.  It is a linear operation in  $x$ .

Nothing is assumed. Everything is proved.

* * *

2.3.1 Orthogonality revisited (now as a constraint)
---------------------------------------------------

Recall from 2.1:

### Definition (orthogonality)

Vectors  $u,v \in V$  are **orthogonal**, written  $u \perp v$ , if

$$
\langle u,v\rangle = 0.
$$

This is not geometry yet; it is an algebraic condition.

### Definition (orthogonal complement)

Given a subspace  $W \subset V$ , define its **orthogonal complement**:

$$
W^\perp := \{v \in V : \langle v,w\rangle = 0 \ \forall w \in W\}.
$$

This is the set of all vectors orthogonal to **every** vector in  $W$ .

* * *

2.3.2 First structural result:  $W^\perp$  is a subspace
--------------------------------------------------------

This must be proved, not assumed.

### Proposition

 $W^\perp$  is a linear subspace of  $V$ .

### Proof

We verify the three subspace properties.

1.  **Zero vector**  
    For any  $w \in W$ ,
    
$$
\langle 0, w\rangle = 0.
$$

Hence  $0 \in W^\perp$ .

2.  **Closure under addition**  
    Let  $v_1,v_2 \in W^\perp$ . For any  $w \in W$ ,
    
$$
\langle v_1+v_2, w\rangle = \langle v_1,w\rangle + \langle v_2,w\rangle = 0 + 0 = 0.
$$

So  $v_1+v_2 \in W^\perp$ .

3.  **Closure under scalar multiplication**  
    Let  $v \in W^\perp$ ,  $\alpha \in \mathbb R$ . For any  $w \in W$ ,
    
$$
\langle \alpha v, w\rangle = \alpha \langle v,w\rangle = \alpha \cdot 0 = 0.
$$

So  $\alpha v \in W^\perp$ .

Thus  $W^\perp$  is a subspace. ∎

This already tells us: orthogonality is not a vague geometric idea; it defines linear structure.

* * *

2.3.3 The Pythagorean theorem (fully algebraic)
-----------------------------------------------

The Pythagorean theorem is not geometry. It is a bilinear identity.

### Proposition (Pythagorean identity)

If  $u \perp v$ , then

$$
\|u+v\|^2 = \|u\|^2 + \|v\|^2.
$$

### Proof

Expand using the inner product:

$$
\|u+v\|^2 = \langle u+v, u+v\rangle.
$$

Use bilinearity:

$$
= \langle u,u\rangle + \langle u,v\rangle + \langle v,u\rangle + \langle v,v\rangle.
$$

By symmetry and orthogonality:

$$
\langle u,v\rangle = \langle v,u\rangle = 0.
$$

So:

$$
\|u+v\|^2 = \|u\|^2 + \|v\|^2.
$$

∎

This identity will be the engine of minimization.

* * *

2.3.4 The key minimization lemma (distance to a subspace)
---------------------------------------------------------

We now formalize the optimization problem.

Let  $W \subset V$  be a subspace, and let  $x \in V$ .

Suppose we can write:

$$
x = w + z, \quad\text{with } w \in W,\ z \in W^\perp.
$$

### Lemma (optimality of orthogonal decomposition)

For any  $w' \in W$ ,

$$
\|x - w'\|^2 = \|z\|^2 + \|w - w'\|^2.
$$

### Proof

Compute:

$$
x - w' = (w+z) - w' = (w-w') + z.
$$

Now observe:

*    $w-w' \in W$ ,
*    $z \in W^\perp$ ,
*   hence  $(w-w') \perp z$ .

Apply the Pythagorean identity:

$$
\|x-w'\|^2 = \|w-w'\|^2 + \|z\|^2.
$$

∎

### Immediate consequence

The quantity  $\|z\|^2$  is fixed.  
The term  $\|w-w'\|^2$  is minimized **iff**  $w'=w$ .

Thus:

> Among all  $w' \in W$ , the unique minimizer of  $\|x-w'\|$  is  $w$ .

So if such a decomposition exists, the minimizer is automatic.

* * *

2.3.5 Existence and uniqueness of orthogonal decomposition
----------------------------------------------------------

We now prove the central structural theorem.

### Theorem (orthogonal decomposition)

Let  $W$  be a **finite-dimensional** subspace of an inner product space  $V$ .  
Then every vector  $x \in V$  can be written **uniquely** as:

$$
\boxed{ x = w + z, \quad w \in W, \quad z \in W^\perp. }
$$

This is not trivial. We must prove both existence and uniqueness.

* * *

### Proof: uniqueness

Assume:

$$
x = w_1 + z_1 = w_2 + z_2,
$$

with  $w_1,w_2 \in W$  and  $z_1,z_2 \in W^\perp$ .

Subtract:

$$
w_1 - w_2 = z_2 - z_1.
$$

Left side lies in  $W$ .  
Right side lies in  $W^\perp$ .

Thus  $w_1-w_2 \in W \cap W^\perp$ .

But the only vector orthogonal to itself is zero:

$$
\langle v,v\rangle = 0 \Rightarrow v=0.
$$

So:

$$
w_1-w_2 = 0,\quad z_1-z_2 = 0.
$$

Hence  $w_1=w_2$ ,  $z_1=z_2$ . Uniqueness proved.

* * *

### Proof: existence (finite-dimensional case)

Let  $\{u_1,\dots,u_k\}$  be an **orthonormal basis** of  $W$ .  
(Existence will be proved later via Gram–Schmidt; for now assume it.)

Define:

$$
w := \sum_{i=1}^k \langle x, u_i\rangle u_i.
$$

Clearly  $w \in W$ .

Now define:

$$
z := x - w.
$$

We claim  $z \in W^\perp$ .

Take any basis vector  $u_j$ :

$$
\langle z, u_j\rangle = \langle x, u_j\rangle - \sum_{i=1}^k \langle x,u_i\rangle \langle u_i,u_j\rangle.
$$

But orthonormality gives:

$$
\langle u_i,u_j\rangle = \delta_{ij}.
$$

So the sum collapses:

$$
\langle z,u_j\rangle = \langle x,u_j\rangle - \langle x,u_j\rangle = 0.
$$

Since this holds for every basis vector, and inner product is linear,

$$
\langle z,w'\rangle = 0 \quad \forall w' \in W.
$$

Thus  $z \in W^\perp$ .

Existence proved. ∎

* * *

2.3.6 Definition: orthogonal projection
---------------------------------------

This motivates a fundamental operator.

### Definition (orthogonal projection onto  $W$ )

The **orthogonal projection** of  $x$  onto  $W$  is the unique vector:

$$
\boxed{ \operatorname{proj}_W(x) := w, }
$$

where  $x = w + z$  with  $w \in W$ ,  $z \in W^\perp$ .

Equivalently:

$$
\operatorname{proj}_W(x) = \arg\min_{w' \in W} \|x-w'\|.
$$

So projection is not a geometric trick; it is the solution to a precise optimization problem.

* * *

2.3.7 Projection formula in an orthonormal basis
------------------------------------------------

If  $\{u_1,\dots,u_k\}$  is an orthonormal basis of  $W$ , then:

$$
\boxed{ \operatorname{proj}_W(x) = \sum_{i=1}^k \langle x, u_i\rangle u_i. }
$$

This formula is:

*   exact,
*   coordinate-free (basis-dependent but intrinsic),
*   linear in  $x$ .

* * *

2.3.8 Projection is a linear operator
-------------------------------------

This is critical.

### Proposition

 $\operatorname{proj}_W : V \to W$  is a linear map.

### Proof

Let  $x,y \in V$ ,  $\alpha,\beta \in \mathbb R$ . Using the formula:

$$
\operatorname{proj}_W(\alpha x + \beta y) = \sum_{i=1}^k \langle \alpha x + \beta y, u_i\rangle u_i
$$

Use linearity of the inner product:

$$
= \sum_{i=1}^k (\alpha \langle x,u_i\rangle + \beta \langle y,u_i\rangle) u_i = \alpha \operatorname{proj}_W(x) + \beta \operatorname{proj}_W(y).
$$

∎

So projection is a **linear transformation**.

* * *

2.3.9 Fundamental identities of projection
------------------------------------------

These follow immediately from the decomposition.

### Identity 1: idempotence

$$
\operatorname{proj}_W(\operatorname{proj}_W(x)) = \operatorname{proj}_W(x).
$$

Once you project, projecting again does nothing.

### Identity 2: self-adjointness

$$
\langle \operatorname{proj}_W(x), y\rangle = \langle x, \operatorname{proj}_W(y)\rangle \quad \forall x,y.
$$

(This will later connect to symmetric matrices.)

### Identity 3: residual orthogonality

$$
x - \operatorname{proj}_W(x) \in W^\perp.
$$

This is the defining property of the minimizer.

* * *

2.3.10 Least squares as projection (conceptual preview)
-------------------------------------------------------

Suppose:

*    $A \in \mathbb R^{m\times n}$ ,
*    $b \in \mathbb R^m$ ,
*   the system  $Ax=b$  is inconsistent.

The problem:

$$
\min_x \|Ax - b\|^2
$$

is exactly:

> project  $b$  onto the column space of  $A$ .

The residual  $b - Ax^\*$  is orthogonal to the column space:

$$
A^\top(b - Ax^\*) = 0.
$$

These are the **normal equations**.  
They are nothing but orthogonality conditions.

This entire theory rests on 2.3.

* * *

2.3.11 Geometric meaning (now earned)
-------------------------------------

After all proofs, we are finally allowed to say:

*   Projection = “drop a perpendicular”.
*   Orthogonality = “right angle”.
*   Pythagorean theorem = distance decomposition.
*   Least squares = best approximation in a subspace.

But these are **consequences**, not assumptions.

* * *

2.3.12 Mastery checklist for 2.3
--------------------------------

You fully own this section if you can:

*   Define  $W^\perp$  and prove it is a subspace.
*   Prove the Pythagorean identity algebraically.
*   Prove existence and uniqueness of orthogonal decomposition.
*   Derive projection as a minimizer, not a guess.
*   Write and manipulate the projection formula.
*   Explain why least squares is projection.

* * *

At this point, you have crossed a major conceptual threshold:

*   2.1 gave **measurement**,
*   2.2 gave **inequality and distance**,
*   2.3 gives **optimality and decomposition**.

The next natural step is **2.4 Orthogonal bases and Gram–Schmidt**, where we construct the tools that make all of this computationally usable.

Whenever you want, we proceed to **2.4** with the same level of depth.

2/2

## Response:
3.1 Vector spaces — the axiomatic definition
--------------------------------------------

_(what linear algebra really studies, stripped to its irreducible core)_

Up to now, we have been very concrete:

*   Scalars were  $\mathbb R$ .
*   Vectors lived in  $\mathbb R^n$ .
*   Operations were defined coordinatewise.
*   Geometry came from the dot product.

This was intentional. It gave intuition **earned through proofs**, not pictures.

Now we perform a conceptual compression.

> **We extract exactly the properties of  $\mathbb R^n$  that mattered, discard everything accidental (coordinates, dimension, geometry), and keep only what is logically essential.**

That distilled object is a **vector space**.

This section is foundational. Every theorem from here on will depend on it, explicitly or implicitly.

We will proceed in five layers:

1.  Why axiomatize at all
2.  The formal definition (axioms, fully unpacked)
3.  Immediate consequences (proved, not assumed)
4.  Minimal examples and non-examples (to sharpen necessity of axioms)
5.  Structural meaning of each axiom (why it exists, what breaks without it)

No handwaving. No shortcuts.

* * *

3.1.0 Why we need an axiomatic definition
-----------------------------------------

In  $\mathbb R^n$ , we relied on:

*   addition,
*   scalar multiplication,
*   distributive laws,
*   inverses,
*   identities.

But **nothing** in our proofs of:

*   linear combinations,
*   span,
*   independence,
*   projection,
*   least squares,

actually depended on:

*   coordinates,
*   dimension being finite,
*   vectors being tuples,
*   geometry (except when we explicitly added inner products).

So we ask:

> What is the _minimal structure_ needed for all linear-algebraic reasoning to go through?

The answer is: a set with two operations satisfying a specific list of axioms.

That is what a vector space is.

* * *

3.1.1 Ingredients of the definition (before axioms)
---------------------------------------------------

A **vector space** consists of three ingredients:

1.  A field  $\mathbb F$   
    (scalars; already defined rigorously in 0.1)
2.  A set  $V$   
    (the vectors; abstract elements, no coordinates assumed)
3.  Two operations:
    *   **vector addition**:
        $$
        + : V \times V \to V
        $$
    *   **scalar multiplication**:
        $$
        \cdot : \mathbb F \times V \to V
        $$

Everything else will be axioms constraining how these behave.

* * *

3.1.2 The vector space axioms (formal statement)
------------------------------------------------

Let  $\mathbb F$  be a field.  
A **vector space over  $\mathbb F$ ** is a set  $V$  equipped with operations  $+$  and scalar multiplication such that, for all  $u,v,w \in V$  and all  $\alpha,\beta \in \mathbb F$ , the following axioms hold.

We group them logically.

* * *

### A. Axioms for vector addition

_( $V$  must be an abelian group under addition)_

**(VS1) Closure of addition**

$$
u + v \in V.
$$

Addition never leaves the set.

* * *

**(VS2) Associativity of addition**

$$
(u + v) + w = u + (v + w).
$$

This ensures sums of many vectors are unambiguous.

* * *

**(VS3) Commutativity of addition**

$$
u + v = v + u.
$$

Order of addition does not matter.

* * *

**(VS4) Additive identity**  
There exists an element  $0 \in V$  such that

$$
u + 0 = u \quad \forall u \in V.
$$

This element is called the **zero vector**.

* * *

**(VS5) Additive inverses**  
For every  $u \in V$ , there exists an element  $-u \in V$  such that

$$
u + (-u) = 0.
$$

This makes subtraction meaningful.

* * *

### B. Axioms linking scalars and vectors

_(scalar multiplication behaves like scaling)_

**(VS6) Compatibility of scalar multiplication**

$$
\alpha(\beta u) = (\alpha\beta)u.
$$

Scaling twice is the same as scaling once by the product.

* * *

**(VS7) Scalar identity**

$$
1u = u,
$$

where  $1$  is the multiplicative identity in  $\mathbb F$ .

* * *

### C. Distributive axioms

_(this is where linearity lives)_

**(VS8) Distributivity over vector addition**

$$
\alpha(u + v) = \alpha u + \alpha v.
$$

* * *

**(VS9) Distributivity over scalar addition**

$$
(\alpha + \beta)u = \alpha u + \beta u.
$$

* * *

That’s it.

> **A vector space is exactly a set where these nine axioms hold. Nothing more. Nothing less.**

* * *

3.1.3 Immediate consequences (proved rigorously)
------------------------------------------------

These are _not axioms_. They are theorems that follow from the axioms and are used constantly.

We prove them now so you see exactly where they come from.

* * *

### Proposition 1: The zero vector is unique

**Claim.** If  $0$  and  $0'$  both satisfy the additive identity axiom, then  $0 = 0'$ .

**Proof.**

$$
0 = 0 + 0' \quad (\text{since }0'\text{ is identity})
$$

but also:

$$
0 + 0' = 0' \quad (\text{since }0\text{ is identity}).
$$

Hence  $0 = 0'$ . ∎

* * *

### Proposition 2: Additive inverses are unique

**Claim.** For each  $u \in V$ , the vector  $-u$  is unique.

**Proof.**  
Suppose  $v$  and  $w$  both satisfy:

$$
u + v = 0,\quad u + w = 0.
$$

Then:

$$
v = v + 0 = v + (u + w) = (v + u) + w = (u + v) + w = 0 + w = w.
$$

∎

* * *

### Proposition 3:  $0u = 0$  for all  $u \in V$ 

**Proof.**  
Using distributivity over scalar addition:

$$
(0 + 0)u = 0u + 0u.
$$

But  $0 + 0 = 0$ , so:

$$
0u = 0u + 0u.
$$

Add the additive inverse of  $0u$  to both sides:

$$
0 = 0u.
$$

∎

* * *

### Proposition 4:  $\alpha 0 = 0$  for all  $\alpha \in \mathbb F$ 

**Proof.**

$$
\alpha 0 = \alpha(0 + 0) = \alpha 0 + \alpha 0.
$$

Subtract  $\alpha 0$  from both sides to get:

$$
\alpha 0 = 0.
$$

∎

* * *

### Proposition 5:  $(-1)u = -u$ 

**Proof.**

$$
u + (-1)u = (1 + (-1))u = 0u = 0.
$$

So  $(-1)u$  is the additive inverse of  $u$ , hence equals  $-u$ . ∎

* * *

These facts were used constantly in Chapters 1 and 2; now you know their logical origin.

* * *

3.1.4 Why each axiom is necessary (and what breaks without it)
--------------------------------------------------------------

This is crucial for deep understanding.

### If (VS1) fails (closure)

You can add vectors and fall outside the set → linear combinations stop being well-defined.

* * *

### If (VS2) fails (associativity)

Expressions like  $u + v + w$  become ambiguous. Linear combinations cease to be meaningful.

* * *

### If (VS3) fails (commutativity)

Order matters. Span and linear independence become order-dependent — disastrous.

* * *

### If (VS4) fails (zero vector)

You cannot define “no displacement,” null solutions, or homogeneous systems properly.

* * *

### If (VS5) fails (additive inverse)

You cannot subtract vectors. Linear equations break.

* * *

### If (VS6) fails (scalar associativity)

Repeated scaling becomes inconsistent. You lose control of coefficients.

* * *

### If (VS7) fails (scalar identity)

Scaling by 1 would not preserve vectors — coefficients lose meaning.

* * *

### If (VS8) or (VS9) fails (distributivity)

Linear combinations collapse.  
Matrix multiplication, projection, least squares all fail.

> **Every axiom exists because something essential breaks without it.**

* * *

3.1.5 Examples (canonical and nontrivial)
-----------------------------------------

### Example 1:  $\mathbb R^n$ 

*   Scalars:  $\mathbb R$ 
*   Vectors:  $n$ \-tuples
*   Operations: componentwise

This is the **model** vector space.

* * *

### Example 2: Function spaces

Let  $V = \{f : [0,1] \to \mathbb R\}$ .

Define:

$$
(f + g)(x) := f(x) + g(x),\quad (\alpha f)(x) := \alpha f(x).
$$

All axioms hold (proved pointwise).

This shows:

> Vectors need not be arrows or tuples. They can be functions.

* * *

### Example 3: Polynomials

Let  $V = \mathbb R[x]$ , the set of all real polynomials.

Addition and scalar multiplication defined coefficientwise.

Infinite-dimensional vector space.

* * *

### Example 4: Matrices

Let  $V = \mathbb R^{m \times n}$ .

Matrix addition and scalar multiplication satisfy all axioms.

* * *

3.1.6 Non-examples (to sharpen intuition)
-----------------------------------------

### Non-example 1:  $\mathbb R^n$  without the zero vector

Remove  $0$ .  
Fails (VS4) and (VS5). Not a vector space.

* * *

### Non-example 2:  $\mathbb R^n$  with restricted scalars

Let scalars be  $\mathbb R_{\ge 0}$ .  
Fails additive inverses in the field. Scalar multiplication breaks linearity.

* * *

### Non-example 3: Positive functions only

Functions  $f(x) > 0$  on  $[0,1]$ .  
Fails closure under addition and scalar multiplication by negatives.

* * *

These show vector spaces are **fragile**: small changes destroy the structure.

* * *

3.1.7 The philosophical compression (important)
-----------------------------------------------

A vector space is:

> a place where **linear combinations make sense and behave predictably**.

Everything else:

*   dimension,
*   basis,
*   matrices,
*   geometry,
*   optimization,

is built on top of this.

This is why linear algebra is not about  $\mathbb R^n$ .  
It is about **vector spaces**.

* * *

3.1.8 Mastery checklist for 3.1
-------------------------------

You truly understand this section if you can:

*   State all vector space axioms from memory.
*   Explain why each axiom is necessary.
*   Prove basic consequences like  $0u=0$ ,  $(-1)u=-u$ .
*   Identify whether a given structure is a vector space (and which axiom fails if not).
*   See  $\mathbb R^n$  as just one instance of a much larger class.

* * *

### Where this leads next

With the axiomatic definition in place, the next steps are inevitable:

*   **3.2 Subspaces** — recognizing vector spaces inside vector spaces
*   **3.3 Linear combinations revisited (abstractly)**
*   **3.4 Basis and dimension (why coordinates exist at all)**

When ready, we proceed to **3.2** with the same level of rigor and depth.

## Response:
3.2 Subspaces — “closed worlds” inside a vector space
-----------------------------------------------------

_(how linear structure reproduces itself, and why almost everything you study is a subspace)_

In 3.1 we defined a **vector space** as a set where linear combinations behave predictably.  
Now we ask the next unavoidable question:

> If a big vector space exists, when does a **subset** of it inherit the same linear structure?

This is not a technical aside. This is the organizing principle of linear algebra.

*   Solution sets of linear equations are subspaces.
*   Column spaces, null spaces, row spaces are subspaces.
*   Orthogonal complements are subspaces.
*   Feasible directions, tangent spaces, kernels, images — all subspaces.

So 3.2 is where linear algebra becomes _structural_:  
we learn how linear worlds sit inside other linear worlds.

We will proceed very carefully:

1.  Definition of subspace (axiomatic, not heuristic)
2.  Equivalent characterizations (including the one-line test)
3.  Why “closure” is the real content
4.  Immediate consequences and structural lemmas
5.  Canonical examples (null space, range, intersections, sums)
6.  Non-examples that look tempting but fail
7.  Why subspaces are the natural objects of linear algebra

No shortcuts. No pictures. Only structure.

* * *

3.2.0 What “closed world” means (conceptually)
----------------------------------------------

A subspace is not just a subset.  
It is a **self-contained linear universe**:

*   You add two things inside it → you stay inside.
*   You scale anything inside → you stay inside.
*   You never “fall out” when forming linear combinations.

That is what “closed” means here.

This is not topological closure.  
It is **algebraic closure under linear operations**.

* * *

3.2.1 Definition: subspace (full axiomatic form)
------------------------------------------------

Let  $V$  be a vector space over a field  $\mathbb F$ .

### Definition (subspace)

A subset  $W \subseteq V$  is a **subspace of  $V$ ** if:

1.   $W$  is itself a vector space over  $\mathbb F$ ,
2.  with **the same operations** of addition and scalar multiplication as  $V$ .

This definition is correct but inefficient, because it requires checking **all** vector space axioms again.

We now compress it.

* * *

3.2.2 The Subspace Criterion (minimal test)
-------------------------------------------

### Theorem (Subspace Test)

A nonempty subset  $W \subseteq V$  is a subspace **if and only if**:

1.  **Closure under addition**
    $$
    u,v \in W \;\Rightarrow\; u+v \in W
    $$
2.  **Closure under scalar multiplication**
    $$
    u \in W,\ \alpha \in \mathbb F \;\Rightarrow\; \alpha u \in W
    $$

That’s it.

No need to check identities or inverses explicitly.

* * *

### Proof (⇒ direction)

If  $W$  is a vector space under inherited operations, then by the vector space axioms:

*   it is closed under addition,
*   it is closed under scalar multiplication.

So the two conditions hold.

* * *

### Proof (⇐ direction)

Assume  $W$  is nonempty and satisfies the two closure properties.

We must show all vector space axioms hold in  $W$ .

Let  $u,v,w \in W$ ,  $\alpha,\beta \in \mathbb F$ .

1.  **Zero vector exists**  
    Since  $W$  is nonempty, pick  $w_0 \in W$ .  
    By scalar closure,  $0 w_0 = 0 \in W$ .
2.  **Additive inverses exist**  
    For any  $u \in W$ , scalar closure gives  $(-1)u \in W$ .  
    But  $(-1)u = -u$ .
3.  **Associativity, commutativity, distributivity**  
    These hold in  $V$ , and  $W$  uses the same operations, so they hold automatically.

Thus  $W$  is a vector space. ∎

* * *

### Why this test is so powerful

It reduces **nine axioms** to **two checks**.

That is why virtually all subspace proofs use it.

* * *

3.2.3 The “one-line” subspace test (even more compressed)
---------------------------------------------------------

There is an even more compact criterion.

### Corollary (One-line subspace test)

A nonempty subset  $W \subseteq V$  is a subspace **if and only if**:

$$
\forall u,v \in W,\ \forall \alpha,\beta \in \mathbb F, \quad \alpha u + \beta v \in W.
$$

This says:

> ** $W$  is closed under all linear combinations of two vectors.**

* * *

### Proof

*   Taking  $\alpha=\beta=1$  gives closure under addition.
*   Taking  $\beta=0$  gives closure under scalar multiplication.

Conversely, closure under addition and scalar multiplication implies closure under any linear combination.

∎

This form exposes the essence:  
**subspaces are exactly the sets closed under linear combinations.**

* * *

3.2.4 Immediate structural consequences
---------------------------------------

These facts follow instantly but are worth stating explicitly.

* * *

### Proposition 1: Every subspace contains the zero vector

Already proved in the Subspace Test proof, but restated:

> If  $W$  is a subspace, then  $0 \in W$ .

This gives a fast way to rule out non-subspaces.

* * *

### Proposition 2: Subspaces are closed under finite linear combinations

If  $u_1,\dots,u_k \in W$  and  $\alpha_1,\dots,\alpha_k \in \mathbb F$ , then:

$$
\sum_{i=1}^k \alpha_i u_i \in W.
$$

**Proof (by induction)**

*   Base case  $k=1$ : scalar closure.
*   Step  $k \to k+1$ : sum of two elements in  $W$ .

This is why **span** always lands inside the smallest subspace.

* * *

### Proposition 3: Intersection of subspaces is a subspace

Let  $\{W_i\}_{i \in I}$  be any family of subspaces of  $V$ .

Then:

$$
\bigcap_{i \in I} W_i
$$

is a subspace.

**Proof**

*   Nonempty: contains  $0$ , since  $0 \in W_i$  for all  $i$ .
*   Closed under addition and scalar multiplication because each  $W_i$  is.

∎

This fact is crucial for defining “smallest subspace with a property.”

* * *

3.2.5 Canonical examples (the backbone of linear algebra)
---------------------------------------------------------

These are not just examples; they are the main actors.

* * *

### Example 1: The zero subspace and the whole space

*    $\{0\}$  is a subspace.
*    $V$  itself is a subspace.

These are called the **trivial subspaces**.

* * *

### Example 2: Span of a set

Given any subset  $S \subset V$ ,

$$
\mathrm{span}(S)
$$

is a subspace.

In fact, it is:

> the **intersection of all subspaces** that contain  $S$ .

This explains why span is the “smallest closed world” containing  $S$ .

* * *

### Example 3: Null space (kernel)

Let  $T : V \to W$  be a linear map.

Define:

$$
\ker(T) := \{v \in V : T(v) = 0\}.
$$

#### Claim

 $\ker(T)$  is a subspace of  $V$ .

**Proof**

*    $T(0)=0$ , so  $0 \in \ker(T)$ .
*   If  $T(u)=T(v)=0$ , then:
    $$
    T(u+v)=T(u)+T(v)=0.
    $$
*   If  $T(u)=0$ , then:
    $$
    T(\alpha u)=\alpha T(u)=0.
    $$

∎

This is one of the most important subspaces in all of mathematics.

* * *

### Example 4: Range (image)

Define:

$$
\mathrm{range}(T) := \{T(v) : v \in V\}.
$$

This is a subspace of the codomain.

This is the other half of the structure theorem for linear maps.

* * *

### Example 5: Solution set of homogeneous linear equations

Let  $A \in \mathbb R^{m \times n}$ .

$$
\{x \in \mathbb R^n : Ax = 0\}
$$

is a subspace (null space of the linear map  $x \mapsto Ax$ ).

This is why **homogeneous systems are linear**.

* * *

3.2.6 Non-examples (what fails and why)
---------------------------------------

These sharpen understanding by failure.

* * *

### Non-example 1: Affine sets not through the origin

$$
\{x \in \mathbb R^n : Ax = b\}, \quad b \neq 0.
$$

Fails because:

*    $0$  is not a solution.
*   Not closed under scalar multiplication.

These are **affine subspaces**, not linear subspaces.

* * *

### Non-example 2: Unit vectors only

$$
\{x : \|x\| = 1\}.
$$

Fails:

*   Not closed under addition.
*   Not closed under scalar multiplication.

* * *

### Non-example 3: Positive orthant

$$
\mathbb R^n_{\ge 0}.
$$

Fails:

*   Not closed under scalar multiplication by negative scalars.

* * *

### Non-example 4: Polynomials of degree exactly  $n$ 

Fails:

*   Zero polynomial not included.
*   Addition changes degree.

* * *

3.2.7 Why subspaces are the _true objects_ of linear algebra
------------------------------------------------------------

Here is the deep structural insight:

> **Vector spaces are static.  
> Subspaces encode constraints, structure, and solutions.**

When you solve problems, you are almost never studying the entire space. You are studying:

*   directions allowed by constraints,
*   null directions,
*   feasible variations,
*   tangent directions.

All of these are subspaces.

That is why:

*   linear algebra is not about vectors,
*   it is about **subspaces and maps between them**.

* * *

3.2.8 Subspaces as “closed under forgetting coordinates”
--------------------------------------------------------

Another way to see subspaces:

A subspace is a set where you can:

*   forget some information (collapse directions),
*   but never introduce nonlinearity.

This is why projection lands in subspaces, not arbitrary sets.

* * *

3.2.9 Mastery checklist for 3.2
-------------------------------

You fully understand this section if you can:

*   State and use the Subspace Test fluently.
*   Instantly rule out non-subspaces by checking zero or closure.
*   Prove kernels, ranges, intersections are subspaces.
*   Explain why solution sets of  $Ax=0$  are subspaces but  $Ax=b$  are not (unless  $b=0$ ).
*   View subspaces as self-contained linear universes.

* * *

### Where this leads next

Now that we know what subspaces are, the next unavoidable questions are:

*   **3.3 Linear combinations revisited (abstractly)**
*   **3.4 Basis and dimension: why coordinates exist at all**

When you are ready, we proceed to **3.3** with the same depth and rigor.

## Response:
3.2 Subspaces — “closed worlds” (ultra-deep, fully unpacked)
------------------------------------------------------------

A subspace is one of those ideas that looks simple (“a subset closed under addition and scaling”) but is secretly the load-bearing beam of linear algebra. If you really internalize 3.2, then:

*   “Solve  $Ax=b$ ” becomes “understand an affine translate of a subspace.”
*   “Rank” becomes “dimension of a subspace.”
*   “Least squares” becomes “projection onto a subspace.”
*   “Eigenvectors” become “1D invariant subspaces.”
*   “Constraints” become “subspaces or translates of subspaces.”

So we’re going to go deeper than the standard two-line definition. We’ll build the concept from first principles and then prove a whole bundle of structural facts that you will use constantly later.

We’ll proceed in layers:

1.  What “closed world” means at the level of operations and linear combinations
2.  The subspace definition and three equivalent tests (9 axioms → 2 axioms → 1 line)
3.  The “smallest subspace containing a set” viewpoint (intersection construction)
4.  Core closure properties: intersection, sum, span, orthogonal complement
5.  Subspaces vs affine subspaces (Ax=0 vs Ax=b) with a rigorous decomposition theorem
6.  How to _compute_ and _recognize_ subspaces in  $\mathbb R^n$ : equations, parametrizations, row reduction (conceptual, not full algorithm yet)
7.  Common traps and sharp non-examples (and exactly which axiom fails)

No handwaving; every statement will be justified.

* * *

### 3.2.0 The primitive question: “When does a subset inherit linear structure?”

Let  $V$  be a vector space over a field  $\mathbb F$  with operations  $+$  and scalar multiplication.

A subset  $W \subseteq V$  is “just a subset” until we ask:

> If I take vectors in  $W$  and do the **allowed linear operations** (add, scale, build linear combinations), do I stay inside  $W$ ?

Because the entire meaning of “linear” is: “closed under linear combinations.”

So the true essence of “subspace” is:

> **A subspace is a set that is closed under the formation of linear combinations.**

But we must phrase this carefully and minimally, because “closed under all linear combinations” is a big statement; we want an efficient check.

* * *

3.2.1 Three equivalent definitions/tests (and why they are equivalent)
----------------------------------------------------------------------

### Definition A (full, conceptual)

 $W\subseteq V$  is a **subspace** if  $W$  is a vector space with the operations inherited from  $V$ .

This is correct but impractical: it sounds like you must verify all vector space axioms inside  $W$ . We don’t want that.

So we compress.

* * *

### Theorem 1 (Subspace Test: 2-condition form)

A subset  $W\subseteq V$  is a subspace **iff**:

1.   $W\neq\emptyset$  (nonempty), and
2.  **closure under addition**:
    $$
    u,v\in W \Rightarrow u+v\in W,
    $$
3.  **closure under scalar multiplication**:
    $$
    u\in W,\ \alpha\in\mathbb F \Rightarrow \alpha u\in W.
    $$

#### Proof (⇒)

If  $W$  is a vector space under inherited operations, these closures are axioms. Nonempty holds because every vector space has at least the zero vector.

#### Proof (⇐) (this is the important direction)

Assume nonempty + the two closures. We must show  $W$  satisfies **all** vector space axioms.

*   **Zero exists in  $W$ :** pick some  $w_0\in W$ . By scalar closure,  $0\cdot w_0 \in W$ . But in any vector space,  $0\cdot w_0 = 0$  (proved in 3.1). So  $0\in W$ .
*   **Additive inverses exist:** let  $u\in W$ . By scalar closure,  $(-1)u\in W$ . But  $(-1)u=-u$ . So  $-u\in W$ .
*   **Associativity/commutativity/distributive laws:** these are identities that hold for all vectors in  $V$ . Since  $W\subseteq V$  uses the same operations, the identities automatically hold when you restrict to  $W$ .

Thus  $W$  is a vector space, i.e., a subspace. ∎

So the whole 9-axiom burden collapses into: nonempty + two closures.

* * *

### Theorem 2 (One-line subspace test: linear-combination closure)

A subset  $W\subseteq V$  is a subspace **iff**:

*    $W\neq\emptyset$ , and
*   for all  $u,v\in W$  and all  $\alpha,\beta\in\mathbb F$ ,
    $$
    \alpha u + \beta v \in W.
    $$

#### Why this is equivalent

*   Take  $\alpha=\beta=1$ : then  $u+v\in W$  (addition closure).
*   Take  $\beta=0$ : then  $\alpha u\in W$  (scalar closure).
*   Conversely, if you have addition closure and scalar closure, then  $\alpha u\in W$  and  $\beta v\in W$ , and adding them stays in  $W$ .

So this “one-line” form is exactly the statement:

> “ $W$  is closed under linear combinations of two vectors.”

And by induction, that implies closure under any finite linear combination.

* * *

### Practical corollary (fastest falsification rule)

If  $W$  is a subspace, then **necessarily**:

$$
0\in W.
$$

So if  $0\notin W$ , you can stop immediately: **not a subspace**.

This is why sets like  $Ax=b$  with  $b\neq 0$ , spheres  $\|x\|=1$ , and  $\mathbb R^n_{>0}$  fail instantly.

* * *

3.2.2 Closure under _all_ finite linear combinations (proved)
-------------------------------------------------------------

This is the real “span logic” you’ll reuse constantly.

### Proposition 1

If  $W$  is a subspace and  $w_1,\dots,w_k \in W$  with  $\alpha_1,\dots,\alpha_k\in\mathbb F$ , then

$$
\sum_{i=1}^k \alpha_i w_i \in W.
$$

#### Proof (induction on  $k$ )

*   Base  $k=1$ :  $\alpha_1 w_1\in W$  by scalar closure.
*   Step: assume true for  $k$ . For  $k+1$ ,
    $$
    \sum_{i=1}^{k+1}\alpha_i w_i = \left(\sum_{i=1}^k \alpha_i w_i\right) + \alpha_{k+1} w_{k+1}.
    $$
    The first term is in  $W$  by induction hypothesis; the second is in  $W$  by scalar closure; the sum is in  $W$  by addition closure.

Thus closure under all finite linear combinations holds. ∎

This proves, in a fully rigorous way, the slogan:

> **Subspace = closed under linear combinations.**

* * *

3.2.3 The “smallest subspace containing a set” viewpoint (intersection construction)
------------------------------------------------------------------------------------

This is one of the deepest structural viewpoints, and it explains why span is the “right” object.

Let  $S\subseteq V$  be any set (not necessarily finite).

Define:

$$
\mathcal C := \{W \subseteq V : W \text{ is a subspace and } S\subseteq W\}.
$$

So  $\mathcal C$  is the collection of all subspaces that contain  $S$ .

### Proposition 2 (intersection of subspaces is a subspace)

If  $\{W_i\}_{i\in I}$  is any family of subspaces of  $V$ , then

$$
\bigcap_{i\in I} W_i
$$

is a subspace.

#### Proof

*   Nonempty:  $0\in W_i$  for every  $i$ , hence  $0\in\cap_i W_i$ .
*   If  $u,v$  are in the intersection, then they’re in each  $W_i$ . Since each  $W_i$  is a subspace,  $u+v\in W_i$  for all  $i$ , so  $u+v$  lies in the intersection.
*   Same for scalar multiplication.

So intersection is a subspace. ∎

Now define:

$$
\boxed{\mathrm{span}(S) := \bigcap_{W\in\mathcal C} W.}
$$

This definition says:

>  $\mathrm{span}(S)$  is the set of vectors that you cannot avoid including if you want a subspace that contains  $S$ .

It is “the smallest closed world containing  $S$ .”

If  $S=\{v_1,\dots,v_k\}$  is finite, you can prove this equals the “linear combination” definition from 1.3:

$$
\mathrm{span}(S)=\left\{\sum_{i=1}^k \alpha_i v_i\right\}.
$$

So span is not a trick; it is the canonical minimal closure object created by intersection.

* * *

3.2.4 Subspace algebra: intersection, sum, direct sum (structural operations)
-----------------------------------------------------------------------------

Subspaces can be combined into new subspaces in specific ways. These operations are everywhere.

### A) Intersection  $U\cap W$ 

Always a subspace (proved above).  
Interpretation: vectors satisfying both sets of linear constraints.

* * *

### B) Sum of subspaces  $U+W$ 

Define:

$$
U+W := \{u+w : u\in U,\ w\in W\}.
$$

This is the set of all sums of one vector from each subspace.

#### Proposition 3

 $U+W$  is a subspace of  $V$ .

**Proof**

*   Nonempty:  $0=0+0\in U+W$ .
*   Closure under addition:  
    take  $u_1+w_1$  and  $u_2+w_2$ .
    $$
    (u_1+w_1)+(u_2+w_2)=(u_1+u_2)+(w_1+w_2)\in U+W
    $$
    because  $U,W$  are subspaces.
*   Closure under scalar multiplication:
    $$
    \alpha(u+w)=(\alpha u)+(\alpha w)\in U+W.
    $$

∎

Interpretation:

*    $U+W$  is the “smallest subspace containing both  $U$  and  $W$ .”

In fact:

$$
U+W = \mathrm{span}(U\cup W).
$$

* * *

### C) Direct sum (when the decomposition is unique)

If  $U\cap W = \{0\}$ , then every element of  $U+W$  has a **unique** representation  $u+w$ . In that case we write:

$$
U\oplus W.
$$

This is the subspace-level analog of “independence”: the only shared vector is zero, so you don’t have redundancy.

We will later formalize dimension additivity:

$$
\dim(U\oplus W)=\dim(U)+\dim(W),
$$

but that’s for the dimension chapter.

* * *

3.2.5 Subspaces vs affine subspaces: the real reason  $Ax=0$  is special
------------------------------------------------------------------------

This is a major point many learners half-understand.

### Key fact

A subspace must contain  $0$ . Therefore any solution set that does not contain  $0$  cannot be a subspace.

Consider linear equations in  $\mathbb R^n$ .

### Homogeneous system

$$
Ax=0
$$

Solution set:

$$
\mathcal N(A) := \{x: Ax=0\}
$$

is a subspace.

Proof:  $x\mapsto Ax$  is linear, and the kernel of a linear map is a subspace (we’ll show kernels properly below too).

### Non-homogeneous system

$$
Ax=b,\quad b\neq 0.
$$

Solution set:

$$
\mathcal S := \{x: Ax=b\}
$$

is typically **not** a subspace because  $0\notin \mathcal S$  (since  $A0=0\neq b$ ).

But  $\mathcal S$  is an **affine translate** of the nullspace.

#### Theorem (affine decomposition)

If  $\mathcal S$  is nonempty and  $x_p$  is one particular solution ( $Ax_p=b$ ), then:

$$
\boxed{ \mathcal S = x_p + \mathcal N(A) = \{x_p + z : z\in\mathcal N(A)\}. }
$$

**Proof**

*   If  $z\in\mathcal N(A)$ , then:
    $$
    A(x_p+z)=Ax_p+Az=b+0=b
    $$
    so  $x_p+z\in\mathcal S$ .
*   If  $x\in\mathcal S$ , then  $Ax=b$  and  $Ax_p=b$ . Subtract:
    $$
    A(x-x_p)=0
    $$
    so  $x-x_p \in \mathcal N(A)$ , hence  $x=x_p+z$ .

Thus equality holds. ∎

Interpretation:

*   The “direction structure” is the subspace  $\mathcal N(A)$ .
*   The “location” is given by the particular solution  $x_p$ .

This is exactly the point-vs-vector distinction from 1.2 showing up again.

* * *

3.2.6 Kernels and images are subspaces (fundamental theoremlets)
----------------------------------------------------------------

These are the subspaces you meet constantly.

Let  $T:V\to W$  be a **linear map**.

### Kernel (null space)

$$
\ker(T) := \{v\in V : T(v)=0\}.
$$

#### Proposition 4

 $\ker(T)$  is a subspace of  $V$ .

**Proof**

*    $T(0)=0$  by linearity, so  $0\in\ker(T)$ .
*   If  $u,v\in\ker(T)$ , then  $T(u)=T(v)=0$ , so:
    $$
    T(u+v)=T(u)+T(v)=0.
    $$
*   If  $u\in\ker(T)$ , then:
    $$
    T(\alpha u)=\alpha T(u)=0.
    $$

Thus subspace. ∎

### Image (range)

$$
\mathrm{Im}(T):=\{T(v):v\in V\}\subseteq W.
$$

#### Proposition 5

 $\mathrm{Im}(T)$  is a subspace of  $W$ .

**Proof**

*    $0=T(0)\in \mathrm{Im}(T)$ .
*   If  $a=T(u)$  and  $b=T(v)$ , then:
    $$
    a+b=T(u)+T(v)=T(u+v)\in \mathrm{Im}(T).
    $$
*   For scalar  $\alpha$ :
    $$
    \alpha a=\alpha T(u)=T(\alpha u)\in \mathrm{Im}(T).
    $$

∎

These two subspaces are the domain-side and codomain-side “shadows” of a linear map. Later, rank–nullity is the dimension relationship between them.

* * *

3.2.7 How to recognize subspaces in  $\mathbb R^n$ : two equivalent representations
-----------------------------------------------------------------------------------

In  $\mathbb R^n$ , subspaces tend to appear in two forms:

### Form 1: as solution sets of homogeneous linear equations

$$
W = \{x\in\mathbb R^n : Ax=0\}.
$$

This is the kernel of  $x\mapsto Ax$ , hence a subspace.

### Form 2: as spans of vectors (parametric form)

$$
W = \mathrm{span}\{v_1,\dots,v_k\} = \left\{\sum_{i=1}^k \alpha_i v_i\right\}.
$$

This is clearly a subspace (closed under linear combinations).

A huge part of computational linear algebra is converting between these two forms (via row reduction), because:

*   equations describe constraints,
*   spans describe degrees of freedom.

You’ll later learn:

*   columns of a matrix span its column space,
*   nullspace has a spanning set computed from free variables,
*   row space is span of rows.

* * *

3.2.8 Non-examples and “which axiom fails” (sharpening to a blade)
------------------------------------------------------------------

A good way to master 3.2 is to diagnose failures precisely.

### Non-example A: line not through origin

$$
L = \{(t,1): t\in\mathbb R\}\subseteq\mathbb R^2.
$$
*    $0\notin L$ . So not a subspace.
*   Also not closed under scalar multiplication:  $2(t,1)=(2t,2)\notin L$ .

But it is an affine subspace:  $(0,1)+\mathrm{span}\{(1,0)\}$ .

### Non-example B: unit circle

$$
C=\{x:\|x\|=1\}.
$$
*    $0\notin C$ .
*   Not closed under scaling:  $2x$  has norm 2.

### Non-example C:  $\mathbb R^n_{\ge 0}$ 

*   Contains 0, closed under addition, but not under scalar multiplication by negative numbers, so fails scalar closure.

### Non-example D: “degree exactly  $d$ ” polynomials

*   Excludes the zero polynomial, so fails  $0\in W$ .
*   Addition can change degree, so also fails closure.

These examples teach you to check subspace property like a machine: zero first, then closures.

* * *

3.2.9 The real mental model to keep forever
-------------------------------------------

Here is the “closed world” idea in its most precise form:

> A subspace is exactly a set of vectors that is stable under the operations that define linearity.  
> It is the natural habitat of “solutions,” “constraints,” and “allowable directions.”

Everything else you’ll do in linear algebra is:

*   describing a subspace,
*   comparing two subspaces,
*   mapping one subspace into another,
*   decomposing the space into subspaces.

* * *

3.2.10 Mastery checklist (strong version)
-----------------------------------------

You own 3.2 at a high level if you can do all of the following on sight:

1.  Given a subset  $W\subseteq V$ , decide subspace or not, and cite the exact failure (zero missing, not closed under addition, not closed under scalar multiplication).
2.  Prove kernel and image are subspaces from linearity alone.
3.  Prove intersection of any family of subspaces is a subspace.
4.  Define  $U+W$ , prove it is a subspace, and interpret it as the smallest subspace containing both.
5.  Given  $Ax=b$  with a known solution  $x_p$ , prove solution set is  $x_p+\mathcal N(A)$ .
6.  Convert between “equation form” and “span form” conceptually (even before doing computations).

* * *

If you want to continue in the roadmap order, the next node is **3.3 Span and generating sets**, where we study subspaces through the lens of “what generates them” and begin the path to basis and dimension.

## Response:
3.3 Span and generating sets — “everything you can build by linear combinations” (ultra-deep)
---------------------------------------------------------------------------------------------

In 3.1 you got the axioms (what “linear” is).  
In 3.2 you got subspaces (closed worlds under linear combinations).

Now 3.3 is the keystone that connects them:

> A **subspace** is exactly the set of vectors you can produce from some generators using **finite linear combinations**.

So 3.3 is where we formalize “generation,” “span,” “redundancy,” and the algorithmic problem:

*   Is a vector in the span?
*   Can we remove some generators without changing the span?
*   How do we certify minimality?

This section is also where you learn the _correct_ mental model:

> “A subspace is not a mysterious object. It is a closure under linear combinations.”

We’ll proceed in a precise logical order:

1.  Definitions: linear combination, span of a set, generating set
2.  Span is a subspace (proved)
3.  Span is the **smallest** subspace containing the set (proved via intersection)
4.  Membership in a span as a solvability question (“coordinates in generators”)
5.  Redundancy, dependence, and minimal generating sets
6.  Span of unions, span of spans, monotonicity laws
7.  Concrete computations in  $\mathbb R^n$ : matrix viewpoint
8.  “Finite span” vs “infinite generating sets” (finite linear combos only!)
9.  Bridges to basis/dimension (preview, but clean)

* * *

### 3.3.0 Setup and notation (no ambiguity)

Let  $V$  be a vector space over a field  $\mathbb F$ .  
Let  $S \subseteq V$  be any subset (possibly finite, possibly infinite).

Important: “subset” means we’re not assuming  $S$  is a subspace. It’s just a collection of vectors.

* * *

3.3.1 Linear combinations (abstract definition, not just  $\mathbb R^n$ )
-------------------------------------------------------------------------

### Definition (finite linear combination)

Given vectors  $v_1,\dots,v_k \in V$  and scalars  $\alpha_1,\dots,\alpha_k \in \mathbb F$ , the vector

$$
\sum_{i=1}^k \alpha_i v_i
$$

is called a **linear combination** of  $v_1,\dots,v_k$ .

Key word: **finite**.  
A linear combination always uses **finitely many** vectors and **finitely many** scalars.

Why “finite” matters: vector space axioms guarantee closure under _finite_ addition, not infinite sums. Infinite sums require topology/analysis (convergence), which is extra structure. In pure linear algebra, we do **not** assume it.

* * *

3.3.2 Span of a set (the closure operator)
------------------------------------------

### Definition (span)

The **span** of  $S$ , denoted  $\mathrm{span}(S)$ , is the set of all finite linear combinations of elements of  $S$ .

Formally:

$$
\boxed{ \mathrm{span}(S) := \left\{\sum_{i=1}^k \alpha_i s_i \;\middle|\; k\in\mathbb N,\ s_i\in S,\ \alpha_i\in\mathbb F\right\}. }
$$

This definition works whether  $S$  is finite or infinite.

If  $S=\{v_1,\dots,v_k\}$  is finite, we often write:

$$
\mathrm{span}(v_1,\dots,v_k) = \left\{\sum_{i=1}^k \alpha_i v_i : \alpha_i\in\mathbb F\right\}.
$$

* * *

3.3.3 Generating set (what it means to “generate a space”)
----------------------------------------------------------

### Definition (generating set)

A subset  $S \subseteq V$  is called a **generating set** (or **spanning set**) for a subspace  $W\subseteq V$  if

$$
W = \mathrm{span}(S).
$$

In particular,  $S$  generates all of  $V$  if  $V=\mathrm{span}(S)$ .

Interpretation:

*    $S$  is a set of “building blocks.”
*   You’re allowed to scale and add finitely many of them.
*   Everything in  $W$  must be buildable that way.

* * *

3.3.4 Fundamental theorem 1: span is a subspace (proved from axioms)
--------------------------------------------------------------------

### Theorem

For any  $S\subseteq V$ ,  $\mathrm{span}(S)$  is a subspace of  $V$ .

### Proof (subspace test, explicitly)

We must show:

*   nonempty (or show  $0\in\mathrm{span}(S)$ ),
*   closure under addition,
*   closure under scalar multiplication.

**Step 1:  $0 \in \mathrm{span}(S)$ .**  
Take  $k=1$ , choose any  $s_1\in S$  if  $S\neq \varnothing$ , and set  $\alpha_1=0$ : then  $\alpha_1 s_1 = 0$ .  
If  $S=\varnothing$ , we handle separately below.  
More robust: allow  $k=0$  and define the empty sum as  $0$ . Many texts do this. Either way,  $0\in\mathrm{span}(S)$  whenever  $S$  is nonempty, and if  $S=\varnothing$ , the span is  $\{0\}$  (by convention of empty linear combination).

So  $\mathrm{span}(S)$  is nonempty and contains  $0$ .

**Step 2: closure under addition.**  
Let  $x,y \in \mathrm{span}(S)$ . Then by definition there exist:

$$
x=\sum_{i=1}^k \alpha_i s_i,\qquad y=\sum_{j=1}^m \beta_j t_j
$$

with  $s_i,t_j\in S$ .

Then

$$
x+y = \sum_{i=1}^k \alpha_i s_i + \sum_{j=1}^m \beta_j t_j
$$

is still a finite linear combination of elements of  $S$  (just concatenate the lists).  
Hence  $x+y\in\mathrm{span}(S)$ .

**Step 3: closure under scalar multiplication.**  
Let  $x\in\mathrm{span}(S)$ , so  $x=\sum_{i=1}^k \alpha_i s_i$ . For any  $\gamma\in\mathbb F$ ,

$$
\gamma x = \gamma\sum_{i=1}^k \alpha_i s_i = \sum_{i=1}^k (\gamma\alpha_i) s_i,
$$

again a finite linear combination from  $S$ .  
Hence  $\gamma x \in \mathrm{span}(S)$ .

By the subspace test,  $\mathrm{span}(S)$  is a subspace. ∎

* * *

3.3.5 Fundamental theorem 2: span is the _smallest_ subspace containing  $S$ 
-----------------------------------------------------------------------------

There are two equivalent ways to formalize “smallest”: containment order and intersection.

### Theorem (minimality)

 $\mathrm{span}(S)$  is the smallest subspace of  $V$  that contains  $S$ . Concretely:

1.   $S \subseteq \mathrm{span}(S)$ 
2.  If  $W$  is a subspace with  $S\subseteq W$ , then  $\mathrm{span}(S)\subseteq W$ .

### Proof

**(1)  $S \subseteq \mathrm{span}(S)$ .**  
Take any  $s\in S$ . Then  $s = 1\cdot s$ , a linear combination. Hence  $s\in\mathrm{span}(S)$ .

**(2) Minimality.**  
Let  $W$  be a subspace with  $S\subseteq W$ .  
Take any  $x\in\mathrm{span}(S)$ . Then  $x=\sum_{i=1}^k \alpha_i s_i$  with  $s_i\in S\subseteq W$ .  
Since  $W$  is a subspace, it is closed under scalar multiplication and addition, so  $\sum_{i=1}^k \alpha_i s_i \in W$ .  
Therefore  $x\in W$ . So  $\mathrm{span}(S)\subseteq W$ . ∎

### Equivalent “intersection” characterization (very important)

Let  $\mathcal{F}$  be the family of all subspaces of  $V$  that contain  $S$ :

$$
\mathcal{F} := \{W \le V : S\subseteq W\}.
$$

Then

$$
\boxed{ \mathrm{span}(S) = \bigcap_{W\in\mathcal F} W. }
$$

Why this is true:

*   the intersection of all subspaces containing  $S$  is itself a subspace (3.2),
*   it contains  $S$ ,
*   it must be the smallest such subspace (intersection is contained in every member).

This viewpoint is powerful because it makes span a **closure operator** in the order-theoretic sense.

* * *

3.3.6 Span as a closure operator (three laws)
---------------------------------------------

Define  $ \mathrm{cl}(S):=\mathrm{span}(S)$ . Then:

1.  **Extensive**:  $S \subseteq \mathrm{span}(S)$ 
2.  **Monotone**: if  $S\subseteq T$  then  $\mathrm{span}(S)\subseteq \mathrm{span}(T)$ 
3.  **Idempotent**:  $\mathrm{span}(\mathrm{span}(S))=\mathrm{span}(S)$ 

### Proof sketches (but still rigorous)

*   Extensive: proved above.
*   Monotone: if  $S\subseteq T$ , any linear combo of elements of  $S$  is also a linear combo of elements of  $T$ , so inclusion holds.
*   Idempotent:  $\mathrm{span}(S)$  is a subspace containing  $S$ ; spanning it again adds nothing, because “span of a subspace is itself.”

This triad is the mathematical meaning of “span closes a set under linear combinations.”

* * *

3.3.7 Membership in a span is a solvability problem
---------------------------------------------------

### Question (core task)

Given  $x\in V$  and a set  $S\subseteq V$ , decide whether:

$$
x \in \mathrm{span}(S).
$$

By definition:

$$
x \in \mathrm{span}(S) \iff \exists k,\ s_1,\dots,s_k\in S,\ \alpha_1,\dots,\alpha_k\in\mathbb F \text{ such that } x=\sum_{i=1}^k \alpha_i s_i.
$$

If  $S$  is finite, say  $S=\{v_1,\dots,v_k\}$ , then this becomes:

> Does the linear system in unknown coefficients  $\alpha_1,\dots,\alpha_k$ :

$$
\alpha_1 v_1 + \cdots + \alpha_k v_k = x
$$

have a solution?

This is the algebraic heart of “coordinates with respect to generators.”

Two crucial distinctions:

*   **Existence**: is  $x$  representable at all?
*   **Uniqueness**: if representable, is the representation unique?

Uniqueness happens exactly when the generators are linearly independent (next section), which leads to bases.

* * *

3.3.8 Redundancy: when a generator is unnecessary
-------------------------------------------------

Let  $S$  be a generating set for some subspace  $W=\mathrm{span}(S)$ .  
A vector  $v\in S$  is **redundant** if removing it does not change the span:

$$
\mathrm{span}(S\setminus\{v\}) = \mathrm{span}(S).
$$

### The redundancy criterion (precise)

**Proposition**  
Let  $S\subseteq V$  and  $v\in S$ . Then the following are equivalent:

1.   $v$  is redundant in  $S$ 
2.   $v \in \mathrm{span}(S\setminus\{v\})$ 

#### Proof

**(2 ⇒ 1)**  
Assume  $v \in \mathrm{span}(S\setminus\{v\})$ .  
Take any  $x\in \mathrm{span}(S)$ . Write:

$$
x = \alpha v + \sum_{s\in S\setminus\{v\}} \alpha_s s.
$$

But since  $v$  itself is a linear combo of  $S\setminus\{v\}$ , the term  $\alpha v$  can be rewritten as a linear combo of  $S\setminus\{v\}$ . Therefore  $x\in \mathrm{span}(S\setminus\{v\})$ .  
So  $\mathrm{span}(S)\subseteq \mathrm{span}(S\setminus\{v\})$ . The reverse inclusion is trivial, hence equality.

**(1 ⇒ 2)**  
Assume  $\mathrm{span}(S\setminus\{v\}) = \mathrm{span}(S)$ .  
Since  $v\in \mathrm{span}(S)$ , we have  $v\in \mathrm{span}(S\setminus\{v\})$ . ∎

This proposition is extremely operational:  
to see if you can delete  $v$ , check if it can be produced from the others.

* * *

3.3.9 Span and linear dependence (the exact bridge)
---------------------------------------------------

A set  $S=\{v_1,\dots,v_k\}$  is linearly **dependent** precisely when at least one  $v_j$  lies in the span of the others.

### Theorem

For a finite set  $\{v_1,\dots,v_k\}$ , the following are equivalent:

1.   $\{v_1,\dots,v_k\}$  is linearly dependent
2.  There exists  $j$  such that  $v_j \in \mathrm{span}(\{v_1,\dots,v_k\}\setminus\{v_j\})$ 

### Proof (tight)

*   Dependence means  $\sum_{i=1}^k \alpha_i v_i = 0$  with not all  $\alpha_i$  zero.
*   Pick  $j$  with  $\alpha_j\neq 0$ . Then
    $$
    v_j = -\sum_{i\neq j}\frac{\alpha_i}{\alpha_j}v_i,
    $$
    which shows  $v_j$  is in the span of the others.
*   Conversely, if some  $v_j$  is in the span of the others, bring all terms to one side to get a nontrivial linear relation.

∎

So “dependence” is exactly “redundancy” in generating.

* * *

3.3.10 Concrete computational form in  $\mathbb R^n$ : matrices as span encoders
--------------------------------------------------------------------------------

Let  $v_1,\dots,v_k \in \mathbb R^n$ . Form the matrix

$$
A := [v_1\ v_2\ \cdots\ v_k] \in \mathbb R^{n\times k}.
$$

Then:

$$
\mathrm{span}(v_1,\dots,v_k) = \{A\alpha : \alpha \in \mathbb R^k\}.
$$

Membership  $x\in \mathrm{span}(v_1,\dots,v_k)$  is exactly solvability of:

$$
A\alpha = x.
$$

This is the exact bridge to:

*   Gaussian elimination,
*   rank,
*   column space  $\mathrm{Col}(A)$ ,
*   null space  $\mathrm{Null}(A)$ .

And note the conceptual identity:

> **The column space of  $A$  is the span of its columns.**

So “span” is not a side definition; it is literally what matrix multiplication _means_.

* * *

3.3.11 Finite vs infinite generating sets (subtle but important)
----------------------------------------------------------------

If  $S$  is infinite (e.g., all polynomials, all functions), then:

$$
\mathrm{span}(S)
$$

still consists of **finite** linear combinations of elements of  $S$ .

Example: let  $S=\{1,x,x^2,x^3,\dots\}\subset \mathbb R[x]$ .  
Then  $\mathrm{span}(S)$  is all polynomials (each polynomial uses finitely many powers).

But if you tried to allow infinite sums like  $\sum_{k=0}^\infty a_k x^k$ , you would get **power series**, which is a different object requiring convergence notions.

So when you read “span,” you must automatically hear:

> span = finite linear combination closure, not infinite.

* * *

3.3.12 Key algebraic identities involving span
----------------------------------------------

These are frequently used and worth proving once cleanly.

### (A)  $\mathrm{span}(S\cup T) = \mathrm{span}(\mathrm{span}(S)\cup \mathrm{span}(T))$ 

Reason: adding already-closed sets doesn’t change what you can generate.  
More useful is the next identity:

### (B)  $\mathrm{span}(S\cup T) = \mathrm{span}(S) + \mathrm{span}(T)$ 

Here “+” denotes **sum of subspaces**:

$$
W_1 + W_2 := \{w_1+w_2 : w_1\in W_1,\ w_2\in W_2\}.
$$

**Proof**

*   Any element of  $\mathrm{span}(S\cup T)$  is a linear combination of elements from  $S$  and  $T$ , which can be grouped into a sum of an element from  $\mathrm{span}(S)$  and one from  $\mathrm{span}(T)$ .
*   Conversely, any  $w_1+w_2$  with  $w_1\in\mathrm{span}(S)$ ,  $w_2\in\mathrm{span}(T)$  is a linear combination of elements from  $S\cup T$ .

∎

This identity is the algebra behind “combine generating sets to generate sums.”

* * *

3.3.13 What span is _not_ (common pitfalls)
-------------------------------------------

1.  Span is not “all linear combos with coefficients summing to 1.”  
    That’s **affine hull**, not span.
2.  Span is not “all infinite series combos.”  
    That’s outside pure linear algebra.
3.  Span depends on the field.  
    Example: vectors might span a space over  $\mathbb R$  but not over  $\mathbb Q$ .  
    The allowed scalars matter.

* * *

3.3.14 Preview: why bases are “spanning + nonredundant”
-------------------------------------------------------

A **basis** (next layer) is exactly:

*   a spanning set (generates the space),
*   with no redundancy (independent).

So 3.3 gives the “spanning/generating” half of the basis concept.  
3.4 will add the “independence/minimality” half and prove uniqueness of coordinate representations.

* * *

3.3.15 Mastery checklist for 3.3
--------------------------------

You truly own 3.3 if you can do all of the following fluently:

*   Define  $\mathrm{span}(S)$  for finite and infinite  $S$ , emphasizing **finite** linear combos.
*   Prove  $\mathrm{span}(S)$  is a subspace using the subspace test.
*   Prove minimality: any subspace containing  $S$  contains  $\mathrm{span}(S)$ .
*   Use the redundancy criterion:  $v$  removable iff  $v$  is in the span of the others.
*   Translate span membership into solving  $A\alpha=x$  in  $\mathbb R^n$ .
*   Use identities: monotonicity, idempotence, and  $\mathrm{span}(S\cup T)=\mathrm{span}(S)+\mathrm{span}(T)$ .
*   Keep the field  $\mathbb F$  explicit and understand how it affects span.

* * *

If you want to continue in the roadmap order, the next conceptual step is **3.4** (linear independence, basis, dimension) where we formalize “no redundancy” and prove the big theorem: all bases of a space have the same size.

## Response:
3.4 Linear independence, basis, and dimension
---------------------------------------------

_(redundancy, coordinates, “degrees of freedom,” and why dimension is well-defined)_

Up to 3.3 you learned how to **generate** a subspace: take some vectors, allow finite linear combinations, and you get a subspace. That’s the “span” half of the story.

But span alone is sloppy: a spanning set can contain massive redundancy. You can generate the same subspace with infinitely many different sets, and many of them are bloated with vectors that add nothing new.

Section 3.4 answers the precise structural questions:

1.  What does it mean that a set of vectors has **no redundancy**?
2.  When do “coordinates” make sense (existence + uniqueness)?
3.  Why does “number of degrees of freedom” (dimension) not depend on which basis you pick?
4.  How do spanning sets and independent sets relate (exchange / replacement)?

This is where linear algebra becomes a _theory of minimal representations_.

We’ll proceed in a rigorous chain:

*   Independence (definition → redundancy theorem)
*   Basis (spanning + independent → unique coordinates)
*   Dimension (size of a basis → well-definedness theorem)
*   Core proof engine: the exchange lemma (Steinitz)
*   Algorithms as theorems: extend independent → basis; shrink spanning → basis
*   Subspace dimension rules (including a key inequality and the dimension formula preview)

Throughout:  $V$  is a vector space over a field  $\mathbb F$ .

* * *

3.4.1 Linear independence: the “no nontrivial linear relation” condition
------------------------------------------------------------------------

### Definition (linear dependence / independence)

A finite list of vectors  $(v_1,\dots,v_k)$  in  $V$  is **linearly dependent** if there exist scalars  $\alpha_1,\dots,\alpha_k \in \mathbb F$ , not all zero, such that

$$
\alpha_1 v_1 + \cdots + \alpha_k v_k = 0.
$$

It is **linearly independent** if the only way to get zero is the trivial combination:

$$
\alpha_1 v_1 + \cdots + \alpha_k v_k = 0 \;\Rightarrow\; \alpha_1=\cdots=\alpha_k=0.
$$

This definition is **purely algebraic**. It makes no reference to coordinates, geometry, or matrices.

### Why this definition captures “redundancy”

A dependence relation says: one vector can be expressed using the others. That is the precise meaning of redundancy.

We prove that equivalence cleanly next.

* * *

3.4.2 Independence ⇔ no vector lies in the span of the others
-------------------------------------------------------------

This is the key equivalence that turns independence into an operational tool.

### Theorem (dependence ↔ redundancy)

For vectors  $v_1,\dots,v_k$ , the following are equivalent:

1.   $\{v_1,\dots,v_k\}$  is linearly dependent.
2.  There exists an index  $j$  such that
    
$$
v_j \in \mathrm{span}\{v_1,\dots,v_{j-1},v_{j+1},\dots,v_k\}.
$$

#### Proof

**(1 ⇒ 2).**  
Assume dependence. Then there exist  $\alpha_1,\dots,\alpha_k$ , not all zero, with

$$
\sum_{i=1}^k \alpha_i v_i = 0.
$$

Pick an index  $j$  with  $\alpha_j \neq 0$ . (We can because not all  $\alpha_i$  are zero.)  
Rearrange:

$$
\alpha_j v_j = -\sum_{i\neq j} \alpha_i v_i.
$$

Multiply by  $\alpha_j^{-1}$  (allowed because  $\alpha_j\neq 0$  and we are over a field):

$$
v_j = -\sum_{i\neq j} \frac{\alpha_i}{\alpha_j} v_i.
$$

That is exactly a linear combination of the other vectors, so  $v_j$  lies in their span.

**(2 ⇒ 1).**  
Assume  $v_j = \sum_{i\neq j} \beta_i v_i$ . Move everything to one side:

$$
v_j - \sum_{i\neq j} \beta_i v_i = 0.
$$

This is a nontrivial dependence relation (coefficient of  $v_j$  is 1), hence the set is dependent.

∎

**Interpretation:**

*   Independent set: every vector contributes a genuinely new direction not buildable from the others.
*   Dependent set: at least one vector is redundant.

This is the conceptual bridge between 3.3 and 3.4.

* * *

3.4.3 Basis: spanning + independence (existence of coordinates and no redundancy)
---------------------------------------------------------------------------------

### Definition (basis)

A set  $B=\{b_1,\dots,b_n\}\subseteq V$  is a **basis** of  $V$  if:

1.  (Spanning)  $\mathrm{span}(B)=V$ .
2.  (Independent)  $B$  is linearly independent.

A basis is a spanning set with _no redundancy_.

### Why both conditions are necessary

*   Spanning alone: you can represent every vector, but not uniquely (too many generators).
*   Independence alone: no redundancy, but you might not represent everything (too few vectors).

A basis is exactly the sweet spot where representation is possible and unique.

We now prove that “basis” is equivalent to “unique coordinates.”

* * *

3.4.4 The coordinate theorem: existence + uniqueness of representation
----------------------------------------------------------------------

### Theorem (unique representation in a basis)

Let  $B=\{b_1,\dots,b_n\}$  be a basis of  $V$ . Then every  $v\in V$  can be written **uniquely** as

$$
v = c_1 b_1 + \cdots + c_n b_n,
$$

for some scalars  $c_1,\dots,c_n\in\mathbb F$ .

#### Proof

**Existence.**  
Since  $B$  spans  $V$ , by definition of span, for each  $v\in V$  there exist scalars  $c_i$  such that  $v=\sum c_i b_i$ .

**Uniqueness.**  
Suppose

$$
v = \sum_{i=1}^n c_i b_i = \sum_{i=1}^n d_i b_i.
$$

Subtract:

$$
0 = \sum_{i=1}^n (c_i-d_i)b_i.
$$

Because  $B$  is linearly independent, the only linear combination of  $b_i$  that equals 0 is the trivial one. Therefore  $c_i-d_i=0$  for all  $i$ , i.e.  $c_i=d_i$  for all  $i$ . Uniqueness proved.

∎

**Meaning:**  
A basis is precisely what makes “coordinates” well-defined. Without independence, the coordinates are not unique; without spanning, some vectors have no coordinates at all.

* * *

3.4.5 Dimension: “how many basis vectors” and why it’s well-defined
-------------------------------------------------------------------

### Definition (dimension)

If  $V$  has a finite basis with  $n$  vectors, we say  $V$  is **finite-dimensional** and define

$$
\dim(V) := n.
$$

But we must confront the big logical problem:

> How do we know a different basis won’t have a different number of vectors?

This is the well-definedness of dimension. The proof is not trivial; it requires the exchange lemma (Steinitz).

* * *

3.4.6 The exchange lemma (Steinitz replacement) — the core proof engine
-----------------------------------------------------------------------

This lemma is the hidden motor behind:

*   “all bases have the same size,”
*   “independent sets can’t be bigger than spanning sets,”
*   “you can replace vectors in a spanning set by independent ones.”

### Lemma (Steinitz exchange lemma)

Let  $V$  be a vector space. Suppose:

*    $S = \{s_1,\dots,s_m\}$  spans  $V$ .
*    $L = \{\ell_1,\dots,\ell_k\}$  is linearly independent in  $V$ .

Then:

1.   $k \le m$ .
2.  You can replace  $k$  vectors in  $S$  with  $\ell_1,\dots,\ell_k$  and the resulting set still spans  $V$ .

We prove it in a very explicit step-by-step replacement style.

#### Proof

We build a sequence of spanning sets  $S^{(0)}, S^{(1)},\dots,S^{(k)}$  where:

*    $S^{(0)} = \{s_1,\dots,s_m\}$  spans  $V$ ,
*    $S^{(j)}$  spans  $V$  and contains  $\ell_1,\dots,\ell_j$ ,
*    $|S^{(j)}|=m$  always (we replace, not add).

**Step 0:**  $S^{(0)}$  spans  $V$  by assumption.

**Inductive step:** assume  $S^{(j-1)}$  spans  $V$  and contains  $\ell_1,\dots,\ell_{j-1}$ . We want to incorporate  $\ell_j$ .

Because  $S^{(j-1)}$  spans  $V$ , we can express  $\ell_j$  as a linear combination of elements of  $S^{(j-1)}$ :

$$
\ell_j = \sum_{u \in S^{(j-1)}} a_u\, u.
$$

Move to one side:

$$
0 = \ell_j - \sum_{u \in S^{(j-1)}} a_u\, u.
$$

Now, crucial point: among the vectors in  $S^{(j-1)}$ , some are already the  $\ell_1,\dots,\ell_{j-1}$ . We claim: **at least one coefficient on a vector not among  $\{\ell_1,\dots,\ell_{j-1}\}$  must be nonzero**.

Why? Suppose for contradiction that every coefficient on “non- $\ell$ ” vectors is zero, meaning  $\ell_j$  is in the span of  $\ell_1,\dots,\ell_{j-1}$ . That would make  $\{\ell_1,\dots,\ell_j\}$  linearly dependent, contradicting that  $L$  is independent. Therefore, there exists some vector  $u^\*\in S^{(j-1)}\setminus\{\ell_1,\dots,\ell_{j-1}\}$  with coefficient  $a_{u^\*}\neq 0$ .

Solve the representation for  $u^\*$ :

$$
a_{u^\*}u^\* = \ell_j - \sum_{u\in S^{(j-1)}\setminus\{u^\*\}} a_u\,u
$$
 
$$
u^\* = a_{u^\*}^{-1}\ell_j - \sum_{u\in S^{(j-1)}\setminus\{u^\*\}} \frac{a_u}{a_{u^\*}}\,u.
$$

So  $u^\*$  lies in the span of  $\ell_j$  plus the other vectors in  $S^{(j-1)}\setminus\{u^\*\}$ .

Now define:

$$
S^{(j)} := (S^{(j-1)}\setminus\{u^\*\})\cup\{\ell_j\}.
$$

We claim  $S^{(j)}$  still spans  $V$ .  
Reason:  $S^{(j-1)}$  spans  $V$ . The only vector removed is  $u^\*$ , but we just showed  $u^\*$  is in the span of  $S^{(j)}$ . Therefore everything that could be built from  $S^{(j-1)}$  can still be built from  $S^{(j)}$ . So  $S^{(j)}$  spans  $V$ .

This completes the induction.

After  $k$  steps,  $S^{(k)}$  spans  $V$  and contains all  $\ell_1,\dots,\ell_k$ , and its size is still  $m$ . Therefore we must have  $k\le m$  (you can’t fit  $k$  distinct  $\ell$ ’s into a set of size  $m$  unless  $k\le m$ ). That gives (1), and the construction gives (2).

∎

This lemma is the reason dimension is a theorem, not a definition-by-fiat.

* * *

3.4.7 All bases have the same size (dimension is well-defined)
--------------------------------------------------------------

### Theorem (basis cardinality invariance)

If  $B$  and  $C$  are two bases of a finite-dimensional vector space  $V$ , then  $|B|=|C|$ .

#### Proof

Let  $|B|=n$ ,  $|C|=m$ .

*   Since  $B$  is a basis, it spans  $V$ . Since  $C$  is a basis, it is linearly independent.  
    Apply Steinitz with spanning set  $B$  and independent set  $C$ : we get  $m\le n$ .
*   Swap roles:  $C$  spans  $V$ ,  $B$  is linearly independent. Apply Steinitz again:  $n\le m$ .

Thus  $n=m$ . ∎

So  $\dim(V)$  is well-defined.

* * *

3.4.8 Two fundamental “algorithm theorems”
------------------------------------------

These are the practical moves you will do constantly.

### Theorem A (extend an independent set to a basis)

Let  $V$  be finite-dimensional and let  $L\subseteq V$  be linearly independent. Then there exists a basis  $B$  of  $V$  with  $L\subseteq B$ .

#### Proof idea (rigorous, constructive)

If  $L$  already spans  $V$ , it is a basis and we’re done.

If not, there exists  $v_1\in V\setminus \mathrm{span}(L)$ . Then  $L\cup\{v_1\}$  is still independent (prove: if  $v_1$  were dependent on  $L$ , it would be in the span).

If the enlarged set still doesn’t span, pick  $v_2\notin \mathrm{span}(L\cup\{v_1\})$ , and continue.

This process must stop after finitely many steps because  $V$  is finite-dimensional: an independent set cannot have more vectors than a spanning set (Steinitz), so you cannot keep adding forever.

When it stops, the set spans  $V$  and remains independent → basis.

∎

Key takeaway: **independence can always be completed to a coordinate system**.

* * *

### Theorem B (reduce a spanning set to a basis)

Let  $S\subseteq V$  be a finite spanning set. Then there exists a subset  $B\subseteq S$  that is a basis of  $V$ .

#### Proof (redundancy elimination)

If  $S$  is independent, it is already a basis.

If it is dependent, then by the redundancy theorem (3.4.2), some vector  $s\in S$  lies in the span of the others. Remove it; span does not change.

Repeat: each removal decreases the number of vectors. This process must stop after finitely many steps. When it stops, no vector is redundant → the set is independent. It still spans (since we only removed redundant vectors). Thus it is a basis.

∎

Key takeaway: **any spanning set contains a basis**.

* * *

3.4.9 Dimension as “max size of independent set” = “min size of spanning set”
-----------------------------------------------------------------------------

This is a beautiful equivalence that becomes extremely useful.

### Theorem (dimension characterizations)

Let  $V$  be finite-dimensional. For an integer  $n$ , the following are equivalent:

1.   $\dim(V)=n$ .
2.  Every basis has exactly  $n$  vectors.
3.  The largest possible size of a linearly independent set is  $n$ .
4.  The smallest possible size of a spanning set is  $n$ .

#### Proof sketch (but logically tight)

*   If  $B$  is a basis of size  $n$ , then any independent set has size  $\le n$  (Steinitz with spanning set  $B$ ).
*   Any spanning set has size  $\ge n$  (Steinitz with independent set  $B$ ).
*   The basis itself shows the bounds are achievable, hence “max independent = n” and “min spanning = n.”

∎

This is why dimension really is “degrees of freedom.”

* * *

3.4.10 Subspace dimension facts (essential toolkit)
---------------------------------------------------

Let  $W$  be a subspace of a finite-dimensional space  $V$ .

### Fact 1:  $\dim(W) \le \dim(V)$ 

Because any basis of  $W$  is an independent set in  $V$ , and independent sets can’t be larger than a basis of  $V$ .

### Fact 2: If  $W \neq V$ , then  $\dim(W) < \dim(V)$ 

Because if  $W\neq V$ , a basis of  $W$  cannot span  $V$ . Extending that basis to a basis of  $V$  adds at least one vector.

### Fact 3 (preview of a major theorem): dimension of a sum

For subspaces  $U,W\subseteq V$ ,

$$
\dim(U+W) = \dim(U) + \dim(W) - \dim(U\cap W).
$$

We won’t fully prove this until you have more machinery, but keep it mentally filed: intersections measure “overlap / redundancy” between subspaces.

* * *

3.4.11 Concrete viewpoint in  $\mathbb R^n$  (coordinates are a theorem, not a default)
---------------------------------------------------------------------------------------

In  $\mathbb R^n$ , the standard basis  $e_1,\dots,e_n$  is a basis, hence:

*   every vector  $x\in\mathbb R^n$  has unique coordinates  $(x_1,\dots,x_n)$ ,
*    $\dim(\mathbb R^n)=n$ .

But the point of 3.4 is: this coordinate miracle is not special to tuples. It happens in any finite-dimensional vector space once you pick a basis.

So “coordinates” are not the definition of vectors; they are a **representation theorem**.

* * *

3.4.12 Common traps (that reveal what you truly understand)
-----------------------------------------------------------

1.  **Confusing “spans” with “independent.”**  
    A set can span and still be dependent (redundant generators).  
    A set can be independent and still not span (too small).
2.  **Assuming coordinates exist without a basis.**  
    Coordinates are only defined relative to a chosen basis.
3.  **Forgetting the field matters.**  
    Independence and spanning can change if you change  $\mathbb F$ .
4.  **Using “infinite linear combinations.”**  
    Not allowed in pure linear algebra: “span” means finite linear combos.

* * *

3.4.13 Mastery checklist for 3.4
--------------------------------

You genuinely own 3.4 if you can do the following without “pattern-matching”:

*   Given a set  $\{v_1,\dots,v_k\}$ , prove dependent by finding a nontrivial relation, or prove independent by showing only trivial relation exists.
*   Use the redundancy theorem: dependent ⇔ one vector is in span of others.
*   Prove “basis ⇒ unique representation” and explain exactly where independence is used.
*   State and apply Steinitz exchange lemma (and understand the replacement construction).
*   Prove all bases have same size.
*   Extend an independent set to a basis, and reduce a spanning set to a basis (as theorems, not algorithms).
*   Translate “dimension” into: max independent size = min spanning size.

* * *

