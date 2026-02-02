import os
import re

def check_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    errors = []

    # Check for Appendix (except L02)
    if "02-introduction" not in filepath:
        if '<section class="section-card" id="section-appendix">' not in content:
            errors.append("Missing Appendix section")

    # Check for Navigation (Prev/Next)
    if '<nav class="nav" role="navigation" aria-label="Lecture Navigation">' not in content:
        errors.append("Missing Navigation")

    # Check for Footer
    if '<footer class="site-footer">' not in content:
        errors.append("Missing Footer")

    return errors

topics_dir = "topics"
for root, dirs, files in os.walk(topics_dir):
    for file in files:
        if file == "index.html":
            path = os.path.join(root, file)
            errs = check_file(path)
            if errs:
                print(f"{path}: {errs}")
            else:
                pass # print(f"{path}: OK")
