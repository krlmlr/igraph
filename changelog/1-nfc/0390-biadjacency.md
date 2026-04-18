# igraph_biadjacency()

**Category**: Core graph manipulation

The order of edges in the graph returned by `igraph_(weighted_)adjacency()` and `igraph_biadjacency()` has changed. Note that these functions do not guarantee any specific edge order.

---

**Original changelog wording:**

> The order of edges in the graph returned by `igraph_(weighted_)adjacency()` and `igraph_biadjacency()` has changed. Note that these functions do not guarantee any specific edge order.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0390-biadjacency.md
```

Notes on remaining differences:
The code changes for this entry (edge ordering in adjacency/biadjacency constructors) were already present on `main-dev` from prior porting work. Only the changelog file itself needed to be added. The after diff shows 0/0 for this file since it now matches the `next` branch exactly (before the proof-of-work section was added). The overall diff decreased by 1 file and 11 insertions, corresponding exactly to the changelog file added.
