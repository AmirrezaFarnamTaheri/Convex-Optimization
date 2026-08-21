# Documentation Reading Guide

Start with the docs in this repository:

1. **`CURRICULUM.md`**: The course blueprint — learning graph, per-lecture specs, content-status audit, capstone spec, and prioritized roadmap.
2. **`PEDAGOGY.md`**: How lectures are built — concept pipeline, cognitive-load rules, analogy registry, callout taxonomy, audit checklists.
3. **`NOTATION.md`**: The course-wide symbol standard (sign conventions, layout conventions, code↔math naming, reserved-letter disambiguation).
4. **`ASSESSMENT.md`**: Problem-bank architecture — taxonomy, tiers, per-lecture targets, solution-key standard, rubrics, solved exemplars.
5. **`WIDGETS.md`**: Interactive-widget architecture, audited inventory, design merge bar, and build backlog.
6. **`REFERENCES.md`**: Canonical bibliography, per-lecture Boyd & Vandenberghe mapping, citation rules.
7. **`SETUP.md`**: How to run the site locally for development/testing.
8. **`IMAGE_SOURCES.md`**: Notes about image provenance and planned additions.

Authoring conventions and quality invariants for contributors live in the repo-root **`CLAUDE.md`**; the six docs above are its normative companions.

### Useful scripts

- `verify_site.py`: Checks that **all local** `href`/`src` references across pages resolve (lectures + widgets).
- `tools/normalize_project.py`: Normalizes lecture shell markup and cleans up common widget-page path issues.
