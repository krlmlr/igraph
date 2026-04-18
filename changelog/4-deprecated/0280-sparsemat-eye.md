# igraph_sparsemat_eye(), igraph_sparsemat_init_eye()

The deprecated `igraph_sparsemat_eye()` was removed. Use `igraph_sparsemat_init_eye()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_sparsemat_eye()` was removed. Use `igraph_sparsemat_init_eye()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     28     5     24  include/igraph_sparsemat.h
  31    329    31    315  src/core/sparsemat.c
```

Notes on remaining differences:
- `include/igraph_sparsemat.h`: del reduced 28→24 (4 lines: declaration + blank line). Remaining diff (5 add, 24 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, removal of other deprecated sparse matrix functions).
- `src/core/sparsemat.c`: del reduced 329→315 (14 lines: function + doc comment). Remaining diff (31 add, 315 del) is from other changelog entries (copyright/header, removal of many other deprecated sparsemat functions, code changes).
