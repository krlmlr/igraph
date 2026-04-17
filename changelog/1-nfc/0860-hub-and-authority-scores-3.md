# igraph_hub_and_authority_scores()

**Category**: Warnings and behavioral refinements

`igraph_hub_and_authority_scores()` now warns when providing an undirected graph as input, and falls back to the equivalent eigenvector centrality computation.

---

**Original changelog wording:**

> `igraph_hub_and_authority_scores()` now warns when providing an undirected graph as input, and falls back to the equivalent eigenvector centrality computation.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0860-hub-and-authority-scores-3.md
```

Notes on remaining differences:
- `changelog/1-nfc/0860-hub-and-authority-scores-3.md`: Fully ported (11→0 add). No code changes needed because the undirected graph warning and eigenvector centrality fallback were already ported as part of the previous entry (0850-hub-and-authority-scores-2.md), which included the full set of warning improvements to `igraph_hub_and_authority_scores()`.
