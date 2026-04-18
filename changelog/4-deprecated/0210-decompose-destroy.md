# igraph_decompose_destroy()

The deprecated `igraph_decompose_destroy()` was removed.

---

**Original changelog wording:**

> The deprecated `igraph_decompose_destroy()` was removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   8     22     9     17  include/igraph_components.h
  16     55    16     26  src/connectivity/components.c
```

Notes on remaining differences:
- `include/igraph_components.h`: del reduced 22→17 (5 lines: include, comment+declaration, blank line). add increased 8→9 because the removal of the `igraph_vector_ptr.h` include exposes a blank line difference vs next. Remaining diff (9 add, 17 del) is from other changelog entries (copyright/license header changes, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`/`__END_DECLS`→`IGRAPH_END_C_DECLS`, removal of `igraph_clusters` deprecated alias, `IGRAPH_EXPERIMENTAL` additions to percolation functions).
- `src/connectivity/components.c`: del reduced 55→26. Remaining diff (16 add, 26 del) is from other changelog entries (copyright/comment header changes, removal of `igraph_clusters`, `igraph_neighbors` call reformatting, `0`→`NULL`/`1`→`true` changes, comment rewording, blank line addition, removal of `\experimental` from `igraph_is_biconnected`).
