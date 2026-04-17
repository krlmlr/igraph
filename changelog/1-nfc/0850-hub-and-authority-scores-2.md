# igraph_hub_and_authority_scores()

**Category**: Warnings and behavioral refinements

`igraph_hub_and_authority_scores()` now warns when a large fraction of centrality scores are zero, as this indicates a non-unique solution, and thus the returned result may not be meaningful.

---

**Original changelog wording:**

> `igraph_hub_and_authority_scores()` now warns when a large fraction of centrality scores are zero, as this indicates a non-unique solution, and thus the returned result may not be meaningful.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0850-hub-and-authority-scores-2.md
 110   111     3   109  src/centrality/hub_authority.c
```

Notes on remaining differences:
- `changelog/1-nfc/0850-hub-and-authority-scores-2.md`: Fully ported (11→0 add).
- `src/centrality/hub_authority.c`: Massively reduced from 110→3 add, 111→109 del. The 107-line reduction in additions reflects all the warning infrastructure, undirected graph fallback, zero-entry check, and related documentation now ported. Remaining 3 add / 109 del are from other entries: copyright/license header changes and removal of deprecated `igraph_hub_score()` and `igraph_authority_score()` functions.
