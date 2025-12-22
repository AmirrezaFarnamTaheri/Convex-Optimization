
# Breakdown of convexity examples

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/12/2025 18:14:46  
**Updated:** 12/13/2025 1:30:22  
**Exported:** 12/13/2025 11:40:18  
**Link:** [https://chatgpt.com/g/g-p-693c475fdf788191a00d9dc0fb4c40b3/c/693c2a5d-2450-8328-8d22-e40cb72ed76c](https://chatgpt.com/g/g-p-693c475fdf788191a00d9dc0fb4c40b3/c/693c2a5d-2450-8328-8d22-e40cb72ed76c)  

## Prompt:
Breakdown, unpack, explain these four examples step-by-step, from first principle. Explain each step-completely, deep, detailed. Unpack everthing, make everything crystal clear.
  Be deep, detailed, rigorous, be self-contained and explain everything zero to hero! Breakdown into small granular steps, do not overlook anything. Explain everything verbally, make it crystal clear.

Below are the four examples, unpacked “from bedrock.” The unifying trick is: **if you can rewrite a function as a pointwise supremum of linear (affine) functions, it’s convex**; and similarly, **some structured infima/projections preserve convexity**.

---

## Example 3.10 — Maximum eigenvalue is convex

**Claim (as in the text).** For symmetric (X\in \mathbf S^m),
[
\lambda_{\max}(X)=\sup{,y^\top Xy \mid |y|_2=1,},
]
and since this is the supremum of linear functions of (X), it is convex.

### 1) What is (\lambda_{\max}(X))?

If (X\in \mathbf S^m) (real symmetric), it has an orthonormal eigen-decomposition
[
X = Q\Lambda Q^\top,\qquad Q^\top Q=I,\qquad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_m),
]
with real eigenvalues. Define (\lambda_{\max}(X)=\max_i \lambda_i).

### 2) Why (\lambda_{\max}(X)=\max_{|y|=1} y^\top Xy)? (Rayleigh–Ritz)

Take any unit vector (y). Write it in the eigenbasis: (y=Qz) where (|z|*2=|y|*2=1).
Then
[
y^\top Xy
= (Qz)^\top (Q\Lambda Q^\top)(Qz)
= z^\top \Lambda z
= \sum*{i=1}^m \lambda_i z_i^2.
]
Now note: (z_i^2\ge 0) and (\sum_i z_i^2=1), so ({z_i^2}) are weights of a convex combination. Therefore
[
\sum_i \lambda_i z_i^2 \le \lambda*{\max}\sum_i z_i^2 = \lambda_{\max}.
]
So (y^\top Xy \le \lambda_{\max}(X)) for every unit (y), hence
[
\sup_{|y|=1} y^\top Xy \le \lambda_{\max}(X).
]
Conversely, if (v) is a unit eigenvector for (\lambda_{\max}), then (v^\top Xv=\lambda_{\max}), so the supremum is **at least** (\lambda_{\max}). Combine both directions:
[
\lambda_{\max}(X)=\sup_{|y|=1} y^\top Xy.
]

### 3) Why is (X\mapsto y^\top Xy) linear in (X)?

Fix (y). Then
[
y^\top Xy = \sum_{i,j} y_i X_{ij} y_j
]
is a linear combination of the entries (X_{ij}) with coefficients (y_i y_j). Even cleaner:
[
y^\top Xy = \mathrm{tr}(y^\top Xy)=\mathrm{tr}(Xyy^\top)=\langle X,,yy^\top\rangle,
]
where (\langle A,B\rangle=\mathrm{tr}(A^\top B)) is the Frobenius inner product. That’s linear in (X).

### 4) Why does “supremum of linear” imply convex?

A linear function is convex. The pointwise supremum of any family of convex functions is convex. So (X\mapsto \sup_{|y|=1} y^\top Xy) is convex, exactly as stated in the book.

**Sanity check:** If (X=\mathrm{diag}(d)), then (y^\top Xy=\sum_i d_i y_i^2), whose max over (|y|=1) is (\max_i d_i). So this reduces to “max of coordinates,” which is convex.

---

## Example 3.11 — Matrix norm (spectral norm, and induced norms) is convex

The text gives the key variational forms:
[
|X|_2=\sup{u^\top Xv\mid |u|*2=1,\ |v|*2=1},
]
and more generally,
[
|X|*{a,b}
=\sup*{v\ne 0}\frac{|Xv|_a}{|v|*b}
=\sup{u^\top Xv\mid |u|*{a^\ast}=1,\ |v|_b=1}.
]
Then convexity follows because these are suprema of linear functions of (X).

### Part A) Spectral norm: (|X|_2)

#### 1) Definition

For (X\in\mathbb R^{p\times q}), the spectral norm is the operator norm induced by Euclidean norms:
[
|X|*2 := \sup*{|v|_2=1} |Xv|*2.
]
It equals the largest singular value (\sigma*{\max}(X)).

#### 2) Why (|X|*2 = \sup*{|u|=|v|=1} u^\top Xv)?

Fix (v) with (|v|*2=1). Consider the quantity (\sup*{|u|_2=1} u^\top (Xv)).
By Cauchy–Schwarz,
[
u^\top (Xv)\le |u|_2|Xv|_2 = |Xv|_2,
]
and equality is achieved by choosing (u = \frac{Xv}{|Xv|*2}) when (Xv\neq 0). Hence
[
\sup*{|u|_2=1} u^\top Xv = |Xv|_2.
]
Now take (\sup) over (|v|*2=1):
[
\sup*{|v|*2=1}\sup*{|u|*2=1} u^\top Xv
= \sup*{|v|_2=1} |Xv|_2
= |X|_2.
]
So indeed
[
|X|_2 = \sup{u^\top Xv\mid |u|_2=|v|_2=1},
]
matching the book’s statement.

#### 3) Why convex?

For fixed (u,v), the map (X\mapsto u^\top Xv) is linear in (X) (it’s (\langle X, uv^\top\rangle)). The supremum of linear functions is convex. Done.

---

### Part B) Induced norm (|X|_{a,b})

#### 1) Definition and rescaling

Given norms (|\cdot|*a) on (\mathbb R^p) and (|\cdot|*b) on (\mathbb R^q), the induced operator norm is
[
|X|*{a,b}=\sup*{v\ne 0}\frac{|Xv|_a}{|v|_b}.
]
Because norms are positively homogeneous, you can normalize (v): set (\tilde v = v/|v|_b) so (|\tilde v|_b=1). Then
[
\frac{|Xv|_a}{|v|_b}=|X\tilde v|*a,
]
so
[
|X|*{a,b}=\sup{|Xv|_a\mid |v|_b=1}.
]

#### 2) Dual norm identity: (|z|*a=\sup*{|u|_{a^\ast}=1} u^\top z)

The **dual norm** is defined by
[
|u|*{a^\ast}:=\sup*{|z|_a\le 1} u^\top z.
]
A standard theorem (essentially support functions of the unit ball) gives
[
|z|*a=\sup{u^\top z\mid |u|*{a^\ast}=1}.
]
Intuition: a norm is the support function of its dual unit ball.

Apply this with (z=Xv):
[
|Xv|*a = \sup*{|u|*{a^\ast}=1} u^\top (Xv)=\sup*{|u|_{a^\ast}=1} u^\top Xv.
]

#### 3) Put it together (swap suprema)

[
|X|*{a,b}
= \sup*{|v|*b=1}|Xv|*a
= \sup*{|v|*b=1}\ \sup*{|u|*{a^\ast}=1} u^\top Xv
= \sup{u^\top Xv\mid |u|_{a^\ast}=1,\ |v|_b=1},
]
which is exactly what the book writes.

#### 4) Convexity

Again: fixed (u,v) gives a linear function of (X); supremum of linear functions is convex. The book states this conclusion explicitly.

---

## Example 3.14 — Vector composition examples (the “monotone outer function” machine)

The book lists several composite constructions (f(x)=h(g_1(x),\dots,g_k(x))) where convexity/concavity drops out of two properties:

1. (h) is convex/concave, and
2. (h) is **monotone in each argument** (nondecreasing),
   plus (g_i) being convex/concave of the matching type.

### 0) The core composition proof (componentwise monotone outer function)

Let (g(x)=(g_1(x),\dots,g_k(x))).

Assume:

* each (g_i) is convex,
* (h:\mathbb R^k\to\mathbb R) is convex and nondecreasing in each component.

Take any (x_1,x_2) and (\theta\in[0,1]).

1. Convexity of each (g_i) gives the componentwise inequality
   [
   g(\theta x_1+(1-\theta)x_2)\ \le\ \theta g(x_1)+(1-\theta)g(x_2)
   \quad\text{(componentwise)}.
   ]
2. Since (h) is nondecreasing in each argument, plugging a smaller vector into (h) gives a smaller value:
   [
   h(g(\theta x_1+(1-\theta)x_2))
   \le
   h(\theta g(x_1)+(1-\theta)g(x_2)).
   ]
3. Now apply convexity of (h):
   [
   h(\theta g(x_1)+(1-\theta)g(x_2))
   \le
   \theta h(g(x_1))+(1-\theta)h(g(x_2)).
   ]
   Chaining these gives Jensen for (f=h\circ g), hence (f) is convex.

For concavity you flip the inequalities in the appropriate way (concave (h), concave (g_i), and monotone (h)).

The book summarizes these vector composition rules explicitly around this example.

Now the bullets.

---

### (i) Sum of the (r) largest components

The book’s statement: (h(z)=z_{[1]}+\cdots+z_{[r]}) is convex and nondecreasing; therefore the pointwise sum of the (r) largest (g_i(x)) is convex if the (g_i) are convex.

#### Why is (h) convex?

Key representation (earlier in the chapter): the sum of the (r) largest entries equals the maximum over all subsets (S) of size (r):
[
h(z)=\max\Big{\sum_{i\in S} z_i \ \Big|\ S\subset{1,\dots,k},\ |S|=r\Big}.
]
Each (\sum_{i\in S} z_i) is linear in (z). A pointwise maximum of linear functions is convex. Therefore (h) is convex.

#### Why nondecreasing?

If you increase some coordinate (z_j) and keep others fixed, then every subset-sum that includes (j) increases, and those that don’t include (j) stay the same; the maximum cannot go down. Hence (h) is nondecreasing in each argument.

Then the composition rule above gives convexity of (x\mapsto) “sum of the (r) largest (g_i(x)).”

---

### (ii) Log-sum-exp

Book statement: (h(z)=\log\big(\sum_i e^{z_i}\big)) is convex and nondecreasing, so (\log\big(\sum_i e^{g_i(x)}\big)) is convex when the (g_i) are convex.

#### Why nondecreasing?

Compute partial derivative:
[
\frac{\partial h}{\partial z_i}
=\frac{e^{z_i}}{\sum_j e^{z_j}}

> 0.
> ]
> So increasing any (z_i) increases (h).

#### Why convex? (Hessian is PSD)

Let (S=\sum_j e^{z_j}) and define softmax weights (s_i=e^{z_i}/S) so (s_i\ge 0), (\sum_i s_i=1).
Then
[
\nabla h(z)=s,\qquad
\nabla^2 h(z)=\mathrm{diag}(s)-ss^\top.
]
To show PSD, test any vector (v):
[
v^\top(\mathrm{diag}(s)-ss^\top)v
=================================

# \sum_i s_i v_i^2 - \Big(\sum_i s_i v_i\Big)^2

\mathrm{Var}_{i\sim s}(v_i)\ \ge\ 0.
]
So (\nabla^2 h(z)\succeq 0), hence (h) is convex. (This matches the standard derivation used in the slides, too.)

Then apply the composition rule (convex + nondecreasing outer, convex inner) to get convexity of (\log\sum e^{g_i(x)}).

---

### (iii) “(p)-aggregation” for (0<p\le 1): concavity on (\mathbb R_+^k)

Book statement: for (0<p\le 1),
[
h(z)=\Big(\sum_i z_i^p\Big)^{1/p}
\quad\text{on }\mathbb R_+^k
]
is concave, and its extension is nondecreasing; thus if (g_i) are concave and nonnegative, then (\big(\sum_i g_i(x)^p\big)^{1/p}) is concave.

Here’s a clean “first-principles” route that avoids messy second derivatives:

#### Step 1: (h) is 1-homogeneous

For (\alpha\ge 0),
[
h(\alpha z)
=\Big(\sum_i (\alpha z_i)^p\Big)^{1/p}
=\Big(\alpha^p\sum_i z_i^p\Big)^{1/p}
=\alpha h(z).
]

#### Step 2: (h) is log-concave on (\mathbb R_{++}^k)

For (z\succ 0),
[
\log h(z)
= \frac{1}{p}\log\Big(\sum_i z_i^p\Big).
]
Now:

* for (0<p\le 1), (t\mapsto t^p) is concave on (\mathbb R_+),
* sum of concave functions is concave, so (z\mapsto \sum_i z_i^p) is concave on (\mathbb R_+^k),
* (\log(\cdot)) is concave and increasing on (\mathbb R_{++}),
  so (\log\circ(\text{concave})) is concave. Multiply by (1/p>0): still concave.
  Therefore (\log h) is concave, i.e. (h) is log-concave.

#### Step 3: 1-homogeneous + log-concave (\Rightarrow) concave (the key lemma)

Let (f) be positive, 1-homogeneous, and log-concave on a convex cone. We prove:
[
f(\theta x+(1-\theta)y)\ \ge\ \theta f(x)+(1-\theta)f(y).
]
Take any (x,y) with (f(x),f(y)>0). Define
[
\bar x = \frac{x}{f(x)},\qquad \bar y = \frac{y}{f(y)}.
]
By 1-homogeneity, (f(\bar x)=f(\bar y)=1). Log-concavity gives
[
f(\theta \bar x+(1-\theta)\bar y)\ \ge\ f(\bar x)^\theta f(\bar y)^{1-\theta} = 1.
]
Now scale back. Consider
[
z = \theta x + (1-\theta) y
= \theta f(x)\bar x + (1-\theta)f(y)\bar y.
]
Let (s=\theta f(x)+(1-\theta)f(y)) and write
[
z = s\Big(\frac{\theta f(x)}{s}\bar x + \frac{(1-\theta)f(y)}{s}\bar y\Big),
]
where the coefficients are nonnegative and sum to 1. Using 1-homogeneity:
[
f(z)= s\cdot f\Big(\frac{\theta f(x)}{s}\bar x + \frac{(1-\theta)f(y)}{s}\bar y\Big).
]
By concavity of (\log f) (i.e. log-concavity of (f)) and the fact (f(\bar x)=f(\bar y)=1), the term in parentheses has (f(\cdot)\ge 1). Hence
[
f(z)\ge s = \theta f(x)+(1-\theta)f(y).
]
So (f) is concave.

Apply this lemma to (h): it is 1-homogeneous and log-concave, so it is concave on (\mathbb R_+^k).

#### Step 4: Why the “extension is nondecreasing” comment matters

The book notes we extend (h) by setting (h(z)=-\infty) if any component is negative, and that this extension is nondecreasing componentwise.
This is a technical condition needed for the most general composition theorem with extended-value functions; in this particular setting it ensures the monotonicity logic remains valid even on boundary/outside-domain points.

Then, with concave nonnegative (g_i), the composition rule yields concavity of (x\mapsto \big(\sum_i g_i(x)^p\big)^{1/p}), exactly as the book concludes.

---

### (iv) (p\ge 1): convex “(p)-aggregation”

Book statement: if (p\ge 1) and (g_i) are convex and nonnegative, then (\big(\sum_i g_i(x)^p\big)^{1/p}) is convex. The book proves it by introducing
[
h(z)=\Big(\sum_i \max{z_i,0}^p\Big)^{1/p},
]
which is convex and nondecreasing on all (\mathbb R^k). (full statement continues)

#### Why is this (h) convex?

Think of it as two layers:

1. **Positive part:** (z\mapsto z_+=\max{z,0}) (componentwise) is convex because each coordinate is the maximum of two affine functions (z_i) and (0).

2. **(\ell_p) norm:** (w\mapsto |w|*p=(\sum_i |w_i|^p)^{1/p}) is a norm for (p\ge 1), hence convex. On (\mathbb R*+^k), it is also nondecreasing in each coordinate.

Now (h(z)=|z_+|_p). This is a convex function of (z) (composition of convex pieces in a way that preserves convexity here; the book asserts convexity and monotonicity directly).

#### Why does this give the desired conclusion?

If the (g_i(x)\ge 0), then (g(x)\succeq 0) and (\max{g_i(x),0}=g_i(x)), so
[
h(g(x))=\Big(\sum_i g_i(x)^p\Big)^{1/p}.
]
Since (h) is convex and nondecreasing and each (g_i) is convex, (h\circ g) is convex, matching the book’s conclusion.

---

### (v) Geometric mean is concave (and composes with concave (g_i))

Book statement: (h(z)=\big(\prod_i z_i\big)^{1/k}) is concave on (\mathbb R_+^k), its extension is nondecreasing, and thus the geometric mean of nonnegative concave (g_i) is concave.

A crisp proof:
[
\log h(z)=\frac{1}{k}\sum_{i=1}^k \log z_i.
]
Each (\log z_i) is concave on (\mathbb R_{++}), so their average is concave; therefore (\log h) is concave, i.e. (h) is log-concave. Also (h) is 1-homogeneous:
[
h(\alpha z) = \alpha h(z)\quad (\alpha\ge 0).
]
By the same lemma used above (1-homogeneous + log-concave (\Rightarrow) concave), (h) is concave. Then composition with nonnegative concave (g_i) gives concavity of (\big(\prod_i g_i(x)\big)^{1/k}), as stated.

---

## Example 3.17 — Minimization over a linear equality preserves convexity

Book statement:
If (h) is convex, then
[
g(x)=\inf{h(y)\mid Ay=x}
]
is convex. The book shows this by defining
[
f(x,y)=\begin{cases}
h(y) & Ay=x\
\infty & \text{otherwise}
\end{cases}
]
which is convex in ((x,y)); then (g) is the minimum of (f) over (y), hence convex.

Let’s unpack every moving part.

### 1) Why is (f(x,y)) convex in ((x,y))?

Rewrite (f) as
[
f(x,y)=h(y)+I_{{(x,y):Ay=x}}(x,y),
]
where (I_S) is the indicator function: (0) on (S), (+\infty) outside.

* (h(y)) is convex in ((x,y)) because it doesn’t depend on (x) and is convex in (y).
* The set ({(x,y):Ay=x}) is an affine set (a linear equality), hence convex; the indicator of a convex set is a convex extended-value function.
* Sum of convex (extended-value) functions is convex.

So (f) is convex in ((x,y)).

### 2) Why does minimizing a jointly convex function over (y) give a convex function of (x)?

Define
[
g(x)=\inf_y f(x,y).
]
There are two equivalent “first principles” proofs.

#### Proof A (epigraph projection intuition)

The epigraph of (g) is
[
\mathrm{epi},g
= {(x,t): g(x)\le t}
= {(x,t): \exists y \text{ with } f(x,y)\le t}.
]
But ({(x,y,t): f(x,y)\le t}=\mathrm{epi},f), which is convex because (f) is convex.
Now (\mathrm{epi},g) is the projection of (\mathrm{epi},f) onto ((x,t)). Projections of convex sets are convex. Therefore (\mathrm{epi},g) is convex, hence (g) is convex.

#### Proof B (direct Jensen with (\varepsilon)-minimizers)

Take (x_1,x_2) and (\varepsilon>0). Choose (y_1,y_2) feasible with
[
Ay_i=x_i,\qquad h(y_i)\le g(x_i)+\varepsilon.
]
Then for (\theta\in[0,1]),
[
A(\theta y_1+(1-\theta)y_2)=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2,
]
so (y_\theta:=\theta y_1+(1-\theta)y_2) is feasible for (x_\theta:=\theta x_1+(1-\theta)x_2).
By convexity of (h),
[
h(y_\theta)\le \theta h(y_1)+(1-\theta)h(y_2)
\le \theta(g(x_1)+\varepsilon)+(1-\theta)(g(x_2)+\varepsilon).
]
Since (g(x_\theta)) is the infimum of (h(y)) over feasible (y), we have
[
g(x_\theta)\le h(y_\theta)\le \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
]
Let (\varepsilon\downarrow 0). This is Jensen’s inequality for (g), so (g) is convex.

That’s exactly the logic the book is invoking when it says “(g) is the minimum of (f) over (y), and hence is convex.”

**Interpretation:** (g) is an **optimal value function** of a convex problem parameterized by (x). Convexity of the value function is one of the most useful meta-facts in convex analysis.

---

If you want to go even deeper next, the natural continuations are: (1) subgradients of (\lambda_{\max}) and (|X|_2) via the argmax/arg-sup vectors, and (2) viewing Example 3.17 as an “infimal projection” / “partial minimization,” with explicit dual representations.

2/2

## Response:
You’ve already got the _right skeleton_ in your writeup. What I’ll do now is: **fill in every “obvious” step**, prove the meta-lemmas (supremum trick, projection trick, dual norm trick, monotone composition trick), and then re-derive each example as a clean corollary. Zero-to-hero, no handwaving.

* * *

Bedrock tools (you will use these 20 times)
===========================================

A. Convexity: the definition you must always reduce to
------------------------------------------------------

A function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  is **convex** if for all  $x_1,x_2$  and all  $\theta\in[0,1]$ ,

$$
f(\theta x_1+(1-\theta)x_2)\;\le\;\theta f(x_1)+(1-\theta)f(x_2).
$$

If  $f$  can take  $+\infty$ , that inequality is interpreted in the extended-value sense (and remains meaningful).

B. Lemma 1: supremum of affine functions is convex
--------------------------------------------------

Let  $\{a_\alpha,b_\alpha\}$  be any collection. Define

$$
f(x)=\sup_{\alpha}\,(a_\alpha^\top x+b_\alpha).
$$

Then  $f$  is convex.

**Proof (from the definition).** For any  $x_1,x_2,\theta$ :

$$
\begin{aligned} f(\theta x_1+(1-\theta)x_2) &=\sup_\alpha \big(a_\alpha^\top(\theta x_1+(1-\theta)x_2)+b_\alpha\big)\\ &=\sup_\alpha \big(\theta(a_\alpha^\top x_1+b_\alpha)+(1-\theta)(a_\alpha^\top x_2+b_\alpha)\big)\\ &\le \theta\sup_\alpha(a_\alpha^\top x_1+b_\alpha)\;+\;(1-\theta)\sup_\alpha(a_\alpha^\top x_2+b_\alpha)\\ &=\theta f(x_1)+(1-\theta)f(x_2). \end{aligned}
$$

The only “idea” step is  $\sup_\alpha(\theta u_\alpha+(1-\theta)v_\alpha)\le \theta\sup_\alpha u_\alpha+(1-\theta)\sup_\alpha v_\alpha$ , which is true because for each  $\alpha$ ,  $u_\alpha\le \sup u$  and  $v_\alpha\le \sup v$ . □

> Mental model: **a convex function is a “tent roof” made of supporting planes**. A supremum of affine functions is literally “take the highest plane at each point.”

C. Lemma 2: indicator of a convex set is convex
-----------------------------------------------

For a set  $C\subseteq\mathbb{R}^n$ , define the indicator

$$
I_C(x)=\begin{cases} 0,&x\in C,\\ +\infty,&x\notin C. \end{cases}
$$

Then  $I_C$  is convex **iff**  $C$  is convex.

**Reason:** the epigraph of  $I_C$  is  $C\times [0,\infty)$ , convex exactly when  $C$  is.

D. Lemma 3: projection (existential quantifier) preserves convexity
-------------------------------------------------------------------

If  $S\subseteq \mathbb{R}^{n+m}$  is convex, then its projection

$$
\Pi_x(S)=\{x\in\mathbb{R}^n:\exists y\in\mathbb{R}^m\text{ s.t. }(x,y)\in S\}
$$

is convex.

**Proof:** take two points  $x_1,x_2\in\Pi_x(S)$ . Then  $\exists y_1,y_2$  with  $(x_1,y_1),(x_2,y_2)\in S$ . By convexity of  $S$ ,  
 $(\theta x_1+(1-\theta)x_2,\;\theta y_1+(1-\theta)y_2)\in S$ .  
Hence  $\theta x_1+(1-\theta)x_2\in\Pi_x(S)$ . □

> This is the geometric engine behind “minimize over  $y$ ” preserving convexity.

E. Dual norm identity (support function of the dual ball)
---------------------------------------------------------

Given a norm  $\|\cdot\|_a$  on  $\mathbb{R}^p$ , its **dual norm** is

$$
\|u\|_{a^*}=\sup_{\|z\|_a\le 1}u^\top z.
$$

Then for every  $z$ ,

$$
\|z\|_a=\sup_{\|u\|_{a^*}\le 1}u^\top z=\sup_{\|u\|_{a^*}=1}u^\top z.
$$

**Proof (two inequalities).**

1.  For any  $\|u\|_{a^*}\le 1$ , by definition of dual norm,
    
$$
u^\top z \le \|u\|_{a^*}\|z\|_a\le \|z\|_a.
$$

So  $\sup_{\|u\|_{a^*}\le 1}u^\top z\le \|z\|_a$ .

2.  Existence of a maximizer / equality: geometrically,  $\|\cdot\|_a$  is the support function of the dual unit ball. More concretely: since the unit ball  $\{u:\|u\|_{a^*}\le 1\}$  is compact and  $u\mapsto u^\top z$  is continuous linear, the supremum is achieved at some  $u^\star$ . One can show (via supporting hyperplane theorem) that the optimum equals  $\|z\|_a$ . □

> For Euclidean norm, this reduces to “ $\|z\|_2=\max_{\|u\|_2=1}u^\top z$ ” with maximizer  $u=z/\|z\|_2$ .

* * *

Example 3.10 —  $\lambda_{\max}(X)$  is convex
==============================================

We work on  $\mathbf{S}^m$ : real symmetric matrices.

1) Spectral theorem (why symmetric matters)
-------------------------------------------

If  $X=X^\top$ , then there exists an orthonormal  $Q$  and real eigenvalues  $\lambda_1,\dots,\lambda_m$  such that

$$
X=Q\Lambda Q^\top,\qquad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_m),\qquad Q^\top Q=I.
$$

Define  $\lambda_{\max}(X)=\max_i \lambda_i$ .

2) Rayleigh quotient bound (the whole point)
--------------------------------------------

For any nonzero  $y$ ,

$$
R_X(y)=\frac{y^\top Xy}{y^\top y}.
$$

If  $\|y\|_2=1$ , then  $R_X(y)=y^\top Xy$ .

Write  $y=Qz$  with  $\|z\|_2=\|y\|_2=1$ . Then

$$
y^\top Xy=(Qz)^\top(Q\Lambda Q^\top)(Qz)=z^\top \Lambda z=\sum_{i=1}^m \lambda_i z_i^2.
$$

Now the key observation:

*   each  $z_i^2\ge 0$ ,
*    $\sum_i z_i^2=\|z\|_2^2=1$ .

So  $(z_i^2)$  are **weights of a convex combination**. Therefore

$$
\sum_{i=1}^m \lambda_i z_i^2 \le \lambda_{\max}(X)\sum_i z_i^2=\lambda_{\max}(X).
$$

Hence, for every unit  $y$ ,

$$
y^\top Xy\le \lambda_{\max}(X) \quad\Rightarrow\quad \sup_{\|y\|_2=1}y^\top Xy\le \lambda_{\max}(X).
$$

For the reverse inequality: let  $v$  be a unit eigenvector corresponding to  $\lambda_{\max}(X)$ , i.e.  $Xv=\lambda_{\max}(X)v$ . Then

$$
v^\top Xv=v^\top(\lambda_{\max}v)=\lambda_{\max}\,v^\top v=\lambda_{\max}(X).
$$

So the supremum is at least  $\lambda_{\max}(X)$ . Combine:

$$
\lambda_{\max}(X)=\max_{\|y\|_2=1}y^\top Xy=\sup_{\|y\|_2=1}y^\top Xy.
$$

3) Why  $X\mapsto y^\top Xy$  is linear
---------------------------------------

Fix  $y$ . Expand:

$$
y^\top Xy=\sum_{i,j}y_iX_{ij}y_j,
$$

a linear combination of the entries  $X_{ij}$ .

Cleaner: use Frobenius inner product  $\langle A,B\rangle=\mathrm{tr}(A^\top B)$ . Then

$$
y^\top Xy=\mathrm{tr}(y^\top Xy)=\mathrm{tr}(Xyy^\top)=\langle X,yy^\top\rangle.
$$

That’s linear in  $X$ .

4) Convexity (one line, but now justified)
------------------------------------------

$$
\lambda_{\max}(X)=\sup_{\|y\|_2=1}\langle X,yy^\top\rangle
$$

is a supremum of linear functions of  $X$ , so by Lemma 1 it’s convex.

### Edge case sanity

If the top eigenvalue has multiplicity  $>1$ , the maximizer  $y$  is not unique (any unit vector in the top eigenspace works). Convexity doesn’t care; it loves non-uniqueness.

* * *

Example 3.11 — Matrix operator norms are convex
===============================================

Part A: spectral norm  $\|X\|_2$ 
---------------------------------

### 1) Definition

For  $X\in\mathbb{R}^{p\times q}$ ,

$$
\|X\|_2=\sup_{\|v\|_2=1}\|Xv\|_2.
$$

### 2) Turn  $\|Xv\|_2$  into a supremum of linear forms

For a fixed  $v$ , use the Euclidean dual identity:

$$
\|Xv\|_2=\sup_{\|u\|_2=1}u^\top (Xv).
$$

**Why?** By Cauchy–Schwarz,  $u^\top(Xv)\le \|u\|_2\|Xv\|_2=\|Xv\|_2$ . Equality if  $u=Xv/\|Xv\|_2$  when  $Xv\neq 0$ ; if  $Xv=0$ , both sides are  $0$ .

Now plug into the definition:

$$
\|X\|_2 =\sup_{\|v\|_2=1}\sup_{\|u\|_2=1}u^\top Xv =\sup_{\|u\|_2=1,\ \|v\|_2=1}u^\top Xv.
$$

### 3) Convexity

For fixed  $u,v$ ,

$$
u^\top Xv=\langle X,uv^\top\rangle
$$

is linear in  $X$ . Supremum of linear functions ⇒ convex.

Part B: induced norm  $\|X\|_{a,b}$ 
------------------------------------

### 1) Definition and normalization

Given norms  $\|\cdot\|_a$  on  $\mathbb{R}^p$ ,  $\|\cdot\|_b$  on  $\mathbb{R}^q$ ,

$$
\|X\|_{a,b}=\sup_{v\neq 0}\frac{\|Xv\|_a}{\|v\|_b}.
$$

Because norms are positively homogeneous, set  $\tilde v=v/\|v\|_b$ . Then  $\|\tilde v\|_b=1$  and

$$
\frac{\|Xv\|_a}{\|v\|_b}=\|X\tilde v\|_a.
$$

So

$$
\|X\|_{a,b}=\sup_{\|v\|_b=1}\|Xv\|_a.
$$

### 2) Dualize  $\|Xv\|_a$ 

By the dual norm identity (tool E),

$$
\|Xv\|_a=\sup_{\|u\|_{a^*}=1}u^\top (Xv)=\sup_{\|u\|_{a^*}=1}u^\top Xv.
$$

Hence

$$
\|X\|_{a,b} =\sup_{\|v\|_b=1}\sup_{\|u\|_{a^*}=1}u^\top Xv =\sup_{\|u\|_{a^*}=1,\ \|v\|_b=1}u^\top Xv.
$$

### 3) Convexity

Again,  $X\mapsto u^\top Xv$  is linear. Supremum of linear ⇒ convex.

### Edge case notes

*   If the feasible set  $\{v:\|v\|_b=1\}$  is compact (true in finite dimensions), the supremum is achieved.
*   If  $X=0$ , the maximizers are wildly non-unique; still convex.

* * *

Example 3.14 — Vector composition rules (a.k.a. “monotone outer function machine”)
==================================================================================

This example is really: **prove one theorem**, then treat all the bullets as plug-ins.

0) The composition theorem you’re actually using
------------------------------------------------

Let  $g:\mathbb{R}^n\to\mathbb{R}^k$  with components  $g_i$ . Let  $h:\mathbb{R}^k\to\mathbb{R}\cup\{+\infty\}$ .  
Assume:

1.  each  $g_i$  is convex, so  $g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y)$  componentwise;
2.   $h$  is convex;
3.   $h$  is **nondecreasing in each component**: if  $u\le v$  componentwise, then  $h(u)\le h(v)$ .

Define  $f(x)=h(g(x))$ . Then  $f$  is convex.

### Proof (pure definition chasing)

Take  $x_1,x_2,\theta$ . By convexity of each  $g_i$ ,

$$
g(\theta x_1+(1-\theta)x_2)\;\le\;\theta g(x_1)+(1-\theta)g(x_2)\quad\text{(componentwise)}.
$$

Monotonicity of  $h$  preserves the inequality:

$$
h(g(\theta x_1+(1-\theta)x_2)) \le h(\theta g(x_1)+(1-\theta)g(x_2)).
$$

Then apply convexity of  $h$ :

$$
h(\theta g(x_1)+(1-\theta)g(x_2)) \le \theta h(g(x_1))+(1-\theta)h(g(x_2)).
$$

Chain them and you get Jensen for  $f$ . □

> Concave version: flip the convex/concave assumptions consistently. The proof is literally the same inequality chain with directions flipped.

Now the specific  $h$ ’s.

* * *

(i) Sum of the  $r$  largest components is convex + monotone
------------------------------------------------------------

Let  $z\in\mathbb{R}^k$ . Let  $z_{[1]}\ge z_{[2]}\ge\cdots\ge z_{[k]}$  be the sorted components. Define

$$
h(z)=\sum_{j=1}^r z_{[j]}.
$$

### Convexity via “max of linear”

Claim:

$$
h(z)=\max_{\substack{S\subset\{1,\dots,k\}\\|S|=r}}\ \sum_{i\in S} z_i.
$$

**Why true?**

*   For any fixed subset  $S$  of size  $r$ ,  $\sum_{i\in S}z_i$  is the sum of some  $r$  components.
*   The **largest** such subset sum is achieved by picking the  $r$  largest components, i.e.  $\{[1],\dots,[r]\}$ .  
    So the maximum over subsets equals the sum of the top  $r$ .

Each subset sum is linear in  $z$ . Maximum of linear functions is convex (Lemma 1).

### Monotonicity

Increase one coordinate  $z_j$ . Any subset sum that includes  $j$  increases, the rest stay unchanged, so the maximum cannot decrease.

**Composition punchline:** If each  $g_i(x)$  is convex, then  $x\mapsto$  “sum of the  $r$  largest  $g_i(x)$ ” is convex.

* * *

(ii) Log-sum-exp is convex + strictly increasing
------------------------------------------------

Define

$$
h(z)=\log\left(\sum_{i=1}^k e^{z_i}\right).
$$

### Monotonicity

Compute partial derivative (where finite):

$$
\frac{\partial h}{\partial z_i}=\frac{e^{z_i}}{\sum_j e^{z_j}}>0.
$$

So it’s strictly increasing in each coordinate.

### Convexity (Hessian is PSD, no vibes)

Let  $S=\sum_j e^{z_j}$  and  $s_i=e^{z_i}/S$  (softmax). Then  $\sum_i s_i=1$ ,  $s_i\ge 0$ .  
You can compute

$$
\nabla h(z)=s,\qquad \nabla^2 h(z)=\mathrm{diag}(s)-ss^\top.
$$

Test PSD: for any  $v\in\mathbb{R}^k$ ,

$$
v^\top(\mathrm{diag}(s)-ss^\top)v=\sum_i s_i v_i^2-\left(\sum_i s_i v_i\right)^2.
$$

That is exactly  $\mathrm{Var}_{i\sim s}(v_i)\ge 0$ . Hence Hessian  $\succeq 0$ , so  $h$  is convex.

**Composition punchline:** if each  $g_i$  convex, then  $x\mapsto \log\sum_i e^{g_i(x)}$  is convex.

* * *

(iii) “ $p$ \-aggregation” for  $0<p\le 1$ : concave on  $\mathbb{R}_+^k$ 
--------------------------------------------------------------------------

Define for  $z\in\mathbb{R}_+^k$ :

$$
h(z)=\Big(\sum_i z_i^p\Big)^{1/p}.
$$

Two facts to prove: **(1) it is 1-homogeneous**, **(2) it is log-concave**. Then use the lemma “1-homogeneous + log-concave ⇒ concave”.

### Step 1: 1-homogeneity

For  $\alpha\ge 0$ ,

$$
h(\alpha z)=\left(\sum_i (\alpha z_i)^p\right)^{1/p} =\left(\alpha^p\sum_i z_i^p\right)^{1/p} =\alpha h(z).
$$

### Step 2: log-concavity

Consider  $z\succ 0$  (strictly positive components) so logs are finite.

$$
\log h(z)=\frac{1}{p}\log\left(\sum_i z_i^p\right).
$$

Now:

*   for  $0<p\le 1$ ,  $t\mapsto t^p$  is concave on  $\mathbb{R}_+$ ;
*   hence  $z\mapsto \sum_i z_i^p$  is concave on  $\mathbb{R}_+^k$ ;
*    $\log(\cdot)$  is concave and increasing on  $\mathbb{R}_{++}$ ;
*   **increasing concave  $\circ$  concave is concave** (same inequality chain as earlier but with concavity directions).  
    Thus  $\log(\sum_i z_i^p)$  is concave, and multiplying by  $1/p>0$  preserves concavity. So  $\log h$  is concave:  $h$  is log-concave.

### Step 3: Lemma — positive + 1-homogeneous + log-concave ⇒ concave

Assume  $f>0$ , 1-homogeneous, and log-concave on a convex cone  $K$ . Then  $f$  is concave on  $K$ .

**Proof (clean and explicit).** Take  $x,y\in K$ ,  $\theta\in[0,1]$ . Let

$$
a=f(x),\quad b=f(y),\quad \bar x=x/a,\quad \bar y=y/b.
$$

By 1-homogeneity,  $f(\bar x)=f(\bar y)=1$ .

Let  $s=\theta a+(1-\theta)b$  and define weights

$$
\alpha=\frac{\theta a}{s},\qquad \beta=\frac{(1-\theta)b}{s},
$$

so  $\alpha,\beta\ge 0$  and  $\alpha+\beta=1$ .

Now rewrite the convex combination:

$$
\theta x+(1-\theta)y =\theta a\bar x+(1-\theta)b\bar y =s(\alpha \bar x+\beta \bar y).
$$

Apply 1-homogeneity:

$$
f(\theta x+(1-\theta)y)=s\,f(\alpha \bar x+\beta \bar y).
$$

Apply log-concavity to  $\alpha \bar x+\beta \bar y$ :

$$
f(\alpha \bar x+\beta \bar y)\ge f(\bar x)^\alpha f(\bar y)^\beta = 1^\alpha 1^\beta=1.
$$

So

$$
f(\theta x+(1-\theta)y)\ge s=\theta f(x)+(1-\theta)f(y).
$$

That’s concavity. □

Apply to  $h$ . Conclusion:  $h$  is concave on  $\mathbb{R}_+^k$ .

**Composition punchline:** if each  $g_i$  is concave and  $g_i(x)\ge 0$ , then  $x\mapsto(\sum_i g_i(x)^p)^{1/p}$  is concave.

* * *

(iv) For  $p\ge 1$ : convex  $p$ \-aggregation (with nonnegativity)
-------------------------------------------------------------------

Let  $p\ge 1$ . Define on all  $\mathbb{R}^k$ :

$$
\tilde h(z)=\left(\sum_i (z_i)_+^p\right)^{1/p},\qquad (t)_+=\max\{t,0\}.
$$

### Why convex?

*    $z\mapsto z_+$  is convex (max of two affine functions).
*    $w\mapsto \|w\|_p=(\sum_i |w_i|^p)^{1/p}$  is a norm for  $p\ge 1$ , hence convex.
*   Also  $\|w\|_p$  is nondecreasing in each coordinate on  $\mathbb{R}_+^k$ .

And  $\tilde h(z)=\|z_+\|_p$ . This is a standard convex construction (it’s essentially a norm applied after a convex monotone map).

If additionally  $g_i(x)\ge 0$ , then  $(g_i(x))_+=g_i(x)$ , so

$$
\tilde h(g(x))=\left(\sum_i g_i(x)^p\right)^{1/p}.
$$

By the monotone convex composition theorem, convexity follows when  $g_i$  are convex and nonnegative.

* * *

(v) Geometric mean is concave on  $\mathbb{R}_+^k$ 
---------------------------------------------------

$$
h(z)=\left(\prod_{i=1}^k z_i\right)^{1/k},\qquad z\in\mathbb{R}_+^k.
$$

On  $z\succ 0$ ,

$$
\log h(z)=\frac{1}{k}\sum_{i=1}^k \log z_i.
$$

Each  $\log z_i$  is concave, average is concave ⇒  $\log h$  concave ⇒  $h$  log-concave.  
Also  $h(\alpha z)=\alpha h(z)$  (1-homogeneous).  
By the same lemma,  $h$  is concave.

**Composition punchline:** geometric mean of nonnegative concave  $g_i$  is concave.

* * *

Example 3.17 — Partial minimization with linear equality preserves convexity
============================================================================

We’re given convex  $h:\mathbb{R}^m\to\mathbb{R}\cup\{+\infty\}$ , matrix  $A\in\mathbb{R}^{n\times m}$ , and define

$$
g(x)=\inf\{h(y)\mid Ay=x\}.
$$

(If the constraint is infeasible, the infimum over an empty set is  $+\infty$ .)

1) Build the joint function  $f(x,y)$ 
--------------------------------------

Define the affine constraint set

$$
C=\{(x,y)\in\mathbb{R}^n\times\mathbb{R}^m:\ Ay=x\}.
$$

This is an **affine** (hence convex) set.

Define

$$
f(x,y)=h(y)+I_C(x,y) = \begin{cases} h(y),&Ay=x,\\ +\infty,&\text{otherwise}. \end{cases}
$$

### Why is  $f$  convex in  $(x,y)$ ?

*    $h(y)$  is convex in  $(x,y)$  because it is convex in  $y$  and independent of  $x$ .
*    $I_C(x,y)$  is convex because  $C$  is convex (Lemma 2).
*   Sum of convex functions is convex (still true for extended-value functions).

So  $f$  is jointly convex.

2) Show  $g(x)=\inf_y f(x,y)$  is convex
----------------------------------------

### Proof A: epigraph projection (pure geometry)

The epigraph of  $f$  is

$$
\mathrm{epi}\,f=\{(x,y,t): f(x,y)\le t\},
$$

which is convex because  $f$  is convex.

Now compute epigraph of  $g$ :

$$
\begin{aligned} \mathrm{epi}\,g &=\{(x,t): g(x)\le t\}\\ &=\{(x,t): \exists y\ \text{s.t.}\ f(x,y)\le t\}\\ &=\Pi_{x,t}(\mathrm{epi}\,f), \end{aligned}
$$

a projection of a convex set. Projections preserve convexity (Lemma 3). Hence  $\mathrm{epi}\,g$  is convex, so  $g$  is convex.

That’s the cleanest “why minimization preserves convexity” proof.

### Proof B:  $\varepsilon$ \-minimizers (pure Jensen algebra)

Take  $x_1,x_2,\theta$ . Fix  $\varepsilon>0$ . Choose feasible  $y_1,y_2$  such that

$$
Ay_i=x_i,\qquad h(y_i)\le g(x_i)+\varepsilon.
$$

Define  $y_\theta=\theta y_1+(1-\theta)y_2$ . Then

$$
Ay_\theta=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2=:x_\theta.
$$

So  $y_\theta$  is feasible for  $x_\theta$ . By convexity of  $h$ ,

$$
h(y_\theta)\le \theta h(y_1)+(1-\theta)h(y_2) \le \theta(g(x_1)+\varepsilon)+(1-\theta)(g(x_2)+\varepsilon).
$$

Since  $g(x_\theta)$  is the infimum over feasible  $y$ ,  $g(x_\theta)\le h(y_\theta)$ . So

$$
g(x_\theta)\le \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
$$

Let  $\varepsilon\downarrow 0$  to get Jensen. So  $g$  is convex.

3) Interpretation you should keep in your head
----------------------------------------------

 $g(x)$  is the **optimal value function** of a convex problem parameterized by  $x$ . Example 3.17 is the generic theorem behind “value functions of convex problems are convex in the parameters.”

### Edge cases

*   If for some  $x$ , there is no  $y$  with  $Ay=x$ , then  $g(x)=+\infty$ . That is still a convex function (its epigraph remains convex).
*   If  $h$  is not proper (e.g. identically  $+\infty$  or can take  $-\infty$ ), you need to be careful. Standard convex analysis assumes **proper convex**: never  $-\infty$ , not identically  $+\infty$ .

* * *

Optional but extremely useful “next layer”: subgradients (why these variational forms are gold)
===============================================================================================

You hinted at this, so here’s the crisp version.

Subgradient of  $\lambda_{\max}$ 
---------------------------------

If  $X\in \mathbf{S}^m$  and the top eigenvalue is simple with unit eigenvector  $v$ , then

$$
\partial \lambda_{\max}(X)=\{vv^\top\}.
$$

If the top eigenvalue has multiplicity  $r$ , then

$$
\partial \lambda_{\max}(X)=\mathrm{conv}\{vv^\top:\ v\ \text{unit in the top eigenspace}\}.
$$

This drops straight out of “supremum of linear forms”: active maximizers give supporting hyperplanes.

Subgradient of  $\|X\|_2$ 
--------------------------

If  $X$  has a unique top singular value with left/right unit singular vectors  $u,v$ , then

$$
\partial \|X\|_2=\{uv^\top\}.
$$

With multiplicity, take convex hull of  $u_iv_i^\top$  over top singular vector pairs.

* * *

If you want to push even further in a mathematically satisfying way, the natural “boss fight” is to connect **Example 3.17** to Fenchel duality and derive a dual representation for  $g$  (it becomes a supremum over Lagrange multipliers), which loops you right back to the “supremum of affine” convexity engine—everything becomes one big self-referential convexity ouroboros.

## Prompt:
Further unpacl, breakdown. Also if you have used a theorem, if possible prove directly.
In addition, if there is an interesting alternative proof, also add it.

Be more granular, detaoeld. Further unpack, breakdown, explain completer, crystal clear.

## Response:
Thought for 28s

Alright. I’ll go **more granular**, and I’ll **prove (directly) every theorem/lemma I invoke**, plus give **interesting alternative proofs** where they exist. This will feel like peeling an onion until you reach the axioms and cry a little.

I’ll structure this as:

1.  **Bedrock lemmas** (proved from scratch)
2.  **Example 3.10** (λmax convex) + alternative proofs
3.  **Example 3.11** (operator norms convex) + alternative proofs
4.  **Example 3.14** (composition machine) + multiple alternative proofs for key bullets
5.  **Example 3.17** (partial minimization under linear equality) + dual representation alternative proof

Throughout, I’ll be explicit about what is _definition_, what is _lemma_, what is _corollary_, and what assumptions matter.

* * *

1) Bedrock lemmas, proved directly
==================================

1.1 Convexity definition (extended-value version)
-------------------------------------------------

A function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  is **convex** if for all  $x_1,x_2\in\mathbb{R}^n$  and all  $\theta\in[0,1]$ ,

$$
f(\theta x_1+(1-\theta)x_2)\ \le\ \theta f(x_1)+(1-\theta)f(x_2),
$$

where arithmetic with  $+\infty$  uses the standard conventions:

*    $a + (+\infty) = +\infty$ ,
*    $\theta(+\infty)=+\infty$  if  $\theta>0$ .

This definition works smoothly for indicator functions and constrained problems.

* * *

1.2 Lemma: pointwise supremum of convex functions is convex
-----------------------------------------------------------

Let  $\{f_\alpha\}_{\alpha\in\mathcal{A}}$  be any family of convex functions (possibly extended-value). Define

$$
f(x):=\sup_{\alpha\in\mathcal{A}} f_\alpha(x).
$$

Then  $f$  is convex.

### Proof (from the definition, with no geometry)

Fix  $x_1,x_2,\theta$ . For every  $\alpha$ ,

$$
f_\alpha(\theta x_1+(1-\theta)x_2)\le \theta f_\alpha(x_1)+(1-\theta)f_\alpha(x_2)
$$

(convexity of  $f_\alpha$ ). Now take supremum over  $\alpha$  on the left:

$$
\sup_\alpha f_\alpha(\theta x_1+(1-\theta)x_2)\le \sup_\alpha\big(\theta f_\alpha(x_1)+(1-\theta)f_\alpha(x_2)\big).
$$

Next use the elementary inequality (true for any real families  $u_\alpha,v_\alpha$ ):

$$
\sup_\alpha(\theta u_\alpha+(1-\theta)v_\alpha)\le \theta \sup_\alpha u_\alpha+(1-\theta)\sup_\alpha v_\alpha.
$$

Apply it with  $u_\alpha=f_\alpha(x_1)$ ,  $v_\alpha=f_\alpha(x_2)$ . Then:

$$
f(\theta x_1+(1-\theta)x_2)\le \theta f(x_1)+(1-\theta)f(x_2).
$$

So  $f$  is convex. □

**Special case:** if each  $f_\alpha$  is affine (linear + constant), this says _sup of affine ⇒ convex_.

* * *

1.3 Lemma: max of finitely many affine functions is convex
----------------------------------------------------------

If  $f(x)=\max_{i=1,\dots,m}(a_i^\top x+b_i)$ , then  $f$  is convex.

**Proof:** it’s a supremum over a finite set, so it’s a special case of Lemma 1.2. □

* * *

1.4 Lemma: indicator of a convex set is convex (proved by Jensen directly)
--------------------------------------------------------------------------

Let  $C\subseteq\mathbb{R}^n$ . Define

$$
I_C(x)=\begin{cases} 0,&x\in C,\\ +\infty,&x\notin C. \end{cases}
$$

Then  $I_C$  is convex **iff**  $C$  is convex.

### Proof (⇒ direction)

Assume  $I_C$  is convex. Take any  $x_1,x_2\in C$ . Then  $I_C(x_1)=I_C(x_2)=0$ . By convexity,

$$
I_C(\theta x_1+(1-\theta)x_2)\le \theta\cdot 0+(1-\theta)\cdot 0=0.
$$

But  $I_C$  only takes values  $0$  or  $+\infty$ , so the left side must be  $0$ , meaning  $\theta x_1+(1-\theta)x_2\in C$ . Hence  $C$  is convex.

### Proof (⇐ direction)

Assume  $C$  is convex. We must show Jensen for  $I_C$ . Consider any  $x_1,x_2$  and  $\theta\in[0,1]$ . There are cases:

*   If either  $x_1\notin C$  or  $x_2\notin C$ , then the RHS  $\theta I_C(x_1)+(1-\theta)I_C(x_2)=+\infty$ . The inequality  $I_C(\cdot)\le +\infty$  holds automatically.
*   If  $x_1,x_2\in C$ , then RHS  $=0$ . Since  $C$  is convex,  $\theta x_1+(1-\theta)x_2\in C$ , so LHS  $=0$ . Inequality holds with equality.

So  $I_C$  is convex. □

* * *

1.5 Lemma: projection of a convex set is convex (proved directly)
-----------------------------------------------------------------

Let  $S\subseteq\mathbb{R}^{n+m}$  be convex. Define its projection onto  $x$ \-space:

$$
\Pi_x(S)=\{x\in\mathbb{R}^n:\exists y\in\mathbb{R}^m\text{ such that }(x,y)\in S\}.
$$

Then  $\Pi_x(S)$  is convex.

### Proof

Take  $x_1,x_2\in \Pi_x(S)$ . By definition, there exist  $y_1,y_2$  such that  $(x_1,y_1)\in S$  and  $(x_2,y_2)\in S$ .  
Since  $S$  is convex,

$$
(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2)\in S.
$$

Therefore  $\theta x_1+(1-\theta)x_2\in\Pi_x(S)$ . □

This is the **existential quantifier preserves convexity** fact: “ $\exists y$ ” corresponds to projection.

* * *

1.6 Dual norm identity (proved carefully)
-----------------------------------------

### Definitions

Let  $\|\cdot\|_a$  be a norm on  $\mathbb{R}^p$ . Define its dual norm:

$$
\|u\|_{a^\*} := \sup_{\|z\|_a\le 1} u^\top z.
$$

### Claim A (generalized Cauchy–Schwarz / Hölder inequality)

For all  $u,z$ ,

$$
u^\top z \le \|u\|_{a^\*}\,\|z\|_a.
$$

#### Proof

If  $z=0$ , trivial. If  $z\neq 0$ , write  $z=\|z\|_a \cdot \bar z$  where  $\|\bar z\|_a=1$ . Then

$$
u^\top z = \|z\|_a\, u^\top \bar z \le \|z\|_a \sup_{\|w\|_a\le 1} u^\top w = \|z\|_a\,\|u\|_{a^\*}.
$$

□

### Claim B (support function representation of the primal norm)

For all  $z$ ,

$$
\|z\|_a = \sup_{\|u\|_{a^\*}\le 1} u^\top z = \sup_{\|u\|_{a^\*}=1} u^\top z.
$$

#### Proof (two inequalities)

**(≤)** For any  $\|u\|_{a^\*}\le 1$ , Claim A gives  $u^\top z \le \|z\|_a$ . Taking supremum over such  $u$ ,

$$
\sup_{\|u\|_{a^\*}\le 1} u^\top z \le \|z\|_a.
$$

**(≥)** This direction is the “supporting hyperplane exists” fact. Here’s a direct finite-dimensional proof sketch that doesn’t hide the logic:

*   Let  $B=\{w:\|w\|_a\le 1\}$ , the (closed, convex, bounded) unit ball.
*   Fix  $z\neq 0$ . Consider the point  $\bar z = z/\|z\|_a$ , which lies on the boundary of  $B$  (since  $\|\bar z\|_a=1$ ).
*   In finite dimensions, for any closed convex set and a boundary point, there exists a supporting hyperplane at that boundary point. Concretely: there exists  $u\neq 0$  such that
    $$
    u^\top w \le u^\top \bar z \quad \forall w\in B.
    $$
*   Divide  $u$  by  $u^\top \bar z$  (which is positive after choosing the outward normal) to get a vector  $\tilde u$  satisfying
    $$
    \tilde u^\top w \le 1\quad \forall w\in B, \qquad\text{and}\qquad \tilde u^\top \bar z = 1.
    $$
*   The condition  $\tilde u^\top w \le 1$  for all  $\|w\|_a\le 1$  is exactly  $\|\tilde u\|_{a^\*}\le 1$ .
*   Then
    $$
    \sup_{\|u\|_{a^\*}\le 1} u^\top z \ \ge\ \tilde u^\top z = \tilde u^\top (\|z\|_a \bar z) = \|z\|_a(\tilde u^\top \bar z) = \|z\|_a.
    $$

Combine with (≤), we get equality. □

**Important:** the only “theorem” used is existence of a supporting hyperplane for a closed convex set at a boundary point (true in finite dimensions; it’s a standard separation theorem consequence).

* * *

1.7 Composition theorem with monotone outer function (proved from scratch)
--------------------------------------------------------------------------

### Statement (convex version)

Let  $g:\mathbb{R}^n\to\mathbb{R}^k$  with components  $g_i$ . Let  $h:\mathbb{R}^k\to\mathbb{R}\cup\{+\infty\}$ .

Assume:

1.  each  $g_i$  is convex,
2.   $h$  is convex,
3.   $h$  is componentwise nondecreasing:  $u\le v\Rightarrow h(u)\le h(v)$ .

Then  $f(x):=h(g(x))$  is convex.

### Proof (pure inequality chaining)

Fix  $x_1,x_2,\theta\in[0,1]$ . For each component  $i$ ,

$$
g_i(\theta x_1+(1-\theta)x_2)\le \theta g_i(x_1)+(1-\theta)g_i(x_2).
$$

Stack them: this is the vector inequality

$$
g(\theta x_1+(1-\theta)x_2)\le \theta g(x_1)+(1-\theta)g(x_2) \quad\text{(componentwise)}.
$$

Monotonicity of  $h$  preserves inequality:

$$
h(g(\theta x_1+(1-\theta)x_2))\le h(\theta g(x_1)+(1-\theta)g(x_2)).
$$

Then convexity of  $h$  gives Jensen in  $\mathbb{R}^k$ :

$$
h(\theta g(x_1)+(1-\theta)g(x_2)) \le \theta h(g(x_1))+(1-\theta)h(g(x_2)).
$$

Chain them:

$$
f(\theta x_1+(1-\theta)x_2)\le \theta f(x_1)+(1-\theta)f(x_2).
$$

So  $f$  is convex. □

(Concave version is identical with inequalities reversed and “nondecreasing” used the same way.)

* * *

2) Example 3.10 — Maximum eigenvalue is convex (more granular + alt proofs)
===========================================================================

We work with **symmetric** matrices  $X\in\mathbf{S}^m$  (real,  $X=X^\top$ ). Symmetry matters because it guarantees:

*   real eigenvalues,
*   orthonormal eigenvectors,
*   the Rayleigh quotient characterization.

2.1 Rayleigh–Ritz: prove  $\lambda_{\max}(X)=\max_{\|y\|_2=1} y^\top X y$ 
--------------------------------------------------------------------------

### Step 0: spectral decomposition

By the spectral theorem,

$$
X = Q\Lambda Q^\top,\quad Q^\top Q=I,\quad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_m).
$$

Let  $\lambda_{\max}=\max_i\lambda_i$ .

### Step 1: change coordinates

Take any unit vector  $y$  ( $\|y\|_2=1$ ). Define  $z:=Q^\top y$ . Since  $Q$  is orthonormal,

$$
\|z\|_2=\|Q^\top y\|_2=\|y\|_2=1.
$$

### Step 2: expand the quadratic form

$$
\begin{aligned} y^\top X y &= y^\top (Q\Lambda Q^\top) y\\ &= (Q^\top y)^\top \Lambda (Q^\top y)\\ &= z^\top \Lambda z\\ &= \sum_{i=1}^m \lambda_i z_i^2. \end{aligned}
$$

### Step 3: interpret  $z_i^2$  as convex weights

Because  $z_i^2\ge 0$  and  $\sum_i z_i^2=\|z\|_2^2=1$ , the numbers  $w_i:=z_i^2$  satisfy

$$
w_i\ge 0,\qquad \sum_i w_i=1.
$$

So  $\sum_i\lambda_i w_i$  is a **convex combination** of the eigenvalues.

### Step 4: bound by the maximum eigenvalue

A convex combination never exceeds the maximum value:

$$
\sum_{i=1}^m \lambda_i w_i \le \lambda_{\max}\sum_i w_i=\lambda_{\max}.
$$

So for every unit  $y$ ,

$$
y^\top X y \le \lambda_{\max}(X).
$$

Therefore

$$
\sup_{\|y\|_2=1} y^\top X y \le \lambda_{\max}(X).
$$

### Step 5: achieve equality

Let  $v$  be a unit eigenvector associated with  $\lambda_{\max}$ :  $Xv=\lambda_{\max}v$ ,  $\|v\|_2=1$ .  
Then

$$
v^\top X v = v^\top (\lambda_{\max} v)=\lambda_{\max} v^\top v = \lambda_{\max}.
$$

So

$$
\sup_{\|y\|_2=1} y^\top X y \ge \lambda_{\max}(X).
$$

### Conclusion

$$
\lambda_{\max}(X)=\max_{\|y\|_2=1} y^\top X y.
$$

* * *

2.2 Prove convexity using only this characterization (no extra theorem)
-----------------------------------------------------------------------

We want:

$$
\lambda_{\max}(\theta X+(1-\theta)Y)\le \theta\lambda_{\max}(X)+(1-\theta)\lambda_{\max}(Y).
$$

Start with Rayleigh–Ritz:

$$
\lambda_{\max}(\theta X+(1-\theta)Y) = \max_{\|u\|_2=1} u^\top (\theta X+(1-\theta)Y) u.
$$

Distribute:

$$
u^\top (\theta X+(1-\theta)Y) u = \theta (u^\top X u) + (1-\theta)(u^\top Y u).
$$

Now take max over  $u$ . Use the basic inequality:

$$
\max_u \big(\theta a_u+(1-\theta)b_u\big) \le \theta \max_u a_u + (1-\theta)\max_u b_u.
$$

Apply with  $a_u=u^\top X u$ ,  $b_u=u^\top Y u$ . Get

$$
\lambda_{\max}(\theta X+(1-\theta)Y) \le \theta \max_{\|u\|=1} u^\top X u + (1-\theta)\max_{\|u\|=1} u^\top Y u = \theta\lambda_{\max}(X)+(1-\theta)\lambda_{\max}(Y).
$$

So convexity is proved **directly**, essentially by “max preserves Jensen in the right direction.”

This is the “supremum of linear forms” idea, but written purely as inequalities.

* * *

2.3 Alternative proof #1: SDP / “sup over density matrices”
-----------------------------------------------------------

There is a stronger variational representation:

$$
\lambda_{\max}(X)=\max\{\langle X,W\rangle \ :\ W\succeq 0,\ \mathrm{tr}(W)=1\}.
$$

Here  $\langle X,W\rangle=\mathrm{tr}(XW)$ .

### Why this is true (step-by-step)

**(≤)** Let  $W\succeq 0$ ,  $\mathrm{tr}(W)=1$ . Diagonalize  $X=Q\Lambda Q^\top$  and write

$$
\mathrm{tr}(XW)=\mathrm{tr}(Q\Lambda Q^\top W)=\mathrm{tr}(\Lambda\underbrace{Q^\top W Q}_{\tilde W}).
$$

Now  $\tilde W\succeq 0$  and  $\mathrm{tr}(\tilde W)=\mathrm{tr}(W)=1$ .  
So

$$
\mathrm{tr}(\Lambda \tilde W)=\sum_i \lambda_i \tilde W_{ii}.
$$

For PSD  $\tilde W$ , diagonal entries satisfy  $\tilde W_{ii}\ge 0$  and  $\sum_i \tilde W_{ii}=\mathrm{tr}(\tilde W)=1$ . Thus it’s again a convex combination of eigenvalues:

$$
\sum_i \lambda_i \tilde W_{ii}\le \lambda_{\max}.
$$

So  $\mathrm{tr}(XW)\le \lambda_{\max}(X)$  for all feasible  $W$ .

**(≥)** Choose  $W=vv^\top$  where  $v$  is a unit top eigenvector. Then  $W\succeq 0$ ,  $\mathrm{tr}(W)=v^\top v=1$ , and

$$
\mathrm{tr}(XW)=\mathrm{tr}(Xvv^\top)=v^\top X v=\lambda_{\max}(X).
$$

So the max is at least  $\lambda_{\max}(X)$ .

Hence equality.

### Convexity from this representation

It’s now literally a maximum of linear functions  $X\mapsto \mathrm{tr}(XW)$  over a fixed convex set of  $W$ ’s, so convex.

**Bonus:** this representation also makes subgradients very transparent: active maximizers  $W$  are subgradients.

* * *

2.4 Alternative proof #2: epigraph as a spectrahedron
-----------------------------------------------------

Another characterization:

$$
\lambda_{\max}(X)\le t \quad\Longleftrightarrow\quad tI - X \succeq 0.
$$

So

$$
\mathrm{epi}(\lambda_{\max}) =\{(X,t): tI-X\succeq 0\}.
$$

The set  $\{M: M\succeq 0\}$  is convex, and  $(X,t)\mapsto tI-X$  is affine, so the preimage is convex. Therefore the epigraph is convex, hence  $\lambda_{\max}$  is convex.

This is a very “convex geometry / SDP” flavored proof.

* * *

3) Example 3.11 — Matrix/operator norms are convex (more granular + alt proofs)
===============================================================================

We’ll do two things:

1.  prove the “sup of bilinear forms” representation carefully (using dual norms),
2.  give a completely different proof: **it’s a norm in  $X$ ** ⇒ convex.

* * *

3.1 Spectral norm  $\|X\|_2$ : prove  $\|X\|_2=\sup_{\|u\|=\|v\|=1}u^\top Xv$ 
------------------------------------------------------------------------------

### Step 0: definition

$$
\|X\|_2 = \sup_{\|v\|_2=1} \|Xv\|_2.
$$

### Step 1: dualize the vector norm  $\|Xv\|_2$ 

For fixed  $v$ , use the Euclidean dual identity:

$$
\|Xv\|_2 = \sup_{\|u\|_2\le 1} u^\top (Xv).
$$

**Proof of this identity (fully explicit):**

*   By Cauchy–Schwarz, for any  $\|u\|_2\le 1$ ,
    $$
    u^\top (Xv)\le \|u\|_2\|Xv\|_2\le \|Xv\|_2.
    $$
    So the supremum is ≤  $\|Xv\|_2$ .
*   If  $Xv\neq 0$ , choose  $u^\star = (Xv)/\|Xv\|_2$ , which has unit norm, and then
    $$
    (u^\star)^\top (Xv) = \frac{(Xv)^\top (Xv)}{\|Xv\|_2}=\|Xv\|_2.
    $$
    So supremum is ≥  $\|Xv\|_2$ .
*   If  $Xv=0$ , both sides are 0.

So equality holds.

### Step 2: plug back and collapse suprema

$$
\|X\|_2 = \sup_{\|v\|_2=1}\ \sup_{\|u\|_2=1}\ u^\top Xv = \sup_{\|u\|_2=1,\ \|v\|_2=1} u^\top Xv.
$$

### Step 3: convexity from supremum of linear functions

For fixed  $u,v$ ,

$$
u^\top Xv = \sum_{i,j} u_i X_{ij} v_j = \langle X, uv^\top\rangle,
$$

linear in  $X$ . Supremum of linear ⇒ convex.

* * *

3.2 General induced norm  $\|X\|_{a,b}$ : prove the bilinear sup form
---------------------------------------------------------------------

### Step 0: definition

$$
\|X\|_{a,b} = \sup_{v\neq 0}\frac{\|Xv\|_a}{\|v\|_b}.
$$

### Step 1: normalize  $v$  using homogeneity

Let  $v\neq 0$ . Set  $\tilde v = v/\|v\|_b$ . Then  $\|\tilde v\|_b=1$  and

$$
\frac{\|Xv\|_a}{\|v\|_b}=\|X\tilde v\|_a.
$$

Thus

$$
\|X\|_{a,b} = \sup_{\|v\|_b=1}\|Xv\|_a.
$$

### Step 2: dualize  $\|Xv\|_a$  using the dual norm theorem

By the dual norm identity proved earlier,

$$
\|Xv\|_a = \sup_{\|u\|_{a^\*}=1} u^\top (Xv).
$$

So

$$
\|X\|_{a,b} = \sup_{\|v\|_b=1}\ \sup_{\|u\|_{a^\*}=1} u^\top Xv = \sup_{\|u\|_{a^\*}=1,\ \|v\|_b=1} u^\top Xv.
$$

### Step 3: convexity

Again  $X\mapsto u^\top Xv$  is linear, so supremum ⇒ convex.

* * *

3.3 Alternative proof:  $\|X\|_{a,b}$  is a norm in  $X$  ⇒ convex
------------------------------------------------------------------

This is genuinely a different path: you don’t need “sup of linear” at all.

### Step 1: show  $\|\cdot\|_{a,b}$  is a norm on matrices

We must verify the three norm axioms for  $X\mapsto \|X\|_{a,b}$ :

**(i) Nonnegativity and definiteness.**  
 $\|X\|_{a,b}\ge 0$  because it is a supremum of nonnegative quantities  $\|Xv\|_a/\|v\|_b$ .

If  $\|X\|_{a,b}=0$ , then  $\|Xv\|_a=0$  for all  $v$ , hence  $Xv=0$  for all  $v$ , so  $X=0$ .

**(ii) Positive homogeneity.**  
For scalar  $\alpha$ ,

$$
\|\alpha X\|_{a,b} =\sup_{v\neq 0}\frac{\|\alpha Xv\|_a}{\|v\|_b} =\sup_{v\neq 0}\frac{|\alpha|\|Xv\|_a}{\|v\|_b} =|\alpha|\|X\|_{a,b}.
$$

**(iii) Triangle inequality.**  
For  $X,Y$ ,

$$
\|(X+Y)v\|_a \le \|Xv\|_a+\|Yv\|_a
$$

(by triangle inequality of  $\|\cdot\|_a$ ). Divide by  $\|v\|_b$ :

$$
\frac{\|(X+Y)v\|_a}{\|v\|_b}\le \frac{\|Xv\|_a}{\|v\|_b}+\frac{\|Yv\|_a}{\|v\|_b}.
$$

Take supremum over  $v\neq 0$ :

$$
\|X+Y\|_{a,b}\le \|X\|_{a,b}+\|Y\|_{a,b}.
$$

So it’s a norm.

### Step 2: any norm is convex (prove directly)

Take a norm  $\|\cdot\|$ . Then for  $\theta\in[0,1]$ ,

$$
\|\theta x+(1-\theta)y\| \le \|\theta x\|+\|(1-\theta)y\| = \theta\|x\|+(1-\theta)\|y\|.
$$

That uses only triangle inequality + homogeneity. Hence norms are convex.

Therefore  $\|X\|_{a,b}$  is convex.

**This proof is often the cleanest conceptual one**: “operator norm is a norm on matrices; norms are convex.”

* * *

4) Example 3.14 — Composition examples (more granular + alternative proofs)
===========================================================================

The “machine” is the composition theorem (proved in §1.7). Now we must verify for each bullet:

*    $h$  is convex/concave,
*    $h$  is monotone,
*   (sometimes) domain/extension issues.

I’ll go deeper on the ones where the book tends to handwave.

* * *

4.1 (i) Sum of the  $r$  largest components: two equivalent convex representations
----------------------------------------------------------------------------------

Define  $h(z)=\sum_{j=1}^r z_{[j]}$ .

### Representation A (subset max; you already used)

$$
h(z)=\max_{S\subseteq\{1,\dots,k\},\ |S|=r}\ \sum_{i\in S} z_i.
$$

Convex because max of linear.

### Representation B (LP over weights  $w$ )

A very useful alternative:

$$
h(z) = \max\left\{\sum_{i=1}^k w_i z_i \ \Big|\ 0\le w_i\le 1,\ \sum_{i=1}^k w_i = r\right\}.
$$

#### Why Representation B is true (step-by-step)

*   The feasible set for  $w$  is a polytope: all vectors in  $[0,1]^k$  with sum  $r$ .
*   The objective is linear in  $w$ , so the maximum is attained at an extreme point of the polytope.
*   Extreme points here are exactly vectors with  $r$  ones and  $k-r$  zeros (one can prove: if a feasible  $w$  has two fractional components, you can move mass between them and stay feasible, so it’s not extreme).
*   Therefore the optimum equals the maximum over “pick  $r$  indices” which is exactly Representation A.

This representation is often better for deriving duals/subgradients and for optimization modeling.

### Monotonicity

If you increase any coordinate  $z_j$ , every feasible weighted sum  $\sum_i w_i z_i$  with  $w_i\ge 0$  increases by  $w_j\Delta\ge 0$ , so the maximum cannot decrease. Hence monotone.

Then composition theorem applies.

* * *

4.2 (ii) Log-sum-exp: two different convexity proofs
----------------------------------------------------

Let

$$
h(z)=\log\left(\sum_{i=1}^k e^{z_i}\right).
$$

### Proof 1 (Hessian PSD; you already had) — I’ll make it more explicit

Define  $S=\sum_j e^{z_j}$ , and  $s_i = e^{z_i}/S$ .

*   Gradient:
    $$
    \frac{\partial h}{\partial z_i} = \frac{1}{S}\frac{\partial S}{\partial z_i}=\frac{e^{z_i}}{S}=s_i.
    $$
*   Hessian entries:
    $$
    \frac{\partial^2 h}{\partial z_i\partial z_\ell} = \frac{\partial s_i}{\partial z_\ell}.
    $$
    Compute:
    $$
    \frac{\partial s_i}{\partial z_\ell} = \frac{\partial}{\partial z_\ell}\left(\frac{e^{z_i}}{S}\right) = \frac{\delta_{i\ell}e^{z_i}S - e^{z_i}e^{z_\ell}}{S^2} = \delta_{i\ell}s_i - s_is_\ell.
    $$

So

$$
\nabla^2 h(z)=\mathrm{diag}(s)-ss^\top.
$$

Now prove PSD by quadratic form:

$$
v^\top(\mathrm{diag}(s)-ss^\top)v = \sum_i s_i v_i^2 - \left(\sum_i s_i v_i\right)^2.
$$

Interpret  $s$  as a probability distribution on  $\{1,\dots,k\}$ . Then this is

$$
\mathbb{E}[v^2] - (\mathbb{E}[v])^2 = \mathrm{Var}(v)\ge 0.
$$

Hence Hessian  $\succeq 0$ , so convex.

Monotonicity:  $\partial h/\partial z_i=s_i>0$ .

### Proof 2 (very “convex analysis”): log-sum-exp is a supremum of affine functions (entropy conjugate)

There is a famous variational identity:

$$
\log\left(\sum_{i=1}^k e^{z_i}\right) = \sup_{p\in\Delta}\left\{\sum_{i=1}^k p_i z_i - \sum_{i=1}^k p_i\log p_i\right\},
$$

where  $\Delta=\{p\ge 0,\ \sum_i p_i=1\}$  is the simplex, and  $-\sum p_i\log p_i$  is Shannon entropy.

#### Why this is true (sketch but honest)

Fix  $z$ . Consider maximizing over  $p\in\Delta$  the function

$$
\Phi(p)=p^\top z - \sum_i p_i\log p_i.
$$

Use Lagrange multipliers with constraint  $\sum p_i=1$ . The optimality condition gives

$$
z_i - (1+\log p_i) = \lambda \quad\Rightarrow\quad p_i \propto e^{z_i}.
$$

So  $p^\star = \text{softmax}(z)$  and plugging back yields  $\log\sum e^{z_i}$ .

Now convexity is immediate: it’s a supremum over  $p$  of affine functions in  $z$  (since  $p^\top z$  is linear and the entropy term doesn’t depend on  $z$ ). Supremum of affine ⇒ convex.

This proof is powerful because it generalizes: many “log partition functions” are convex because they are conjugates of entropies.

* * *

4.3 (iii)  $h(z)=(\sum z_i^p)^{1/p}$  for  $0<p\le 1$ : deeper proof + an alternative route
-------------------------------------------------------------------------------------------

You used the clean lemma:

*   show 1-homogeneous,
*   show log-concave,
*   prove “1-homogeneous + log-concave ⇒ concave.”

That is a great route. I’ll (a) prove the log-concavity step more carefully, and (b) give an alternative proof flavor.

### (a) Log-concavity step, with the exact composition justification

Let  $q(z)=\sum_{i=1}^k z_i^p$  on  $\mathbb{R}_+^k$ . For  $0<p\le 1$ , each  $z_i^p$  is concave on  $\mathbb{R}_+$ , so  $q$  is concave.

Now define  $\psi(t)=\log t$ , concave and increasing on  $\mathbb{R}_{++}$ .  
Claim:  $\psi\circ q$  is concave.

**Proof:** take  $z,w$  and  $\theta\in[0,1]$ .

*   concavity of  $q$ :  $q(\theta z+(1-\theta)w)\ge \theta q(z)+(1-\theta)q(w)$ .
*    $\psi$  increasing:  $\psi(q(\theta z+(1-\theta)w))\ge \psi(\theta q(z)+(1-\theta)q(w))$ .
*    $\psi$  concave:  $\psi(\theta q(z)+(1-\theta)q(w))\ge \theta \psi(q(z))+(1-\theta)\psi(q(w))$ .

Chain them. So  $\log q(z)$  is concave. Multiply by  $1/p>0$ : still concave. Therefore  $\log h(z)$  is concave, i.e.  $h$  log-concave.

Then your lemma gives concavity of  $h$ .

### (b) Alternative proof flavor: “concave gauge / quasi-norm geometry”

For  $0<p<1$ ,  $\|z\|_p=(\sum |z_i|^p)^{1/p}$  is not a norm (triangle inequality fails), but on  $\mathbb{R}_+^k$  it behaves like a **concave gauge**: level sets  $\{z:h(z)\ge c\}$  are convex cones. One can prove concavity by showing the hypograph is convex (dual to epigraph). This tends to be longer than the log-concavity + homogeneity route, but it gives geometric intuition: for  $p<1$ , the “unit ball” is nonconvex, and the function becomes concave on the positive orthant due to “reverse Minkowski” behavior.

Practically: your lemma route is the cleanest rigorous proof.

* * *

4.4 (iv)  $p\ge 1$ : convex  $p$ \-aggregation, more explicit
-------------------------------------------------------------

We want convexity of

$$
x\mapsto \left(\sum_{i=1}^k g_i(x)^p\right)^{1/p}
$$

when  $p\ge 1$  and  $g_i(x)\ge 0$  and convex.

### Why the “positive part” trick works (granular)

Define  $\tilde h(z)=\|z_+\|_p$  where  $(z_+)_i=\max\{z_i,0\}$ .

1.   $z\mapsto z_+$  is convex coordinatewise because each coordinate is  $\max\{z_i,0\}$ , a max of two affine functions.
2.   $w\mapsto \|w\|_p$  is a norm for  $p\ge 1$ , hence convex.
3.  Also  $\|w\|_p$  is **nondecreasing** on  $\mathbb{R}_+^k$ : if  $0\le w\le w'$  componentwise, then  $w_i^p\le (w'_i)^p$ , sum preserves inequality, and  $t\mapsto t^{1/p}$  is increasing.

Now, to apply the monotone composition theorem, you need the outer function to be convex and nondecreasing, and the inner components convex. The map  $z\mapsto z_+$  is convex, and  $\|\,\cdot\,\|_p$  is convex and nondecreasing on  $\mathbb{R}_+^k$ , so  $\tilde h$  is convex and nondecreasing.

Finally if  $g(x)\ge 0$ , then  $g(x)_+=g(x)$  and

$$
\tilde h(g(x))=\left(\sum_i g_i(x)^p\right)^{1/p}.
$$

So convex by composition.

### Alternative proof (when you’re allowed to use norm convexity)

You can also show directly that  $z\mapsto(\sum z_i^p)^{1/p}$  is a norm on  $\mathbb{R}^k$  (for  $p\ge 1$ ), hence convex; then you only need to argue the composition with  $g(x)\ge 0$  and convex works via monotonicity (same as above). But the positive-part trick is what makes it globally well-defined/monotone in the extended-value setting.

* * *

4.5 (v) Geometric mean concave: second proof via AM–GM (alternative to log trick)
---------------------------------------------------------------------------------

You used:

$$
\log h(z)=\frac1k\sum_i \log z_i
$$

and then “1-homogeneous + log-concave ⇒ concave.” Great.

### Alternative proof: Weighted AM–GM gives concavity directly

For  $z,w\in\mathbb{R}_+^k$  and  $\theta\in[0,1]$ , consider componentwise:

$$
\theta z_i + (1-\theta)w_i \ \ge\ z_i^\theta w_i^{1-\theta}
$$

(this is the weighted AM–GM inequality for scalars).

Multiply over  $i=1,\dots,k$ :

$$
\prod_{i=1}^k (\theta z_i+(1-\theta)w_i) \ \ge\ \prod_{i=1}^k z_i^\theta w_i^{1-\theta} = \left(\prod_i z_i\right)^\theta \left(\prod_i w_i\right)^{1-\theta}.
$$

Now take  $k$ \-th roots:

$$
h(\theta z+(1-\theta)w) \ \ge\ h(z)^\theta h(w)^{1-\theta}.
$$

So  $h$  is log-concave. Then apply 1-homogeneous + log-concave ⇒ concave, or (if you want) apply the inequality  $a^\theta b^{1-\theta}\le \theta a+(1-\theta)b$  to convert to concavity.

This proof is “classical inequality” flavored and very satisfying.

* * *

5) Example 3.17 — Minimization over  $Ay=x$  preserves convexity (more granular + alternative proof via duality)
================================================================================================================

We’re given convex  $h:\mathbb{R}^m\to\mathbb{R}\cup\{+\infty\}$  and define

$$
g(x) := \inf\{h(y): Ay=x\}.
$$

If no  $y$  satisfies  $Ay=x$ , then the infimum over empty set is  $+\infty$ .

* * *

5.1 Prove  $f(x,y)=h(y)+I_{\{Ay=x\}}(x,y)$  is convex (fully explicit)
----------------------------------------------------------------------

Define the set

$$
C:=\{(x,y): Ay=x\}.
$$

### Step 1:  $C$  is convex

Take  $(x_1,y_1),(x_2,y_2)\in C$ . That means  $Ay_1=x_1$  and  $Ay_2=x_2$ .  
Then for  $\theta\in[0,1]$ ,

$$
A(\theta y_1+(1-\theta)y_2)=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2.
$$

So  $(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2)\in C$ . Hence  $C$  convex.

### Step 2: indicator  $I_C$  is convex

This is Lemma 1.4. (We proved it by case analysis using Jensen.)

### Step 3:  $h(y)$  is convex in  $(x,y)$ 

Because for any  $(x_1,y_1),(x_2,y_2)$ ,

$$
h(\theta y_1+(1-\theta)y_2)\le \theta h(y_1)+(1-\theta)h(y_2)
$$

and  $x$  doesn’t appear at all, so it’s convex as a function on the product space.

### Step 4: sum preserves convexity

Define

$$
f(x,y)=h(y)+I_C(x,y).
$$

Sum of convex functions is convex (check Jensen: inequality adds).

Hence  $f$  is jointly convex.

* * *

5.2 Prove  $g(x)=\inf_y f(x,y)$  is convex: two fully rigorous proofs
---------------------------------------------------------------------

### Proof A (epigraph projection; ultra clean)

We need to show  $\mathrm{epi}(g)$  is convex, where

$$
\mathrm{epi}(g)=\{(x,t): g(x)\le t\}.
$$

Now expand the definition of  $g$ :

$$
g(x)\le t \quad\Longleftrightarrow\quad \exists y\ \text{such that}\ f(x,y)\le t.
$$

So

$$
\mathrm{epi}(g)=\{(x,t): \exists y,\ f(x,y)\le t\}.
$$

But the set

$$
\mathrm{epi}(f)=\{(x,y,t): f(x,y)\le t\}
$$

is convex because  $f$  is convex (standard epigraph characterization). Then  $\mathrm{epi}(g)$  is exactly the projection of  $\mathrm{epi}(f)$  onto  $(x,t)$ :

$$
\mathrm{epi}(g) = \Pi_{x,t}(\mathrm{epi}(f)).
$$

Projection of convex set is convex (Lemma 1.5). Hence  $\mathrm{epi}(g)$  is convex, so  $g$  is convex.

### Proof B ( $\varepsilon$ \-minimizers; pure Jensen algebra)

Take any  $x_1,x_2,\theta\in[0,1]$  and  $\varepsilon>0$ . Choose  $y_1,y_2$  satisfying

$$
Ay_1=x_1,\quad Ay_2=x_2, \quad\text{and}\quad h(y_i)\le g(x_i)+\varepsilon.
$$

Define  $y_\theta=\theta y_1+(1-\theta)y_2$ . Then

$$
Ay_\theta = \theta x_1+(1-\theta)x_2=:x_\theta,
$$

so  $y_\theta$  is feasible for  $x_\theta$ .

By convexity of  $h$ :

$$
h(y_\theta)\le \theta h(y_1)+(1-\theta)h(y_2) \le \theta(g(x_1)+\varepsilon)+(1-\theta)(g(x_2)+\varepsilon).
$$

Since  $g(x_\theta)$  is the infimum over feasible  $y$ ,  $g(x_\theta)\le h(y_\theta)$ . Thus:

$$
g(x_\theta)\le \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
$$

Let  $\varepsilon\downarrow 0$ . Done.

* * *

5.3 Alternative proof (very interesting): derive a dual “sup of affine” representation
--------------------------------------------------------------------------------------

This one is _powerful_ because it ties Example 3.17 back to the “supremum trick.”

### Step 0: rewrite constraint with an indicator

$$
g(x)=\inf_y\ \big(h(y)+I_{\{Ay=x\}}(y)\big) =\inf_y\ \big(h(y)+I_{\{0\}}(Ay-x)\big),
$$

where  $I_{\{0\}}(u)=0$  if  $u=0$ , else  $+\infty$ .

### Step 1: represent the indicator of  $\{0\}$  as a supremum of linear forms

Key identity:

$$
I_{\{0\}}(u)=\sup_{\nu\in\mathbb{R}^n}\ \nu^\top u.
$$

**Proof (direct):**

*   If  $u=0$ : RHS  $=\sup_\nu \nu^\top 0 = 0 = I_{\{0\}}(0)$ .
*   If  $u\neq 0$ : choose  $\nu = t u$  with  $t\to+\infty$ . Then  $\nu^\top u = t\|u\|_2^2\to+\infty$ . So RHS  $=+\infty=I_{\{0\}}(u)$ .

So the identity holds.

### Step 2: plug into  $g(x)$ 

$$
g(x)=\inf_y\left(h(y)+\sup_\nu \nu^\top(Ay-x)\right).
$$

This is

$$
g(x)=\inf_y\sup_\nu \left(h(y)+\nu^\top Ay - \nu^\top x\right).
$$

### Step 3: swap inf and sup to get a lower bound (always valid)

In general,  $\inf\sup \ge \sup\inf$ . So:

$$
g(x)\ \ge\ \sup_\nu\ \inf_y \left(h(y)+\nu^\top Ay - \nu^\top x\right).
$$

The term  $-\nu^\top x$  does not involve  $y$ , so:

$$
\inf_y (h(y)+\nu^\top Ay - \nu^\top x) = -\nu^\top x + \inf_y (h(y)+(A^\top \nu)^\top y).
$$

### Step 4: identify the conjugate

Recall the Fenchel conjugate:

$$
h^\*(s) = \sup_y (s^\top y - h(y)).
$$

Then

$$
\inf_y \big(h(y) + (A^\top\nu)^\top y\big) = - \sup_y \big(-(A^\top\nu)^\top y - h(y)\big) = - h^\*(-A^\top\nu).
$$

So we get

$$
g(x)\ \ge\ \sup_{\nu}\ \big(-\nu^\top x - h^\*(-A^\top\nu)\big).
$$

Equivalently (rename  $\mu=-\nu$ ):

$$
g(x)\ \ge\ \sup_{\mu}\ \big(\mu^\top x - h^\*(A^\top\mu)\big).
$$

### Step 5: what does this buy us?

Even as a **lower bound**, the RHS is a supremum of affine functions in  $x$  (for each  $\mu$ ,  $\mu^\top x - h^\*(A^\top\mu)$  is affine in  $x$ ). A supremum of affine functions is convex. Therefore the lower bound is convex.

Under mild regularity (essentially feasibility + closedness conditions), you actually get equality (strong duality for this value function), and then you obtain:

$$
g(x)=\sup_{\mu}\ \big(\mu^\top x - h^\*(A^\top\mu)\big),
$$

which makes convexity immediate.

**Why this alternative is interesting:** it shows  $g$  is convex because it is (often) a **support-function-like supremum**, i.e. it is literally built as a supremum of affine minorants. This connects Example 3.17 to Fenchel duality.

* * *

What you should take away (the unifying “DNA”)
==============================================

All four examples reduce to two meta-mechanisms:

1.  **Supremum mechanism:** If you can express something as
    $$
    f(\cdot)=\sup_{\alpha}\{\text{affine in }(\cdot)\},
    $$
    then  $f$  is convex.  
    This drives:  $\lambda_{\max}$ , operator norms, max/“top-r sum”, log-sum-exp (via entropy dual).
2.  **Projection/minimization mechanism:** If you start with a jointly convex set/function and eliminate variables (projection / partial infimum), convexity survives.  
    This drives:  $g(x)=\inf\{h(y):Ay=x\}$ .

These are essentially the two ways convexity “propagates through constructions.”

* * *

If you want an even more “from bedrock” layer next, the natural targets are:

*   **Prove the supporting hyperplane theorem** (the only nontrivial geometric ingredient used in the dual norm identity).
*   **Derive subgradients** for each variational form (λmax, operator norm, log-sum-exp, top-r sum, and the value function  $g$ ), and explain how “active maximizers = subgradients” follows from the supremum representation.

## Prompt:
Breakdown, unpack, explain even more. Push further to make everything crystal clear, and suitable for self-study from zero. Breakdown the densities. Expand Explanations and make everything abolutely crystal clear!

## Response:
Thought for 23s

Got it. I’m going to push this to “someone could learn it from scratch” level: I’ll slow down, define every object, show the logic chain **one inequality at a time**, and when I say something like “this is PSD” I’ll prove it by testing a quadratic form.

You also said **“breakdown the densities”**. In these examples there are two places “density-like” objects naturally appear:

1.  **Log-sum-exp:** the softmax weights  $s_i=\frac{e^{z_i}}{\sum_j e^{z_j}}$  form a **probability mass function** (a discrete “density”). The Hessian becomes a **covariance matrix**, so PSD becomes “variance is nonnegative.”
2.  ** $\lambda_{\max}$ :** the SDP form uses  $W\succeq 0$ ,  $\mathrm{tr}(W)=1$ , which is literally called a **density matrix** in quantum mechanics. It’s a “matrix-valued density.”

I’ll unpack both fully.

* * *

Part 0 — Absolute bedrock: what “convex” means and the two magic closure tricks
===============================================================================

0.1 Convexity (definition, no shortcuts)
----------------------------------------

A function  $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  is **convex** if for any two points  $x_1,x_2$  and any mixing weight  $\theta\in[0,1]$ ,

$$
f(\theta x_1+(1-\theta)x_2)\ \le\ \theta f(x_1)+(1-\theta)f(x_2).
$$

Interpretation: “value at the mixture is at most the mixture of the values.” Graphically: the line segment between  $(x_1,f(x_1))$  and  $(x_2,f(x_2))$  lies **above** the graph.

0.2 Inner products and linearity in matrices (so you know what “linear in  $X$ ” means)
---------------------------------------------------------------------------------------

For matrices  $A,B\in\mathbb{R}^{m\times m}$ , define Frobenius inner product

$$
\langle A,B\rangle := \mathrm{tr}(A^\top B)=\sum_{i,j} A_{ij}B_{ij}.
$$

A map  $X\mapsto \langle X, M\rangle$  is **linear in  $X$ ** because:

*    $\langle X_1+X_2,M\rangle = \langle X_1,M\rangle+\langle X_2,M\rangle$ 
*    $\langle \alpha X,M\rangle = \alpha \langle X,M\rangle$ .

This will let us recognize “ $u^\top Xv$ ” and “ $y^\top Xy$ ” as linear functions of  $X$ .

* * *

0.3 Closure Trick #1 (proved): supremum of affine functions is convex
---------------------------------------------------------------------

### Claim

If  $f(x)=\sup_{\alpha}(a_\alpha^\top x + b_\alpha)$ , then  $f$  is convex.

### Proof (painfully explicit)

Fix  $x_1,x_2,\theta$ . For every  $\alpha$ ,

$$
a_\alpha^\top(\theta x_1+(1-\theta)x_2)+b_\alpha = \theta(a_\alpha^\top x_1+b_\alpha)+(1-\theta)(a_\alpha^\top x_2+b_\alpha).
$$

Now take supremum over  $\alpha$  of the left side:

$$
\sup_\alpha[a_\alpha^\top(\theta x_1+(1-\theta)x_2)+b_\alpha] = f(\theta x_1+(1-\theta)x_2).
$$

For the right side, use: for each  $\alpha$ ,

$$
\theta(a_\alpha^\top x_1+b_\alpha)\le \theta\sup_\beta(a_\beta^\top x_1+b_\beta)=\theta f(x_1),
$$

and similarly  $(1-\theta)(a_\alpha^\top x_2+b_\alpha)\le (1-\theta)f(x_2)$ .  
Add them:

$$
\theta(a_\alpha^\top x_1+b_\alpha)+(1-\theta)(a_\alpha^\top x_2+b_\alpha)\le \theta f(x_1)+(1-\theta)f(x_2).
$$

This holds for _every_  $\alpha$ , so it holds for the supremum over  $\alpha$ . Hence

$$
f(\theta x_1+(1-\theta)x_2)\le \theta f(x_1)+(1-\theta)f(x_2).
$$

So  $f$  is convex. □

* * *

0.4 Closure Trick #2 (proved): projection / minimizing out variables preserves convexity
----------------------------------------------------------------------------------------

There are two equivalent “atoms” here:

### Atom A: projection of a convex set is convex

If  $S\subseteq\mathbb{R}^{n+m}$  is convex, then

$$
\Pi_x(S):=\{x:\exists y\ \text{s.t. }(x,y)\in S\}
$$

is convex.

**Proof:** take  $x_1,x_2\in\Pi_x(S)$ . So  $(x_1,y_1)\in S$ ,  $(x_2,y_2)\in S$  for some  $y_1,y_2$ .  
Convexity of  $S$  implies

$$
(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2)\in S,
$$

so  $\theta x_1+(1-\theta)x_2\in\Pi_x(S)$ . □

### Atom B: partial minimization of a jointly convex function is convex

If  $f(x,y)$  is convex in  $(x,y)$ , define

$$
g(x):=\inf_y f(x,y).
$$

Then  $g$  is convex.

**Proof idea:** epigraph of  $g$  is the projection of the epigraph of  $f$ . I’ll do it in Example 3.17 in excruciating detail.

* * *

Example 3.10 —  $\lambda_{\max}(X)$  is convex
==============================================

We’ll do it in layers:

1.  what eigenvalues are (enough to follow),
2.  Rayleigh quotient identity (proved step-by-step),
3.  convexity proof (two ways),
4.  “density matrix” viewpoint (this is one of your “densities”),
5.  subgradient (so you can actually use it).

* * *

1\. What is  $\lambda_{\max}(X)$ ?
----------------------------------

Let  $X\in\mathbf{S}^m$ , meaning:

*    $X$  is real  $m\times m$ ,
*   symmetric:  $X=X^\top$ .

An **eigenvector**  $v\neq 0$  and **eigenvalue**  $\lambda$  satisfy

$$
Xv=\lambda v.
$$

For symmetric  $X$ , you can choose an orthonormal basis of eigenvectors; equivalently:

$$
X = Q\Lambda Q^\top,\quad Q^\top Q=I,\quad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_m)\in\mathbb{R}^{m\times m}.
$$

Define

$$
\lambda_{\max}(X):=\max_i \lambda_i.
$$

> If you don’t want to assume the full spectral theorem, you can treat it as a standard fact about symmetric matrices. The Rayleigh–Ritz identity below can be proved with weaker tools, but the cleanest self-study path uses the diagonalization.

* * *

2\. Rayleigh–Ritz: prove  $\lambda_{\max}(X)=\max_{\|y\|_2=1} y^\top Xy$ 
-------------------------------------------------------------------------

### Step 2.1: start with any unit vector  $y$ 

Pick  $y\in\mathbb{R}^m$  with  $\|y\|_2=1$ .

### Step 2.2: express  $y$  in the eigenbasis

Let  $X=Q\Lambda Q^\top$ . Define  $z:=Q^\top y$ . Because  $Q$  is orthonormal:

$$
\|z\|_2^2 = z^\top z = y^\top QQ^\top y = y^\top y = \|y\|_2^2 = 1.
$$

### Step 2.3: expand the quadratic form

Compute:

$$
\begin{aligned} y^\top Xy &= y^\top(Q\Lambda Q^\top)y\\ &= (Q^\top y)^\top \Lambda (Q^\top y) \quad\text{(move \(Q^\top\) to the left)}\\ &= z^\top \Lambda z\\ &= \sum_{i=1}^m \lambda_i z_i^2. \end{aligned}
$$

### Step 2.4: interpret  $z_i^2$  as weights

Each  $z_i^2\ge 0$  and  $\sum_i z_i^2 = \|z\|_2^2 = 1$ .  
So  $w_i:=z_i^2$  satisfy

$$
w_i\ge 0,\qquad \sum_i w_i=1.
$$

That means  $\sum_i \lambda_i w_i$  is a **convex combination** of the eigenvalues.

### Step 2.5: convex combinations are bounded by the max

Since  $\lambda_i\le \lambda_{\max}$  for all  $i$ ,

$$
\sum_i \lambda_i w_i \le \sum_i \lambda_{\max} w_i = \lambda_{\max}\sum_i w_i = \lambda_{\max}.
$$

So for every unit  $y$ ,

$$
y^\top Xy \le \lambda_{\max}(X).
$$

Taking the supremum over all unit  $y$ ,

$$
\sup_{\|y\|_2=1} y^\top Xy \le \lambda_{\max}(X).
$$

### Step 2.6: show you can hit  $\lambda_{\max}$ 

Let  $v$  be a unit eigenvector for  $\lambda_{\max}$ , so  $Xv=\lambda_{\max}v$  and  $\|v\|_2=1$ .  
Then

$$
v^\top Xv = v^\top(\lambda_{\max}v)=\lambda_{\max}v^\top v=\lambda_{\max}.
$$

So

$$
\sup_{\|y\|_2=1} y^\top Xy \ge \lambda_{\max}(X).
$$

### Conclusion

$$
\lambda_{\max}(X)=\sup_{\|y\|_2=1} y^\top Xy.
$$

* * *

3\. Convexity proof #1 (direct Jensen via Rayleigh–Ritz)
--------------------------------------------------------

We want to prove:

$$
\lambda_{\max}(\theta X+(1-\theta)Y)\ \le\ \theta\lambda_{\max}(X)+(1-\theta)\lambda_{\max}(Y).
$$

Start:

$$
\lambda_{\max}(\theta X+(1-\theta)Y) =\max_{\|u\|_2=1} u^\top(\theta X+(1-\theta)Y)u.
$$

Distribute inside:

$$
u^\top(\theta X+(1-\theta)Y)u=\theta(u^\top Xu)+(1-\theta)(u^\top Yu).
$$

Now take max over  $u$ . Use a basic inequality:

$$
\max_u\big(\theta a_u+(1-\theta)b_u\big) \le \theta \max_u a_u + (1-\theta)\max_u b_u.
$$

(Reason: for every  $u$ ,  $a_u\le \max a$  and  $b_u\le \max b$ ; multiply by weights and add; then maximize left side.)

Apply it:

$$
\lambda_{\max}(\theta X+(1-\theta)Y) \le \theta \max_{\|u\|=1}u^\top Xu + (1-\theta)\max_{\|u\|=1}u^\top Yu = \theta\lambda_{\max}(X)+(1-\theta)\lambda_{\max}(Y).
$$

Convexity proved.

* * *

4\. Convexity proof #2 (the “density matrix” representation — density breakdown)
--------------------------------------------------------------------------------

This is the more grown-up version:

$$
\lambda_{\max}(X) =\max\{\langle X,W\rangle:\ W\succeq 0,\ \mathrm{tr}(W)=1\}.
$$

Here  $W\succeq 0$  means PSD:  $v^\top Wv\ge 0\ \forall v$ .

### Step 4.1: why this set is called “density matrices”

A matrix  $W$  with  $W\succeq 0$ ,  $\mathrm{tr}(W)=1$  behaves like a probability distribution:

*   PSD is like “nonnegative probabilities,”
*   trace  $=1$  is like “total mass = 1.”

Rank-1 choices  $W=yy^\top$  with  $\|y\|=1$  are the “pure states” (extreme points). Mixtures (convex combinations) correspond to “mixed states.”

### Step 4.2: prove the representation (very explicitly)

**(≥)** Choose  $W=vv^\top$ , where  $v$  is unit top eigenvector.

*    $W\succeq 0$  because  $v^\top W v = v^\top (vv^\top)v = (v^\top v)^2\ge 0$ .
*    $\mathrm{tr}(W)=\mathrm{tr}(vv^\top)=v^\top v=1$ .  
    Then
    
$$
\langle X,W\rangle=\mathrm{tr}(Xvv^\top)=v^\top Xv=\lambda_{\max}(X).
$$

So the max is at least  $\lambda_{\max}(X)$ .

**(≤)** Take any feasible  $W\succeq 0$ ,  $\mathrm{tr}(W)=1$ . Diagonalize  $X=Q\Lambda Q^\top$ . Let  $\tilde W:=Q^\top WQ$ . Then:

*    $\tilde W\succeq 0$  (PSD preserved under congruence by orthonormal  $Q$ ),
*    $\mathrm{tr}(\tilde W)=\mathrm{tr}(W)=1$ .  
    Now:
    
$$
\mathrm{tr}(XW)=\mathrm{tr}(Q\Lambda Q^\top W)=\mathrm{tr}(\Lambda Q^\top WQ)=\mathrm{tr}(\Lambda \tilde W).
$$

Because  $\Lambda$  is diagonal,

$$
\mathrm{tr}(\Lambda \tilde W)=\sum_{i=1}^m \lambda_i \tilde W_{ii}.
$$

For PSD  $\tilde W$ , diagonal entries satisfy  $\tilde W_{ii}\ge 0$ , and  $\sum_i \tilde W_{ii}=\mathrm{tr}(\tilde W)=1$ . So  $(\tilde W_{ii})$  is a probability vector — a “density.” Thus it’s a convex combination:

$$
\sum_i \lambda_i \tilde W_{ii}\le \lambda_{\max}\sum_i\tilde W_{ii}=\lambda_{\max}.
$$

So  $\mathrm{tr}(XW)\le \lambda_{\max}(X)$  for all feasible  $W$ . Hence the max is ≤  $\lambda_{\max}(X)$ .

Combine both: equality.

### Step 4.3: convexity becomes trivial

For fixed  $W$ ,  $X\mapsto \langle X,W\rangle$  is linear. Taking a maximum over  $W$  gives convexity by the supremum trick.

* * *

5\. Subgradients (so it’s usable)
---------------------------------

Because

$$
\lambda_{\max}(X)=\sup_{\|y\|=1}\langle X,yy^\top\rangle,
$$

this is a supremum of linear functions. General fact: **subgradients come from active maximizers.**

*   If the top eigenvalue is **simple** with unit eigenvector  $v$ , then
    $$
    \nabla \lambda_{\max}(X) = vv^\top.
    $$
*   If multiplicity  $>1$ , then subdifferential is convex hull of  $vv^\top$  over unit vectors in the top eigenspace:
    $$
    \partial \lambda_{\max}(X)=\mathrm{conv}\{vv^\top:\ v\in\mathcal{E}_{\max},\ \|v\|=1\}.
    $$

This matches the “density matrix” picture: any optimal  $W$  is a density matrix supported on the top eigenspace.

* * *

Example 3.11 — Operator norms are convex (and “densities” appear again)
=======================================================================

We’ll do spectral norm first (cleanest), then general induced norms, then derivatives.

* * *

A. Spectral norm  $\|X\|_2$ 
----------------------------

### A1. Definitions (slow)

For  $X\in\mathbb{R}^{p\times q}$  and vector  $v\in\mathbb{R}^q$ ,

*    $\|v\|_2 = \sqrt{v^\top v}$ ,
*    $Xv\in\mathbb{R}^p$ ,
*   define operator norm:
    
$$
\|X\|_2 := \sup_{\|v\|_2=1}\|Xv\|_2.
$$

Meaning: “largest stretching factor” in Euclidean geometry.

### A2. Key identity:  $\|Xv\|_2 = \sup_{\|u\|_2=1} u^\top (Xv)$ 

This is the Euclidean dual norm identity. Proof is just Cauchy–Schwarz + equality case (you already saw it, but now it’s fully owned).

### A3. Collapse suprema

$$
\|X\|_2 = \sup_{\|v\|_2=1}\ \sup_{\|u\|_2=1} u^\top Xv = \sup_{\|u\|_2=1,\ \|v\|_2=1} u^\top Xv.
$$

### A4. Why  $X\mapsto u^\top Xv$  is linear

Expand:

$$
u^\top Xv = \sum_{i=1}^p\sum_{j=1}^q u_i X_{ij} v_j,
$$

a linear combination of the entries  $X_{ij}$  with fixed coefficients  $u_iv_j$ . So linear in  $X$ .

### A5. Convexity

 $\|X\|_2$  is the supremum of linear functions of  $X$ , hence convex.

* * *

B. General induced norm  $\|X\|_{a,b}$ 
---------------------------------------

### B1. Definition

Given norms  $\|\cdot\|_a$  on  $\mathbb{R}^p$ ,  $\|\cdot\|_b$  on  $\mathbb{R}^q$ ,

$$
\|X\|_{a,b}:=\sup_{v\ne 0}\frac{\|Xv\|_a}{\|v\|_b}.
$$

### B2. Normalize  $v$ 

For any  $v\ne 0$ , let  $\tilde v=v/\|v\|_b$ . Then  $\|\tilde v\|_b=1$  and

$$
\frac{\|Xv\|_a}{\|v\|_b}=\|X\tilde v\|_a.
$$

So

$$
\|X\|_{a,b}=\sup_{\|v\|_b=1}\|Xv\|_a.
$$

### B3. Dualize  $\|Xv\|_a$  using the dual norm theorem

$$
\|Xv\|_a = \sup_{\|u\|_{a^\*}=1} u^\top (Xv).
$$

Therefore

$$
\|X\|_{a,b} = \sup_{\|v\|_b=1}\sup_{\|u\|_{a^\*}=1} u^\top Xv = \sup_{\|u\|_{a^\*}=1,\ \|v\|_b=1} u^\top Xv.
$$

Again: supremum of linear forms ⇒ convex.

* * *

C. “Density breakdown” for norms: where probability-like objects show up
------------------------------------------------------------------------

For spectral norm, if you do SVD  $X=U\Sigma V^\top$ , the maximizing  $u,v$  are the top singular vectors. When the top singular value is unique, the “direction of stretch” is unique.

For other norms, the maximizers may live on the dual unit balls — those are convex compact sets, and optimality often picks extreme points (analogous to “pure densities”).

* * *

D. Subgradients for  $\|X\|_2$  (very useful)
---------------------------------------------

If the top singular value is simple and  $u,v$  are the top left/right singular vectors ( $Xv=\sigma_{\max}u$ ,  $X^\top u=\sigma_{\max}v$ ,  $\|u\|=\|v\|=1$ ), then

$$
\nabla \|X\|_2 = uv^\top.
$$

If multiplicity > 1,

$$
\partial \|X\|_2 = \mathrm{conv}\{u_iv_i^\top:\ (u_i,v_i)\ \text{top singular pairs}\}.
$$

This is the exact analog of the  $\lambda_{\max}$  story.

* * *

Example 3.14 — The composition machine, now _ultra_ explicit + “density” (softmax) breakdown
============================================================================================

You want self-study, so we’ll do:

1.  prove the composition theorem again but with “componentwise” spelled out,
2.  for each bullet, prove convexity/concavity + monotonicity,
3.  for log-sum-exp, do a full derivative/Hessian computation and interpret as a categorical “density.”

* * *

1) Composition theorem, componentwise spelled out
-------------------------------------------------

Assume:

*    $g_i:\mathbb{R}^n\to\mathbb{R}$  are convex,
*    $h:\mathbb{R}^k\to\mathbb{R}$  is convex,
*    $h$  is nondecreasing in each coordinate.

Define  $g(x)=(g_1(x),\dots,g_k(x))$ ,  $f(x)=h(g(x))$ .

### Step 1: convexity of each  $g_i$ 

For each  $i$ ,

$$
g_i(\theta x_1+(1-\theta)x_2)\le \theta g_i(x_1)+(1-\theta)g_i(x_2).
$$

### Step 2: stack into a vector inequality

Define vectors:

*   left side vector  $L$  with entries  $L_i=g_i(\theta x_1+(1-\theta)x_2)$ ,
*   right side vector  $R$  with entries  $R_i=\theta g_i(x_1)+(1-\theta)g_i(x_2)$ .  
    Then  $L_i\le R_i$  for all  $i$ . That’s exactly:
    
$$
g(\theta x_1+(1-\theta)x_2)\ \le\ \theta g(x_1)+(1-\theta)g(x_2) \quad\text{(componentwise)}.
$$

### Step 3: monotonicity of  $h$  uses “componentwise ≤”

Since  $h$  is nondecreasing in each coordinate,  $L\le R$  implies  $h(L)\le h(R)$ :

$$
h(g(\theta x_1+(1-\theta)x_2)) \le h(\theta g(x_1)+(1-\theta)g(x_2)).
$$

### Step 4: convexity of  $h$ 

$$
h(\theta g(x_1)+(1-\theta)g(x_2)) \le \theta h(g(x_1))+(1-\theta)h(g(x_2)).
$$

Chain them and you have Jensen for  $f$ . Done.

* * *

2) Bullet (i): sum of the  $r$  largest components
--------------------------------------------------

### Convexity via “max over subsets” (fully explicit)

Define

$$
h(z)=z_{[1]}+\cdots+z_{[r]},
$$

where  $z_{[1]}\ge\cdots\ge z_{[k]}$  are sorted components.

Claim:

$$
h(z)=\max_{|S|=r}\ \sum_{i\in S} z_i.
$$

**Why?**

*   For any set  $S$  of  $r$  indices,  $\sum_{i\in S} z_i$  is the sum of some  $r$  components.
*   The biggest such sum is obtained by choosing the  $r$  largest components. That’s exactly  $z_{[1]}+\cdots+z_{[r]}$ .

Each  $\sum_{i\in S} z_i$  is linear in  $z$ . Max of linear ⇒ convex.

### Monotonicity

Increase one coordinate  $z_j$  by  $\Delta>0$ . Any subset-sum including  $j$  increases by  $\Delta$ , others unchanged. Max cannot decrease. So coordinatewise nondecreasing.

* * *

3) Bullet (ii): log-sum-exp — full “density” breakdown
------------------------------------------------------

Let

$$
h(z)=\log\left(\sum_{i=1}^k e^{z_i}\right).
$$

Define

$$
S(z)=\sum_{i=1}^k e^{z_i}.
$$

### 3.1 Monotonicity (derivative computed slowly)

Compute partial derivative:

*   First,  $\frac{\partial S}{\partial z_i} = e^{z_i}$  (since derivative of  $e^{z_i}$  is  $e^{z_i}$ , others are constants).
*   Then  $h(z)=\log S(z)$ , so by chain rule:
    
$$
\frac{\partial h}{\partial z_i} = \frac{1}{S(z)}\frac{\partial S}{\partial z_i} = \frac{e^{z_i}}{\sum_j e^{z_j}}.
$$

Define the **softmax weights**

$$
s_i(z):=\frac{e^{z_i}}{\sum_j e^{z_j}}.
$$

Then  $\partial h/\partial z_i = s_i(z)$ .

Now note:

*    $s_i(z)>0$  for all  $i$ ,
*    $\sum_i s_i(z)=1$ .

So  $\{s_i\}$  is literally a **probability mass function** on  $\{1,\dots,k\}$ . That’s your “density.”  
Monotonicity is immediate because each partial derivative is positive: increasing  $z_i$  increases  $h$ .

### 3.2 Convexity via Hessian = covariance (super clear)

We compute second derivatives. Start with

$$
s_i=\frac{e^{z_i}}{S},\quad S=\sum_j e^{z_j}.
$$

Differentiate  $s_i$  w.r.t.  $z_\ell$ :

**Case 1:  $\ell=i$ .**

$$
\frac{\partial s_i}{\partial z_i} = \frac{e^{z_i}S - e^{z_i}\cdot e^{z_i}}{S^2} = \frac{e^{z_i}}{S}\left(1-\frac{e^{z_i}}{S}\right) = s_i(1-s_i).
$$

**Case 2:  $\ell\ne i$ .**  
Only  $S$  changes:

$$
\frac{\partial s_i}{\partial z_\ell} = \frac{0\cdot S - e^{z_i}\cdot e^{z_\ell}}{S^2} = -\frac{e^{z_i}}{S}\frac{e^{z_\ell}}{S} = -s_i s_\ell.
$$

So the Hessian matrix  $H=\nabla^2 h(z)$  has entries:

$$
H_{i\ell}= \begin{cases} s_i(1-s_i),&i=\ell,\\ -s_i s_\ell,&i\ne\ell. \end{cases}
$$

In matrix form:

$$
\nabla^2 h(z)=\mathrm{diag}(s)-ss^\top.
$$

Now: **why is this PSD?** Test a quadratic form with an arbitrary  $v\in\mathbb{R}^k$ :

$$
\begin{aligned} v^\top(\mathrm{diag}(s)-ss^\top)v &= v^\top \mathrm{diag}(s)v - v^\top ss^\top v\\ &= \sum_i s_i v_i^2 - \left(\sum_i s_i v_i\right)^2. \end{aligned}
$$

Interpret  $I\sim s$  as a categorical random variable with  $\mathbb{P}(I=i)=s_i$ .  
Then:

*    $\mathbb{E}[v_I]=\sum_i s_i v_i$ ,
*    $\mathbb{E}[v_I^2]=\sum_i s_i v_i^2$ .

So the expression is

$$
\mathbb{E}[v_I^2] - (\mathbb{E}[v_I])^2 = \mathrm{Var}(v_I)\ge 0.
$$

Variance is always nonnegative. Therefore Hessian is PSD. Hence  $h$  is convex.

That’s as “crystal clear” as convexity proofs get: **convexity = nonnegative variance**.

### 3.3 Alternative convexity proof (no derivatives): Hölder inequality

This is a gorgeous self-contained one-liner once you see it.

We want:

$$
h(\theta z+(1-\theta)w)\le \theta h(z)+(1-\theta)h(w).
$$

Exponentiate both sides (since exp is increasing):

$$
\sum_i e^{\theta z_i+(1-\theta)w_i} \le \left(\sum_i e^{z_i}\right)^\theta \left(\sum_i e^{w_i}\right)^{1-\theta}.
$$

But

$$
e^{\theta z_i+(1-\theta)w_i} = (e^{z_i})^\theta (e^{w_i})^{1-\theta}.
$$

So inequality becomes:

$$
\sum_i (a_i)^\theta (b_i)^{1-\theta}\le \left(\sum_i a_i\right)^\theta \left(\sum_i b_i\right)^{1-\theta}
$$

with  $a_i=e^{z_i}$ ,  $b_i=e^{w_i}$ , which is exactly Hölder. Then take log. Done.

* * *

4) Bullet (iii):  $h(z)=(\sum z_i^p)^{1/p}$  for  $0<p\le 1$  is concave on  $\mathbb{R}_+^k$ 
----------------------------------------------------------------------------------------------

This one is subtle; the clean route is:

1.  show 1-homogeneous,
2.  show log-concave,
3.  prove lemma: 1-homogeneous + log-concave ⇒ concave.

### 4.1 1-homogeneous (slow)

For  $\alpha\ge 0$ :

$$
h(\alpha z)=\left(\sum_i (\alpha z_i)^p\right)^{1/p} =\left(\alpha^p\sum_i z_i^p\right)^{1/p} =\alpha\left(\sum_i z_i^p\right)^{1/p} =\alpha h(z).
$$

### 4.2 log-concave (slow, with the exact monotone-composition logic)

Assume  $z\succ 0$  (all entries positive) so logs are finite.

$$
\log h(z)=\frac{1}{p}\log\left(\sum_i z_i^p\right).
$$

For  $0<p\le 1$ , scalar map  $t\mapsto t^p$  is concave on  $\mathbb{R}_+$ . So  $z\mapsto \sum_i z_i^p$  is concave (sum of concave).

Then use the “concave increasing outer” rule:

*    $\log(\cdot)$  is concave and increasing on  $\mathbb{R}_{++}$ .
*   If  $q$  is concave and  $\phi$  is concave increasing, then  $\phi\circ q$  is concave (same inequality chain as before, just reversed).

So  $\log(\sum z_i^p)$  is concave. Multiply by  $1/p>0$ : still concave. Therefore  $\log h$  is concave, i.e.  $h$  is log-concave.

### 4.3 Lemma (proved slowly): 1-homogeneous + log-concave ⇒ concave

Assume  $f>0$ , 1-homogeneous, log-concave. Want:

$$
f(\theta x+(1-\theta)y)\ge \theta f(x)+(1-\theta)f(y).
$$

Let  $a=f(x)$ ,  $b=f(y)$ . Define normalized points:

$$
\bar x=\frac{x}{a},\qquad \bar y=\frac{y}{b}.
$$

By 1-homogeneity:

$$
f(\bar x)=f(x/a)=\frac{1}{a}f(x)=1,\quad f(\bar y)=1.
$$

Now write the mixture  $z=\theta x+(1-\theta)y$  as a scaled convex combo of  $\bar x,\bar y$ :

$$
z=\theta a\bar x + (1-\theta)b\bar y.
$$

Let  $s=\theta a+(1-\theta)b$ . Define weights

$$
\alpha=\frac{\theta a}{s},\quad \beta=\frac{(1-\theta)b}{s},\quad \alpha+\beta=1.
$$

Then

$$
z = s(\alpha \bar x+\beta \bar y).
$$

Apply 1-homogeneity:

$$
f(z)=s\,f(\alpha \bar x+\beta \bar y).
$$

Apply log-concavity to  $\alpha\bar x+\beta\bar y$ :

$$
f(\alpha \bar x+\beta \bar y)\ge f(\bar x)^\alpha f(\bar y)^\beta = 1^\alpha 1^\beta=1.
$$

So

$$
f(z)\ge s=\theta a+(1-\theta)b=\theta f(x)+(1-\theta)f(y).
$$

Concavity proved.

Apply to  $h$ . Done.

* * *

5) Bullet (iv):  $p\ge 1$  “ $p$ \-aggregation” is convex (and why the positive-part trick is used)
---------------------------------------------------------------------------------------------------

You want convexity of:

$$
x\mapsto \left(\sum_i g_i(x)^p\right)^{1/p}
$$

when  $p\ge 1$ ,  $g_i$  convex, and  $g_i(x)\ge 0$ .

Define

$$
\tilde h(z)=\left(\sum_i (z_i)_+^p\right)^{1/p},\quad (t)_+=\max(t,0).
$$
*   Each coordinate map  $t\mapsto (t)_+$  is convex (max of two affine functions  $t$  and  $0$ ).
*   The map  $w\mapsto \|w\|_p=(\sum_i |w_i|^p)^{1/p}$  is a norm for  $p\ge 1$  ⇒ convex.
*   On  $\mathbb{R}_+^k$ ,  $\|w\|_p$  is nondecreasing coordinatewise (increasing entries increases the sum).

Thus  $\tilde h(z)=\|z_+\|_p$  is convex and nondecreasing. If  $g_i(x)\ge 0$ , then  $g(x)_+=g(x)$ , so  $\tilde h(g(x))=(\sum g_i(x)^p)^{1/p}$ . Apply composition theorem.

(If you want, I can also give a full proof of Minkowski/Hölder that  $\|\cdot\|_p$  is a norm for  $p\ge 1$ ; it’s a bit long but doable.)

* * *

6) Bullet (v): geometric mean concave — “density-free” and “density-like” proofs
--------------------------------------------------------------------------------

Geometric mean:

$$
h(z)=\left(\prod_{i=1}^k z_i\right)^{1/k}.
$$
*   Log trick:  $\log h(z)=\frac{1}{k}\sum_i \log z_i$  concave ⇒  $h$  log-concave; plus 1-homogeneous ⇒ concave (same lemma).
*   AM–GM trick:  $\theta a+(1-\theta)b\ge a^\theta b^{1-\theta}$  applied coordinatewise, multiply, take roots ⇒ log-concavity ⇒ concavity via the lemma.

* * *

Example 3.17 — Minimization over  $Ay=x$  preserves convexity (fully unpacked)
==============================================================================

We define:

$$
g(x)=\inf\{h(y): Ay=x\}.
$$

1) Why the constraint set is convex (no mystery)
------------------------------------------------

Set

$$
C=\{(x,y): Ay=x\}.
$$

Take two points  $(x_1,y_1)$ ,  $(x_2,y_2)$  in  $C$ . So  $Ay_1=x_1$ ,  $Ay_2=x_2$ .  
Then

$$
A(\theta y_1+(1-\theta)y_2)=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2.
$$

So  $(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2)\in C$ . Convex.

2) Build the joint function  $f(x,y)$ 
--------------------------------------

Define indicator of  $C$ :

$$
I_C(x,y)=\begin{cases}0,&(x,y)\in C\\ +\infty,&\text{else.}\end{cases}
$$

Then define

$$
f(x,y)=h(y)+I_C(x,y).
$$

This means:

*   If  $Ay=x$ ,  $f(x,y)=h(y)$ .
*   Otherwise,  $f(x,y)=+\infty$ .

### Why  $f$  is convex

*    $h(y)$  convex in  $y$ , and doesn’t depend on  $x$  ⇒ convex in  $(x,y)$ .
*    $I_C$  is convex because  $C$  is convex.
*   Sum of convex functions is convex.

3) Why  $g(x)=\inf_y f(x,y)$  is convex (projection proof, fully explicit)
--------------------------------------------------------------------------

Define epigraph:

$$
\mathrm{epi}(g)=\{(x,t): g(x)\le t\}.
$$

Now expand  $g(x)\le t$ :

$$
g(x)=\inf_y f(x,y)\le t \quad\Longleftrightarrow\quad \exists y \text{ such that } f(x,y)\le t.
$$

So

$$
\mathrm{epi}(g)=\{(x,t): \exists y,\ f(x,y)\le t\}.
$$

Define epigraph of  $f$ :

$$
\mathrm{epi}(f)=\{(x,y,t): f(x,y)\le t\}.
$$

Since  $f$  is convex,  $\mathrm{epi}(f)$  is a convex set.

And  $\mathrm{epi}(g)$  is exactly the projection of  $\mathrm{epi}(f)$  onto  $(x,t)$ :

$$
\mathrm{epi}(g)=\Pi_{x,t}(\mathrm{epi}(f)).
$$

Projection of a convex set is convex. Hence  $\mathrm{epi}(g)$  is convex. Hence  $g$  is convex.

4) Alternative proof (epsilon-minimizers) — same result, pure inequalities
--------------------------------------------------------------------------

Pick  $x_1,x_2,\theta$ . For any  $\varepsilon>0$ , pick feasible  $y_1,y_2$  such that:

$$
Ay_i=x_i,\quad h(y_i)\le g(x_i)+\varepsilon.
$$

Let  $y_\theta=\theta y_1+(1-\theta)y_2$ . Then  $Ay_\theta=\theta x_1+(1-\theta)x_2$ . And

$$
h(y_\theta)\le \theta h(y_1)+(1-\theta)h(y_2)\le \theta(g(x_1)+\varepsilon)+(1-\theta)(g(x_2)+\varepsilon).
$$

Since  $g(x_\theta)\le h(y_\theta)$ , conclude

$$
g(x_\theta)\le \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
$$

Let  $\varepsilon\downarrow 0$ . Convexity.

* * *

Where to go next (still “self-study mode”)
==========================================

If you want this to be _complete_ as a learning module, the next “crystal clarity” upgrades are:

1.  **Prove the supporting hyperplane theorem** (used implicitly in the dual norm identity’s ≥ direction).
2.  **Prove Minkowski/Hölder in full detail** to fully justify “ $\ell_p$  is a norm for  $p\ge 1$ .”
3.  **Do subgradients/value-function duals** for Example 3.17: show when
    $$
    g(x)=\sup_\mu\big(\mu^\top x - h^\*(A^\top\mu)\big)
    $$
    holds with equality (constraint qualification / closedness conditions).

If you tell me which of those you want first, I’ll expand it all the way down to the axioms and keep it readable.

2/2

## Prompt:
Let's Focus on 3.10. Breakdown, unpack, explain even more. Push further to make everything crystal clear, and suitable for self-study from zero. Expand Explanations and make everything abolutely crystal clear! EXPLAIN ALL STEPS. BREAKDOWN EVEN THE SIMPLEST PARTS OF THE PROOFS!

## Response:
Thought for 21s

Let’s laser-focus on **Example 3.10** and rebuild it from _bedrock_, with **every single step explained** (including the “obvious” ones). I’ll give you **two full proofs** of the Rayleigh–Ritz formula (so you’re not hostage to any one theorem), then **three different convexity proofs** (supremum-of-linear, direct Jensen, and the SDP/epigraph proof). Along the way I’ll prove the needed mini-lemmas.

* * *

Example 3.10 — The maximum eigenvalue is convex
===============================================

We study the function

$$
f(X)=\lambda_{\max}(X) \quad\text{for }X\in\mathbf S^m,
$$

where  $\mathbf S^m$  is the set of real  $m\times m$  **symmetric** matrices ( $X=X^\top$ ).

Roadmap
-------

1.  Define eigenvalues/eigenvectors and  $\lambda_{\max}$ .
2.  Prove the **Rayleigh–Ritz variational formula**
    $$
    \lambda_{\max}(X)=\max_{\|y\|_2=1} y^\top Xy.
    $$
    I’ll do this in two ways:
    *   **Proof A:** via the spectral theorem (and I’ll also prove the spectral theorem constructively for symmetric matrices).
    *   **Proof B:** via “maximize on the sphere + first-order optimality ⇒ eigenvector” (Lagrange-multiplier style, fully explained).
3.  Prove **convexity** of  $\lambda_{\max}$  in three ways:
    *   **(1)** supremum of linear functions,
    *   **(2)** direct Jensen inequality using the max formula,
    *   **(3)** epigraph / PSD constraint representation  $\lambda_{\max}(X)\le t \iff tI-X\succeq 0$ .

* * *

0) Absolute basics: what all symbols mean
=========================================

0.1 Inner product and norm
--------------------------

For vectors  $y\in\mathbb R^m$ ,

*   Euclidean norm:  $\|y\|_2=\sqrt{y^\top y}$ .
*   Unit vector means  $\|y\|_2=1$ .

0.2 Quadratic form  $y^\top Xy$ 
--------------------------------

Given a matrix  $X$  and vector  $y$ , the number  $y^\top Xy$  is a scalar.

If  $X=(X_{ij})$  and  $y=(y_i)$ , then

$$
y^\top Xy=\sum_{i=1}^m\sum_{j=1}^m y_i\,X_{ij}\,y_j.
$$

That’s literally: multiply  $Xy$  first (a vector), then dot with  $y$ .

When  $X$  is symmetric,  $y^\top Xy$  behaves nicely (real-valued, “directional curvature”).

0.3 Eigenvalues and eigenvectors
--------------------------------

A scalar  $\lambda$  is an **eigenvalue** of  $X$  if there exists a nonzero vector  $v\neq 0$  such that

$$
Xv=\lambda v.
$$

That vector  $v$  is an **eigenvector** for  $\lambda$ .

We define

$$
\lambda_{\max}(X) = \max\{\lambda:\lambda\text{ is an eigenvalue of }X\}.
$$

* * *

1) Rayleigh quotient and the key target identity
================================================

Define the **Rayleigh quotient**:

$$
R_X(y)=\frac{y^\top Xy}{y^\top y}\quad (y\neq 0).
$$

Why define it? Because:

*   If you scale  $y$  by a nonzero scalar  $\alpha$ , then
    $$
    R_X(\alpha y)=\frac{(\alpha y)^\top X(\alpha y)}{(\alpha y)^\top (\alpha y)} =\frac{\alpha^2 y^\top Xy}{\alpha^2 y^\top y} =R_X(y).
    $$
    So it depends only on the _direction_ of  $y$ , not its length.
*   On the unit sphere  $\{y:\|y\|_2=1\}$ , the Rayleigh quotient is simply
    $$
    R_X(y)=y^\top Xy \quad\text{when }\|y\|_2=1.
    $$

**Goal:** prove

$$
\boxed{\lambda_{\max}(X)=\max_{\|y\|_2=1} y^\top Xy.}
$$

This is the Rayleigh–Ritz formula.

* * *

2) Proof B first (no spectral theorem needed): maximize on the sphere ⇒ eigenvector
===================================================================================

This is the most “from zero” proof, because it uses only:

*   compactness of the unit sphere (so maxima exist),
*   basic calculus / first-order optimality on constrained problems.

2.1 Step 1: the maximum exists (no handwaving)
----------------------------------------------

Consider the unit sphere:

$$
S=\{y\in\mathbb R^m:\|y\|_2=1\}.
$$

Facts:

*    $S$  is **closed** (contains its limit points).
*    $S$  is **bounded** ( $\|y\|_2=1$  for all  $y\in S$ ).

In  $\mathbb R^m$ , “closed + bounded” implies **compact** (Heine–Borel theorem).

Now the function  $g(y)=y^\top Xy$  is continuous in  $y$  (it’s a polynomial in components of  $y$ ). A continuous function on a compact set attains its maximum.

So there exists  $y^\star\in S$  such that

$$
y^\star\in\arg\max_{\|y\|_2=1} y^\top Xy.
$$

This already matters: the “max” is not just a “sup”; it is actually achieved.

2.2 Step 2: write the constrained optimization problem
------------------------------------------------------

We are maximizing:

$$
\max_{y\in\mathbb R^m}\ y^\top Xy \quad\text{subject to}\quad y^\top y = 1.
$$

The constraint  $y^\top y=1$  is exactly  $\|y\|_2=1$ .

2.3 Step 3: compute gradients carefully
---------------------------------------

### Gradient of  $y^\top y$ 

Let  $c(y)=y^\top y=\sum_i y_i^2$ .  
Then

$$
\nabla c(y)=2y.
$$

(Each partial derivative  $\partial/\partial y_i$  gives  $2y_i$ .)

### Gradient of  $y^\top Xy$  when  $X$  is symmetric

Let  $f(y)=y^\top Xy$ .

Expand:

$$
f(y)=\sum_{i,j} y_i X_{ij} y_j.
$$

Differentiate with respect to  $y_k$ . Only terms with  $i=k$  or  $j=k$  matter:

$$
\frac{\partial f}{\partial y_k} = \sum_j X_{kj}y_j + \sum_i y_i X_{ik}.
$$

In vector form:

$$
\nabla f(y) = Xy + X^\top y.
$$

If  $X$  is symmetric,  $X^\top=X$ , so

$$
\nabla f(y)=2Xy.
$$

This “2” is not cosmetic; it matters in the Lagrange condition.

2.4 Step 4: Lagrange multiplier condition (explained, not magic)
----------------------------------------------------------------

At an optimum  $y^\star$  on the constraint surface  $y^\top y=1$ , the gradient of the objective must be parallel to the gradient of the constraint (intuitively: you can’t increase the objective by moving along the tangent directions).

Formally, there exists a scalar  $\mu$  such that

$$
\nabla f(y^\star)=\mu \nabla c(y^\star).
$$

Plug the gradients:

$$
2Xy^\star = \mu (2y^\star).
$$

Cancel the factor  $2$ :

$$
Xy^\star = \mu y^\star.
$$

That is _exactly_ the eigenvector equation. So:

$$
\boxed{\text{Any maximizer }y^\star\text{ is an eigenvector of }X.}
$$

And the corresponding scalar  $\mu$  is the eigenvalue.

2.5 Step 5: the maximum value equals that eigenvalue
----------------------------------------------------

We have  $Xy^\star=\mu y^\star$ . Multiply on the left by  $(y^\star)^\top$ :

$$
(y^\star)^\top Xy^\star = (y^\star)^\top(\mu y^\star)=\mu (y^\star)^\top y^\star.
$$

But  $(y^\star)^\top y^\star=\|y^\star\|_2^2=1$ . So:

$$
(y^\star)^\top Xy^\star = \mu.
$$

Meaning: the _value_ of the objective at the maximizer equals the eigenvalue.

So the maximum of  $y^\top Xy$  over  $\|y\|=1$  is **some** eigenvalue of  $X$ .

2.6 Step 6: it must be the _largest_ eigenvalue
-----------------------------------------------

Let  $\lambda$  be any eigenvalue with unit eigenvector  $v$ . Then  $v^\top Xv=\lambda$ . Since  $y^\top Xy$  achieves its maximum at  $y^\star$ ,

$$
v^\top Xv \le (y^\star)^\top Xy^\star.
$$

So every eigenvalue  $\lambda\le (y^\star)^\top Xy^\star$ . Hence the maximum value is at least the largest eigenvalue, but also (since it equals an eigenvalue) it can’t exceed the largest.

Conclusion:

$$
\boxed{\max_{\|y\|_2=1} y^\top Xy = \lambda_{\max}(X).}
$$

That completes Rayleigh–Ritz **without** needing the full spectral theorem.

* * *

3) Proof A (with spectral theorem): expand in eigenbasis and bound by convex combination
========================================================================================

Now I’ll also do the classic eigenbasis proof, _and_ I’ll prove the spectral theorem in a constructive way (not the full linear algebra textbook route, but enough to be self-contained).

3.1 Constructive spectral theorem for symmetric matrices (core ideas)
---------------------------------------------------------------------

### Step 1: existence of at least one eigenpair

The optimization proof above already produced an eigenvector  $y^\star$  and eigenvalue  $\mu$  (the max Rayleigh quotient). So symmetric  $X$  has at least one real eigenvalue and eigenvector.

Let  $v_1=y^\star$  and  $\lambda_1=\mu=\lambda_{\max}(X)$ , with  $\|v_1\|_2=1$ .

### Step 2: orthogonality of eigenvectors for distinct eigenvalues (prove it)

Suppose  $Xv=\lambda v$  and  $Xw=\mu w$ , with  $\lambda\neq \mu$ , and  $X=X^\top$ .

Compute  $v^\top Xw$  two ways:

1.  Using  $Xw=\mu w$ :
    
$$
v^\top Xw = v^\top(\mu w)=\mu v^\top w.
$$
2.  Using symmetry to move  $X$  to the other side:
    
$$
v^\top Xw = (X^\top v)^\top w = (Xv)^\top w = (\lambda v)^\top w=\lambda v^\top w.
$$

So  $\mu v^\top w = \lambda v^\top w$ . Subtract:

$$
(\mu-\lambda) v^\top w = 0.
$$

Since  $\mu\neq\lambda$ , we must have

$$
v^\top w = 0.
$$

So eigenvectors from distinct eigenvalues are orthogonal.

### Step 3: reduce dimension by restricting to orthogonal complement

Let  $V_1=\mathrm{span}\{v_1\}$ . Consider the orthogonal complement:

$$
V_1^\perp = \{y: v_1^\top y = 0\}.
$$

Claim:  $V_1^\perp$  is invariant under  $X$ : if  $y\in V_1^\perp$ , then  $Xy\in V_1^\perp$ .

**Proof:**  
Take  $y$  with  $v_1^\top y=0$ . Compute  $v_1^\top (Xy)$ :

$$
v_1^\top Xy = (X^\top v_1)^\top y = (Xv_1)^\top y = (\lambda_1 v_1)^\top y = \lambda_1 v_1^\top y = 0.
$$

So  $Xy$  is still orthogonal to  $v_1$ . Done.

Now  $X$  restricted to  $V_1^\perp$  is again symmetric (in that subspace). Repeat: maximize Rayleigh quotient on the unit sphere inside  $V_1^\perp$  to get  $v_2,\lambda_2$ , etc.

By induction, you build an orthonormal basis of eigenvectors  $v_1,\dots,v_m$  and real eigenvalues  $\lambda_1,\dots,\lambda_m$ .

Put them into an orthonormal matrix  $Q=[v_1\ \cdots\ v_m]$ . Then  $Q^\top Q=I$  and

$$
X = Q\Lambda Q^\top,\quad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_m).
$$

That’s the spectral theorem, constructed.

3.2 Rayleigh–Ritz from eigenbasis (convex combination argument)
---------------------------------------------------------------

Take any unit vector  $y$ . Write it in the eigenbasis:

$$
y = Qz,\quad z=Q^\top y.
$$

Because  $Q$  is orthonormal,  $\|z\|_2=\|y\|_2=1$ .

Now compute:

$$
y^\top Xy = (Qz)^\top(Q\Lambda Q^\top)(Qz)=z^\top\Lambda z = \sum_{i=1}^m \lambda_i z_i^2.
$$

Key micro-step: why is  $\sum \lambda_i z_i^2\le \lambda_{\max}$ ?

*   Each  $z_i^2\ge 0$ .
*    $\sum_i z_i^2 = \|z\|_2^2=1$ .  
    So  $z_i^2$  are weights  $w_i$  with  $w_i\ge 0$  and  $\sum w_i=1$ .  
    A weighted average of numbers can never exceed their maximum:
    
$$
\sum_i \lambda_i w_i \le \lambda_{\max}\sum_i w_i = \lambda_{\max}.
$$

So for every unit  $y$ ,

$$
y^\top Xy \le \lambda_{\max}(X).
$$

Equality happens when  $y$  is a top eigenvector (all weight on the max eigenvalue). Therefore

$$
\max_{\|y\|=1} y^\top Xy = \lambda_{\max}(X).
$$

* * *

4) Convexity of  $\lambda_{\max}$ : three fully explicit proofs
===============================================================

Now that we have

$$
\lambda_{\max}(X) = \max_{\|y\|_2=1} y^\top Xy,
$$

we show  $X\mapsto \lambda_{\max}(X)$  is convex.

* * *

Proof 1: “supremum of linear functions” (with every piece proven)
-----------------------------------------------------------------

### Step 1: show  $X\mapsto y^\top Xy$  is linear for fixed  $y$ 

Fix  $y$ . Consider two matrices  $X, Z$  and scalars  $\alpha,\beta$ . Then:

$$
y^\top(\alpha X+\beta Z)y = \alpha y^\top Xy + \beta y^\top Zy.
$$

This uses distributivity of matrix multiplication and dot products:

*    $(\alpha X+\beta Z)y = \alpha (Xy)+\beta(Zy)$ ,
*   then dot with  $y^\top$  distributes.

So it is linear in  $X$ .

If you want the “entrywise” view:

$$
y^\top Xy=\sum_{i,j} y_i X_{ij} y_j,
$$

a linear combination of the entries  $X_{ij}$  with coefficients  $y_i y_j$ .

### Step 2: prove the lemma “sup of linear ⇒ convex” (again, from Jensen)

Let

$$
f(X)=\sup_{y\in\mathcal Y} \ell_y(X)
$$

where each  $\ell_y$  is linear in  $X$ .  
Take  $X_1,X_2,\theta\in[0,1]$ .  
For every  $y$ ,

$$
\ell_y(\theta X_1+(1-\theta)X_2)=\theta \ell_y(X_1)+(1-\theta)\ell_y(X_2).
$$

Now take supremum over  $y$  on the left:

$$
\sup_y \ell_y(\theta X_1+(1-\theta)X_2) \le \sup_y\big(\theta \ell_y(X_1)+(1-\theta)\ell_y(X_2)\big).
$$

Then use the basic inequality

$$
\sup_y(\theta a_y+(1-\theta)b_y)\le \theta \sup_y a_y+(1-\theta)\sup_y b_y.
$$

So:

$$
f(\theta X_1+(1-\theta)X_2)\le \theta f(X_1)+(1-\theta)f(X_2).
$$

That is convexity.

### Step 3: apply to  $\lambda_{\max}$ 

We have

$$
\lambda_{\max}(X)=\sup_{\|y\|_2=1} y^\top Xy,
$$

a supremum of linear functions of  $X$ . Therefore  $\lambda_{\max}$  is convex.

* * *

Proof 2: direct Jensen inequality (no “supremum theorem” needed)
----------------------------------------------------------------

Take  $X_1,X_2$  symmetric and  $\theta\in[0,1]$ .

Start from Rayleigh–Ritz:

$$
\lambda_{\max}(\theta X_1+(1-\theta)X_2) =\max_{\|y\|=1} y^\top(\theta X_1+(1-\theta)X_2)y.
$$

Expand inside:

$$
y^\top(\theta X_1+(1-\theta)X_2)y =\theta y^\top X_1 y+(1-\theta) y^\top X_2 y.
$$

Now take maximum over  $y$ . Use the elementary fact:

$$
\max_y \big(\theta a_y+(1-\theta)b_y\big) \le \theta \max_y a_y+(1-\theta)\max_y b_y.
$$

Why is that fact true? Because for every  $y$ ,

$$
a_y\le \max_y a_y,\quad b_y\le \max_y b_y,
$$

so

$$
\theta a_y+(1-\theta)b_y \le \theta \max a + (1-\theta)\max b.
$$

Taking max over  $y$  preserves the inequality.

So:

$$
\lambda_{\max}(\theta X_1+(1-\theta)X_2) \le \theta \lambda_{\max}(X_1)+(1-\theta)\lambda_{\max}(X_2).
$$

That is exactly convexity.

* * *

Proof 3: epigraph / PSD constraint representation
-------------------------------------------------

This is the “semidefinite programming geometry” proof.

### Step 1: define PSD order

For symmetric matrices,  $M\succeq 0$  (“positive semidefinite”) means

$$
y^\top My \ge 0 \quad \forall y.
$$

### Step 2: prove the equivalence

Claim:

$$
\lambda_{\max}(X)\le t \quad\Longleftrightarrow\quad tI - X \succeq 0.
$$

**( $\Rightarrow$ )** Assume  $\lambda_{\max}(X)\le t$ . Take any  $y$  with  $\|y\|=1$ . Then by Rayleigh–Ritz,

$$
y^\top Xy \le \lambda_{\max}(X)\le t.
$$

So

$$
y^\top(tI-X)y = t\underbrace{y^\top Iy}_{=y^\top y=\|y\|^2=1} - y^\top Xy \ge t - t = 0.
$$

So for all unit  $y$ ,  $y^\top(tI-X)y\ge 0$ . Scaling  $y$  shows it holds for all  $y\neq 0$  too. Hence  $tI-X\succeq 0$ .

**( $\Leftarrow$ )** Assume  $tI-X\succeq 0$ . Then for all unit  $y$ ,

$$
y^\top(tI-X)y \ge 0 \Rightarrow t - y^\top Xy \ge 0 \Rightarrow y^\top Xy \le t.
$$

Take max over unit  $y$ :

$$
\lambda_{\max}(X)=\max_{\|y\|=1} y^\top Xy \le t.
$$

So equivalence is proved.

### Step 3: convexity from convex epigraph

The epigraph of  $\lambda_{\max}$  is

$$
\mathrm{epi}(\lambda_{\max})=\{(X,t): \lambda_{\max}(X)\le t\} =\{(X,t): tI-X\succeq 0\}.
$$

The set  $\{M: M\succeq 0\}$  is convex (because if  $M,N\succeq 0$ , then  $\theta M+(1-\theta)N\succeq 0$  since quadratic forms average nonnegatives). The map  $(X,t)\mapsto tI-X$  is affine. Preimage of a convex set under an affine map is convex. Therefore the epigraph is convex, hence  $\lambda_{\max}$  is convex.

* * *

5) Sanity checks (so you _feel_ the theorem)
============================================

5.1 Diagonal matrix case reduces to “max coordinate”
----------------------------------------------------

Let  $X=\mathrm{diag}(d_1,\dots,d_m)$ . Then for unit  $y$ ,

$$
y^\top Xy = \sum_{i=1}^m d_i y_i^2.
$$

Since  $y_i^2\ge 0$  and  $\sum y_i^2=1$ , this is a weighted average of the  $d_i$ ’s, hence ≤  $\max_i d_i$ . Achieve equality by choosing  $y=e_{i^\star}$  where  $i^\star$  is an index of the maximum  $d_i$ . So:

$$
\lambda_{\max}(X)=\max_i d_i.
$$

That’s obviously convex in  $d$ . So the general result matches the “coordinate max” intuition.

5.2 2×2 concrete formula
------------------------

For

$$
X=\begin{pmatrix}a&b\\b&c\end{pmatrix},
$$
 
$$
\lambda_{\max}(X)=\frac{a+c}{2}+\sqrt{\left(\frac{a-c}{2}\right)^2+b^2},
$$

which is convex because it’s affine + norm of an affine map. This is a nice “explicit convexity witness.”

* * *

6) What to remember (mental model)
==================================

*    $y^\top Xy$  is the “curvature” of  $X$  in direction  $y$ .
*    $\lambda_{\max}(X)$  is the **largest curvature direction**:
    $$
    \lambda_{\max}(X)=\max_{\|y\|=1} y^\top Xy.
    $$
*   Convexity comes from a universal pattern:  
    **“maximum over a family of linear functions” is convex.**

* * *

If you want, next we can go _even more self-study friendly_ by doing:

*   a fully worked 3×3 example where we numerically see the maximizer direction,
*   the geometry of the unit sphere mapping  $y\mapsto y^\top Xy$  (ellipsoids),
*   subgradients: why  $vv^\top$  is the gradient/subgradient at  $X$  when the top eigenvalue is simple.

## Prompt:
This is the approach I want you to take from now on! REMEMBER THAT!

Now go for 3.11.

## Response:
Updated saved memory

Locked in. From now on: **ultra-granular, from-first-principles, every step spelled out, with direct proofs + alternatives.**

Now let’s do **Example 3.11** (matrix/operator norms are convex) in exactly that style.

* * *

Example 3.11 — Matrix norms (spectral norm and induced norms) are convex
========================================================================

We’ll prove the book’s two key variational formulas:

1.  **Spectral norm**
    
$$
\|X\|_2=\sup\{u^\top Xv:\ \|u\|_2=1,\ \|v\|_2=1\}.
$$
2.  **General induced norm**
    
$$
\|X\|_{a,b}=\sup_{v\neq 0}\frac{\|Xv\|_a}{\|v\|_b} =\sup\{u^\top Xv:\ \|u\|_{a^\*}=1,\ \|v\|_b=1\}.
$$

Then we’ll prove convexity in **multiple independent ways** (so you really own it):

*   **Way A:** supremum of linear functions in  $X$ 
*   **Way B:** show  $\|\cdot\|_{a,b}$  is a norm in  $X$  ⇒ convex
*   **Way C (spectral norm):** LMI (semidefinite) epigraph representation

I’ll also unpack “dual norm” properly (since that’s the engine here), and give subgradient intuition.

* * *

0) Bedrock definitions (no skipping)
------------------------------------

### 0.1 Vector norms

A function  $\|\cdot\|:\mathbb{R}^n\to\mathbb{R}$  is a **norm** if:

1.  **Nonnegativity + definiteness:**  $\|x\|\ge 0$ , and  $\|x\|=0\iff x=0$ .
2.  **Homogeneity:**  $\|\alpha x\|=|\alpha|\|x\|$  for all scalars  $\alpha$ .
3.  **Triangle inequality:**  $\|x+y\|\le \|x\|+\|y\|$ .

### 0.2 Induced (operator) norm

Let  $\|\cdot\|_a$  be a norm on  $\mathbb{R}^p$  and  $\|\cdot\|_b$  a norm on  $\mathbb{R}^q$ .  
For a matrix  $X\in\mathbb{R}^{p\times q}$ , define

$$
\|X\|_{a,b}:=\sup_{v\neq 0}\frac{\|Xv\|_a}{\|v\|_b}.
$$

Interpretation: among all nonzero inputs  $v$ , it measures the **largest amplification factor** from  $\|\cdot\|_b$  to  $\|\cdot\|_a$ .

### 0.3 Spectral norm is the special case  $a=b=2$ 

$$
\|X\|_2:=\sup_{\|v\|_2=1}\|Xv\|_2.
$$

* * *

1) First core tool: dual norms (proved carefully)
=================================================

This is the engine that turns “ $\|Xv\|$ ” into a supremum of dot products, which then becomes a supremum of linear forms in  $X$ .

1.1 Definition of dual norm
---------------------------

Given a norm  $\|\cdot\|_a$  on  $\mathbb{R}^p$ , define the **dual norm**

$$
\|u\|_{a^\*}:=\sup_{\|z\|_a\le 1} u^\top z.
$$

This says: look at all vectors  $z$  in the unit ball of  $\|\cdot\|_a$ ; the dual norm is the maximum dot product with  $u$ .

1.2 “Generalized Cauchy–Schwarz”:  $u^\top z\le \|u\|_{a^\*}\|z\|_a$ 
---------------------------------------------------------------------

### Proof (every step)

*   If  $z=0$ , then  $u^\top z=0$ , RHS is  $\|u\|_{a^\*}\cdot 0=0$ . True.
*   If  $z\neq 0$ , define  $\bar z:=z/\|z\|_a$ . Then  $\|\bar z\|_a=1$  by homogeneity.
*   Now:
    $$
    u^\top z = u^\top(\|z\|_a\bar z)=\|z\|_a(u^\top \bar z).
    $$
*   Since  $\|\bar z\|_a=1$ ,  $\bar z$  is feasible in the supremum defining  $\|u\|_{a^\*}$ , so
    $$
    u^\top \bar z \le \sup_{\|w\|_a\le 1} u^\top w = \|u\|_{a^\*}.
    $$
*   Multiply by  $\|z\|_a\ge 0$ :
    $$
    u^\top z \le \|z\|_a\|u\|_{a^\*}.
    $$

Done.

1.3 Dual representation of the primal norm:
-------------------------------------------

 $$
\boxed{\ \|z\|_a=\sup_{\|u\|_{a^\*}\le 1} u^\top z\ }.
$$

### Proof (two inequalities)

#### (≤) direction

If  $\|u\|_{a^\*}\le 1$ , then by the inequality we just proved:

$$
u^\top z \le \|u\|_{a^\*}\|z\|_a \le 1\cdot \|z\|_a=\|z\|_a.
$$

So every feasible  $u$  gives  $u^\top z\le \|z\|_a$ . Taking supremum over feasible  $u$ ,

$$
\sup_{\|u\|_{a^\*}\le 1} u^\top z \le \|z\|_a.
$$

#### (≥) direction (why you can achieve it)

In finite dimensions, the unit ball  $B=\{w:\|w\|_a\le 1\}$  is a **closed convex** set. The point  $\bar z=z/\|z\|_a$  lies on its boundary ( $\|\bar z\|_a=1$ ). A standard separation/supporting-hyperplane fact says there exists some nonzero  $u$  such that

$$
u^\top w \le u^\top \bar z \quad \forall w\in B.
$$

Scale  $u$  so that  $u^\top \bar z=1$ . Then for all  $w\in B$ ,  $u^\top w\le 1$ , which is exactly  $\|u\|_{a^\*}\le 1$  by the definition of the dual norm. With that  $u$ ,

$$
u^\top z = u^\top(\|z\|_a\bar z)=\|z\|_a(u^\top \bar z)=\|z\|_a.
$$

So the supremum is at least  $\|z\|_a$ .

Combine with (≤): equality.

> If you want, I can also prove the supporting-hyperplane step from scratch using separation of convex sets; it’s the only “geometry theorem” hiding here.

* * *

2) Spectral norm: derive  $\|X\|_2=\sup_{\|u\|=\|v\|=1}u^\top Xv$ 
==================================================================

We do this with nothing except Euclidean duality (which is just Cauchy–Schwarz).

2.1 Start from definition
-------------------------

$$
\|X\|_2=\sup_{\|v\|_2=1}\|Xv\|_2.
$$

2.2 Expand  $\|Xv\|_2$  as a supremum of dot products
-----------------------------------------------------

For a fixed vector  $w$ , the Euclidean norm satisfies:

$$
\|w\|_2=\sup_{\|u\|_2=1}u^\top w.
$$

### Proof (fully explicit)

*   For any  $\|u\|_2=1$ , Cauchy–Schwarz gives:
    $$
    u^\top w \le \|u\|_2\|w\|_2 = 1\cdot \|w\|_2.
    $$
    So  $\sup_{\|u\|=1}u^\top w \le \|w\|_2$ .
*   If  $w\neq 0$ , choose  $u=w/\|w\|_2$ , which has unit norm. Then
    $$
    u^\top w = \left(\frac{w}{\|w\|_2}\right)^\top w = \frac{w^\top w}{\|w\|_2}=\|w\|_2.
    $$
    So the supremum is ≥  $\|w\|_2$ .
*   If  $w=0$ , both sides are 0.

Thus equality holds.

Apply with  $w=Xv$ :

$$
\|Xv\|_2=\sup_{\|u\|_2=1}u^\top (Xv)=\sup_{\|u\|_2=1}u^\top Xv.
$$

2.3 Substitute and collapse the two suprema
-------------------------------------------

$$
\|X\|_2 =\sup_{\|v\|_2=1}\ \sup_{\|u\|_2=1}u^\top Xv =\sup_{\|u\|_2=1,\ \|v\|_2=1}u^\top Xv.
$$

That proves the book’s formula.

* * *

3) Convexity of spectral norm: three proofs
===========================================

3.1 Proof A: supremum of linear functions in  $X$ 
--------------------------------------------------

Fix  $u,v$ . Consider the map

$$
\phi_{u,v}(X):=u^\top Xv.
$$

Show it’s linear in  $X$ :

Take matrices  $X_1,X_2$  and scalars  $\alpha,\beta$ :

$$
\phi_{u,v}(\alpha X_1+\beta X_2) =u^\top(\alpha X_1+\beta X_2)v =\alpha u^\top X_1v+\beta u^\top X_2v =\alpha\phi_{u,v}(X_1)+\beta\phi_{u,v}(X_2).
$$

So linear.

Now

$$
\|X\|_2=\sup_{\|u\|=\|v\|=1}\phi_{u,v}(X)
$$

is a supremum of linear functions ⇒ convex (by the lemma you liked in 3.10).

* * *

3.2 Proof B:  $\|\cdot\|_2$  is a norm in  $X$  ⇒ convex
--------------------------------------------------------

We prove  $\|X\|_2$  is a norm on the vector space  $\mathbb{R}^{p\times q}$ . Then all norms are convex.

### Step 1: triangle inequality for  $\|X\|_2$ 

For any unit  $v$ ,

$$
\|(X+Y)v\|_2 \le \|Xv\|_2+\|Yv\|_2
$$

(vector triangle inequality). Take supremum over  $\|v\|_2=1$ :

$$
\|X+Y\|_2=\sup_{\|v\|=1}\|(X+Y)v\|_2 \le \sup_{\|v\|=1}(\|Xv\|_2+\|Yv\|_2) \le \sup_{\|v\|=1}\|Xv\|_2+\sup_{\|v\|=1}\|Yv\|_2 =\|X\|_2+\|Y\|_2.
$$

### Step 2: homogeneity

$$
\|\alpha X\|_2=\sup_{\|v\|=1}\|\alpha Xv\|_2 =\sup_{\|v\|=1}|\alpha|\|Xv\|_2 =|\alpha|\sup_{\|v\|=1}\|Xv\|_2 =|\alpha|\|X\|_2.
$$

### Step 3: definiteness

 $\|X\|_2\ge 0$ . If  $\|X\|_2=0$ , then  $\|Xv\|_2=0$  for all unit  $v$ , hence  $Xv=0$  for all  $v$ , so  $X=0$ .

So  $\|\cdot\|_2$  is a norm on matrices.

### Step 4: any norm is convex (micro-proof)

For  $\theta\in[0,1]$ ,

$$
\|\theta X+(1-\theta)Y\| \le \|\theta X\|+\|(1-\theta)Y\| =\theta\|X\|+(1-\theta)\|Y\|.
$$

(used triangle inequality + homogeneity). That’s convexity.

So  $\|X\|_2$  is convex.

* * *

3.3 Proof C (spectral norm only): epigraph via an LMI
-----------------------------------------------------

There is a classic semidefinite characterization:

 $$
\boxed{\ \|X\|_2 \le t \quad\Longleftrightarrow\quad \begin{pmatrix} tI_p & X\\ X^\top & tI_q \end{pmatrix}\succeq 0\ }.
$$

### Why this is true (step-by-step with quadratic forms)

Let

$$
M=\begin{pmatrix} tI & X\\ X^\top & tI \end{pmatrix}.
$$

 $M\succeq 0$  means for all vectors  $\begin{pmatrix}u\\ v\end{pmatrix}$ ,

$$
\begin{pmatrix}u\\ v\end{pmatrix}^\top M \begin{pmatrix}u\\ v\end{pmatrix}\ge 0.
$$

Compute the left side explicitly:

$$
u^\top(tI)u + 2u^\top Xv + v^\top(tI)v = t\|u\|_2^2 + 2u^\top Xv + t\|v\|_2^2.
$$

Now, fix  $v$  and choose  $u$  cleverly to extract a condition. The sharpest choice is  $u = -\frac{1}{t}Xv$  (assuming  $t>0$ ). Plug it in:

*    $t\|u\|^2 = t\left\|\frac{1}{t}Xv\right\|^2 = \frac{1}{t}\|Xv\|^2$ 
*    $2u^\top Xv = 2\left(-\frac{1}{t}Xv\right)^\top Xv = -\frac{2}{t}\|Xv\|^2$ 
*    $t\|v\|^2 = t\|v\|^2$ 

Sum:

$$
\frac{1}{t}\|Xv\|^2 - \frac{2}{t}\|Xv\|^2 + t\|v\|^2 = -\frac{1}{t}\|Xv\|^2 + t\|v\|^2 = \frac{1}{t}\big(t^2\|v\|^2 - \|Xv\|^2\big).
$$

PSD requires this ≥ 0 for all  $v$ , so

$$
t^2\|v\|^2 - \|Xv\|^2 \ge 0 \quad\Rightarrow\quad \|Xv\| \le t\|v\|.
$$

Now take supremum over  $v\neq 0$ :

$$
\sup_{v\neq 0}\frac{\|Xv\|}{\|v\|}\le t \quad\Rightarrow\quad \|X\|_2\le t.
$$

That shows  $M\succeq 0 \Rightarrow \|X\|_2\le t$ .

The reverse direction can be shown by bounding  $2u^\top Xv$  using Cauchy–Schwarz and  $\|X\|_2\le t$ :

$$
|u^\top Xv|\le \|u\|\,\|Xv\|\le \|u\|\,(t\|v\|)=t\|u\|\|v\|.
$$

Then

$$
t\|u\|^2 + 2u^\top Xv + t\|v\|^2 \ge t\|u\|^2 - 2t\|u\|\|v\| + t\|v\|^2 = t(\|u\|-\|v\|)^2\ge 0.
$$

So PSD holds.

Thus the equivalence is proved.

### Convexity from the LMI

The epigraph  $\{(X,t): \|X\|_2\le t\}$  equals  $\{(X,t): M(X,t)\succeq 0\}$ . PSD constraints define convex sets;  $M$  depends affinely on  $(X,t)$ . Therefore the epigraph is convex ⇒  $\|X\|_2$  is convex.

* * *

4) General induced norm  $\|X\|_{a,b}$ : derive the bilinear supremum form
==========================================================================

We now prove:

 $$
\boxed{\ \|X\|_{a,b}=\sup\{u^\top Xv:\ \|u\|_{a^\*}=1,\ \|v\|_b=1\}\ }.
$$

4.1 Start from the definition
-----------------------------

$$
\|X\|_{a,b}=\sup_{v\neq 0}\frac{\|Xv\|_a}{\|v\|_b}.
$$

4.2 Normalize  $v$  (explain why you’re allowed)
------------------------------------------------

If  $v\neq 0$ , define  $\tilde v:=v/\|v\|_b$ . Then  $\|\tilde v\|_b=1$ . Also by homogeneity of  $\|\cdot\|_a$ ,

$$
\|Xv\|_a = \|X(\|v\|_b\tilde v)\|_a = \|\|v\|_b(X\tilde v)\|_a = \|v\|_b\|X\tilde v\|_a.
$$

Divide by  $\|v\|_b$ :

$$
\frac{\|Xv\|_a}{\|v\|_b}=\|X\tilde v\|_a.
$$

So

$$
\|X\|_{a,b}=\sup_{\|v\|_b=1}\|Xv\|_a.
$$

4.3 Dualize  $\|Xv\|_a$  into a supremum of dot products
--------------------------------------------------------

Using the dual representation proved earlier:

$$
\|Xv\|_a=\sup_{\|u\|_{a^\*}\le 1}u^\top (Xv).
$$

So

$$
\|X\|_{a,b} =\sup_{\|v\|_b=1}\ \sup_{\|u\|_{a^\*}\le 1} u^\top Xv =\sup_{\|u\|_{a^\*}\le 1,\ \|v\|_b=1} u^\top Xv.
$$

You can replace  $\le 1$  with  $=1$  because if  $\|u\|_{a^\*}<1$  and the dot product is positive, scaling  $u$  up increases it; and if it’s negative, the supremum won’t choose it anyway. Formally:

$$
\sup_{\|u\|\le 1} u^\top z = \sup_{\|u\|=1} u^\top z
$$

for  $z\neq 0$ . (And if  $z=0$ , both are 0.)

Thus:

$$
\|X\|_{a,b} =\sup\{u^\top Xv:\ \|u\|_{a^\*}=1,\ \|v\|_b=1\}.
$$

* * *

5) Convexity of  $\|X\|_{a,b}$ : two independent proofs
=======================================================

5.1 Supremum-of-linear proof
----------------------------

For fixed  $u,v$ ,  $X\mapsto u^\top Xv$  is linear (same distributivity argument as before).  
Then  $\|X\|_{a,b}$  is a supremum of these linear functions, so it’s convex.

5.2 “It’s a norm in  $X$ ” proof (often the cleanest)
-----------------------------------------------------

We show  $\|X\|_{a,b}$  satisfies norm axioms on matrices.

### Nonnegativity/definiteness

 $\|X\|_{a,b}\ge 0$  since it’s a supremum of nonnegative values  $\|Xv\|_a/\|v\|_b$ .  
If  $\|X\|_{a,b}=0$ , then for all  $v\neq 0$ ,

$$
\frac{\|Xv\|_a}{\|v\|_b}\le 0 \Rightarrow \|Xv\|_a=0 \Rightarrow Xv=0.
$$

So  $X$  maps every vector to 0 ⇒  $X=0$ .

### Homogeneity

$$
\|\alpha X\|_{a,b} =\sup_{v\neq 0}\frac{\|\alpha Xv\|_a}{\|v\|_b} =\sup_{v\neq 0}\frac{|\alpha|\|Xv\|_a}{\|v\|_b} =|\alpha|\|X\|_{a,b}.
$$

### Triangle inequality

For any  $v\neq 0$ ,

$$
\|(X+Y)v\|_a \le \|Xv\|_a+\|Yv\|_a.
$$

Divide by  $\|v\|_b$ :

$$
\frac{\|(X+Y)v\|_a}{\|v\|_b}\le \frac{\|Xv\|_a}{\|v\|_b}+\frac{\|Yv\|_a}{\|v\|_b}.
$$

Now take supremum over  $v\neq 0$ :

$$
\|X+Y\|_{a,b}\le \|X\|_{a,b}+\|Y\|_{a,b}.
$$

So  $\|X\|_{a,b}$  is a norm. And as shown earlier, **every norm is convex** by triangle + homogeneity:

$$
\|\theta X+(1-\theta)Y\|\le \theta\|X\|+(1-\theta)\|Y\|.
$$

* * *

6) Extra: what the maximizers “mean” (subgradient intuition)
============================================================

Because

$$
\|X\|_2=\sup_{\|u\|=\|v\|=1} u^\top Xv,
$$

any pair  $(u^\*,v^\*)$  achieving the supremum (when it exists) gives a subgradient:

$$
G = u^\* (v^\*)^\top \in \partial \|X\|_2.
$$

If the top singular value is unique, this subgradient is actually the gradient.

Same story for  $\|X\|_{a,b}$ : optimal  $u^\*,v^\*$  give a supporting hyperplane in  $X$ \-space.

* * *

If you want the next increment of “zero-to-hero completeness,” I can do either (or both) of these in the same ultra-granular style:

1.  Prove from scratch that for  $p\ge 1$ ,  $\ell_p$  is a norm (full Hölder/Minkowski proof).
2.  Prove  $\|X\|_2 = \sqrt{\lambda_{\max}(X^\top X)}$  and connect Example 3.11 to Example 3.10 via eigenvalues (with all steps).

## Prompt:
NEXT EXAMPLE FROM THE ORIGINAL set of 4!

3/3

## Response:
Next from the original 4 is **Example 3.14 (Vector composition / “monotone outer function” machine)**.

I’m going to do it the same way as 3.10/3.11: **zero-to-hero, every step, no magic**, and when I use a theorem (composition rule, “max of affine is convex,” etc.) I’ll **prove it directly**. I’ll also give **alternative proofs** where there’s a nice one (log-sum-exp,  $p$ \-aggregations, geometric mean).

* * *

Example 3.14 — Vector composition rules (the “outer monotone convex” machine)
=============================================================================

What this example is really about
---------------------------------

You often build a function  $f:\mathbb{R}^n\to\mathbb{R}$  by:

1.  computing several “features”  $g_1(x),\dots,g_k(x)$  (each  $g_i:\mathbb{R}^n\to\mathbb{R}$ ),
2.  then combining them by a function  $h:\mathbb{R}^k\to\mathbb{R}$ .

So:

$$
f(x)=h(g_1(x),\dots,g_k(x)).
$$

Write vector  $g(x)=(g_1(x),\dots,g_k(x))\in\mathbb{R}^k$ . Then  $f=h\circ g$ .

The whole game: **when is  $f$  convex or concave** given properties of  $h$  and the  $g_i$ ’s?

* * *

0) Bedrock definitions you must not skip
----------------------------------------

### 0.1 Convex / concave

*    $f$  convex means:
    $$
    f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y).
    $$
*    $f$  concave means the inequality flips:
    $$
    f(\theta x+(1-\theta)y)\ge \theta f(x)+(1-\theta)f(y).
    $$

### 0.2 “Nondecreasing in each argument” (componentwise monotone)

 $h:\mathbb{R}^k\to\mathbb{R}$  is **nondecreasing in each component** if:

$$
z\le z' \text{ componentwise }(\forall i,\ z_i\le z'_i) \quad\Rightarrow\quad h(z)\le h(z').
$$

This is crucial: it’s the bridge that lets you push inequalities through  $h$ .

* * *

1) The core composition theorem (proved from scratch)
=====================================================

Theorem (convex + coordinatewise nondecreasing outer)
-----------------------------------------------------

Assume:

1.  each  $g_i:\mathbb{R}^n\to\mathbb{R}$  is **convex**,
2.   $h:\mathbb{R}^k\to\mathbb{R}$  is **convex**,
3.   $h$  is **nondecreasing in each coordinate**.

Define  $f(x)=h(g_1(x),\dots,g_k(x))$ .  
Then  $f$  is convex.

### Proof (every inequality justified)

Take any  $x,y\in\mathbb{R}^n$  and  $\theta\in[0,1]$ . Define

$$
x_\theta:=\theta x+(1-\theta)y.
$$

**Step 1 (apply convexity of each  $g_i$  separately).**  
For each  $i$ ,

$$
g_i(x_\theta)=g_i(\theta x+(1-\theta)y)\ \le\ \theta g_i(x)+(1-\theta)g_i(y).
$$

**Step 2 (stack into a vector inequality).**  
Let

$$
g(x)=(g_1(x),\dots,g_k(x)).
$$

Then the  $k$  inequalities above mean:

$$
g(x_\theta)\ \le\ \theta g(x)+(1-\theta)g(y)\quad\text{componentwise}.
$$

**Step 3 (use monotonicity of  $h$ ).**  
Since  $h$  is nondecreasing coordinatewise and the input vector got smaller componentwise,

$$
h(g(x_\theta))\ \le\ h(\theta g(x)+(1-\theta)g(y)).
$$

**Step 4 (use convexity of  $h$  in  $\mathbb{R}^k$ ).**  
Convexity of  $h$  gives:

$$
h(\theta g(x)+(1-\theta)g(y))\ \le\ \theta h(g(x))+(1-\theta)h(g(y)).
$$

**Step 5 (chain the inequalities).**

$$
f(x_\theta)=h(g(x_\theta)) \le h(\theta g(x)+(1-\theta)g(y)) \le \theta h(g(x))+(1-\theta)h(g(y)) = \theta f(x)+(1-\theta)f(y).
$$

That is exactly convexity. □

* * *

Concave version (same proof, flipped)
-------------------------------------

If:

*   each  $g_i$  is **concave**,
*    $h$  is **concave** and **nondecreasing** coordinatewise,

then  $h(g(x))$  is concave (same chain but with reversed inequalities at the convexity/concavity steps).

* * *

2) Now the specific functions  $h$  in Example 3.14
===================================================

The book lists several important “outer functions”  $h$  that are convex/concave **and** coordinatewise monotone. Once you prove those properties for  $h$ , the composition theorem gives you convexity/concavity of  $h(g_1(x),\dots,g_k(x))$ .

I’ll do each one as:  
**(A) prove monotonicity**, **(B) prove convexity/concavity**, **(C) conclude composition**.

* * *

(i) Sum of the  $r$  largest components is convex and nondecreasing
-------------------------------------------------------------------

### Definition

Let  $z\in\mathbb{R}^k$ . Let  $z_{[1]}\ge z_{[2]}\ge\cdots\ge z_{[k]}$  be the components sorted in nonincreasing order.  
Define

$$
h(z)=z_{[1]}+\cdots+z_{[r]}.
$$

### A) Monotonicity (componentwise)

Suppose we increase one coordinate  $z_j$  while keeping others fixed.

*   Any sum that includes  $z_j$  increases (because that term increased),
*   sums that don’t include  $z_j$  stay the same,  
    so the maximum/top- $r$  sum cannot go down.  
    Therefore  $h$  is nondecreasing in each coordinate.

### B) Convexity via “max over subset sums” (proved carefully)

**Claim**

$$
h(z)=\max_{\substack{S\subseteq\{1,\dots,k\}\\|S|=r}}\ \sum_{i\in S} z_i.
$$

**Why is this identity true?**

*   For any subset  $S$  with  $|S|=r$ ,  $\sum_{i\in S} z_i$  is the sum of some  $r$  components.
*   The largest possible sum of  $r$  components is obtained by choosing the  $r$  largest components, i.e.  $z_{[1]}+\cdots+z_{[r]}$ .  
    So the maximum over all such subset sums equals the top- $r$  sum.

Now, for each fixed subset  $S$ ,

$$
\phi_S(z):=\sum_{i\in S} z_i
$$

is **linear** in  $z$ . (It is literally a dot product with an indicator vector.)

Then

$$
h(z)=\max_{|S|=r}\phi_S(z)
$$

is a **pointwise maximum of linear functions**, hence convex.

> Direct proof “max of affine is convex” (no quoting):  
> For any  $\theta$ ,  
>  $\max_i a_i(\theta x+(1-\theta)y)\le \theta\max_i a_i(x)+(1-\theta)\max_i a_i(y)$   
> because for each  $i$ ,  $a_i(\theta x+(1-\theta)y)=\theta a_i(x)+(1-\theta)a_i(y)\le \theta\max_j a_j(x)+(1-\theta)\max_j a_j(y)$ , then take max over  $i$ .

### C) Composition conclusion

If each  $g_i(x)$  is convex, then

$$
x\mapsto \text{sum of the \(r\) largest of }(g_1(x),\dots,g_k(x))
$$

is convex.

* * *

(ii) Log-sum-exp is convex and nondecreasing (and “softmax density” appears)
----------------------------------------------------------------------------

### Definition

$$
h(z)=\log\left(\sum_{i=1}^k e^{z_i}\right).
$$

Let  $S(z)=\sum_i e^{z_i}$ .

### A) Monotonicity (show partial derivatives are positive)

Compute:

$$
\frac{\partial S}{\partial z_i}=e^{z_i}.
$$

By chain rule:

$$
\frac{\partial h}{\partial z_i}=\frac{1}{S(z)}\frac{\partial S}{\partial z_i} =\frac{e^{z_i}}{\sum_j e^{z_j}}.
$$

Define

$$
s_i(z):=\frac{e^{z_i}}{\sum_j e^{z_j}}.
$$

Then  $s_i(z)>0$  and  $\sum_i s_i(z)=1$ . This is a **probability mass function** (a discrete “density”). Since  $\partial h/\partial z_i>0$ ,  $h$  is coordinatewise increasing.

### B) Convexity via Hessian = covariance/variance (fully explicit)

We compute  $\nabla^2 h(z)$  and show it’s PSD (positive semidefinite).

We already have  $\nabla h(z)=s(z)$ .

Differentiate  $s_i$  w.r.t.  $z_\ell$ :

*   If  $i=\ell$ :
    $$
    \frac{\partial s_i}{\partial z_i}=s_i(1-s_i).
    $$
*   If  $i\ne \ell$ :
    $$
    \frac{\partial s_i}{\partial z_\ell}=-s_i s_\ell.
    $$

So in matrix form:

$$
\nabla^2 h(z)=\mathrm{diag}(s)-ss^\top.
$$

**Now prove PSD by quadratic form (no shortcuts).**  
Take any  $v\in\mathbb{R}^k$ . Compute

$$
v^\top(\mathrm{diag}(s)-ss^\top)v =\sum_i s_i v_i^2-\left(\sum_i s_i v_i\right)^2.
$$

Interpret  $I$  as a random index with  $\mathbb{P}(I=i)=s_i$ . Then

*    $\mathbb{E}[v_I]=\sum_i s_i v_i$ ,
*    $\mathbb{E}[v_I^2]=\sum_i s_i v_i^2$ .

So the expression equals

$$
\mathbb{E}[v_I^2]-(\mathbb{E}[v_I])^2=\mathrm{Var}(v_I)\ge 0.
$$

Variance is always nonnegative. Hence  $\nabla^2 h(z)\succeq 0$ , so  $h$  is convex.

### Alternative convexity proof (no derivatives): Hölder

You can prove:

$$
\log\sum_i e^{\theta z_i+(1-\theta)w_i}\le \theta\log\sum_i e^{z_i}+(1-\theta)\log\sum_i e^{w_i}
$$

by exponentiating and applying Hölder to  $\sum_i (e^{z_i})^\theta (e^{w_i})^{1-\theta}$ . Very clean.

### C) Composition conclusion

If  $g_i(x)$  are convex, then

$$
x\mapsto \log\left(\sum_i e^{g_i(x)}\right)
$$

is convex (outer  $h$  convex + increasing, inner  $g_i$  convex).

* * *

(iii)  $p$ \-aggregation for  $0<p\le 1$  is concave on  $\mathbb{R}_+^k$ 
--------------------------------------------------------------------------

### Definition

For  $z\in\mathbb{R}_+^k$  (all components nonnegative),

$$
h(z)=\left(\sum_{i=1}^k z_i^p\right)^{1/p},\quad 0<p\le 1.
$$

### A) Monotonicity

If you increase any  $z_i\ge 0$ , then  $z_i^p$  increases (since  $t\mapsto t^p$  is increasing on  $\mathbb{R}_+$ ). Sum increases, power  $1/p$  preserves monotonicity. So  $h$  is coordinatewise nondecreasing.

### B) Concavity (clean route)

This is the subtle part. A very robust proof uses:

1.  **1-homogeneity:**  $h(\alpha z)=\alpha h(z)$  for  $\alpha\ge 0$ .
2.  **log-concavity:**  $\log h(z)$  is concave.
3.  **Lemma:** 1-homogeneous + log-concave ⇒ concave.

I will prove all three.

#### Step B1: 1-homogeneity

$$
h(\alpha z)=\left(\sum (\alpha z_i)^p\right)^{1/p} =\left(\alpha^p\sum z_i^p\right)^{1/p} =\alpha\left(\sum z_i^p\right)^{1/p} =\alpha h(z).
$$

#### Step B2: log-concavity

For  $z\succ 0$ ,

$$
\log h(z)=\frac{1}{p}\log\left(\sum_i z_i^p\right).
$$

For  $0<p\le 1$ ,  $t\mapsto t^p$  is concave on  $\mathbb{R}_+$ , so  $z\mapsto \sum_i z_i^p$  is concave.  
 $\log(\cdot)$  is concave and increasing on  $\mathbb{R}_{++}$ .  
Composition “concave increasing outer with concave inner” preserves concavity. Multiply by  $1/p>0$ : still concave.  
So  $\log h$  is concave ⇒  $h$  is log-concave.

#### Step B3: Lemma (proved): 1-homogeneous + log-concave ⇒ concave

Assume  $f>0$ , 1-homogeneous, log-concave. Want:

$$
f(\theta x+(1-\theta)y)\ge \theta f(x)+(1-\theta)f(y).
$$

Let  $a=f(x)$ ,  $b=f(y)$ . Define normalized points  $\bar x=x/a$ ,  $\bar y=y/b$ . Then  $f(\bar x)=f(\bar y)=1$ .  
Write  $z=\theta x+(1-\theta)y=\theta a\bar x+(1-\theta)b\bar y$ . Let  $s=\theta a+(1-\theta)b$  and weights  $\alpha=\theta a/s$ ,  $\beta=(1-\theta)b/s$  so  $\alpha+\beta=1$ . Then

$$
z=s(\alpha\bar x+\beta\bar y).
$$

By 1-homogeneity:

$$
f(z)=s f(\alpha\bar x+\beta\bar y).
$$

By log-concavity:

$$
f(\alpha\bar x+\beta\bar y)\ge f(\bar x)^\alpha f(\bar y)^\beta = 1.
$$

So  $f(z)\ge s=\theta a+(1-\theta)b$ . Done.

Apply lemma to  $h$ : concave.

### C) Composition conclusion

If each  $g_i(x)$  is **concave and nonnegative**, then

$$
x\mapsto \left(\sum_i g_i(x)^p\right)^{1/p}
$$

is concave.

* * *

(iv)  $p$ \-aggregation for  $p\ge 1$  is convex (with the “positive part” trick)
---------------------------------------------------------------------------------

### Definition

Assume  $p\ge 1$ . Define

$$
\tilde h(z)=\left(\sum_i (z_i)_+^p\right)^{1/p},\quad (t)_+=\max(t,0).
$$

### A) Monotonicity

Each  $(z_i)_+$  is nondecreasing in  $z_i$ . The map  $w\mapsto \|w\|_p$  is nondecreasing on  $\mathbb{R}_+^k$ . So  $\tilde h$  is coordinatewise nondecreasing.

### B) Convexity (two-layer argument)

1.   $z\mapsto z_+$  is convex (it’s  $\max(z,0)$ , a max of affine functions).
2.   $w\mapsto \|w\|_p$  is a norm for  $p\ge 1$ , hence convex.  
    Then  $\tilde h(z)=\|z_+\|_p$  is convex (and the book uses this because it behaves well even when inputs can be negative).

### C) Composition conclusion

If  $g_i(x)\ge 0$  and convex, then  $(g_i(x))_+=g_i(x)$ , so

$$
\tilde h(g(x))=\left(\sum_i g_i(x)^p\right)^{1/p}
$$

is convex by the composition theorem (outer convex+monotone, inner convex).

* * *

(v) Geometric mean is concave on  $\mathbb{R}_+^k$ 
---------------------------------------------------

### Definition

$$
h(z)=\left(\prod_{i=1}^k z_i\right)^{1/k},\quad z\in\mathbb{R}_+^k.
$$

### A) Monotonicity

Increasing any  $z_i$  increases the product, hence increases  $h$ . So coordinatewise nondecreasing.

### B) Concavity (log trick + lemma)

For  $z\succ 0$ ,

$$
\log h(z)=\frac{1}{k}\sum_{i=1}^k \log z_i.
$$

Each  $\log z_i$  is concave on  $\mathbb{R}_{++}$ . An average of concave functions is concave. So  $\log h$  is concave ⇒  $h$  log-concave.  
Also  $h$  is 1-homogeneous:

$$
h(\alpha z)=\alpha h(z).
$$

By the same lemma (1-homogeneous + log-concave ⇒ concave),  $h$  is concave.

### Alternative proof (AM–GM flavored)

You can also derive log-concavity from weighted AM–GM and then use the lemma to upgrade to concavity.

### C) Composition conclusion

If  $g_i(x)$  are concave and nonnegative, then

$$
x\mapsto \left(\prod_i g_i(x)\right)^{1/k}
$$

is concave.

* * *

What you should “walk away with”
================================

Example 3.14 is a toolbox:

*   Prove ** $h$ ** is convex/concave and **coordinatewise monotone**.
*   Then  $h(g_1(x),\dots,g_k(x))$  inherits convexity/concavity from the  $g_i$ ’s via the theorem.

* * *

If you want the next step in the same style, I can now do **Example 3.17** (partial minimization / equality constraint) ultra-granular, including: epigraph projection proof,  $\varepsilon$ \-minimizer proof, and the dual representation (“value function is convex because it’s a supremum of affine functions”).

## Prompt:
Next

## Response:
Next is **Example 3.17 — Minimization over a linear equality preserves convexity**.

We’ll go _full bedrock_ again: define every object, prove every “obvious” lemma (indicator convexity, projection convexity), then give **three proofs**:

1.  **Epigraph = projection** (clean geometric proof)
2.  **Direct Jensen via  $\varepsilon$ \-minimizers** (pure inequalities)
3.  **Lagrange dual / conjugate representation** (cool alternative; shows  $g$  is a supremum of affine functions)

* * *

Example 3.17 (statement)
========================

Let  $h:\mathbb{R}^m\to\mathbb{R}\cup\{+\infty\}$  be **convex** (extended-value allowed). Let  $A\in\mathbb{R}^{n\times m}$  be fixed.

Define a new function  $g:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$  by

$$
g(x) \;:=\; \inf\{\, h(y)\;:\; Ay=x \,\}.
$$

Claim: ** $g$  is convex.**

Intuition:  $x$  is a “parameter” in the equality constraint  $Ay=x$ . You’re taking the **optimal value** of a convex problem as a function of the parameter. Optimal value functions of convex problems are convex (under the right structure), and here the structure is as clean as it gets: a linear equality.

* * *

0) Conventions and “extended value” arithmetic (important)
==========================================================

Because  $h$  may take  $+\infty$ , we interpret:

*   If the constraint  $Ay=x$  is infeasible (no  $y$  satisfies it), then the infimum is over an empty set, and by convention:
    $$
    \inf \emptyset = +\infty.
    $$
    So  $g(x)=+\infty$  for infeasible  $x$ . That’s _good_ — it encodes infeasibility as “outside the domain.”
*   Rules you’ll need:
    *    $+\infty + c = +\infty$  for any real  $c$ .
    *    $\theta(+\infty) = +\infty$  for any  $\theta>0$ .
    *   Comparisons: any real number  $\le +\infty$ .

This is how convex analysis keeps proofs clean without constantly saying “assume feasible.”

* * *

1) The book’s construction: build a joint function  $f(x,y)$ 
=============================================================

Define

$$
f(x,y)= \begin{cases} h(y), & \text{if } Ay=x,\\ +\infty, & \text{otherwise.} \end{cases}
$$

Then by definition,

$$
g(x)=\inf_{y} f(x,y).
$$

So  $g$  is the **partial minimization** of  $f$  over  $y$ .

To prove  $g$  convex, we’ll prove:

1.   $f$  is convex in the joint variable  $(x,y)$ , and
2.  partial minimization of a jointly convex function is convex.

We will prove both from scratch.

* * *

2) Step 1: Prove  $f$  is convex in  $(x,y)$ 
=============================================

The clean way is to write  $f$  as:

$$
f(x,y)=h(y)+I_C(x,y),
$$

where  $C=\{(x,y): Ay=x\}$  and  $I_C$  is an indicator function.

2.1 Define the indicator function  $I_C$ 
-----------------------------------------

For a set  $C\subseteq\mathbb{R}^{n+m}$ ,

$$
I_C(z)= \begin{cases} 0,& z\in C,\\ +\infty,& z\notin C. \end{cases}
$$

Here  $z=(x,y)$ .

So indeed:

*   If  $(x,y)\in C$  (meaning  $Ay=x$ ), then  $f(x,y)=h(y)+0=h(y)$ .
*   If  $(x,y)\notin C$ , then  $f(x,y)=h(y)+(+\infty)=+\infty$ .

2.2 Prove  $C=\{(x,y):Ay=x\}$  is convex (actually affine)
----------------------------------------------------------

Take any  $(x_1,y_1)\in C$  and  $(x_2,y_2)\in C$ . That means:

$$
Ay_1=x_1,\qquad Ay_2=x_2.
$$

Take any  $\theta\in[0,1]$ . Consider the convex combination:

$$
(x_\theta,y_\theta) := (\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2).
$$

Check if it satisfies the defining equation:

$$
Ay_\theta = A(\theta y_1+(1-\theta)y_2)=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2=x_\theta.
$$

So  $(x_\theta,y_\theta)\in C$ . Therefore  $C$  is convex.

(And because it’s defined by a linear equality, it’s actually an **affine** set, which is always convex.)

2.3 Prove: indicator of a convex set is a convex function
---------------------------------------------------------

**Claim:** If  $C$  is convex, then  $I_C$  is convex (as an extended-value function).

**Proof (case-by-case, no handwave):**  
Take any  $z_1,z_2$  and  $\theta\in[0,1]$ . We must show:

$$
I_C(\theta z_1+(1-\theta)z_2)\ \le\ \theta I_C(z_1)+(1-\theta)I_C(z_2).
$$

There are only a few cases:

*   **Case A:**  $z_1\in C$  and  $z_2\in C$ .  
    Then  $I_C(z_1)=I_C(z_2)=0$ .  
    Since  $C$  is convex,  $\theta z_1+(1-\theta)z_2\in C$ , so LHS  $=0$ .  
    RHS  $=\theta\cdot 0+(1-\theta)\cdot 0=0$ .  
    So  $0\le 0$ . True.
*   **Case B:** at least one of  $z_1,z_2$  is not in  $C$ .  
    Then at least one of  $I_C(z_1), I_C(z_2)$  is  $+\infty$ .  
    If  $\theta\in(0,1)$ , RHS becomes  $+\infty$  (because a positive weight times  $+\infty$  is  $+\infty$ , and adding keeps  $+\infty$ ).  
    LHS is either  $0$  or  $+\infty$ , but either way  $ \text{LHS} \le +\infty$  is true.

So the inequality always holds. Hence  $I_C$  is convex. □

2.4 Prove:  $h(y)$  viewed as a function of  $(x,y)$  is convex
---------------------------------------------------------------

Define  $\tilde h(x,y):=h(y)$ . It ignores  $x$ .

Take  $(x_1,y_1),(x_2,y_2)$  and  $\theta$ :

$$
\tilde h(\theta(x_1,y_1)+(1-\theta)(x_2,y_2)) =\tilde h(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2) =h(\theta y_1+(1-\theta)y_2).
$$

Since  $h$  is convex:

$$
h(\theta y_1+(1-\theta)y_2)\le \theta h(y_1)+(1-\theta)h(y_2) =\theta\tilde h(x_1,y_1)+(1-\theta)\tilde h(x_2,y_2).
$$

So  $\tilde h$  is convex in  $(x,y)$ .

2.5 Sum of convex functions is convex (extended-value version)
--------------------------------------------------------------

We know:

*    $\tilde h$  is convex,
*    $I_C$  is convex.

Define  $f=\tilde h + I_C$ . Then for any points and  $\theta$ ,

$$
f(\theta z_1+(1-\theta)z_2) =\tilde h(\theta z_1+(1-\theta)z_2)+I_C(\theta z_1+(1-\theta)z_2) \le \theta \tilde h(z_1)+(1-\theta)\tilde h(z_2)+\theta I_C(z_1)+(1-\theta)I_C(z_2) = \theta f(z_1)+(1-\theta)f(z_2).
$$

All steps are just “add inequalities.” (Extended-value arithmetic is consistent here:  $+\infty$  behaves monotonically.)

So ** $f$  is convex in  $(x,y)$ .**

* * *

3) Step 2: Prove partial minimization preserves convexity
=========================================================

We now prove: if  $f(x,y)$  is convex in  $(x,y)$ , then

$$
g(x):=\inf_y f(x,y)
$$

is convex.

I’ll give you **two proofs**.

* * *

Proof 1 (geometric): epigraph of  $g$  is a projection of epigraph of  $f$ 
---------------------------------------------------------------------------

### 3.1 Define epigraphs

For any function  $q$ , its epigraph is:

$$
\mathrm{epi}(q)=\{(u,t): q(u)\le t\}.
$$

### 3.2 Write  $\mathrm{epi}(g)$  using the definition of infimum

Start:

$$
(x,t)\in\mathrm{epi}(g)\quad \Longleftrightarrow\quad g(x)\le t.
$$

But  $g(x)=\inf_y f(x,y)$ . So:

$$
\inf_y f(x,y)\le t.
$$

Now: what does “infimum  $\le t$ ” mean? It means **there exists** some  $y$  with  $f(x,y)\le t$ . (If every  $y$  had  $f(x,y)>t$ , the inf would be  $>t$ .)

So:

$$
g(x)\le t \quad\Longleftrightarrow\quad \exists y \text{ such that } f(x,y)\le t.
$$

Therefore:

$$
\mathrm{epi}(g)=\{(x,t): \exists y\ \text{s.t. } f(x,y)\le t\}.
$$

### 3.3 Recognize this as a projection

Define

$$
\mathrm{epi}(f)=\{(x,y,t): f(x,y)\le t\}.
$$

Then

$$
(x,t)\in\mathrm{epi}(g)\quad\Longleftrightarrow\quad \exists y\ \text{s.t. } (x,y,t)\in \mathrm{epi}(f).
$$

That is exactly:

$$
\mathrm{epi}(g)=\Pi_{x,t}(\mathrm{epi}(f)),
$$

the projection of  $\mathrm{epi}(f)$  onto the  $(x,t)$ \-coordinates.

### 3.4 Two mini-lemmas

*   **Lemma A:**  $f$  convex    $\iff \mathrm{epi}(f)$  convex.  
    (Standard, but can be checked directly from the definition.)
*   **Lemma B:** projection of a convex set is convex.  
    Proof: take two projected points, lift them to points in the big set, take convex combination (stays in big set), then project back. (I proved this earlier, but it’s one line.)

### 3.5 Conclude

Since  $f$  is convex,  $\mathrm{epi}(f)$  is convex. Its projection  $\mathrm{epi}(g)$  is convex. Therefore  $g$  is convex. □

* * *

Proof 2 (algebraic):  $\varepsilon$ \-minimizers + Jensen
---------------------------------------------------------

This proof is “pure inequalities,” no epigraph geometry.

Take  $x_1,x_2\in\mathbb{R}^n$  and  $\theta\in[0,1]$ . Let

$$
x_\theta=\theta x_1+(1-\theta)x_2.
$$

If  $g(x_1)=+\infty$  or  $g(x_2)=+\infty$ , the convexity inequality is automatically true (RHS is  $+\infty$ ). So assume both are finite.

By definition of infimum: for any  $\varepsilon>0$ , we can choose  $y_1,y_2$  such that

$$
Ay_1=x_1,\quad h(y_1)\le g(x_1)+\varepsilon,
$$
 
$$
Ay_2=x_2,\quad h(y_2)\le g(x_2)+\varepsilon.
$$

(That’s what “infimum” means: you can get within  $\varepsilon$  of it.)

Now define the convex combination:

$$
y_\theta:=\theta y_1+(1-\theta)y_2.
$$

**Feasibility check (don’t skip):**

$$
Ay_\theta = A(\theta y_1+(1-\theta)y_2)=\theta Ay_1+(1-\theta)Ay_2=\theta x_1+(1-\theta)x_2=x_\theta.
$$

So  $y_\theta$  is feasible for  $x_\theta$ .

Now apply convexity of  $h$ :

$$
h(y_\theta)\le \theta h(y_1)+(1-\theta)h(y_2) \le \theta(g(x_1)+\varepsilon)+(1-\theta)(g(x_2)+\varepsilon) = \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
$$

Finally, because  $g(x_\theta)$  is the infimum over all feasible  $y$ , it is  $\le$  the value at this particular feasible  $y_\theta$ :

$$
g(x_\theta)\le h(y_\theta)\le \theta g(x_1)+(1-\theta)g(x_2)+\varepsilon.
$$

Since this holds for every  $\varepsilon>0$ , let  $\varepsilon\downarrow 0$ :

$$
g(x_\theta)\le \theta g(x_1)+(1-\theta)g(x_2).
$$

Convexity proved. □

* * *

4) Alternative “interesting” proof: Lagrange dual / conjugate representation
============================================================================

This is the slick “adult” view:  $g$  becomes a **supremum of affine functions of  $x$ **, hence convex immediately.

4.1 Start from the constrained problem
--------------------------------------

$$
g(x)=\inf_y \{\, h(y): Ay=x\,\}.
$$

Equivalently,

$$
g(x)=\inf_y \left(h(y)+I_{\{x\}}(Ay)\right),
$$

but we’ll do Lagrange multipliers directly.

4.2 Build the Lagrangian
------------------------

Introduce multiplier  $\nu\in\mathbb{R}^n$  for constraint  $Ay=x$ . Define

$$
\mathcal{L}(y,\nu)=h(y)+\nu^\top(x-Ay).
$$

For fixed  $\nu$ , this is an unconstrained function of  $y$ .

4.3 Weak dual lower bound (every step)
--------------------------------------

For any feasible  $y$  (i.e.  $Ay=x$ ),

$$
\mathcal{L}(y,\nu)=h(y)+\nu^\top(x-Ay)=h(y)+\nu^\top(0)=h(y).
$$

So for feasible  $y$ ,  $\mathcal{L}(y,\nu)$  equals the objective.

Therefore for any  $\nu$ ,

$$
\inf_y \mathcal{L}(y,\nu)\ \le\ \inf_{Ay=x} \mathcal{L}(y,\nu)\ =\ \inf_{Ay=x} h(y) \ =\ g(x).
$$

So:

$$
\underbrace{\inf_y \mathcal{L}(y,\nu)}_{\text{a function of }x,\nu}\ \le\ g(x)\quad\forall \nu.
$$

Taking supremum over  $\nu$  preserves the inequality:

$$
\sup_\nu \inf_y \mathcal{L}(y,\nu)\ \le\ g(x).
$$

That’s **weak duality**.

4.4 Compute  $\inf_y \mathcal{L}(y,\nu)$  using the conjugate
-------------------------------------------------------------

Expand:

$$
\inf_y \mathcal{L}(y,\nu) =\inf_y \left(h(y)+\nu^\top x-\nu^\top Ay\right) =\nu^\top x + \inf_y \left(h(y) - (A^\top\nu)^\top y\right).
$$

Now recall conjugate definition:

$$
h^\*(s)=\sup_y (s^\top y - h(y)).
$$

Then:

$$
\inf_y (h(y)-s^\top y) = - \sup_y (s^\top y - h(y)) = -h^\*(s).
$$

So with  $s=A^\top \nu$ ,

$$
\inf_y \mathcal{L}(y,\nu)=\nu^\top x - h^\*(A^\top \nu).
$$

Thus weak duality gives:

$$
\sup_{\nu}\left(\nu^\top x - h^\*(A^\top \nu)\right)\ \le\ g(x).
$$

4.5 Strong duality (when you get equality)
------------------------------------------

Under standard regularity (e.g.  $h$  closed convex and the equality system is “compatible” in the right way; in many textbook settings this holds), you get equality:

$$
\boxed{g(x)=\sup_{\nu}\left(\nu^\top x - h^\*(A^\top \nu)\right).}
$$

Now the convexity is immediate because:

*   for each fixed  $\nu$ ,  $x\mapsto \nu^\top x - h^\*(A^\top\nu)$  is **affine** in  $x$ ,
*   supremum of affine functions is convex.

Even if you _don’t_ assume strong duality, the projection/Jensen proofs already established convexity of  $g$ . This dual form is the “bonus structure.”

* * *

5) Concrete sanity example (to make it feel real)
=================================================

Let

$$
h(y)=\frac{1}{2}\|y\|_2^2 \quad\text{(convex quadratic)}.
$$

Then

$$
g(x)=\inf\left\{\frac12\|y\|^2: Ay=x\right\}.
$$

This is “minimum norm solution” under a linear equality. The optimal value  $g(x)$  is convex in  $x$ . If  $A$  has full row rank, the solution is  $y^\*=A^\top(AA^\top)^{-1}x$ , and you can compute  $g(x)=\tfrac12 x^\top(AA^\top)^{-1}x$ , a convex quadratic.

So the theorem matches explicit algebra.

* * *

What you should remember
------------------------

*   The equality set  $\{(x,y):Ay=x\}$  is affine ⇒ convex.
*   Turning a constraint into an indicator keeps convexity.
*   Minimizing out variables corresponds to **projecting an epigraph**, and projection preserves convexity.

That’s the core “convexity survives optimization” meta-fact.

If you want to keep going in this same mode, the next natural “extra” is: compute **subgradients of  $g$ ** via dual multipliers  $\nu^\*$  (envelope theorem / KKT), which is exactly how sensitivity analysis works in convex optimization.

## Prompt:
Do the same treat for 3.35 from below:

Below are **Example 3.35** and **Example 3.36**, unpacked from first principles. The hidden theme is the same in both:

> **Nonnegativity / PSD kills cancellation.**
> So when you add (or take a convex combination), “support” (nonzeros) and “range” can only grow, not shrink.

That one sentence is doing basically all the work.

---

# 1) The “modified Jensen inequality” for quasiconcavity (what they’re invoking)

## 1.1 Quasiconcave: the real definition

A function (f:\mathrm{dom} f\subseteq \mathbb R^n\to \mathbb R\cup{-\infty}) is **quasiconcave** if **all its upper level sets are convex**:
[
U_\alpha ;:=;{x\in \mathrm{dom}f \mid f(x)\ge \alpha}
\quad \text{is convex for every }\alpha.
]

## 1.2 Equivalent “modified Jensen inequality”

This is the characterization they call “modified Jensen”:
[
f(\theta x+(1-\theta)y)\ \ge\ \min{f(x),f(y)}
\qquad \forall x,y,\ \theta\in[0,1].
]
Why is this equivalent to convexity of upper level sets?

### (⇒) If upper level sets are convex, then the inequality holds

Let (a=\min{f(x),f(y)}). Then (x\in U_a) and (y\in U_a).
If (U_a) is convex, then (\theta x+(1-\theta)y\in U_a).
So (f(\theta x+(1-\theta)y)\ge a=\min{f(x),f(y)}).

### (⇐) If the inequality holds, then upper level sets are convex

Take any (\alpha) and any (x,y\in U_\alpha). Then (f(x)\ge \alpha) and (f(y)\ge \alpha), so (\min{f(x),f(y)}\ge \alpha).
Apply the inequality:
[
f(\theta x+(1-\theta)y)\ge \min{f(x),f(y)}\ge \alpha,
]
so (\theta x+(1-\theta)y\in U_\alpha). Hence (U_\alpha) is convex.

So: **to prove quasiconcavity it’s enough to prove the modified Jensen inequality**.

---

# 2) Example 3.35 — Cardinality on (\mathbb R_+^n)

## 2.1 Definition (what “cardinality” means here)

For a vector (x\in\mathbb R^n), define its **support**
[
\mathrm{supp}(x)={i\in{1,\dots,n}: x_i\neq 0},
]
and its **cardinality**
[
\mathrm{card}(x)=|\mathrm{supp}(x)|,
]
the number of nonzero components.

The claim: **(\mathrm{card}(x)) is quasiconcave on (\mathbb R_+^n)** (but not on all (\mathbb R^n)).

---

## 2.2 The key “no cancellation” fact on (\mathbb R_+^n)

Assume (x\ge 0) and (y\ge 0) componentwise.

### Claim: (\mathrm{supp}(x+y)=\mathrm{supp}(x)\cup \mathrm{supp}(y))

Pick a coordinate (i).

* If (i\in \mathrm{supp}(x)\cup\mathrm{supp}(y)), then either (x_i>0) or (y_i>0).
  Since both are (\ge 0), we get ((x+y)_i=x_i+y_i>0), so (i\in\mathrm{supp}(x+y)).

* If (i\notin \mathrm{supp}(x)\cup\mathrm{supp}(y)), then (x_i=0) and (y_i=0), hence ((x+y)_i=0), so (i\notin\mathrm{supp}(x+y)).

So equality holds.

### Consequence for cardinality

[
\mathrm{card}(x+y)=|\mathrm{supp}(x)\cup\mathrm{supp}(y)|
\ \ge\ \max{|\mathrm{supp}(x)|,|\mathrm{supp}(y)|}
\ \ge\ \min{\mathrm{card}(x),\mathrm{card}(y)}.
]

That already proves the inequality they wrote, and actually gives a **stronger** one:
[
\mathrm{card}(x+y)\ge \max{\mathrm{card}(x),\mathrm{card}(y)}
\qquad (x,y\ge 0).
]

---

## 2.3 From that to quasiconcavity (modified Jensen)

Take any (x,y\in\mathbb R_+^n) and any (\theta\in(0,1)). Consider
[
z=\theta x+(1-\theta)y.
]
Coordinatewise:

* If (x_i>0) or (y_i>0), then since (\theta>0) and (1-\theta>0),
  [
  z_i=\theta x_i+(1-\theta)y_i>0.
  ]
* If (x_i=y_i=0), then (z_i=0).

So again
[
\mathrm{supp}(z)=\mathrm{supp}(x)\cup \mathrm{supp}(y),
]
hence
[
\mathrm{card}(\theta x+(1-\theta)y)
=|\mathrm{supp}(x)\cup\mathrm{supp}(y)|
\ge \min{\mathrm{card}(x),\mathrm{card}(y)}.
]
That is exactly the modified Jensen inequality, so **(\mathrm{card}) is quasiconcave on (\mathbb R_+^n)**.

(For (\theta=0) or (\theta=1) the inequality is trivial.)

---

## 2.4 Why it fails on all of (\mathbb R^n)

Outside (\mathbb R_+^n), **cancellation** can happen.

Example in (\mathbb R^1):
[
x=1,\quad y=-1.
]
Then (\mathrm{card}(x)=\mathrm{card}(y)=1), but
[
\theta x+(1-\theta)y = \theta -(1-\theta) = 2\theta-1.
]
At (\theta=\tfrac12) this is (0), so
[
\mathrm{card}\big(\tfrac12 x+\tfrac12 y\big)=\mathrm{card}(0)=0
;<; 1=\min{1,1}.
]
So the modified Jensen inequality fails, hence **not quasiconcave on (\mathbb R^n)**.

---

# 3) Example 3.36 — Rank on (\mathbf S_+^n)

## 3.1 Setup and definitions

(\mathbf S_+^n) is the cone of symmetric positive semidefinite (PSD) matrices:
[
X\succeq 0 \iff v^\top Xv\ge 0\ \ \forall v.
]

The function is
[
f(X)=\mathrm{rank}(X),
]
and the claim: **(\mathrm{rank}) is quasiconcave on (\mathbf S_+^n)**.

---

## 3.2 The PSD “no cancellation” lemma you need

### Lemma: If (X\succeq 0) and (v^\top Xv=0), then (Xv=0).

Reason: PSD matrices have a (unique PSD) square root (X^{1/2}\succeq 0) with (X=X^{1/2}X^{1/2}). Then
[
v^\top Xv = v^\top X^{1/2}X^{1/2}v = |X^{1/2}v|_2^2.
]
If this equals 0, then (X^{1/2}v=0), hence (Xv=X^{1/2}(X^{1/2}v)=0).

This is the matrix analogue of: for nonnegative numbers, if (a+b=0) then (a=b=0).

---

## 3.3 Nullspace of a PSD sum is an intersection

Let (X,Y\succeq 0). Claim:
[
\mathcal N(X+Y)=\mathcal N(X)\cap \mathcal N(Y),
]
where (\mathcal N(\cdot)) is the nullspace.

### Proof

* If (v\in\mathcal N(X)\cap\mathcal N(Y)), then (Xv=0) and (Yv=0), so ((X+Y)v=0). Thus (v\in\mathcal N(X+Y)).

* Conversely, if (v\in\mathcal N(X+Y)), then ((X+Y)v=0). Multiply on the left by (v^\top):
  [
  0 = v^\top(X+Y)v = v^\top Xv + v^\top Yv.
  ]
  Each term is (\ge 0) (PSD), so the only way their sum is 0 is if
  [
  v^\top Xv=0 \quad\text{and}\quad v^\top Yv=0.
  ]
  By the lemma above, (Xv=0) and (Yv=0). Hence (v\in\mathcal N(X)\cap\mathcal N(Y)).

So equality holds.

---

## 3.4 Turn nullspace intersection into a rank inequality

Let (n) be the matrix size. Use rank-nullity:
[
\mathrm{rank}(X)=n-\dim\mathcal N(X).
]

From (\mathcal N(X+Y)=\mathcal N(X)\cap\mathcal N(Y)), we get
[
\dim\mathcal N(X+Y)=\dim(\mathcal N(X)\cap\mathcal N(Y))
\le \min{\dim\mathcal N(X),\dim\mathcal N(Y)}.
]
Subtract from (n):
[
\mathrm{rank}(X+Y)
= n-\dim\mathcal N(X+Y)
\ge n-\min{\dim\mathcal N(X),\dim\mathcal N(Y)}
= \max{\mathrm{rank}(X),\mathrm{rank}(Y)}.
]
In particular,
[
\mathrm{rank}(X+Y)\ge \min{\mathrm{rank}(X),\mathrm{rank}(Y)},
]
which is the inequality the book displays.

Again: the book states a weaker inequality, but the PSD structure actually gives a stronger one.

---

## 3.5 Quasiconcavity via modified Jensen

Take (X,Y\succeq 0) and (\theta\in(0,1)). Consider
[
Z=\theta X+(1-\theta)Y.
]
Scaling by a positive constant doesn’t change rank:
[
\mathrm{rank}(Z)=\mathrm{rank}!\left(\frac{1}{\theta}Z\right)
=\mathrm{rank}!\left(X+\frac{1-\theta}{\theta}Y\right).
]
Let (t=\frac{1-\theta}{\theta}>0). Then (tY\succeq 0), and from the sum inequality:
[
\mathrm{rank}(X+tY)\ge \min{\mathrm{rank}(X),\mathrm{rank}(tY)}.
]
But (\mathrm{rank}(tY)=\mathrm{rank}(Y)) for (t>0). So
[
\mathrm{rank}(\theta X+(1-\theta)Y)\ge \min{\mathrm{rank}(X),\mathrm{rank}(Y)}.
]
That is exactly the modified Jensen inequality, hence **rank is quasiconcave on (\mathbf S_+^n)**.

(Endpoints (\theta=0,1) are trivial.)

---

## 3.6 Relation to Example 3.35: (\mathrm{rank}(\mathrm{diag}(x))=\mathrm{card}(x)) for (x\ge 0)

If (x\ge 0), then (\mathrm{diag}(x)\succeq 0).
A diagonal matrix has rank equal to the number of nonzero diagonal entries, i.e.
[
\mathrm{rank}(\mathrm{diag}(x)) = |{i: x_i\neq 0}| = \mathrm{card}(x).
]
So the rank example is literally the matrix generalization of cardinality on the PSD diagonal cone.

---

# 4) What’s really going on (the moral)

Both examples exploit the same structural fact:

* On (\mathbb R_+^n), **no cancellation**: if (\theta x+(1-\theta)y=0) in a coordinate with (\theta,1-\theta>0), then both entries were 0.
* On (\mathbf S_+^n), **no cancellation in quadratic forms**: if (v^\top(\theta X+(1-\theta)Y)v=0), then both quadratic forms were 0, forcing (Xv=Yv=0).

So **support** (for vectors) and **nullspace** (for PSD matrices) behave monotonically under convex combinations, and that monotonicity is exactly quasiconcavity.

If you want the next layer of brutality: we can explicitly characterize the **superlevel sets** ({x\ge 0:\mathrm{card}(x)\ge k}) and ({X\succeq 0:\mathrm{rank}(X)\ge k}) and prove their convexity directly (it becomes a clean “intersection-of-nullspaces” geometric argument).

## Response:
Thought for 17s

Alright—**Example 3.35 only**, same “from bedrock” treatment, with **every step explained**, **all lemmas proved**, plus **alternative proofs** and **failure modes**.

* * *

Example 3.35 — Cardinality is quasiconcave on  $\mathbb{R}_+^n$ 
================================================================

We study the function

$$
f(x)=\mathrm{card}(x)\qquad \text{on }\mathbb{R}_+^n:=\{x\in\mathbb{R}^n:\ x_i\ge 0\ \forall i\}.
$$

The book’s claim:

 $$
\boxed{\ \mathrm{card}(x)\ \text{is quasiconcave on }\mathbb{R}_+^n\ }.
$$

The _one_ structural reason it works is: **no cancellation** when you take convex combinations of nonnegative vectors.

* * *

0) Definitions (no skipping)
----------------------------

### 0.1 Support

For any  $x\in\mathbb{R}^n$ ,

$$
\mathrm{supp}(x):=\{i\in\{1,\dots,n\}: x_i\neq 0\}.
$$

On  $\mathbb{R}_+^n$ , “ $x_i\neq 0$ ” is the same as “ $x_i>0$ ” (because coordinates can’t be negative).

### 0.2 Cardinality

$$
\mathrm{card}(x):=|\mathrm{supp}(x)|,
$$

the number of nonzero coordinates.

Example: if  $x=(3,0,0,5)$ , then  $\mathrm{supp}(x)=\{1,4\}$ ,  $\mathrm{card}(x)=2$ .

### 0.3 Quasiconcavity (two equivalent definitions)

A function  $f$  is **quasiconcave** if **every upper level set**

$$
U_\alpha:=\{x\in\mathrm{dom}f:\ f(x)\ge \alpha\}
$$

is convex.

Equivalent “modified Jensen inequality”:

 $$
\boxed{\ f(\theta x+(1-\theta)y)\ \ge\ \min\{f(x),f(y)\}\quad \forall x,y,\ \forall\theta\in[0,1].\ }
$$

I’ll prove this equivalence (quickly but fully) because we’ll use it as the proof engine.

* * *

1) Proof that “modified Jensen” ⇔ “upper level sets convex”
-----------------------------------------------------------

### (⇒) Upper level sets convex ⇒ modified Jensen

Assume every  $U_\alpha$  is convex. Take any  $x,y$  and  $\theta\in[0,1]$ . Let

$$
a:=\min\{f(x),f(y)\}.
$$

Then  $f(x)\ge a$  and  $f(y)\ge a$ , i.e.  $x,y\in U_a$ . Since  $U_a$  is convex,

$$
\theta x+(1-\theta)y\in U_a,
$$

meaning

$$
f(\theta x+(1-\theta)y)\ge a=\min\{f(x),f(y)\}.
$$

Done.

### (⇐) Modified Jensen ⇒ upper level sets convex

Assume modified Jensen holds. Fix any  $\alpha$ . Take any  $x,y\in U_\alpha$ . Then  $f(x)\ge \alpha$  and  $f(y)\ge \alpha$ , so

$$
\min\{f(x),f(y)\}\ge \alpha.
$$

Modified Jensen gives

$$
f(\theta x+(1-\theta)y)\ge \min\{f(x),f(y)\}\ge \alpha,
$$

so  $\theta x+(1-\theta)y\in U_\alpha$ . Thus  $U_\alpha$  is convex.

So: **to prove quasiconcavity, it suffices to prove modified Jensen.**

* * *

2) The “no cancellation” lemma on  $\mathbb{R}_+^n$  (the real core)
--------------------------------------------------------------------

Everything reduces to a one-dimensional fact.

### Lemma (scalar no-cancellation)

Let  $a\ge 0$ ,  $b\ge 0$ , and  $\theta\in(0,1)$ . Then

$$
\theta a+(1-\theta)b=0\quad\Longleftrightarrow\quad a=0\ \text{and}\ b=0.
$$

#### Proof

*   (**If**) If  $a=b=0$ , then  $\theta a+(1-\theta)b=0$ . Trivial.
*   (**Only if**) Suppose  $\theta a+(1-\theta)b=0$ . Since  $a,b\ge 0$  and  $\theta,(1-\theta)>0$ , we have  $\theta a\ge 0$  and  $(1-\theta)b\ge 0$ .  
    A sum of two nonnegative numbers equals 0 **only if each term is 0**. So  $\theta a=0$  and  $(1-\theta)b=0$ . Because  $\theta>0$  and  $1-\theta>0$ , this implies  $a=0$  and  $b=0$ . □

That’s it. Now we lift it coordinatewise to vectors.

* * *

3) Support of a convex combination on  $\mathbb{R}_+^n$ 
--------------------------------------------------------

Let  $x,y\in\mathbb{R}_+^n$  and  $\theta\in(0,1)$ . Define

$$
z=\theta x+(1-\theta)y.
$$

### Claim

 $$
\boxed{\ \mathrm{supp}(z)=\mathrm{supp}(x)\cup \mathrm{supp}(y)\ }.
$$

#### Proof (coordinate-by-coordinate, no skipping)

Fix an index  $i\in\{1,\dots,n\}$ . Look at the scalar relation:

$$
z_i=\theta x_i+(1-\theta)y_i.
$$

Because  $x_i,y_i\ge 0$ , we can use the scalar lemma.

*   If  $i\in \mathrm{supp}(x)\cup\mathrm{supp}(y)$ , then **at least one** of  $x_i,y_i$  is nonzero, i.e.  $x_i>0$  or  $y_i>0$ .  
    Then  $z_i=\theta x_i+(1-\theta)y_i>0$  (sum of two nonnegative terms, at least one strictly positive, with positive weights). Hence  $z_i\neq 0$ , so  $i\in\mathrm{supp}(z)$ .
*   If  $i\notin \mathrm{supp}(x)\cup\mathrm{supp}(y)$ , then  $x_i=0$  and  $y_i=0$ . Then  $z_i=0$ , so  $i\notin\mathrm{supp}(z)$ .

So membership in  $\mathrm{supp}(z)$  is **exactly** membership in  $\mathrm{supp}(x)\cup\mathrm{supp}(y)$ . Therefore the sets are equal. □

> Edge cases:  
> • If  $\theta=0$ , then  $z=y$  and  $\mathrm{supp}(z)=\mathrm{supp}(y)$ .  
> • If  $\theta=1$ , then  $z=x$ .  
> The union identity is guaranteed exactly for  $\theta\in(0,1)$ . (That’s why we handled endpoints separately later.)

* * *

4) Convert support identity into the quasiconcavity inequality
--------------------------------------------------------------

Using the support identity:

$$
\mathrm{card}(z)=|\mathrm{supp}(z)| =|\mathrm{supp}(x)\cup\mathrm{supp}(y)|.
$$

Now use basic set-size facts:

*   For any sets  $A,B$ ,
    $$
    |A\cup B|\ge |A|\quad\text{and}\quad |A\cup B|\ge |B|.
    $$
    So
    $$
    |A\cup B|\ge \max\{|A|,|B|\}.
    $$
*   And always  $\max\{u,v\}\ge \min\{u,v\}$ .

Apply with  $A=\mathrm{supp}(x)$ ,  $B=\mathrm{supp}(y)$ :

$$
\mathrm{card}(z) =|\mathrm{supp}(x)\cup\mathrm{supp}(y)| \ge \max\{\mathrm{card}(x),\mathrm{card}(y)\} \ge \min\{\mathrm{card}(x),\mathrm{card}(y)\}.
$$

So we have shown:

 $$
\boxed{\ \mathrm{card}(\theta x+(1-\theta)y)\ \ge\ \min\{\mathrm{card}(x),\mathrm{card}(y)\}\quad \forall x,y\in\mathbb{R}_+^n,\ \forall\theta\in[0,1].\ }
$$

That is exactly the modified Jensen inequality for quasiconcavity. Therefore:

 $$
\boxed{\ \mathrm{card}(\cdot)\text{ is quasiconcave on }\mathbb{R}_+^n.\ }
$$

* * *

5) Alternative proof (directly from upper level sets)
=====================================================

Sometimes it’s nice to prove quasiconcavity using the definition: “upper level sets are convex.”

### Step 1: understand what the upper level sets look like

Since  $\mathrm{card}(x)\in\{0,1,\dots,n\}$ , the only meaningful thresholds are integers. For any real  $\alpha$ , define  $k=\lceil \alpha\rceil$ . Then

$$
\{x:\mathrm{card}(x)\ge \alpha\}=\{x:\mathrm{card}(x)\ge k\}.
$$

So we can focus on sets

$$
U_k := \{x\in\mathbb{R}_+^n:\mathrm{card}(x)\ge k\}.
$$

### Step 2: prove  $U_k$  is convex

Take  $x,y\in U_k$ . That means  $\mathrm{card}(x)\ge k$  and  $\mathrm{card}(y)\ge k$ .  
Let  $z=\theta x+(1-\theta)y$  with  $\theta\in(0,1)$ . From the support identity,

$$
\mathrm{card}(z)=|\mathrm{supp}(x)\cup\mathrm{supp}(y)|\ge \max\{\mathrm{card}(x),\mathrm{card}(y)\}\ge k.
$$

So  $z\in U_k$ . Endpoints  $\theta=0,1$  are trivial. Hence  $U_k$  is convex.

Since all upper level sets are convex,  $\mathrm{card}$  is quasiconcave. □

This proof is basically the same logic but phrased “set-first.”

* * *

6) Why it fails on all of  $\mathbb{R}^n$ : cancellation destroys support
=========================================================================

On  $\mathbb{R}^n$ , coordinates can be negative, so  $\theta x_i+(1-\theta)y_i$  can become 0 even if both are nonzero.

**One-dimensional counterexample:**

$$
x=1,\qquad y=-1,\qquad \theta=\tfrac12.
$$

Then  $\mathrm{card}(x)=\mathrm{card}(y)=1$ , but

$$
\tfrac12 x+\tfrac12 y = 0 \quad\Rightarrow\quad \mathrm{card}(0)=0,
$$

so

$$
0 \not\ge \min\{1,1\}=1.
$$

Modified Jensen fails ⇒ not quasiconcave on  $\mathbb{R}^n$ .

* * *

7) Extra facts (useful “don’t get tricked” notes)
=================================================

### 7.1 The inequality is actually stronger on  $\mathbb{R}_+^n$ 

For  $\theta\in(0,1)$ ,

$$
\mathrm{card}(\theta x+(1-\theta)y)\ \ge\ \max\{\mathrm{card}(x),\mathrm{card}(y)\}.
$$

So convex combinations can only keep or increase the number of nonzeros (never decrease).

### 7.2 Not quasiconvex (even on  $\mathbb{R}_+^n$ )

Lower level sets are typically not convex. Example in  $\mathbb{R}_+^2$ :

$$
x=(1,0),\quad y=(0,1).
$$

Both have  $\mathrm{card}=1$ , so they belong to  $\{x:\mathrm{card}(x)\le 1\}$ .  
But their average is  $(1/2,1/2)$ , which has  $\mathrm{card}=2$ , not  $\le 1$ .  
So the lower level set is not convex ⇒ not quasiconvex.

### 7.3 Multi-point generalization (nice and clean)

If  $x^{(1)},\dots,x^{(m)}\in\mathbb{R}_+^n$  and weights  $\theta_j>0$ ,  $\sum_j\theta_j=1$ , then

$$
\mathrm{supp}\Big(\sum_j\theta_j x^{(j)}\Big)=\bigcup_j \mathrm{supp}(x^{(j)}),
$$

so cardinality is at least the maximum cardinality among them.

* * *

If you want, we can now do the **same brutality** for **Example 3.36 (rank on  $\mathbf S_+^n$ )**, and I’ll explicitly mirror the scalar lemma with the PSD lemma (“ $v^\top Xv=0\Rightarrow Xv=0$ ”), so the analogy becomes impossible to unsee.

## Prompt:
3.36

## Response:
Thought for 22s

Alright. **Example 3.36 —  $\mathrm{rank}(X)$  is quasiconcave on  $\mathbf S_+^n$ **, from bedrock, _every step explicit_, with **direct proofs** of the lemmas and **nice alternative proofs**.

* * *

Example 3.36 — Rank is quasiconcave on  $\mathbf S_+^n$ 
========================================================

Statement
---------

Let  $\mathbf S_+^n$  be the cone of **symmetric positive semidefinite (PSD)** matrices:

$$
X\succeq 0 \quad\Longleftrightarrow\quad v^\top Xv\ge 0\ \ \forall v\in\mathbb R^n.
$$

Define

$$
f(X)=\mathrm{rank}(X).
$$

Claim:

 $$
\boxed{\ \mathrm{rank}(\cdot)\ \text{is quasiconcave on }\mathbf S_+^n\ }.
$$

By the “modified Jensen” characterization of quasiconcavity (proved in your 3.35 writeup), it suffices to prove:

 $$
\boxed{\ \mathrm{rank}(\theta X+(1-\theta)Y)\ \ge\ \min\{\mathrm{rank}(X),\mathrm{rank}(Y)\}\quad \forall X,Y\succeq 0,\ \theta\in[0,1].\ }
$$

We will actually prove something **stronger**:

 $$
\boxed{\ \mathrm{rank}(X+Y)\ \ge\ \max\{\mathrm{rank}(X),\mathrm{rank}(Y)\}\quad \forall X,Y\succeq 0.\ }
$$

From that, the Jensen-type inequality follows immediately for convex combinations.

* * *

0) Definitions (rank, nullspace, PSD)
=====================================

0.1 Nullspace and range
-----------------------

For a matrix  $X\in\mathbb R^{n\times n}$ :

*   **Nullspace**
    $$
    \mathcal N(X):=\{v\in\mathbb R^n:\ Xv=0\}.
    $$
*   **Range / column space**
    $$
    \mathcal R(X):=\{Xv:\ v\in\mathbb R^n\}.
    $$

Both are subspaces of  $\mathbb R^n$ .

0.2 Rank-nullity (dimension theorem)
------------------------------------

For any linear map  $X:\mathbb R^n\to\mathbb R^n$ ,

 $$
\boxed{\ \mathrm{rank}(X)=\dim\mathcal R(X)=n-\dim\mathcal N(X).\ }
$$

### Proof (short but real)

Pick a basis of  $\mathcal N(X)$ , extend it to a basis of  $\mathbb R^n$ . The images under  $X$  of the added basis vectors form a basis of  $\mathcal R(X)$ . Counting dimensions yields  
 $\dim\mathcal N(X)+\dim\mathcal R(X)=n$ . So  $\mathrm{rank}(X)=n-\dim\mathcal N(X)$ . □

0.3 Scaling doesn’t change rank (for nonzero scalars)
-----------------------------------------------------

If  $t\neq 0$ ,

 $$
\boxed{\ \mathrm{rank}(tX)=\mathrm{rank}(X).\ }
$$

Because  $tXv=0 \iff Xv=0$ , so  $\mathcal N(tX)=\mathcal N(X)$ , hence ranks match by rank-nullity.

* * *

1) The PSD “no cancellation” lemma (crucial)
============================================

Lemma 1
-------

If  $X\succeq 0$  and  $v^\top Xv=0$ , then

 $$
\boxed{\ Xv=0.\ }
$$

This is the matrix analogue of: “if nonnegative numbers sum to 0, each must be 0.”

I’ll prove it **two ways**.

* * *

Proof A (via spectral theorem + square root)
--------------------------------------------

### Step A1: spectral theorem for symmetric matrices (what we need)

For symmetric  $X$ , there exists an orthonormal matrix  $Q$  and a real diagonal  $\Lambda$  such that

$$
X = Q\Lambda Q^\top,\quad \Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_n).
$$

Moreover,  $X\succeq 0$  implies  $\lambda_i\ge 0$  for all  $i$ .  
(Reason: take eigenvector  $q_i$ :  $q_i^\top X q_i = \lambda_i \|q_i\|^2 = \lambda_i \ge 0$ .)

### Step A2: define the PSD square root explicitly

Define

$$
\Lambda^{1/2}=\mathrm{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_n}), \qquad X^{1/2}:=Q\Lambda^{1/2}Q^\top.
$$

Then

$$
X^{1/2}X^{1/2} =Q\Lambda^{1/2}Q^\top Q\Lambda^{1/2}Q^\top =Q\Lambda Q^\top =X.
$$

So this really is a square root.

### Step A3: rewrite the quadratic form as a norm square

Compute:

$$
v^\top Xv = v^\top X^{1/2}X^{1/2}v = (X^{1/2}v)^\top (X^{1/2}v) = \|X^{1/2}v\|_2^2.
$$

A squared norm is  $\ge 0$  and equals 0 iff the vector is 0. So:

$$
v^\top Xv = 0 \iff \|X^{1/2}v\|_2^2=0 \iff X^{1/2}v=0.
$$

Then

$$
Xv = X^{1/2}(X^{1/2}v)=X^{1/2}\cdot 0 = 0.
$$

Done. □

* * *

Proof B (via Cholesky / Gram factorization)
-------------------------------------------

A standard characterization of PSD matrices is:

$$
X\succeq 0 \quad\Longleftrightarrow\quad \exists B\ \text{s.t.}\ X=B^\top B.
$$

(You can take  $B=X^{1/2}$  from Proof A, or a Cholesky factor when  $X$  is PD.)

Then

$$
v^\top Xv = v^\top B^\top B v = \|Bv\|_2^2.
$$

If  $v^\top Xv=0$ , then  $\|Bv\|^2=0\Rightarrow Bv=0$ . Hence

$$
Xv=B^\top(Bv)=B^\top 0=0.
$$

Done. □

* * *

2) Nullspace of a PSD sum = intersection (this is the “no cancellation” upgrade)
================================================================================

Let  $X,Y\succeq 0$ .

Lemma 2
-------

 $$
\boxed{\ \mathcal N(X+Y)=\mathcal N(X)\cap \mathcal N(Y).\ }
$$

### Proof (both containments, fully explicit)

#### ( $\subseteq$ ) Take  $v\in\mathcal N(X+Y)$ . Show  $v\in\mathcal N(X)\cap\mathcal N(Y)$ .

 $v\in\mathcal N(X+Y)$  means:

$$
(X+Y)v=0.
$$

Left-multiply by  $v^\top$ :

$$
0 = v^\top (X+Y)v = v^\top Xv + v^\top Yv.
$$

Now:

*    $v^\top Xv\ge 0$  because  $X\succeq 0$ ,
*    $v^\top Yv\ge 0$  because  $Y\succeq 0$ .

A sum of two nonnegative real numbers equals 0 **only if each is 0**, so:

$$
v^\top Xv = 0,\qquad v^\top Yv=0.
$$

Apply Lemma 1 to each:

$$
Xv=0,\qquad Yv=0.
$$

So  $v\in\mathcal N(X)\cap\mathcal N(Y)$ .

#### ( $\supseteq$ ) Take  $v\in\mathcal N(X)\cap\mathcal N(Y)$ . Show  $v\in\mathcal N(X+Y)$ .

If  $Xv=0$  and  $Yv=0$ , then

$$
(X+Y)v=Xv+Yv=0+0=0,
$$

so  $v\in\mathcal N(X+Y)$ .

Both containments hold, hence equality. □

* * *

3) Turn nullspace intersection into a rank inequality
=====================================================

From rank-nullity:

$$
\mathrm{rank}(X)=n-\dim\mathcal N(X).
$$

From Lemma 2:

$$
\mathcal N(X+Y)=\mathcal N(X)\cap\mathcal N(Y).
$$

Now use a very simple dimension fact:

Fact
----

If  $U\cap W \subseteq U$ , then  $\dim(U\cap W)\le \dim(U)$ . Similarly  $\dim(U\cap W)\le \dim(W)$ .  
Therefore

$$
\dim(U\cap W)\le \min\{\dim U,\dim W\}.
$$

Apply with  $U=\mathcal N(X)$ ,  $W=\mathcal N(Y)$ :

$$
\dim\mathcal N(X+Y)=\dim(\mathcal N(X)\cap\mathcal N(Y)) \le \min\{\dim\mathcal N(X),\dim\mathcal N(Y)\}.
$$

Subtract from  $n$ :

$$
\mathrm{rank}(X+Y) = n-\dim\mathcal N(X+Y) \ge n-\min\{\dim\mathcal N(X),\dim\mathcal N(Y)\} = \max\{n-\dim\mathcal N(X),\,n-\dim\mathcal N(Y)\} = \max\{\mathrm{rank}(X),\mathrm{rank}(Y)\}.
$$

So we have the strong monotonicity:

 $$
\boxed{\ \mathrm{rank}(X+Y)\ \ge\ \max\{\mathrm{rank}(X),\mathrm{rank}(Y)\}\quad (X,Y\succeq 0).\ }
$$

In particular it implies the weaker inequality the book writes:

$$
\mathrm{rank}(X+Y)\ge \min\{\mathrm{rank}(X),\mathrm{rank}(Y)\}.
$$

* * *

4) Quasiconcavity via “modified Jensen” (convex combinations)
=============================================================

Let  $X,Y\succeq 0$  and  $\theta\in(0,1)$ . Define

$$
Z=\theta X+(1-\theta)Y.
$$

### Step 1: remove the scalar  $\theta$  using rank invariance

Since  $\theta>0$ ,

$$
\mathrm{rank}(Z)=\mathrm{rank}\!\left(\frac{1}{\theta}Z\right) =\mathrm{rank}\!\left(X+\frac{1-\theta}{\theta}Y\right).
$$

Let  $t=\frac{1-\theta}{\theta}>0$ . Then  $tY\succeq 0$ .

### Step 2: apply the rank-of-sum inequality

Using the result from Section 3:

$$
\mathrm{rank}(X+tY)\ge \max\{\mathrm{rank}(X),\mathrm{rank}(tY)\}.
$$

But  $\mathrm{rank}(tY)=\mathrm{rank}(Y)$  (scaling doesn’t change rank). Thus:

$$
\mathrm{rank}(Z)\ge \max\{\mathrm{rank}(X),\mathrm{rank}(Y)\}\ge \min\{\mathrm{rank}(X),\mathrm{rank}(Y)\}.
$$

This is exactly the modified Jensen inequality for quasiconcavity. Therefore:

 $$
\boxed{\ \mathrm{rank}(\cdot)\ \text{is quasiconcave on }\mathbf S_+^n.\ }
$$

Endpoints  $\theta=0,1$  are trivial.

* * *

5) Alternative proof (more “constructive”): factorization + stacking columns
============================================================================

This proof avoids nullspaces entirely and feels very concrete.

### Step 1: PSD factorization

If  $X\succeq 0$ , there exists  $B$  such that

$$
X=BB^\top.
$$

Similarly  $Y=CC^\top$ .

Also note:

$$
\mathrm{rank}(BB^\top)=\mathrm{rank}(B).
$$

(Reason:  $\mathcal N(BB^\top)=\mathcal N(B^\top)$ , and ranks match; or use SVD.)

### Step 2: write the sum as one big Gram matrix

$$
X+Y = BB^\top + CC^\top = \begin{bmatrix}B & C\end{bmatrix} \begin{bmatrix}B & C\end{bmatrix}^\top.
$$

Let  $D=[B\ \ C]$ . Then  $X+Y=DD^\top$ , so

$$
\mathrm{rank}(X+Y)=\mathrm{rank}(DD^\top)=\mathrm{rank}(D).
$$

### Step 3: stacking columns can only increase rank

The column space of  $B$  is contained in the column space of  $[B\ C]$ . So

$$
\mathrm{rank}([B\ C])\ge \mathrm{rank}(B).
$$

Similarly  $\mathrm{rank}([B\ C])\ge \mathrm{rank}(C)$ . Hence

$$
\mathrm{rank}(X+Y)=\mathrm{rank}([B\ C])\ge \max\{\mathrm{rank}(B),\mathrm{rank}(C)\} =\max\{\mathrm{rank}(X),\mathrm{rank}(Y)\}.
$$

Same conclusion, different route.

* * *

6) Why PSD matters: it fails on general symmetric matrices (cancellation)
=========================================================================

If matrices are not PSD, “quadratic forms can cancel,” and the key Lemma 1 fails.

Example in  $\mathbf S^1$  (just numbers):

$$
X=[1],\quad Y=[-1].
$$

Then  $\mathrm{rank}(X)=\mathrm{rank}(Y)=1$ , but

$$
\frac12 X+\frac12 Y = [0] \quad\Rightarrow\quad \mathrm{rank}=0,
$$

violating the modified Jensen inequality. So rank is **not** quasiconcave on all symmetric matrices—PSD is essential.

* * *

7) Connection to Example 3.35 (diagonal PSD case)
=================================================

If  $x\in\mathbb R_+^n$ , then  $\mathrm{diag}(x)\succeq 0$  and

$$
\mathrm{rank}(\mathrm{diag}(x))=\#\{i:\ x_i\neq 0\}=\mathrm{card}(x).
$$

So Example 3.35 is literally the diagonal slice of Example 3.36.

* * *

If you want the “next layer of brutality”: we can explicitly describe the **upper level sets**

$$
\{X\succeq 0:\ \mathrm{rank}(X)\ge r\}
$$

and prove their convexity directly via nullspace behavior (it becomes a clean geometric statement about intersections of nullspaces under convex combinations).

## Prompt:
next layer!

## Response:
Thought for 27s

Cool — “next layer” = we stop proving _quasiconcavity_ indirectly and instead **grab the upper level sets by the collar**, **characterize them**, and **prove they’re convex directly**. Then we’ll add the deeper geometric picture: **faces of the PSD cone**, **range vs nullspace**, and **multi-point (many matrices) versions**.

* * *

Next layer for Example 3.36
===========================

1) What are the upper level sets of rank on  $\mathbf S_+^n$ ?
--------------------------------------------------------------

Since rank takes integer values  $0,1,\dots,n$ , it’s enough to study, for each integer  $r\in\{0,\dots,n\}$ ,

$$
U_r \;:=\;\{\,X\in\mathbf S_+^n:\ \mathrm{rank}(X)\ge r\,\}.
$$

Quasiconcavity is _equivalent_ to: **each  $U_r$  is convex**.

So the next layer is: prove

 $$
\boxed{\ X,Y\in U_r,\ \theta\in[0,1] \ \Rightarrow\ \theta X+(1-\theta)Y\in U_r.\ }
$$

* * *

2) A sharper structural identity for convex combinations (not just sums)
------------------------------------------------------------------------

Earlier we proved for sums:

$$
\mathcal N(X+Y)=\mathcal N(X)\cap\mathcal N(Y)\quad(X,Y\succeq 0).
$$

Here’s the version that matches convex combinations exactly.

### Lemma A (nullspace of a positive-weight combination)

Let  $X_1,\dots,X_m\succeq 0$  and weights  $\theta_i>0$  with  $\sum_{i=1}^m\theta_i=1$ . Define

$$
Z := \sum_{i=1}^m \theta_i X_i.
$$

Then

 $$
\boxed{\ \mathcal N(Z)=\bigcap_{i=1}^m \mathcal N(X_i).\ }
$$

#### Proof (every step)

**(⊇)** If  $v\in\bigcap_i \mathcal N(X_i)$ , then each  $X_i v=0$ . Hence

$$
Zv=\sum_i \theta_i X_i v=\sum_i \theta_i\cdot 0=0,
$$

so  $v\in\mathcal N(Z)$ .

**(⊆)** If  $v\in\mathcal N(Z)$ , then  $Zv=0$ . Left-multiply by  $v^\top$ :

$$
0 = v^\top Zv = v^\top\Big(\sum_i \theta_i X_i\Big)v = \sum_i \theta_i\, v^\top X_i v.
$$

Each term  $v^\top X_i v\ge 0$  because  $X_i\succeq 0$ . Each weight  $\theta_i>0$ . A sum of nonnegative numbers with positive weights equals  $0$  **only if each number is  $0$ **:

$$
v^\top X_i v =0\quad\forall i.
$$

Now use the PSD no-cancellation lemma (proved earlier):

$$
X_i\succeq 0,\ v^\top X_i v=0 \Rightarrow X_i v=0.
$$

So  $v\in\mathcal N(X_i)$  for every  $i$ , i.e.  $v\in\bigcap_i\mathcal N(X_i)$ .

So equality holds. □

**Key point:** the condition  $\theta_i>0$  matters. If some  $\theta_i=0$ , that matrix simply doesn’t participate, and you should drop it from the intersection.

* * *

3) Direct convexity of the upper level sets  $U_r$ 
---------------------------------------------------

Now we prove convexity of  $U_r$  _directly_ using nullspaces.

### Step 1: translate “rank ≥ r” into “nullspace dimension ≤ n−r”

Rank-nullity says:

$$
\mathrm{rank}(X)=n-\dim\mathcal N(X).
$$

So

$$
\mathrm{rank}(X)\ge r \iff n-\dim\mathcal N(X)\ge r \iff \dim\mathcal N(X)\le n-r.
$$

Thus

$$
U_r=\{X\succeq 0:\ \dim\mathcal N(X)\le n-r\}.
$$

### Step 2: show a convex combination can’t _increase_ nullspace dimension

Take  $X,Y\in U_r$ , so

$$
\dim\mathcal N(X)\le n-r,\qquad \dim\mathcal N(Y)\le n-r.
$$

Let  $Z=\theta X+(1-\theta)Y$  with  $\theta\in(0,1)$ . By Lemma A (with  $m=2$ ):

$$
\mathcal N(Z)=\mathcal N(X)\cap\mathcal N(Y).
$$

Intersections of subspaces can only get _smaller_ (never larger), meaning:

$$
\dim(\mathcal N(X)\cap\mathcal N(Y))\le \min\{\dim\mathcal N(X),\dim\mathcal N(Y)\}.
$$

Therefore

$$
\dim\mathcal N(Z) \le \min\{\dim\mathcal N(X),\dim\mathcal N(Y)\} \le n-r.
$$

So  $\dim\mathcal N(Z)\le n-r$ , which means  $\mathrm{rank}(Z)\ge r$ , i.e.  $Z\in U_r$ .

Endpoints  $\theta=0,1$  are trivial.

So:

$$
\boxed{U_r\ \text{is convex for every }r,\ \text{hence rank is quasiconcave on }\mathbf S_+^n.}
$$

That’s the “upper level sets” proof in its cleanest form.

* * *

4) Even deeper: range can only grow, and you can prove it cleanly
=================================================================

For symmetric matrices, there is a tight relationship:

$$
\mathcal R(X)=\mathcal N(X)^\perp.
$$

### Why  $\mathcal R(X)=\mathcal N(X)^\perp$  for symmetric  $X$ 

*   Always:  $\mathcal R(X)\subseteq \mathcal N(X)^\perp$ , because if  $u=Xw$  and  $v\in\mathcal N(X)$ , then  $u^\top v = (Xw)^\top v = w^\top X^\top v = w^\top Xv = 0$ .
*   Dimensions match for symmetric  $X$ :  $\dim\mathcal R(X)=\mathrm{rank}(X)=n-\dim\mathcal N(X)=\dim(\mathcal N(X)^\perp)$ . Inclusion + equal dimension ⇒ equality.

Now apply orthogonal complements to Lemma A (two-matrix case):

$$
\mathcal N(\theta X+(1-\theta)Y)=\mathcal N(X)\cap\mathcal N(Y)
$$

Take orthogonal complements:

$$
\mathcal R(\theta X+(1-\theta)Y) = \mathcal N(\theta X+(1-\theta)Y)^\perp = (\mathcal N(X)\cap\mathcal N(Y))^\perp = \mathcal N(X)^\perp + \mathcal N(Y)^\perp = \mathcal R(X)+\mathcal R(Y).
$$

So you get the very geometric identity:

 $$
\boxed{\ \mathcal R(\theta X+(1-\theta)Y)=\mathcal R(X)+\mathcal R(Y)\quad(\theta\in(0,1),\ X,Y\succeq 0).\ }
$$

**Interpretation:** PSD convex combinations can’t “lose directions.” The range subspace is literally the sum of the ranges.

This is the matrix analogue of Example 3.35’s “support union.”

* * *

5) Geometric picture: faces of the PSD cone (why this is really about faces)
============================================================================

The PSD cone  $\mathbf S_+^n$  has **faces** indexed by subspaces.

For any subspace  $W\subseteq\mathbb R^n$ , define the face

$$
F_W := \{X\succeq 0:\ \mathcal R(X)\subseteq W\}.
$$

Equivalently (using  $\mathcal R(X)=\mathcal N(X)^\perp$ ):

$$
\mathcal R(X)\subseteq W \iff W^\perp \subseteq \mathcal N(X).
$$

So you can also write:

$$
F_W=\{X\succeq 0:\ W^\perp\subseteq \mathcal N(X)\}.
$$

Now notice:

*   “Low-rank” PSD matrices live on **lower-dimensional faces** (they have big nullspaces).
*   When you take convex combinations of PSD matrices, the nullspace becomes an intersection, so you move to a **smaller nullspace**, i.e. you move toward **larger faces / interior**.

This is the cone-geometry version of “no cancellation.”

* * *

6) Subtle but important: these convex upper level sets are generally **not closed**
===================================================================================

Rank can **drop in the limit** (but cannot jump up).

Example: in  $\mathbf S_+^2$ ,

$$
X_\varepsilon=\begin{pmatrix}1&0\\0&\varepsilon\end{pmatrix}\succeq 0.
$$

For every  $\varepsilon>0$ ,  $\mathrm{rank}(X_\varepsilon)=2$ . But as  $\varepsilon\to 0$ ,

$$
X_\varepsilon \to \begin{pmatrix}1&0\\0&0\end{pmatrix},
$$

whose rank is  $1$ . So  $U_2=\{X\succeq 0:\mathrm{rank}(X)\ge 2\}$  is **not closed** (it’s the interior of the cone, essentially).

That’s totally fine: quasiconcavity only asks “convex,” not “closed.”

* * *

7) Quick contrast: why the _lower_ level sets are not convex
============================================================

To make sure you don’t accidentally assume rank is quasiconvex:

Take

$$
X=e_1e_1^\top,\quad Y=e_2e_2^\top \quad(\text{both PSD, rank }1).
$$

Then

$$
\frac12 X+\frac12 Y=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}
$$

has rank  $2$ . So the set  $\{X\succeq 0:\mathrm{rank}(X)\le 1\}$  is **not convex**.

So rank is quasiconcave (upper sets convex), but not quasiconvex.

* * *

If you want to go _one notch deeper still_, the next “layer” is to connect this to **nuclear norm / trace** as the convex surrogate for rank, and show how PSD structure makes  $\mathrm{tr}(X)$  the tightest convex proxy on certain normalized slices (classic convex relaxation story).

## Prompt:
Expample 3.20 from below:

# BV — Problem 15, Example 3.20, Exercises 3.22–3.23

This note proves (with full chain-rule / epigraph / composition-rule detail):

* **Problem 15**: Hessian of (\log f).
* **Example 3.20**: “perspective + affine map” construction.
* **Exercise 3.23**: perspective examples.
* **Exercise 3.22**: composition-rule examples (a)–(e).

Throughout:

* Gradients (\nabla f(x)) are **column vectors**.
* Hessians (\nabla^2 f(x)) are (n\times n) symmetric matrices when (f) is (C^2).

---

## 0) Two core meta-tools

### 0.1 Convexity via epigraph

For (F: \mathbb R^k\to\mathbb R\cup{+\infty}), the **epigraph** is
[
\operatorname{epi} F = {(z,s)\in\mathbb R^k\times\mathbb R : F(z)\le s}.
]
(F) is convex (\iff\ \operatorname{epi}F) is a convex set.

### 0.2 Composition rule (monotone outer function)

Let (g: \mathbb R^m\to\mathbb R) be convex.

* If (g) is **nondecreasing in each argument** and each (u_i(x)) is convex, then (x\mapsto g(u_1(x),\dots,u_m(x))) is convex.
* If (g) is **nonincreasing in each argument** and each (u_i(x)) is concave, then the same composition is convex.

Proof idea (1D sketch, but same logic componentwise):

* convexity gives (u(\theta x+(1-\theta)y)\le \theta u(x)+(1-\theta)u(y));
* monotonicity lets you push that inequality through (g);
* convexity of (g) finishes.

We will repeatedly verify two things about outer functions:

1. convexity (via second derivative / Hessian),
2. monotonicity (sign of derivative / partials).

---

## 1) Problem 15 — Hessian of (h(x)=\log f(x))

**Given:** (f: \mathbb R^n\to\mathbb R) is smooth and strictly positive: (f(x)>0) for all (x).

**Define:** (h(x)=\ln f(x)).

**Goal:** Prove
[
\nabla^2 h(x)=\frac{1}{f(x)},\nabla^2 f(x); -; \frac{1}{f(x)^2},\nabla f(x),\nabla f(x)^\top.
]

### 1.1 Gradient of (\log f)

Start from the scalar chain rule:
[
\frac{d}{ds}\log s = \frac{1}{s}.
]
Treat (f(x)) as the inner scalar function. Then
[
\nabla h(x)= \nabla(\log f(x)) = \frac{1}{f(x)},\nabla f(x).
]
This is the multivariate chain rule: derivative of outer (\log) times gradient of inner (f).

### 1.2 Hessian of (\log f)

We differentiate (\nabla h(x)) again. Write
[
\nabla h(x)= a(x),b(x),\quad a(x)=\frac{1}{f(x)},\quad b(x)=\nabla f(x).
]
Then
[
\nabla^2 h(x) = \nabla\big(a(x)b(x)\big).
]
Use the product rule in matrix form:
[
\nabla(a b) = (\nabla a),b^\top + a,\nabla b.
]
Here:

* (\nabla a) is an (n\times 1) vector;
* (b^\top) is (1\times n);
* so ((\nabla a)b^\top) is (n\times n).
* (\nabla b) is the Jacobian of (\nabla f), i.e. (\nabla^2 f).

So
[
\nabla^2 h(x) = (\nabla a(x)), (\nabla f(x))^\top; +; a(x),\nabla^2 f(x).
]
Now compute (\nabla a). Since (a(x)=f(x)^{-1}),
[
\nabla a(x) = \nabla\big(f(x)^{-1}\big) = -f(x)^{-2},\nabla f(x).
]
(Substitute derivative of (s\mapsto s^{-1}): (-s^{-2}), times (\nabla f).)

Plug in:
[
\nabla^2 h(x)= \big(-f(x)^{-2}\nabla f(x)\big),\nabla f(x)^\top + f(x)^{-1}\nabla^2 f(x).
]
Reorder terms:
[
\boxed{\nabla^2 h(x)=\frac{1}{f(x)}\nabla^2 f(x)-\frac{1}{f(x)^2}\nabla f(x)\nabla f(x)^\top.}
]

### 1.3 Immediate corollary (useful intuition)

For any direction (v\in\mathbb R^n),
[
v^\top\nabla^2(\log f)v = \frac{v^\top\nabla^2 f,v}{f} - \frac{(v^\top\nabla f)^2}{f^2}.
]
That is exactly “curvature of (f) divided by (f)” minus a nonnegative correction term. It’s the multivariate analogue of
((\log f)'' = f''/f - (f'/f)^2).

---

## 2) Perspective transform (the engine behind Example 3.20 and 3.23)

### 2.1 Definition

Given a convex function (f: \mathbb R^m\to\mathbb R\cup{+\infty}), define its **perspective** (\tilde f) by
[
\tilde f(z,t) = t, f\left(\frac{z}{t}\right),\qquad t>0.
]
Domain: (t>0) and (z/t\in\operatorname{dom}f).

### 2.2 Theorem: perspective preserves convexity

**Claim:** If (f) is convex, then (\tilde f) is convex in ((z,t)) on its domain.

#### Proof via epigraph mapping (clean and structural)

Start with
[
\operatorname{epi} f = {(u,\alpha): f(u)\le \alpha}.
]
We want (\operatorname{epi}\tilde f):
[
\operatorname{epi}\tilde f = {(z,t,s): t>0,\ \tilde f(z,t)\le s}.
]
Unpack (\tilde f(z,t)\le s):
[
t f(z/t) \le s \iff f(z/t) \le s/t.
]
So
[
(z,t,s)\in \operatorname{epi}\tilde f
\iff t>0\ \text{and}\ \left(\frac{z}{t},\frac{s}{t}\right)\in \operatorname{epi} f.
]
Equivalently, there exist ((u,\alpha)\in\operatorname{epi}f) and (t>0) such that
[
z = t u,\qquad s = t\alpha.
]
Therefore
[
\operatorname{epi}\tilde f = {(tu,\ t,\ t\alpha): (u,\alpha)\in\operatorname{epi}f,\ t>0}.
]
Now observe:

* (\operatorname{epi}f) is convex (since (f) is convex).
* The set (\operatorname{epi}f\times \mathbb R_{++}) is convex.
* The map
  [
  T(u,\alpha,t)=(tu,\ t,\ t\alpha)
  ]
  is **affine** in ((u,\alpha,t)) (actually bilinear in notation, but as a map on the product set with scalar multiplication by (t), it is a linear map in the extended space if we view (t) as a coordinate and the output as a linear image of the cone generated by epi; concretely, convexity is preserved because this is precisely forming the cone over (\operatorname{epi} f)).

More elementary: take two points ((t_1u_1,t_1,t_1\alpha_1)) and ((t_2u_2,t_2,t_2\alpha_2)) in (\operatorname{epi}\tilde f), with ((u_i,\alpha_i)\in\operatorname{epi}f), (t_i>0). For (\theta\in[0,1]), define
[
t = \theta t_1+(1-\theta)t_2>0,
\quad \lambda = \frac{\theta t_1}{t}\in[0,1].
]
Then the convex combination equals
[
\theta(t_1u_1,t_1,t_1\alpha_1)+(1-\theta)(t_2u_2,t_2,t_2\alpha_2)=(t,u,\ t,\ t,\alpha),
]
where
[
u = \lambda u_1+(1-\lambda)u_2,\qquad \alpha = \lambda \alpha_1+(1-\lambda)\alpha_2.
]
Since ((u_i,\alpha_i)\in\operatorname{epi}f) and (\operatorname{epi}f) is convex, ((u,\alpha)\in\operatorname{epi}f). Hence the convex combination stays in (\operatorname{epi}\tilde f).

So (\operatorname{epi}\tilde f) is convex, hence (\tilde f) is convex.

---

## 3) Example 3.20 — affine perspective of a convex function

**Statement.** Suppose (f: \mathbb R^m\to\mathbb R\cup{+\infty}) is convex, and
(A\in\mathbb R^{m\times n}), (b\in\mathbb R^m), (c\in\mathbb R^n), (d\in\mathbb R).
Define
[
g(x) = (c^\top x + d), f!\left(\frac{Ax+b}{c^\top x + d}\right),
]
with domain
[
\operatorname{dom} g = {x: c^\top x + d > 0,\ (Ax+b)/(c^\top x + d)\in\operatorname{dom}f}.
]
Claim: (g) is convex.

### 3.1 Reduce to perspective + affine composition

Define the perspective (\tilde f(z,t)=t f(z/t)) for (t>0). From Section 2, (\tilde f) is convex in ((z,t)).

Now define an affine map from (x) into ((z,t)):
[
z(x)=Ax+b,\qquad t(x)=c^\top x+d.
]
Then
[
g(x) = \tilde f(z(x), t(x)).
]
Since (\tilde f) is convex and ((z(x),t(x))) is affine in (x), the composition is convex:

* Affine maps preserve convex combinations,
* Convexity inequality for (\tilde f) transfers directly.

Formally: for (x_1,x_2) in dom and (\theta\in[0,1]),
[
(z,t)(\theta x_1+(1-\theta)x_2)=\theta(z,t)(x_1)+(1-\theta)(z,t)(x_2).
]
Then convexity of (\tilde f) gives
[
g(\theta x_1+(1-\theta)x_2)=\tilde f(\theta(z_1,t_1)+(1-\theta)(z_2,t_2))
\le \theta\tilde f(z_1,t_1)+(1-\theta)\tilde f(z_2,t_2)=\theta g(x_1)+(1-\theta)g(x_2).
]
So (g) is convex.

---

## 4) Exercise 3.23 — Perspective of a function

### 4.1 (a) Prove (f(x,t)=\dfrac{|x|_p^p}{t^{p-1}}) is convex on (t>0) (for (p>1))

#### Step 1: Show (\phi(x)=|x|_p^p) is convex

[
|x|*p^p = \sum*{i=1}^n |x_i|^p.
]
For (p\ge 1), the scalar function (u\mapsto |u|^p) is convex on (\mathbb R) (second derivative exists for (u\ne 0) and the epigraph argument handles (u=0)). Sum of convex functions is convex, so (\phi) is convex.

#### Step 2: Recognize (|x|_p^p/t^{p-1}) as a perspective

Compute
[
\tilde\phi(x,t)= t,\phi(x/t) = t\sum_i |x_i/t|^p = t\sum_i \frac{|x_i|^p}{t^p} = \frac{\sum_i |x_i|^p}{t^{p-1}} = \frac{|x|_p^p}{t^{p-1}}.
]
This is exactly the perspective of (\phi).

#### Step 3: Apply “perspective preserves convexity”

Since (\phi) is convex, its perspective (\tilde\phi) is convex on (t>0).
Hence (f(x,t)=|x|_p^p/t^{p-1}) is convex on ({(x,t): t>0}).

---

### 4.2 (b) Prove (f(x)=\dfrac{|Ax+b|_2^2}{c^\top x + d}) is convex on ({x: c^\top x+d>0})

#### Step 1: Start from the “quadratic-over-linear” template

Define
[
\psi(u,y)=\frac{|u|_2^2}{y},\qquad y>0.
]
Claim: (\psi) is convex jointly in ((u,y)).

**Reason 1 (perspective):** (u\mapsto|u|_2^2) is convex. Then
[
\psi(u,y)= y,|u/y|_2^2
]
is the perspective of (|\cdot|_2^2), hence convex.

**Reason 2 (epigraph / cone):**
[
\psi(u,y)\le t \iff |u|_2^2\le y t.
]
The set ({(u,y,t): y>0,\ |u|_2^2\le yt}) is a rotated second-order cone and is convex.

#### Step 2: Compose with affine maps

Let
[
u(x)=Ax+b,\qquad y(x)=c^\top x+d.
]
Then (u(x)) and (y(x)) are affine in (x), and on the domain we have (y(x)>0). Therefore
[
f(x)=\psi(u(x),y(x))
]
is convex as a convex function composed with an affine map.

---

## 5) Exercise 3.22 — Composition rules (a)–(e)

We prove convexity of each function by decomposing it into:

1. inner convex/concave building blocks,
2. outer convex function with monotonicity,
3. applying the composition rule.

### 5.1 (a) (f(x)=-\log\big(-\log(\sum_{i=1}^m e^{a_i^\top x+b_i})\big))

Domain: (\sum_{i=1}^m e^{a_i^\top x+b_i}<1).

#### Step 1: Define the log-sum-exp inner function

Let
[
s(x)=\sum_{i=1}^m e^{a_i^\top x+b_i},\qquad u(x)=\log s(x).
]

* Each term (e^{a_i^\top x+b_i}) is convex (exp of affine).
* Sum of convex functions is convex (\Rightarrow s(x)) convex.
* The function (u(x)=\log\sum e^{\cdot}) (log-sum-exp) is known convex; you can also derive its PSD Hessian via softmax.
  So (u) is convex.

Domain condition (s(x)<1) implies (u(x)=\log s(x)<0).

#### Step 2: Outer function (g(u)=-\log(-u)) on (u<0)

Compute derivatives:
[
g'(u)= -\frac{1}{u},\qquad g''(u)=\frac{1}{u^2}.
]
On (u<0):

* (g''(u)>0) so (g) is convex.
* (g'(u)>0) so (g) is increasing.

#### Step 3: Compose

[
f(x)=g(u(x)).
]
Convex increasing (g) composed with convex (u) gives convex (f).

---

### 5.2 (b) (f(x,u,v)=-\sqrt{uv-x^\top x})

Domain: (u>0,\ v>0,\ uv>x^\top x).

#### Step 1: Convexity of (q(x,u)=x^\top x/u) for (u>0)

Write
[
q(x,u)=u\left|\frac{x}{u}\right|_2^2,
]
so it is the perspective of (|x|_2^2), hence convex in ((x,u)).

#### Step 2: Build a concave positive quantity

For (u>0), define
[
r(x,u,v)=v - \frac{x^\top x}{u}.
]

* (v) is affine.
* (x^\top x/u) is convex.
  So (r) is **concave** (affine minus convex) and on the domain
  [
  uv>x^\top x \iff v>\frac{x^\top x}{u} \iff r(x,u,v)>0.
  ]

#### Step 3: Outer function (\phi(a,b)=-\sqrt{ab}) on (a>0,b>0)

The geometric mean (\sqrt{ab}) is concave on (\mathbb R_{++}^2) (classic fact: it is 1-homogeneous and log-concave).
Therefore (-\sqrt{ab}) is convex.
Also, (\phi) is **nonincreasing** in each argument (derivatives are negative).

#### Step 4: Compose

Observe
[
uv-x^\top x = u\left(v-\frac{x^\top x}{u}\right)=u,r(x,u,v).
]
So
[
f(x,u,v) = -\sqrt{u,r(x,u,v)} = \phi\big(u,\ r(x,u,v)\big).
]

* Outer (\phi) is convex and nonincreasing in both args.
* Inner args: (u) is affine (hence both convex and concave), and (r) is concave.
  Thus by the “convex + nonincreasing outer, concave inner” rule, (f) is convex.

---

### 5.3 (c) (f(x,u,v)=-\log(uv-x^\top x))

Same domain: (u>0,v>0,uv>x^\top x).

Use the same factorization:
[
uv-x^\top x = u,r(x,u,v),\quad r=v-x^\top x/u>0.
]
Then
[
-\log(uv-x^\top x)= -\log u -\log r(x,u,v).
]

* (-\log u) is convex on (u>0).
* (-\log(\cdot)) is convex and **nonincreasing** on (\mathbb R_{++}).
* (r(x,u,v)) is concave and positive on the domain.
  So (-\log r(x,u,v)) is convex by the nonincreasing composition rule.
  Sum of convex functions is convex (\Rightarrow f) convex.

---

### 5.4 (d) (f(x,t)=-(t^p-|x|_p^p)^{1/p}), (p>1)

Domain: (t\ge |x|_p) (so (t\ge 0) and (t^p-|x|_p^p\ge 0)).

The hint suggests using:

* convexity of (|x|_p^p/u^{p-1}) in ((x,u)) for (u>0),
* convexity of (\Phi(a,b)= -a^{1-1/p}b^{1/p}) on (\mathbb R_{++}^2).

#### Step 1: Use the identity

For (t>0), define
[
q(x,t)=\frac{|x|_p^p}{t^{p-1}}.
]
By Exercise 3.23(a), (q) is convex on (t>0).
Now define
[
r(x,t)= t - q(x,t) = t - \frac{|x|_p^p}{t^{p-1}}.
]
This is affine minus convex, hence **concave** (on (t>0)).
On the domain (t\ge |x|_p), we have (|x|_p^p\le t^p), so
[
q(x,t)=\frac{|x|_p^p}{t^{p-1}} \le \frac{t^p}{t^{p-1}}=t
\Rightarrow r(x,t)\ge 0.
]

Now factor:
[
t^p-|x|_p^p = t^{p-1}\Big(t-\frac{|x|_p^p}{t^{p-1}}\Big)= t^{p-1} r(x,t).
]
Take (1/p) power:
[
(t^p-|x|_p^p)^{1/p} = \big(t^{p-1}r(x,t)\big)^{1/p} = t^{(p-1)/p}, r(x,t)^{1/p}.
]
Hence
[
f(x,t)= -t^{(p-1)/p},r(x,t)^{1/p}.
]

#### Step 2: Outer function (\Phi(a,b)=-a^{(p-1)/p} b^{1/p})

Define
[
\Phi(a,b)=-a^{(p-1)/p} b^{1/p},\qquad a>0,\ b>0.
]
The function (a^{(p-1)/p}b^{1/p}) is a **weighted geometric mean** (weights ((p-1)/p) and (1/p)), hence concave on (\mathbb R_{++}^2). Therefore (\Phi) is convex.
Also (\Phi) is **nonincreasing** in each argument (partial derivatives are negative).

#### Step 3: Compose

We have
[
f(x,t)=\Phi\big(t,\ r(x,t)\big).
]

* Outer (\Phi): convex and nonincreasing in both args.
* Inner: (t) is affine; (r(x,t)) is concave.
  Thus the composition is convex on the domain where (t>0) and (r\ge 0). Boundary (r=0) is handled by continuity (value becomes 0).

---

### 5.5 (e) (f(x,t)=-\log(t^p-|x|_p^p)), (p>1)

Domain: (t>|x|_p) so the log argument is strictly positive.

Use the same factorization:
[
t^p-|x|_p^p = t^{p-1} r(x,t),\qquad r(x,t)=t-|x|_p^p/t^{p-1}.
]
Then
[
-\log(t^p-|x|_p^p)= -\log(t^{p-1}) -\log r(x,t)= -(p-1)\log t - \log r(x,t).
]
Now check convexity of each term:

* (-\log t) is convex on (t>0), so (-(p-1)\log t) is convex.
* (-\log(\cdot)) is convex and nonincreasing on (\mathbb R_{++}).
* (r(x,t)) is concave and positive on the domain.
  Therefore (-\log r(x,t)) is convex by the nonincreasing composition rule.
  Sum of convex terms (\Rightarrow f) convex.

---

## 6) Quick “domain sanity checks” (don’t skip these)

* Whenever (\log) appears, ensure its argument is (>0).
* Whenever a fractional power (\cdot^{1/p}) appears with non-integer (1/p), ensure argument is (\ge 0) (or (>0) if you need differentiability).
* In (b)(c): (uv>x^\top x) plus (u,v>0) ensures both (u>0) and (r=v-x^\top x/u>0).
* In (d)(e): (t\ge|x|_p) ensures (t\ge 0) and (t^p-|x|_p^p\ge 0); strict (>) is needed for (-\log).

---

## 7) What to remember (one-line mental model)

1. **Perspective**: (t f(z/t)) is convex if (f) is convex.
2. **Affine precomposition preserves convexity**.
3. **Convex + monotone composition** is your main weapon:

   * outer convex increasing + inner convex  ⇒ convex;
   * outer convex decreasing + inner concave ⇒ convex.
4. Factor tricky expressions until they become (a) a perspective, or (b) an outer convex monotone function applied to a concave quantity.

## Response:
Updated saved memory

Thought for 39s

Example 3.20 (BV) — “Perspective + affine map” gives a convex function
----------------------------------------------------------------------

You’re given a convex function  $f:\mathbb R^m\to\mathbb R\cup\{+\infty\}$  and data

$$
A\in\mathbb R^{m\times n},\quad b\in\mathbb R^m,\quad c\in\mathbb R^n,\quad d\in\mathbb R.
$$

Define

$$
g(x)=\big(c^\top x+d\big)\; f\!\left(\frac{Ax+b}{c^\top x+d}\right),
$$

with domain

$$
\mathrm{dom}\,g=\Big\{x:\ c^\top x+d>0,\ \frac{Ax+b}{c^\top x+d}\in \mathrm{dom}\,f\Big\}.
$$

**Claim:**  $g$  is convex.

The whole proof is:

1.  **Perspective preserves convexity**,
2.  **Convex function composed with an affine map is convex**.

But I’ll prove both from scratch.

* * *

0) Bedrock: what convexity means here (extended-value)
======================================================

Since  $f$  may take  $+\infty$ , we use extended-value convexity:

A function  $F:\mathbb R^k\to\mathbb R\cup\{+\infty\}$  is convex if for all  $u,v$  and  $\theta\in[0,1]$ ,

$$
F(\theta u+(1-\theta)v)\ \le\ \theta F(u)+(1-\theta)F(v),
$$

interpreting arithmetic with  $+\infty$  in the standard way (if RHS is  $+\infty$ , inequality is automatically true).

Key consequence: **we don’t need to separately worry about points outside the domain**—they just have value  $+\infty$  and convexity inequalities become trivially true when infeasible points appear.

* * *

1) Step 1 — Define the perspective and prove it’s convex
========================================================

1.1 Perspective definition (precise)
------------------------------------

Given  $f:\mathbb R^m\to\mathbb R\cup\{+\infty\}$ , define its **perspective**  $\tilde f:\mathbb R^m\times\mathbb R\to\mathbb R\cup\{+\infty\}$  by

$$
\tilde f(z,t)= \begin{cases} t\, f(z/t), & t>0,\\ +\infty, & t\le 0. \end{cases}
$$

(You can also restrict to the natural domain  $t>0$  and set  $+\infty$  elsewhere; same effect.)

So the domain is

$$
\mathrm{dom}\,\tilde f=\{(z,t): t>0,\ z/t\in\mathrm{dom}\,f\}.
$$

1.2 Theorem: if  $f$  is convex, then  $\tilde f$  is convex
------------------------------------------------------------

I’ll prove it by the epigraph method, but with **every** algebra step shown.

### Epigraph definitions

For any  $F$ ,

$$
\mathrm{epi}\,F := \{(u,s): F(u)\le s\}.
$$

Fact (proved in BV, but I’ll restate):

$$
F\text{ convex } \iff \mathrm{epi}\,F \text{ is a convex set.}
$$

### Goal

Show  $\mathrm{epi}\,\tilde f$  is convex.

### Step A: write  $\mathrm{epi}\,\tilde f$  explicitly

A point  $(z,t,s)$  lies in  $\mathrm{epi}\,\tilde f$  iff

*    $t>0$ , and
*    $\tilde f(z,t)\le s$ , i.e.
    
$$
t\, f(z/t)\le s.
$$

Since  $t>0$ , divide both sides by  $t$  (legal because positive):

$$
f(z/t)\ \le\ s/t.
$$

So:

$$
(z,t,s)\in \mathrm{epi}\,\tilde f \iff t>0\ \text{ and }\ \Big(\frac{z}{t},\frac{s}{t}\Big)\in \mathrm{epi}\,f.
$$

Now define

$$
u:=\frac{z}{t},\qquad \alpha:=\frac{s}{t}.
$$

Then  $z=tu,\ s=t\alpha$ . So we can rewrite the epigraph as:

$$
\boxed{ \mathrm{epi}\,\tilde f = \{(tu,\ t,\ t\alpha): (u,\alpha)\in \mathrm{epi}\,f,\ t>0\}. }
$$

This is the “cone over  $\mathrm{epi} f$ ” representation.

### Step B: prove this set is convex (directly, no “magic linear map” claims)

Take two arbitrary points in  $\mathrm{epi}\,\tilde f$ :

$$
(z_1,t_1,s_1)=(t_1u_1,\ t_1,\ t_1\alpha_1),\quad (u_1,\alpha_1)\in \mathrm{epi} f,\ t_1>0,
$$
 
$$
(z_2,t_2,s_2)=(t_2u_2,\ t_2,\ t_2\alpha_2),\quad (u_2,\alpha_2)\in \mathrm{epi} f,\ t_2>0.
$$

Let  $\theta\in[0,1]$ . Consider their convex combination:

$$
(z,t,s):=\theta(z_1,t_1,s_1)+(1-\theta)(z_2,t_2,s_2).
$$

Compute each coordinate:

*    $t = \theta t_1 + (1-\theta)t_2$ .  
    Since  $t_1,t_2>0$  and  $\theta\in[0,1]$ , we get  $t>0$ .
*    $z = \theta t_1u_1 + (1-\theta)t_2u_2$ .
*    $s = \theta t_1\alpha_1 + (1-\theta)t_2\alpha_2$ .

Now define weights

$$
\lambda := \frac{\theta t_1}{t},\qquad 1-\lambda := \frac{(1-\theta)t_2}{t}.
$$

Check they are valid convex weights:

*    $\lambda\ge 0$ ,  $1-\lambda\ge 0$  because numerator and denominator are nonnegative,
*    $\lambda+(1-\lambda)=\dfrac{\theta t_1+(1-\theta)t_2}{t}=1$ .

Now rewrite  $z$  and  $s$  by factoring out  $t$ :

$$
z = t\left(\frac{\theta t_1}{t}u_1 + \frac{(1-\theta)t_2}{t}u_2\right) = t(\lambda u_1 + (1-\lambda)u_2),
$$
 
$$
s = t\left(\frac{\theta t_1}{t}\alpha_1 + \frac{(1-\theta)t_2}{t}\alpha_2\right) = t(\lambda \alpha_1 + (1-\lambda)\alpha_2).
$$

Define

$$
u:=\lambda u_1 + (1-\lambda)u_2,\qquad \alpha:=\lambda \alpha_1 + (1-\lambda)\alpha_2.
$$

Then

$$
(z,t,s)=(tu,\ t,\ t\alpha).
$$

Since  $(u_1,\alpha_1)$  and  $(u_2,\alpha_2)$  are in  $\mathrm{epi} f$  and  $\mathrm{epi} f$  is convex (because  $f$  is convex), we have

$$
(u,\alpha)=\lambda(u_1,\alpha_1)+(1-\lambda)(u_2,\alpha_2)\in \mathrm{epi} f.
$$

And we already have  $t>0$ . Therefore  $(z,t,s)\in \mathrm{epi}\,\tilde f$ .

So  $\mathrm{epi}\,\tilde f$  is convex, hence  $\tilde f$  is convex. □

* * *

2) Step 2 — Show  $g$  is “perspective after an affine map”
===========================================================

Define the affine maps

$$
z(x):=Ax+b,\qquad t(x):=c^\top x + d.
$$

These are affine because:

*    $Ax$  is linear, add  $b$  → affine,
*    $c^\top x$  is linear, add  $d$  → affine.

Now check:

$$
\tilde f(z(x),t(x)) = t(x)\, f\!\left(\frac{z(x)}{t(x)}\right) = (c^\top x+d)\, f\!\left(\frac{Ax+b}{c^\top x+d}\right) =g(x),
$$

for  $t(x)>0$ . And outside  $t(x)>0$  we can define  $g(x)=+\infty$  consistently.

So:

$$
\boxed{g = \tilde f \circ (z,t),\quad \text{where } (z,t)(x)=(Ax+b,\ c^\top x+d).}
$$

* * *

3) Step 3 — Prove “convex composed with affine is convex” (directly)
====================================================================

Lemma (affine precomposition preserves convexity)
-------------------------------------------------

If  $F:\mathbb R^k\to\mathbb R\cup\{+\infty\}$  is convex and  $L:\mathbb R^n\to\mathbb R^k$  is affine, then  $F\circ L$  is convex.

### Proof (Jensen inequality, fully explicit)

Let  $L(x)=Mx+p$  for some matrix  $M$  and vector  $p$ . (Every affine map has this form.)

Take any  $x_1,x_2$  and  $\theta\in[0,1]$ . Then

$$
L(\theta x_1+(1-\theta)x_2) = M(\theta x_1+(1-\theta)x_2)+p = \theta(Mx_1+p)+(1-\theta)(Mx_2+p) = \theta L(x_1)+(1-\theta)L(x_2).
$$

Now apply convexity of  $F$ :

$$
F(L(\theta x_1+(1-\theta)x_2)) = F(\theta L(x_1)+(1-\theta)L(x_2)) \le \theta F(L(x_1))+(1-\theta)F(L(x_2)).
$$

That is exactly convexity of  $F\circ L$ . □

Apply this lemma with  $F=\tilde f$  (convex by Section 1) and  $L(x)=(z(x),t(x))$  (affine). Then  $g=\tilde f\circ L$  is convex. □

* * *

4) Domain convexity (optional but illuminating, and good self-check)
====================================================================

Even though extended-value convexity “handles” domain automatically, it’s intellectually satisfying to verify the domain is convex.

Take  $x_1,x_2\in\mathrm{dom}\,g$ . Then:

*    $t_i:=c^\top x_i+d>0$ ,
*    $u_i:=(Ax_i+b)/t_i\in\mathrm{dom}\,f$ .

For  $\theta\in[0,1]$ , let  $x_\theta=\theta x_1+(1-\theta)x_2$ . Then

$$
t_\theta = c^\top x_\theta + d = \theta t_1+(1-\theta)t_2 >0.
$$

Also

$$
z_\theta = A x_\theta + b = \theta(Ax_1+b)+(1-\theta)(Ax_2+b)=\theta z_1+(1-\theta)z_2.
$$

Now compute the ratio:

$$
\frac{z_\theta}{t_\theta} = \frac{\theta z_1+(1-\theta)z_2}{\theta t_1+(1-\theta)t_2}.
$$

Write it as a convex combination of  $u_1=z_1/t_1$  and  $u_2=z_2/t_2$  by the same trick as before:

Let

$$
\lambda := \frac{\theta t_1}{t_\theta}\in[0,1].
$$

Then

$$
\frac{z_\theta}{t_\theta} = \lambda \frac{z_1}{t_1} + (1-\lambda)\frac{z_2}{t_2} = \lambda u_1+(1-\lambda)u_2.
$$

Since  $f$  is convex,  $\mathrm{dom}\,f$  is convex, so  $u_1,u_2\in\mathrm{dom}\,f\Rightarrow \lambda u_1+(1-\lambda)u_2\in\mathrm{dom}\,f$ . Hence  $x_\theta\in\mathrm{dom}\,g$ .

So  $\mathrm{dom}\,g$  is convex.

* * *

5) Alternative proof (epigraph/projection form for  $g$ )
=========================================================

This is the “more structural” proof: show  $\mathrm{epi}\,g$  is a projection of a convex set.

Start with  $(u,\alpha)\in\mathrm{epi}\,f$ , i.e.  $f(u)\le \alpha$ . If we enforce

$$
Ax+b = t u,\qquad t=c^\top x+d,\qquad t>0,
$$

then

$$
g(x)=t f(u)\le t\alpha.
$$

So  $(x,s)\in \mathrm{epi}\,g$  iff there exist  $t>0,u,\alpha$  such that:

$$
(u,\alpha)\in\mathrm{epi} f,\quad Ax+b=tu,\quad c^\top x+d=t,\quad s\ge t\alpha.
$$

That set is convex because:

*    $\mathrm{epi} f$  is convex,
*   constraints are affine in the lifted variables  $(x,t,u,\alpha,s)$ ,
*   inequality  $s\ge t\alpha$  is handled via the cone representation already embedded in  $(tu,t,t\alpha)$  (equivalently: you can encode it as membership in  $\mathrm{epi}\,\tilde f$ ).  
    Projecting a convex set gives a convex set ⇒  $\mathrm{epi}\,g$  convex ⇒  $g$  convex.

Same conclusion, different lens.

* * *

6) Sanity-check examples (to see the mechanism “click”)
=======================================================

### 6.1 Quadratic-over-linear (classic)

Let  $f(u)=\|u\|_2^2$  (convex). Then

$$
g(x)= (c^\top x+d)\left\|\frac{Ax+b}{c^\top x+d}\right\|_2^2 = \frac{\|Ax+b\|_2^2}{c^\top x+d},
$$

on  $c^\top x+d>0$ . This is the famous convex function “quadratic over linear.”

### 6.2 Norms are 1-homogeneous, so the perspective collapses

If  $f(u)=\|u\|$  is any norm, then for  $t>0$ 

$$
t f(z/t)= t\|z/t\|=\|z\|.
$$

So Example 3.20 produces

$$
g(x)=\|Ax+b\|,
$$

which is convex (and the denominator disappears). This is a great check.

* * *

If you want to push further after this: the next natural brutality is to derive the **Hessian** of  $g$  for smooth  $f$  (using the chain rule + quotient rule carefully), and then recover convexity by showing the Hessian is PSD—this is messier but very instructive when  $f$  is  $C^2$ .

## Prompt:
Exercise 22

## Response:
Thought for 32s

Exercise 3.22 (BV) — parts (a)–(e), fully unpacked from zero
------------------------------------------------------------

You can think of all five parts as the same game:

1.  identify a **simple inner map** (often convex or concave),
2.  identify a **simple outer map** (convex, and either increasing or decreasing in each argument),
3.  apply the **monotone composition rule** (proved below),
4.  don’t forget **domain** (because logs/square-roots/powers silently demand positivity).

I’ll prove the needed meta-lemmas first, then do (a)–(e).

* * *

0) Two composition rules (proved directly)
==========================================

We’ll use these repeatedly.

0.1 Composition Rule A (convex + nondecreasing outer)
-----------------------------------------------------

Let  $u:\mathbb R^n\to\mathbb R^m$  with components  $u_i(x)$ .  
Let  $g:\mathbb R^m\to\mathbb R\cup\{+\infty\}$ .

Assume:

*   each  $u_i$  is **convex**, and
*    $g$  is **convex** and **nondecreasing in each coordinate**:
    $$
    z\le z' \text{ componentwise } \Rightarrow g(z)\le g(z').
    $$

Define  $f(x):=g(u(x)) = g(u_1(x),\dots,u_m(x))$ .  
Then  $f$  is **convex**.

### Proof (Jensen + monotonicity, fully explicit)

Take any  $x,y$  and  $\theta\in[0,1]$ . Convexity of each  $u_i$  gives

$$
u_i(\theta x+(1-\theta)y)\ \le\ \theta u_i(x)+(1-\theta)u_i(y).
$$

Stack these  $m$  inequalities into one vector inequality:

$$
u(\theta x+(1-\theta)y)\ \le\ \theta u(x)+(1-\theta)u(y) \quad\text{(componentwise)}.
$$

Since  $g$  is nondecreasing componentwise, applying  $g$  preserves the inequality:

$$
g(u(\theta x+(1-\theta)y)) \ \le\ g(\theta u(x)+(1-\theta)u(y)).
$$

Now apply convexity of  $g$ :

$$
g(\theta u(x)+(1-\theta)u(y)) \ \le\ \theta g(u(x))+(1-\theta)g(u(y)).
$$

Chain the inequalities:

$$
f(\theta x+(1-\theta)y)\le \theta f(x)+(1-\theta)f(y).
$$

So  $f$  is convex. □

* * *

0.2 Composition Rule B (convex + nonincreasing outer)
-----------------------------------------------------

Assume instead:

*   each  $u_i$  is **concave**, and
*    $g$  is **convex** and **nonincreasing** in each coordinate:
    $$
    z\le z' \Rightarrow g(z)\ge g(z').
    $$

Then  $f(x)=g(u(x))$  is **convex**.

### Proof (same skeleton; only inequality directions flip)

Concavity gives

$$
u(\theta x+(1-\theta)y)\ \ge\ \theta u(x)+(1-\theta)u(y).
$$

Nonincreasing  $g$  reverses inequality when applied:

$$
g(u(\theta x+(1-\theta)y)) \ \le\ g(\theta u(x)+(1-\theta)u(y)).
$$

Then convexity of  $g$  finishes exactly as before. □

* * *

0.3 Two building blocks we’ll also prove once
=============================================

(i) Log-sum-exp is convex
-------------------------

Define

$$
\operatorname{lse}(z):=\log\Big(\sum_{i=1}^m e^{z_i}\Big).
$$

It’s convex. Quick but rigorous Hessian proof:

Let  $S=\sum_j e^{z_j}$  and  $p_i=e^{z_i}/S$  (so  $p_i\ge 0$ ,  $\sum_i p_i=1$ ). Then

$$
\nabla \operatorname{lse}(z)=p,\qquad \nabla^2 \operatorname{lse}(z)=\mathrm{diag}(p)-pp^\top.
$$

For any  $v$ ,

$$
v^\top(\mathrm{diag}(p)-pp^\top)v =\sum_i p_i v_i^2-\Big(\sum_i p_i v_i\Big)^2 =\mathrm{Var}_{i\sim p}(v_i)\ge 0.
$$

So the Hessian is PSD, hence  $\operatorname{lse}$  is convex. Also each partial derivative  $p_i>0$ , so it is **increasing** in every coordinate.

(ii) Perspective of a convex function is convex
-----------------------------------------------

If  $\phi$  is convex, then  $\tilde\phi(x,t):=t\,\phi(x/t)$  (for  $t>0$ ) is convex in  $(x,t)$ .  
(You already have the full epigraph proof in your notes; we’ll use it as a black box here to avoid repeating pages.)

* * *

1) Exercise 3.22(a)
===================

### Function

$$
f(x)=-\log\Big(-\log\Big(\sum_{i=1}^m e^{a_i^\top x+b_i}\Big)\Big).
$$

**Domain:**  $\sum_{i=1}^m e^{a_i^\top x+b_i}<1$  (so the inner  $\log(\cdot)$  is  $<0$ , making  $-\log(\cdot)>0$ , making outer  $\log$  legal).

* * *

Step 1: Identify inner function  $u(x)$  and prove it’s convex
--------------------------------------------------------------

Let

$$
s(x):=\sum_{i=1}^m e^{a_i^\top x+b_i},\qquad u(x):=\log s(x).
$$

### 1.1  $s(x)$  is convex

Each  $x\mapsto a_i^\top x+b_i$  is affine.  
Each  $x\mapsto e^{a_i^\top x+b_i}$  is convex (exp is convex; exp∘affine is convex).  
Sum of convex functions is convex ⇒  $s$  convex.

### 1.2  $u(x)=\log\sum_i e^{a_i^\top x+b_i}$  is convex

This is log-sum-exp composed with an affine map:

$$
u(x)=\operatorname{lse}(z(x)),\qquad z_i(x)=a_i^\top x+b_i.
$$
*    $z(x)$  is affine in  $x$ ,
*    $\operatorname{lse}$  is convex,
*   convex ∘ affine is convex.  
    So  $u$  is convex.

* * *

Step 2: Outer function  $g(u)=-\log(-u)$  on  $u<0$ 
----------------------------------------------------

Define

$$
g(t)=-\log(-t),\qquad t<0.
$$

### 2.1 Check monotonicity

Differentiate carefully:

*    $\frac{d}{dt}\log(-t)=\frac{1}{-t}\cdot(-1)=\frac{1}{t}$ .
*   So
    $$
    g'(t)=-\frac{1}{t}.
    $$

On  $t<0$ , we have  $-1/t>0$ . So  $g$  is **increasing**.

### 2.2 Check convexity

$$
g''(t)=\frac{1}{t^2}>0 \quad (t\neq 0).
$$

On its domain  $t<0$ ,  $g$  is convex.

* * *

Step 3: Compose
---------------

We have  $f(x)=g(u(x))$ .

*    $u$  is convex,
*    $g$  is convex and increasing,  
    so by Composition Rule A,  $f$  is convex on its domain.

**Domain convexity check (good hygiene):**  
Domain is  $\{x: s(x)<1\}$ . Since  $s$  is convex, the sublevel set  $\{x:s(x)\le 1\}$  is convex; the strict version  $<1$  is an open convex set.

✅ (a) proved.

* * *

2) Exercise 3.22(b)
===================

### Function

$$
f(x,u,v)=-\sqrt{uv-x^\top x},
$$

**Domain:**  $u>0,\ v>0,\ uv>x^\top x$ .

The strategy is to rewrite  $uv-x^\top x$  as a product of two **concave** positive terms, then apply a convex **decreasing** outer function.

* * *

Step 1: Prove  $q(x,u)=\dfrac{x^\top x}{u}$  is convex on  $u>0$ 
-----------------------------------------------------------------

### 2.1 Perspective proof (cleanest)

Let  $\phi(x)=x^\top x=\|x\|_2^2$ .  $\phi$  is convex.  
Its perspective is

$$
\tilde\phi(x,u)=u\,\phi(x/u)=u\|x/u\|_2^2=\frac{\|x\|_2^2}{u}.
$$

Perspective of convex is convex ⇒  $q$  convex.

(Alternative: epigraph  $\|x\|^2\le ut$  is a rotated SOC; convex set ⇒ convex function.)

* * *

Step 2: Build a concave positive inner term
-------------------------------------------

Define

$$
r(x,u,v):=v-\frac{x^\top x}{u}=v-q(x,u).
$$
*    $v$  is affine ⇒ both convex and concave.
*    $q$  is convex ⇒  $-q$  is concave.  
    So  $r$  is **concave** (concave + concave).

On the domain  $uv>x^\top x$  and  $u>0$ ,

$$
uv>x^\top x \iff v>\frac{x^\top x}{u}\iff r(x,u,v)>0.
$$

Now observe:

$$
uv-x^\top x = u\left(v-\frac{x^\top x}{u}\right) = u\,r(x,u,v).
$$

* * *

Step 3: Outer function  $\Phi(a,b)=-\sqrt{ab}$  is convex and decreasing
------------------------------------------------------------------------

Define for  $a>0,b>0$ :

$$
\Phi(a,b)=-\sqrt{ab}.
$$

### 3.1 Show  $\sqrt{ab}$  is concave

Use log-concavity + homogeneity:

$$
\log(\sqrt{ab})=\tfrac12(\log a+\log b).
$$

 $\log a$  and  $\log b$  are concave on  $\mathbb R_{++}$ ; average of concave is concave ⇒  $\log(\sqrt{ab})$  concave ⇒  $\sqrt{ab}$  is **log-concave**.

Also  $\sqrt{ab}$  is 1-homogeneous:

$$
\sqrt{(\lambda a)(\lambda b)}=\lambda \sqrt{ab}\quad(\lambda>0).
$$

A positive 1-homogeneous log-concave function is concave (standard lemma; if you want, I can re-prove it line-by-line like we did in 3.14).  
Hence  $\sqrt{ab}$  concave ⇒  $-\sqrt{ab}$  convex.

### 3.2 Show  $\Phi$  is nonincreasing in each argument

Compute partial derivatives:

$$
\frac{\partial \Phi}{\partial a}=-\frac12 \sqrt{\frac{b}{a}}<0,\qquad \frac{\partial \Phi}{\partial b}=-\frac12 \sqrt{\frac{a}{b}}<0.
$$

So  $\Phi$  is **decreasing** in  $a$  and in  $b$ .

* * *

Step 4: Compose using Composition Rule B
----------------------------------------

We have

$$
f(x,u,v)=\Phi\big(u,\ r(x,u,v)\big),
$$

where

*    $u$  is affine ⇒ concave,
*    $r$  is concave,
*    $\Phi$  is convex and nonincreasing in each argument.

Therefore  $f$  is convex on its domain.

✅ (b) proved.

* * *

3) Exercise 3.22(c)
===================

### Function

$$
f(x,u,v)=-\log(uv-x^\top x),
$$

domain  $u>0,v>0,uv>x^\top x$ .

Use the same factorization:

$$
uv-x^\top x = u\,r(x,u,v),\quad r=v-\frac{x^\top x}{u}>0.
$$

Then

$$
-\log(uv-x^\top x)= -\log u - \log r(x,u,v).
$$

Step 1:  $-\log u$  is convex on  $u>0$ 
----------------------------------------

 $(-\log u)'' = 1/u^2>0$ .

Step 2:  $-\log(\cdot)$  is convex and decreasing on  $\mathbb R_{++}$ 
-----------------------------------------------------------------------

Derivative  $-1/t<0$ , second derivative  $1/t^2>0$ .

Step 3: Compose  $-\log\circ r$ 
--------------------------------

We already proved  $r$  is concave and positive on the domain.  
Outer  $-\log$  is convex and **decreasing**.  
So by Composition Rule B,  $-\log(r(x,u,v))$  is convex.

Sum of convex functions is convex ⇒  $f$  convex.

✅ (c) proved.

* * *

4) Exercise 3.22(d)
===================

### Function

For  $p>1$ ,

$$
f(x,t)=-(t^p-\|x\|_p^p)^{1/p},
$$

domain  $t\ge \|x\|_p$  (so the inside is  $\ge 0$ ).

This one looks scary until you “factor it” into a weighted geometric mean.

* * *

Step 1: Prove  $\phi(x)=\|x\|_p^p$  is convex
---------------------------------------------

$$
\|x\|_p^p=\sum_{i=1}^n |x_i|^p.
$$

For  $p\ge 1$ ,  $u\mapsto |u|^p$  is convex on  $\mathbb R$ ; sum preserves convexity ⇒  $\phi$  convex.

Step 2: Use a perspective to get a convex “ratio”
-------------------------------------------------

Define for  $t>0$ :

$$
q(x,t):=\frac{\|x\|_p^p}{t^{p-1}}.
$$

Check it is a perspective of  $\phi$ :

$$
t\,\phi(x/t)=t \sum_i |x_i/t|^p = t\sum_i \frac{|x_i|^p}{t^p} =\frac{\sum_i |x_i|^p}{t^{p-1}}=\frac{\|x\|_p^p}{t^{p-1}}.
$$

So  $q$  is convex on  $t>0$ .

Step 3: Define a concave positive term
--------------------------------------

Let

$$
r(x,t):=t-q(x,t)=t-\frac{\|x\|_p^p}{t^{p-1}}.
$$

Affine minus convex ⇒  $r$  is **concave** on  $t>0$ .

On the domain  $t\ge \|x\|_p$ , we have  $\|x\|_p^p\le t^p$ . Divide by  $t^{p-1}>0$  (for  $t>0$ ):

$$
\frac{\|x\|_p^p}{t^{p-1}}\le \frac{t^p}{t^{p-1}}=t \quad\Rightarrow\quad r(x,t)\ge 0.
$$

Now factor:

$$
t^p-\|x\|_p^p = t^{p-1}\Big(t-\frac{\|x\|_p^p}{t^{p-1}}\Big) = t^{p-1}\, r(x,t).
$$

Take  $1/p$ \-power:

$$
(t^p-\|x\|_p^p)^{1/p} = \big(t^{p-1} r(x,t)\big)^{1/p} = t^{(p-1)/p}\, r(x,t)^{1/p}.
$$

So

$$
f(x,t)= -\, t^{(p-1)/p}\, r(x,t)^{1/p}.
$$

Step 4: Outer function is negative weighted geometric mean
----------------------------------------------------------

Define for  $a>0,b>0$ :

$$
\Phi(a,b)= - a^{(p-1)/p} b^{1/p}.
$$

The function  $a^{\alpha}b^{1-\alpha}$  with  $\alpha\in(0,1)$  is concave on  $\mathbb R_{++}^2$  (same log-concavity + 1-homogeneity argument as geometric mean), hence  $\Phi$  is **convex**.

Monotonicity: since exponents are positive,

$$
a^{(p-1)/p} b^{1/p} \text{ increases in } a,b,
$$

so with the minus sign,  $\Phi$  is **decreasing** in  $a$  and  $b$ .

Step 5: Compose (decreasing convex outer + concave inner)
---------------------------------------------------------

We have

$$
f(x,t)=\Phi\big(a(x,t),b(x,t)\big), \quad a=t,\quad b=r(x,t).
$$
*    $a=t$  is affine ⇒ concave.
*    $b=r(x,t)$  is concave (on  $t>0$ , and  $b\ge 0$  on the domain).
*    $\Phi$  is convex and nonincreasing in each argument.

So by Composition Rule B,  $f$  is convex on its domain (with the usual “boundary  $r=0$ ” handled by continuity).

✅ (d) proved.

* * *

5) Exercise 3.22(e)
===================

### Function

For  $p>1$ ,

$$
f(x,t)= -\log\big(t^p-\|x\|_p^p\big),
$$

domain  $t>\|x\|_p$  (strict, because log needs  $>0$ ).

Use the same factorization:

$$
t^p-\|x\|_p^p=t^{p-1}r(x,t),\quad r(x,t)=t-\frac{\|x\|_p^p}{t^{p-1}}>0.
$$

Then

$$
-\log(t^p-\|x\|_p^p) = -\log(t^{p-1}) - \log r(x,t) = -(p-1)\log t - \log r(x,t).
$$
*    $-(p-1)\log t$  is convex on  $t>0$ .
*    $-\log(\cdot)$  is convex and **decreasing** on  $\mathbb R_{++}$ .
*    $r(x,t)$  is concave and positive on the domain.

So  $-\log(r(x,t))$  is convex by Composition Rule B. Sum ⇒ convex.

✅ (e) proved.

* * *

What’s the real pattern?
------------------------

*   Parts (b),(c): you rewrite  $uv-x^\top x = u\cdot\big(v-\frac{x^\top x}{u}\big)$  and note  $\frac{x^\top x}{u}$  is a **perspective** (hence convex), so the bracket is **concave**.
*   Parts (d),(e): same trick, but with  $\|x\|_p^p/t^{p-1}$  as a **perspective**.

If you want an even deeper “next layer,” we can also do **epigraph-based proofs** for each (show the epigraph is a known convex cone: SOC / rotated SOC / power cone), which is often how these are implemented in conic solvers.

2/2

## Prompt:
3.23

## Response:
Thought for 16s

Exercise 3.23 (BV) — Perspective examples, from bedrock
-------------------------------------------------------

Exercise 3.23 is really: **recognize a scary-looking expression as a perspective** of a simpler convex function, then use “perspective preserves convexity,” and (optionally) verify convexity again via an **epigraph / cone** description.

I’ll do both parts in maximal detail, and I’ll _prove_ any theorem I use.

* * *

0) Bedrock tools (proved)
=========================

0.1 What “convex” means (extended-value friendly)
-------------------------------------------------

A function  $F:\mathbb R^k\to\mathbb R\cup\{+\infty\}$  is convex if for all  $u,v$  and  $\theta\in[0,1]$ ,

$$
F(\theta u+(1-\theta)v)\ \le\ \theta F(u)+(1-\theta)F(v),
$$

with the convention that if the RHS is  $+\infty$ , the inequality is automatically true.

This lets us freely encode domain constraints by setting  $F=+\infty$  outside the natural domain.

* * *

0.2 Perspective transform (definition)
--------------------------------------

Given a function  $\phi:\mathbb R^n\to\mathbb R\cup\{+\infty\}$ , its **perspective**  $\tilde\phi:\mathbb R^n\times\mathbb R\to\mathbb R\cup\{+\infty\}$  is

$$
\tilde\phi(x,t)= \begin{cases} t\,\phi(x/t), & t>0,\\ +\infty, & t\le 0. \end{cases}
$$

Domain:

$$
\mathrm{dom}\,\tilde\phi=\{(x,t): t>0,\ x/t\in\mathrm{dom}\,\phi\}.
$$

* * *

0.3 Theorem: perspective preserves convexity (proved from scratch)
------------------------------------------------------------------

### Theorem

If  $\phi$  is convex, then  $\tilde\phi$  is convex on its domain.

### Proof (epigraph method, fully explicit)

**Step 1.** Epigraph definitions:

$$
\mathrm{epi}\,\phi := \{(u,\alpha): \phi(u)\le \alpha\},\qquad \mathrm{epi}\,\tilde\phi := \{(x,t,s): \tilde\phi(x,t)\le s\}.
$$

Fact:  $\phi$  convex    $\iff$   $\mathrm{epi}\,\phi$  convex. (Standard; we use it.)

**Step 2.** Rewrite the epigraph constraint:

$$
(x,t,s)\in\mathrm{epi}\,\tilde\phi \iff t>0\ \text{and}\ t\,\phi(x/t)\le s.
$$

Since  $t>0$ , divide both sides by  $t$ :

$$
t\,\phi(x/t)\le s \iff \phi(x/t)\le s/t.
$$

So

$$
(x,t,s)\in\mathrm{epi}\,\tilde\phi \iff t>0\ \text{and}\ \left(\frac{x}{t},\frac{s}{t}\right)\in \mathrm{epi}\,\phi.
$$

**Step 3.** Parametrize points in  $\mathrm{epi}\,\tilde\phi$ .  
Let  $u=x/t$  and  $\alpha=s/t$ . Then  $x=tu$ ,  $s=t\alpha$ . So:

$$
\boxed{ \mathrm{epi}\,\tilde\phi = \{(tu,\ t,\ t\alpha): (u,\alpha)\in\mathrm{epi}\,\phi,\ t>0\}. }
$$

**Step 4.** Prove this set is convex.  
Take two points in  $\mathrm{epi}\,\tilde\phi$ :

$$
(x_1,t_1,s_1)=(t_1u_1,\ t_1,\ t_1\alpha_1),\quad (u_1,\alpha_1)\in\mathrm{epi}\,\phi,\ t_1>0,
$$
 
$$
(x_2,t_2,s_2)=(t_2u_2,\ t_2,\ t_2\alpha_2),\quad (u_2,\alpha_2)\in\mathrm{epi}\,\phi,\ t_2>0.
$$

Let  $\theta\in[0,1]$ . Form the convex combination:

$$
(x,t,s)=\theta(x_1,t_1,s_1)+(1-\theta)(x_2,t_2,s_2).
$$

Compute:

*    $t=\theta t_1+(1-\theta)t_2>0$ .
*    $x=\theta t_1u_1+(1-\theta)t_2u_2$ .
*    $s=\theta t_1\alpha_1+(1-\theta)t_2\alpha_2$ .

Define

$$
\lambda:=\frac{\theta t_1}{t}\in[0,1],\qquad 1-\lambda:=\frac{(1-\theta)t_2}{t}.
$$

Then

$$
x=t(\lambda u_1+(1-\lambda)u_2),\qquad s=t(\lambda\alpha_1+(1-\lambda)\alpha_2).
$$

Let  $u=\lambda u_1+(1-\lambda)u_2$  and  $\alpha=\lambda\alpha_1+(1-\lambda)\alpha_2$ . Then

$$
(x,t,s)=(tu,\ t,\ t\alpha).
$$

Because  $\mathrm{epi}\,\phi$  is convex and  $(u_i,\alpha_i)\in\mathrm{epi}\,\phi$ , we have  $(u,\alpha)\in\mathrm{epi}\,\phi$ . Hence  $(x,t,s)\in\mathrm{epi}\,\tilde\phi$ .

So  $\mathrm{epi}\,\tilde\phi$  is convex, hence  $\tilde\phi$  is convex. □

That’s the theorem we’ll use twice.

* * *

1) Exercise 3.23(a)
===================

Statement
---------

For  $p>1$ , prove

$$
F(x,t)=\frac{\|x\|_p^p}{t^{p-1}}
$$

is convex on the domain  $t>0$ .

(Here  $\|x\|_p^p=\sum_{i=1}^n |x_i|^p$ .)

* * *

Step 1: prove  $\phi(x)=\|x\|_p^p$  is convex on  $\mathbb R^n$ 
----------------------------------------------------------------

### 1.1 Reduce to the scalar function  $h(u)=|u|^p$ 

We have

$$
\phi(x)=\sum_{i=1}^n h(x_i),\qquad h(u)=|u|^p.
$$

If  $h$  is convex on  $\mathbb R$ , then  $\phi$  is convex because **a sum of convex functions is convex** (proof: Jensen inequality distributes over sums).

So we prove  $h$  convex.

### 1.2 Prove  $h(u)=|u|^p$  is convex for  $p\ge 1$ 

We’ll do it via second derivatives _carefully_.

**Case 1:  $u>0$ .** Then  $h(u)=u^p$ .

$$
h'(u)=p u^{p-1},\qquad h''(u)=p(p-1)u^{p-2}.
$$

For  $p\ge 1$ , we have  $p(p-1)\ge 0$  and  $u^{p-2}>0$ , so  $h''(u)\ge 0$ . Thus  $h$  is convex on  $(0,\infty)$ .

**Case 2:  $u<0$ .** Then  $h(u)=(-u)^p$ . Let  $w=-u>0$ . Same computation gives  $h''(u)=p(p-1)(-u)^{p-2}\ge 0$ . So convex on  $(-\infty,0)$ .

**At  $u=0$ .** For  $p>1$ ,  $h$  is differentiable at 0 with  $h'(0)=0$ . Convexity across 0 follows because:

*    $h$  is convex on each side,
*    $h$  is continuous at 0,
*   and the left/right slopes satisfy monotonicity (derivative from left  $\le$  derivative from right). Here both are 0 when  $p>1$ .

So  $h$  is convex on all  $\mathbb R$ . □

### 1.3 Conclude  $\phi(x)$  convex

Sum of convex functions:

$$
\phi(\theta x+(1-\theta)y)=\sum_i h(\theta x_i+(1-\theta)y_i) \le \sum_i \big(\theta h(x_i)+(1-\theta)h(y_i)\big) = \theta \phi(x)+(1-\theta)\phi(y).
$$

So  $\phi$  is convex. □

* * *

Step 2: show  $F$  is the perspective of  $\phi$ 
-------------------------------------------------

Compute the perspective of  $\phi$ :

$$
\tilde\phi(x,t)=t\,\phi(x/t),\quad t>0.
$$

Now expand:

$$
\phi(x/t)=\sum_{i=1}^n \left|\frac{x_i}{t}\right|^p =\sum_{i=1}^n \frac{|x_i|^p}{t^p} =\frac{1}{t^p}\sum_{i=1}^n |x_i|^p =\frac{\|x\|_p^p}{t^p}.
$$

Multiply by  $t$ :

$$
\tilde\phi(x,t)=t\cdot \frac{\|x\|_p^p}{t^p} =\frac{\|x\|_p^p}{t^{p-1}} =F(x,t).
$$

So:

$$
\boxed{F=\tilde\phi\ \text{(the perspective of }\phi).}
$$

* * *

Step 3: apply the perspective theorem
-------------------------------------

We proved  $\phi$  is convex. Perspective preserves convexity. Hence  $F$  is convex on  $t>0$ . □

* * *

### Alternative proof idea (same logic, even more “atomic”)

Each scalar term  $\frac{|x_i|^p}{t^{p-1}}$  is the perspective of  $h(u)=|u|^p$ . Since each term is convex in  $(x_i,t)$ , their sum is convex in  $(x,t)$ . This avoids bundling into  $\|x\|_p^p$ , but it’s the same mechanism.

* * *

2) Exercise 3.23(b)
===================

Statement
---------

Prove

$$
f(x)=\frac{\|Ax+b\|_2^2}{c^\top x+d}
$$

is convex on the domain

$$
\{x:\ c^\top x+d>0\}.
$$

You should recognize this as **quadratic-over-linear**, a classic convex form.

I’ll give **two full proofs**:

1.  perspective + affine composition (fast and structural),
2.  epigraph as a rotated second-order cone (conic geometry view).

* * *

Proof 1 (perspective + affine map)
----------------------------------

### Step 1: define a “base” convex function

Let  $\phi(u)=\|u\|_2^2=u^\top u$  on  $\mathbb R^m$ . This is convex (Hessian  $2I\succeq 0$ ).

### Step 2: compute its perspective

$$
\tilde\phi(u,y)=y\,\phi(u/y)=y\left\|\frac{u}{y}\right\|_2^2 = y\cdot \frac{\|u\|_2^2}{y^2} = \frac{\|u\|_2^2}{y}, \quad y>0.
$$

So the function

$$
\psi(u,y):=\frac{\|u\|_2^2}{y}
$$

is exactly the perspective of  $\phi$ , hence **convex in  $(u,y)$ ** on  $y>0$ .

### Step 3: plug in affine functions of  $x$ 

Define

$$
u(x):=Ax+b\quad(\text{affine}),\qquad y(x):=c^\top x+d\quad(\text{affine}).
$$

On the domain,  $y(x)>0$ . Then

$$
f(x)=\psi(u(x),y(x)).
$$

### Step 4: show “convex ∘ affine is convex”

Since  $\psi$  is convex and  $(u(x),y(x))$  is an affine map from  $x$  to  $(u,y)$ , the composition  $x\mapsto \psi(u(x),y(x))$  is convex (direct Jensen proof: affine maps preserve convex combinations).

So  $f$  is convex on  $c^\top x+d>0$ . □

* * *

Proof 2 (epigraph = rotated SOC, fully explicit)
------------------------------------------------

### Step 1: write the epigraph

 $(x,t)\in\mathrm{epi}\,f$  means

$$
\frac{\|Ax+b\|_2^2}{c^\top x+d}\le t,\qquad c^\top x+d>0.
$$

Multiply both sides by the positive number  $c^\top x+d$ :

$$
\|Ax+b\|_2^2 \le t\,(c^\top x+d),\qquad c^\top x+d>0.
$$

Let

$$
u:=Ax+b,\qquad y:=c^\top x+d.
$$

Then the epigraph condition becomes:

$$
\|u\|_2^2 \le t y,\qquad y>0.
$$

### Step 2: recognize the convex cone

The set

$$
\mathcal K:=\{(u,y,t):\ y\ge 0,\ t\ge 0,\ \|u\|_2^2 \le y t\}
$$

is the **rotated second-order cone** (RSOC). It is convex.

If you want a direct convexity proof (no “cone lore”), here is one:

#### Claim:  $\mathcal K$  is convex.

Take  $(u_1,y_1,t_1)$  and  $(u_2,y_2,t_2)$  in  $\mathcal K$ . So

$$
\|u_i\|^2\le y_i t_i,\quad y_i\ge 0,\ t_i\ge 0.
$$

Let  $\theta\in[0,1]$  and define the convex combination

$$
(u,y,t)=\theta(u_1,y_1,t_1)+(1-\theta)(u_2,y_2,t_2).
$$

Then  $y=\theta y_1+(1-\theta)y_2\ge 0$  and  $t=\theta t_1+(1-\theta)t_2\ge 0$  automatically.

Now we must show  $\|u\|^2\le y t$ . Use:

*   convexity of  $\|\cdot\|^2$ :  $\| \theta u_1+(1-\theta)u_2\|^2 \le \theta\|u_1\|^2+(1-\theta)\|u_2\|^2$ ,
*   and the inequality  $\theta a_1+(1-\theta)a_2 \le (\theta y_1+(1-\theta)y_2)(\theta t_1+(1-\theta)t_2)$  when  $a_i=y_i t_i$  and  $y_i,t_i\ge 0$  (this follows because the RHS expands to include cross terms  $ \theta(1-\theta)(y_1 t_2+y_2 t_1)\ge 0$ ).

Concretely:

$$
\|u\|^2 \le \theta\|u_1\|^2+(1-\theta)\|u_2\|^2 \le \theta y_1 t_1+(1-\theta)y_2 t_2 \le (\theta y_1+(1-\theta)y_2)(\theta t_1+(1-\theta)t_2) = y t.
$$

So  $(u,y,t)\in\mathcal K$ . Hence  $\mathcal K$  is convex. □

### Step 3: epigraph is an affine preimage of a convex set

We have

$$
(u,y,t)=(Ax+b,\ c^\top x+d,\ t),
$$

which is an affine map from  $(x,t)$  to  $(u,y,t)$ .

The epigraph of  $f$  is exactly

$$
\mathrm{epi}\,f=\{(x,t): (Ax+b,\ c^\top x+d,\ t)\in\mathcal K,\ c^\top x+d>0\}.
$$

Affine preimages of convex sets are convex, so  $\mathrm{epi}\,f$  is convex, hence  $f$  is convex. □

* * *

3) Relationship to Example 3.20 (nice unification)
==================================================

Part (b) is a direct special case of Example 3.20 with

*   base convex  $f(u)=\|u\|_2^2$ ,
*    $z(x)=Ax+b$ ,
*    $t(x)=c^\top x+d$ ,  
    so
    
$$
g(x)=t(x) f\!\left(\frac{z(x)}{t(x)}\right)=\frac{\|Ax+b\|_2^2}{c^\top x+d}.
$$

* * *

4) Domain sanity checks (don’t skip these)
==========================================

*   In (a),  $t^{p-1}$  is only well-defined as a real number for  $t>0$  (unless you restrict to integer exponents). So the natural domain is  $t>0$ .
*   In (b), multiplying the inequality by  $c^\top x+d$  is only valid without flipping inequality when  $c^\top x+d>0$ . That’s why the domain is exactly that halfspace.

* * *

If you want to keep pushing: the next layer after 3.23 is to compute **gradients/Hessians** of these two functions and verify PSD Hessian directly (it’s messy but educational), and to generalize (b) from  $\|\,\cdot\,\|_2^2$  to any convex  $\phi$  via the perspective template (which is basically Example 3.20 again).

## Prompt:
From below, go for 3.30.

Below are **3.30** and **3.31** done “zero-to-hero,” but I’ll keep the structure tight so you can actually see the machinery.

---

# 3.30 — Convex hull / convex envelope of a function

## 1) Setup: epigraphs and convex hulls

Let (f:\mathbb R^n\to\mathbb R\cup{+\infty}). Its **epigraph** is
[
\operatorname{epi} f := {(x,t)\in\mathbb R^n\times\mathbb R:\ t\ge f(x)}.
]
A function (g) is convex iff (\operatorname{epi} g) is convex.

Define the **convex hull** of a set (S), written (\operatorname{conv} S), as the set of all convex combinations of finitely many points of (S).

The problem defines the convex envelope (g) by
[
g(x):=\inf{t:\ (x,t)\in \operatorname{conv}(\operatorname{epi} f)}.
]
Equivalently: **the epigraph of (g) is the convex hull of the epigraph of (f)** (we’ll prove that precisely).

---

## 2) First claim: (\operatorname{epi} g = \operatorname{conv}(\operatorname{epi} f))

### (⊆) Show (\operatorname{epi} g \subseteq \operatorname{conv}(\operatorname{epi} f))

Take ((x,t)\in \operatorname{epi} g). By definition, (t\ge g(x)=\inf{s:(x,s)\in C}) where (C=\operatorname{conv}(\operatorname{epi} f)).

So for any (\varepsilon>0), there exists (s\le t+\varepsilon) with ((x,s)\in C). Now use that (C) is an epigraph-like set in the vertical direction:

**Key fact (upward closed):** If ((x,s)\in \operatorname{epi} f) then ((x,s+\delta)\in \operatorname{epi} f) for any (\delta\ge 0). Because (s+\delta\ge s\ge f(x)). Therefore (\operatorname{epi} f) is upward closed; convex hull preserves upward-closedness, so (C) is also upward closed: if ((x,s)\in C) then ((x,s+\delta)\in C).

Apply this with (\delta=t-s\ge 0): from ((x,s)\in C) we get ((x,t)\in C). Hence ((x,t)\in \operatorname{conv}(\operatorname{epi} f)).

### (⊇) Show (\operatorname{conv}(\operatorname{epi} f)\subseteq \operatorname{epi} g)

Take ((x,t)\in C=\operatorname{conv}(\operatorname{epi} f)). Then by definition of (g(x)) as the infimum over all such (t) with ((x,t)\in C), we have (g(x)\le t). That is exactly ((x,t)\in\operatorname{epi} g).

So equality holds:
[
\boxed{\operatorname{epi} g = \operatorname{conv}(\operatorname{epi} f).}
]

Immediate consequence: since a convex hull is convex, (\operatorname{epi} g) is convex, hence (g) is convex.

---

## 3) Second claim: (g\le f) (largest convex **underestimator**)

### 3.1 Show (g(x)\le f(x)) for all (x)

Since (\operatorname{epi} f \subseteq \operatorname{conv}(\operatorname{epi} f)), we have ((x,f(x))\in \operatorname{conv}(\operatorname{epi} f)). Therefore by definition of (g(x)) as the infimum of (t) such that ((x,t)) is in that convex hull,
[
g(x)\le f(x).
]

### 3.2 Show the “largest underestimator” property

Assume (h) is convex and (h(x)\le f(x)) for all (x). We must show (h(x)\le g(x)) for all (x).

Since (h\le f), we have epigraph inclusion in the reverse direction:
[
t\ge f(x)\ \Rightarrow\ t\ge h(x)
\quad\Longrightarrow\quad
\operatorname{epi} f \subseteq \operatorname{epi} h.
]
Now (\operatorname{epi} h) is convex (because (h) is convex). The convex hull of (\operatorname{epi} f) is the *smallest convex set containing* (\operatorname{epi} f), so
[
\operatorname{conv}(\operatorname{epi} f) \subseteq \operatorname{epi} h.
]
But (\operatorname{conv}(\operatorname{epi} f)=\operatorname{epi} g) from Section 2, so
[
\operatorname{epi} g \subseteq \operatorname{epi} h.
]
Translate epigraph inclusion to pointwise inequality:

> If (\operatorname{epi} g \subseteq \operatorname{epi} h), then (h(x)\le g(x)) for all (x).
> Proof: ((x,g(x))\in\operatorname{epi} g\subseteq\operatorname{epi} h) implies (g(x)\ge h(x)).

So indeed (h\le g), i.e.
[
\boxed{h(x)\le g(x)\ \ \forall x.}
]
This proves (g) is the **largest convex function dominated by (f)**—the convex envelope.

---

## 4) A concrete “formula” intuition

A point ((x,t)\in \operatorname{conv}(\operatorname{epi} f)) means:
[
(x,t) = \sum_{i=1}^k \theta_i (x_i, t_i),\quad \theta_i\ge 0,\ \sum\theta_i=1,\quad t_i\ge f(x_i).
]
So (x=\sum\theta_i x_i) and (t=\sum\theta_i t_i \ge \sum\theta_i f(x_i)). Taking the **best** such representation yields
[
g(x)=\inf\left{\sum_{i=1}^k \theta_i f(x_i)\ :\ \sum\theta_i=1,\ \theta_i\ge 0,\ \sum\theta_i x_i = x\right},
]
i.e. “the best convex combination bound you can manufacture.” (Carathéodory says you only need (k\le n+2), but that’s extra.)

---

# 3.31 — Largest homogeneous underestimator

Assume (f) is **convex** (as the problem states). Define
[
g(x):=\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}.
]
This is sometimes called a “homogenization” or “gauge-like underestimator.”

We prove:

1. (g) is homogeneous: (g(tx)=t g(x)) for (t\ge 0).
2. (g) is the largest homogeneous underestimator of (f).
3. (g) is convex.

---

## 3.31(a) Homogeneity of (g)

Take (t>0). Compute:
[
g(tx)=\inf_{\alpha>0}\frac{f(\alpha (t x))}{\alpha}.
]
Substitute (\beta=\alpha t) (so (\alpha=\beta/t), and (\beta>0) ranges over all positive reals as (\alpha) does):
[
g(tx)=\inf_{\beta>0}\frac{f(\beta x)}{\beta/t}
= t\inf_{\beta>0}\frac{f(\beta x)}{\beta}
= t g(x).
]

Edge case (t=0): we want (g(0)=0\cdot g(x)=0). Indeed,
[
g(0)=\inf_{\alpha>0}\frac{f(\alpha\cdot 0)}{\alpha}=\inf_{\alpha>0}\frac{f(0)}{\alpha}.
]
If (f(0)>0), this infimum is (0); if (f(0)=0), it is (0); if (f(0)<0), it is (-\infty). In typical BV settings for “underestimator” you’re in the real-valued / proper convex regime where (f(0)) is finite, so (g(0)=0). In any case, for (t>0) the homogeneity identity is clean and is what’s meant.

So:
[
\boxed{g(tx)=t g(x)\quad \forall t\ge 0.}
]

---

## 3.31(b) Largest homogeneous underestimator

We need two things:

### (i) (g(x)\le f(x)) (so it is an underestimator)

Since the infimum is over all (\alpha>0), we can choose (\alpha=1):
[
g(x)=\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}\le \frac{f(1\cdot x)}{1}=f(x).
]
So (g\le f).

### (ii) Any homogeneous (h\le f) satisfies (h\le g)

Let (h) be homogeneous (degree 1): (h(\alpha x)=\alpha h(x)) for (\alpha>0), and assume (h(x)\le f(x)) for all (x).

Fix (x) and any (\alpha>0). Apply (h\le f) at the point (\alpha x):
[
h(\alpha x)\le f(\alpha x).
]
Use homogeneity of (h): (h(\alpha x)=\alpha h(x)). Therefore
[
\alpha h(x)\le f(\alpha x)
\quad\Rightarrow\quad
h(x)\le \frac{f(\alpha x)}{\alpha}.
]
This holds for **every** (\alpha>0). Take the infimum over (\alpha):
[
h(x)\le \inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}=g(x).
]
So (h\le g). That’s exactly “largest homogeneous underestimator.”

---

## 3.31(c) Convexity of (g)

This is the nontrivial part. The cleanest proof uses “inf of convex functions is not always convex” — so we must use a structure that *is* preserved. Here the structure is: (g) is an **infimum over a family of convex functions in ((x,t))** after a clever reparameterization, or equivalently (g) is the support function of a convex set (related to the recession cone of epi(f)). I’ll give a direct Jensen-style proof that avoids that heavy geometry but still uses the convexity of (f) in a controlled way.

### Goal

Show
[
g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y),\quad \theta\in[0,1].
]

### Step 1: Use “almost minimizers” of the inf

Fix (\varepsilon>0). Choose (\alpha_x>0) and (\alpha_y>0) such that
[
\frac{f(\alpha_x x)}{\alpha_x}\le g(x)+\varepsilon,
\qquad
\frac{f(\alpha_y y)}{\alpha_y}\le g(y)+\varepsilon.
]
(We can do this by definition of infimum.)

### Step 2: Create a single scale for the convexity inequality

Let
[
s := \theta \alpha_x + (1-\theta)\alpha_y \quad (>0),
]
and define weights
[
\lambda := \frac{\theta \alpha_x}{s},\qquad 1-\lambda=\frac{(1-\theta)\alpha_y}{s}.
]
Then (\lambda\in[0,1]) and (\lambda+(1-\lambda)=1).

Now observe the key algebra identity:
[
s(\theta x+(1-\theta)y)
= \theta s x + (1-\theta) s y
= \theta\alpha_x x + (1-\theta)\alpha_y y
= \lambda(\alpha_x x) + (1-\lambda)(\alpha_y y),,,\text{scaled by }s?
]
Be careful: we want it *exactly* as a convex combination of (\alpha_x x) and (\alpha_y y).

Compute:
[
\lambda(\alpha_x x) + (1-\lambda)(\alpha_y y)
= \frac{\theta\alpha_x}{s}(\alpha_x x) + \frac{(1-\theta)\alpha_y}{s}(\alpha_y y)
= \frac{1}{s}\big(\theta\alpha_x^2 x + (1-\theta)\alpha_y^2 y\big),
]
which is **not** what we want. So that attempt is wrong.

We need a different trick: choose a *common* scaling (\alpha) and use convexity in the *original* (x)-space.

### Step 2 (correct): choose a single (\alpha) and compare

For any (\alpha>0),
[
g(\theta x+(1-\theta)y)
=\inf_{\beta>0}\frac{f(\beta(\theta x+(1-\theta)y))}{\beta}
\le \frac{f(\alpha(\theta x+(1-\theta)y))}{\alpha}.
]
Now use convexity of (f) at the points (\alpha x) and (\alpha y):
[
f(\alpha(\theta x+(1-\theta)y))
=f(\theta(\alpha x)+(1-\theta)(\alpha y))
\le \theta f(\alpha x)+(1-\theta)f(\alpha y).
]
Divide by (\alpha):
[
\frac{f(\alpha(\theta x+(1-\theta)y))}{\alpha}
\le \theta \frac{f(\alpha x)}{\alpha}+(1-\theta)\frac{f(\alpha y)}{\alpha}.
]
So we have, for every (\alpha>0),
[
g(\theta x+(1-\theta)y)
\le \theta \frac{f(\alpha x)}{\alpha}+(1-\theta)\frac{f(\alpha y)}{\alpha}.
]
Now take infimum over (\alpha>0) on the right side. Use the elementary inequality
[
\inf_\alpha\big(\theta A_\alpha+(1-\theta)B_\alpha\big)
\le \theta \inf_\alpha A_\alpha + (1-\theta)\inf_\alpha B_\alpha
]
(because for any fixed (\alpha), (\theta A_\alpha+(1-\theta)B_\alpha) is ≥ the inf over (\alpha) of that expression, and choosing (\alpha) that is separately good for (A) and (B) can only decrease the RHS bound). More formally: for any (\varepsilon>0), pick (\alpha_1) near-minimizer for (A) and (\alpha_2) for (B); then compare with (\alpha=\alpha_1) and (\alpha=\alpha_2) and let (\varepsilon\to0). The inequality is standard and true.

Apply it with
[
A_\alpha=\frac{f(\alpha x)}{\alpha},\qquad B_\alpha=\frac{f(\alpha y)}{\alpha}.
]
Then
[
\inf_{\alpha>0}\left[\theta \frac{f(\alpha x)}{\alpha}+(1-\theta)\frac{f(\alpha y)}{\alpha}\right]
\le \theta \inf_{\alpha>0}\frac{f(\alpha x)}{\alpha} + (1-\theta)\inf_{\alpha>0}\frac{f(\alpha y)}{\alpha}
=\theta g(x)+(1-\theta)g(y).
]
Therefore
[
\boxed{g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y).}
]
So (g) is convex.

**What made it work?** We never used “inf of convex is convex” (false in general). Instead we used:

* convexity of (f) to produce a bound valid for every (\alpha),
* then took infimum at the very end with a direction of inequality that is safe.

---

# Final “memory hooks”

* **3.30:** convex envelope = function whose epigraph is (\operatorname{conv}(\operatorname{epi}f)). Largest convex under (f) because any convex underestimator has an epigraph that must contain that convex hull.
* **3.31:** “homogenize” a convex (f) by
  [
  g(x)=\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}.
  ]
  This forces 1-homogeneity. It stays below (f). Any other homogeneous underestimator lies below it. Convexity comes from applying convexity of (f) at a common scale (\alpha) and taking the infimum at the end.

If you want, I can also connect 3.31 to **recession functions / gauges / Minkowski functionals** and show that (g) is essentially the “best conic (homogeneous) approximation from below” to (f), with a clean epigraph-cone picture.

## Response:
Thought for 2m 6s

Example 3.30 (BV) — Convex hull / convex envelope of a function, from bedrock
-----------------------------------------------------------------------------

We start with an arbitrary extended-value function

$$
f:\mathbb R^n\to \mathbb R\cup\{+\infty\}.
$$

We define

$$
E := \operatorname{epi} f = \{(x,t)\in\mathbb R^{n}\times\mathbb R:\ t\ge f(x)\}.
$$

Let

$$
C := \operatorname{conv}(E)
$$

(the set of all **finite convex combinations** of points in  $E$ ).

Then define the function  $g$  by

$$
\boxed{ g(x):=\inf\{t\in\mathbb R:\ (x,t)\in C\}. }
$$

(If the set is empty, we interpret the infimum as  $+\infty$ .)

**Goal (what Example 3.30 is really saying):**

1.   $g$  is convex.
2.   $g\le f$ .
3.   $g$  is the **largest convex function dominated by  $f$ ** (the convex envelope / convex hull of  $f$ ).

I’ll prove these with maximum granularity, and I’ll also give the “explicit formula” for  $g$  as an infimum over convex combinations of  $f(x_i)$ .

* * *

0) Three tiny but crucial lemmas
================================

Lemma 0.1 (epigraph convex ⇔ function convex)
---------------------------------------------

A function  $h:\mathbb R^n\to\mathbb R\cup\{+\infty\}$  is convex iff its epigraph

$$
\operatorname{epi}h=\{(x,t): t\ge h(x)\}
$$

is a convex set in  $\mathbb R^{n+1}$ .

### Proof (both directions, no handwaving)

**( $\Rightarrow$ )** Assume  $h$  convex. Take any two points  $(x_1,t_1),(x_2,t_2)\in\operatorname{epi}h$ . That means

$$
t_1\ge h(x_1),\qquad t_2\ge h(x_2).
$$

For  $\theta\in[0,1]$ , define

$$
(x_\theta,t_\theta):=\theta(x_1,t_1)+(1-\theta)(x_2,t_2) =(\theta x_1+(1-\theta)x_2,\ \theta t_1+(1-\theta)t_2).
$$

We want to show  $(x_\theta,t_\theta)\in\operatorname{epi}h$ , i.e.  $t_\theta\ge h(x_\theta)$ .

Convexity of  $h$  gives

$$
h(x_\theta)=h(\theta x_1+(1-\theta)x_2) \le \theta h(x_1)+(1-\theta)h(x_2).
$$

Since  $t_i\ge h(x_i)$ , multiply by weights and add:

$$
\theta t_1+(1-\theta)t_2 \ge \theta h(x_1)+(1-\theta)h(x_2).
$$

Combine the two inequalities:

$$
t_\theta=\theta t_1+(1-\theta)t_2 \ge h(x_\theta).
$$

So  $(x_\theta,t_\theta)\in\operatorname{epi}h$ . Hence  $\operatorname{epi}h$  is convex.

**( $\Leftarrow$ )** Assume  $\operatorname{epi}h$  is convex. Take any  $x_1,x_2$  and  $\theta\in[0,1]$ . Points  $(x_1,h(x_1))$  and  $(x_2,h(x_2))$  belong to the epigraph because  $h(x_i)\ge h(x_i)$  (trivial). By convexity of the epigraph,

$$
(\theta x_1+(1-\theta)x_2,\ \theta h(x_1)+(1-\theta)h(x_2))\in\operatorname{epi}h.
$$

That means

$$
h(\theta x_1+(1-\theta)x_2)\le \theta h(x_1)+(1-\theta)h(x_2),
$$

which is exactly convexity of  $h$ . □

* * *

Lemma 0.2 (epigraphs are “upward closed”)
-----------------------------------------

If  $(x,t)\in\operatorname{epi}f$  and  $\delta\ge 0$ , then  $(x,t+\delta)\in\operatorname{epi}f$ .

### Proof

 $(x,t)\in\operatorname{epi}f$  means  $t\ge f(x)$ . Then  $t+\delta\ge t\ge f(x)$ . So  $(x,t+\delta)\in\operatorname{epi}f$ . □

* * *

Lemma 0.3 (convex hull preserves upward-closedness)
---------------------------------------------------

If a set  $S\subset\mathbb R^{n+1}$  is upward closed in the  $t$ \-direction (i.e.  $(x,t)\in S\Rightarrow (x,t+\delta)\in S$  for all  $\delta\ge 0$ ), then  $\operatorname{conv}(S)$  is also upward closed.

### Proof (explicit)

Take  $(x,t)\in\operatorname{conv}(S)$ . By definition of convex hull, there exist points  $(x_i,t_i)\in S$  and weights  $\theta_i\ge 0$ ,  $\sum_{i=1}^k\theta_i=1$ , such that

$$
(x,t)=\sum_{i=1}^k \theta_i (x_i,t_i).
$$

Now fix  $\delta\ge 0$ . Because  $S$  is upward closed, each  $(x_i,t_i+\delta)\in S$ . Take the same convex combination:

$$
\sum_{i=1}^k \theta_i (x_i,t_i+\delta) = \sum_{i=1}^k \theta_i (x_i,t_i) + \sum_{i=1}^k \theta_i (0,\delta) = (x,t) + (0,\delta\sum\theta_i) = (x,t)+(0,\delta) = (x,t+\delta).
$$

So  $(x,t+\delta)$  is a convex combination of points in  $S$ , hence belongs to  $\operatorname{conv}(S)$ . □

Apply this with  $S=\operatorname{epi}f$ : since epigraphs are upward closed, so is  $C=\operatorname{conv}(\operatorname{epi}f)$ .

* * *

1) What does it mean for  $(x,t)$  to be in  $\operatorname{conv}(\operatorname{epi}f)$ ?
=========================================================================================

This is the key “unpacking” step that makes everything concrete.

Let  $E=\operatorname{epi}f$ . Then  $(x,t)\in C=\operatorname{conv}(E)$  means:

> There exist an integer  $k\ge 1$ , weights  $\theta_1,\dots,\theta_k$  with  $\theta_i\ge 0$  and  $\sum\theta_i=1$ , and points  $(x_i,t_i)\in E$  such that
> 
> $$
> (x,t)=\sum_{i=1}^k \theta_i (x_i,t_i).
> $$

Write this componentwise:

$$
x=\sum_{i=1}^k \theta_i x_i, \qquad t=\sum_{i=1}^k \theta_i t_i, \qquad \text{with } t_i\ge f(x_i)\ \text{for each }i.
$$

Now notice an important monotonicity fact: since each  $t_i$  only needs to be **at least**  $f(x_i)$ , the smallest  $t$  you can get from a fixed representation  $(\theta_i,x_i)$  is achieved by taking  $t_i=f(x_i)$ . So every feasible representation implies

$$
t=\sum\theta_i t_i \ \ge\ \sum\theta_i f(x_i).
$$

Conversely, if you can arrange  $x=\sum\theta_i x_i$  and some number  $t$  satisfies

$$
t \ge \sum_{i=1}^k \theta_i f(x_i),
$$

then you can _force_  $(x,t)\in C$  by choosing suitable  $t_i\ge f(x_i)$  whose convex average equals  $t$ . One explicit construction:

*   Pick any index  $j$  with  $\theta_j>0$  (there is always at least one because  $\sum\theta_i=1$ ).
*   Define
    $$
    t_i:=f(x_i)\ \ (i\neq j),\qquad t_j:=f(x_j)+\frac{t-\sum_{i=1}^k \theta_i f(x_i)}{\theta_j}.
    $$
    The fraction is  $\ge 0$  because  $t\ge\sum\theta_i f(x_i)$ , so  $t_j\ge f(x_j)$ . Then
    $$
    \sum_{i=1}^k \theta_i t_i = \sum_{i=1}^k \theta_i f(x_i) + \theta_j\cdot \frac{t-\sum\theta_i f(x_i)}{\theta_j} =t.
    $$
    So  $(x,t)=\sum\theta_i(x_i,t_i)$  with each  $(x_i,t_i)\in E$ , hence  $(x,t)\in C$ .

So we have a fully explicit characterization:

$$
\boxed{ (x,t)\in \operatorname{conv}(\operatorname{epi}f) \iff \exists k,\ \theta_i\ge 0,\ \sum\theta_i=1,\ x_i:\ x=\sum\theta_i x_i,\ \ t\ge \sum\theta_i f(x_i). }
$$

This is the “epigraph-like” description of the convex hull.

* * *

2) Derive the explicit “formula” for  $g(x)$ 
=============================================

Recall:

$$
g(x)=\inf\{t:\ (x,t)\in C\}.
$$

Using the characterization above, “ $(x,t)\in C$ ” means “there exists a representation  $x=\sum\theta_i x_i$  such that  $t\ge \sum\theta_i f(x_i)$ .”

So for a fixed representation  $(\theta_i,x_i)$ , the smallest permissible  $t$  is exactly  $\sum\theta_i f(x_i)$ . Therefore, when you take the inf over all  $t$  such that such a representation exists, you are equivalently taking the inf over all representations of that sum:

$$
\boxed{ g(x) = \inf\left\{ \sum_{i=1}^k \theta_i f(x_i)\ :\ k\ge 1,\ \theta_i\ge 0,\ \sum\theta_i=1,\ \sum\theta_i x_i = x \right\}. }
$$

This is the “best convex combination bound you can manufacture.”

**Interpretation:** you are allowed to “explain”  $x$  as a convex combination of other points  $x_i$ , and pay the convex combination of their  $f$ \-values;  $g(x)$  is the cheapest possible such payment.

* * *

3) Prove  $g$  is convex (two equivalent proofs)
================================================

I’ll give both:

*   Proof A: epigraph convexity (aligned with BV),
*   Proof B: direct Jensen using the explicit representation formula.

Proof A (epigraph is convex)
----------------------------

### Step 1: compute  $\operatorname{epi}g$  explicitly

By definition:

$$
(x,t)\in\operatorname{epi}g \iff t\ge g(x).
$$

Using the formula for  $g(x)$  as an infimum:

$$
t\ge \inf_{\text{reps}} \sum\theta_i f(x_i) \iff \exists\text{ a representation such that } t\ge \sum\theta_i f(x_i).
$$

So:

$$
\boxed{ (x,t)\in\operatorname{epi}g \iff \exists k,\theta_i,x_i:\ x=\sum\theta_i x_i,\ \ t\ge \sum\theta_i f(x_i). }
$$

But that is **exactly** the characterization we already proved for membership in  $C=\operatorname{conv}(\operatorname{epi}f)$ . Hence:

$$
\boxed{\operatorname{epi}g = \operatorname{conv}(\operatorname{epi}f).}
$$

(Here’s the subtlety: if the inf is not attained at some  $x$ ,  $(x,g(x))$  is still in  $\operatorname{epi}g$  by definition; the characterization above shows it’s also in the convex hull iff the inf is attainable by a finite convex combination. In many BV setups, this “attainment vs closure” subtlety is ignored; if you want the pedantic version, the clean always-true statement is  $\operatorname{epi}g$  is the **smallest epigraph containing**  $\operatorname{conv}(\operatorname{epi}f)$ , and equals its “vertical closure.” If you want, I’ll show an explicit example where the boundary is not attained.)

### Step 2: conclude convexity

 $\operatorname{conv}(\operatorname{epi}f)$  is convex by definition (it’s a convex hull). Therefore  $\operatorname{epi}g$  is convex. By Lemma 0.1,  $g$  is convex. □

* * *

Proof B (direct Jensen from the “representation infimum”)
---------------------------------------------------------

We want:

$$
g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y).
$$

Fix  $\varepsilon>0$ . By definition of infimum, choose representations (possibly with different numbers of points):

*   For  $x$ : pick  $k$ ,  $\theta_i$ ,  $x_i$  such that  $\sum\theta_i x_i=x$  and
    $$
    \sum_{i=1}^k \theta_i f(x_i)\le g(x)+\varepsilon.
    $$
*   For  $y$ : pick  $\ell$ ,  $\eta_j$ ,  $y_j$  such that  $\sum\eta_j y_j=y$  and
    $$
    \sum_{j=1}^\ell \eta_j f(y_j)\le g(y)+\varepsilon.
    $$

Now build a representation for  $x_\theta:=\theta x+(1-\theta)y$  by concatenating the two lists:

*   weights:  $\{\theta\theta_i\}_{i=1}^k$  and  $\{(1-\theta)\eta_j\}_{j=1}^\ell$ ,
*   points:  $x_i$  and  $y_j$ .

Check weights are valid:

*   nonnegative,
*   sum to  $\theta\sum\theta_i + (1-\theta)\sum\eta_j = \theta + (1-\theta)=1$ .

Check the convex combination equals  $x_\theta$ :

$$
\sum_{i=1}^k (\theta\theta_i)x_i + \sum_{j=1}^\ell((1-\theta)\eta_j)y_j = \theta\sum_{i=1}^k\theta_i x_i + (1-\theta)\sum_{j=1}^\ell\eta_j y_j = \theta x+(1-\theta)y =x_\theta.
$$

Therefore this is a feasible representation in the inf defining  $g(x_\theta)$ . So

$$
g(x_\theta)\le \sum_{i=1}^k (\theta\theta_i)f(x_i)+\sum_{j=1}^\ell((1-\theta)\eta_j)f(y_j) = \theta\sum_{i=1}^k\theta_i f(x_i)+(1-\theta)\sum_{j=1}^\ell\eta_j f(y_j).
$$

Use the near-optimality bounds:

$$
g(x_\theta)\le \theta(g(x)+\varepsilon)+(1-\theta)(g(y)+\varepsilon) = \theta g(x)+(1-\theta)g(y)+\varepsilon.
$$

Now send  $\varepsilon\downarrow 0$ :

$$
g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y).
$$

So  $g$  is convex. □

This proof never mentions epigraphs at all; it comes straight from the “inf over convex decompositions” formula.

* * *

4) Prove  $g\le f$ 
===================

This is quick but we’ll still do it slowly.

Take any  $x$ . In the inf defining  $g(x)$ , we are allowed to choose  $k=1$ ,  $\theta_1=1$ ,  $x_1=x$ . Then the constraint  $\sum\theta_i x_i=x$  holds. The objective becomes

$$
\sum_{i=1}^1 \theta_i f(x_i)=1\cdot f(x)=f(x).
$$

Since  $g(x)$  is the **infimum** over all such constructions,

$$
\boxed{g(x)\le f(x)\quad\forall x.}
$$

So  $g$  is a convex underestimator of  $f$ .

* * *

5) Prove  $g$  is the _largest_ convex underestimator of  $f$ 
==============================================================

Let  $h$  be **any** convex function with  $h\le f$  pointwise. We prove:

$$
\boxed{h\le g.}
$$

Take any  $x$ . Consider **any** representation  $x=\sum_{i=1}^k\theta_i x_i$  with  $\theta_i\ge 0$ ,  $\sum\theta_i=1$ .

Since  $h$  is convex, Jensen’s inequality gives:

$$
h(x)=h\Big(\sum_{i=1}^k \theta_i x_i\Big)\le \sum_{i=1}^k \theta_i h(x_i).
$$

Since  $h\le f$ , we have  $h(x_i)\le f(x_i)$  for each  $i$ , hence

$$
\sum_{i=1}^k \theta_i h(x_i)\le \sum_{i=1}^k \theta_i f(x_i).
$$

Combine:

$$
h(x)\le \sum_{i=1}^k \theta_i f(x_i).
$$

This is true for **every** representation. Therefore it is true for the infimum over all representations:

$$
h(x)\le \inf_{\text{reps}}\sum_{i=1}^k \theta_i f(x_i)=g(x).
$$

So  $h(x)\le g(x)$  for all  $x$ . That proves the “largest underestimator” property.

* * *

6) (Optional but powerful) Carathéodory bound: you only need  $n+2$  points
===========================================================================

Because all geometry happens in  $\mathbb R^{n+1}$ , Carathéodory’s theorem says:

> Any point in  $\operatorname{conv}(E)\subset\mathbb R^{n+1}$  can be expressed as a convex combination of at most  $n+2$  points of  $E$ .

So in the explicit formula for  $g(x)$ , it is enough to consider  $k\le n+2$ . This is often used to argue “finite-dimensional” behavior.

If you want, I can also prove Carathéodory line-by-line; it’s a bit of linear algebra (dependence among  $n+3$  points ⇒ you can drop one without changing the convex combination).

* * *

7) A very important nuance (the “closure” subtlety)
===================================================

*    $\operatorname{conv}(\operatorname{epi}f)$  is always convex and upward closed.
*   But it need **not** be closed, and in principle it can miss some boundary points  $(x,\inf t)$ .
*   The function  $g$  is defined using an infimum, so its epigraph is “convex hull + add missing boundary points at each vertical slice.”

BV often sweeps this under the rug because:

*   convexity doesn’t require closedness,
*   many standard  $f$ ’s are “nice” enough (proper, lower semicontinuous) that the **closed convex envelope** is what you really want anyway.

Alternative viewpoint (if  $f$  is proper and lsc): the **closed** convex envelope equals  $f^{**}$  (Fenchel biconjugate). That’s a beautiful “dual” way to compute the envelope.

* * *

Final takeaway (one sentence, but true)
---------------------------------------

$$
\boxed{ g(x)=\inf\Big\{\sum_{i}\theta_i f(x_i)\ :\ \sum_i\theta_i=1,\ \theta_i\ge 0,\ \sum_i\theta_i x_i=x\Big\} }
$$

is convex, satisfies  $g\le f$ , and dominates every other convex  $h\le f$ . That’s exactly “convex envelope.”

If you paste the exact BV statement of Example 3.30 (sometimes they add “closed convex hull” language), I’ll match the proof to their precise wording and flag where the closure issue matters or doesn’t.

## Prompt:
3.31.

## Response:
Thought for 2m 13s

Example 3.31 (BV) — Largest homogeneous underestimator (“homogenization”), from bedrock
---------------------------------------------------------------------------------------

We assume throughout that

*    $f:\mathbb R^n\to \mathbb R\cup\{+\infty\}$  is **convex** (extended-value convexity allowed),
*   and we define
    $$
    \boxed{ g(x):=\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}. }
    $$

This construction forces **positive homogeneity of degree 1** (“scale in, scale out”), while staying **below**  $f$ . The nontrivial part is proving  $g$  is convex (even though it’s an infimum).

I’ll prove:

1.   $g$  is (positively) homogeneous:  $g(tx)=t\,g(x)$  for  $t>0$  (and discuss  $t=0$ ).
2.   $g\le f$ .
3.   $g$  is the **largest** homogeneous underestimator of  $f$ .
4.   $g$  is **convex** (two proofs: a clean algebraic Jensen proof + a geometric epigraph/cone proof).
5.  Bonus: convex + homogeneous ⇒ **subadditive**, so  $g$  is actually **sublinear** (a gauge/support-function–type object).

* * *

0) Definitions (so nothing is implicit)
=======================================

0.1 Convexity (extended value)
------------------------------

 $f$  is convex if for all  $x,y\in\mathbb R^n$  and  $\theta\in[0,1]$ ,

$$
f(\theta x+(1-\theta)y)\ \le\ \theta f(x)+(1-\theta)f(y),
$$

with the standard convention that  $a\le +\infty$  is always true, etc.

0.2 Positive homogeneity (degree 1)
-----------------------------------

A function  $h$  is **(positively) homogeneous of degree 1** if

$$
h(tx)=t\,h(x)\qquad \forall x,\ \forall t\ge 0.
$$

(Some authors only demand this for  $t>0$ . The  $t=0$  case is a subtle corner; we’ll handle it explicitly.)

0.3 “Underestimator”
--------------------

 $h$  is an underestimator of  $f$  if  $h(x)\le f(x)$  for all  $x$ .

* * *

1)  $g$  is homogeneous (the scaling trick, fully spelled out)
==============================================================

Take  $t>0$ . Start from the definition:

$$
g(tx)=\inf_{\alpha>0}\frac{f(\alpha(tx))}{\alpha} =\inf_{\alpha>0}\frac{f((\alpha t)x)}{\alpha}.
$$

Now do a **change of variable** (this is the whole move):

*   Let  $\beta=\alpha t$ .
*   Since  $t>0$ , the map  $\alpha\mapsto \beta$  is a bijection from  $(0,\infty)$  to  $(0,\infty)$ .
*   Also  $\alpha=\beta/t$ .

Substitute:

$$
g(tx)=\inf_{\beta>0}\frac{f(\beta x)}{\beta/t} =t\inf_{\beta>0}\frac{f(\beta x)}{\beta} =t\,g(x).
$$

So:

$$
\boxed{g(tx)=t\,g(x)\quad\text{for all }t>0.}
$$

### What about  $t=0$ ?

$$
g(0)=\inf_{\alpha>0}\frac{f(\alpha\cdot 0)}{\alpha}=\inf_{\alpha>0}\frac{f(0)}{\alpha}.
$$
*   If  $f(0)>0$ , then  $f(0)/\alpha\to 0$  as  $\alpha\to\infty$ , so  $g(0)=0$ .
*   If  $f(0)=0$ , then  $g(0)=0$ .
*   If  $f(0)<0$ , then  $f(0)/\alpha<0$  and the inf over  $\alpha>0$  is  $-\infty$  (because as  $\alpha\downarrow 0$ ,  $f(0)/\alpha\to -\infty$ ). So  $g(0)=-\infty$ .

BV usually lives in the “proper convex / reasonable” regime where you don’t want  $-\infty$  popping up, often with  $f(0)\ge 0$  or  $f(0)=0$ . In that common case,  $g(0)=0$  and homogeneity holds for all  $t\ge 0$ .

* * *

2)  $g\le f$  (underestimator property)
=======================================

This is literally “inf ≤ one particular choice”.

Because the infimum is over **all**  $\alpha>0$ , we may choose  $\alpha=1$ :

$$
g(x)=\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha} \le \frac{f(1\cdot x)}{1} =f(x).
$$

So:

$$
\boxed{g(x)\le f(x)\quad\forall x.}
$$

* * *

3)  $g$  is the **largest** homogeneous underestimator
======================================================

Let  $h$  be **any** homogeneous function (degree 1) such that  $h\le f$ . We prove  $h\le g$ .

Fix an arbitrary  $x\in\mathbb R^n$ . For every  $\alpha>0$ , apply  $h\le f$  at the point  $\alpha x$ :

$$
h(\alpha x)\le f(\alpha x).
$$

Now use homogeneity of  $h$ :  $h(\alpha x)=\alpha h(x)$ . Substitute:

$$
\alpha h(x)\le f(\alpha x).
$$

Divide both sides by  $\alpha>0$ :

$$
h(x)\le \frac{f(\alpha x)}{\alpha}.
$$

This holds for **every**  $\alpha>0$ , so it holds for the infimum over  $\alpha$ :

$$
h(x)\le \inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}=g(x).
$$

Since  $x$  was arbitrary:

$$
\boxed{h\le g.}
$$

Combine with  $g\le f$ :  $g$  is the **largest** (pointwise maximal) homogeneous function lying under  $f$ .

Notice: we did **not** assume  $h$  is convex. The “largest homogeneous underestimator” part is purely algebraic.

* * *

4) Convexity of  $g$  — the important part
==========================================

This is where people commonly slip: “inf of convex functions is convex” is **false** in general. So we need to use special structure.

I’ll give two proofs.

* * *

Proof 1 (direct Jensen, with the _correct_ scaling choice)
----------------------------------------------------------

### Goal

Show for all  $x,y$  and  $\theta\in[0,1]$ ,

$$
g(\theta x+(1-\theta)y)\ \le\ \theta g(x)+(1-\theta)g(y).
$$

### Step 1: pick near-minimizers for  $g(x)$  and  $g(y)$ 

Fix  $\varepsilon>0$ . By definition of infimum, we can choose  $\alpha_1>0$ ,  $\alpha_2>0$  such that

$$
\frac{f(\alpha_1 x)}{\alpha_1}\le g(x)+\varepsilon, \qquad \frac{f(\alpha_2 y)}{\alpha_2}\le g(y)+\varepsilon.
$$

(That’s what “infimum” means: you can get within  $\varepsilon$  of it.)

### Step 2: the key trick — choose ONE  $\alpha$  that makes a convex combination work

Let

$$
z:=\theta x+(1-\theta)y.
$$

We want to use convexity of  $f$ , which demands something like

$$
f(\text{convex combo of two points}) \le \text{same combo of }f(\text{those points}).
$$

So we want to express  $\alpha z$  as a convex combination of  $\alpha_1 x$  and  $\alpha_2 y$ :

$$
\alpha z = \lambda (\alpha_1 x) + (1-\lambda)(\alpha_2 y) \quad\text{for some }\lambda\in[0,1].
$$

Expand the left side:

$$
\alpha z = \alpha(\theta x+(1-\theta)y)= (\alpha\theta)x+(\alpha(1-\theta))y.
$$

So we want coefficients to match:

$$
\lambda\alpha_1 = \alpha\theta, \qquad (1-\lambda)\alpha_2 = \alpha(1-\theta).
$$

Solve these two equations by defining  $\lambda$  in terms of  $\alpha$ :

$$
\lambda = \frac{\alpha\theta}{\alpha_1}, \qquad 1-\lambda = \frac{\alpha(1-\theta)}{\alpha_2}.
$$

Now enforce  $\lambda+(1-\lambda)=1$ . That gives a condition on  $\alpha$ :

$$
\frac{\alpha\theta}{\alpha_1} + \frac{\alpha(1-\theta)}{\alpha_2} = 1 \quad\Longleftrightarrow\quad \alpha\Big(\frac{\theta}{\alpha_1}+\frac{1-\theta}{\alpha_2}\Big)=1.
$$

Thus choose

$$
\boxed{ \alpha := \frac{1}{\frac{\theta}{\alpha_1}+\frac{1-\theta}{\alpha_2}} }
$$

(a weighted harmonic mean of  $\alpha_1,\alpha_2$ ).

With this  $\alpha$ , the resulting  $\lambda=\alpha\theta/\alpha_1$  automatically lies in  $[0,1]$  because  $\alpha\le \alpha_1/\theta$  when  $\theta>0$  (and similarly for the other side). Endpoints  $\theta=0,1$  are trivial anyway.

So we have constructed:

$$
\boxed{ \alpha z = \lambda(\alpha_1 x) + (1-\lambda)(\alpha_2 y) \quad\text{with }\lambda\in[0,1]. }
$$

### Step 3: apply convexity of  $f$ 

Convexity gives

$$
f(\alpha z) \le \lambda f(\alpha_1 x) + (1-\lambda) f(\alpha_2 y).
$$

### Step 4: divide by  $\alpha$  and simplify the coefficients

Divide both sides by  $\alpha>0$ :

$$
\frac{f(\alpha z)}{\alpha} \le \frac{\lambda}{\alpha} f(\alpha_1 x) + \frac{1-\lambda}{\alpha} f(\alpha_2 y).
$$

Now compute  $\lambda/\alpha$  and  $(1-\lambda)/\alpha$  using the definitions:

$$
\lambda=\frac{\alpha\theta}{\alpha_1}\quad\Rightarrow\quad \frac{\lambda}{\alpha}=\frac{\theta}{\alpha_1},
$$
 
$$
1-\lambda=\frac{\alpha(1-\theta)}{\alpha_2}\quad\Rightarrow\quad \frac{1-\lambda}{\alpha}=\frac{1-\theta}{\alpha_2}.
$$

So the inequality becomes:

$$
\frac{f(\alpha z)}{\alpha} \le \theta\frac{f(\alpha_1 x)}{\alpha_1} + (1-\theta)\frac{f(\alpha_2 y)}{\alpha_2}.
$$

### Step 5: replace the ratios by  $g+\varepsilon$ 

Using the  $\varepsilon$ \-near-minimizer bounds:

$$
\frac{f(\alpha_1 x)}{\alpha_1}\le g(x)+\varepsilon,\qquad \frac{f(\alpha_2 y)}{\alpha_2}\le g(y)+\varepsilon,
$$

we get

$$
\frac{f(\alpha z)}{\alpha} \le \theta(g(x)+\varepsilon)+(1-\theta)(g(y)+\varepsilon) = \theta g(x)+(1-\theta)g(y)+\varepsilon.
$$

### Step 6: go from one  $\alpha$  to  $g(z)$ 

By definition of  $g(z)$  as an infimum,

$$
g(z)=\inf_{\beta>0}\frac{f(\beta z)}{\beta} \le \frac{f(\alpha z)}{\alpha}.
$$

So combine:

$$
g(z)\le \theta g(x)+(1-\theta)g(y)+\varepsilon.
$$

Let  $\varepsilon\downarrow 0$ :

$$
\boxed{ g(\theta x+(1-\theta)y)\le \theta g(x)+(1-\theta)g(y). }
$$

That is convexity. □

**Important meta-lesson:** the proof works because we chose  $\alpha$  _dependent on_  $\alpha_1,\alpha_2,\theta$  so that the convexity inequality for  $f$  applies to exactly the right scaled point.

* * *

Proof 2 (geometry): epigraph of  $g$  is the conic hull of epigraph of  $f$ 
----------------------------------------------------------------------------

This is the “BV-style picture proof,” and it’s very enlightening.

### Step 1: epigraph of  $f$  is convex

Since  $f$  is convex,

$$
\mathrm{epi}\,f=\{(x,t): t\ge f(x)\}
$$

is a convex subset of  $\mathbb R^{n+1}$ .

### Step 2: take the conic hull (“cone over the epigraph”)

Define

$$
K := \operatorname{cone}(\mathrm{epi}\,f) :=\{\lambda (x,t): \lambda\ge 0,\ (x,t)\in \mathrm{epi}\,f\}.
$$

This is a **convex cone** (scaling + convexity; you can check directly).

### Step 3: identify  $g$  as the “height function” of this cone

Fix  $x$ . Look at the set of  $t$  such that  $(x,t)\in K$ . By definition,  
 $(x,t)\in K$  means: there exist  $\lambda>0$  and  $(u,s)\in\mathrm{epi}\,f$  such that

$$
(x,t)=\lambda(u,s).
$$

So  $u=x/\lambda$ ,  $s=t/\lambda$ , and  $s\ge f(u)=f(x/\lambda)$ . That is

$$
\frac{t}{\lambda}\ge f\Big(\frac{x}{\lambda}\Big) \quad\Longleftrightarrow\quad t\ge \lambda\, f(x/\lambda).
$$

Let  $\alpha:=1/\lambda$ . Then this becomes

$$
t\ge \frac{f(\alpha x)}{\alpha}.
$$

So the **smallest** such  $t$  is exactly

$$
\inf_{\alpha>0}\frac{f(\alpha x)}{\alpha}=g(x).
$$

So geometrically: ** $\mathrm{epi}\,g$ ** is (essentially) the cone generated by  $\mathrm{epi}\,f$  (up to the usual “boundary attainment” closure nuance).

Since  $K$  is convex,  $\mathrm{epi}\,g$  is convex, hence  $g$  is convex.

This proof is basically “convex + homogeneous ⇔ epigraph is a convex cone.”

* * *

5) Bonus: convex + homogeneous ⇒ subadditive (so  $g$  is sublinear)
====================================================================

Once you know  $g$  is convex and  $g(tx)=t g(x)$  for  $t>0$ , you automatically get

$$
g(x+y)\le g(x)+g(y).
$$

**Proof (don’t skip steps):**  
Convexity at midpoint:

$$
g\Big(\frac{x+y}{2}\Big)\le \frac{g(x)+g(y)}{2}.
$$

Now use homogeneity with  $t=2$ :

$$
g(x+y)=g\Big(2\cdot\frac{x+y}{2}\Big)=2g\Big(\frac{x+y}{2}\Big).
$$

Combine:

$$
g(x+y)\le 2\cdot \frac{g(x)+g(y)}{2}=g(x)+g(y).
$$

So  $g$  is **subadditive**. Together with positive homogeneity,  $g$  is **sublinear** (a gauge-like function).

That’s why this construction is often called a “sublinearization/homogenization” of  $f$ .

* * *

6) Sanity-check examples (so the definition doesn’t feel like witchcraft)
=========================================================================

Example A:  $f$  already homogeneous (degree 1)
-----------------------------------------------

If  $f(\alpha x)=\alpha f(x)$ , then

$$
g(x)=\inf_{\alpha>0}\frac{\alpha f(x)}{\alpha}=f(x).
$$

So the operation leaves truly homogeneous functions unchanged.

Example B:  $f(x)=\|x\|_2^2$ 
-----------------------------

$$
g(x)=\inf_{\alpha>0}\frac{\|\alpha x\|^2}{\alpha} =\inf_{\alpha>0}\frac{\alpha^2\|x\|^2}{\alpha} =\inf_{\alpha>0}\alpha\|x\|^2=0.
$$

So the “best degree-1 homogeneous underestimator” of a pure quadratic is the zero function.

Example C: affine  $f(x)=a^\top x + b$ 
---------------------------------------

$$
g(x)=\inf_{\alpha>0}\frac{a^\top(\alpha x)+b}{\alpha} = a^\top x + \inf_{\alpha>0}\frac{b}{\alpha}.
$$
*   If  $b\ge 0$ , the inf is  $0$ , so  $g(x)=a^\top x$ .
*   If  $b<0$ , the inf is  $-\infty$ , so  $g\equiv -\infty$  (this is that “watch your  $f(0)$ ” pathology).

* * *

What 3.31 really _is_, in one crisp sentence
--------------------------------------------

You start from the convex epigraph  $\mathrm{epi}\,f$ , take the **smallest convex cone** containing it (the conic hull), and read off the resulting cone as the epigraph of a **convex, positively homogeneous** function  $g$ . That  $g$  is the biggest homogeneous function that can’t ever exceed  $f$ .

If you want the next brutality layer after this: we can relate  $g$  to **support functions / gauges** and show how it’s computed via a dual representation (it becomes a supremum of linear functionals under a certain constraint set), which makes its convexity “obvious by supremum-of-linear” again.

## Prompt:
Here are the two new exercises (**3.47, 3.48**) plus **Problem 15** again (since it’s explicitly in your screenshot), all proved from first principles, with every “why” made explicit. First go for 3.47. 

---

# A. Problem 15 (again): Hessian of (h(x)=\log f(x))

**Assumptions.** (f:\mathbb R^n\to\mathbb R) is (C^2) and **strictly positive**: (f(x)>0) for all (x). Define
[
h(x)=\ln f(x).
]
We prove
[
\boxed{;\nabla^2 h(x)=\frac{1}{f(x)}\nabla^2 f(x);-;\frac{1}{f(x)^2},\nabla f(x),\nabla f(x)^\top;}
]
with (\nabla f) treated as a **column** vector.

---

## A1) Gradient: (\nabla h = \frac{1}{f}\nabla f)

For each coordinate (i),
[
\frac{\partial h}{\partial x_i}
=\frac{\partial}{\partial x_i}\big(\log(f(x))\big)
=\frac{1}{f(x)}\frac{\partial f}{\partial x_i}(x),
]
by the 1D chain rule ((\log s)'=1/s). Stack these components into a vector:
[
\boxed{;\nabla h(x)=\frac{1}{f(x)},\nabla f(x);}
]

---

## A2) Hessian: product rule carefully in components

Write (h_i = \partial h/\partial x_i). From above,
[
h_i(x)=\frac{1}{f(x)} f_i(x).
]
Differentiate w.r.t. (x_j):
[
h_{ij}(x)=\frac{\partial}{\partial x_j}\left(\frac{1}{f} f_i\right)
=\left(\frac{\partial}{\partial x_j}\frac{1}{f}\right)f_i+\frac{1}{f}f_{ij}.
]
Now
[
\frac{\partial}{\partial x_j}\left(\frac{1}{f}\right)
= -\frac{1}{f^2} f_j
]
(again chain rule on (f^{-1})). Plug in:
[
h_{ij}=\left(-\frac{1}{f^2}f_j\right)f_i +\frac{1}{f}f_{ij}
=\frac{1}{f}f_{ij}-\frac{1}{f^2}f_i f_j.
]
In matrix form, the matrix ([f_{ij}]) is (\nabla^2 f), and the matrix ([f_i f_j]) is (\nabla f,\nabla f^\top). So
[
\boxed{;\nabla^2 h=\frac{1}{f}\nabla^2 f-\frac{1}{f^2}\nabla f,\nabla f^\top;}
]

A useful “directional” rewrite (often the intuition you actually use):
[
v^\top \nabla^2(\log f), v
=\frac{v^\top (\nabla^2 f), v}{f}-\frac{(v^\top \nabla f)^2}{f^2}.
]
That second term is a square, hence (\ge 0), so (\log) “subtracts curvature” in a precise way.

---

# B. Exercise 3.47: First-order inequality ⇔ log-concavity

**Statement (decoded).** Assume:

* (f:\mathbb R^n\to\mathbb R) is differentiable,
* (\mathrm{dom},f) is **convex**,
* (f(x)>0) for all (x\in\mathrm{dom},f).

Show that (f) is **log-concave** (i.e. (\log f) is concave) **iff** for all (x,y\in\mathrm{dom},f),
[
\boxed{;\frac{f(y)}{f(x)}\le \exp!\left(\frac{\nabla f(x)^\top (y-x)}{f(x)}\right);}
]

This is really a “supporting hyperplane” condition for (\log f).

---

## B0) A key lemma: differentiable concave ⇔ global tangent upper bound

Let (h:\mathcal D\to\mathbb R) be differentiable on a convex set (\mathcal D).

> **Lemma.** (h) is concave on (\mathcal D) **iff**
> [
> \boxed{;h(y)\le h(x)+\nabla h(x)^\top (y-x)\quad \forall x,y\in\mathcal D.;}
> ]
> (Concave functions lie **below** their tangent hyperplanes.)

### Proof (⇒): concave ⇒ tangent upper bound

If (h) is concave then (-h) is convex. A standard fact for differentiable convex functions (g) is:
[
g(y)\ge g(x)+\nabla g(x)^\top(y-x).
]
Apply this to (g=-h):
[
-h(y)\ge -h(x)+\nabla(-h)(x)^\top(y-x)
= -h(x)-\nabla h(x)^\top(y-x).
]
Multiply by (-1) (reverses inequality):
[
h(y)\le h(x)+\nabla h(x)^\top(y-x).
]

*(If you want the “pure first principles” proof of the convex inequality too: restrict to the line (x+t(y-x)) and use the 1D fact that a convex function lies above its tangents; same idea as we’ll use below.)*

### Proof (⇐): tangent upper bound ⇒ concave

Assume
[
h(u)\le h(z)+\nabla h(z)^\top(u-z)\quad \forall u,z\in\mathcal D.
]
Take any (x,y\in\mathcal D) and (\theta\in[0,1]). Let (z=\theta x+(1-\theta)y) (in (\mathcal D) by convexity).
Apply the assumed inequality twice, once with (u=x), once with (u=y), both at basepoint (z):
[
h(x)\le h(z)+\nabla h(z)^\top(x-z),\qquad
h(y)\le h(z)+\nabla h(z)^\top(y-z).
]
Multiply the first by (\theta), second by (1-\theta), and add:
[
\theta h(x)+(1-\theta)h(y)
\le h(z)+\nabla h(z)^\top(\theta(x-z)+(1-\theta)(y-z)).
]
But (\theta(x-z)+(1-\theta)(y-z)=\theta x+(1-\theta)y - z = 0). So the gradient term vanishes:
[
\theta h(x)+(1-\theta)h(y)\le h(z).
]
That is exactly concavity:
[
h(\theta x+(1-\theta)y)\ge \theta h(x)+(1-\theta)h(y).
]
Lemma proved.

---

## B1) Apply the lemma to (h=\log f)

Define (h(x)=\log f(x)). This is well-defined because (f(x)>0).

By the lemma,
[
f\ \text{log-concave} \iff h\ \text{concave}
\iff h(y)\le h(x)+\nabla h(x)^\top(y-x).
]

So it remains to express (\nabla h) in terms of (f).

### Compute (\nabla h(x))

From the chain rule (same as in Problem 15 but only first derivative):
[
\nabla h(x)=\nabla(\log f(x))=\frac{1}{f(x)}\nabla f(x).
]

### Substitute into the tangent inequality

Concavity of (h) is equivalent to:
[
\log f(y)\le \log f(x)+\left(\frac{\nabla f(x)}{f(x)}\right)^\top(y-x)
=\log f(x)+\frac{\nabla f(x)^\top(y-x)}{f(x)}.
]
Subtract (\log f(x)) from both sides:
[
\log\frac{f(y)}{f(x)}\le \frac{\nabla f(x)^\top(y-x)}{f(x)}.
]
Exponentiate (exp is increasing, so inequality direction stays the same):
[
\frac{f(y)}{f(x)}\le \exp!\left(\frac{\nabla f(x)^\top(y-x)}{f(x)}\right).
]
That’s exactly the statement.

---

## B2) The “only if” and the “if” directions are now transparent

* If (f) is log-concave, then (h=\log f) concave, so tangent upper bound holds, so the inequality holds.
* If the inequality holds, take logs (legal since (f>0)) to get the tangent upper bound for (h), hence (h) concave, hence (f) log-concave.

Done.

---

# C. Exercise 3.48: If (f) is log-concave and (a\ge 0), then (g=f-a) is log-concave on ({f>a})

**Statement.** Let (f) be log-concave and (a\ge 0). Define
[
g(x)=f(x)-a,
\qquad
\mathrm{dom},g={x\in\mathrm{dom},f:\ f(x)>a}.
]
Show (g) is log-concave on (\mathrm{dom},g).

This looks suspicious at first because “subtracting constants” often breaks nice properties. The trick is: **work in log-space and use a composition rule.**

---

## C1) Step 1: rewrite using (h=\log f)

Since (f) is log-concave and (f>0), define
[
h(x)=\log f(x).
]
Then (h) is **concave** on (\mathrm{dom},f).

Also,
[
g(x)=e^{h(x)}-a.
]

On (\mathrm{dom},g), we have (e^{h(x)}-a>0), so (\log g(x)) is defined.

---

## C2) Step 2: express (\log g) as a scalar composition (\phi\circ h)

Define a one-variable function
[
\phi(t)=\log(e^t-a),
\qquad\text{with domain } {t:\ e^t>a}.
]
Then for (x\in\mathrm{dom},g),
[
\log g(x)=\log(e^{h(x)}-a)=\phi(h(x)).
]

So the problem reduces to:

* (h(x)) is concave in (x),
* (\phi(t)) is concave and nondecreasing in (t),

⇒ (\phi\circ h) is concave (standard concave composition rule).

Let’s verify concavity + monotonicity of (\phi).

---

## C3) Step 3: show (\phi) is increasing and concave for (a\ge 0)

Compute derivatives on its domain (e^t>a):

### Monotonicity

[
\phi'(t)=\frac{d}{dt}\log(e^t-a)
= \frac{e^t}{e^t-a}.
]
If (a\ge 0) and (e^t>a), then (e^t-a>0), so (\phi'(t)>0).
Thus **(\phi) is strictly increasing**.

### Concavity

Differentiate again:
[
\phi''(t)
= \frac{d}{dt}\left(\frac{e^t}{e^t-a}\right)
= \frac{e^t(e^t-a)-e^t(e^t)}{(e^t-a)^2}
= \frac{-a e^t}{(e^t-a)^2}.
]
If (a\ge 0) and (e^t>a), then denominator (>0) and numerator (\le 0), hence
[
\phi''(t)\le 0.
]
So **(\phi) is concave** (strictly concave if (a>0)).

---

## C4) Step 4: composition rule ⇒ (\log g) concave

We have:

* (h(x)) is concave,
* (\phi) is concave and nondecreasing,

Therefore
[
\log g(x)=\phi(h(x))
]
is concave on its domain.

That means (g) is **log-concave** on (\mathrm{dom},g).

---

## C5) Step 5: domain convexity (don’t skip!)

A log-concave function must be defined on a convex domain (in the usual BV setup). Check:
[
\mathrm{dom},g = {x:\ f(x)>a} = {x:\ \log f(x)>\log a}
\quad (a>0).
]
Since (h=\log f) is concave, its strict superlevel set ({h>\text{const}}) is convex. (Same proof as for quasiconcavity: concave ⇒ upper level sets convex.)

Edge case (a=0): (\mathrm{dom},g=\mathrm{dom},f), and (g=f), trivial.

So everything is consistent.

---

# What to keep in your mental toolkit

* **Exercise 3.47**: “log-concave” ⇔ **tangent upper bound** for (\log f), rewritten back in terms of (f).
* **Exercise 3.48**: subtracting (a\ge 0) works because
  [
  \log(f-a)=\underbrace{\log(e^{\log f}-a)}_{\phi(\log f)}
  ]
  and (\phi(t)=\log(e^t-a)) is **concave increasing**, so concavity survives composition.

If you want to crank it even harder, we can connect 3.47 to a second-order condition using Problem 15: for (C^2) functions,
[
f \text{ log-concave}\iff \nabla^2(\log f)\preceq 0
\iff \frac{1}{f}\nabla^2 f-\frac{1}{f^2}\nabla f\nabla f^\top\preceq 0,
]
and derive 3.47 as an “integrated” first-order consequence of that curvature inequality.

## Response:
Thought for 16s

Exercise 3.47 — First-order inequality ⇔ log-concavity (full “from bedrock” proof)
----------------------------------------------------------------------------------

### What you’re proving (clean statement)

Let  $f:\mathrm{dom}\,f\subseteq \mathbb R^n\to (0,\infty)$  be **differentiable**, and assume  $\mathrm{dom}\,f$  is **convex**.

Define  $h(x):=\log f(x)$  (well-defined because  $f>0$ ).

You must prove the equivalence:

$$
\boxed{ f \text{ is log-concave on }\mathrm{dom}\,f \ \Longleftrightarrow\ \frac{f(y)}{f(x)} \le \exp\!\left(\frac{\nabla f(x)^\top (y-x)}{f(x)}\right) \ \ \forall x,y\in\mathrm{dom}\,f. }
$$

Where **log-concave** means:  $h=\log f$  is **concave** on  $\mathrm{dom} f$ .

* * *

0) The core geometric fact we need (proved from scratch)
========================================================

Everything hinges on a “tangent hyperplane” characterization of concavity.

Lemma (supporting hyperplane inequality for concave functions)
--------------------------------------------------------------

Let  $h:\mathcal D\to\mathbb R$  be differentiable on a **convex** set  $\mathcal D\subseteq\mathbb R^n$ . Then:

$$
\boxed{ h \text{ is concave on }\mathcal D \ \Longleftrightarrow\ h(y)\le h(x)+\nabla h(x)^\top (y-x)\quad \forall x,y\in\mathcal D. }
$$

Interpretation: a differentiable concave function lies **below** every tangent hyperplane.

I’ll prove both directions _without appealing to any “standard theorem”_.

* * *

Proof of Lemma, direction (⇒): concave ⇒ tangent upper bound
------------------------------------------------------------

### Step 1: reduce the  $n$ \-D statement to a 1-D statement along a line

Fix  $x,y\in\mathcal D$ . Because  $\mathcal D$  is convex, the entire segment

$$
x+t(y-x)\in\mathcal D\qquad\forall t\in[0,1].
$$

Define a 1-D function by restricting  $h$  to this segment:

$$
\varphi(t):=h\big(x+t(y-x)\big),\qquad t\in[0,1].
$$

### Step 2: concavity of  $h$  implies concavity of  $\varphi$ 

Take any  $t_1,t_2\in[0,1]$  and  $\theta\in[0,1]$ . Then

$$
x+(\theta t_1+(1-\theta)t_2)(y-x) = \theta\big(x+t_1(y-x)\big)+(1-\theta)\big(x+t_2(y-x)\big).
$$

Concavity of  $h$  gives

$$
\varphi(\theta t_1+(1-\theta)t_2) = h(\theta(\cdots)+(1-\theta)(\cdots)) \ge \theta h(x+t_1(y-x))+(1-\theta)h(x+t_2(y-x)) = \theta\varphi(t_1)+(1-\theta)\varphi(t_2).
$$

So  $\varphi$  is concave on  $[0,1]$ .

### Step 3: a purely 1-D fact: concave differentiable ⇒ derivative is nonincreasing

Because  $\varphi$  is concave and differentiable, its derivative  $\varphi'(t)$  is **nonincreasing** on  $[0,1]$ . Here’s a short proof:

Take  $0\le s<t\le 1$ . For concave  $\varphi$ , the **secant slopes decrease** as you move right:

$$
\frac{\varphi(t)-\varphi(s)}{t-s}\ \le\ \frac{\varphi(s)-\varphi(r)}{s-r}\quad \text{for } r<s<t.
$$

Letting  $r\uparrow s$  and using differentiability turns the RHS into  $\varphi'(s)$ , giving

$$
\frac{\varphi(t)-\varphi(s)}{t-s}\le \varphi'(s).
$$

Now let  $t\downarrow s$  to conclude  $\varphi'(t)\le \varphi'(s)$  for  $t>s$ . So  $\varphi'$  is nonincreasing.

(That’s the bedrock reason “concave curves bend downward”: slopes drop.)

### Step 4: integrate the derivative bound (Fundamental Theorem of Calculus)

By the FTC,

$$
\varphi(1)-\varphi(0)=\int_0^1 \varphi'(t)\,dt.
$$

Since  $\varphi'(t)\le \varphi'(0)$  for all  $t\in[0,1]$  (nonincreasing),

$$
\int_0^1 \varphi'(t)\,dt\le \int_0^1 \varphi'(0)\,dt=\varphi'(0).
$$

So

$$
\varphi(1)\le \varphi(0)+\varphi'(0).
$$

### Step 5: translate back to  $h$ 

Compute these terms:

*    $\varphi(0)=h(x)$ .
*    $\varphi(1)=h(y)$ .
*    $\varphi'(0)$  via the multivariate chain rule:
    $$
    \varphi'(t)=\nabla h\big(x+t(y-x)\big)^\top (y-x) \quad\Rightarrow\quad \varphi'(0)=\nabla h(x)^\top (y-x).
    $$

So the inequality  $\varphi(1)\le \varphi(0)+\varphi'(0)$  becomes

$$
h(y)\le h(x)+\nabla h(x)^\top (y-x).
$$

That’s exactly the tangent upper bound. □

* * *

Proof of Lemma, direction (⇐): tangent upper bound ⇒ concavity
--------------------------------------------------------------

Assume:

$$
h(u)\le h(z)+\nabla h(z)^\top(u-z)\qquad \forall u,z\in\mathcal D.
$$

We must prove concavity:

$$
h(\theta x+(1-\theta)y)\ge \theta h(x)+(1-\theta)h(y).
$$

### Step 1: define the midpoint point  $z$ 

Let

$$
z:=\theta x+(1-\theta)y\in\mathcal D
$$

(using convexity of  $\mathcal D$ ).

### Step 2: apply the tangent inequality twice, both times “based at  $z$ ”

Use the assumed inequality with  $(u=x,z=z)$ :

$$
h(x)\le h(z)+\nabla h(z)^\top(x-z).
$$

Similarly with  $(u=y,z=z)$ :

$$
h(y)\le h(z)+\nabla h(z)^\top(y-z).
$$

### Step 3: take the same convex combination as in concavity

Multiply the first inequality by  $\theta$  and the second by  $(1-\theta)$ , then add:

$$
\theta h(x)+(1-\theta)h(y) \le \theta h(z)+(1-\theta)h(z) + \nabla h(z)^\top\big(\theta(x-z)+(1-\theta)(y-z)\big).
$$

The first part simplifies to  $h(z)$ . Now simplify the vector in the gradient term:

$$
\theta(x-z)+(1-\theta)(y-z) = \theta x+(1-\theta)y - (\theta z+(1-\theta)z) = (\theta x+(1-\theta)y) - z = z-z=0.
$$

So the gradient term vanishes:

$$
\theta h(x)+(1-\theta)h(y)\le h(z).
$$

That is concavity:

$$
h(z)\ge \theta h(x)+(1-\theta)h(y).
$$

So  $h$  is concave. □

Lemma proved.

* * *

1) Apply the lemma to  $h=\log f$ 
==================================

Define

$$
h(x):=\log f(x).
$$

This is well-defined on  $\mathrm{dom}\,f$  because  $f(x)>0$ .

By definition:

$$
f \text{ log-concave } \iff h=\log f \text{ concave}.
$$

So by the Lemma,

$$
h \text{ concave } \iff h(y)\le h(x)+\nabla h(x)^\top (y-x)\quad \forall x,y.
$$

Now we just need to compute  $\nabla h(x)$  explicitly.

* * *

2) Compute  $\nabla(\log f)$  in the most explicit way possible
===============================================================

Because  $f$  is differentiable and positive,  $\log f$  is differentiable and we can apply the chain rule.

### Step-by-step component computation

For each coordinate  $i$ ,

$$
\frac{\partial}{\partial x_i}\log f(x) = (\log)'(f(x))\cdot \frac{\partial f(x)}{\partial x_i} = \frac{1}{f(x)}\, f_i(x).
$$

Stacking those components gives the gradient vector:

$$
\boxed{ \nabla h(x)=\nabla(\log f(x))=\frac{1}{f(x)}\,\nabla f(x). }
$$

* * *

3) Substitute into the tangent inequality and rewrite it into the exercise’s form
=================================================================================

Start from the tangent inequality for concavity of  $h$ :

$$
\log f(y)\le \log f(x)+\nabla(\log f(x))^\top (y-x).
$$

Substitute  $\nabla(\log f(x))=\nabla f(x)/f(x)$ :

$$
\log f(y)\le \log f(x)+\left(\frac{\nabla f(x)}{f(x)}\right)^\top (y-x) = \log f(x)+\frac{\nabla f(x)^\top (y-x)}{f(x)}.
$$

### Step 1: isolate a log ratio

Subtract  $\log f(x)$  from both sides:

$$
\log f(y)-\log f(x)\le \frac{\nabla f(x)^\top (y-x)}{f(x)}.
$$

Use  $\log a-\log b=\log(a/b)$  (valid since both positive):

$$
\log\frac{f(y)}{f(x)}\le \frac{\nabla f(x)^\top (y-x)}{f(x)}.
$$

### Step 2: exponentiate (and explain why the inequality direction stays)

The exponential function  $\exp(\cdot)$  is strictly increasing, meaning:

$$
A\le B\ \Rightarrow\ e^{A}\le e^{B}.
$$

So exponentiating preserves the inequality:

$$
\frac{f(y)}{f(x)} \le \exp\!\left(\frac{\nabla f(x)^\top (y-x)}{f(x)}\right).
$$

This is exactly the desired inequality.

So we have shown:

$$
\boxed{\log f \text{ concave } \Rightarrow \text{ the inequality.}}
$$

* * *

4) Reverse direction (the “if” part) just unwinds the steps
===========================================================

Assume the inequality holds for all  $x,y$ :

$$
\frac{f(y)}{f(x)} \le \exp\!\left(\frac{\nabla f(x)^\top (y-x)}{f(x)}\right).
$$

Because  $f(x),f(y)>0$ , we can safely take logs of both sides.

*    $\log$  is increasing, so inequality direction stays the same.
*    $\log(f(y)/f(x))=\log f(y)-\log f(x)$ .

So:

$$
\log\frac{f(y)}{f(x)} \le \frac{\nabla f(x)^\top (y-x)}{f(x)}.
$$

Rewrite:

$$
\log f(y)\le \log f(x)+\left(\frac{\nabla f(x)}{f(x)}\right)^\top (y-x).
$$

But  $\nabla(\log f(x))=\nabla f(x)/f(x)$ , so

$$
\log f(y)\le \log f(x)+\nabla(\log f(x))^\top (y-x).
$$

That is precisely the tangent upper bound property for  $h=\log f$ . By the Lemma,  $h$  is concave. Therefore  $f$  is log-concave.

So:

$$
\boxed{\text{the inequality} \Rightarrow \log f \text{ concave}.}
$$

That completes the equivalence. □

* * *

5) What this inequality _means_ (so it sticks)
==============================================

Take logs and rearrange:

$$
\log f(y)\ \le\ \log f(x)+\nabla(\log f)(x)^\top (y-x).
$$

This says:

> The graph of  $\log f$  always lies **below** its tangent plane at  $x$ .

So 3.47 is not a random exponential inequality—it’s just the geometric meaning of concavity, translated back from  $\log f$  to  $f$ .

* * *

6) Alternative proof route (nice if you assume  $C^2$ ): via Hessian (connects to Problem 15)
=============================================================================================

If you additionally assume  $f\in C^2$ , then:

*    $f$  is log-concave  
       $\iff$   $\log f$  is concave  
       $\iff$   $\nabla^2(\log f)(x)\preceq 0$  for all  $x$ .

Using Problem 15:

$$
\nabla^2(\log f) = \frac{1}{f}\nabla^2 f-\frac{1}{f^2}\nabla f\,\nabla f^\top.
$$

So log-concavity is equivalent to the matrix inequality

$$
\frac{1}{f}\nabla^2 f-\frac{1}{f^2}\nabla f\,\nabla f^\top \preceq 0.
$$

Then you can derive the first-order inequality of 3.47 by integrating along line segments using the fact that for a  $C^2$  concave function, the tangent upper bound follows from “second derivative ≤ 0” along every line. This is essentially the same 1-D argument we used in the Lemma proof, but it starts from curvature instead of Jensen.

* * *

If you want, paste the exact BV wording for 3.47 (sometimes they phrase it as “show that log-concavity is equivalent to …”), and I’ll match the proof to their exact quantifiers and any domain conventions (open vs closed domain, strict positivity, etc.).

## Prompt:
Further breakdown and explain completer.

## Response:
Thought for 9s

Got it. Let’s take **Exercise 3.47** and grind it down to the atoms: every definition, every inequality direction, every “why is this allowed,” and also two alternative proof viewpoints.

* * *

Exercise 3.47 — What exactly is being claimed?
----------------------------------------------

### Data (assumptions)

*    $f:\mathrm{dom}\,f\subseteq\mathbb R^n\to (0,\infty)$  is **differentiable**.
*    $\mathrm{dom}\,f$  is **convex** (important: every line segment between two points in the domain stays in the domain).
*    $f(x)>0$  everywhere on  $\mathrm{dom}\,f$  (important:  $\log f(x)$  exists).

### Definitions

*    $f$  is **log-concave** iff  $\log f$  is **concave**.
*   Concave means:
    $$
    \log f(\theta x+(1-\theta)y)\ \ge\ \theta\log f(x)+(1-\theta)\log f(y) \quad \forall x,y,\ \forall \theta\in[0,1].
    $$

### Claim to prove (equivalence)

$$
\boxed{ f \text{ is log-concave} \iff \frac{f(y)}{f(x)}\le \exp\!\left(\frac{\nabla f(x)^\top (y-x)}{f(x)}\right) \quad \forall x,y\in\mathrm{dom}\,f. }
$$

* * *

Big picture: this is just “ $\log f$  lies below its tangent plane”
-------------------------------------------------------------------

The inequality looks exotic because of exponentials, but if you take logs it becomes:

$$
\log f(y) - \log f(x) \le \frac{\nabla f(x)^\top (y-x)}{f(x)} = \nabla(\log f)(x)^\top (y-x).
$$

That is exactly:

$$
\boxed{ h(y)\le h(x)+\nabla h(x)^\top (y-x) \quad\text{with }h=\log f. }
$$

So Exercise 3.47 is basically:

> **Concavity of  $h$ ** ⇔ **global “tangent upper bound” inequality**.

We now prove that equivalence from first principles.

* * *

1) Bedrock lemma: concavity ⇔ tangent upper bound
=================================================

Let  $h:\mathcal D\to\mathbb R$  be differentiable on a **convex** set  $\mathcal D$ .

### Lemma

$$
\boxed{ h\ \text{concave} \iff h(y)\le h(x)+\nabla h(x)^\top (y-x)\quad\forall x,y\in\mathcal D. }
$$

I’ll prove both directions, with all micro-steps.

* * *

1.1 Direction (⇒): concave ⇒ lies below tangent plane
-----------------------------------------------------

Fix any  $x,y\in\mathcal D$ .

### Step 1: restrict to the line segment (reduce  $n$ D to 1D)

Because  $\mathcal D$  is convex, the segment

$$
x+t(y-x)\in\mathcal D\quad\forall t\in[0,1].
$$

Define a 1D function

$$
\varphi(t):=h(x+t(y-x)),\qquad t\in[0,1].
$$

### Step 2: show  $\varphi$  is concave on  $[0,1]$ 

Take any  $t_1,t_2\in[0,1]$ ,  $\theta\in[0,1]$ .  
Compute:

$$
x+(\theta t_1+(1-\theta)t_2)(y-x) = \theta(x+t_1(y-x))+(1-\theta)(x+t_2(y-x)).
$$

Now apply concavity of  $h$ :

$$
\varphi(\theta t_1+(1-\theta)t_2) = h(\theta(\cdot)+(1-\theta)(\cdot)) \ge \theta h(x+t_1(y-x))+(1-\theta)h(x+t_2(y-x)) = \theta\varphi(t_1)+(1-\theta)\varphi(t_2).
$$

So  $\varphi$  is concave.

### Step 3: the key 1D fact (proved): concave differentiable ⇒ tangent upper bound at 0

We want to prove:

$$
\varphi(1)\le \varphi(0)+\varphi'(0).
$$

Here’s the cleanest “no black boxes” proof.

#### Step 3a: concavity gives a secant-slope inequality

Concavity of  $\varphi$  implies: for any  $t\in(0,1]$ ,

$$
\varphi(t)\ \ge\ \varphi(0)+t\cdot\frac{\varphi(1)-\varphi(0)}{1-0}.
$$

Why? Because concavity says

$$
\varphi(t)\ge (1-t)\varphi(0)+t\varphi(1),
$$

and that rearranges to the above.

Now subtract  $\varphi(0)$  and divide by  $t>0$ :

$$
\frac{\varphi(t)-\varphi(0)}{t}\ \ge\ \varphi(1)-\varphi(0).
$$

#### Step 3b: take the limit  $t\downarrow 0$ 

Because  $\varphi$  is differentiable at 0,

$$
\lim_{t\downarrow 0}\frac{\varphi(t)-\varphi(0)}{t} = \varphi'(0).
$$

So taking limits in the inequality gives:

$$
\varphi'(0)\ \ge\ \varphi(1)-\varphi(0).
$$

Rearrange:

$$
\varphi(1)\le \varphi(0)+\varphi'(0).
$$

That’s exactly the tangent upper bound in 1D, at the left endpoint.

### Step 4: translate  $\varphi'(0)$  back into  $\nabla h(x)$ 

We already have:

$$
\varphi(1)\le \varphi(0)+\varphi'(0).
$$

Compute each term:

*    $\varphi(0)=h(x)$ .
*    $\varphi(1)=h(y)$ .
*    $\varphi'(0)$ : by chain rule for curves,
    $$
    \varphi'(t)=\nabla h(x+t(y-x))^\top (y-x),
    $$
    so
    $$
    \varphi'(0)=\nabla h(x)^\top (y-x).
    $$

Substitute:

$$
h(y)\le h(x)+\nabla h(x)^\top (y-x).
$$

Done.

**This direction used only:**

*   convexity of the domain (so the line segment stays inside),
*   definition of concavity,
*   derivative definition as a limit.

* * *

1.2 Direction (⇐): tangent upper bound ⇒ concave
------------------------------------------------

Assume:

$$
h(u)\le h(z)+\nabla h(z)^\top(u-z)\quad\forall u,z\in\mathcal D.
$$

We must prove:

$$
h(\theta x+(1-\theta)y)\ge \theta h(x)+(1-\theta)h(y).
$$

### Step 1: define the “mix point”

Let

$$
z:=\theta x+(1-\theta)y.
$$

Because  $\mathcal D$  is convex,  $z\in\mathcal D$ .

### Step 2: apply the tangent inequality twice (same basepoint  $z$ )

With  $u=x$ , basepoint  $z$ :

$$
h(x)\le h(z)+\nabla h(z)^\top(x-z).
$$

With  $u=y$ , basepoint  $z$ :

$$
h(y)\le h(z)+\nabla h(z)^\top(y-z).
$$

### Step 3: take the same convex combination  $\theta,(1-\theta)$ 

Multiply the first by  $\theta$ , second by  $1-\theta$ , add:

$$
\theta h(x)+(1-\theta)h(y) \le \theta h(z)+(1-\theta)h(z) +\nabla h(z)^\top\big(\theta(x-z)+(1-\theta)(y-z)\big).
$$

The first part is just  $h(z)$ . Now simplify the bracket:

$$
\theta(x-z)+(1-\theta)(y-z) = \theta x+(1-\theta)y - (\theta z+(1-\theta)z) = (\theta x+(1-\theta)y)-z = z-z=0.
$$

So the gradient term is  $\nabla h(z)^\top 0=0$ . Hence:

$$
\theta h(x)+(1-\theta)h(y)\le h(z),
$$

i.e.

$$
h(\theta x+(1-\theta)y)\ge \theta h(x)+(1-\theta)h(y).
$$

So  $h$  is concave. Lemma proved.

* * *

2) Apply lemma to  $h=\log f$ 
==============================

Define

$$
h(x):=\log f(x).
$$

This is valid because  $f(x)>0$ .

Then:

$$
f\text{ log-concave} \iff h\text{ concave}.
$$

By the lemma:

$$
h\text{ concave} \iff h(y)\le h(x)+\nabla h(x)^\top (y-x).
$$

So the whole exercise becomes: compute  $\nabla(\log f)$  and rewrite.

* * *

3) Compute  $\nabla(\log f)$  _painfully explicitly_
====================================================

### What is the gradient?

 $\nabla h(x)$  is the column vector whose  $i$ \-th component is  $\partial h/\partial x_i$ .

### Compute componentwise using the 1D chain rule

For each  $i$ ,

$$
\frac{\partial}{\partial x_i}\log f(x) = (\log)'(f(x))\cdot \frac{\partial f(x)}{\partial x_i} = \frac{1}{f(x)}\, f_i(x).
$$

Stack these into a vector:

$$
\boxed{\nabla(\log f)(x)=\frac{1}{f(x)}\nabla f(x).}
$$

No magic: it’s just the scalar derivative  $(\log s)'=1/s$  plus multivariate chain rule componentwise.

* * *

4) Turn tangent inequality into the exponential inequality
==========================================================

Start from the tangent inequality for concavity of  $h$ :

$$
\log f(y)\le \log f(x)+\nabla(\log f)(x)^\top (y-x).
$$

Substitute  $\nabla(\log f)(x)=\nabla f(x)/f(x)$ :

$$
\log f(y)\le \log f(x)+\left(\frac{\nabla f(x)}{f(x)}\right)^\top (y-x) = \log f(x)+\frac{\nabla f(x)^\top(y-x)}{f(x)}.
$$

### Step 1: isolate a log ratio

Subtract  $\log f(x)$ :

$$
\log f(y)-\log f(x)\le \frac{\nabla f(x)^\top(y-x)}{f(x)}.
$$

Use  $\log a-\log b=\log(a/b)$ , allowed since  $f(x),f(y)>0$ :

$$
\log\frac{f(y)}{f(x)}\le \frac{\nabla f(x)^\top(y-x)}{f(x)}.
$$

### Step 2: exponentiate, and explain why order is preserved

The exponential function  $e^t$  is strictly increasing: if  $A\le B$  then  $e^A\le e^B$ .  
Therefore:

$$
\frac{f(y)}{f(x)} \le \exp\!\left(\frac{\nabla f(x)^\top(y-x)}{f(x)}\right).
$$

That’s exactly the statement.

* * *

5) Reverse direction is literally “undo the algebra”
====================================================

Assume the exercise inequality holds. Take logs (legal because both sides  $>0$ ):

*   LHS:  $\log(f(y)/f(x))$ .
*   RHS:  $\log(\exp(\cdot))=(\cdot)$ .

Because  $\log$  is increasing, inequality direction stays the same. You recover:

$$
\log f(y)\le \log f(x)+\nabla(\log f)(x)^\top (y-x).
$$

By the lemma,  $\log f$  is concave, i.e.  $f$  is log-concave.

So the “if and only if” is complete.

* * *

6) What the inequality is _really_ saying (intuition that is still exact)
=========================================================================

Rewrite the result as

$$
\log f(y)\le \log f(x)+\nabla(\log f)(x)^\top (y-x).
$$

That is the exact multivariate analogue of the 1D fact:

> a concave function has its graph below its tangent line.

Exponentiating just converts an **additive** upper bound in log-space into a **multiplicative** upper bound in original space:

$$
f(y)\le f(x)\cdot \exp(\nabla(\log f)(x)^\top(y-x)).
$$

So: log-concavity says “multiplicative growth is controlled linearly in the exponent.”

* * *

7) Equality cases (when is the bound tight?)
============================================

In the lemma, equality

$$
h(y)=h(x)+\nabla h(x)^\top(y-x)
$$

happens when  $h$  is **affine along the segment** between  $x$  and  $y$  (i.e.  $\varphi(t)=h(x+t(y-x))$  is linear in  $t$ ).

So in Exercise 3.47, equality holds when  $\log f$  is affine along that segment. Example: if

$$
f(x)=\exp(a^\top x+b),
$$

then  $\log f(x)=a^\top x+b$  is affine everywhere, and the inequality holds with equality for all  $x,y$ .

* * *

8) Alternative proof viewpoint (C² case): “curvature ≤ 0” ⇒ tangent inequality
==============================================================================

If you assume  $f\in C^2$ , then  $h=\log f\in C^2$ , and:

*    $h$  concave    $\iff \nabla^2 h(x)\preceq 0$  for all  $x$ .
*   Negative semidefinite Hessian along a line means the 1D second derivative is  $\le 0$ , hence the 1D tangent upper bound holds, hence the global inequality holds.

Then using Problem 15:

$$
\nabla^2(\log f)=\frac{1}{f}\nabla^2 f-\frac{1}{f^2}\nabla f\nabla f^\top,
$$

you get a pure second-order criterion for log-concavity. Exercise 3.47 is the integrated first-order version.

* * *

If you want the _next_ layer beyond this: I can rewrite 3.47 as a statement about **support functions** and **Bregman divergences** (it’s essentially saying the “Bregman divergence” of  $-\log f$  is nonnegative), which gives another geometric lens that’s very BV-ish.

## Prompt:
3.48

## Response:
Exercise 3.48 — If  $f$  is log-concave and  $a\ge 0$ , then  $g=f-a$  is log-concave on  $\{f>a\}$ 
----------------------------------------------------------------------------------------------------

We’ll go _from bedrock_, and we will be annoyingly explicit about:

*   what “log-concave” means,
*   what the domain is,
*   why we’re allowed to take logs,
*   why a certain 1D function is concave and increasing,
*   and exactly how the composition rule is proved (not quoted).

* * *

0) Statement (clean and precise)
================================

### Assumptions

*    $f:\mathrm{dom} f\subseteq\mathbb R^n \to (0,\infty)$  is **log-concave** on  $\mathrm{dom} f$ .  
    Meaning:  $h(x):=\log f(x)$  is **concave** on  $\mathrm{dom} f$ .
*    $a\ge 0$  is a constant.

### Define

$$
g(x):=f(x)-a.
$$

But  $g$  is not positive everywhere, so we define its natural domain:

$$
\mathrm{dom} g := \{x\in \mathrm{dom} f : f(x)>a\}.
$$

On this set,  $g(x)=f(x)-a>0$ , so  $\log g(x)$  is defined.

### Goal

Show:  $g$  is log-concave on  $\mathrm{dom} g$ , i.e.

$$
\boxed{\log g \text{ is concave on }\mathrm{dom} g.}
$$

Equivalently:

$$
\boxed{ g(\theta x+(1-\theta)y)\ \ge\ g(x)^\theta g(y)^{1-\theta} \quad\forall x,y\in\mathrm{dom} g,\ \theta\in[0,1]. }
$$

* * *

1) First sanity check: is  $\mathrm{dom} g$  convex?
====================================================

This matters because “concave on its domain” in BV is usually meant on a convex domain.

Take any  $x,y\in \mathrm{dom} g$ . So  $f(x)>a$  and  $f(y)>a$ .

Since  $f$  is log-concave, we have for any  $\theta\in[0,1]$ :

$$
f(\theta x+(1-\theta)y)\ \ge\ f(x)^\theta f(y)^{1-\theta}.
$$

Now if  $f(x)>a$  and  $f(y)>a$ , then  $f(x)^\theta f(y)^{1-\theta} > a^\theta a^{1-\theta}=a$  (because  $a\ge0$  and both factors exceed  $a$ ; if  $a=0$  it’s trivial). Hence:

$$
f(\theta x+(1-\theta)y) > a,
$$

so  $\theta x+(1-\theta)y \in \mathrm{dom} g$ .

So:

$$
\boxed{\mathrm{dom} g \text{ is convex.}}
$$

Good: we’re allowed to talk about concavity/log-concavity on  $\mathrm{dom}g$  without domain weirdness.

* * *

2) Strategy: rewrite  $\log g$  as a scalar composition
=======================================================

Define

$$
h(x):=\log f(x).
$$

Because  $f>0$ ,  $h$  is well-defined. Because  $f$  is log-concave,  $h$  is **concave**.

Also  $f(x)=e^{h(x)}$ . Therefore

$$
g(x)=f(x)-a=e^{h(x)}-a.
$$

On  $\mathrm{dom}g$ , we have  $e^{h(x)}-a>0$ , so we can take logs:

$$
\log g(x) = \log(e^{h(x)}-a).
$$

Now define a _one-variable_ function

$$
\phi(t) := \log(e^t-a),
$$

with domain

$$
\mathrm{dom}\,\phi := \{t\in\mathbb R: e^t>a\}.
$$

Then for every  $x\in\mathrm{dom}g$ , we have  $h(x)\in\mathrm{dom}\phi$  and

$$
\boxed{\log g(x) = \phi(h(x)).}
$$

So the entire problem becomes:

>  $h$  is concave, and  $\phi$  is concave and nondecreasing  
>  $\Longrightarrow$   $\phi\circ h$  is concave.

We will prove this composition fact from scratch after we verify  $\phi$ ’s properties.

* * *

3) Verify  $\phi(t)=\log(e^t-a)$  is increasing and concave (when  $a\ge 0$ )
=============================================================================

3.1 Domain check
----------------

We need  $e^t-a>0$  to define  $\log(e^t-a)$ .  
That is exactly  $e^t>a$ , i.e.  $t>\log a$  if  $a>0$ .  
If  $a=0$ , then  $e^t-a=e^t>0$  for all  $t$ , so  $\mathrm{dom}\phi=\mathbb R$ .

So the domain is consistent.

* * *

3.2 Monotonicity: show  $\phi'(t)\ge 0$ 
----------------------------------------

Compute derivative carefully:

*   Outer:  $\frac{d}{du}\log u = 1/u$ .
*   Inner:  $u(t)=e^t-a$  has derivative  $u'(t)=e^t$ .

Chain rule:

$$
\phi'(t)=\frac{1}{e^t-a}\cdot e^t = \frac{e^t}{e^t-a}.
$$

Now on the domain  $e^t-a>0$ , the denominator is positive; the numerator  $e^t$  is always positive. Therefore

$$
\phi'(t)>0.
$$

So:

$$
\boxed{\phi \text{ is strictly increasing on its domain.}}
$$

This “increasing” property is crucial: it lets us push inequalities through  $\phi$  without flipping them.

* * *

3.3 Concavity: show  $\phi''(t)\le 0$ 
--------------------------------------

Differentiate  $\phi'(t)=\dfrac{e^t}{e^t-a}$ .

Let  $N(t)=e^t$ ,  $D(t)=e^t-a$ . Then  $\phi'(t)=N/D$ .

Quotient rule:

$$
\phi''(t) = \frac{N' D - N D'}{D^2}.
$$

Here  $N'(t)=e^t$  and  $D'(t)=e^t$ . So:

$$
\phi''(t) = \frac{e^t(e^t-a) - e^t(e^t)}{(e^t-a)^2} = \frac{e^t(e^t-a-e^t)}{(e^t-a)^2} = \frac{-a e^t}{(e^t-a)^2}.
$$

Now inspect sign:

*    $e^t>0$ .
*    $(e^t-a)^2>0$ .
*   If  $a\ge 0$ , then  $-a e^t \le 0$ .

Hence:

$$
\phi''(t)\le 0.
$$

So:

$$
\boxed{\phi \text{ is concave on its domain (for }a\ge 0).}
$$

Also note the “knife edge”:

*   If  $a>0$ :  $\phi''(t)<0$  (strictly concave).
*   If  $a=0$ :  $\phi(t)=\log(e^t)=t$  is affine (both concave and convex).

* * *

4) Composition theorem (proved, not quoted)
===========================================

Theorem (1D outer,  $n$ D inner)
--------------------------------

Let  $\mathcal D\subseteq\mathbb R^n$  be convex.  
Let  $h:\mathcal D\to\mathbb R$  be concave.  
Let  $\phi:I\to\mathbb R$  be concave and nondecreasing on an interval  $I$  containing  $h(\mathcal D)$ .  
Define  $H(x)=\phi(h(x))$ . Then  $H$  is concave on  $\mathcal D$ .

### Proof (line-by-line)

Take any  $x,y\in\mathcal D$  and  $\theta\in[0,1]$ . Let

$$
z:=\theta x+(1-\theta)y\in\mathcal D.
$$

**Step 1: apply concavity of  $h$ **  
Concavity means:

$$
h(z)\ \ge\ \theta h(x)+(1-\theta)h(y).
$$

**Step 2: push through  $\phi$  using monotonicity**  
Since  $\phi$  is nondecreasing, larger input gives larger output. Therefore:

$$
\phi(h(z))\ \ge\ \phi(\theta h(x)+(1-\theta)h(y)).
$$

**Step 3: apply concavity of  $\phi$ **  
Concavity of  $\phi$  means:

$$
\phi(\theta u+(1-\theta)v)\ \ge\ \theta\phi(u)+(1-\theta)\phi(v)
$$

for any  $u,v$  in its domain. Apply with  $u=h(x)$ ,  $v=h(y)$ :

$$
\phi(\theta h(x)+(1-\theta)h(y)) \ \ge\ \theta\phi(h(x))+(1-\theta)\phi(h(y)).
$$

**Step 4: chain the inequalities**  
Combine Step 2 and Step 3:

$$
\phi(h(z)) \ge \theta\phi(h(x))+(1-\theta)\phi(h(y)).
$$

That is exactly:

$$
H(z)\ge \theta H(x)+(1-\theta)H(y).
$$

So  $H$  is concave. □

* * *

5) Apply it to the problem
==========================

We already set:

*    $h(x)=\log f(x)$ , which is concave (because  $f$  log-concave).
*    $\phi(t)=\log(e^t-a)$ , which is concave and increasing on its domain (because  $a\ge 0$ ).

And we have:

$$
\log g(x)=\log(f(x)-a)=\log(e^{h(x)}-a)=\phi(h(x)).
$$

Therefore by the theorem:

$$
\boxed{\log g \text{ is concave on }\mathrm{dom}g.}
$$

So:

$$
\boxed{g \text{ is log-concave on }\mathrm{dom}g.}
$$

That completes the proof. □

* * *

6) Why the condition  $a\ge 0$  is not decoration (failure mode)
================================================================

Look at  $\phi''(t)=\dfrac{-a e^t}{(e^t-a)^2}$ .

*   If  $a\ge 0$ :  $\phi''(t)\le 0$  ⇒  $\phi$  concave ⇒ composition works.
*   If  $a<0$ : then  $-a e^t>0$  ⇒  $\phi''(t)>0$  ⇒  $\phi$  is **convex**, not concave, so the composition rule breaks and the statement generally fails.

So  $a\ge 0$  is exactly what makes the outer function concave.

* * *

7) Alternative proof (same bones, slightly different outfit): use first-order characterization (Exercise 3.47)
==============================================================================================================

If you also want a “match the previous exercise” route:

*   3.47 says log-concavity of a differentiable positive function is equivalent to a certain first-order inequality.
*   You can attempt to show  $g=f-a$  satisfies that inequality on  $\{f>a\}$ .

That proof is more algebra-heavy (you’ll be manipulating  $\nabla g=\nabla f$  and ratios  $g(y)/g(x)$ ), and the composition proof above is the clean BV-intended approach.

* * *

If you paste the exact BV wording of 3.48 (sometimes they specify “proper” or allow extended values), I can align the domain and edge cases (especially  $a=0$  and boundary  $f=a$ ) exactly to the book’s conventions.

## Prompt:
Problem 15.

## Response:
Problem 15 — Hessian of  $h(x)=\log f(x)$  (ultra-granular, from bedrock)
-------------------------------------------------------------------------

We assume:

*    $f:\mathbb R^n\to\mathbb R$  is **twice continuously differentiable** ( $C^2$ ) on its domain.
*    $f(x)>0$  for all  $x$  in the domain (so  $\log f(x)$  is defined and smooth).

Define:

$$
h(x)=\log f(x).
$$

### Goal

Show:

$$
\boxed{ \nabla^2 h(x) = \frac{1}{f(x)}\,\nabla^2 f(x) - \frac{1}{f(x)^2}\,\nabla f(x)\,\nabla f(x)^\top. }
$$

Conventions:

*    $\nabla f(x)\in\mathbb R^n$  is a **column** vector:
    $$
    \nabla f(x)=\begin{bmatrix}f_1(x)\\ \vdots\\ f_n(x)\end{bmatrix}, \quad f_i(x):=\frac{\partial f}{\partial x_i}(x).
    $$
*    $\nabla^2 f(x)\in\mathbb R^{n\times n}$  is the matrix of second partials:
    $$
    \nabla^2 f(x)=\big[f_{ij}(x)\big]_{i,j=1}^n, \quad f_{ij}(x):=\frac{\partial^2 f}{\partial x_i\partial x_j}(x).
    $$

* * *

0) Warm-up: what is the Hessian, concretely?
============================================

The Hessian of  $h$  is the matrix

$$
\nabla^2 h(x)=\big[h_{ij}(x)\big]_{i,j=1}^n, \quad h_{ij}(x):=\frac{\partial^2 h}{\partial x_i\partial x_j}(x).
$$

So to prove the boxed formula, it is enough to prove **for each pair  $(i,j)$ **:

$$
h_{ij}(x)=\frac{1}{f(x)}f_{ij}(x)-\frac{1}{f(x)^2}f_i(x)f_j(x).
$$

Then we’ll recognize the matrix form.

We will do exactly that.

* * *

1) Step 1: compute the gradient  $\nabla h(x)$  component-by-component
======================================================================

Fix an index  $i\in\{1,\dots,n\}$ .

1.1 Write  $h(x)$  as a composition (so we can chain-rule it)
-------------------------------------------------------------

Let the 1D outer function be

$$
\psi(s)=\log s,
$$

and the inner function be

$$
s=f(x).
$$

Then

$$
h(x)=\psi(f(x)).
$$

1.2 The derivative of  $\log$  in 1D
------------------------------------

For  $s>0$ ,

$$
\psi'(s)=\frac{d}{ds}\log s=\frac{1}{s}.
$$

1.3 Apply chain rule for partial derivative  $\partial/\partial x_i$ 
---------------------------------------------------------------------

Chain rule (scalar-on-scalar) says:

$$
\frac{\partial}{\partial x_i}\psi(f(x))=\psi'(f(x))\cdot \frac{\partial f(x)}{\partial x_i}.
$$

Substitute  $\psi'(f(x))=1/f(x)$  and  $\partial f/\partial x_i=f_i(x)$ :

$$
h_i(x):=\frac{\partial h}{\partial x_i}(x) =\frac{1}{f(x)}\,f_i(x).
$$

So the gradient (stacking all components) is:

$$
\boxed{ \nabla h(x)=\frac{1}{f(x)}\,\nabla f(x). }
$$

That’s the first-order part.

* * *

2) Step 2: compute the Hessian entry  $h_{ij}$  by differentiating  $h_i$ 
==========================================================================

We have:

$$
h_i(x)=\frac{f_i(x)}{f(x)}.
$$

Now fix another index  $j$ . We need:

$$
h_{ij}(x)=\frac{\partial}{\partial x_j}\left(\frac{f_i(x)}{f(x)}\right).
$$

This is a quotient (or product) derivative. Let’s do it _carefully_.

* * *

2.1 View it as a product to avoid quotient-rule confusion
---------------------------------------------------------

Write:

$$
h_i(x)=\underbrace{f(x)^{-1}}_{a(x)}\ \underbrace{f_i(x)}_{b(x)}.
$$

So  $h_i=a\cdot b$ , where

$$
a(x)=\frac{1}{f(x)},\qquad b(x)=f_i(x).
$$

Then

$$
h_{ij}=\frac{\partial}{\partial x_j}(a b) =\left(\frac{\partial a}{\partial x_j}\right)b + a\left(\frac{\partial b}{\partial x_j}\right).
$$

This is just the ordinary product rule.

So we need two pieces:

1.   $\partial a/\partial x_j$ ,
2.   $\partial b/\partial x_j$ .

* * *

2.2 Compute  $\partial a/\partial x_j$  where  $a(x)=f(x)^{-1}$ 
----------------------------------------------------------------

Again, it’s a composition.

Let  $\eta(s)=s^{-1}$  (for  $s>0$ ). Then  $a(x)=\eta(f(x))$ .

### 2.2.1 Derivative of  $s^{-1}$  in 1D

$$
\eta'(s)=\frac{d}{ds}(s^{-1}) = -s^{-2}.
$$

### 2.2.2 Apply chain rule

$$
\frac{\partial a}{\partial x_j} = \eta'(f(x))\cdot \frac{\partial f(x)}{\partial x_j} = \left(-f(x)^{-2}\right)\cdot f_j(x) = -\frac{f_j(x)}{f(x)^2}.
$$

So:

$$
\boxed{ a_j(x):=\frac{\partial a}{\partial x_j}(x)= -\frac{f_j(x)}{f(x)^2}. }
$$

* * *

2.3 Compute  $\partial b/\partial x_j$  where  $b(x)=f_i(x)$ 
-------------------------------------------------------------

By definition:

$$
\frac{\partial b}{\partial x_j} = \frac{\partial}{\partial x_j}\left(\frac{\partial f}{\partial x_i}\right) = \frac{\partial^2 f}{\partial x_j\partial x_i} = f_{ij}(x)
$$

(up to symmetry; with  $C^2$ ,  $f_{ij}=f_{ji}$ , but we don’t even need symmetry to write it).

So:

$$
\boxed{ b_j(x):=\frac{\partial b}{\partial x_j}(x)= f_{ij}(x). }
$$

* * *

2.4 Plug into product rule
--------------------------

Recall:

$$
h_{ij}=a_j b + a b_j.
$$

Substitute:

*    $a_j = -\dfrac{f_j}{f^2}$ ,
*    $b = f_i$ ,
*    $a = \dfrac{1}{f}$ ,
*    $b_j = f_{ij}$ .

Compute:

$$
h_{ij} = \left(-\frac{f_j}{f^2}\right)f_i +\left(\frac{1}{f}\right)f_{ij} = \frac{1}{f}f_{ij} -\frac{1}{f^2}f_i f_j.
$$

So for every  $i,j$ ,

$$
\boxed{ h_{ij}(x)=\frac{1}{f(x)}f_{ij}(x)-\frac{1}{f(x)^2}f_i(x)f_j(x). }
$$

That is the exact componentwise identity.

* * *

3) Convert the componentwise formula into matrix form
=====================================================

Let’s identify the matrices:

*   The matrix with entries  $f_{ij}$  is  $\nabla^2 f$ .
*   The rank-1 matrix with entries  $f_i f_j$  is  $\nabla f\,\nabla f^\top$ .

So the componentwise identity becomes:

$$
\nabla^2 h = \frac{1}{f}\nabla^2 f -\frac{1}{f^2}\nabla f\,\nabla f^\top.
$$

Hence the desired formula:

$$
\boxed{ \nabla^2(\log f)(x)=\frac{1}{f(x)}\,\nabla^2 f(x)-\frac{1}{f(x)^2}\,\nabla f(x)\nabla f(x)^\top. }
$$

* * *

4) Directional (quadratic form) version — often the real “intuition”
====================================================================

Take any direction  $v\in\mathbb R^n$ . Multiply left and right by  $v^\top$  and  $v$ :

$$
v^\top \nabla^2(\log f)\,v = \frac{1}{f}\,v^\top(\nabla^2 f)\,v -\frac{1}{f^2}\,v^\top(\nabla f\nabla f^\top)\,v.
$$

Now simplify the second term:

$$
v^\top(\nabla f\nabla f^\top)v = (\nabla f^\top v)(\nabla f^\top v) = (\nabla f^\top v)^2.
$$

So:

$$
\boxed{ v^\top \nabla^2(\log f)\,v = \frac{v^\top \nabla^2 f\,v}{f} - \frac{(\nabla f^\top v)^2}{f^2}. }
$$

Key observation:  $(\nabla f^\top v)^2\ge 0$ .  
So compared to  $\frac{1}{f}\nabla^2 f$ , the Hessian of  $\log f$  is “more negative” by subtracting a PSD rank-1 term.

This is exactly why  $\log$  tends to turn things toward concavity/log-concavity.

* * *

5) Alternative derivation (same result, different algebra): quotient rule
=========================================================================

Starting from  $h_i=f_i/f$ , quotient rule says:

$$
\frac{\partial}{\partial x_j}\left(\frac{f_i}{f}\right) = \frac{f\cdot f_{ij}-f_i\cdot f_j}{f^2} = \frac{1}{f}f_{ij}-\frac{1}{f^2}f_i f_j.
$$

Same result, just packaged differently.

* * *

6) Quick sanity checks (never skip)
===================================

### Check 1: 1D case  $n=1$ 

Then  $h=\log f$ , and the formula becomes:

$$
(\log f)'' = \frac{f''}{f}-\frac{(f')^2}{f^2},
$$

which is the standard calculus identity. Good.

### Check 2: exponential  $f(x)=e^{a^\top x+b}$ 

*    $\log f = a^\top x+b$  is affine ⇒ Hessian should be  $0$ .  
    Compute:
*    $\nabla f = f a$ .
*    $\nabla^2 f = f aa^\top$ .  
    Plug in:
    
$$
\frac{1}{f}(f aa^\top)-\frac{1}{f^2}(fa)(fa)^\top = aa^\top-aa^\top=0.
$$

Passes.

* * *

If you want the next brutality-layer: we can use this identity to prove the standard **second-order condition for log-concavity**:

$$
f \text{ log-concave} \iff \nabla^2(\log f)\preceq 0 \iff f\nabla^2 f - \nabla f\nabla f^\top \preceq 0,
$$

and then connect it directly back to Exercise 3.47’s first-order inequality via integration along a line.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)
