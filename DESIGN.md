# DESIGN.md — Convex Optimization Visual Design & Interactive Laboratory System

> **Aesthetic Essence:** *Geometric Precision & Rigorous Convex Analysis*  
> **Brand Adjectives:** Axiomatic · High-Precision · Architectural · Tactile · Uncluttered  
> **Stack Adapter:** Static Web Components + D3.js + Three.js + Pyodide + KaTeX + OKLCH CSS Tokens  
> **Hallmark Version:** 2026 Anti-Slop Compliant

---

## 1. Aesthetic Direction & Positioning

- **Artifact Type:** Interactive Graduate-Level Optimization Compendium & WebGL/D3 Mathematical Laboratory.
- **Audience:** Applied mathematicians, machine learning researchers, quantitative engineers, operations researchers, and computer scientists.
- **Single Core Outcome:** Master the geometry, duality, and algorithmic machinery of convex optimization through formal theorem-proof derivations, live interactive D3/Three.js geometric manipulators, and in-browser Pyodide code executions.
- **Signature Move:** Real-time geometric dual-split view — mathematical primal formulation with live D3/Three.js hyperplane separation manipulators on the left, and synchronized dual function / KKT slackness trajectories on the right.

---

## 2. Typography System

| Role | Font Family | Weights | Usage & Rules |
| :--- | :--- | :--- | :--- |
| **Display / Headings** | `Newsreader`, Georgia, serif | 600, 700 | Lecture titles, theorem environments, lemma headers. **Always roman (`font-style: normal`) — zero italic headings.** |
| **UI & Controls** | `Cabinet Grotesk`, `Satoshi`, sans-serif | 500, 600, 700 | Interactive widget sliders, parameter inputs, tab strips, badges. |
| **Body Text** | `Satoshi`, -apple-system, sans-serif | 400, 500 | Mathematical narrative, geometric intuition, algorithm steps. |
| **Code & Tabular Numbers** | `JetBrains Mono`, monospace | 400, 500 | Python code, matrix dimensions, iteration logs (`font-variant-numeric: tabular-nums`). |

### Modular Scale (Ratio: 1.250 — Major Third)
- `--font-size-xs`: `0.75rem` (12px)
- `--font-size-sm`: `0.875rem` (14px)
- `--font-size-base`: `1.000rem` (16px)
- `--font-size-md`: `1.250rem` (20px)
- `--font-size-lg`: `1.563rem` (25px)
- `--font-size-xl`: `1.953rem` (31px)
- `--font-size-xxl`: `2.441rem` (39px)

---

## 3. OKLCH Color Palette & Semantic Roles (60-30-10 Distribution)

