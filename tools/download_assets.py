import os
import requests
import json
import re
from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).parent.parent
LIB_DIR = PROJECT_ROOT / "static" / "lib"
LIB_DIR.mkdir(parents=True, exist_ok=True)

# Configuration
PYODIDE_VERSION = "v0.26.4"
KATEX_VERSION = "0.16.9"
PRISM_VERSION = "1.29.0"

def download_file(url, dest_path):
    if dest_path.exists():
        print(f"Skipping {dest_path.name} (already exists)")
        return
    
    print(f"Downloading {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def setup_katex():
    base_url = f"https://cdn.jsdelivr.net/npm/katex@{KATEX_VERSION}/dist"
    dest_dir = LIB_DIR / "katex"
    
    # Core files
    files = [
        "katex.min.js",
        "katex.min.css",
        "contrib/auto-render.min.js"
    ]
    
    for f in files:
        download_file(f"{base_url}/{f}", dest_dir / f)

    # Fonts - Parse CSS to find them or just download common ones
    # KaTeX fonts are standard.
    fonts = [
        "KaTeX_AMS-Regular.woff2",
        "KaTeX_Caligraphic-Bold.woff2",
        "KaTeX_Caligraphic-Regular.woff2",
        "KaTeX_Fraktur-Bold.woff2",
        "KaTeX_Fraktur-Regular.woff2",
        "KaTeX_Main-Bold.woff2",
        "KaTeX_Main-BoldItalic.woff2",
        "KaTeX_Main-Italic.woff2",
        "KaTeX_Main-Regular.woff2",
        "KaTeX_Math-BoldItalic.woff2",
        "KaTeX_Math-Italic.woff2",
        "KaTeX_SansSerif-Bold.woff2",
        "KaTeX_SansSerif-Italic.woff2",
        "KaTeX_SansSerif-Regular.woff2",
        "KaTeX_Script-Regular.woff2",
        "KaTeX_Size1-Regular.woff2",
        "KaTeX_Size2-Regular.woff2",
        "KaTeX_Size3-Regular.woff2",
        "KaTeX_Size4-Regular.woff2",
        "KaTeX_Typewriter-Regular.woff2"
    ]
    
    font_dir = dest_dir / "fonts"
    for font in fonts:
        download_file(f"{base_url}/fonts/{font}", font_dir / font)

def setup_prism():
    base_url = f"https://cdnjs.cloudflare.com/ajax/libs/prism/{PRISM_VERSION}"
    dest_dir = LIB_DIR / "prism"
    
    files = [
        "prism.min.js",
        "themes/prism.min.css",
        "components/prism-python.min.js"
    ]
    
    for f in files:
        download_file(f"{base_url}/{f}", dest_dir / f)

def setup_d3():
    # D3 v7 ESM
    # We need the ESM version because the code uses 'import * as d3'
    # Fetching from the +esm endpoint returns the bundled ESM code.
    url = "https://cdn.jsdelivr.net/npm/d3@7/+esm"
    download_file(url, LIB_DIR / "d3" / "d3.esm.js")

    # D3 Polygon
    download_file("https://cdn.jsdelivr.net/npm/d3-polygon@3/+esm", LIB_DIR / "d3" / "d3-polygon.esm.js")


def setup_three():
    # OrbitControls
    base_url = "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/jsm/controls"
    dest_dir = LIB_DIR / "three" / "examples" / "jsm" / "controls"
    download_file(f"{base_url}/OrbitControls.js", dest_dir / "OrbitControls.js")
    
    # Three.min.js (for non-module script tags)
    download_file("https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js", LIB_DIR / "three" / "three.min.js")

def setup_marked():
    download_file("https://cdn.jsdelivr.net/npm/marked/marked.min.js", LIB_DIR / "marked" / "marked.min.js")

def setup_pyodide():
    base_url = f"https://cdn.jsdelivr.net/pyodide/{PYODIDE_VERSION}/full"
    dest_dir = LIB_DIR / "pyodide"
    
    # Core files
    core_files = [
        "pyodide.js",
        "pyodide.asm.js",
        "pyodide.asm.wasm",
        "pyodide-lock.json", # New lock file
        "python_stdlib.zip"
    ]
    
    for f in core_files:
        download_file(f"{base_url}/{f}", dest_dir / f)
        
    # Parse pyodide-lock.json to find numpy and scipy
    try:
        lock_path = dest_dir / "pyodide-lock.json"
        if not lock_path.exists():
            print("pyodide-lock.json not found, skipping package download")
            return

        with open(lock_path, "r") as f:
            data = json.load(f)
            
        packages_to_install = ["numpy", "scipy", "micropip", "packaging", "matplotlib"] # added matplotlib just in case
        
        queue = packages_to_install[:]
        seen = set()
        
        while queue:
            pkg_name = queue.pop(0)
            if pkg_name in seen:
                continue
            seen.add(pkg_name)
            
            # Lock file structure: "packages" -> key is import name or similar? 
            # Usually key is "numpy" or "numpy-1.2.3..."
            # Let's search for the package entry.
            
            pkg_info = None
            # Direct lookup
            if pkg_name in data["packages"]:
                pkg_info = data["packages"][pkg_name]
            else:
                # Find by name field
                for p in data["packages"].values():
                    if p.get("name") == pkg_name:
                        pkg_info = p
                        break
            
            if not pkg_info:
                print(f"Warning: {pkg_name} not found in pyodide-lock.json")
                continue
                
            file_name = pkg_info["file_name"]
            download_file(f"{base_url}/{file_name}", dest_dir / file_name)
            
            # Add dependencies
            for dep in pkg_info.get("depends", []):
                if dep not in seen:
                    queue.append(dep)
                    
    except Exception as e:
        print(f"Error processing Pyodide packages: {e}")

if __name__ == "__main__":
    print("Starting asset download...")
    setup_katex()
    setup_prism()
    setup_d3()
    setup_three()
    setup_marked()
    setup_pyodide()
    print("Download complete.")

