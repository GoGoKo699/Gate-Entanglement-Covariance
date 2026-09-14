#!/usr/bin/env python3
"""Check the maintained reading route's portable Markdown math conventions, using only stdlib.

This is a source linter, not GitHub's renderer or a complete TeX parser. The
command inventory is deliberately conservative: review new commands before
extending it. Ordinary code examples are ignored; fenced math is checked.
Use GitHub's protected $`...`$ syntax for inline expressions and keep prose
words and hyphens outside, separated by spaces. A source check cannot prove
that a particular browser has rendered the resulting Markdown correctly.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
# Reviewed common MathJax commands used in the repository. This is a project policy,
# not a claim to enumerate every command supported or blocked by GitHub.
COMMANDS = set("""
Delta Gamma Omega Phi Pi alpha bar begin beta bigl bigr binom boldsymbol boxed cdots chi cos
cup dagger delta dim ell end eta exp frac gamma ge geq in infty int lambda langle ldots
le left leq lim limsup ln log longrightarrow mathbb mathbf mathcal mathop mathrm mid min mu ne nolimits omega
otimes overline partial phi pi pm prod propto psi quad qquad rangle rho right rm
sigma sim simeq sin sqrt sum tau text tfrac theta times to varepsilon widehat xi
""".split())
COMMAND = re.compile(r"\\([A-Za-z]+)")
TOKEN = re.compile(r"\\(?:[A-Za-z]+|[^\n])|\$\$|\$|[{}]")
# High-confidence formula fragments in this English-language reading route.
# This is not a complete detector for mathematics written in prose.
RAW_MATH = re.compile(
    r"(?<![\w/])(?:[A-Za-zΑ-Ωα-ω]|eta|rho|Gamma|delta)(?:\\?[_^])[{(\w+-]"
    r"|\b(?:sqrt|min|max|exp)\("
    r"|[)\]]\^[{(\w+-]"
    r"|(?<![\w/])[A-Za-zΑ-Ωα-ω]\s*(?:=|>=|<=|≥|≤)\s*[A-Za-zΑ-Ωα-ω0-9(]"
    r"|[Α-Ωα-ω†²³⁻≥≤]"
    r"|\\[A-Za-z]+"
)
# Both inline forms are documented by GitHub. The protected form is this
# project's convention, since it isolates TeX from ordinary Markdown parsing:
# https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
ATTACHED_PROSE = re.compile(r"[\w\-‐‑‒–—]", re.UNICODE)


def inline_errors(text: str, start: int, end: int) -> list[str]:
    """Check original delimiters and boundaries, before code masking loses backticks."""
    errors = []
    if not (text.startswith("$`", start) and text[end - 2:end] == "`$"):
        errors.append("use GitHub's protected $`...`$ delimiters for inline math")
    before, after = text[max(0, start - 1):start], text[end:end + 1]
    if ATTACHED_PROSE.fullmatch(before) or ATTACHED_PROSE.fullmatch(after):
        errors.append("inline math is attached to prose or a hyphen; rephrase with spaces, such as 'degree $`k`$'")
    return errors


def mask_code(text: str) -> str:
    """Keep offsets, newlines and math; blank ordinary fenced/inline code."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})([^\n]*)", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                lines.append(("$$" if fence[2] else "").ljust(len(line.rstrip("\n"))) + ("\n" if line.endswith("\n") else ""))
                fence = None
            else:
                lines.append(line if fence[2] else re.sub(r"[^\n]", " ", line))
        elif marker:
            fence = (marker[1][0], len(marker[1]), marker[2].strip() == "math")
            lines.append(("$$" if fence[2] else "").ljust(len(line.rstrip("\n"))) + ("\n" if line.endswith("\n") else ""))
        else:
            # GitHub's $`...`$ math syntax must survive ordinary code masking.
            pattern = r"\$`[^\n]*?`\$|(`+)(?!`)[^\n]*?(?<!`)\1(?!`)"
            lines.append(re.sub(pattern, lambda m: m[0].replace("`", " ") if m[0].startswith("$`") else " " * len(m[0]), line))
    return "".join(lines)


