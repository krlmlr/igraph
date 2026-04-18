# igraph_vector_binsearch2(), igraph_vector_contains_sorted()

The deprecated `igraph_vector_binsearch2()` was removed. Use `igraph_vector_contains_sorted()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_vector_binsearch2()` was removed. Use `igraph_vector_contains_sorted()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0150-vector-binsearch2.md
  51    80    51    68  src/core/vector.pmt
   4    16     4    14  include/igraph_vector_pmt.h
```

Notes on remaining differences:
- `src/core/vector.pmt`: del reduced 80→68. Remaining are other deprecated removals (init_seq, move_interval2), OOM macro, doc changes, index_int rename.
- `include/igraph_vector_pmt.h`: del reduced 16→14. Remaining are other deprecated decl removals (init_seq, move_interval2), index_int rename, copyright changes.
