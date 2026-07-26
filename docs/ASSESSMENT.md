# ASSESSMENT.md — Problem-Bank Architecture & Rubrics

Normative for all exercises, example problems, and the capstone rubric.
Companion to `docs/CURRICULUM.md` (per-lecture targets) and `docs/PEDAGOGY.md`
§3 (faded scaffolding).

---

## 1. Problem Taxonomy

Every problem carries exactly one `type`:

| `type` | The student must… | Typical stem |
| :--- | :--- | :--- |
| `verification` | prove a stated property holds | "Show that the epigraph of a norm is convex." |
| `computation` | carry a defined procedure to a numeric/closed-form answer | "Find the projection of $(2,1)$ onto …" |
| `derivation` | produce a multi-step symbolic result (dual, KKT system, conjugate) | "Derive the dual of basis pursuit." |
| `modeling` | translate a word problem into a standard-form convex program | "A factory ships…" |
| `implementation` | write runnable code meeting stated assertions | "Implement backtracking GD; the test cell must pass." |
| `analysis` | explain/predict behavior, compare methods, interpret results | "Why does the iterate zig-zag when $\kappa$ grows?" |
| `counterexample` | construct an object refuting a plausible claim | "Find two quasiconvex functions whose sum is not." |

Balance rule per lecture bank: no type exceeds 40% of the bank; every bank
contains ≥ 1 `counterexample` or `analysis` problem (concept, not syntax —
the Socratic-educator check).

## 2. Difficulty Tiers

Tier names match the existing index vocabulary (`easy` / `medium` / `hard`).

| Tier | Definition | Scaffolding shown to student | Time budget |
| :--- | :--- | :--- | :--- |
| `easy` | single concept, single step or direct definition-application | completion skeleton or strong hint | 10–20 min |
| `medium` | two concepts composed, or one concept in an unfamiliar setting | guided hints only | 20–40 min |
| `hard` | cross-lecture composition, open modeling, or proof requiring an idea | bare statement | 40–90 min |

Target mix per bank: roughly **3 : 4 : 2** (easy : medium : hard), adjusted
per lecture in `docs/CURRICULUM.md` §4. Hard problems should preferentially be
cross-lecture compositions (`docs/PEDAGOGY.md` §9).

## 3. Per-Lecture Bank Targets vs. Current State

Current indexed inventory (audit 2026-07): **15 problems**, all under stale
slugs; L15 additionally has 5 in-page problems (P15.1–P15.5) not yet indexed.

| Lecture | Target (e/m/h) | Currently indexed | Action |
| :--- | :--- | :--- | :--- |
| L00 | 8 (3/3/2) | 0 | author |
| L01 | 6 (2/3/1) | 0 | author |
| L02 | 8 (3/3/2) | 0 | author |
| L03 | 8 (3/3/2) | 14 under stale `02-convex-sets` | re-key, rebalance, prune to 8 |
| L04 | 7 (2/3/2) | 0 | author |
| L05 | 9 (3/4/2) | 0 | author |
| L06 | 8 (2/4/2) | 1 under stale `03-convex-functions` (Fenchel/biconjugate → belongs here, see §5) | re-key, extend |
| L07 | 8 (2/4/2) | 0 | author |
| L08 | 7 (2/3/2) | 0 | author |
| L09 | 10 (3/4/3) | 0 (page has exercises; index empty) | index + extend |
| L10 | 8 (3/3/2) | 0 | author with build-out (R1) |
| L11 | 7 (2/3/2) | 0 | author with build-out |
| L12 | 6 (2/3/1) | 0 | author with build-out |
| L13 | 8 (2/4/2) | 0 (page has solved exercises) | index + extend |
| L14 | 6 (2/3/1) | 0 | author with build-out |
| L15 | 8 (2/4/2) | 0 indexed; 5 in-page (P15.1–5) | index existing + 3 new |
| **Total** | **122** | **15 indexed** | |

## 4. Solution-Key Standard (invariant 4, operationalized)

