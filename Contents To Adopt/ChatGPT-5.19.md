# 5.19

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:12:38  
**Updated:** 12/28/2025 23:34:42  
**Exported:** 12/29/2025 0:10:57  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060d5-bc54-832b-a885-2f6d29c89717](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/695060d5-bc54-832b-a885-2f6d29c89717)  

## Response:
Thought for 2m 7s

Let’s go slowly and build intuition as we go. This exercise is really about one idea:

**“Sum of the largest  $r$  components” = “best you can do by selecting  $r$  components.”**  
And “best you can do by selecting” is naturally an LP (linear program).

* * *

0) What is  $f(x)$  exactly?
----------------------------

You have a vector  $x \in \mathbb{R}^n$ . Sort its components in decreasing order:

$$
x_{[1]} \ge x_{[2]} \ge \cdots \ge x_{[n]}.
$$

Then define

$$
f(x) = \sum_{i=1}^r x_{[i]}.
$$

So  $f(x)$  is: **take the  $r$  biggest entries of  $x$ , add them up**.

Example: if  $x=(3,-1,2,2)$  and  $r=2$ , sorted is  $(3,2,2,-1)$ , so  $f(x)=3+2=5$ .

* * *

(a) Show  $f(x)$  equals an LP optimal value
--------------------------------------------

The LP is:

$$
\begin{aligned} \text{maximize} \quad & x^T y \\ \text{subject to} \quad & 0 \le y \le 1 \\ & \mathbf{1}^T y = r, \end{aligned}
$$

with variable  $y \in \mathbb{R}^n$ .

### Step 1: Interpret the constraints on  $y$ 

*    $0 \le y_i \le 1$ : each  $y_i$  is like a “selection weight” for component  $x_i$ , between not chosen (0) and fully chosen (1).
*    $\mathbf{1}^T y = r$ : the total selection weight is exactly  $r$ .

So you are distributing “selection mass”  $r$  across the coordinates, but each coordinate can receive at most 1.

### Step 2: Why the optimal  $y$  will pick the largest entries

The objective is

$$
x^T y = \sum_{i=1}^n x_i y_i.
$$

To maximize this, you want to put as much  $y_i$  as possible on the indices where  $x_i$  is large.

Intuition: if  $x_i > x_j$  and you’re currently giving some mass to  $j$  while  $i$  isn’t maxed out, you should move weight from  $j$  to  $i$  to increase the objective.

### Step 3: Formal “swap” argument (crystal-clear)

Take any feasible  $y$ . Suppose there exist indices  $i,j$  such that:

*    $x_i > x_j$ ,
*    $y_i < 1$  (so  $i$  still has room),
*    $y_j > 0$  (so  $j$  has some mass you can take away).

Define a small  $\varepsilon>0$  such that  $\varepsilon \le 1-y_i$  and  $\varepsilon \le y_j$ . Now modify:

*    $y_i' = y_i + \varepsilon$ 
*    $y_j' = y_j - \varepsilon$ 
*   all other coordinates unchanged.

Then constraints still hold:

*   bounds  $0\le y'\le 1$  still hold by the choice of  $\varepsilon$ ,
*   sum constraint  $\mathbf{1}^T y' = \mathbf{1}^T y = r$  still holds (we added and subtracted the same  $\varepsilon$ ).

Objective change:

$$
x^T y' - x^T y = x_i\varepsilon - x_j\varepsilon = (x_i-x_j)\varepsilon > 0.
$$

So any feasible  $y$  that puts weight on a smaller  $x_j$  while a larger  $x_i$  isn’t saturated cannot be optimal.

**Conclusion:** at optimum, you must have  $y_i=1$  on the indices of the largest  $r$  entries, and  $y_i=0$  elsewhere (up to ties).

### Step 4: What is the optimal value then?

If  $y$  is exactly “choose the largest  $r$  entries,” then

$$
x^T y = \sum_{i=1}^r x_{[i]} = f(x).
$$

So the LP optimal value is  $f(x)$ . ✅

(Another clean way to say this: the feasible region is a polytope whose extreme points are exactly the  $0/1$  vectors with exactly  $r$  ones; linear objectives achieve optimum at an extreme point; and the best extreme point picks the largest  $r$ .)

* * *

(b) Derive the dual and the compact constraint form
---------------------------------------------------

### Step 1: Put the primal LP into “standard” inequality form

We have:

*    $y \le \mathbf{1}$ 
*    $\mathbf{1}^T y = r$  (turn into two inequalities)
    *    $\mathbf{1}^T y \le r$ 
    *    $-\mathbf{1}^T y \le -r$ 
*   and  $y \ge 0$ 

So primal is:

$$
\begin{aligned} \max \ & x^T y \\ \text{s.t. } & y \le \mathbf{1} \\ & \mathbf{1}^T y \le r \\ & -\mathbf{1}^T y \le -r \\ & y \ge 0. \end{aligned}
$$

### Step 2: Assign dual variables

*   For  $y \le \mathbf{1}$ : dual variable  $u \in \mathbb{R}^n_+$ 
*   For  $\mathbf{1}^T y \le r$ : dual scalar  $s \ge 0$ 
*   For  $-\mathbf{1}^T y \le -r$ : dual scalar  $v \ge 0$ 

### Step 3: Write the dual objective  $b^T\lambda$ 

Right-hand-sides are  $\mathbf{1}$ ,  $r$ ,  $-r$ . So:

$$
\min \ \mathbf{1}^T u + r s + (-r)v = \min \ \mathbf{1}^T u + r(s-v).
$$

### Step 4: Write the dual constraints  $A^T\lambda \ge c$ 

The constraint matrix rows are:

*    $I$  for  $y \le \mathbf{1}$ 
*    $\mathbf{1}^T$  for  $\mathbf{1}^T y \le r$ 
*    $-\mathbf{1}^T$  for  $-\mathbf{1}^T y \le -r$ 

So

$$
I^T u + \mathbf{1}s + (-\mathbf{1})v \ \ge\ x \quad\Longleftrightarrow\quad u + (s-v)\mathbf{1} \ge x.
$$

Now define a free scalar

$$
t := s-v \quad (\text{difference of two nonnegative numbers, so } t \in \mathbb{R}\ \text{is unrestricted}).
$$

Then the dual becomes exactly:

$$
\begin{aligned} \text{minimize}\quad & r t + \mathbf{1}^T u \\ \text{subject to}\quad & t\mathbf{1} + u \ge x \\ & u \ge 0, \end{aligned}
$$

with variables  $t\in\mathbb{R}$ ,  $u\in\mathbb{R}^n$ . ✅

### Step 5: Turn the inequality  $f(x)\le \alpha$  into a compact system

From (a), primal optimum =  $f(x)$ . From strong LP duality, dual optimum = primal optimum. Therefore:

$$
f(x) \le \alpha \quad\Longleftrightarrow\quad \exists\, (t,u)\ \text{s.t.}\ \begin{cases} rt + \mathbf{1}^T u \le \alpha,\\ t\mathbf{1} + u \ge x,\\ u \ge 0. \end{cases}
$$

That’s the “compact representation”: instead of  $\binom{n}{r}$  subset inequalities, you use  $2n+1$  linear inequalities in  $(x,u,t)$ .

Extra intuition (very useful): for fixed  $t$ , the best (smallest)  $u$  satisfying  $t+u_i\ge x_i, u_i\ge0$  is

$$
u_i = \max(0, x_i - t).
$$

So the dual objective becomes

$$
rt + \sum_{i=1}^n \max(0, x_i - t),
$$

and minimizing over  $t$  “finds the threshold” that captures exactly the top  $r$  pieces. This is closely related to CVaR-type formulas in risk theory.

* * *

(c) Add the diversification constraint to Markowitz and write as a QP
---------------------------------------------------------------------

The Markowitz problem given is:

$$
\begin{aligned} \text{minimize}\quad & x^T \Sigma x \\ \text{subject to}\quad & \bar p^T x \ge r_{\min}\\ & \mathbf{1}^T x = 1 \\ & x \ge 0, \end{aligned}
$$

where  $x$  is the portfolio weights.

Diversification constraint says:

*   Let  $r = \lfloor 0.1n \rfloor$  (that’s what  $[0.1n]$  means here: integer part).
*   Then “no more than 80% of the budget can be invested in the top 10% of assets” becomes:
    
$$
\sum_{i=1}^{r} x_{[i]} \le 0.8 \quad\Longleftrightarrow\quad f(x) \le 0.8
$$

with this new  $r$ .

Using (b), this is equivalent to: there exist  $t\in\mathbb{R}$ ,  $u\in\mathbb{R}^n$  such that

$$
rt + \mathbf{1}^T u \le 0.8,\qquad t\mathbf{1} + u \ge x,\qquad u \ge 0.
$$

### Final QP formulation (objective quadratic, constraints linear)

Decision variables:  $x\in\mathbb{R}^n$ ,  $u\in\mathbb{R}^n$ ,  $t\in\mathbb{R}$ .

$$
\begin{aligned} \text{minimize}\quad & x^T \Sigma x \\ \text{subject to}\quad & \bar p^T x \ge r_{\min}\\ & \mathbf{1}^T x = 1 \\ & x \ge 0 \\ & rt + \mathbf{1}^T u \le 0.8 \\ & t\mathbf{1} + u \ge x \\ & u \ge 0. \end{aligned}
$$

That is a convex QP because:

*    $x^T\Sigma x$  is convex when  $\Sigma \succeq 0$  (covariance matrices are PSD),
*   everything else is linear equalities/inequalities.

If you want “canonical QP” notation, you can also write the objective as  $\tfrac12 x^T(2\Sigma)x$ , but it’s the same optimization problem.

* * *

If you want, I can also show (with a tiny example  $n=5$ ) how the  $t,u$  constraints literally “reconstruct” the sum of the top  $r$  entries, so you can _see_ why the compact form works mechanically—not just algebraically.

## Response:
Thought for 1m 8s

Below is a complete, rigorous, step-by-step solution to Exercise 5.19.

