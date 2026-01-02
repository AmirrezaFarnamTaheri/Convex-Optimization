# Primal Dual Optimization Walkthrough

**User:** Anonymous (meqrvsl88948@hotmail.com)  
**Created:** 12/28/2025 2:01:34  
**Updated:** 12/28/2025 2:04:41  
**Exported:** 12/29/2025 0:12:00  
**Link:** [https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505e44-7dcc-8330-9d72-4b20879596d7](https://chatgpt.com/g/g-p-694aced048448191ad02c68b2c4055b0-new-unpacked/c/69505e44-7dcc-8330-9d72-4b20879596d7)  

## Response:
You already did the “skeleton derivation.” What you’re asking for now is the stuff that makes it _feel inevitable_: why those PSD/range conditions are exactly the “no  $-\infty$ ” conditions, why the pseudoinverse formula is not a magic trick, and (big one) why the dual becomes _exact_ even when the primal is nonconvex.

I’ll rebuild the whole trust-region story as a newcomer walkthrough, but with the emphasis on the parts that are usually waved away.

* * *

0) The object we are studying (trust-region subproblem)
-------------------------------------------------------

Primal (original) problem:

$$
\begin{aligned} \min_{x\in\mathbb R^n}\quad & f(x):=x^T A x +2b^T x\\ \text{s.t.}\quad & x^T x \le 1. \end{aligned} \tag{P}
$$

Here  $A\in\mathbb S^n$  (symmetric) and  $b\in\mathbb R^n$ .

### 0.1 Why the optimum exists (so  $p^\star$  is a real number, not “inf of nothing”)

*   Feasible set is the closed unit ball  $\{x:\|x\|_2\le 1\}$ , which is **compact** (closed + bounded in  $\mathbb R^n$ ).
*    $f(x)$  is a continuous polynomial.
*   Continuous function on a compact set attains a minimum.

So here  $\inf$  is actually a  $\min$ . (Using  $\inf$  is still the clean general definition.)

* * *

1) Primal vs dual: what are we _trying to manufacture_?
-------------------------------------------------------

*   Primal optimal value:
    $$
    p^\star := \min_{\|x\|\le 1} f(x).
    $$
*   Dual idea: produce numbers  $L$  that you can **prove** satisfy  $L\le p^\star$ . Any such  $L$  is a **certificate lower bound** on the best possible primal value.

Duality is basically: “Here’s a systematic machine that outputs lower bounds; then we tune the machine to output the largest possible lower bound.”

* * *

2) Lagrangian: the “lower-bound machine”
----------------------------------------

Constraint can be written as one inequality:

$$
g(x):=x^Tx-1 \le 0.
$$

Choose a multiplier  $\lambda\ge 0$ . Define the Lagrangian

$$
L(x,\lambda) := f(x) + \lambda g(x) = x^TAx+2b^Tx+\lambda(x^Tx-1).
$$

Group terms:

$$
L(x,\lambda)=x^T(A+\lambda I)x + 2b^Tx - \lambda. \tag{L}
$$

### 2.1 The one-line reason  $\lambda\ge 0$  is forced

If  $x$  is feasible, then  $g(x)\le 0$ . Multiplying by  $\lambda\ge 0$  preserves the sign:  $\lambda g(x)\le 0$ . Therefore for feasible  $x$ ,

$$
L(x,\lambda)=f(x)+\lambda g(x)\le f(x).
$$

That inequality is the entire engine.

* * *

3) Dual function  $g(\lambda)$ : why it is _always_ a lower bound
-----------------------------------------------------------------

Dual function is

$$
g(\lambda):=\inf_{x\in\mathbb R^n} L(x,\lambda).
$$

Important: inf over **all**  $x$ , not just feasible  $x$ .

Take any feasible  $x$ . We had  $L(x,\lambda)\le f(x)$ . Since  $g(\lambda)$  is the infimum over all  $x$ ,

$$
g(\lambda)\le L(x,\lambda)\le f(x).
$$

Now take the minimum over feasible  $x$  on the far right:

$$
g(\lambda)\le \min_{\|x\|\le 1} f(x)=p^\star.
$$

So **every**  $\lambda\ge 0$  gives a certified lower bound  $g(\lambda)\le p^\star$ . This is weak duality.

* * *

