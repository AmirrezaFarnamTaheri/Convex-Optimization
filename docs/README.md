# Documentation Reading Guide

Start with the docs in this repository:

1. **`CURRICULUM.md`**: The course blueprint — learning graph, per-lecture objectives, assessments, capstone spec, and maintenance roadmap.
2. **`SETUP.md`**: How to run the site locally for development/testing.
3. **`IMAGE_SOURCES.md`**: Notes about image provenance and planned additions.

Authoring conventions and quality invariants for contributors live in the repo-root **`CLAUDE.md`**.

### Useful scripts

- `verify_site.py`: Checks that **all local** `href`/`src` references across pages resolve (lectures + widgets).
- `tools/normalize_project.py`: Normalizes lecture shell markup and cleans up common widget-page path issues.
