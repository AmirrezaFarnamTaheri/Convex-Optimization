# PEDAGOGY.md — Pedagogical Engineering Handbook

How lectures in this course are *built*. `CLAUDE.md` states the invariants;
this document is the working manual for satisfying them. It is normative for
every content PR.

---

## 1. The Concept Presentation Pipeline

Every substantive concept moves through four stations, **in this order**:

```text
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────────┐
│ 1. INTUITION │──►│ 2. FORMALISM │──►│ 3. MECHANISM │──►│ 4. REALITY CHECK │
│ mental model,│   │ definition,  │   │ widget, code,│   │ edge cases, when │
│ picture, why │   │ theorem,     │   │ worked       │   │ it fails, cost,  │
│ we care      │   │ full proof   │   │ computation  │   │ practice caveats │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────────┘
```

Rules of the pipeline:

- **Never open with a definition.** Open with the question the definition
  answers, or the failure the theorem prevents.
- **Station 2 is complete or it is absent.** A proof too long for the flow
  moves to the lecture Appendix *in full* — with a forward reference at the
  point of use. "It can be shown" is banned (`CLAUDE.md` invariant 1).
- **Station 3 grounds notation.** Widget controls and code variables carry the
  same symbols as the math ($t$, $\lambda$, $\kappa$ — see `docs/NOTATION.md` §6).
- **Station 4 is where honesty lives.** Every idealized statement gets its
  boundary: Slater can fail, Newton can diverge undamped, relaxations are bounds.

## 2. Cognitive Load Rules

Concrete limits, learned from where the developed lectures (L00–L09) succeed:

| Rule | Operational form |
| :--- | :--- |
| **One new object per subsection** | An `<h3>` introduces at most one new definition; a second definition means a second subsection |
| **Notation before use, always** | Any symbol not in `docs/NOTATION.md`'s core tables is defined in the sentence where it first appears |
| **Chunk proofs** | Multi-step proofs are numbered steps with a one-line *goal statement* before step 1 ("We will show the gap is exactly $m/t$ by constructing a dual feasible point") |
| **Interleave, don't batch** | After ≤ 2 theory subsections, a worked example or widget; never three theory sections back-to-back |
| **Preview forward edges** | When a concept exists to serve a later lecture (rel-int → Slater), say so explicitly at introduction — purpose reduces perceived arbitrariness |
| **Close every loop** | When the later lecture arrives, name the callback ("This is why L03 §5 insisted on relative interior") |

## 3. Worked Examples & Faded Scaffolding

Exercises follow a fading gradient within each lecture:

