#!/usr/bin/env python3
"""Check local navigation in the maintained scientific reading route.

Historical checkpoint documents and external URLs are outside this check.
The immutable-data and scientific-calculation checks have separate commands.
"""
from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def check_repository():
    pages = sorted(ROOT.glob('*.md'))
    pages += sorted((ROOT / 'docs').glob('*.md'))
    pages += sorted((ROOT / 'theory').glob('*.md'))
    checked = 0
    failures = []
    for page in pages:
        contents = page.read_text()
        # Ignore fenced examples; inline scientific links are left intact.
        outside_fences = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', contents,
                                flags=re.MULTILINE | re.DOTALL)
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', outside_fences):
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (page.parent / unquote(url.path)).resolve()
            checked += 1
            if not destination.exists():
                failures.append(f'{page.relative_to(ROOT)}: {target}')
    if failures:
        raise SystemExit('Missing local destinations:\n' + '\n'.join(failures))
    return {'status': 'passed', 'maintained_markdown_pages': len(pages),
            'local_link_destinations_checked': checked,
            'scope': 'Local path destinations in maintained Markdown; external URLs, '
                     'heading anchors, and historical checkpoint navigation are not audited.'}


if __name__ == '__main__':
    print(json.dumps(check_repository(), indent=2))