* * *

Problem setup (what is being studied)
-------------------------------------

Fix an integer  $r\in\{1,\dots,n\}$ . For  $x\in\mathbb{R}^n$ , let

$$
x_{[1]} \ge x_{[2]} \ge \cdots \ge x_{[n]}
$$

denote the components of  $x$  sorted in **nonincreasing** order. Define

$$
f(x) := \sum_{i=1}^r x_{[i]},
$$

i.e. the sum of the  $r$  largest components of  $x$ .

We study the constraint  $f(x)\le \alpha$ , and the exercise asks for a compact LP-based representation.

* * *

(a) Show  $f(x)$  equals the optimal value of an LP
---------------------------------------------------

### Claim

For any  $x\in\mathbb{R}^n$ ,

$$
f(x) \;=\; \max \left\{x^T y \;:\; 0\le y\le \mathbf 1,\ \mathbf 1^T y = r\right\}.
$$

(Here inequalities are componentwise, and  $y\in\mathbb{R}^n$  is the decision variable.)

Let the feasible set be

$$
\mathcal{Y}:=\{y\in\mathbb{R}^n:\ 0\le y\le \mathbf 1,\ \mathbf 1^T y=r\}.
$$

We will prove the claim in two clean steps:

1.  characterize the extreme points of  $\mathcal{Y}$ ;
2.  use “linear objective achieves optimum at an extreme point.”

* * *

### Step 1:  $\mathcal{Y}$  is a bounded polytope

It is defined by linear equalities/inequalities, so it is a polyhedron. Also  $0\le y\le \mathbf 1$  makes it bounded, so it is a **polytope**. Therefore, a linear objective  $x^T y$  attains its maximum over  $\mathcal{Y}$ .

* * *

### Step 2: Identify the extreme points of  $\mathcal{Y}$ 

**Lemma.** The extreme points of  $\mathcal{Y}$  are exactly the  $\{0,1\}$ \-vectors with exactly  $r$  ones:

$$
\operatorname{ext}(\mathcal{Y}) =\left\{y\in\{0,1\}^n:\ \mathbf 1^T y=r\right\}.
$$

**Proof.**

**(i) Any such  $\{0,1\}$  vector is feasible.**  
If  $y\in\{0,1\}^n$  and  $\mathbf 1^T y=r$ , then clearly  $0\le y\le \mathbf 1$  and  $\mathbf 1^T y=r$ , so  $y\in\mathcal{Y}$ .

**(ii) Any feasible  $y$  that has a fractional component cannot be extreme.**  
Suppose  $y\in\mathcal{Y}$  and at least two components are strictly between 0 and 1. That is, there exist indices  $i\neq j$  with

$$
0<y_i<1,\qquad 0<y_j<1.
$$

Define the perturbation vector  $d\in\mathbb{R}^n$  by  $d_i=1$ ,  $d_j=-1$ , and  $d_k=0$  for  $k\notin\{i,j\}$ . Then  $\mathbf 1^T d = 1 + (-1)=0$ .

Pick  $\varepsilon>0$  small enough that

$$
0\le y_i\pm \varepsilon \le 1,\qquad 0\le y_j\mp \varepsilon \le 1.
$$

This is possible because  $y_i,y_j$  are in the interior  $(0,1)$ . Now set

$$
y^{+}:=y+\varepsilon d,\qquad y^{-}:=y-\varepsilon d.
$$

Then:

*   Bounds: by construction  $0\le y^{\pm}\le \mathbf 1$ .
*   Sum constraint:  $\mathbf 1^T y^{\pm} = \mathbf 1^T y \pm \varepsilon\,\mathbf 1^T d = r\pm \varepsilon\cdot 0=r$ .

So  $y^{+},y^{-}\in\mathcal{Y}$ , and  $y=\tfrac12 y^{+}+\tfrac12 y^{-}$  with  $y^{+}\neq y^{-}$ . Hence  $y$  is **not** an extreme point.

**(iii) Therefore any extreme point can have at most one fractional component.**  
From (ii), an extreme point cannot have two fractional components. So an extreme point can have either 0 or 1 fractional component.

**(iv) But it cannot have exactly one fractional component because  $\mathbf 1^T y=r$  is an integer.**  
If exactly one component  $y_k$  were fractional and all others were in  $\{0,1\}$ , then  $\mathbf 1^T y$  would be “integer + fractional,” hence not an integer—contradiction, since  $\mathbf 1^T y=r\in\mathbb{Z}$ .

So an extreme point has **no fractional components**, i.e. is in  $\{0,1\}^n$ . With  $\mathbf 1^T y=r$ , it must have exactly  $r$  ones.

This proves the lemma. ∎

* * *

### Step 3: Reduce the LP to choosing a subset of size  $r$ 

Because the objective is linear and  $\mathcal{Y}$  is a polytope,

$$
\max_{y\in\mathcal{Y}} x^T y
$$

is attained at an extreme point. By the lemma, every extreme point corresponds to choosing a subset  $S\subseteq\{1,\dots,n\}$  with  $|S|=r$  via

$$
y_i = \begin{cases} 1,& i\in S\\ 0,& i\notin S. \end{cases}
$$

Then

$$
x^T y = \sum_{i\in S} x_i.
$$

So the LP value is

$$
\max_{|S|=r}\ \sum_{i\in S} x_i.
$$

* * *

### Step 4: Show the best subset is “the top  $r$  entries”

Let  $\pi$  be a permutation such that  $x_{\pi(1)}=x_{[1]},\dots,x_{\pi(n)}=x_{[n]}$ . Consider the subset

$$
S^\star := \{\pi(1),\dots,\pi(r)\},
$$

i.e. indices of the  $r$  largest components. Then

$$
\sum_{i\in S^\star} x_i = \sum_{k=1}^r x_{\pi(k)} = \sum_{k=1}^r x_{[k]} = f(x).
$$

Now we argue no other subset can do better:

Take any subset  $S$  with  $|S|=r$ . Let its elements, when sorted by their  $x$ \-values, be  $i_1,\dots,i_r$  such that

$$
x_{i_1}\ge x_{i_2}\ge \cdots \ge x_{i_r}.
$$

Since  $x_{[k]}$  is the  $k$ \-th largest component overall, we must have

$$
x_{i_k}\le x_{[k]}\quad \text{for each }k=1,\dots,r.
$$

(Reason: among all components, the  $k$ \-th largest is  $x_{[k]}$ ; the  $k$ \-th largest within any particular subset cannot exceed that.)  
Summing:

$$
\sum_{i\in S} x_i = \sum_{k=1}^r x_{i_k} \le \sum_{k=1}^r x_{[k]} = f(x).
$$

Thus the maximum over all subsets  $|S|=r$  equals  $f(x)$ , achieved by  $S^\star$ .

Therefore,

$$
\max_{y\in\mathcal{Y}} x^T y \;=\; f(x).
$$

This proves part (a). ✅

* * *

(b) Derive the dual and obtain the compact representation for  $f(x)\le \alpha$ 
--------------------------------------------------------------------------------

We start from the primal LP in (a):

$$
\begin{aligned} \text{maximize}\quad & x^T y\\ \text{subject to}\quad & 0\le y\le \mathbf 1,\\ & \mathbf 1^T y = r. \end{aligned} \tag{P}
$$

### Step 1: Put constraints into standard inequality/equality form

Write

$$
y \le \mathbf 1,\qquad -y \le 0,\qquad \mathbf 1^T y - r = 0.
$$

### Step 2: Form the Lagrangian (carefully)

Introduce dual variables:

*    $u\in\mathbb{R}^n_+$  for  $y-\mathbf 1\le 0$ ,
*    $v\in\mathbb{R}^n_+$  for  $-y\le 0$ ,
*    $t\in\mathbb{R}$  (free) for  $\mathbf 1^T y - r = 0$ .

Because the primal is a **maximization**, a clean way is to convert it to minimization by negating the objective. Equivalent primal:

$$
\begin{aligned} \text{minimize}\quad & -x^T y\\ \text{subject to}\quad & y-\mathbf 1\le 0,\\ & -y \le 0,\\ & \mathbf 1^T y - r = 0. \end{aligned} \tag{P-min}
$$

Now the Lagrangian is

$$
\begin{aligned} L(y,u,v,t) &= -x^T y \;+\; u^T(y-\mathbf 1)\;+\; v^T(-y)\;+\; t(\mathbf 1^T y-r)\\ &= \Big(-x + u - v + t\mathbf 1\Big)^T y \;-\; \mathbf 1^T u \;-\; rt. \end{aligned}
$$

### Step 3: Compute the dual function  $g(u,v,t)=\inf_y L(y,u,v,t)$ 

*   If the coefficient of  $y$  is nonzero, i.e.  $-x+u-v+t\mathbf 1\neq 0$ , then  $\inf_y L=-\infty$  because  $y$  is unconstrained in the Lagrangian minimization.
*   Therefore, for the infimum to be finite, we must impose
    
$$
-x + u - v + t\mathbf 1 = 0 \quad\Longleftrightarrow\quad u - v + t\mathbf 1 = x.
$$

Under this condition,

$$
g(u,v,t)= -\mathbf 1^T u - rt.
$$

### Step 4: Write the dual optimization problem

The Lagrange dual of a minimization primal is:

$$
\text{maximize } g(u,v,t)\ \text{ subject to } u\ge 0,\ v\ge 0,\ t\in\mathbb{R},\ u-v+t\mathbf 1=x.
$$

So:

$$
\begin{aligned} \text{maximize}\quad & -\mathbf 1^T u - rt\\ \text{subject to}\quad & u - v + t\mathbf 1 = x,\\ & u\ge 0,\ v\ge 0. \end{aligned} \tag{D1}
$$

Now convert this to the equivalent minimization form by multiplying the objective by  $-1$ :

$$
\begin{aligned} \text{minimize}\quad & \mathbf 1^T u + rt\\ \text{subject to}\quad & u - v + t\mathbf 1 = x,\\ & u\ge 0,\ v\ge 0. \end{aligned} \tag{D1-min}
$$