4) Dual problem: “best lower bound”
-----------------------------------

$$
d^\star:=\sup_{\lambda\ge 0} g(\lambda), \qquad \text{dual is}\quad \max_{\lambda\ge 0} g(\lambda). \tag{D}
$$

Weak duality always says  $d^\star\le p^\star$ . The miracle here is: for this trust-region problem, actually  $d^\star=p^\star$  (strong duality), even if  $A$  is indefinite.

But first we must compute  $g(\lambda)$ .

* * *

5) Computing  $g(\lambda)=\inf_x L(x,\lambda)$ : the real meat
--------------------------------------------------------------

Write

$$
L(x,\lambda)= x^T M x + 2b^T x - \lambda, \qquad M:=A+\lambda I.
$$

So

$$
g(\lambda)=\Big(\inf_x \big[x^T M x +2b^Tx\big]\Big)-\lambda. \tag{*}
$$

Everything reduces to understanding the unconstrained quadratic

$$
q(x):=x^T M x +2b^Tx.
$$

This splits into three fundamental cases.

* * *

### Case 1:  $M$  is not PSD  $\Rightarrow$  the infimum is  $-\infty$ 

“ $M\succeq 0$ ” means  $x^TMx\ge 0$  for all  $x$ . If not, then there exists some direction  $v\neq 0$  with  $v^TMv<0$ .

Test along the ray  $x=t v$ :

$$
q(tv)=t^2(v^TMv) +2t(b^Tv).
$$

As  $t\to+\infty$ , the  $t^2(v^TMv)$  term dominates and goes to  $-\infty$  because  $v^TMv<0$ . Therefore

$$
\inf_x q(x)=-\infty.
$$

So for the dual function to be finite we must have

$$
A+\lambda I \succeq 0. \tag{C1}
$$

This is not a “random constraint”; it is literally “otherwise the Lagrangian is a downhill canyon and the infimum is  $-\infty$ .”

* * *

### Case 2:  $M\succeq 0$  but singular: why the **range condition** appears

Assume  $M\succeq 0$  and singular. Then it has a nontrivial nullspace:

$$
\ker(M)=\{v: Mv=0\}\neq\{0\}.
$$

Pick  $v\in\ker(M)$ ,  $v\neq 0$ . Along the line  $x=x_0+tv$ ,

*   quadratic term:
    $$
    (x_0+tv)^TM(x_0+tv)=x_0^TMx_0 + 2t\,v^TMx_0 + t^2 v^TMv.
    $$
    But  $Mv=0\Rightarrow v^TM=0$  and  $v^TMv=0$ . So the whole dependence on  $t$  vanishes:
    $$
    (x_0+tv)^TM(x_0+tv)=x_0^TMx_0.
    $$
*   linear term:
    $$
    2b^T(x_0+tv)=2b^Tx_0 +2t(b^Tv).
    $$

So along a nullspace direction, the quadratic part gives **no growth** in either direction; only the linear term changes.

If there exists  $v\in\ker(M)$  with  $b^Tv\neq 0$ , then sending  $t\to -\infty$  (or  $+\infty$ ) makes  $2t(b^Tv)\to -\infty$ . Therefore  $q(x)$  is unbounded below:

$$
\inf_x q(x)=-\infty \quad \text{if } \exists v\in\ker(M): b^Tv\neq 0.
$$

So to avoid  $-\infty$ , we need

$$
b^Tv=0 \quad \forall v\in\ker(M). \tag{C2a}
$$

Now the linear algebra translation:

For symmetric  $M$ , a standard fact is

$$
\mathcal R(M) = \ker(M)^\perp,
$$

where  $\mathcal R(M)$  is the column space (range). So “ $b$  is orthogonal to  $\ker(M)$ ” is equivalent to “ $b\in \mathcal R(M)$ .”

Thus the finiteness condition is exactly

$$
b\in \mathcal R(A+\lambda I). \tag{C2}
$$

That’s the “range condition.”

* * *

### Case 3:  $M\succeq 0$  and  $b\in\mathcal R(M)$ : now the infimum is finite and computable

Now we can actually compute

$$
\inf_x \big(x^TMx+2b^Tx\big).
$$

#### 3.1 Why the stationarity equation is  $Mx=-b$ 

