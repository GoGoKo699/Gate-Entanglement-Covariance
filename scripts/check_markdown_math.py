#!/usr/bin/env python3
"""Check the maintained reading route's portable Markdown math conventions, using only stdlib.

This is a source linter, not GitHub's renderer or a complete TeX parser. The
command inventory is deliberately conservative: review new commands before
extending it. Ordinary code examples are ignored; fenced math is checked.
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
        errors.append(f"line {line_at(legacy.start())}: use $...$ or $$...$$ instead of {legacy[0]}")
    for number, line in enumerate(source.splitlines(), 1):
        if re.match(r"^ {0,3}#{1,6}\s", line) and "$" in line:
            errors.append(f"line {number}: use a plain-text heading and put the equation in the body")
    opening = None
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
            expressions.append((line, tex, token[0] == "$$"))
            opening = None
    if opening is not None:
        errors.append(f"line {line_at(opening.start())}: unclosed math delimiter {opening[0]}")
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
    # AGENTS.md freezes evidence/, limits/, legacy/ and historical records.
    # Match the maintained root/docs/theory scope of check_repository.py.
    return sorted(root.glob("*.md")) + sorted((root / "docs").glob("*.md")) + sorted((root / "theory").glob("*.md"))


def self_test() -> None:
    # Exercise the actual GitHub backtick delimiters, math fences, escaped
    # braces/dollars, and deliberate delimiter, command, grouping and heading failures.
    valid = "$`\\mathop{\\mathrm{Tr}}\\nolimits\\rho`$\n```math\n\\frac{1}{2}\\{x\\}\n```\n"
    assert not inspect(valid)[0]
    assert len(inspect(valid)[1]) == 2
    assert not inspect("`$\\operatorname{x}$`\n```tex\n$\\operatorname{x}$\n```\n")[0]
    for bad in (r"$\operatorname{Tr}\rho$", r"$`\operatorname{Tr}\rho`$", "```math\n\\operatorname{Tr}\\rho\n```", r"\[x\]", r"\(x\)", r"$\frac{1}{2$", "$x", "$x\ny$", r"$\unknown{x}$", "## $x$", "## $$x$$"):
        assert inspect(bad)[0], bad
    assert not inspect(r"$\{x\} + \$1$")[0]
    assert not inspect(r"$\begin{pmatrix}0&-i\\i&0\end{pmatrix}$")[0]
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
    print("Maintained pages only; frozen records are excluded. Live GitHub rendering requires a separate check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