### Step 5: Eliminate  $v$  to get the stated compact dual

From the equality constraint:

$$
u = x - t\mathbf 1 + v.
$$

Since  $v\ge 0$ , this implies

$$
u \ge x - t\mathbf 1 \quad\Longleftrightarrow\quad t\mathbf 1 + u \ge x.
$$

Also  $u\ge 0$  remains.

Conversely, if  $u\ge 0$  and  $t\mathbf 1+u\ge x$ , define

$$
v := u - (x - t\mathbf 1) = u + t\mathbf 1 - x \ge 0,
$$

which satisfies the equality  $u-v+t\mathbf 1=x$ . So the conditions are equivalent.

Therefore the dual can be written with only  $(t,u)$  as:

$$
\begin{aligned} \text{minimize}\quad & rt+\mathbf 1^T u\\ \text{subject to}\quad & t\mathbf 1 + u \ge x,\\ & u\ge 0, \end{aligned} \tag{D}
$$

which is exactly what the problem statement claims. ✅

### Step 6: Justify “same optimal value” (strong duality)

This is an LP with a nonempty, bounded feasible set:

*   Feasible: since  $r\in\{1,\dots,n\}$ , pick any  $y\in\{0,1\}^n$  with exactly  $r$  ones, then  $0\le y\le 1$  and  $\mathbf 1^T y=r$ .
*   Bounded:  $0\le y\le 1$  implies bounded.  
    So the primal optimal value is finite, and LP strong duality applies: primal optimum = dual optimum.

Combine with part (a): primal optimum =  $f(x)$ . Hence dual optimum =  $f(x)$  as well.

### Step 7: Convert the constraint  $f(x)\le \alpha$  into existence of  $(t,u)$ 

Since

$$
f(x)=\min\{rt+\mathbf 1^T u:\ t\mathbf 1+u\ge x,\ u\ge 0\},
$$

we have

$$
f(x)\le \alpha \quad\Longleftrightarrow\quad \exists\, t\in\mathbb{R},\ u\in\mathbb{R}^n \text{ such that } \begin{cases} rt+\mathbf 1^T u \le \alpha,\\ t\mathbf 1+u \ge x,\\ u\ge 0. \end{cases}
$$

This gives a compact representation using  $2n+1$  linear inequalities in variables  $(x,u,t)$ . ✅

* * *

(c) Markowitz portfolio with the diversification constraint as a QP
-------------------------------------------------------------------

### Step 1: Base Markowitz problem (given)

Decision variable: portfolio weights  $x\in\mathbb{R}^n$ .

Given:

*    $\bar p\in\mathbb{R}^n$ : mean return vector,
*    $\Sigma\in\mathbb{S}^n_+$ : covariance matrix (PSD),
*    $r_{\min}$ : required minimum expected return.

The standard Markowitz QP:

$$
\begin{aligned} \text{minimize}\quad & x^T\Sigma x\\ \text{subject to}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf 1^T x = 1,\\ & x \ge 0. \end{aligned}
$$

### Step 2: Write the diversification constraint using  $f(x)$ 

The diversification constraint says:

> “No more than 80% of the total budget can be invested in the top 10% of assets.”

Top 10% by _weight_ means “sum of the largest  $r$  components of  $x$ ” where

$$
r = [0.1n].
$$

Different books use  $[\,\cdot\,]$  differently; the usual interpretation in this context is the nearest integer or integer part. To be concrete and standard in optimization modeling, take

$$
r := \lfloor 0.1n\rfloor
$$

(or if your course defines  $[\,\cdot\,]$  as nearest integer, replace  $\lfloor\cdot\rfloor$  accordingly; the modeling steps are identical).

Then the constraint is:

$$
\sum_{i=1}^{r} x_{[i]} \le 0.8 \quad\Longleftrightarrow\quad f(x)\le 0.8.
$$

### Step 3: Replace  $f(x)\le 0.8$  by the compact linear system from (b)

Using the result from (b),  $f(x)\le 0.8$  is equivalent to existence of variables  $t\in\mathbb{R}$  and  $u\in\mathbb{R}^n$  such that

$$
\begin{cases} rt+\mathbf 1^T u \le 0.8,\\ t\mathbf 1 + u \ge x,\\ u\ge 0. \end{cases}
$$

### Step 4: Final QP formulation (objective quadratic, constraints linear)

Decision variables:  $x\in\mathbb{R}^n$ ,  $u\in\mathbb{R}^n$ ,  $t\in\mathbb{R}$ .

$$
\boxed{ \begin{aligned} \text{minimize}\quad & x^T\Sigma x\\[2mm] \text{subject to}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf 1^T x = 1,\\ & x \ge 0,\\[1mm] & rt+\mathbf 1^T u \le 0.8,\\ & t\mathbf 1 + u \ge x,\\ & u \ge 0. \end{aligned}}
$$

This is a convex QP because:

*    $x^T\Sigma x$  is convex when  $\Sigma\succeq 0$ ,
*   all constraints are linear.

That completes part (c). ✅

## Response:
Thought for 6s

Got it. I’ll write the “real” version: slower, more rigorous, and with all the little facts proved instead of hand-waved. This problem is a classic because it turns a nasty-looking “sort-and-sum” object into a clean LP/QP modeling primitive.

I’ll go in three layers:

1.  What  $f(x)$  really is (as a combinatorial max over subsets), and why it’s convex.
2.  Part (a): prove the LP representation carefully (two proofs: extreme-point proof + exchange argument).
3.  Part (b): derive the dual in full detail and prove the “compact constraint” equivalence, including why it replaces  $\binom nr$  inequalities.
4.  Part (c): plug it into Markowitz and show the final QP in explicit modeling form (dimensions, variables, and why it’s convex).

* * *

1) First principles: what is  $f(x)$ ?
--------------------------------------

### 1.1 Sorting notation and ties

For  $x\in\mathbb{R}^n$ , let  $(x_{[1]},\dots,x_{[n]})$  be the components sorted so that

$$
x_{[1]} \ge x_{[2]} \ge \cdots \ge x_{[n]}.
$$

If there are ties (equal components), the sorted order is not unique, but the **multiset**  $\{x_{[1]},\dots,x_{[n]}\}$  is uniquely determined, and so is any symmetric function of the sorted values, including  $\sum_{i=1}^r x_{[i]}$ . So  $f(x)$  is well-defined even with ties.

### 1.2 The key combinatorial identity

Define, for any subset  $S\subseteq\{1,\dots,n\}$  with  $|S|=r$ ,

$$
\phi_S(x):=\sum_{i\in S} x_i.
$$

**Claim (fundamental):**

$$
f(x)=\max_{S:\ |S|=r}\ \sum_{i\in S} x_i.
$$

**Reason:** the maximum sum of  $r$  components is achieved by choosing the  $r$  largest components.

**Proof (rigorous):** Let  $S^\star$  be indices of the  $r$  largest components of  $x$  (break ties arbitrarily). Then  $\sum_{i\in S^\star}x_i=f(x)$ . Now take any other  $S$  with  $|S|=r$ . Let its elements be ordered so that

$$
x_{i_1}\ge x_{i_2}\ge \cdots \ge x_{i_r}.
$$

Since  $x_{[k]}$  is the  $k$ \-th largest component overall, we must have  $x_{i_k}\le x_{[k]}$  for each  $k=1,\dots,r$ . Summing gives

$$
\sum_{i\in S}x_i=\sum_{k=1}^r x_{i_k}\le \sum_{k=1}^r x_{[k]}=f(x).
$$

So no subset beats  $S^\star$ . Hence the max equals  $f(x)$ . ∎

This identity is the conceptual core of the whole exercise. The LP in (a) is just a continuous relaxation that happens to be exact.

### 1.3 Why this constraint explodes combinatorially

The book mentions the equivalence

$$
f(x)\le \alpha \quad \Longleftrightarrow \quad \sum_{i\in S}x_i \le \alpha\quad \text{for all }S\subseteq\{1,\dots,n\},\ |S|=r.
$$

This is immediate from the max-over-subsets identity:

*   If  $f(x)\le\alpha$ , then for any  $S$  with  $|S|=r$ ,  
     $\sum_{i\in S}x_i \le \max_{|T|=r}\sum_{i\in T}x_i=f(x)\le\alpha$ .
*   Conversely, if  $\sum_{i\in S}x_i\le\alpha$  for all such  $S$ , then the maximum over  $S$  is also  $\le\alpha$ , i.e.  $f(x)\le\alpha$ .

There are  $\binom nr$  such inequalities, which is enormous even for moderate  $n$ . The whole point is to replace them by  $O(n)$  constraints.

* * *

2) Part (a): LP representation of  $f(x)$ 
------------------------------------------

We must show:

$$
f(x) \;=\; \max \left\{x^T y:\ 0\le y\le \mathbf 1,\ \mathbf 1^T y = r\right\}.
$$

Call the feasible set

$$
\mathcal{Y}:=\{y\in\mathbb{R}^n:\ 0\le y_i\le 1,\ \sum_{i=1}^n y_i = r\}.
$$

Think of  $y_i$  as “how much we select component  $i$ .” Total selection mass is exactly  $r$ , and each coordinate can get at most 1 unit.

I’ll give two proofs because each teaches something different.

* * *

### Proof 1 (polytope + extreme points, fully proved)

#### Step A:  $\mathcal{Y}$  is a polytope

It’s defined by linear equalities and inequalities, and bounded by  $0\le y\le 1$ . So it’s a nonempty bounded polyhedron, i.e. a polytope.

#### Step B: Linear objectives achieve optimum at extreme points

Fact from linear programming/convexity:

> If  $P$  is a nonempty polytope and  $c^T y$  is linear, then  $\max_{y\in P} c^T y$  is attained at an extreme point of  $P$ .

I won’t re-prove the full theorem (it’s standard), but the intuition is: if the maximizer were not extreme, you could write it as a convex combination of two distinct feasible points and at least one of them would do at least as well.