Differentiate w.r.t.  $x$  (with  $M$  symmetric):

*    $\nabla(x^TMx)=2Mx$ ,
*    $\nabla(2b^Tx)=2b$ .

So

$$
\nabla q(x)=2Mx+2b.
$$

Setting gradient to zero gives the stationarity equation

$$
Mx=-b. \tag{S}
$$
*   If  $M\succ 0$  (invertible), unique solution  $x^\star=-M^{-1}b$ .
*   If  $M\succeq 0$  singular, solutions exist **iff**  $b\in\mathcal R(M)$ . When solutions exist, one canonical minimum-norm solution is
    $$
    x^\star=-M^\dagger b,
    $$
    where  $M^\dagger$  is the Moore–Penrose pseudoinverse.

#### 3.2 Completing the square “correctly” with a pseudoinverse

When  $M\succeq 0$  and  $b\in\mathcal R(M)$ , you can write

$$
x^TMx+2b^Tx = (x+M^\dagger b)^T M (x+M^\dagger b)\;-\; b^T M^\dagger b. \tag{CS}
$$

Why this is true (no handwaving):

Expand the RHS:

$$
(x+M^\dagger b)^T M (x+M^\dagger b) = x^TMx + 2x^T M M^\dagger b + (M^\dagger b)^T M (M^\dagger b).
$$

Now use two key pseudoinverse facts for symmetric  $M$ :

1.   $MM^\dagger$  is the orthogonal projector onto  $\mathcal R(M)$ .
2.  If  $b\in\mathcal R(M)$ , then  $MM^\dagger b = b$ .

So the cross term becomes  $2x^T b = 2b^T x$ , exactly what we need.

Also,  $(M^\dagger b)^T M (M^\dagger b)= b^T M^\dagger M M^\dagger b$ . Since  $b\in \mathcal R(M)$ , this simplifies to  $b^T M^\dagger b$ . (You can verify via spectral decomposition; it’s exactly the “invert on nonzero eigenspaces” behavior.)

Therefore RHS of (CS) equals  $x^TMx+2b^Tx + b^TM^\dagger b - b^TM^\dagger b$ , i.e.  $q(x)$ .

Now: because  $M\succeq 0$ , the quadratic term  $(x+M^\dagger b)^T M (x+M^\dagger b)\ge 0$  for all  $x$ , and it achieves 0 exactly when  $x+M^\dagger b\in\ker(M)$ , i.e. when  $Mx=-b$ . So the minimum value is

$$
\inf_x q(x)= -b^T M^\dagger b.
$$

Plug back into  $g(\lambda)=\inf_x q(x)-\lambda$ :

$$
\boxed{ g(\lambda)= \begin{cases} -\,b^T(A+\lambda I)^\dagger b \;-\;\lambda, & \lambda\ge 0,\ A+\lambda I\succeq 0,\ b\in\mathcal R(A+\lambda I),\\ -\infty,&\text{otherwise.} \end{cases}}
$$

That’s exactly the formula you quoted, now with every moving part explained.

* * *

6) Eigenvalue form: what the “range condition” means in coordinates
-------------------------------------------------------------------

Let  $A=Q\Lambda Q^T$  with eigenvalues  $\alpha_1,\dots,\alpha_n$  and orthonormal eigenvectors  $q_i$  (columns of  $Q$ ).

Write  $b$  in this basis:

$$
b=\sum_{i=1}^n \beta_i q_i,\quad \beta_i:=q_i^Tb.
$$

Then

*    $A+\lambda I$  has eigenvalues  $\alpha_i+\lambda$  with eigenvectors  $q_i$ .
*    $(A+\lambda I)^\dagger$  has eigenvalues
    $$
    \mu_i(\lambda)= \begin{cases} \frac{1}{\alpha_i+\lambda},&\alpha_i+\lambda\neq 0,\\[2mm] 0,&\alpha_i+\lambda=0. \end{cases}
    $$

Therefore

$$
b^T(A+\lambda I)^\dagger b =\sum_{i:\alpha_i+\lambda\neq 0}\frac{\beta_i^2}{\alpha_i+\lambda}.
$$

Now the **range condition**  $b\in\mathcal R(A+\lambda I)$  translates to:

