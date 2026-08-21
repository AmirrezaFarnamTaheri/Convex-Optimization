# WIDGETS.md — Interactive Widget Inventory, Standard & Backlog

Normative for all interactive content. Pedagogical rationale: `docs/PEDAGOGY.md` §7.
Inventory below is audited against the filesystem (2026-07); widget descriptions
are taken from the widgets' own header docstrings, not inferred.

---

## 1. Architecture: How Widgets Actually Load

Two mechanisms coexist (both offline-only, vendored libs, per `CLAUDE.md`):

### 1.1 ES-module widgets (the standard for new work)

- File: `topics/NN-slug/widgets/js/<name>.js`, exporting a single
  `init<PascalName>(containerId)` function.
- The lecture page provides a mount div `<div id="widget-<name>" …>` inside a
  `.widget-container` block, and mounts it with an inline module script at the
  bottom of the page:

  ```html
  <script type="module">
    import { initConvexCombination } from './widgets/js/convex-combination.js';
    initConvexCombination('widget-convex-combination');
  </script>
  ```

- Rendering libraries are imported as ES modules from the vendored tree, e.g.
  `import * as d3 from "../../../../static/lib/d3/d3.esm.js";` three.js is
  available via the page's import map (`"three": "../../static/lib/three/three.module.js"`).
- Widgets style themselves with the **site's CSS custom properties**
  (`var(--bg-surface-1)`, `var(--accent-400)`, `var(--font-mono)`, …) so they
  follow theme switching automatically.
- Python-powered widgets (currently `classification-boundary.js`, L11) go
  through `static/js/pyodide-manager.js` and the vendored Pyodide; packages
  must already be vendored — no runtime downloads.

### 1.2 Iframe widgets (L09 legacy suite)

- File: `topics/09-duality/widgets/<name>.html` — fully standalone pages with
  their **own inline styles** — embedded via `<iframe src="widgets/….html">`.
- Known deficiency: they hardcode a dark palette (`background:#0b0d12` etc.)
  instead of using site CSS variables, so they ignore the site theme switcher
  (roadmap item W-R2 below).

### 1.3 Optional convention-based loader

`static/js/widgets-loader.js` exports `mountWidgets({root, basePath})`, which
dynamic-imports and mounts every element carrying an explicit `data-widget`
attribute:

```html
<div id="widget-gd-vs-newton" data-widget="gd-vs-newton"></div>
<script type="module">
  import { mountWidgets } from '../../static/js/widgets-loader.js';
  mountWidgets();
</script>
```

It resolves `data-widget="gd-vs-newton"` to `./widgets/js/gd-vs-newton.js` and
calls `init` + PascalCase(name), falling back to a default export or a lone
named export (which is how the real-world `initGDvsNewton` casing resolves).
It returns a per-element result array so failures are inspectable rather than
silent, and it skips elements already marked `data-widget-mounted`.

**The inline form in §1.1 remains the default** — it is greppable and fails
loudly. Reach for the loader only on pages that would otherwise repeat the same
boilerplate many times. No page uses it today; it exists so the choice is
available rather than the file being dead code.

## 2. Design Standard (merge bar for any new/modified widget)

Structural:
- [ ] One file, one exported `init*(containerId)`; no globals; no CDN or
      network access; deterministic behavior (seed any randomness and expose
      the seed).
- [ ] Header docstring: `Widget:` title, `Description:`, and a
      `Concept:` line naming the lecture section it serves. *(The four L13
      widgets currently fail this — see §4.)*
- [ ] Styles via site CSS custom properties; no hardcoded colors.
- [ ] Degrades gracefully: absent container → silent return (the existing
      `if (!container) return;` idiom); tiny viewport → controls stack.

Pedagogical (from `docs/PEDAGOGY.md` §7):
- [ ] Answers **one question** the student can state beforehand; the question
      is the widget's caption in the lecture page.
- [ ] Controls labeled with the **same symbols as the adjacent math**
      (`docs/NOTATION.md` §7); a slider for the barrier parameter is labeled
      $t$, not "speed".
