# igraph_vector_qsort_ind(), igraph_vector_sort_ind()

The deprecated `igraph_vector_qsort_ind()` was removed. Use `igraph_vector_sort_ind()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_vector_qsort_ind()` was removed. Use `igraph_vector_sort_ind()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0140-vector-qsort-ind.md
  51    91    51    80  src/core/vector.pmt
   4    19     4    16  include/igraph_vector_pmt.h
```

Notes on remaining differences:
- `src/core/vector.pmt`: del reduced 91→80. Remaining are other deprecated removals (init_seq, binsearch2, move_interval2), OOM macro, doc changes, index_int rename.
- `include/igraph_vector_pmt.h`: del reduced 19→16. Remaining are other deprecated decl removals and copyright changes.
