# CLAUDE.md — Curriculum Architect Operating Manual

This repository is a self-contained **static website** of interactive convex optimization
lecture notes (16 lectures, `topics/00` – `topics/15`). All authoring work in this repo —
new lectures, revisions, widgets, exercises — follows the protocol in this file.

---

## 1. Repository Map

```text
/
├── index.html                  # Landing page (lecture grid)
├── syllabus.html               # Course syllabus page
├── verify_site.py              # Local reference checker (run before every commit)
├── data/
│   ├── glossary.json           # Site-wide glossary terms
│   ├── problems-index.json     # Exercise/problem metadata index
│   └── diagrams-index.json     # Diagram metadata index
├── docs/
│   ├── CURRICULUM.md           # Course blueprint (learning graph, objectives, capstone)
│   ├── SETUP.md                # Local development setup
│   └── IMAGE_SOURCES.md        # Image provenance
├── topics/NN-slug/
│   ├── index.html              # The lecture page
│   ├── assets/                 # Lecture-local images/data
│   └── widgets/*.html          # Self-contained interactive widgets
├── static/
│   ├── css/convex-unified.css  # Single unified stylesheet
│   ├── js/                     # Site JS (toc, math-renderer, widgets-loader, …)
│   └── lib/                    # Vendored: katex, d3, three, pyodide, prism, marked, feather
└── tools/                      # normalize_project.py, verify/download helpers
```

**Stack facts (do not violate):**

- Pure static site — no build step, no bundler, no server-side code. Everything must
  work from `python -m http.server 8000`.
- Math renders with **KaTeX** (auto-render). Use `\( … \)` / `$ … $` for inline and
  `$$ … $$` for display math inside lecture HTML.
- All libraries are **vendored** under `static/lib/`. Never add CDN links; never add
  network fetches at runtime.
- Widgets are standalone HTML files under `topics/NN/widgets/`, loaded into lecture
  pages; interactive code execution uses the vendored **Pyodide**.
- Lecture pages share a common shell: sticky header with Prev/Next nav, sidebar TOC
  (`#toc-container`), `<main id="main" class="lecture-content">`, content in
  `<section class="section-card">` blocks, callouts via `.insight` / note / warning
  classes. Copy the shell from a neighboring lecture; `tools/normalize_project.py`
  can normalize drift.

**Quality gate:** `python verify_site.py` must pass (all local `href`/`src` resolve)
before any commit that touches HTML.

---

## 2. Non-Negotiable Educational Invariants

Every authored artifact must satisfy all six:

1. **Zero-Handwaving Guarantee.** No "left as an exercise" without a provided solution,
   no skipped derivation steps, no code stubs that don't run, no undefined notation.
   Long proofs may move to a lecture Appendix — but they must exist in full.
2. **Artifact-First Delivery.** The deliverable is the finished lecture page, widget,
   or problem set — not an outline or a recommendation.
3. **First-Principles Progression.** Every concept is presented in this order:
   Intuition (mental model) → Formal theory (LaTeX derivation) → Concrete
   implementation (widget / Pyodide code) → Production reality and edge cases.
4. **Complete Solution Duality.** Every exercise ships with both the student-facing
   prompt and a complete, verified reference solution (collapsed/toggled in the page,
   indexed in `data/problems-index.json`).
5. **Visual & Scannable Structuring.** Section cards, tables for side-by-side
   comparisons, explicit diagrams, `.insight` callouts for key takeaways, and
   warning callouts for pitfalls. Content must serve both first-time deep reading
   and rapid exam revision.
6. **Dual-Perspective Auditing.** Before finalizing, audit every explanation as
   (a) a struggling student — where does complexity spike? what notation appears
   undefined? — and (b) a skeptical principal engineer — is anything simplified
   into inaccuracy? do numerical claims hold?

---

## 3. Authoring Workflow

For any lecture-content change, run this loop:

1. **Read the neighbors.** Open the previous and next lectures; keep notation,
   terminology, and shell markup consistent across the course
   (e.g., $f_0$ for objective, $f_i \le 0$ for inequality constraints,
   $\lambda, \nu$ for dual variables — Boyd & Vandenberghe conventions).
2. **Draft against the invariants** in §2. Pair every proof with a geometric or
   economic interpretation. Match widget variable names to the LaTeX symbols.
3. **Lint pass.**
   - Math: every step explicit; every symbol defined at first use; KaTeX-renderable
     (no unsupported macros).
   - Code/widgets: self-contained file, vendored libs only, deterministic seeds,
     works offline.
   - Links: `python verify_site.py` passes.
4. **Update the indexes** when adding problems, glossary terms, or diagrams
   (`data/*.json`).
5. **Cross-check the blueprint.** New or restructured content must stay consistent
   with `docs/CURRICULUM.md` (objectives, prerequisite edges, assessment). Update
   the blueprint in the same commit if scope changed.

---

## 4. Content Conventions

| Element | Convention |
| :--- | :--- |
| Lecture numbering | `NN-slug` directories, `NN. Title` in `<h1>` and `<title>` |
| Learning objectives | First `section-card` after the header; 4–6 actionable, Bloom-verb items |
| Derivations | Full step-by-step in-line for short proofs; Appendix section for long proofs — never omitted |
| Exercises | Tiered difficulty (easy / intermediate / hard) with `estimatedTime`, typed (`verification`, `computation`, `modeling`, …), full solutions |
| Widgets | One concept per widget; controls labeled with the same symbols as the math; a "what to notice" caption |
| Pitfalls | Explicit warning callouts: misconception → correct mental model |
| Citations | These are unofficial study notes; keep the README disclaimer intact; respect `docs/IMAGE_SOURCES.md` for any image |

---

## 5. Definition of Done (per artifact)

- [ ] All six invariants in §2 hold.
- [ ] `python verify_site.py` passes.
- [ ] Notation consistent with adjacent lectures and the glossary.
- [ ] Every exercise has a complete solution; every code cell runs offline.
- [ ] `docs/CURRICULUM.md` still accurately describes the course.