- [ ] Ships ≥ 1 **preset** exhibiting the interesting regime (e.g.
      $\kappa = 100$; Slater failure; separable data).
- [ ] "What to notice" list (2–4 items) beside the mount div.
- [ ] Any numerical claim shown (optimal value, gap, rate) is *recomputed* by
      the widget, not hardcoded — hardcoded values rot when parameters change.
      Exception: fixed pedagogical examples may hardcode **derived** values if
      the derivation appears in the adjacent text (e.g. `primal_dual_1d.html`
      displays $g(\lambda) = \lambda - \lambda^2/4$ for
      $\min (x{-}2)^2$ s.t. $x \le 1$ — verified correct: $x^\star = 1$,
      $\lambda^\star = 2$, $p^\star = d^\star = 1$).

## 3. Where Interaction Is Worth It (priority function)

Widget-building effort ranks by how badly statics fail:

1. **Trajectories over time** (algorithm paths, central path, GD zig-zag) — statics can't show dynamics.
2. **Limiting/degenerate behavior** (Slater failure, $t \to \infty$, separable logistic divergence) — the interesting regime is a boundary.
3. **High-dimensional projections** (PSD cone slices, dual cones) — no faithful static picture exists.
4. **Counterexample hunting** (drag points until a claimed property breaks) — active refutation beats reading one.
5. Static-replaceable illustration — **do not build**; use a figure.

## 4. Audited Inventory (2026-07)

~9,500 lines of widget JS across 40 modules + 9 standalone HTML widgets + 3 shared batch pages.

| Lecture | Widget (file) | Docstring description (abridged) | Notes |
| :--- | :--- | :--- | :--- |
| L00 | `la_batch1.html`, `la_batch2.html` | batch pages of linear-algebra visualizations | shared-batch legacy format |
| L00 | `hessian-landscape-visualizer.js` | 3-D surface of a quadratic + its Hessian | |
| L00 | `norm-geometry-visualizer.js` | unit balls of $\ell_p$ norms | |
| L01 | `la_batch2.html`, `la_batch3.html` | batch pages (`la_batch2` shared with L00) | |
| L02 | `convex-combination.js` | convex hull / convex combination explorer (drag 3 vertices + target point) | |
| L02 | `optimization-landscape.js` | 1-D convexity incl. Jensen's inequality | |
| L02 | `problem-flowchart.js` | interactive decision tree classifying problems | |
| L02 | `convergence-comparison.js` | animated convergence-rate comparison | |
| L03 | `convex-geometry-lab.js` | unified convex-set workspace | |
| L03 | `ellipsoid-explorer.js` | ellipsoid geometry from its defining matrix | |
| L03 | `polyhedron-visualizer.js` | build a polyhedron from inequality constraints | |
| L04 | `separating-hyperplane.js` | draw two convex sets, find a separating hyperplane | |
| L05 | `convex-function-inspector.js` | analyze convex functions interactively | |
| L05 | `hessian-heatmap.js` | heatmap of $\lambda_{\min}(\nabla^2 f)$ with probe | |
| L05 | `operations-preserving.js` | convexity-preserving operations demo | |
| L06 | *(same three files as L05, duplicated)* | | **gap: no conjugate/subgradient widget** (backlog W2, W3) |
| L07 | `reformulation-tool.js` | reformulations into standard form | |
| L08 | `sdp-visualizer.js` | PSD cone of $2\times2$ symmetric matrices | overlaps L09's `psd_cone_2x2.html` — consolidate (W-R3) |
| L08 | `solver-guide.js` | solver selection by problem type | |
| L09 | 9 standalone HTML widgets (`primal_dual_1d`, `kkt_vector_balance`, `value_function_support`, `slater_failure_dual_attainment`, `logsumexp_conjugate_widget`, `equality_dual_projection_2d`, `separation_two_disks`, `soc_dual_cone`, `psd_cone_2x2`) | flagship duality suite | iframe mechanism; theme-blind (W-R2) |
| L10 | `least-squares-regularization.js` | polynomial regression with L1/L2 regularization | |
| L10 | `regularization-theory.js` | ball-meets-level-set geometry of LASSO/ridge | |
| L10 | `robust-regression.js` | Huber vs. least squares under outliers | |
| L10 | `sparse-recovery.js` | LASSO sparse-signal recovery | |
| L10 | `matrix-completion.js` | low-rank matrix (image) recovery from samples | |
| L11 | `classification-boundary.js` | classification playground via **Pyodide + scikit-learn** | heaviest widget; needs load-time warning UI |
| L11 | `logistic-regression.js` | likelihood surface + convergence of logistic fit | |
| L11 | `svm-margin.js` | drag support vectors, watch margin/boundary | |
| L12 | `chebyshev-center.js` | largest inscribed circle in a user polyhedron | |
| L12 | `mvee-visualizer.js` | MVEE via **Khachiyan's algorithm**, visualized | |
| L12 | `distance-between-sets.js` | min distance between draggable convex polygons | |
| L12 | `best-fit-shape.js` | best-fit line/circle to points | |
| L12 | `robust-geometry.js` | smallest enclosing circle, standard vs. robust | |
| L12 | `rank-minimization.js` | nuclear-norm heuristic toy example | overlaps L10 `matrix-completion.js` — differentiate or merge (W-R3) |
| L13 | `gradient-descent-visualizer.js` | GD iterates on an anisotropic quadratic; anisotropy γ sets κ | zig-zag demo |
| L13 | `gd-vs-newton.js` | GD vs. Newton from the same start on $x^2 + 10y^2$ | |
| L13 | `convergence-rate.js` | log-error plot: linear (GD) vs. quadratic (Newton) rates | |
| L13 | `norm-steepest.js` | steepest-descent direction as the norm's unit ball changes | |
| L14 | `null-space-visualizer.js` | null-space method on an equality-constrained QP | |
| L14 | `projected-gd.js` | projected GD: gradient step + projection animated | |
| L14 | `feasible-vs-interior.js` | projected-GD path vs. interior-path comparison | |
| L15 | `barrier-method-path-tracer.js` | central path traced as $t$ increases | |
| L15 | `newton-step-ipm.js` | single Newton step inside an IPM | |
| L15 | `lp-simplex-vs-ip.js` | simplex (exterior vertices) vs. IPM (interior) paths | |