So we need to characterize extreme points of  $\mathcal{Y}$ .

#### Step C: Characterize  $\mathrm{ext}(\mathcal{Y})$ 

**Lemma:**

$$
\mathrm{ext}(\mathcal{Y})=\{y\in\{0,1\}^n:\ \mathbf 1^T y = r\}.
$$

**Proof (no shortcuts):**

1.  **Any  $0/1$  vector with  $r$  ones is feasible.**  
    Immediate: if  $y_i\in\{0,1\}$ , then  $0\le y_i\le 1$ ; and if it has  $r$  ones, its sum is  $r$ .
2.  **Any feasible  $y$  with two fractional components is not extreme.**  
    Assume  $y\in\mathcal{Y}$  and there exist distinct indices  $i\neq j$  with
    
$$
0<y_i<1,\quad 0<y_j<1.
$$

Define direction  $d\in\mathbb{R}^n$  by  $d_i=1$ ,  $d_j=-1$ , others 0. Then  $\mathbf 1^T d=0$ . Choose  $\varepsilon>0$  small enough that

$$
y_i\pm \varepsilon \in [0,1],\qquad y_j\mp \varepsilon \in [0,1].
$$

Possible because  $y_i,y_j$  are strictly inside  $(0,1)$ . Define

$$
y^+ := y+\varepsilon d,\qquad y^- := y-\varepsilon d.
$$

Then:

*   Bounds hold by construction.
*   Sum holds because  $\mathbf 1^T y^\pm = \mathbf 1^T y \pm \varepsilon \mathbf 1^T d = r$ .  
    So  $y^\pm\in\mathcal{Y}$  and  $y=\tfrac12(y^+ + y^-)$  with  $y^+\neq y^-$ . Hence  $y$  is not extreme.
    3.  **Therefore an extreme point has at most one fractional component.**
4.  **But it cannot have exactly one fractional component because  $\sum y_i=r$  is an integer.**  
    If exactly one component were fractional and the rest were  $0$  or  $1$ , then  $\sum y_i$  would be “integer + non-integer,” hence non-integer, contradicting  $\sum y_i=r\in\mathbb{Z}$ .

So extreme points have no fractional components: they are  $0/1$ , and the sum constraint forces exactly  $r$  ones. ∎

#### Step D: Reduce the LP to subset selection

At any extreme point  $y$ , the objective is

$$
x^T y = \sum_{i=1}^n x_i y_i = \sum_{i:\ y_i=1} x_i.
$$

So maximizing over extreme points is the same as

$$
\max_{S:\ |S|=r}\ \sum_{i\in S} x_i.
$$

But by the max-over-subsets identity proved in Section 1.2, this equals  $f(x)$ .

Therefore the LP optimal value equals  $f(x)$ . ✅

* * *

### Proof 2 (direct “exchange argument,” no polytope theory)

Let  $y\in\mathcal{Y}$  be optimal. Suppose there exist indices  $i,j$  such that:

*    $x_i > x_j$ ,
*    $y_i < 1$ ,
*    $y_j > 0$ .

Define  $\varepsilon := \min\{1-y_i,\ y_j\} > 0$ . Construct  $y'$  by moving  $\varepsilon$  mass from  $j$  to  $i$ :

$$
y'_i = y_i + \varepsilon,\quad y'_j = y_j - \varepsilon,\quad y'_k=y_k \ (k\neq i,j).
$$

Then  $y'$  stays feasible (bounds and sum preserved). Objective change:

$$
x^T y' - x^T y = x_i\varepsilon - x_j\varepsilon = (x_i-x_j)\varepsilon > 0,
$$

contradicting optimality of  $y$ . Therefore at optimum, you cannot put any positive mass on a smaller  $x_j$  while a larger  $x_i$  is not saturated.

This forces the structure: optimal  $y$  must allocate  $y_i=1$  to the  $r$  largest components (and  $0$  elsewhere, except possibly fractional splitting among ties). The achieved value is exactly  $\sum_{i=1}^r x_{[i]}=f(x)$ . ✅

* * *

3) Part (b): derive the dual, then turn  $f(x)\le \alpha$  into  $O(n)$  inequalities
-------------------------------------------------------------------------------------

We start from the primal LP:

$$
\begin{aligned} \max_{y\in\mathbb{R}^n}\quad & x^T y\\ \text{s.t.}\quad & 0\le y\le \mathbf 1,\\ & \mathbf 1^T y=r. \end{aligned} \tag{P}
$$

### 3.1 Rewrite constraints in a form convenient for Lagrangian duality

The constraints are:

*    $y \le \mathbf 1$  (componentwise)
*    $y \ge 0$  is  $-y\le 0$ 
*    $\mathbf 1^T y = r$ 

So:

$$
y-\mathbf 1 \le 0,\qquad -y\le 0,\qquad \mathbf 1^T y - r =0.
$$

### 3.2 Form the Lagrangian carefully (sign discipline)

A standard sign-safe route is to convert to minimization. Maximize  $x^Ty$  is equivalent to minimize  $-x^Ty$ . So consider:

$$
\begin{aligned} \min_y\quad & -x^T y\\ \text{s.t.}\quad & y-\mathbf 1 \le 0,\\ & -y\le 0,\\ & \mathbf 1^T y - r = 0. \end{aligned} \tag{P-min}
$$

Introduce multipliers:

*    $u\in\mathbb{R}^n_+$  for  $y-\mathbf 1\le 0$ ,
*    $v\in\mathbb{R}^n_+$  for  $-y\le 0$ ,
*    $t\in\mathbb{R}$  (free) for equality  $\mathbf 1^T y - r = 0$ .

Lagrangian:

$$
\begin{aligned} L(y,u,v,t) &= -x^T y + u^T(y-\mathbf 1) + v^T(-y) + t(\mathbf 1^T y - r)\\ &= \big(-x + u - v + t\mathbf 1\big)^T y \;-\; \mathbf 1^T u \;-\; rt. \end{aligned}
$$

### 3.3 Dual function  $g(u,v,t)=\inf_y L(y,u,v,t)$ 

Since  $y$  is unconstrained in the Lagrangian minimization, the infimum is:

*    $-\infty$  if the coefficient of  $y$  is nonzero,
*   finite (equal to the constant term) only if the coefficient is exactly 0.

So we need:

$$
-x + u - v + t\mathbf 1 = 0 \quad\Longleftrightarrow\quad u - v + t\mathbf 1 = x. \tag{stationarity}
$$

Under this, the  $y$ \-term disappears and

$$
g(u,v,t)= -\mathbf 1^T u - rt.
$$

### 3.4 The dual problem

The dual of a minimization primal is maximize the dual function subject to feasibility of multipliers:

$$
\begin{aligned} \max_{u,v,t}\quad & -\mathbf 1^T u - rt\\ \text{s.t.}\quad & u - v + t\mathbf 1 = x,\\ & u\ge 0,\ v\ge 0. \end{aligned} \tag{D1}
$$

Flip to minimization (multiply objective by  $-1$ ):

$$
\begin{aligned} \min_{u,v,t}\quad & \mathbf 1^T u + rt\\ \text{s.t.}\quad & u - v + t\mathbf 1 = x,\\ & u\ge 0,\ v\ge 0. \end{aligned} \tag{D1-min}
$$

### 3.5 Eliminate  $v$  to get the compact dual in the book

From  $u - v + t\mathbf 1 = x$ , we have

$$
v = u + t\mathbf 1 - x.
$$

Constraint  $v\ge 0$  becomes

$$
u + t\mathbf 1 - x \ge 0 \quad\Longleftrightarrow\quad t\mathbf 1 + u \ge x.
$$

So we can drop  $v$  and write:

$$
\boxed{ \begin{aligned} \min_{t\in\mathbb{R},\ u\in\mathbb{R}^n}\quad & rt + \mathbf 1^T u\\ \text{s.t.}\quad & t\mathbf 1 + u \ge x,\\ & u\ge 0. \end{aligned}} \tag{D}
$$

This matches exactly.

### 3.6 Strong duality justification (why the dual value equals  $f(x)$ )

This is an LP. A sufficient condition for strong duality is that the primal is feasible and bounded (or Slater-type conditions for LP; feasibility + boundedness is enough here).

*   Feasible: choose  $y$  with exactly  $r$  ones and the rest zeros, then  $0\le y\le 1$  and  $\mathbf 1^T y=r$ .
*   Bounded: because  $0\le y\le 1$ , the objective  $x^T y$  is bounded above by  $\sum_i \max(x_i,0)$ , finite.

Hence both primal and dual have equal optimal value.

Combine with part (a): primal optimum =  $f(x)$ . Therefore dual optimum =  $f(x)$  too.

* * *

4) The “compact representation” of  $f(x)\le \alpha$ 
-----------------------------------------------------

From (b),

$$
f(x) = \min\{rt+\mathbf 1^T u:\ t\mathbf 1+u\ge x,\ u\ge 0\}.
$$

Therefore:

### Claim

$$
f(x)\le \alpha \quad\Longleftrightarrow\quad \exists\, t\in\mathbb{R},\ u\in\mathbb{R}^n \text{ such that } \begin{cases} rt+\mathbf 1^T u \le \alpha,\\ t\mathbf 1+u \ge x,\\ u\ge 0. \end{cases}
$$

### Proof (both directions)

**( $\Rightarrow$ )** If  $f(x)\le \alpha$ :  
Let  $(t^\star,u^\star)$  be an optimal solution of the dual (exists because feasible set is closed and objective coercive enough here; in any case infimum is attained for LP). Then

$$
rt^\star+\mathbf 1^T u^\star = f(x)\le \alpha,
$$

and it satisfies constraints  $t^\star\mathbf 1+u^\star\ge x$ ,  $u^\star\ge 0$ . So existence holds.

**( $\Leftarrow$ )** If such  $t,u$  exist:  
By definition of  $f(x)$  as the minimum over all feasible  $(t,u)$ ,

$$
f(x)\le rt+\mathbf 1^T u \le \alpha.
$$

