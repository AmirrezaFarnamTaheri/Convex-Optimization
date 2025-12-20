import re
import sys

def process_latex(latex_content):
    # Variables to boldify
    targets = ['x', 'y', 'z', 'u', 'v', 'w', 'b', 'p', 'q', 'r', 'g']

    # Tokenize by backslash commands to avoid replacing inside commands like \max, \frac
    tokens = re.split(r'(\\[a-zA-Z]+)', latex_content)

    # Regex Explanation:
    # (?<![\\a-z]) : Lookbehind. Match if NOT preceded by a lowercase letter or backslash.
    #                This allows 'Ax' (preceded by 'A'), ' x' (space), '(x' (paren).
    #                This avoids 'max' (preceded by 'a'), '\x' (preceded by \), 'convex' (preceded by 'e').
    #                Also avoids 'dx' (preceded by 'd').
    #
    # (targets)    : The variable to match.
    #
    # (?![a-zA-Z]) : Lookahead. Match if NOT followed by any letter.
    #                Avoids 'xi' (if x was target), 'xp'.
    #
    # (?!_)        : Lookahead. Match if NOT followed by underscore.
    #                Avoids 'x_i', 'x_1'.
    #
    # (?!\()       : Lookahead. Match if NOT followed by open parenthesis.
    #                Avoids 'f(x)' replacing f (if f was target), 'p(t)'.
    #                Note: This does NOT prevent replacing x in f(x).

    target_pattern = r'(?<![\\a-z])(' + '|'.join(targets) + r')(?![a-zA-Z])(?!_)(?!\()'

    new_tokens = []
    for token in tokens:
        if token.startswith('\\'):
            new_tokens.append(token)
        else:
            # Check for double bolding prevention (e.g. \mathbf{x})
            # The token is text. If the previous token was \mathbf, and this token starts with {x}, we might double bold.
            # But tokens are split by commands. \mathbf is a token. {x} is the next token.
            # We are processing the text token `{x}`.
            # Inside `{x}`, `x` is preceded by `{`. `{` is not `[\\a-z]`. So it matches.
            # Result `{\mathbf{x}}`.
            # This results in `\mathbf{\mathbf{x}}`.
            # We can try to avoid this by looking at context or just accepting it.
            # To fix properly, we'd need a full latex parser.
            # For now, let's just use the regex. Double bold is acceptable visual output.

            new_token = re.sub(target_pattern, r'\\mathbf{\1}', token)
            new_tokens.append(new_token)

    return ''.join(new_tokens)

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern to find math blocks: $$...$$, $...$, \[...\], \(...\)
    pattern = r'(\$\$(?:(?!\$\$).)*?\$\$)|(\$(?:(?!\$).)*?\$)|(\\\[(?:(?!\\\]).)*?\\\])|(\\\((?:.|\n)*?\\\))'

    def replacer(m):
        text = m.group(0)
        if text.startswith('$$'):
            inner = text[2:-2]
            return f'$${process_latex(inner)}$$'
        elif text.startswith('$'):
            inner = text[1:-1]
            return f'${process_latex(inner)}$'
        elif text.startswith('\\['):
            inner = text[2:-2]
            return f'\\[{process_latex(inner)}\\]'
        elif text.startswith('\\('):
            inner = text[2:-2]
            return f'\\({process_latex(inner)}\\)'
        return text

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 bold_vectors.py <filepath>")
        sys.exit(1)
    process_file(sys.argv[1])