1. **Worked example (in the flow):** full solution, every step narrated,
   including the *choice* of technique ("Hessian would work but composition is
   two lines").
2. **Completion problems (easy tier):** solution skeleton given, student fills
   marked gaps.
3. **Guided problems (medium tier):** hint structure only ("First show the
   constraint is active at the optimum").
4. **Open problems (hard tier):** bare statement; the solution key carries the
   full narrative.

Every tier ships with a complete reference solution (`CLAUDE.md` invariant 4);
tiers differ in what the *student-facing* face reveals, never in whether the
solution exists. Full tier definitions and rubrics: `docs/ASSESSMENT.md` §2–3.

## 4. Analogy Registry

Analogies are load-bearing infrastructure: reused consistently, each with a
documented breaking point (stated in-lecture at first use, so students know
where the analogy ends).

| Concept | Canonical analogy | Where it breaks |
| :--- | :--- | :--- |
| Convex set | "No hiding": every point sees every other point | Says nothing about closedness/boundedness |
| Convex function | Bowl / sagging rope under gravity | Rope suggests smoothness — kinks ($\|x\|$) are still convex |
| Lagrange multiplier | Price per unit of constraint violation (shadow price) | Prices are *local* rates; large perturbations break linearity |
| KKT stationarity | Force balance: objective gradient vs. constraint normal forces | Forces only push from *active* constraints (complementary slackness is the "contact" condition) |
| Dual problem | The adversary's best certified lower bound | "Adversary" wrongly suggests zero-sum symmetry when the gap is nonzero |
| Conjugate $f^*$ | Best profit at posted prices $y$: $\sup_x(y^\top x - f(x))$ (cost $f$, revenue $y^\top x$) | Needs the extended-value convention to price outside the domain |
| Central path | A road through the interior that avoids the walls until the destination | The road is followed *approximately*; exact centering is never needed |
| Condition number | Steep narrow valley: gradient points across, not along | Affine invariance of Newton means the valley is a *coordinate* artifact |
| Subgradient | Any support line you can slide under the graph | At smooth points the set collapses — multiplicity is the kink phenomenon |

New analogies must be added here (with breaking point) before use in a lecture.

## 5. Callout Taxonomy

The unified stylesheet supports callout blocks. Use them with these fixed
semantics (do not improvise new meanings):

| Callout | Purpose | Frequency budget |
| :--- | :--- | :--- |
| **Insight** (`.insight`) | The one-sentence takeaway a student should retain a year later | ≤ 1 per section |
| **Warning** | A documented misconception or failure mode, phrased as *trap → fix* | Wherever §4-of-CURRICULUM lists a trap |
| **Thread** | One-liner locating this section on a cross-cutting thread (duality / conditioning / reformulation, CURRICULUM §1.2) | ≤ 1 per lecture per thread |
| **Preview** | Forward edge: "this exists for Lecture N" | At forward-edge introductions |
| **Callback** | Backward edge closing a Preview loop | When the debt is paid |

## 6. Math Writing Standards

- KaTeX only; check any new macro renders under the vendored KaTeX before commit.
- Display math (`$$…$$`) for anything referenced later or longer than ~half a
  line; inline math never wraps mid-expression.
- Derivation steps: one operation per line, with the justification on the line
  (e.g., `\quad\text{(Cauchy–Schwarz)}`), aligned on the relation symbol.
- Theorem/Definition/Proof blocks are labeled and numbered within a lecture;
  references use those numbers, never "the theorem above."
- Sign and orientation conventions are fixed course-wide by `docs/NOTATION.md`
  §4–5 (minimization default, $f_i \le 0$, $\lambda \succeq 0$, gradient as
  column vector). A lecture may not deviate even if a cited source does; add a
  conversion remark instead.

## 7. Widget Pedagogy

(Design standard and inventory in `docs/WIDGETS.md`; the pedagogy in brief.)

- A widget exists to answer **one question** the student can state before
  touching it; the question appears as the widget's caption.
- Every widget ships a **"What to notice"** list (2–4 observations) and at
  least one **preset** that exhibits the interesting regime (e.g.,
  $\kappa = 100$ zig-zag; Slater failure).
- Controls map 1:1 to symbols in the adjacent math. If the math has $t$, the
  slider is labeled $t$, not "speed".
- A widget that merely *decorates* (animates something the static figure
  already shows) is cut — interaction must buy insight that statics can't
  (limits, trajectories, high-dimensional projections, counterexample hunting).

## 8. The Dual-Perspective Audit (operational form)

Before a lecture PR merges, walk both personas from CURRICULUM §2.1 through
the page:

**Struggling-student pass** — mark every place where:
1. a symbol appears before its definition line,
2. two consecutive derivation steps hide more than one operation,
3. a section exceeds the one-new-object rule,
4. a claim's *purpose* is not stated before its content.

**Skeptical-engineer pass** — mark every place where:
1. an idealized claim lacks its Station-4 boundary,
2. a numerical assertion (rate, complexity, tolerance) lacks a derivation or citation,
3. code/widget behavior could diverge from the stated math (seeds, tolerances, degenerate inputs),
4. a simplification would mislead if quoted out of context.

Zero unresolved marks is the merge bar. The checklist lives here so review
comments can cite rule numbers (e.g., "PEDAGOGY §8.1-2").

## 9. Revision & Retention Layer

Each lecture's closing apparatus serves the Exam-Reviser persona:

- **Cheat sheet section:** every key formula in a scannable table, each row
  linking back to its derivation anchor.
- **Mastery checklist** (CURRICULUM §4 per lecture): 4–6 checkbox items a
  student can self-test in < 30 minutes; these are the merge-time definition
  of the lecture's scope.
- **Spaced re-encounter:** the assessment banks deliberately re-test earlier
  lectures' tools under later lectures' problems (e.g., L09 problems require
  L06 conjugates; L15 problems require L13 Newton analysis) — when authoring
  problems, prefer a cross-lecture composition over an isolated drill at equal
  difficulty.