*   If  $\alpha_i+\lambda=0$ , then the eigenspace is in  $\ker(A+\lambda I)$ .
*   For  $b$  to be in the range, it must have **no component** in that kernel.
*   So you must have
    $$
    \beta_i=0 \quad \text{for all } i \text{ with } \alpha_i+\lambda=0.
    $$

If not, the dual function is  $-\infty$ .

This is the precise meaning behind the informal “ $0/0$  convention” people say.

* * *

7) KKT-style “recipe”: how  $\lambda^\star$  and  $x^\star$  fit together
-------------------------------------------------------------------------

When strong duality holds (it does here), primal and dual solutions satisfy the familiar pattern:

*   Primal feasibility:  $\|x^\star\|^2\le 1$ .
*   Dual feasibility:  $\lambda^\star\ge 0$ ,  $A+\lambda^\star I\succeq 0$ , and range condition.
*   Complementary slackness:
    $$
    \lambda^\star(\|x^\star\|^2-1)=0.
    $$
    So either  $\lambda^\star=0$  (interior optimum), or  $\|x^\star\|=1$  (boundary optimum).
*   Stationarity (from minimizing  $L(\cdot,\lambda^\star)$ ):
    $$
    (A+\lambda^\star I)x^\star=-b. \tag{KKT}
    $$

### 7.1 The “easy” case:  $A+\lambda^\star I$  invertible

Then

$$
x^\star=-(A+\lambda^\star I)^{-1}b.
$$

And complementary slackness says:

*   if  $\|x^\star\|<1$ , then  $\lambda^\star=0$ ,
*   if  $\|x^\star\|=1$ , then  $\lambda^\star>0$ .

### 7.2 The “hard” case:  $A+\lambda^\star I$  singular (boundary + minimum-eigenvalue edge)

Then solutions to  $(A+\lambda^\star I)x=-b$  exist iff the range condition holds. Among them, a canonical choice is

$$
x_0:=- (A+\lambda^\star I)^\dagger b.
$$

But because the matrix is singular, you can add any kernel vector  $v\in\ker(A+\lambda^\star I)$ :

$$
x = x_0 + v,\quad v\in\ker(A+\lambda^\star I),
$$

and still satisfy  $(A+\lambda^\star I)x=-b$ . You then pick  $v$  (if needed) to enforce  $\|x\|=1$  when the constraint must be active. This is the classical trust-region “hard case.”

* * *

8) The big question: why strong duality holds here even if  $A$  is indefinite
------------------------------------------------------------------------------

This is the “hidden convexity” fact: one quadratic objective + one quadratic inequality constraint is special.

A clean way to say it:

*   Weak duality always gives  $g(\lambda)\le p^\star$ .
*   Strong duality here means: there exists some  $\lambda^\star\ge 0$  such that  $g(\lambda^\star)=p^\star$ .

The standard theorem behind this is the **S-lemma** (also called S-procedure). You asked not to merely cite it, so here’s the logic specialized to this problem in a way that shows what it’s doing.

### 8.1 Convert “ $p^\star$  is the minimum” into an emptiness statement

Let  $\gamma<p^\star$ . Then by definition of  $p^\star$ , there is **no** feasible  $x$  with  $f(x)\le \gamma$ . In other words, the system

$$
\|x\|^2\le 1,\qquad f(x)\le \gamma
$$

is infeasible.

Equivalently, the set

$$
\{x:\ \|x\|^2\le 1 \ \text{and}\ f(x)-\gamma\le 0\}
$$

is empty.

So “ $\gamma<p^\star$ ” is exactly “the intersection of two quadratic-inequality regions is empty.”

### 8.2 What S-lemma gives you (specialized statement)

Define two quadratic functions:

$$
q_1(x):=1-\|x\|^2, \qquad q_0(x):=f(x)-\gamma = x^TAx+2b^Tx-\gamma.
$$

So feasibility is:  $q_1(x)\ge 0$  and  $q_0(x)\le 0$ .

Now note **Slater**: there exists an  $x$  with  $q_1(x)>0$ . Here  $x=0$  gives  $q_1(0)=1>0$ . That strict feasibility is the crucial regularity condition.

**S-lemma (in this orientation)** says:

If there exists some  $x$  with  $q_1(x)>0$  (Slater), and the system

$$
q_1(x)\ge 0,\quad q_0(x)\le 0
$$