So  $f(x)\le \alpha$ . ∎

### Why this is “compact”

The original “subset inequality” form uses  $\binom nr$  inequalities:

$$
\sum_{i\in S} x_i \le \alpha \quad \forall S,\ |S|=r.
$$

The new form uses:

*    $n$  inequalities  $t+u_i\ge x_i$ ,
*    $n$  inequalities  $u_i\ge 0$ ,
*   1 inequality  $rt+\mathbf 1^T u \le \alpha$ .

Total:  $2n+1$  inequalities. That’s linear in  $n$ , not combinatorial.

### Extra deep intuition: what do  $t$  and  $u$  _mean_?

From constraints  $t\mathbf 1+u\ge x$  and  $u\ge 0$ , for each  $i$ :

$$
u_i \ge x_i - t,\quad u_i\ge 0 \quad\Rightarrow\quad u_i \ge \max(0, x_i - t).
$$

Given a fixed  $t$ , to minimize  $\mathbf 1^T u$ , you would choose the smallest feasible  $u$ , namely

$$
u_i(t)=\max(0, x_i - t).
$$

Plugging into the objective yields a 1D convex function:

$$
\psi(t)=rt+\sum_{i=1}^n \max(0, x_i - t).
$$

Then

$$
f(x)=\min_{t\in\mathbb{R}}\ \psi(t).
$$

The minimizing  $t$  acts like a **threshold**: components above  $t$  contribute  $x_i-t$  in the hinge terms, and the  $rt$  term compensates. At the optimum,  $t$  sits around the  $r$ \-th order statistic, which is why this recovers the “top  $r$ ” sum.

Edge cases:

*   If  $r=n$ : then  $f(x)=\sum_i x_i$ . In the dual, you can set  $u=0$  and pick  $t$  large enough so  $t\ge \max_i x_i$ ; minimizing  $nt$  pushes  $t$  down to  $\max_i x_i$ , but then hinge terms vanish; the structure still works and collapses to  $\sum_i x_i$ .
*   If  $r=1$ : then  $f(x)=\max_i x_i$ . The dual becomes  $\min_{t,u} t+\sum u_i$  with  $t+u_i\ge x_i$ ,  $u\ge 0$ ; minimizing yields the familiar epigraph form for max.

* * *

5) Part (c): Markowitz with diversification constraint as a QP
--------------------------------------------------------------

### 5.1 Base Markowitz problem

Variable  $x\in\mathbb{R}^n$ : portfolio weights.

Given:

*    $\Sigma\succeq 0$  covariance matrix,
*    $\bar p$  mean return vector,
*    $r_{\min}$  required return.

Problem:

$$
\begin{aligned} \min_x\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf 1^T x = 1,\\ & x\ge 0. \end{aligned} \tag{M}
$$

This is a convex QP (quadratic objective, linear constraints) because  $\Sigma\succeq 0$ .

### 5.2 Diversification constraint in the language of  $f(x)$ 

“Top 10% of assets” means take  $r=[0.1n]$  (some integer rounding convention). Define

$$
r := \lfloor 0.1n\rfloor \quad \text{(or whatever your text’s bracket means; the modeling is identical).}
$$

“No more than 80% in the top 10%” means:

$$
\sum_{i=1}^r x_{[i]} \le 0.8 \quad\Longleftrightarrow\quad f(x)\le 0.8.
$$

### 5.3 Replace  $f(x)\le 0.8$  by the compact linear constraints

From part (b),

$$
f(x)\le 0.8 \Longleftrightarrow \exists\, t\in\mathbb{R},\ u\in\mathbb{R}^n: \begin{cases} rt+\mathbf 1^T u \le 0.8,\\ t\mathbf 1 + u \ge x,\\ u\ge 0. \end{cases}
$$

### 5.4 Final QP (explicit, complete)

Decision variables:  $(x,u,t)\in\mathbb{R}^n\times\mathbb{R}^n\times\mathbb{R}$ .

$$
\boxed{ \begin{aligned} \min_{x,u,t}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf 1^T x = 1,\\ & x \ge 0,\\ & rt+\mathbf 1^T u \le 0.8,\\ & t\mathbf 1 + u \ge x,\\ & u \ge 0. \end{aligned}}
$$

### 5.5 Why this is a QP (and convex)

*   Objective depends only on  $x$ : quadratic form  $x^T\Sigma x$ . Since  $\Sigma\succeq 0$ , it is convex.
*   All constraints are linear in  $(x,u,t)$ .  
    Therefore the whole problem is a convex QP.

### 5.6 Practical modeling note (what solvers see)

Many QP solvers want the objective as  $\tfrac12 x^T Q x + c^T x$ . Here  $Q=2\Sigma$ ,  $c=0$ . Variables are  $(x,u,t)$ , but the quadratic term only touches the  $x$ \-block; the  $u,t$  blocks have zero quadratic coefficients.

* * *

6) What you should take away (the “why this matters” core)
----------------------------------------------------------

*   The ugly sorting operator “sum of top  $r$ ” is equivalent to a clean LP.
*   Duality turns “top  $r$ ” into a small number of linear constraints using auxiliary variables.
*   That turns a combinatorial-looking diversification rule into a solver-friendly QP constraint set.

If you want the deepest possible intuition: this is the same mathematical trick underlying CVaR/expected shortfall representations in risk management—order statistics become linear constraints after introducing a threshold  $t$  and slack variables  $u$ .

## Response:
Thought for 26s

Absolutely. I’ll go _even deeper_ and make every equivalence explicit, including the geometry behind the LP, the exact dual derivation with matrices, and the “why the compact constraints replace  $\binom{n}{r}$  constraints” argument in a way you could reproduce on an exam.

* * *

0) The object we’re modeling: “sum of the largest  $r$  components”
-------------------------------------------------------------------

Let  $x\in\mathbb{R}^n$ . Let  $x_{[1]}\ge x_{[2]}\ge \cdots \ge x_{[n]}$  be the components sorted in nonincreasing order (ties allowed; the sorted list is not unique under ties, but the multiset of values is, and the sum of the top  $r$  is unique).

Define

$$
f(x):=\sum_{i=1}^r x_{[i]}.
$$

So  $f(x)$  is an “order-statistic” functional: it depends on the ranking of the components.

* * *

1) A crucial identity:  $f(x)$  is a maximum over subsets of size  $r$ 
-----------------------------------------------------------------------

For any subset  $S\subseteq\{1,\dots,n\}$  with  $|S|=r$ , define

$$
\phi_S(x):=\sum_{i\in S} x_i.
$$

### Claim 1.1

$$
f(x)=\max_{S:\ |S|=r}\ \sum_{i\in S} x_i.
$$

### Proof (fully rigorous)

Let  $\pi$  be a permutation such that  $x_{\pi(1)}=x_{[1]},\dots,x_{\pi(n)}=x_{[n]}$ . Consider

$$
S^\star:=\{\pi(1),\dots,\pi(r)\}.
$$

Then

$$
\sum_{i\in S^\star} x_i=\sum_{k=1}^r x_{\pi(k)}=\sum_{k=1}^r x_{[k]}=f(x).
$$

Now take any other  $S$  with  $|S|=r$ . List its elements as  $i_1,\dots,i_r$  in decreasing order of their values:

$$
x_{i_1}\ge x_{i_2}\ge \cdots \ge x_{i_r}.
$$

Because  $x_{[k]}$  is the  $k$ \-th largest component _overall_, the  $k$ \-th largest value inside any subset of size  $r$  cannot exceed it:

$$
x_{i_k}\le x_{[k]} \quad \text{for each }k=1,\dots,r.
$$

Summing:

$$
\sum_{i\in S}x_i=\sum_{k=1}^r x_{i_k}\le \sum_{k=1}^r x_{[k]}=f(x).
$$

So no subset beats  $S^\star$ . Therefore the maximum over all size- $r$  subsets equals  $f(x)$ . ∎

This identity is the backbone of everything that follows.

* * *

2) Why  $f(x)\le \alpha$  equals  $\binom{n}{r}$  linear inequalities
---------------------------------------------------------------------

Using Claim 1.1:

$$
f(x)\le \alpha \quad\Longleftrightarrow\quad \max_{|S|=r}\sum_{i\in S} x_i \le \alpha \quad\Longleftrightarrow\quad \sum_{i\in S} x_i \le \alpha\ \ \forall S\text{ with }|S|=r.
$$

So the naive linear description is:

$$
\sum_{i\in S} x_i \le \alpha\quad \text{for all } S\subseteq\{1,\dots,n\},\ |S|=r.
$$

That’s  $\binom{n}{r}$  constraints: combinatorially huge.

The goal of the exercise is: replace those  $\binom{n}{r}$  inequalities by  $O(n)$  inequalities using auxiliary variables and LP duality.

* * *

3) Part (a): prove the LP representation of  $f(x)$ 
----------------------------------------------------

We must show:

$$
f(x)=\max\Big\{x^T y:\ 0\le y\le \mathbf{1},\ \mathbf{1}^T y=r\Big\}.
$$

Let the feasible set be

$$
\mathcal{Y}:=\{y\in\mathbb{R}^n:\ 0\le y_i\le 1,\ \sum_{i=1}^n y_i=r\}.
$$

There are two deep facts to show:

1.   $\mathcal{Y}$  is exactly the **convex hull** of all 0–1 vectors with exactly  $r$  ones (subset indicator vectors).
2.  A linear objective maximized over a convex hull achieves its maximum at one of the vertices (extreme points), i.e. at a 0–1 indicator, so it becomes “choose a subset of size  $r$ ”.

I’ll prove (1) rigorously via extreme points (and then (2) becomes immediate).

* * *

### Step 3.1: Extreme points of  $\mathcal{Y}$  are exactly subset indicators

Define the set of subset-indicator vectors:

$$
\mathcal{V}:=\{v\in\{0,1\}^n:\ \mathbf{1}^T v=r\}.
$$

#### Claim 3.1 (extreme point characterization)

$$
\mathrm{ext}(\mathcal{Y})=\mathcal{V}.
$$