def inspect(text: str) -> tuple[list[str], list[tuple[int, str, bool]]]:
    """Return source errors and (line, TeX, display) expressions."""
    source = mask_code(text)
    errors, expressions = [], []
    line_at = lambda offset: source.count("\n", 0, offset) + 1
    for legacy in re.finditer(r"(?<!\\)\\[\[\]()]", source):
        errors.append(f"line {line_at(legacy.start())}: use $`...`$ or fenced math instead of {legacy[0]}")
    for number, line in enumerate(source.splitlines(), 1):
        if re.match(r"^ {0,3}#{1,6}\s", line) and "$" in line:
            errors.append(f"line {number}: use a plain-text heading and put the equation in the body")
    opening = None
    math_spans = []
    for token in TOKEN.finditer(source):
        if token[0] not in {"$", "$$"}:
            continue
        if opening is None:
            opening = token
        elif opening[0] != token[0]:
            errors.append(f"line {line_at(token.start())}: mixed inline/display math delimiters")
        else:
            tex = source[opening.end():token.start()]
            line = line_at(opening.start())
            if token[0] == "$" and "\n" in tex:
                errors.append(f"line {line}: inline math crosses a line; use display math")
            if token[0] == "$":
                errors.extend(f"line {line}: {error}" for error in inline_errors(text, opening.start(), token.end()))
            expressions.append((line, tex, token[0] == "$$"))
            math_spans.append((opening.start(), token.end()))
            opening = None
    if opening is not None:
        errors.append(f"line {line_at(opening.start())}: unclosed math delimiter {opening[0]}")
    prose = list(source)
    for start, end in math_spans:
        prose[start:end] = ["\n" if c == "\n" else " " for c in source[start:end]]
    prose = "".join(prose)
    # Destinations, bare URLs and filenames are not mathematical notation.
    blank = lambda m: re.sub(r"[^\n]", " ", m[0])
    prose = re.sub(r"\]\([^\n)]*\)|https?://\S+|\b[\w./-]+\.(?:md|py|json|npz|png|svg|txt)\b", blank, prose)
    for match in RAW_MATH.finditer(prose):
        errors.append(f"line {line_at(match.start())}: formula fragment {match[0]!r} outside math; use $`...`$ or fenced math")
    for line, tex, _ in expressions:
        for token in TOKEN.finditer(tex):
            command = COMMAND.fullmatch(token[0])
            if command and command[1] not in COMMANDS:
                detail = "use \\mathop{\\mathrm{NAME}}\\nolimits" if command[1] == "operatorname" else "review compatibility before adding it to COMMANDS"
                errors.append(f"line {line}: unreviewed math command {command[0]}; {detail}")
        depth = 0
        for token in TOKEN.finditer(tex):
            if token[0] == "{":
                depth += 1
            elif token[0] == "}":
                depth -= 1
                if depth < 0:
                    break
        if depth:
            errors.append(f"line {line}: unbalanced TeX grouping braces")
    return errors, expressions


def markdown_paths(root: Path) -> list[Path]:
    # Check every reader page, including detailed studies and exact checks.
    # Preserved source archives are outside these maintained directories.
    paths = set(root.glob("*.md"))
    for directory in ("docs", "theory", "studies", "checks"):
        paths.update((root / directory).rglob("*.md"))
    return sorted(paths)


def self_test() -> None:
    # Exercise the actual GitHub backtick delimiters, math fences, escaped
    # braces/dollars, and deliberate delimiter, command, grouping and heading failures.
    valid = "$`\\mathop{\\mathrm{Tr}}\\nolimits\\rho`$\n```math\n\\frac{1}{2}\\{x\\}\n```\n"
    assert not inspect(valid)[0]
    assert len(inspect(valid)[1]) == 2
    assert not inspect("`$\\operatorname{x}$`\n```tex\n$\\operatorname{x}$\n```\n")[0]
    for bad, expected in (
        (r"$`\operatorname{Tr}\rho`$", "unreviewed math command"),
        ("```math\n\\operatorname{Tr}\\rho\n```", "unreviewed math command"),
        (r"\[x\]", "instead of"),
        (r"\(x\)", "instead of"),
        (r"$`\frac{1}{2`$", "unbalanced TeX grouping"),
        ("$x", "unclosed math delimiter"),
        ("$x\ny$", "inline math crosses a line"),
        (r"$`\unknown{x}`$", "unreviewed math command"),
        ("## $`x`$", "plain-text heading"),
        ("## $$x$$", "plain-text heading"),
    ):
        assert any(expected in error for error in inspect(bad)[0]), (bad, inspect(bad)[0])
    assert not inspect(r"$`\{x\} + \$1`$")[0]
    assert not inspect(r"$`\begin{pmatrix}0&-i\\i&0\end{pmatrix}`$")[0]
    for bad in ("every F_k=1", r"every F\_k=1", "sqrt(rs)", "q^(2-2k)", "U(t)U(s)^dagger", "η_h", "r=s=d", "R=min(r²,s²)", r"\eta=(1)"):
        assert any("outside math" in error for error in inspect(bad)[0]), bad
    assert not inspect("See [the proof](theory/THEOREM.md#x_y) and AGENTS.md. Run `F_k = sqrt(rs)`.\n```python\nq**2\n```\n")[0]
    assert not inspect("**Rank bound.** $`F_k\\ge\\min(r^2,s^2)^{1-k}`$.\n```math\nU(t)U(s)^\\dagger\n```\n")[0]
    # TeX can compile while Markdown delimiter handling still fails. Check
    # actual source boundaries as well as the extracted mathematical content.
    for bad in ("degree-$k$", "degree-$`k`$", "$`q`$-dimensional", "pre$`k`$", "$`k`$post", "finite‑$`d`$"):
        assert any("attached to prose" in error for error in inspect(bad)[0]), bad
    for bad in ("degree $k$", "| Degree | $k$ |", "**$k$**"):
        assert any("protected" in error for error in inspect(bad)[0]), bad
    for good in ("degree $`k`$", "dimension $`q`$", "($`k`$), [$`m`$].", "**$`k`$**", "| Degree | $`k`$ |", "`degree-$k$`", "``$`k`$``", "~~~text\ndegree-$k$\n~~~\n"):
        assert not inspect(good)[0], (good, inspect(good)[0])
    assert inspect("degree-$k$")[1][0][1] == "k"
    assert inspect("degree $`k`$")[1][0][1].strip() == "k"
    print("Markdown math self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    paths, errors, count = markdown_paths(ROOT), [], 0
    for path in paths:
        failures, expressions = inspect(path.read_text(encoding="utf-8"))
        errors.extend(f"{path.relative_to(ROOT)}:{failure}" for failure in failures)
        count += len(expressions)
    if errors:
        print("Markdown math check failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Markdown math checks passed: {len(paths)} pages, {count} expressions")
    print("Reader pages checked; source archives are excluded. Live GitHub rendering requires a separate check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
