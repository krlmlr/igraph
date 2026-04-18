#!/usr/bin/env python3
"""Split CHANGELOG.md into separate files, one per change entry.

Directory hierarchy:
  changelog/
    README.md
    1-nfc/           (Non-functional changes)
    2-added/         (Added functionality)
    3-modified/      (Modified functionality)
    4-deprecated/    (Deprecated and removed functionality)

Each entry gets a file like 0010-short-name.md with:
  - Title
  - Description (expanded from the bullet point)
  - Original wording as a > citation
"""

import re
import shutil
import sys
from pathlib import Path


def extract_identifiers(text):
    """Extract all igraph/IGRAPH/RNG identifiers from text."""
    ids = []
    # Functions: igraph_foo()
    ids.extend(re.findall(r'`(igraph_\w+)\(\)`', text))
    # Types/constants: igraph_foo_t, IGRAPH_FOO
    ids.extend(re.findall(r'`(igraph_\w+)`', text))
    ids.extend(re.findall(r'`(IGRAPH_\w+)`', text))
    ids.extend(re.findall(r'`(RNG_\w+)\(\)`', text))
    return ids


def slugify(text, seen_slugs, max_len=50):
    """Create a unique filesystem-safe slug from text."""
    text = text.strip()
    # Remove markdown formatting
    clean = re.sub(r'`([^`]*)`', r'\1', text)
    clean = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', clean)
    clean = re.sub(r'\*\*([^*]*)\*\*', r'\1', clean)
    clean = re.sub(r'_([^_]*)_', r'\1', clean)

    # Try to find the primary identifier
    ids = extract_identifiers(text)
    if ids:
        # Use first identifier, removing igraph_ prefix for brevity
        slug = ids[0].lower()
        slug = re.sub(r'^igraph_', '', slug)
        # If multiple functions mentioned, try to capture intent
        if len(ids) > 1 and slug in seen_slugs:
            # Combine first two
            id2 = ids[1].lower().replace('igraph_', '')
            slug = f'{slug}-{id2}'
    else:
        # Use first few words
        slug = clean[:max_len]

    slug = re.sub(r'[^a-z0-9]+', '-', slug.lower())
    slug = slug.strip('-')
    if len(slug) > max_len:
        slug = slug[:max_len].rsplit('-', 1)[0]

    # Ensure uniqueness
    base = slug
    counter = 2
    while slug in seen_slugs:
        slug = f'{base}-{counter}'
        counter += 1

    seen_slugs.add(slug)
    return slug


def make_title(text):
    """Extract a concise title from a changelog bullet."""
    text = text.strip()

    # Look for all backtick-quoted identifiers to find the best title
    all_backtick = re.findall(r'`([^`]+)`', text)

    # Extract functions (with parens) and other identifiers
    funcs = re.findall(r'`(igraph_\w+)\(\)`', text)
    macros = re.findall(r'`(IGRAPH_\w+)`', text)
    rng_macros = re.findall(r'`(RNG_\w+)\(\)`', text)
    types = re.findall(r'`(igraph_\w+_t)`', text)

    # RNG macros take precedence if they appear first
    if rng_macros and (not funcs or text.index(f'`{rng_macros[0]}') < text.index(f'`{funcs[0]}')):
        if len(rng_macros) > 1:
            return ', '.join(f'{m}()' for m in rng_macros)
        return rng_macros[0] + '()'

    # Multi-function entries: list all (up to 3)
    if len(funcs) > 3:
        return f'{funcs[0]}() and {len(funcs) - 1} others'
    if len(funcs) > 1:
        return ', '.join(f'{f}()' for f in funcs)
    if funcs:
        return funcs[0] + '()'

    # Types
    if types:
        return types[0]

    # IGRAPH_ macros/constants
    if macros:
        if len(macros) > 3:
            return f'{macros[0]} and {len(macros) - 1} others'
        if len(macros) > 1:
            return ', '.join(macros)
        return macros[0]

    # Any backtick-quoted content
    if all_backtick:
        return all_backtick[0]

    # Fall back to abbreviated text
    short = re.sub(r'`([^`]*)`', r'\1', text)
    short = re.sub(r'\*\*([^*]*)\*\*', r'\1', short)
    if len(short) > 80:
        short = short[:77] + '...'
    return short


