# Setup

## Quick Start

1. **Run a local server** (required for module imports and widget assets):
   ```bash
   python -m http.server 8000
   ```
   (If `python` points to Python 2 on your system, use `python3` instead.)

2. **Open the site**:
   - Visit `http://localhost:8000`

## Why a Local Server?

Browsers block `fetch()` and module imports from `file://` URLs. Serving the site over HTTP avoids CORS issues and ensures widgets, JSON assets, and KaTeX render correctly.

## Sanity Checks

- LaTeX equations render (KaTeX).
- Widgets load without console errors.
- Navigation links resolve correctly.

If you see errors, check your browser console first—missing files or blocked requests are the most common causes.
