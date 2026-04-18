# igraph_sparsemat_diag(), igraph_sparsemat_init_diag()

The deprecated `igraph_sparsemat_diag()` was removed. Use `igraph_sparsemat_init_diag()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_sparsemat_diag()` was removed. Use `igraph_sparsemat_init_diag()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     24     5     21  include/igraph_sparsemat.h
  31    315    31    301  src/core/sparsemat.c
```

Notes on remaining differences:
- `include/igraph_sparsemat.h`: del reduced 24→21 (3 lines for declaration). Remaining diff (5 add, 21 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, removal of other deprecated sparse matrix functions).
- `src/core/sparsemat.c`: del reduced 315→301 (14 lines: function + doc comment). Remaining diff (31 add, 301 del) is from other changelog entries.
