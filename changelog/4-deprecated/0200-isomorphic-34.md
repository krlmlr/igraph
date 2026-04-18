# igraph_isomorphic_34(), igraph_isomorphic()

The deprecated `igraph_isomorphic_34()` was removed. Its functionality is accessible through `igraph_isomorphic()`.

---

**Original changelog wording:**

> The deprecated `igraph_isomorphic_34()` was removed. Its functionality is accessible through `igraph_isomorphic()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  13     37    13     31  include/igraph_isomorphism.h
   1     29     1      2  src/isomorphism/queries.c
```

Notes on remaining differences:
- `include/igraph_isomorphism.h`: del reduced 37→31 (6 lines: declaration + blank lines). Remaining diff (13 add, 31 del) is from other changelog entries (copyright/license header changes, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`/`__END_DECLS`→`IGRAPH_END_C_DECLS`, removal of DAG functions, function reorderings, typo fix in BLISS enum comment).
- `src/isomorphism/queries.c`: del reduced 29→2. Remaining diff (1 add, 2 del) is from other changelog entries (copyright/comment header: removal of `/* -*- mode: C -*- */` and `IGraph`→`igraph` rename).
