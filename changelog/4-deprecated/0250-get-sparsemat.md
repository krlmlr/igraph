# igraph_get_sparsemat(), igraph_get_adjacency_sparse()

The deprecated `igraph_get_sparsemat()` was removed. Use `igraph_get_adjacency_sparse()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_get_sparsemat()` was removed. Use `igraph_get_adjacency_sparse()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     18     5     15  include/igraph_conversion.h
  40    122    41     95  src/misc/conversion.c
```

Notes on remaining differences:
- `include/igraph_conversion.h`: del reduced 18→15 (3 lines: comment + declaration). Remaining diff (5 add, 15 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, removal of other deprecated functions like `igraph_get_stochastic_sparsemat`).
- `src/misc/conversion.c`: del reduced 122→95 (27 lines: function + doc comment). add increased 40→41 due to diff context shift. Remaining diff (41 add, 95 del) is from other changelog entries (copyright/header, removal of `igraph_get_stochastic_sparsemat` and other deprecated functions, code changes).