## 5. Remediation Items

| ID | Item | Detail |
| :--- | :--- | :--- |
| W-R1 | ~~Resolve `widgets-loader.js` stub~~ | **Done** — implemented as an opt-in `mountWidgets()` mounter (§1.3) |
| W-R2 | Theme-unify L09 iframes | Replace hardcoded dark palettes with site CSS variables (or port to ES-module widgets); until then they clash in light theme |
| W-R3 | De-duplicate | `sdp-visualizer.js` vs `psd_cone_2x2.html`; `rank-minimization.js` vs `matrix-completion.js` — keep one canonical widget each, cross-link from the other lecture |
| W-R4 | ~~L13 headers~~ | **Done** — all four L13 widgets carry §2 headers (Widget/Description/Concept/What to notice) |
| W-R5 | Presets audit | Verify every existing widget ships an interesting-regime preset; add where missing |

## 6. Build Backlog (specs; ordered by priority-function §3)

Each spec: *Question* the widget answers → *Controls* (symbol-labeled) → *Display* → *What to notice* → *Preset(s)*.

**W1 · L15 — Central-path + gap dashboard** *(upgrade of `barrier-method-path-tracer.js`)*
Q: "Why does following the path beat jumping straight to large $t$?"
Controls: $t$ slider (log scale), $\mu$ selector, "jump to $t{=}10^6$" button.
Display: 2-D LP feasible region with central path $x^\star(t)$; side panel plots duality gap $m/t$ vs. cumulative Newton iterations.
Notice: gap line is exactly $m/t$; the jump button makes Newton iterations explode (basin loss); moderate $\mu$ minimizes total work.
Presets: $\mu \in \{2, 10, 50\}$ on the same LP.