#### Proof (fully detailed)

**(i) Every  $v\in\mathcal{V}$  is feasible.**  
If  $v_i\in\{0,1\}$  then  $0\le v_i\le 1$ , and  $\mathbf{1}^T v=r$  by definition. So  $v\in\mathcal{Y}$ .

**(ii) Any feasible  $y\in\mathcal{Y}$  with at least two fractional components is not extreme.**  
Assume  $y\in\mathcal{Y}$  and there exist distinct indices  $i\neq j$  with

$$
0<y_i<1,\qquad 0<y_j<1.
$$

Define  $d\in\mathbb{R}^n$  by  $d_i=1$ ,  $d_j=-1$ , and  $d_k=0$  otherwise. Note:

$$
\mathbf{1}^T d = 1 + (-1) = 0.
$$

Choose  $\varepsilon>0$  such that simultaneously:

$$
y_i+\varepsilon\le 1,\quad y_i-\varepsilon\ge 0,\quad y_j+\varepsilon\le 1,\quad y_j-\varepsilon\ge 0.
$$

This is possible because  $y_i,y_j$  are strictly between 0 and 1.

Now define

$$
y^{+}:=y+\varepsilon d,\qquad y^{-}:=y-\varepsilon d.
$$

Then:

*   Bounds:  $0\le y^\pm\le \mathbf{1}$  by the choice of  $\varepsilon$ .
*   Sum constraint:
    
$$
\mathbf{1}^T y^\pm=\mathbf{1}^T y \pm \varepsilon\,\mathbf{1}^T d = r \pm \varepsilon\cdot 0=r.
$$

So  $y^+,y^-\in\mathcal{Y}$ . Also  $y^+\neq y^-$  (they differ in coordinates  $i,j$ ). And

$$
y=\tfrac12 y^+ + \tfrac12 y^-,
$$

a nontrivial convex combination. Therefore  $y$  is **not** an extreme point.

**(iii) Therefore, any extreme point has at most one fractional component.**

**(iv) But it cannot have exactly one fractional component because  $\sum y_i=r$  is an integer.**  
If exactly one coordinate  $y_k$  were fractional and all others were 0 or 1, then  $\sum_i y_i$  would be “integer + fractional”, hence not an integer, contradicting  $\sum_i y_i=r\in\mathbb{Z}$ .

So an extreme point has **no** fractional components: every coordinate is 0 or 1. Together with  $\mathbf{1}^T y=r$ , that means exactly  $r$  ones.

Thus  $\mathrm{ext}(\mathcal{Y})=\mathcal{V}$ . ∎

* * *

### Step 3.2: Maximizing  $x^T y$  over  $\mathcal{Y}$  reduces to choosing a subset

Standard LP/convex fact (you should know it, but here is the exact logic):

If  $P$  is a polytope and you maximize a linear function over  $P$ , an optimum exists and can be chosen at an extreme point of  $P$ . (Because if an optimum were not extreme, it is a convex combination of two distinct feasible points; at least one of those points attains at least the same objective value.)

Thus:

$$
\max_{y\in\mathcal{Y}} x^T y = \max_{y\in \mathrm{ext}(\mathcal{Y})} x^T y = \max_{v\in\mathcal{V}} x^T v.
$$

But if  $v\in\mathcal{V}$  is 0–1 with exactly  $r$  ones, it corresponds to a subset  $S$  of size  $r$ , and

$$
x^T v = \sum_{i=1}^n x_i v_i = \sum_{i:\ v_i=1} x_i = \sum_{i\in S} x_i.
$$

So

$$
\max_{v\in\mathcal{V}} x^T v = \max_{S:\ |S|=r} \sum_{i\in S} x_i = f(x)
$$

by Claim 1.1.

This proves part (a). ✅

(And notice what happened: the LP feasible region  $\mathcal{Y}$  is the convex hull of subset indicators, so the LP is a “convexified” subset-choice problem, but it stays exact because the extreme points are integral.)

* * *

4) Part (b): derive the dual carefully and get the compact constraint form
--------------------------------------------------------------------------

We start with the primal from (a):

$$
\begin{aligned} \max_{y\in\mathbb{R}^n}\quad & x^T y\\ \text{s.t.}\quad & 0\le y\le \mathbf{1},\\ & \mathbf{1}^T y=r. \end{aligned} \tag{P}
$$

I’ll derive the dual in a way that makes every sign and dimension transparent.

* * *

### Step 4.1: Put the primal into a standard “max with  $\le$  constraints + equality” form

Constraints:

*    $y\le \mathbf{1}$  (upper bounds)
*    $-y\le 0$  (lower bounds)
*    $\mathbf{1}^T y = r$  (equality)

So:

$$
\begin{aligned} \max\quad & x^T y\\ \text{s.t.}\quad & y-\mathbf{1}\le 0\\ & -y \le 0\\ & \mathbf{1}^T y - r = 0. \end{aligned}
$$

* * *

### Step 4.2: Lagrangian with correct multiplier sign conventions for a max problem

For a **maximization** primal with constraints  $g(y)\le 0$  and  $h(y)=0$ , a convenient convention is:

$$
L(y,u,v,t)= x^T y - u^T(y-\mathbf{1}) - v^T(-y) - t(\mathbf{1}^T y - r),
$$

with  $u\ge 0$ ,  $v\ge 0$ , and  $t\in\mathbb{R}$  free.

Why these minus signs? Because we want  $L(y,u,v,t)$  to be an **upper bound** on the primal objective over feasible  $y$ . For feasible  $y$ :

*    $y-\mathbf{1}\le 0$  and  $u\ge 0$  imply  $-u^T(y-\mathbf{1})\ge 0$ ,
*    $-y\le 0$  and  $v\ge 0$  imply  $-v^T(-y)=v^T y\ge 0$ ,
*   equality term is zero.

So  $L(y,u,v,t)\ge x^T y$  for feasible  $y$ . Then minimizing the upper bound gives the best bound, which is exactly the dual.

Compute  $L$ :

$$
\begin{aligned} L(y,u,v,t) &= x^T y - u^T y + u^T\mathbf{1} + v^T y - t\mathbf{1}^T y + tr\\ &= (x - u + v - t\mathbf{1})^T y + \mathbf{1}^T u + tr. \end{aligned}
$$

* * *

### Step 4.3: Dual function (sup over  $y$ )

Dual function is

$$
g(u,v,t)=\sup_{y\in\mathbb{R}^n} L(y,u,v,t).
$$

Now:  $\sup_{y} a^T y$  is  $+\infty$  unless  $a=0$ . So for the supremum to be finite, we must have the coefficient of  $y$  equal to zero:

$$
x - u + v - t\mathbf{1} = 0 \quad\Longleftrightarrow\quad u - v + t\mathbf{1} = x. \tag{*}
$$

Under this condition, the  $y$ \-term disappears, and

$$
g(u,v,t)=\mathbf{1}^T u + tr.
$$

* * *

### Step 4.4: The dual optimization problem

We minimize this bound subject to feasibility:

$$
\begin{aligned} \min_{u,v,t}\quad & \mathbf{1}^T u + tr\\ \text{s.t.}\quad & u - v + t\mathbf{1} = x\\ & u\ge 0,\ v\ge 0,\ t\in\mathbb{R}. \end{aligned} \tag{D-raw}
$$

Now eliminate  $v$ . From  $(*)$ ,

$$
v = u + t\mathbf{1} - x.
$$

Constraint  $v\ge 0$  becomes

$$
u + t\mathbf{1} - x \ge 0 \quad\Longleftrightarrow\quad t\mathbf{1} + u \ge x.
$$

So we can drop  $v$  and get exactly:

$$
\boxed{ \begin{aligned} \min_{t\in\mathbb{R},\ u\in\mathbb{R}^n}\quad & rt + \mathbf{1}^T u\\ \text{s.t.}\quad & t\mathbf{1} + u \ge x\\ & u\ge 0. \end{aligned}} \tag{D}
$$

That is the dual shown in the text. ✅

* * *

### Step 4.5: Strong duality (why the optimal values match)

This is an LP. Sufficient conditions for strong duality: primal feasible and bounded (or existence of an interior point; here feasibility and boundedness are enough).

*   Feasible: choose  $y$  with exactly  $r$  ones and the rest zeros.
*   Bounded: because  $0\le y\le 1$ , we have  $x^T y \le \sum_i \max(x_i,0)$ , finite.

Hence the primal optimum equals the dual optimum.

Combine with part (a): primal optimum is  $f(x)$ . Therefore:

$$
f(x)=\min\{rt+\mathbf{1}^T u:\ t\mathbf{1}+u\ge x,\ u\ge 0\}.
$$

* * *

5) Turn  $f(x)\le \alpha$  into  $2n+1$  linear inequalities
------------------------------------------------------------

We now have:

$$
f(x)=\min_{t,u}\ \big(rt+\mathbf{1}^T u\big) \quad \text{s.t.}\quad t\mathbf{1}+u\ge x,\ u\ge 0.
$$

### Claim 5.1 (exact equivalence)

$$
f(x)\le \alpha \quad\Longleftrightarrow\quad \exists\, t\in\mathbb{R},\ u\in\mathbb{R}^n\ \text{s.t. } \begin{cases} rt+\mathbf{1}^T u \le \alpha,\\ t\mathbf{1}+u\ge x,\\ u\ge 0. \end{cases}
$$

### Proof (both directions, no gaps)

**( $\Leftarrow$ )** Suppose such  $t,u$  exist. Then  $(t,u)$  is feasible for the minimization defining  $f(x)$ . Since  $f(x)$  is the minimum objective value over all feasible pairs,

$$
f(x)\le rt+\mathbf{1}^T u \le \alpha.
$$

**( $\Rightarrow$ )** Suppose  $f(x)\le \alpha$ . Let  $(t^\star,u^\star)$  be an optimal solution of the dual LP (an optimum exists because the feasible region is closed and the LP is bounded below when feasible). Then

