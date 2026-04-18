# igraph_community_infomap()

`igraph_community_infomap()` now supports regularization and gained the `is_regularized` and `regularization_strength` parameters.

---

**Original changelog wording:**

> `igraph_community_infomap()` now supports regularization and gained the `is_regularized` and `regularization_strength` parameters.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0150-community-infomap.md
  38    19    35    18  include/igraph_community.h
   0   323     0   328  src/community/infomap/infomap.cc
 105    61   105    62  tests/unit/igraph_community_infomap.c
  21     8    21     8  tests/unit/null_communities.c
 322   353   322   354  interfaces/functions.yaml
```

Notes on remaining differences:
- **include/igraph_community.h**: Reduced add by 3 (38→35) — new parameters added. Reduced del by 1 (19→18) — const removed from function signature as part of this port. Other diffs are from other entries.
- **src/community/infomap/infomap.cc**: Increased del by 5 (323→328) — the new parameters were added with IGRAPH_UNUSED() stubs since the full infomap rewrite (which moves to a vendored library) is a later change. The regularization parameters are accepted but not yet effective.
- **tests/unit/igraph_community_infomap.c**: Increased del by 1 (61→62) — callers updated to pass new parameters. Full test expansion (regularization tests) will come with the infomap library rewrite.
- **tests/unit/null_communities.c**: No change in diff — caller updated with new parameters.
- **interfaces/functions.yaml**: Increased del by 1 (353→354) — new parameters added to infomap entry.
