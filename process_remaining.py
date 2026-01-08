import re
import os
from bs4 import BeautifulSoup

def process_file(filepath, start_fig_num):
    print(f"Processing {filepath} starting at Figure {start_fig_num}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return start_fig_num

    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Clean Inline Styles
    tags_to_clean = ['div', 'figure', 'img']
    for tag_name in tags_to_clean:
        for tag in soup.find_all(tag_name):
            if tag.has_attr('style'):
                 # Check if it's a layout flex container before deleting all styles?
                 # In previous steps we replaced div style="display:flex..." with class="figure-group"
                 # Let's keep that logic if relevant, though mostly likely relevant for L05.
                 # For general cleanup, stripping style is what we want.
                 del tag['style']

            if tag_name == 'img':
                if tag.has_attr('width'): del tag['width']
                if tag.has_attr('height'): del tag['height']

    # 2. Renumber Figures
    current_fig_num = start_fig_num
    figures = soup.find_all('figure')

    for fig in figures:
        caption = fig.find('figcaption')
        if caption:
            # Robust replacement logic
            # We look for the figure label pattern.

            # Helper to recursively find and replace text
            def replace_in_node(node):
                nonlocal current_fig_num
                replaced = False

                # Check text content of this node
                if node.string:
                    # Regex for "Figure X" or "Figure X." or "Figure X:"
                    # We want to match "Figure" followed by digits, maybe punctuation
                    match = re.search(r'Figure\s+(\d+)', node.string)
                    if match:
                        new_string = re.sub(r'Figure\s+\d+', f"Figure {current_fig_num}", node.string, count=1)
                        if new_string != node.string:
                            node.replace_with(new_string)
                            return True

                # Recurse children
                if hasattr(node, 'children'):
                    for child in node.children:
                        if replace_in_node(child):
                            return True
                return False

            # Try to replace existing number
            found = replace_in_node(caption)

            if not found:
                # If no "Figure X" text found, prepend it
                prefix_text = f"Figure {current_fig_num}: "
                new_b_tag = soup.new_tag("b")
                new_b_tag.string = prefix_text

                # Insert at beginning of caption
                if caption.contents:
                    caption.insert(0, new_b_tag)
                else:
                    caption.append(new_b_tag)

            current_fig_num += 1

    # Save the modified HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Finished {filepath}. Next figure is {current_fig_num}.")
    return current_fig_num

if __name__ == "__main__":
    files = [
        "topics/10-approximation-fitting/index.html",
        "topics/11-statistical-estimation/index.html",
        "topics/12-geometric-problems/index.html",
        "topics/13-unconstrained-minimization/index.html",
        "topics/14-equality-constrained-minimization/index.html",
        "topics/15-interior-point-methods/index.html"
    ]

    next_fig = 42 # Starting after Lecture 09

    for filepath in files:
        if os.path.exists(filepath):
            next_fig = process_file(filepath, next_fig)
        else:
            print(f"Skipping {filepath} (not found)")