$$
rt^\star+\mathbf{1}^T u^\star = f(x)\le \alpha
$$

and constraints hold. So existence is proved. ∎

This gives exactly  $n$  inequalities from  $t+u_i\ge x_i$ , plus  $n$  inequalities  $u_i\ge 0$ , plus 1 inequality  $rt+\sum u_i\le \alpha$ : total  $2n+1$ .

* * *

6) Deeper insight: you can eliminate  $u$  and get a 1D “threshold” formula
---------------------------------------------------------------------------

From constraints  $t\mathbf{1}+u\ge x$ ,  $u\ge 0$ , the smallest feasible  $u$  for a fixed  $t$  is componentwise:

$$
u_i = \max(0, x_i - t).
$$

Reason: you need  $u_i\ge x_i-t$  and  $u_i\ge 0$ , so  $u_i\ge \max(0,x_i-t)$ , and choosing equality minimizes  $\sum u_i$ .

Plugging this into the dual objective gives the equivalent 1D convex minimization:

$$
f(x)=\min_{t\in\mathbb{R}} \left[ rt + \sum_{i=1}^n \max(0, x_i - t)\right].
$$

This shows  $t$  is literally a “cutoff” level: only components above  $t$  contribute via the hinge  $(x_i-t)_+$ .

You can even see where the minimizer sits: if  $x_{[r]}>x_{[r+1]}$  (strict gap), an optimal  $t^\star$  lies in  $[x_{[r+1]},x_{[r]}]$ , and the formula reproduces exactly  $\sum_{i=1}^r x_{[i]}$ . (With ties, the minimizing interval widens, but the value stays the same.)

This is the same structural trick behind CVaR/expected shortfall representations in risk optimization.

* * *

7) Part (c): Markowitz portfolio + diversification constraint as a QP
---------------------------------------------------------------------

### 7.1 Base Markowitz problem

Decision variable  $x\in\mathbb{R}^n$  (portfolio weights).

Given:

*    $\bar p\in\mathbb{R}^n$  expected returns,
*    $\Sigma\in\mathbb{S}^n_+$  covariance matrix (PSD),
*    $r_{\min}\in\mathbb{R}$  required return.

Problem:

$$
\begin{aligned} \min_{x}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf{1}^T x = 1,\\ & x\ge 0. \end{aligned}
$$

This is a convex QP because the objective is a PSD quadratic form and constraints are linear.

### 7.2 Diversification constraint is  $f(x)\le 0.8$  with  $r=[0.1n]$ 

Let

$$
r := [0.1n]
$$

(where  $[\,\cdot\,]$  is whatever integer rounding your text uses; common choices are  $\lfloor\cdot\rfloor$  or nearest integer—either way it’s an integer in  $\{1,\dots,n\}$ ).

Constraint:

$$
\sum_{i=1}^{r} x_{[i]} \le 0.8 \quad\Longleftrightarrow\quad f(x)\le 0.8.
$$

### 7.3 Use the compact representation from (b)

Introduce auxiliary variables:

*    $t\in\mathbb{R}$ ,
*    $u\in\mathbb{R}^n$ .

Replace  $f(x)\le 0.8$  by:

$$
rt+\mathbf{1}^T u \le 0.8,\qquad t\mathbf{1}+u\ge x,\qquad u\ge 0.
$$

### 7.4 Final QP (fully explicit)

Decision variables are  $(x,u,t)\in\mathbb{R}^n\times\mathbb{R}^n\times\mathbb{R}$ :

$$
\boxed{ \begin{aligned} \min_{x,u,t}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min},\\ & \mathbf{1}^T x = 1,\\ & x \ge 0,\\ & rt+\mathbf{1}^T u \le 0.8,\\ & t\mathbf{1}+u \ge x,\\ & u \ge 0. \end{aligned}}
$$

Everything is linear except the quadratic objective, so it is indeed a QP.

### 7.5 If you want the “canonical QP matrix form”

Let  $z:=\begin{bmatrix}x\\ u\\ t\end{bmatrix}\in\mathbb{R}^{2n+1}$ . Then the objective is

$$
\min\ \frac12 z^T Q z + c^T z
$$

with

$$
Q= \begin{bmatrix} 2\Sigma & 0 & 0\\ 0&0&0\\ 0&0&0 \end{bmatrix}, \qquad c=0.
$$

And the constraints are linear inequalities/equalities in  $z$ .

* * *

8) Why this is _exactly_ the compact replacement of  $\binom{n}{r}$  constraints
--------------------------------------------------------------------------------

The “exploded” constraint set is:

$$
\sum_{i\in S} x_i \le 0.8\quad \forall S,\ |S|=r.
$$

That is an intersection of  $\binom{n}{r}$  halfspaces in  $x$ \-space.

The compact set is the projection of a polyhedron in  $(x,u,t)$ \-space:

$$
\{x:\exists (u,t)\text{ s.t. } rt+\mathbf{1}^T u \le 0.8,\ t\mathbf{1}+u\ge x,\ u\ge 0\}.
$$

Duality guarantees these sets are identical because both describe the epigraph/level set of the same convex function  $f$ .

This is the general convex-optimization theme: “combinatorial max of linear functions” ↔ “LP” ↔ “small extended formulation.”

* * *

If you want _even more depth_ beyond this (like deriving the KKT/complementary slackness conditions and showing explicitly how  $t^\star$  pins to the  $r$ \-th order statistic and how  $u^\star$  becomes  $(x-t^\star)_+$ ), I can write that too. That’s the “microscope view” that makes the dual variables feel inevitable rather than magical.

## Response:
Thought for 35s

Next layer: let’s open the machine and look at the **optimality conditions** (KKT / complementary slackness) and the “threshold” structure that makes the dual variables  $(t,u)$  feel inevitable instead of magical.

I’ll do four things:

1.  Write the primal–dual pair cleanly in one place.
2.  Derive the full KKT system (including the “missing” dual variable for the lower bound  $y\ge 0$ ).
3.  Prove the **threshold rule**: optimal  $y$  is  $1$  on entries above a cutoff  $t^\star$ ,  $0$  below, and possibly fractional on ties at the cutoff; this is exactly “pick the top  $r$ ”.
4.  Eliminate  $u$  explicitly to get the 1-dimensional hinge formula and solve it via subgradients to locate  $t^\star$  between  $x_{[r]}$  and  $x_{[r+1]}$ .

* * *

1) Primal–dual pair (full, with all variables)
----------------------------------------------

### Primal (from part a)

$$
\begin{aligned} \text{(P)}\qquad \max_{y\in\mathbb{R}^n}\quad & x^T y\\ \text{s.t.}\quad & y \le \mathbf{1},\\ & y \ge 0,\\ & \mathbf{1}^T y = r. \end{aligned}
$$

### Dual (the compact form in the book, from part b)

$$
\begin{aligned} \text{(D)}\qquad \min_{t\in\mathbb{R},\ u\in\mathbb{R}^n}\quad & rt + \mathbf{1}^T u\\ \text{s.t.}\quad & t\mathbf{1} + u \ge x,\\ & u \ge 0. \end{aligned}
$$

Important: the compact dual hides one extra dual vector that comes from the constraint  $y\ge 0$ . If we derive the dual _before eliminating variables_, we see it explicitly.

* * *

2) Derive KKT conditions (including the “hidden” vector)
--------------------------------------------------------

Write (P) constraints as

*    $y-\mathbf{1}\le 0$  (upper bound),
*    $-y\le 0$  (lower bound),
*    $\mathbf{1}^T y - r = 0$  (equality).

Introduce multipliers:

*    $u\in\mathbb{R}^n_+$  for  $y-\mathbf{1}\le 0$ ,
*    $v\in\mathbb{R}^n_+$  for  $-y\le 0$ ,
*    $t\in\mathbb{R}$  for  $\mathbf{1}^T y - r = 0$ .

Using the “maximization” Lagrangian convention:

$$
L(y,u,v,t)=x^T y - u^T(y-\mathbf{1}) - v^T(-y) - t(\mathbf{1}^T y-r).
$$

Expand:

$$
L = (x - u + v - t\mathbf{1})^T y + \mathbf{1}^T u + rt.
$$

### KKT system

At optimality (and strong duality holds for LPs here), we have:

**(i) Primal feasibility**

$$
0\le y \le \mathbf{1},\qquad \mathbf{1}^T y = r.
$$

**(ii) Dual feasibility**

$$
u\ge 0,\qquad v\ge 0.
$$

**(iii) Stationarity (gradient w.r.t.  $y$  must vanish)**  
Since  $L$  is linear in  $y$ , “stationarity” means the coefficient of  $y$  must be zero:

$$
x - u + v - t\mathbf{1} = 0 \quad\Longleftrightarrow\quad u - v + t\mathbf{1} = x. \tag{S}
$$

**(iv) Complementary slackness** (componentwise)

$$
u_i (y_i-1)=0,\qquad v_i(-y_i)=0 \iff v_i y_i=0\quad \text{for each }i. \tag{CS}
$$

These four blocks completely characterize optimal primal/dual solutions.

Now watch what these conditions _force_  $y$  to look like.

* * *

3) The threshold structure (this is the heart)
----------------------------------------------

From stationarity (S),

$$
u_i - v_i + t = x_i.
$$

Rearrange:

$$
x_i - t = u_i - v_i. \tag{T}
$$

Remember:

*    $u_i\ge 0$ ,  $v_i\ge 0$ .
*   Complementary slackness ties  $u_i$  to whether  $y_i$  hits the **upper bound**  $1$ , and ties  $v_i$  to whether  $y_i$  hits the **lower bound**  $0$ .

Let’s do a full case split on  $x_i$  relative to  $t$ .

### Case A:  $x_i > t$ 

Then  $x_i - t > 0$ . From (T),  $u_i - v_i > 0$ . Since  $u_i,v_i\ge 0$ , the only way the difference is positive is:

$$
u_i > v_i.
$$

In particular  $u_i>0$ . Then complementary slackness  $u_i(y_i-1)=0$  forces

