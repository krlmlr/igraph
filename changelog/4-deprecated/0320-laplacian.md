# igraph_laplacian(), igraph_get_laplacian(), igraph_get_laplacian_sparse()

The deprecated `igraph_laplacian()` was removed. Use `igraph_get_laplacian()` or `igraph_get_laplacian_sparse()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_laplacian()` was removed. Use `igraph_get_laplacian()` or `igraph_get_laplacian_sparse()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  16     34    17     30  include/igraph_structural.h
   1     59     1      3  src/properties/spectral.c
```

Notes on remaining differences:
- `include/igraph_structural.h`: del reduced 34→30 (4 lines for declaration + blank line). add increased 16→17 from context shift. Remaining diff is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, other function changes).
- `src/properties/spectral.c`: del reduced 59→3. Remaining diff (1 add, 3 del) is from other changelog entries (copyright/comment header changes).
