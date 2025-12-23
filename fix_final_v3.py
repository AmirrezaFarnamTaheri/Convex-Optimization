
import os
import re

def fix_l04():
    filepath = "topics/04-convex-sets-cones/index.html"
    with open(filepath, "r") as f:
        content = f.read()

    # Fix corruption: newline + otin -> \notin
    # We use regex to match whitespace including newline followed by otin
    content = re.sub(r'\s*\n\s*otin', r' \\notin', content)

    # Fix corruption: formfeed + orall -> \forall
    content = re.sub(r'\s*\f\s*orall', r' \\forall', content)
    # Also handle just "\n orall" if interpreted as newline
    content = re.sub(r'\s*\n\s*orall', r' \\forall', content)

    # Just in case: literal " \n otin" replacement
    content = content.replace(" \n otin", r" \notin")

    with open(filepath, "w") as f:
        f.write(content)
    print("Fixed L04 corruption.")

def fix_l05():
    filepath = "topics/05-convex-functions-basics/index.html"
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Domain Convexity (Insert after Section 1 header)
    domain_content = r"""
        <div class="insight">
          <h4>Why "Domain Convexity" is Mandatory</h4>
          <p>A common mistake is to check the inequality $f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$ without verifying that the domain is convex. If the domain is not convex, the inequality is meaningless because the convex combination might not even be in the domain.</p>
          <p><b>Example:</b> Let $f(x) = 0$ if $x \in \{0, 1\}$ and $\infty$ otherwise. The domain $\{0, 1\}$ is not convex. The inequality holds wherever defined, but $f$ is clearly not convex (its epigraph is not a convex set).</p>
        </div>
"""
    # Look for a good place. After "<h2>1. Definition and Basic Properties</h2>".
    # There is usually a <p> or <ul> after. Let's insert it after the H2 closing tag.
    if "Domain Convexity" not in content:
        content = content.replace("<h2>1. Definition and Basic Properties</h2>", "<h2>1. Definition and Basic Properties</h2>" + domain_content)

    # 2. Epigraph Patterns (Insert before Section 3)
    epigraph_content = r"""
        <div class="insight">
          <h4>Standard Epigraph Modeling Patterns</h4>
          <p>These are the "reflexes" for converting objectives to constraints:</p>
          <ul>
            <li><b>Maximum:</b> $\min \max_i f_i(x) \iff \min t \text{ s.t. } f_i(x) \le t \ \forall i$.</li>
            <li><b>Absolute Value:</b> $|u| \le t \iff -t \le u \le t$.</li>
            <li><b>Norms:</b> $\|Ax+b\| \le t$. For $\ell_2$, this is SOCP. For $\ell_1/\ell_\infty$, this is LP.</li>
            <li><b>Piecewise:</b> $f(x) = \max(f_1(x), f_2(x))$ becomes intersection of epigraphs.</li>
          </ul>
        </div>
"""
    if "Standard Epigraph Modeling Patterns" not in content:
        content = content.replace("<h2>3. First-Order Conditions", epigraph_content + "\n        <h2>3. First-Order Conditions")

    # 3. Log Barrier Hessian (Insert before Section 5)
    barrier_content = r"""
        <div class="example-box">
          <h4>Example: Log Barrier Hessian</h4>
          <p>Consider $f(x) = -\sum \log(b_i - a_i^\top x)$. The domain is the open polyhedron $\{x \mid Ax < b\}$.</p>
          <p>Gradient: $\nabla f(x) = \sum \frac{a_i}{b_i - a_i^\top x}$.</p>
          <p>Hessian: $\nabla^2 f(x) = \sum \frac{a_i a_i^\top}{(b_i - a_i^\top x)^2}$.</p>
          <p>Since each term $a_i a_i^\top$ is a rank-1 PSD matrix and coefficients are positive, the sum is PSD. Thus $f$ is convex.</p>
        </div>
"""
    if "Log Barrier Hessian" not in content:
        content = content.replace("<h2>5. Operations Preserving Convexity", barrier_content + "\n        <h2>5. Operations Preserving Convexity")

    with open(filepath, "w") as f:
        f.write(content)
    print("Fixed L05 content.")

if __name__ == "__main__":
    fix_l04()
    fix_l05()