```css
:root {
  /* 60% Dominant Surfaces (Crisp Mathematical Alabaster) */
  --color-bg: oklch(0.985 0.005 85);            /* #fcfbf9 Warm Ivory White */
  --color-surface: oklch(0.965 0.008 85);       /* #f5f4ef Surface Card */
  --color-surface-hover: oklch(0.945 0.012 85); /* #eee9e0 Card Hover */
  --color-border: oklch(0.880 0.015 85);        /* #dfdcce Hairline Border */
  --color-border-focus: oklch(0.450 0.180 250); /* #2a6fdb Focus Outline */

  /* 30% Typographic Content & Neutrals */
  --color-text-primary: oklch(0.180 0.020 260);   /* #1a1e24 Deep Obsidian */
  --color-text-secondary: oklch(0.420 0.025 260); /* #525a66 Muted Text */
  --color-text-tertiary: oklch(0.600 0.020 260);  /* #8892a0 Subtitle / Meta */

  /* 10% Geometric Accents & Optimization Signals */
  --color-primal: oklch(0.550 0.180 240);         /* #1971c2 Primal Set Blue */
  --color-dual: oklch(0.580 0.220 340);           /* #c2255c Dual Space Magenta */
  --color-accent: oklch(0.620 0.180 145);         /* #2b8a3e Optimal Solution Emerald */
  --color-accent-hover: oklch(0.540 0.200 145);   /* #237032 Dark Emerald */
  --color-accent-subtle: oklch(0.950 0.040 145);  /* #ebfbee Light Emerald Tint */

  --color-warning: oklch(0.720 0.160 75);         /* #e67700 Suboptimality Gap Amber */
  --color-error: oklch(0.580 0.220 25);           /* #c92a2a Infeasible / Unbounded Red */
  --color-info: oklch(0.580 0.180 260);           /* #3b5bdb Theorem Callout Purple */

  /* Spacing Scale (4-pt base) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.50rem;  /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1.00rem;  /* 16px */
  --space-6: 1.50rem;  /* 24px */
  --space-8: 2.00rem;  /* 32px */
  --space-12: 3.00rem; /* 48px */
  --space-16: 4.00rem; /* 64px */

  /* Radii */
  --radius-sm: 4px;   /* Sliders, buttons, badges */
  --radius-md: 8px;   /* Canvas frames, widget containers */

  /* Elevation */
  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.05), 0 0 0 1px var(--color-border);
  --shadow-dropdown: 0 4px 12px rgba(0, 0, 0, 0.08), 0 0 0 1px var(--color-border);
}

/* Dark Mode (High-contrast geometric darkroom) */
[data-theme="dark"] {
  --color-bg: oklch(0.130 0.015 260);            /* #0d1117 Obsidian Slate */
  --color-surface: oklch(0.170 0.018 260);       /* #161b22 Surface Card */
  --color-surface-hover: oklch(0.210 0.022 260); /* #21262d Card Hover */
  --color-border: oklch(0.260 0.020 260);        /* #30363d Hairline Border */

  --color-text-primary: oklch(0.920 0.010 85);   /* #e6edf3 Off-White */
  --color-text-secondary: oklch(0.700 0.015 85); /* #8b949e Muted Slate */
  --color-text-tertiary: oklch(0.500 0.015 260); /* #484f58 Metadata */

  --color-primal: oklch(0.680 0.160 240);        /* #58a6ff Vivid Blue */
  --color-dual: oklch(0.720 0.180 340);          /* #f778ba Vivid Pink */
  --color-accent: oklch(0.720 0.180 145);        /* #3fb950 Electric Emerald */
  --color-accent-subtle: oklch(0.220 0.050 145);

  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.3), 0 0 0 1px var(--color-border);
}
```

---

## 4. The 8-State Interactive Component Discipline

Every interactive slider, toggle, step button, and canvas manipulator in the D3/Three.js widgets must define explicit styling for all **8 interactive states**:
`default` · `hover` · `focus-visible` · `active` · `disabled` · `loading` · `error` · `success`.

---

## 5. Anti-Patterns & De-Slop Prohibitions (NEVER LIST)

- ❌ **No Generic SaaS Blue/Purple Gradients**: Replaced by dedicated OKLCH geometric palette (Blue primal, Magenta dual, Emerald optimum).
- ❌ **No Italic Headings or Theorem Titles**: Headings are always upright roman (`font-style: normal`).
- ❌ **No Centered Numeric Table Columns**: Numbers are always right-aligned with `font-variant-numeric: tabular-nums`.
- ❌ **No Fabricated Performance Claims**: Real algorithm convergence rates with theoretical proofs and exact step logs.
- ❌ **No Hand-Drawn Fake Browser Chrome**: Clean `<figure>` containers and SVG/Canvas viewports only.
- ❌ **No Horizontal Mobile Overflow**: Non-negotiable `overflow-x: clip` verified at 320px, 375px, 414px, and 768px.

---

## 6. Hallmark Pre-Emit Quality Gate Stamp

Before delivering any visual or interactive update, verify against the 6 Hallmark Axes:
`/* Hallmark · pre-emit critique: Philosophy:5 Hierarchy:5 Execution:5 Specificity:5 Restraint:5 Variety:5 */`