def parse_changelog(path):
    """Parse CHANGELOG.md and return structured sections."""
    with open(path, 'r') as f:
        content = f.read()

    lines = content.split('\n')

    # Map top-level sections to directory names
    section_map = {
        'Non-functional changes': '1-nfc',
        'Added functionality': '2-added',
        'Modified functionality': '3-modified',
        'Deprecated and removed functionality': '4-deprecated',
    }

    sections = {}
    current_h2 = None
    current_h3 = None
    current_bullets = []
    preamble_lines = []
    h2_descriptions = {}

    i = 0
    # Collect preamble (before first ##)
    while i < len(lines):
        if lines[i].startswith('## '):
            break
        preamble_lines.append(lines[i])
        i += 1

    intro_text = '\n'.join(preamble_lines).strip()

    def flush_bullets():
        nonlocal current_bullets, current_h2, current_h3
        if current_bullets and current_h2:
            key = current_h2
            if key not in sections:
                sections[key] = []
            for bullet in current_bullets:
                sections[key].append({
                    'subsection': current_h3,
                    'text': bullet,
                })
            current_bullets = []

    while i < len(lines):
        line = lines[i]

        if line.startswith('## '):
            flush_bullets()
            heading = line[3:].strip()
            current_h2 = heading
            current_h3 = None
            current_bullets = []
            # Collect description text after heading (before first ### or -)
            desc_lines = []
            j = i + 1
            while j < len(lines):
                if lines[j].startswith('## ') or lines[j].startswith('### ') or lines[j].startswith('- '):
                    break
                if lines[j].strip():
                    desc_lines.append(lines[j])
                j += 1
            if desc_lines:
                h2_descriptions[heading] = '\n'.join(desc_lines)
        elif line.startswith('### '):
            flush_bullets()
            current_h3 = line[4:].strip()
        elif line.startswith('- '):
            # Start of a new bullet; collect continuation lines
            bullet = line[2:].strip()
            j = i + 1
            while j < len(lines) and lines[j].startswith('  ') and not lines[j].startswith('- '):
                bullet += ' ' + lines[j].strip()
                j += 1
            current_bullets.append(bullet)
            i = j - 1  # will be incremented below
        i += 1

    flush_bullets()

    return intro_text, sections, section_map, h2_descriptions


def write_entry(filepath, entry, subsection):
    """Write a single changelog entry file."""
    text = entry['text']
    title = make_title(text)

    with open(filepath, 'w') as f:
        f.write(f'# {title}\n\n')
        if subsection:
            f.write(f'**Category**: {subsection}\n\n')
        f.write(f'{text}\n')
        f.write(f'\n---\n\n')
        f.write(f'**Original changelog wording:**\n\n')
        f.write(f'> {text}\n')


def main():
    repo = Path(__file__).resolve().parent.parent
    changelog_path = repo / 'CHANGELOG.md'
    out_dir = repo / 'changelog'

    if not changelog_path.exists():
        print(f'ERROR: {changelog_path} not found', file=sys.stderr)
        sys.exit(1)

    intro_text, sections, section_map, h2_descriptions = parse_changelog(changelog_path)

    # Clean and create directory structure
    if out_dir.exists():
        shutil.rmtree(out_dir)

    out_dir.mkdir()

    # Create README.md
    readme_path = out_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write('# Changelog — Split Structure\n\n')
        f.write('This directory contains the changelog split into individual files,\n')
        f.write('one per change entry. The structure mirrors the top-level categories\n')
        f.write('in `CHANGELOG.md`.\n\n')
        f.write('## Directory layout\n\n')
        f.write('```\n')
        f.write('changelog/\n')
        f.write('  README.md           — this file\n')
        for heading, dirname in section_map.items():
            f.write(f'  {dirname}/          — {heading}\n')
        f.write('```\n\n')
        f.write('## Numbering\n\n')
        f.write('Files are numbered `0010-`, `0020-`, etc. within each directory.\n')
        f.write('Gaps in numbering allow inserting new entries without renumbering.\n')
        f.write('The ordering reflects estimated lines affected (descending),\n')
        f.write('so the most impactful changes appear first.\n\n')
        f.write('## Preamble\n\n')
        f.write(intro_text + '\n')

    total_files = 0

    for heading, dirname in section_map.items():
        if heading not in sections:
            continue

        entries = sections[heading]
        section_dir = out_dir / dirname
        section_dir.mkdir()

        # Write section README with description
        sec_readme = section_dir / 'README.md'
        with open(sec_readme, 'w') as f:
            f.write(f'# {heading}\n\n')
            if heading in h2_descriptions:
                f.write(h2_descriptions[heading] + '\n\n')
            f.write(f'{len(entries)} entries in this section.\n')

        seen_slugs = set()

        # Group by subsection for NFC, keep flat for others
        if heading == 'Non-functional changes':
            subsections_order = []
            subsections_map = {}
            for entry in entries:
                sub = entry['subsection'] or 'General'
                if sub not in subsections_map:
                    subsections_order.append(sub)
                    subsections_map[sub] = []
                subsections_map[sub].append(entry)

            seq = 10
            for sub in subsections_order:
                for entry in subsections_map[sub]:
                    slug = slugify(entry['text'], seen_slugs)
                    filename = f'{seq:04d}-{slug}.md'
                    write_entry(section_dir / filename, entry, sub)
                    seq += 10
                    total_files += 1
        else:
            seq = 10
            for entry in entries:
                slug = slugify(entry['text'], seen_slugs)
                filename = f'{seq:04d}-{slug}.md'
                write_entry(section_dir / filename, entry, entry.get('subsection'))
                seq += 10
                total_files += 1

    print(f'Created {total_files} entry files in {out_dir}/')
    print(f'Directories: {", ".join(d for d in section_map.values())}')

    # Print summary
    for heading, dirname in section_map.items():
        if heading in sections:
            count = len(sections[heading])
            print(f'  {dirname}: {count} entries')


if __name__ == '__main__':
    main()