$$
y_i = 1.
$$

So: **if  $x_i>t$ , the coordinate must be fully selected:  $y_i=1$ .**

Also, because  $u_i-v_i=x_i-t>0$  and  $v_i\ge 0$ , the minimum consistent choice is often  $v_i=0,\ u_i=x_i-t$ , but we don’t even need that yet.

### Case B:  $x_i < t$ 

Then  $x_i - t < 0$ . From (T),  $u_i - v_i < 0$ , so necessarily

$$
v_i > u_i,
$$

in particular  $v_i>0$ . Complementary slackness  $v_i y_i=0$  forces

$$
y_i = 0.
$$

So: **if  $x_i<t$ , the coordinate must be unselected:  $y_i=0$ .**

### Case C:  $x_i = t$ 

Then  $x_i - t = 0$ . From (T),  $u_i=v_i$ . This can happen in many ways:

*    $u_i=v_i=0$ , or
*    $u_i=v_i>0$ .

Complementary slackness does not force  $y_i$  to be 0 or 1 in this case; it only says:

*   if  $u_i>0$  then  $y_i=1$ ,
*   if  $v_i>0$  then  $y_i=0$ ,
*   but if both are zero,  $y_i$  can be strictly between 0 and 1.

So: **if  $x_i=t$ ,  $y_i$  can be fractional (this is where ties are handled).**

### Conclusion: the structure forced by KKT

There exists a scalar  $t^\star$  such that:

*   if  $x_i > t^\star$ , then  $y_i^\star=1$ ,
*   if  $x_i < t^\star$ , then  $y_i^\star=0$ ,
*   if  $x_i = t^\star$ , then  $y_i^\star\in[0,1]$  is allowed.

Then the equality constraint  $\sum_i y_i=r$  determines how much mass is placed on the tie set  $\{i: x_i=t^\star\}$ .

That is _exactly_ “pick the top  $r$ ” with possible fractional splitting among equal values at the cutoff.

This is the deepest reason the LP in (a) returns  $f(x)$ : its KKT system literally encodes “threshold + fill to total mass  $r$ ”.

* * *

4) How to locate  $t^\star$  precisely: the hinge formula and subgradients
--------------------------------------------------------------------------

Now connect this to the compact dual (D). In (D),

$$
t\mathbf{1}+u\ge x,\quad u\ge 0.
$$

Componentwise that means:

$$
u_i \ge x_i - t,\qquad u_i\ge 0 \quad\Rightarrow\quad u_i \ge \max(0, x_i - t).
$$

Given a fixed  $t$ , the dual objective  $rt+\mathbf{1}^T u$  is minimized by choosing the smallest feasible  $u$ , i.e.

$$
u_i(t)=\max(0, x_i - t).
$$

Plugging back yields the 1D problem

$$
f(x)=\min_{t\in\mathbb{R}}\ \psi(t), \qquad \psi(t):= rt + \sum_{i=1}^n (x_i - t)_+,
$$

where  $(a)_+:=\max(0,a)$ .

### 4.1  $\psi(t)$  is convex and piecewise linear

Each function  $(x_i-t)_+$  is convex in  $t$  (it is the max of two affine functions:  $0$  and  $x_i-t$ ). A nonnegative sum of convex functions plus  $rt$  is convex. Because it’s max-of-affine, it’s piecewise linear.

So the minimizer  $t^\star$  is characterized by the subgradient condition:

$$
0\in \partial \psi(t^\star).
$$

### 4.2 Compute the subgradient  $\partial \psi(t)$  exactly

For a single term  $g_i(t)=(x_i-t)_+$ :

*   If  $t<x_i$ , then  $g_i(t)=x_i-t$  so derivative is  $-1$ .
*   If  $t>x_i$ , then  $g_i(t)=0$  so derivative is  $0$ .
*   If  $t=x_i$ , it’s nondifferentiable, and the subgradient is the interval  $[-1,0]$ .

So:

$$
\partial g_i(t)= \begin{cases} \{-1\}, & t<x_i,\\ [-1,0], & t=x_i,\\ \{0\}, & t>x_i. \end{cases}
$$

Therefore

$$
\partial \psi(t) = r + \sum_{i=1}^n \partial g_i(t).
$$

Define:

*    $m(t):=\#\{i: x_i>t\}$  (strictly above  $t$ ),
*    $k(t):=\#\{i: x_i=t\}$  (equal to  $t$ ).

Then:

*   for indices with  $x_i>t$ , contribute  $-1$ ,
*   for indices with  $x_i<t$ , contribute  $0$ ,
*   for indices with  $x_i=t$ , contribute an element of  $[-1,0]$ .

So the subgradient set is:

$$
\partial \psi(t)= r - m(t) + [-k(t),0].
$$

Equivalently:

$$
\partial \psi(t)= [\,r - m(t) - k(t),\ \ r - m(t)\,].
$$

### 4.3 Optimality condition  $0\in \partial\psi(t^\star)$ 

This means

$$
r - m(t^\star) - k(t^\star) \le 0 \le r - m(t^\star).
$$

Rearrange:

$$
m(t^\star)\ \le\ r\ \le\ m(t^\star)+k(t^\star). \tag{OC}
$$

Interpretation: at the threshold  $t^\star$ ,

*   there are  $m(t^\star)$  entries strictly above  $t^\star$ , and they _must_ be fully selected ( $y_i=1$ ),
*   there are  $k(t^\star)$  entries exactly at  $t^\star$ , and you choose just enough of them (possibly fractionally) so the total selected mass becomes  $r$ .

This is the exact analytic version of the KKT “threshold” logic from Section 3.

### 4.4 Where is  $t^\star$  relative to the order statistics?

Let  $x_{[1]}\ge \cdots \ge x_{[n]}$ . Consider any  $t$  strictly between  $x_{[r]}$  and  $x_{[r+1]}$  (assuming  $r<n$  and strict inequality). Then:

*   exactly  $r$  components exceed  $t$ , so  $m(t)=r$ ,
*   and no components equal  $t$ , so  $k(t)=0$ .

Then (OC) holds:  $m=r\le r\le r$ . So any such  $t$  is optimal. That’s why the minimizer might not be unique, but the value  $f(x)$  is.

If there are ties around the  $r$ \-th place,  $t^\star$  lands on that tied value, and the fractional selection happens inside the tie set.

This is also why your LP optimum can have multiple optimal  $y$ ’s when ties occur: any way of distributing mass within equal entries is optimal.

* * *

5) Complementary slackness gives the exact primal optimizer  $y^\star$ 
-----------------------------------------------------------------------

Let  $t^\star$  be any minimizer of  $\psi(t)$ . Define:

*    $A=\{i: x_i>t^\star\}$ ,
*    $B=\{i: x_i=t^\star\}$ ,
*    $C=\{i: x_i<t^\star\}$ .

Then the KKT/OC condition implies  $|A|\le r \le |A|+|B|$ .

A valid optimal  $y^\star$  is:

*    $y_i^\star=1$  for  $i\in A$ ,
*    $y_i^\star=0$  for  $i\in C$ ,
*   choose  $y_i^\star\in[0,1]$  on  $B$  such that  $\sum_{i\in B} y_i^\star = r-|A|$ .

This always exists because  $0\le r-|A|\le |B|$ .

Then the primal value is

$$
x^T y^\star = \sum_{i\in A} x_i + \sum_{i\in B} x_i y_i^\star = \sum_{i\in A} x_i + t^\star\sum_{i\in B} y_i^\star = \sum_{i\in A} x_i + t^\star(r-|A|),
$$

which equals  $\sum_{i=1}^r x_{[i]}$  (check by matching the number of fully-selected strictly-larger entries plus the needed amount at the tied level).

That’s the “microscope proof” that the LP returns the sum of the  $r$  largest components.

* * *

6) Part (c) revisited: subtle feasibility/meaning checks (often skipped)
------------------------------------------------------------------------

In Markowitz, you already have:

$$
x\ge 0,\qquad \mathbf{1}^T x = 1.
$$

So  $x$  lies in the simplex.

The diversification constraint  $f(x)\le 0.8$  with  $r\approx 0.1n$  has a useful interpretation in simplex geometry:

*    $f(x)$  is the maximum mass you can concentrate on any subset of  $r$  assets (because it sums the top  $r$  weights).
*   So  $f(x)\le 0.8$  says: _even the heaviest 10% of assets cannot collectively exceed 80% of the portfolio._

Feasibility sanity check: for any simplex point, the sum of the largest  $r$  entries is at least  $r/n$  (uniform weights achieves equality). Here  $r/n\approx 0.1$ , which is  $\ll 0.8$ , so this constraint is nonempty and not “too tight”. It’s a meaningful diversification rule, not a contradiction.

The final QP you already have remains exactly correct:

$$
\begin{aligned} \min_{x,u,t}\quad & x^T\Sigma x\\ \text{s.t.}\quad & \bar p^T x \ge r_{\min},\ \ \mathbf{1}^T x = 1,\ \ x\ge 0,\\ & rt+\mathbf{1}^T u \le 0.8,\ \ t\mathbf{1}+u\ge x,\ \ u\ge 0. \end{aligned}
$$

* * *

7) What “Next” could mean from here (continuation without fluff)
----------------------------------------------------------------

If you keep going deeper, the natural next pieces are:

*   the **subdifferential of  $f(x)$ **: show  $\partial f(x)$  is exactly the set of optimal  $y$ ’s in (a), which are “ $0/1$  on strict ranks and fractional on ties”; this links directly to sensitivity analysis and to how solvers generate cutting planes,
*   an **extended formulation** viewpoint:  $f(x)$  is the support function of the “uniform matroid base polytope” (that’s the fancy geometry name for  $\mathcal{Y}$ ),
*   implementation details: how to encode it in CVX/CVXPY and what numerical scaling issues to watch for in portfolio QPs.

Tell your brain it’s allowed to enjoy this: what looked like “sorting” got converted into linear inequalities via duality and convex geometry. That’s the whole Boyd & Vandenberghe vibe.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)