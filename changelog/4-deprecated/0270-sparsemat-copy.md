# igraph_sparsemat_copy(), igraph_sparsemat_init_copy()

The deprecated `igraph_sparsemat_copy()` was removed. Use `igraph_sparsemat_init_copy()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_sparsemat_copy()` was removed. Use `igraph_sparsemat_init_copy()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     30     5     28  include/igraph_sparsemat.h
  31    342    31    329  src/core/sparsemat.c
```

Notes on remaining differences:
- `include/igraph_sparsemat.h`: del reduced 30→28 (2 lines for declaration). Remaining diff (5 add, 28 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, removal of other deprecated sparse matrix functions).
- `src/core/sparsemat.c`: del reduced 342→329 (13 lines: function + doc comment). Remaining diff (31 add, 329 del) is from other changelog entries (copyright/header, removal of many other deprecated sparsemat functions, code changes).
