import os
import re
from typing import List, Tuple

def iter_html_paths(root: str) -> List[str]:
    pages: List[str] = []
    topics_dir = os.path.join(root, "topics")
    if os.path.isdir(topics_dir):
        for topic in sorted(os.listdir(topics_dir)):
            topic_index = os.path.join(topics_dir, topic, "index.html")
            if os.path.exists(topic_index):
                pages.append(topic_index)
    return pages

def check_file(filepath: str) -> List[str]:
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check Title Format
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1)
        if not re.match(r'^\d{2}\. .* — Convex Optimization$', title):
            errors.append(f"Title format incorrect: '{title}'")
    else:
        errors.append("Missing <title> tag")

    # Check Date Format (YYYY-MM-DD)
    if not re.search(r'Date: \d{4}-\d{2}-\d{2}', content):
        errors.append("Missing or incorrect Date format (expected 'Date: YYYY-MM-DD')")

    # Check Sections
    if "Learning Objectives" not in content:
        errors.append("Missing 'Learning Objectives' section")

    # Check Math Delimiters
    # This is a heuristic. We expect even number of $$ and \( \) pairs.
    num_double_dollar = content.count('$$')
    if num_double_dollar % 2 != 0:
        errors.append(f"Odd number of '$$' delimiters: {num_double_dollar}")

    # Common Typos
    typos = {
        "teh": "the",
        "recieve": "receive",
        "adress": "address",
        "occured": "occurred",
        "seperate": "separate",
        "funtion": "function",
        "matrixes": "matrices",
        "optmization": "optimization",
        "constaint": "constraint",
        "Constraint constraint": "Constraint",
        "Constraints Constraints": "Constraints"
    }

    for typo, correction in typos.items():
        # strict word boundary check to avoid partial matches
        matches = re.finditer(r'\b' + re.escape(typo) + r'\b', content, re.IGNORECASE)
        for match in matches:
            start = max(0, match.start() - 20)
            end = min(len(content), match.end() + 20)
            context = content[start:end].replace('\n', ' ')
            errors.append(f"Potential typo: '{typo}' -> '{correction}' in context: ...{context}...")

    # Repeated words (ignoring common math symbols if possible)
    # We ignore single letters to avoid flagging 'A A' in 'A A^T'
    repeated_words = re.finditer(r'\b([a-zA-Z]{2,})\s+\1\b', content, re.IGNORECASE)
    for match in repeated_words:
        word = match.group(1)
        # Filter out likely false positives
        if word.lower() in ['long', 'that', 'had', 'is']: # "long long" type, "that that"
             pass # might be valid, but worth checking. "that that" is usually an error.

        start = max(0, match.start() - 20)
        end = min(len(content), match.end() + 20)
        context = content[start:end].replace('\n', ' ')
        errors.append(f"Repeated word: '{word} {word}' in context: ...{context}...")

    return errors

def main():
    root = "."
    pages = iter_html_paths(root)

    total_errors = 0
    for page in pages:
        errors = check_file(page)
        if errors:
            print(f"File: {page}")
            for error in errors:
                print(f"  - {error}")
            print()
            total_errors += len(errors)

    if total_errors == 0:
        print("No obvious errors found!")
    else:
        print(f"Found {total_errors} potential issues.")

if __name__ == "__main__":
    main()
