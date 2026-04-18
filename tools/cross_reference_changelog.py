#!/usr/bin/env python3
"""Cross-reference the original CHANGELOG.md with the split changelog/ structure.

For each bullet point in CHANGELOG.md, checks that a matching entry file exists
in the changelog/ directory with the original wording preserved as a > citation.

Reports:
  - Total entries found in CHANGELOG.md
  - Total entry files found in changelog/
  - Matched entries (original wording found in a split file)
  - Unmatched entries from CHANGELOG.md (not found in any split file)
  - Orphan files in changelog/ (no matching CHANGELOG.md entry)
"""

import re
import sys
from pathlib import Path


def normalize(text):
    """Normalize text for comparison: strip, collapse whitespace."""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text


def extract_citation(filepath):
    """Extract the > citation block from a split changelog file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the citation after "Original changelog wording:"
    m = re.search(r'\*\*Original changelog wording:\*\*\s*\n((?:>.*\n?)+)', content)
    if m:
        citation = m.group(1)
        # Remove > prefix and join
        lines = [line.lstrip('>').strip() for line in citation.strip().split('\n')]
        return normalize(' '.join(lines))
    return None


def parse_changelog_bullets(path):
    """Extract all bullet points from CHANGELOG.md."""
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    bullets = []
    current_h2 = None
    current_h3 = None

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith('## '):
            current_h2 = line[3:].strip()
            current_h3 = None
        elif line.startswith('### '):
            current_h3 = line[4:].strip()
        elif line.startswith('- '):
            bullet = line[2:].strip()
            j = i + 1
            while j < len(lines) and lines[j].startswith('  ') and not lines[j].startswith('- '):
                bullet += ' ' + lines[j].strip()
                j += 1
            bullets.append({
                'text': normalize(bullet),
                'section': current_h2,
                'subsection': current_h3,
                'line': i + 1,
            })
            i = j - 1
        i += 1

    return bullets


def main():
    repo = Path(__file__).resolve().parent.parent
    changelog_path = repo / 'CHANGELOG.md'
    changelog_dir = repo / 'changelog'

    if not changelog_path.exists():
        print(f'ERROR: {changelog_path} not found', file=sys.stderr)
        sys.exit(1)

    if not changelog_dir.exists():
        print(f'ERROR: {changelog_dir} not found — run split_changelog.py first',
              file=sys.stderr)
        sys.exit(1)

    # Parse original changelog
    bullets = parse_changelog_bullets(changelog_path)
    print(f'CHANGELOG.md: {len(bullets)} bullet entries found\n')

    # Collect all split entry files
    entry_files = {}
    for subdir in sorted(changelog_dir.iterdir()):
        if subdir.is_dir():
            for f in sorted(subdir.iterdir()):
                if f.name.endswith('.md') and f.name != 'README.md':
                    citation = extract_citation(f)
                    rel = f.relative_to(changelog_dir)
                    entry_files[str(rel)] = citation

    print(f'changelog/: {len(entry_files)} entry files found\n')

    # Match bullets to files
    matched = []
    unmatched_bullets = []
    used_files = set()

    for bullet in bullets:
        found = False
        for rel_path, citation in entry_files.items():
            if citation and citation == bullet['text']:
                matched.append({
                    'bullet': bullet,
                    'file': rel_path,
                })
                used_files.add(rel_path)
                found = True
                break
        if not found:
            unmatched_bullets.append(bullet)

    orphan_files = [f for f in entry_files if f not in used_files]

    # Report
    print(f'=== Cross-Reference Results ===\n')
    print(f'Matched:          {len(matched)} / {len(bullets)}')
    print(f'Unmatched:        {len(unmatched_bullets)}')
    print(f'Orphan files:     {len(orphan_files)}')
    print()

    if unmatched_bullets:
        print(f'--- Unmatched bullets from CHANGELOG.md ---')
        for b in unmatched_bullets:
            print(f'  Line {b["line"]}: {b["text"][:100]}...')
        print()

    if orphan_files:
        print(f'--- Orphan files in changelog/ ---')
        for f in orphan_files:
            print(f'  {f}')
        print()

    if not unmatched_bullets and not orphan_files:
        print('✅ All entries match perfectly. No orphans, no missing entries.')

    # Return exit code
    sys.exit(0 if not unmatched_bullets else 1)


if __name__ == '__main__':
    main()
