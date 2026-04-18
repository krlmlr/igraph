# igraph_subisomorphic_function_vf2(), igraph_get_subisomorphisms_vf2_callback()

The deprecated `igraph_subisomorphic_function_vf2()` was removed. Use `igraph_get_subisomorphisms_vf2_callback()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_subisomorphic_function_vf2()` was removed. Use `igraph_get_subisomorphisms_vf2_callback()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  13     47    13     37  include/igraph_isomorphism.h
   2     23     2      3  src/isomorphism/vf2.c
```

Notes on remaining differences:
- `include/igraph_isomorphism.h`: del reduced 47→37 (10 lines removed matching the deprecated declaration block). Remaining diff (13 add, 37 del) is from other changelog entries (copyright/license header changes, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, removal of DAG functions, `igraph_isomorphic_34`, other function reorderings, typo fix in BLISS enum comment).
- `src/isomorphism/vf2.c`: del reduced 23→3. Remaining diff (2 add, 3 del) is from other changelog entries (copyright/comment header: removal of `/* -*- mode: C -*- */` and `IGraph`→`igraph` rename, and `igraph_count_automorphisms`→`igraph_count_automorphisms_bliss` in `\sa` reference).