**W2 · L06 — Conjugate geometry** *(fills the L06 identity gap; generalizes L09's `logsumexp_conjugate_widget.html`)*
Q: "What does $f^*(y)$ measure geometrically?"
Controls: slope $y$ slider; function picker ($\tfrac12 x^2$, $e^x$, $|x|$, picker-defined piecewise-linear).
Display: graph of $f$ with the moving line $yx - f^*(y)$ tangent from below; second panel accumulates the graph of $f^*$ point-by-point as $y$ sweeps.
Notice: $f^*(y)$ = maximal signed gap between line $yx$ and $f$; kinks in $f$ ↔ affine pieces of $f^*$ and vice versa; for $|x|$, $f^*$ is the indicator of $[-1,1]$ — "slopes outside $[-1,1]$ are unpayable prices".
Presets: the four functions above.

**W3 · L06 — Subgradient fan**
Q: "What is the set $\partial f(x)$ at a kink?"
Controls: point $x$ slider along $f(x) = \|x\|_1$-style piecewise function; $g$ slider within the valid subgradient interval.
Display: all valid support lines shaded as a fan at kinks, single tangent at smooth points; readout of $\partial f(x)$ as an interval.
Notice: $0 \in \partial f(x)$ exactly at minimizers; the fan collapses to one line where $f$ is differentiable.
Preset: soft-threshold problem $\tfrac12(x - a)^2 + \lambda|x|$ with $a$, $\lambda$ sliders showing the solution formula appear.

**W4 · L13 — Conditioning arena** *(upgrade of `gradient-descent-visualizer.js`)*
Q: "What does $\kappa$ cost, and why does Newton not care?"
Controls: $\kappa$ slider (1–1000, log), method toggles (GD fixed step $1/L$, GD exact line search, Newton), start-point drag.
Display: contour plot of $f(x) = \tfrac12(x_1^2 + \kappa x_2^2)$ with iterate trajectories; side panel: $\log(f - p^\star)$ vs. iteration with the theoretical slope $\log\!\big(\tfrac{\kappa-1}{\kappa+1}\big)^2$ overlaid.
Notice: zig-zag angle vs. $\kappa$; empirical slope hugs the theory line; Newton's trajectory is invariant when the widget re-scales coordinates (affine-invariance toggle).
Presets: $\kappa = 2$, $\kappa = 100$ from the same start.

**W5 · L14 — KKT system anatomy**
Q: "What does the equality-constrained Newton step solve?"
Controls: drag $\nabla^2 f$ eigenvalues; drag the constraint line $Ax = b$.
Display: the block KKT matrix rendered with live numbers; the step $\Delta x$ decomposed into null-space and range-space components, drawn on the contour plot.
Notice: $\Delta x$ stays in $\mathcal{N}(A)$ from a feasible point; the KKT matrix stays invertible even when $\nabla^2 f$ is singular on $\mathcal{N}(A)^\perp$ only.
Preset: singular-(1,1)-block example.

**W6 · L11 — Separable-logistic pathology**
Q: "Why does unregularized logistic regression diverge on separable data?"
Controls: drag data points; $\lambda$ (ridge) slider incl. $\lambda = 0$.
Display: decision boundary + $\|\theta\|$ vs. iteration plot.
Notice: with separable data and $\lambda = 0$, $\|\theta\|$ grows without bound while the loss → 0; any $\lambda > 0$ stabilizes it.
Preset: one point-drag away from separability.

**W7 · L04 — Dual-cone duality dance**
Q: "How does $K^*$ move when $K$ moves?"
Controls: drag the two extreme rays of a 2-D cone $K$.
Display: $K$ and $K^*$ overlaid; angle readouts.
Notice: narrower $K$ ⇒ wider $K^*$; self-duality at right angles ($\mathbb{R}^2_+$ after rotation); $K^{**} = K$ (closure) live.
Preset: rotate-into-self-dual configuration.

Backlog items must be built to §2 and cross-referenced from
`docs/CURRICULUM.md` §4 (per-lecture widget lines) when they land.
