# igraph_hub_and_authority_scores()

**Category**: Centralities

`igraph_hub_and_authority_scores()` no longer has a `scale` parameter. The result is now always scaled so that the largest hub and authority scores are each 1.

---

**Original changelog wording:**

> `igraph_hub_and_authority_scores()` no longer has a `scale` parameter. The result is now always scaled so that the largest hub and authority scores are each 1.

## `git diff --numstat HEAD..next` (before → after)

```
before                after                 file
add     del           add     del
11      0             -       -             changelog/1-nfc/0720-hub-and-authority-scores.md
57      71            57      71            include/igraph_centrality.h
400     380           399     380           interfaces/functions.yaml
4       4             3       4             src/centrality/centrality_internal.h
25      5             3       5             src/centrality/centrality_other.c
133     149           110     111           src/centrality/hub_authority.c
13      13            1       1             tests/unit/hub_and_authority.c
5       5             -       -             tests/unit/hub_and_authority.out
```

Remaining diffs in `include/igraph_centrality.h` and `interfaces/functions.yaml` are unrelated to this change (other API changes on `next`). Remaining diffs in `src/centrality/hub_authority.c` include changes from later changelog entries (0850: warn_zero_entries, 0860: undirected fallback, removal of deprecated functions in 4-deprecated/0050). The `src/centrality/centrality_internal.h` and `centrality_other.c` remaining diffs are whitespace/macro renames. The 1-line remaining diff in `tests/unit/hub_and_authority.c` is a copyright header change.