is infeasible, then there exists  $\lambda\ge 0$  such that for all  $x$ ,

$$
q_0(x)+\lambda\, q_1(x)\ge 0. \tag{S}
$$

Unpack what that inequality means:

$$
f(x)-\gamma + \lambda(1-\|x\|^2)\ge 0\quad \forall x.
$$

Rearrange:

$$
f(x) + \lambda(\|x\|^2-1)\ \ge\ \gamma \quad \forall x.
$$

Now take the inf over  $x$  on the left:

$$
\inf_x\big(f(x)+\lambda(\|x\|^2-1)\big)\ \ge\ \gamma.
$$

But the left-hand side is exactly  $g(\lambda)$ . So:

$$
g(\lambda)\ge \gamma. \tag{LB-gamma}
$$

So for every  $\gamma<p^\star$ , S-lemma produces a  $\lambda\ge 0$  with  $g(\lambda)\ge \gamma$ .

Now take  $\gamma\uparrow p^\star$ . Because weak duality always gives  $g(\lambda)\le p^\star$ , the only possible limit is

$$
\sup_{\lambda\ge 0} g(\lambda)=p^\star.
$$

That is strong duality.

So the dual exactness is literally: “emptiness of the intersection implies existence of a nonnegative multiplier that separates them globally.”

### 8.3 What did we _actually use_?

Only two special facts:

1.  There is **one** quadratic constraint (the ball).
2.  That constraint satisfies Slater ( $x=0$  is strictly inside).

That’s why this class is special. Nonconvex QCQPs with multiple quadratic constraints generally do **not** have exact Lagrangian duals.

* * *

9) A very practical way to see  $\lambda^\star$ : derivative gives the boundary condition
-----------------------------------------------------------------------------------------

Assume we are in the invertible regime ( $A+\lambda I\succ 0$ , which happens for  $\lambda>-\lambda_{\min}(A)$ ). Then

$$
g(\lambda)= -\lambda - b^T(A+\lambda I)^{-1}b.
$$

Define

$$
x(\lambda):=-(A+\lambda I)^{-1}b.
$$

Then  $b=(A+\lambda I)(-x(\lambda))\Rightarrow (A+\lambda I)^{-1}b=-x(\lambda)$ . So

$$
b^T(A+\lambda I)^{-2}b=\|(A+\lambda I)^{-1}b\|^2=\|x(\lambda)\|^2.
$$

Differentiate  $g$ :

$$
g'(\lambda)= -1 + b^T(A+\lambda I)^{-2}b = -1 + \|x(\lambda)\|^2.
$$

So the maximizer  $\lambda^\star$  (when interior in the dual feasible set) satisfies

$$
g'(\lambda^\star)=0 \quad\Longleftrightarrow\quad \|x(\lambda^\star)\|=1.
$$

That is exactly complementary slackness: “if  $\lambda^\star>0$ , primal constraint is active.”

This is why algorithms for TRS often solve a 1D equation for  $\lambda$ : find  $\lambda$  such that the unconstrained minimizer of the Lagrangian has norm 1.

* * *

10) What to remember as the mental model (no mysticism)
-------------------------------------------------------

*   The dual variable  $\lambda$  is not a random multiplier; it is literally “how much quadratic curvature  $\lambda\|x\|^2$  you must add to make the Lagrangian minimization well-defined.”
*    $A+\lambda I\succeq 0$  is exactly “no downhill direction to  $-\infty$ .”
*   The range condition is exactly “no downhill line inside the nullspace direction.”
*   Strong duality holds here because with **one** quadratic constraint and Slater, the S-lemma guarantees there is a  $\lambda^\star$  that makes the global separation inequality true, forcing  $g(\lambda^\star)=p^\star$ .
*   Once you have  $\lambda^\star$ , you recover  $x^\star$  from  $(A+\lambda^\star I)x^\star=-b$ , adjusting by nullspace only in the singular “hard case.”

* * *

If you want the next step in the same ultra-granular style: I can take a concrete “hard case” example (where  $\lambda^\star=-\lambda_{\min}(A)$  and  $b$  is orthogonal to the min-eigenspace), and show explicitly how the set of primal minimizers forms a circle/affine slice on the boundary, while the dual still gives the exact value. That example is where people’s intuition usually finally locks into place.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)