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
 110   111    36   109  src/centrality/hub_authority.c
```

Notes on remaining differences:
- `changelog/1-nfc/0850-hub-and-authority-scores-2.md`: Fully resolved (11→0).
- `src/centrality/hub_authority.c`: Large reduction from 110/111 to 36/109. Added the `warn_zero_entries()` function, the call to it, doc comments about non-unique solutions and negative weights, warnings for empty graphs and all-zero-weights, and improved starting values for ARPACK. Remaining diffs (36/109) are from other entries: copyright header, undirected graph fallback (entry 0860), deprecated function removal (entry 4-deprecated/0050), and whitespace reformatting. The del count stayed nearly the same (111→109) because the deprecated function removals are in later entries.
