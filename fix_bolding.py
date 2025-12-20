import re
import sys

def fix_l00(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix 'r' in Section 2 (Rank-Nullity) where it is a scalar (count/dimension)
    # Heuristic: Replace \mathbf{r} with r if it appears in lines 250-320 (approx)
    # Better: Replace \mathbf{r} with r if followed by ' vectors' or '= n' or 'Indices'?
    # Let's just target the specific occurrences in the text we saw.

    # Contexts:
    # "We add \mathbf{r} = n-k vectors"
    # "vectors \{Aw_1, \dots, Aw_\mathbf{r}\}" -> subscript r should not have been bolded!
    # Wait, my script avoids `_`.
    # But `Aw_\mathbf{r}`. `r` is NOT immediately after `_`. `w_` then `\mathbf{r}`?
    # No, LaTeX is `w_\mathbf{r}` or `w_{\mathbf{r}}`.
    # Original was `w_r`. My script saw `r`. Is `r` preceded by `_`?
    # `w_r`. Yes.
    # So `r` should NOT have been bolded.
    # Why was it bolded?
    # Grep output: `Aw_\mathbf{r}`.
    # Maybe `_` is not immediately before `r` in the token stream?
    # `re.split` by commands. `Aw_r` -> `Aw_r` (text).
    # `(?<![\\a-z])` check. `_` is not `[\\a-z]`.
    # `(?!_)`. `r` is not followed by `_`.
    # But lookbehind `(?<!_)` was NOT in my script!
    # My script had `(?<![\\a-z])`. `_` allows match.
    # I missed the lookbehind for `_`! I only had lookahead `(?!_)`.

    # Correction: I need to unbold vars that are subscripts.
    # `_\mathbf{x}` -> `_x`.
    # `_{\mathbf{x}}` -> `_{x}`.
    # `^\mathbf{x}` -> `^x` (if scalar exponent).

    # General Fixes:
    # 1. Unbold subscripts: `_(\{[^}]*\}|[a-zA-Z0-9\\])\mathbf{([a-zA-Z])}` -> `_\1\2`?
    # Easier: `_\mathbf{r}` -> `_r`.
    # `_\mathbf{p}` -> `_p`.
    # `Aw_\mathbf{r}` -> `Aw_r`.

    content = re.sub(r'_\s*\\mathbf\{([a-zA-Z])\}', r'_\1', content)
    content = re.sub(r'\^\s*\\mathbf\{([a-zA-Z])\}', r'^\1', content) # Exponents too?

    # Fix 'r' as scalar in L00
    # "We add \mathbf{r} = n-k"
    content = content.replace(r'We add \mathbf{r} = n-k', r'We add r = n-k')
    # "sum_{j=1}^{\mathbf{r}}" -> "sum_{j=1}^{r}"
    content = content.replace(r'^{\mathbf{r}}', r'^{r}')
    content = content.replace(r'^\mathbf{r}', r'^r')

    # "r vectors"
    content = content.replace(r'\mathbf{r} vectors', r'r vectors')
    content = content.replace(r'these \mathbf{r} vectors', r'these r vectors')

    # "dimension ... is exactly \mathbf{r}"
    content = content.replace(r'exactly \mathbf{r}', r'exactly r')

    # "defined \mathbf{r} = n"
    content = content.replace(r'defined \mathbf{r} = n', r'defined r = n')

    # "equation \mathbf{r} + k = n"
    content = content.replace(r'\mathbf{r} + k = n', r'r + k = n')

    with open(filepath, 'w') as f:
        f.write(content)

def fix_l01(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Revert all \mathbf{r} to r (Rank is always scalar r in L01)
    content = content.replace(r'\mathbf{r}', r'r')

    # 2. Revert \mathbf{p}, \mathbf{q} in Norm contexts
    # Subscripts
    content = re.sub(r'_\s*\\mathbf\{p\}', r'_p', content)
    content = re.sub(r'_\s*\\mathbf\{q\}', r'_q', content)

    # Exponents
    content = re.sub(r'\^\s*\\mathbf\{p\}', r'^p', content)
    content = re.sub(r'\^\s*\\mathbf\{q\}', r'^q', content)

    # Inequalities and Algebra involving p, q (scalars)
    # "1 < \mathbf{p} < \infty"
    content = content.replace(r'1 < \mathbf{p} < \infty', r'1 < p < \infty')
    # "\mathbf{p} + \mathbf{q}"? No, "1/\mathbf{p} + 1/\mathbf{q}"
    content = content.replace(r'1/\mathbf{p}', r'1/p')
    content = content.replace(r'1/\mathbf{q}', r'1/q')

    # "\mathbf{p}=\infty"
    content = content.replace(r'\mathbf{p}=\infty', r'p=\infty')
    content = content.replace(r'\mathbf{p}=1', r'p=1')
    content = content.replace(r'\mathbf{p}=2', r'p=2')

    # "\ell_\mathbf{p}"
    content = content.replace(r'\ell_\mathbf{p}', r'\ell_p')
    content = content.replace(r'\ell_\mathbf{q}', r'\ell_q')

    # Check for "\mathbf{p} - 1"
    content = content.replace(r'\mathbf{p}-1', r'p-1')
    content = content.replace(r'\mathbf{q}-1', r'q-1')

    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    fix_l00('topics/00-linear-algebra-basics/index.html')
    fix_l01('topics/01-linear-algebra-advanced/index.html')
