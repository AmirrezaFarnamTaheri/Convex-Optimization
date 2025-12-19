import re

filepath = "topics/01-linear-algebra-advanced/index.html"

with open(filepath, "r") as f:
    content = f.read()

# Extract exercises section
start_marker = '<section class="section-card" id="section-exercises">'
end_marker = '<section class="section-card" id="section-readings">'

start_pos = content.find(start_marker)
end_pos = content.find(end_marker)

if start_pos == -1 or end_pos == -1:
    print("Could not find exercises section markers.")
    exit(1)

exercises_content = content[start_pos:end_pos]

# Find all exercise headers like <h3>P1.X — Title</h3>
# We want to renumber them sequentially starting from P1.1

# We will use a callback to replace the numbers
counter = 1

def replace_header(match):
    global counter
    # match.group(0) is the whole h3 tag
    # match.group(1) is the number "1.X"
    # match.group(2) is the rest of the title

    # regex used: <h3>P1\.(\d+)(.*?)</h3>

    old_num = match.group(1)
    rest = match.group(2)

    new_header = f"<h3>P1.{counter}{rest}</h3>"
    counter += 1
    return new_header

new_exercises_content = re.sub(r'<h3>P1\.(\d+)(.*?)</h3>', replace_header, exercises_content)

new_content = content[:start_pos] + new_exercises_content + content[end_pos:]

with open(filepath, "w") as f:
    f.write(new_content)

print(f"Renumbered {counter-1} exercises.")
