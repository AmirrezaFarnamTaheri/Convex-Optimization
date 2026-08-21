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

## 3. Per-Lecture Bank Inventory

### 3.1 What the index used to say, and why it was rebuilt

The pre-2026-07 `data/problems-index.json` held 15 entries under pre-renumbering
slugs (`02-convex-sets`, `03-convex-functions`). Verifying each against page
content showed the problem was worse than stale keys: **14 of the 15 referenced
exercises that no longer exist anywhere on the site** (titles like "P1 — Epigraph
of a norm is convex" and "BV 2.1 — Two-point convexity implies k-point
convexity" return no match in any `topics/*/index.html`). They were residue from
a content generation that has since been rewritten. The single survivor,
Fenchel's inequality and the biconjugate, lives in **L06** — confirming the
per-problem re-key call in §5 rather than a bulk rename to L05.

The index was therefore **regenerated from page content** rather than repaired:
every `<h3 id="prob-NN-XXX">` exercise heading across all 16 lectures is now
indexed, and each problem heading carries a stable `id` so `solutionAnchor`
resolves to a real target.

### 3.2 Current inventory (regenerated 2026-07)

**211 problems indexed; 211 carry a complete in-page solution** — invariant 4
(Complete Solution Duality) verified mechanically, not assumed.

| Lecture | Indexed | e / m / h | Target (§2 mix) | Gap |
| :--- | ---: | :--- | :--- | :--- |
| L00 | 21 | 0 / 14 / 7 | 8 | over target; **no easy tier** |
| L01 | 12 | 0 / 8 / 4 | 6 | over target; no easy tier |
| L02 | 8 | 0 / 5 / 3 | 8 | count met; no easy tier |
| L03 | 21 | 7 / 12 / 2 | 8 | over target; well-balanced |
| L04 | 17 | 6 / 9 / 2 | 7 | over target |
| L05 | 11 | 2 / 6 / 3 | 9 | healthy |
| L06 | 32 | 4 / 24 / 4 | 8 | largest bank; medium-heavy |
| L07 | 12 | 0 / 9 / 3 | 8 | no easy tier |
| L08 | 20 | 1 / 16 / 3 | 7 | medium-heavy |
| L09 | 17 | 0 / 11 / 6 | 10 | keystone bank; **no easy tier** |
| L10 | 5 | 3 / 2 / 0 | 8 | **thin; no hard tier** |
| L11 | 5 | 4 / 1 / 0 | 7 | **thin; no hard tier** |
| L12 | 5 | 0 / 5 / 0 | 6 | **thin; no hard tier** |
| L13 | 15 | 5 / 10 / 0 | 8 | count fine; **no hard tier** |
| L14 | 5 | 5 / 0 / 0 | 6 | **thin; easy-only** |
| L15 | 5 | 5 / 0 / 0 | 8 | **thin; easy-only** |
| **Total** | **211** | 42 / 132 / 37 | — | |

> **Difficulty labels are provisional.** They are assigned by a length proxy
> (solution length plus half the statement length) at index-generation time, not
> by human judgment. The proxy is honest about direction — long multi-part
> derivations do land in `hard` — but it systematically misreads two cases: a
> terse statement of a genuinely deep result reads `easy`, and a verbose
> walkthrough of a routine computation reads `hard`. **Calibrating these labels
> by hand is roadmap item R2b**; until then, treat the tier as a hint and the
> `estimatedTime` derived from it as a lower bound.

### 3.3 What the inventory reveals

- **Application and algorithm lectures are the assessment gap**, matching the
  content-depth gap: L10–L12, L14, L15 have exactly 5 problems each with **no
  hard tier at all**, while L06 alone has 32.
- **Seven lectures have no easy-tier problems** (L00, L01, L02, L07, L09 and,
  by the proxy, others), meaning there is no gentle on-ramp for the
  completion-problem scaffolding described in `docs/PEDAGOGY.md` §3.
- **Type mix skews to `verification`** (130 of 211). The balance rule in §1 caps
  any single type at 40%; the bank is at ~62%. Authoring priority is
  `modeling`, `implementation` (currently 1), `computation` (4), and
  `counterexample` (1).

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

The file is `{schemaVersion: 2, generatedNote, problems: [...]}`. Each problem:

```json
{
  "id": "09-004",
  "lecture": "09-duality",
  "title": "P9.4 — Dual of basis pursuit",
  "difficulty": "hard",
  "type": "derivation",
  "estimatedTime": 55,
  "solutionAnchor": "#prob-09-004",
  "hasSolution": true,
  "requiresLectures": ["06-convex-functions-advanced"],
  "threads": ["duality"]
}
```

Field notes:

- `id` is `NN-XXX` (lecture number, zero-padded problem number) and matches the
  in-page heading id `prob-NN-XXX` exactly — that pairing is what makes the
  index verifiable against content.
- `solutionAnchor` is the in-page fragment; `#prob-NN-XXX` resolves because
  every problem `<h3>` now carries that id.
- `hasSolution` records the mechanical check that the problem body contains a
  solution block (a `solution-box`, a `Solution:`/`Proof:`/`Analysis:` marker, or
  an explicit appendix pointer). It is `true` for all 211 problems; a `false`
  here is an invariant-4 violation and should fail review.
- `requiresLectures` lists detected cross-lecture prerequisites (81 problems
  carry one), driving the "what to backfill" hints of roadmap R8.
- `threads` ⊆ {`duality`, `conditioning`, `reformulation`} (CURRICULUM §1.2).

**Regenerating.** The index is derived from page content, so after adding or
retitling exercises, regenerate rather than hand-editing — hand edits drift
from the pages, which is exactly how the previous index came to reference
14 nonexistent problems.

- `lecture` **must** be a current `topics/` slug; regeneration guarantees this
  because the slug is the directory the problem was read from.
- If a future problem is a re-derivation of a [BV] exercise, keep a "BV x.y"
  marker in its title so the provenance stays visible
  (`docs/REFERENCES.md` §1) — solutions must still be original.
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
