import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LIB_REL = "static/lib" # Path to lib from root

# Mappings for HTML files
# Regex pattern -> (library name, file path inside lib)
# We will construct the relative path dynamically.
HTML_REPLACEMENTS = [
    (r'https://cdn\.jsdelivr\.net/npm/katex@[\d\.]+/dist/katex\.min\.js', 'katex/katex.min.js'),
    (r'https://cdn\.jsdelivr\.net/npm/katex@[\d\.]+/dist/contrib/auto-render\.min\.js', 'katex/contrib/auto-render.min.js'),
    (r'https://cdn\.jsdelivr\.net/npm/katex@[\d\.]+/dist/katex\.min\.css', 'katex/katex.min.css'),
    (r'https://cdnjs\.cloudflare\.com/ajax/libs/prism/[\d\.]+/prism\.min\.js', 'prism/prism.min.js'),
    (r'https://cdnjs\.cloudflare\.com/ajax/libs/prism/[\d\.]+/themes/prism\.min\.css', 'prism/themes/prism.min.css'),
    (r'https://cdnjs\.cloudflare\.com/ajax/libs/prism/[\d\.]+/components/prism-python\.min\.js', 'prism/components/prism-python.min.js'),
    (r'https://cdn\.jsdelivr\.net/pyodide/v[\d\.]+/full/pyodide\.js', 'pyodide/pyodide.js'),
    # Handle both full and non-full if present
    (r'https://cdn\.jsdelivr\.net/pyodide/v[\d\.]+/pyodide\.js', 'pyodide/pyodide.js'), 
    # D3 (if used in script src, not module)
    (r'https://cdn\.jsdelivr\.net/npm/d3@7/dist/d3\.min\.js', 'd3/d3.min.js'),
    # Three.js
    (r'https://cdn\.jsdelivr\.net/npm/three@[\d\.]+/build/three\.min\.js', 'three/three.min.js'),
    # Marked
    (r'https://cdn\.jsdelivr\.net/npm/marked/marked\.min\.js', 'marked/marked.min.js'),
]

# Mappings for JS files (ES Modules)
# These are relative to the JS file location. 
# Most JS files are in static/js or topics/.../widgets/js
# We need to calculate relative path to static/lib.
JS_REPLACEMENTS = [
    (r'https://cdn\.jsdelivr\.net/npm/d3@7/\+esm', 'd3/d3.esm.js'),
    (r'https://cdn\.jsdelivr\.net/npm/d3-polygon@3/\+esm', 'd3/d3-polygon.esm.js'),
    (r'https://cdn\.jsdelivr\.net/npm/three@[\d\.]+/build/three\.module\.js', 'three/three.module.js'),
    (r'https://cdn\.jsdelivr\.net/npm/three@[\d\.]+/examples/jsm/controls/OrbitControls\.js', 'three/examples/jsm/controls/OrbitControls.js'),
]

def get_relative_lib_path(file_path):
    """Returns the relative path string from file_path to static/lib"""
    # file_path is absolute or relative to cwd.
    # We want path from file_dir to PROJECT_ROOT/static/lib
    
    file_dir = file_path.parent
    lib_dir = PROJECT_ROOT / LIB_REL
    
    try:
        rel_path = os.path.relpath(lib_dir, file_dir)
        return rel_path.replace("\\", "/") # Ensure forward slashes for web
    except ValueError:
        return None # Different drives on Windows? Unlikely here.

def process_html(file_path):
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    rel_lib = get_relative_lib_path(file_path)
    
    for pattern, local_file in HTML_REPLACEMENTS:
        # Check if pattern exists
        if re.search(pattern, content):
            replacement = f"{rel_lib}/{local_file}"
            content = re.sub(pattern, replacement, content)
            
    if content != original_content:
        print(f"Updating HTML: {file_path.relative_to(PROJECT_ROOT)}")
        file_path.write_text(content, encoding='utf-8')

def process_js(file_path):
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    rel_lib = get_relative_lib_path(file_path)
    
    # Special case for pyodide-manager.js
    if file_path.name == "pyodide-manager.js":
        # Replace indexURL
        # old: indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/'
        pattern = r"indexURL:\s*['\"]https://cdn\.jsdelivr\.net/pyodide/[^'\"]+['\"]"
        # We want: indexURL: new URL('../lib/pyodide/', import.meta.url).href
        # rel_lib should be "../lib" for static/js
        replacement = f"indexURL: new URL('{rel_lib}/pyodide/', import.meta.url).href"
        content = re.sub(pattern, replacement, content)

    # Standard imports
    for pattern, local_file in JS_REPLACEMENTS:
        if re.search(pattern, content):
            replacement = f"{rel_lib}/{local_file}"
            content = re.sub(pattern, replacement, content)
            
    # Handle marked.js dynamic load in notes-widget.js
    if file_path.name == "notes-widget.js":
         pattern = r"script\.src = 'https://cdn\.jsdelivr\.net/npm/marked/marked\.min\.js';"
         replacement = f"script.src = '{rel_lib}/marked/marked.min.js';" # This relies on notes-widget being in static/js
         # Actually notes-widget.js is in static/js. If it runs in index.html (root), relative path is static/lib...
         # But wait, script.src in JS assigns the path relative to the PAGE, not the script.
         # This is tricky.
         # If notes-widget.js is included in topics/01/index.html, path should be ../../static/lib
         # If included in index.html, path is static/lib.
         # Best way: Use an absolute-ish path or detect root?
         # Or use import.meta.url to find the script location, then find lib relative to that.
         # Since notes-widget.js is likely NOT a module (just a script), we can't use import.meta.
         # But the file says `class NotesWidget`. It might be loaded as module?
         # In index.html: <script src="static/js/notes-widget.js"></script> -> standard script.
         # In this case, we might need a global config for LIB_PATH, or just assume it works if we use a relative path from the page.
         # BUT the page depth varies.
         # Hack: Check if `window.LIB_PATH` is defined, else guess?
         # Or simpler: Just leave marked as CDN? No, user wants offline.
         # We can try to use a function to get the root path.
         pass # Skipping manual replace here, relying on manual fix or global var strategy if needed.
         # Let's try to replace it with a relative path assuming it resolves from the HTML. 
         # The `rel_lib` calculated here is relative to the JS file. 
         # If we use `import.meta.url` (if module), we are good. 
         # If not, we have a problem.
         # notes-widget.js seems to be a standard script.
         # We'll fix notes-widget.js manually.

    if content != original_content:
        print(f"Updating JS: {file_path.relative_to(PROJECT_ROOT)}")
        file_path.write_text(content, encoding='utf-8')

def main():
    # Walk through all files
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Skip hidden/tools
        if ".git" in root or "tools" in root or "node_modules" in root:
            continue
            
        root_path = Path(root)
        
        for file in files:
            file_path = root_path / file
            if file.endswith(".html"):
                process_html(file_path)
            elif file.endswith(".js"):
                process_js(file_path)

if __name__ == "__main__":
    main()

