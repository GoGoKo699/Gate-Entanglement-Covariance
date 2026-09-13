#!/usr/bin/env python3
"""Check local navigation in the maintained scientific reading route.

Historical checkpoint documents and external URLs are outside this check.
The immutable-data and scientific-calculation checks have separate commands.
"""
from pathlib import Path
from html import unescape
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def outside_fences(contents):
    """Remove fenced examples, including tilde fences and embedded backticks."""
    lines = []
    fence = None
    for line in contents.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence is None:
            if marker:
                fence = marker.group(1)
            else:
                lines.append(line)
        elif (marker and marker.group(1)[0] == fence[0]
              and len(marker.group(1)) >= len(fence)
              and not marker.group(2).strip()):
            fence = None
    return '\n'.join(lines)


def heading_anchors(contents):
    """GitHub-style slugs for the Markdown headings used in this repository.

    Inline link labels and HTML entities contribute visible heading text.
    Repeated headings receive -1, -2, ... suffixes, avoiding earlier slugs.
    Explicit HTML id/name anchors retain their spelling and case.
    """
    contents = outside_fences(contents)
    anchors = set(re.findall(
        r'<[^>]+\b(?:id|name)\s*=\s*[\"\']([^\"\']+)[\"\']',
        contents, flags=re.IGNORECASE))
    generated = set()
    lines = contents.splitlines()
    for i, line in enumerate(lines):
        match = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*$', line)
        if match:
            heading = re.sub(r'\s+#+\s*$', '', match.group(1))
        elif (i + 1 < len(lines) and line.strip()
              and re.match(r'^ {0,3}(?:=+|-+)\s*$', lines[i + 1])):
            heading = line.strip()
        else:
            continue
        heading = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', heading)
        heading = unescape(re.sub(r'<[^>]*>', '', heading)).lower()
        slug = re.sub(r'[^\w\-\s]', '', heading)
        slug = re.sub(r'\s', '-', slug)
        candidate = slug
        suffix = 0
        while candidate in generated:
            suffix += 1
            candidate = f'{slug}-{suffix}'
        generated.add(candidate)
    return anchors | generated


def local_targets(contents):
    """Inline links/images, reference definitions, and HTML image sources."""
    contents = outside_fences(contents)
    yield from re.findall(r'!?\[[^\]]*\]\(([^\s)]+)', contents)
    yield from re.findall(r'^ {0,3}\[[^\]]+\]:\s*(\S+)', contents,
                          flags=re.MULTILINE)
    yield from re.findall(r'<img\b[^>]*\bsrc\s*=\s*[\"\']([^\"\']+)',
                          contents, flags=re.IGNORECASE)


def check_repository():
    pages = sorted(ROOT.glob('*.md'))
    pages += sorted((ROOT / 'docs').glob('*.md'))
    pages += sorted((ROOT / 'theory').glob('*.md'))
    checked = 0
    fragments_checked = 0
    anchor_cache = {}
    failures = []
    for page in pages:
        contents = page.read_text()
        for target in local_targets(contents):
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc:
                continue
            destination = ((page.parent / unquote(url.path)).resolve()
                           if url.path else page)
            checked += 1
            if not destination.exists():
                failures.append(f'{page.relative_to(ROOT)}: {target}')
                continue
            if url.fragment and destination.suffix.lower() == '.md':
                fragments_checked += 1
                if destination not in anchor_cache:
                    anchor_cache[destination] = heading_anchors(destination.read_text())
                if unquote(url.fragment) not in anchor_cache[destination]:
                    failures.append(f'{page.relative_to(ROOT)}: {target} (missing anchor)')
    if failures:
        raise SystemExit('Missing local destinations:\n' + '\n'.join(failures))
    return {'status': 'passed', 'maintained_markdown_pages': len(pages),
            'local_link_destinations_checked': checked,
            'local_markdown_fragments_checked': fragments_checked,
            'scope': 'Local paths, image targets, and Markdown section anchors linked '
                     'from maintained Markdown, including same-page anchors. External '
                     'URLs and navigation originating in historical records are not audited.'}


if __name__ == '__main__':
    print(json.dumps(check_repository(), indent=2))