Every problem's reference solution must contain, in order:

1. **Strategy line** — one sentence naming the technique *and why it's the
   cheapest one that works* ("Composition rules; the Hessian is a mess here").
2. **Full worked steps** — one operation per line for derivations
   (`docs/PEDAGOGY.md` §6); runnable code for implementations.
3. **Verification** — a check that is *independent of the derivation path*:
   numeric substitution, weak-duality cross-check, assertion cell, or
   dimension/units audit.
4. **Moral** — one sentence on what the problem was really testing.

Implementation problems additionally ship an assertion block the student's
code must pass *before* they open the solution (self-service grading).

## 5. `data/problems-index.json` Schema (v2)

Current entries use `{id, lecture, title, difficulty, type, estimatedTime}`.
Extended schema — existing fields keep their meaning:

```json
{
  "id": "09-004",
  "lecture": "09-duality",
  "title": "P4 — Dual of basis pursuit",
  "difficulty": "hard",
  "type": "derivation",
  "estimatedTime": 45,
  "requiresLectures": ["06-convex-functions-advanced"],
  "threads": ["duality"],
  "solutionAnchor": "#sol-09-004"
}
```

- `lecture` **must** be a current `topics/` slug. Stale-slug repair
  (per-problem, verified against each problem's actual content 2026-07):
  all 14 `02-convex-sets` problems are convex-sets material (several are
  literally [BV] Ch. 2 exercises) → `03-convex-sets-geometry`; the single
  `03-convex-functions` problem (`03-015`, Fenchel's inequality &
  biconjugate) is conjugacy material → `06-convex-functions-advanced`, **not**
  L05 — in this course conjugates live in L06. The stale keys are a
  pre-renumbering scheme from before the two linear-algebra lectures were
  prepended; re-keying is a per-problem decision, not a bulk rename.
- Problems titled "BV x.y" are re-derivations of [BV] exercises with original
  solutions (`docs/REFERENCES.md` §1); keep the "BV x.y" title prefix so the
  provenance stays visible.
- `requiresLectures` encodes cross-lecture composition (drives the "what to
  backfill" hints, roadmap R6).
- `threads` ⊆ {`duality`, `conditioning`, `reformulation`} (CURRICULUM §1.2).
- `solutionAnchor` links the index to the in-page solution block.

## 6. Solved Exemplars (one per tier — the authoring gold standard)

The three problems below are complete instances of the §4 standard. New
problems are reviewed against them.

---

### Exemplar E (easy · `verification` · L05) — "Epigraph of a norm is convex"

**Problem.** Let $f(x) = \|x\|$ be any norm on $\mathbb{R}^n$. Show that
$\operatorname{\mathbf{epi}} f = \{(x,t) \in \mathbb{R}^{n+1} : \|x\| \le t\}$
is a convex set.

**Solution.**

*Strategy:* direct verification from the definition of convexity, using only
the two norm axioms (triangle inequality, absolute homogeneity) — no calculus
needed or possible (norms aren't differentiable at $0$).

Take $(x_1, t_1), (x_2, t_2) \in \operatorname{\mathbf{epi}} f$ and
$\theta \in [0,1]$. We must show
$\theta(x_1, t_1) + (1{-}\theta)(x_2, t_2) \in \operatorname{\mathbf{epi}} f$,
i.e. $\|\theta x_1 + (1{-}\theta)x_2\| \le \theta t_1 + (1{-}\theta)t_2$:

$$
\begin{aligned}
\|\theta x_1 + (1-\theta)x_2\|
&\le \|\theta x_1\| + \|(1-\theta)x_2\| && \text{(triangle inequality)}\\
&= \theta\|x_1\| + (1-\theta)\|x_2\|   && \text{(homogeneity; } \theta, 1{-}\theta \ge 0\text{)}\\
&\le \theta t_1 + (1-\theta)t_2        && \text{(membership: } \|x_i\| \le t_i\text{)}.
\end{aligned}
$$

*Verification (independent check):* the epigraph is also
$\bigcap_{\|u\|_* \le 1} \{(x,t): u^\top x \le t\}$ — an intersection of
halfspaces via the dual-norm characterization — and intersections of convex
sets are convex (L03 §3). Two different routes, one answer.

*Moral:* epigraph convexity is exactly function convexity; for nonsmooth
functions the definition-level argument is the *only* tool, which is why it
must be automatic.

---

### Exemplar M (medium · `derivation` + `analysis` · L09) — "KKT case analysis with a sensitivity check"

**Problem.** Solve, by KKT case analysis (no solver):

$$
\text{minimize } x_1^2 + x_2^2 \quad \text{subject to } x_1 + x_2 \ge 1 .
$$

Then predict, using the multiplier, the change in $p^\star$ when the
constraint tightens to $x_1 + x_2 \ge 1.1$, and compare with the exact value.

**Solution.**

*Strategy:* the problem is convex (quadratic objective, affine constraint) and
Slater holds (e.g. $x = (1,1)$ is strictly feasible), so KKT is necessary and
sufficient; two cases on the active set.

Standard form: $f_0 = x_1^2 + x_2^2$, $f_1(x) = 1 - x_1 - x_2 \le 0$.
Lagrangian: $L = x_1^2 + x_2^2 + \lambda(1 - x_1 - x_2)$.

KKT system:

$$
2x_1 - \lambda = 0, \qquad 2x_2 - \lambda = 0, \qquad
\lambda \ge 0, \qquad 1 - x_1 - x_2 \le 0, \qquad \lambda(1 - x_1 - x_2) = 0 .
$$

- **Case $\lambda = 0$ (constraint inactive):** stationarity gives $x = (0,0)$,
  but $f_1(0,0) = 1 > 0$ — infeasible. Case rejected.
- **Case $f_1 = 0$ (active):** stationarity gives $x_1 = x_2 = \lambda/2$;
  activity gives $x_1 + x_2 = 1$, so $\lambda^\star = 1 \ge 0$ ✓ and
  $x^\star = (\tfrac12, \tfrac12)$, $p^\star = \tfrac12$.

*Sensitivity:* tightening to $x_1 + x_2 \ge 1.1$ is the perturbation
$f_1(x) \le u$ with $u = -0.1$. Shadow-price prediction (L09 §6):
$\Delta p^\star \approx -\lambda^\star u = -(1)(-0.1) = +0.05$.

*Verification (independent check):* by symmetry the perturbed optimum is
$x = (0.55, 0.55)$, $p^\star(u) = 2(0.55)^2 = 0.605$; exact change
$= 0.605 - 0.5 = 0.105$ vs. predicted $0.100$ — first-order agreement, with
the positive curvature of $p^\star(u) = (1-u)^2/2$ explaining the
second-order excess $u^2/2 = 0.005$ exactly.

*Moral:* KKT solves small problems *by hand* via active-set casework, and the
multiplier is not a bookkeeping device — it prices the constraint.

---

### Exemplar H (hard · `derivation`, cross-lecture L06→L09 · L09) — "Dual of basis pursuit"

**Problem.** Derive the Lagrange dual of basis pursuit
($A \in \mathbb{R}^{m\times n}$, $m < n$):

$$
\text{minimize } \|x\|_1 \quad \text{subject to } Ax = b,
$$

state weak duality explicitly, and interpret the dual constraint.

**Solution.**

*Strategy:* the objective is nonsmooth, so conjugate machinery (L06 §3) beats
any attempt at stationarity with gradients; the key fact is
$\|\cdot\|_1^* = I_{\{\|\cdot\|_\infty \le 1\}}$ (conjugate of a norm =
indicator of the dual-norm ball; $\ell_1$ and $\ell_\infty$ are dual norms).

Lagrangian (equality multipliers $\nu \in \mathbb{R}^m$, sign-free):

$$
L(x, \nu) = \|x\|_1 + \nu^\top(Ax - b).
$$

Dual function:

$$
\begin{aligned}
g(\nu) &= \inf_x \left( \|x\|_1 + (A^\top\nu)^\top x \right) - b^\top \nu \\
&= -\sup_x \left( (-A^\top\nu)^\top x - \|x\|_1 \right) - b^\top \nu
  && \text{(rewrite inf as } -\sup\text{)} \\
&= -\,\|\cdot\|_1^*(-A^\top\nu) - b^\top \nu
  && \text{(definition of conjugate)} \\
&= \begin{cases} -\,b^\top \nu & \|A^\top \nu\|_\infty \le 1 \\ -\infty & \text{otherwise} \end{cases}
  && \text{(norm conjugate = dual-ball indicator; } \|{-}z\|_\infty = \|z\|_\infty\text{)}.
\end{aligned}
$$

Dual problem (implicit-constraint form, then substituting $\nu \to -\nu$ for
readability — allowed since $\nu$ ranges over all of $\mathbb{R}^m$):

$$
\text{maximize } b^\top \nu \quad \text{subject to } \|A^\top \nu\|_\infty \le 1 .
$$

**Weak duality, explicitly:** for any feasible $x$ ($Ax = b$) and dual-feasible
$\nu$: $b^\top\nu = (Ax)^\top\nu = x^\top(A^\top\nu) \le \|x\|_1\,\|A^\top\nu\|_\infty
\le \|x\|_1$ (Hölder) — every dual-feasible point certifies a lower bound,
with no optimization theory invoked.

*Verification (independent check):* $n=1, A = 1, b = 1$: primal optimum
$x = 1$, $p^\star = 1$; dual: maximize $\nu$ s.t. $|\nu| \le 1$ gives
$d^\star = 1$. Gap zero, as strong duality predicts (linear constraints +
finite $p^\star$).

*Interpretation:* the dual searches for the correlation pattern $A^\top\nu$
most aligned with $b$ while every entry stays in $[-1,1]$; at optimum,
entries of $A^\top\nu^\star$ hitting $\pm 1$ flag the coordinates where
$x^\star$ may be nonzero — the complementary-slackness reading that underlies
sparse-recovery certificates (L10 §5).

*Moral:* conjugates turn nonsmooth duals into table lookups; Hölder *is*
weak duality here — the abstract theorem specializes to a classical
inequality.

---

## 7. Grading Rubrics

### 7.1 Derivation / verification problems (10 pts)

| Points | Criterion |
| ---: | :--- |
| 2 | Correct setup: standard form, symbols per `docs/NOTATION.md`, hypotheses stated |
| 4 | Steps: complete, one operation per line, each justified |
| 2 | Result correct (incl. domain/sign discipline) |
| 2 | Independent verification present and meaningful |

### 7.2 Modeling problems (10 pts)

| Points | Criterion |
| ---: | :--- |
| 3 | Faithful translation (all constraints captured; no invented ones) |
| 3 | Correct class placement + convexity argument |
| 2 | Reformulation legality argued (tightness of relaxed/auxiliary constraints) |
| 2 | Solution-recovery map back to original variables |

### 7.3 Implementation problems (10 pts)

| Points | Criterion |
| ---: | :--- |
| 3 | Passes the shipped assertion block |
| 3 | Algorithm matches the stated math (names per `docs/NOTATION.md` §7) |
| 2 | Numerical hygiene: tolerances, seeds, degenerate-input behavior |
| 2 | Output interpretation (plot or printed diagnostic with one-line reading) |

The capstone matrix in `docs/CURRICULUM.md` §6.4 composes these rubrics.

## 8. Mastery Checkpoints

- Per-lecture mastery checklists live in `docs/CURRICULUM.md` §4 and are the
  self-test layer (< 30 min each, `docs/PEDAGOGY.md` §9).
- **Midterm checkpoint** (semester plan Wk 7): checklists L02–L06 plus one
  hard-tier problem from each of L04, L05.
- **Pre-capstone gate** (Wk 11): the L09 checklist is a hard prerequisite —
  every capstone option depends on step 2 (dualize).
