# igraph_clusters(), igraph_connected_components()

The deprecated `igraph_clusters()` function was removed. Use `igraph_connected_components()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_clusters()` function was removed. Use `igraph_connected_components()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
    9      0      -      -  changelog/4-deprecated/0350-clusters.md
    9     17      9     13  include/igraph_components.h
   16     26     16     12  src/connectivity/components.c
```

Notes on remaining differences:
- `changelog/4-deprecated/0350-clusters.md`: Before 9+/0-. After: file matches `next` (minus proof-of-work section).
- `include/igraph_components.h`: Deletions decreased 17→13. The 4-line decrease corresponds to the removed `igraph_clusters` declaration and its comment. Remaining 9+/13- are copyright header updates, `__BEGIN_DECLS`/`__END_DECLS` → `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS`, and addition of `IGRAPH_EXPERIMENTAL` to percolation functions — all later entries.
- `src/connectivity/components.c`: Deletions decreased 26→12. The 14-line decrease is the removed `igraph_clusters` function with its doc comment. Remaining 16+/12- are copyright header, formatting changes to `igraph_neighbors` calls, `0`→`NULL`/`1`→`true`, comment wording changes, blank line additions, `\experimental` removal — all later entries.
