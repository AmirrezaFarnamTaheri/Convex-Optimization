import os
from bs4 import BeautifulSoup
import re

def audit_directory(root_dir):
    print(f"# Lecture Structure Audit\n")
    print(f"Generated from: `{root_dir}`\n")

    topics_dir = os.path.join(root_dir, 'topics')
    if not os.path.exists(topics_dir):
        print("Error: 'topics' directory not found.")
        return

    # Sort directories numerically if possible, otherwise alphabetically
    dirs = sorted(os.listdir(topics_dir))

    for dirname in dirs:
        dirpath = os.path.join(topics_dir, dirname)
        if not os.path.isdir(dirpath):
            continue

        index_path = os.path.join(dirpath, 'index.html')
        if not os.path.exists(index_path):
            continue

        audit_file(index_path, dirname)

def audit_file(filepath, dirname):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"## Error reading {dirname}: {e}\n")
        return

    # Extract Title
    title_tag = soup.select_one('.lecture-header h1')

    # Fallback for topics 10-15 which might use different structure
    if not title_tag:
        title_tag = soup.select_one('.section-card h1')

    title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

    print(f"## [{dirname}] {title}")
    print(f"*File: `topics/{dirname}/index.html`*\n")

    # Sections and Subsections
    print("### Sections")
    # Broaden selection for sections
    sections = soup.select('.section-card')
    for section in sections:
        h2 = section.find('h2')
        if h2:
            print(f"- **{h2.get_text(strip=True)}**")
            # Subsections (h3)
            h3s = section.find_all('h3')
            for h3 in h3s:
                print(f"  - {h3.get_text(strip=True)}")

    print("")

    # Key Elements Counts
    print("### Key Elements")
    element_types = {
        '.theorem-box': 'Theorems/Definitions',
        '.proof-box': 'Proofs',
        '.example': 'Examples',
        '.problem': 'Exercises',
        '.widget-container': 'Interactive Widgets'
    }

    # Check if elements are found, otherwise try to search H3s for patterns if classes are missing
    # (Handling unstructured files 10-15)

    for selector, name in element_types.items():
        elements = soup.select(selector)
        count = len(elements)

        # If no elements found by class, but it's an "Example" or "Exercise" section,
        # we might want to count H3s inside specific sections.
        # But for now, just report what is found by class.

        if count > 0:
            print(f"- **{name}**: {count}")
            # Optional: Print titles if they exist (usually h3 or h4 inside)
            for el in elements:
                title_el = el.find(['h3', 'h4'])
                if title_el:
                    print(f"  - {title_el.get_text(strip=True)}")

        # Heuristic for unstructured "Example Problems" sections
        if count == 0 and name == 'Examples':
             example_section = soup.find(lambda tag: tag.name == 'h2' and 'Example Problems' in tag.get_text())
             if example_section:
                 parent = example_section.find_parent('section')
                 if parent:
                     examples = parent.find_all('h3')
                     if examples:
                         print(f"- **{name} (Heuristic)**: {len(examples)}")
                         for ex in examples:
                             print(f"  - {ex.get_text(strip=True)}")

    print("")

    # Link Validation (Local Relative Links)
    print("### Broken Links Check")
    links = soup.find_all('a', href=True)
    broken_links = []

    base_dir = os.path.dirname(filepath)

    for link in links:
        href = link['href']
        if href.startswith('#') or href.startswith('http') or href.startswith('mailto:') or href.startswith('javascript:'):
            continue

        # Resolve relative path
        try:
            target_path = os.path.normpath(os.path.join(base_dir, href))
            # Remove query params or anchors for file check
            target_file = target_path.split('#')[0].split('?')[0]

            if not os.path.exists(target_file):
                broken_links.append(href)
        except Exception as e:
            broken_links.append(f"{href} (Error: {e})")

    if broken_links:
        for bl in broken_links:
            print(f"- [FAILED] `{bl}`")
    else:
        print("- All local links appear valid.")

    print("\n---\n")

if __name__ == "__main__":
    audit_directory('.')
