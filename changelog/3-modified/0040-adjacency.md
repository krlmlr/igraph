# igraph_adjacency()

`igraph_adjacency()` now treats `IGRAPH_LOOPS_TWICE` as `IGRAPH_LOOPS_ONCE` when the mode is `IGRAPH_ADJ_DIRECTED`, `IGRAPH_ADJ_UPPER` or `IGRAPH_ADJ_LOWER`. For directed graphs, this is for the sake of consistency with the rest of the library where `IGRAPH_LOOPS_TWICE` is considered for undirected graphs only. For the "upper" and "lower" modes, double-counting the diagonal makes no sense because the double-counting artifact appears when you add the _transpose_ of an upper (or lower) diagonal matrix on top of the matrix itself. See Github issue #2501 for more context.

---

**Original changelog wording:**

> `igraph_adjacency()` now treats `IGRAPH_LOOPS_TWICE` as `IGRAPH_LOOPS_ONCE` when the mode is `IGRAPH_ADJ_DIRECTED`, `IGRAPH_ADJ_UPPER` or `IGRAPH_ADJ_LOWER`. For directed graphs, this is for the sake of consistency with the rest of the library where `IGRAPH_LOOPS_TWICE` is considered for undirected graphs only. For the "upper" and "lower" modes, double-counting the diagonal makes no sense because the double-counting artifact appears when you add the _transpose_ of an upper (or lower) diagonal matrix on top of the matrix itself. See Github issue #2501 for more context.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/3-modified/0040-adjacency.md
```

Notes on remaining differences:
The code changes for this entry (IGRAPH_LOOPS_TWICE treated as IGRAPH_LOOPS_ONCE for DIRECTED/UPPER/LOWER modes) were already ported as part of entry `1-nfc/0950-adjacency.md`, which noted that the performance improvements and behavioral changes were closely intertwined and could not be cleanly separated. Only the changelog file itself needed to be added. The after diff shows 0/0 for this file since it now matches the `next` branch exactly (before the proof-of-work section was added). The overall diff decreased by 1 file and 9 insertions, corresponding exactly to the changelog file added.
