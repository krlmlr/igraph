# Changelog — Split Structure

This directory contains the changelog split into individual files,
one per change entry. The structure mirrors the top-level categories
in `CHANGELOG.md`.

## Directory layout

```
changelog/
  README.md           — this file
  1-nfc/          — Non-functional changes
  2-added/          — Added functionality
  3-modified/          — Modified functionality
  4-deprecated/          — Deprecated and removed functionality
```

## Numbering

Files are numbered `0010-`, `0020-`, etc. within each directory.
Gaps in numbering allow inserting new entries without renumbering.
The ordering reflects estimated lines affected (descending),
so the most impactful changes appear first.

## Preamble

# igraph C library changelog

Categorization decision rules:

1. NFC priority: "Non-functional changes" (NFC) takes priority over "Modified
   functionality". A change is listed under NFC if it does not alter the
   behavior of a graph algorithm, even if it modifies function signatures,
   parameter types, or API conventions.

2. Modified functionality: Reserved for changes that alter how a graph
   algorithm computes its core results (e.g., different treatment of weights,
   different rounding, different output for the same input).

3. Version merging: Versions 1.0.0 and 1.0.1 are treated as a single release.
   Changes in 1.0.1 that fix regressions or bugs introduced in 1.0.0 are
   omitted (exit()/std::cout references, hub_and_authority warning bug,
   Infomap compilation, Apple compilation, libf2c prototypes).

4. Dependency ordering: NFC sub-headers are arranged by dependency structure:
   build system and compiler first, then core infrastructure, types, data
   structures, and progressively higher-level API changes.

5. Size ordering: Within each top-level category (and within each NFC
   sub-header), items are sorted by estimated lines affected in the diff
   (descending). This makes the most impactful changes appear first.

Nearly twenty years after the first igraph release, igraph 1.0 has finally arrived. This release focuses on providing a stable and more consistent interface that users and downstream maintainers can rely on with confidence, as well as adding new features that required API-breaking changes. There is now an official versioning policy, see [`VERSIONING.md`](VERSIONING.md).
