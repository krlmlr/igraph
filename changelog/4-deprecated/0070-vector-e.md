# igraph_vector_e() and 3 others

The deprecated `igraph_vector_e()`, `igraph_vector_e_ptr()`, `igraph_matrix_e()` and `igraph_matrix_e_ptr()` were removed. Use the alternatives ending in `_get()` and `_get_ptr()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_vector_e()`, `igraph_vector_e_ptr()`, `igraph_matrix_e()` and `igraph_matrix_e_ptr()` were removed. Use the alternatives ending in `_get()` and `_get_ptr()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0070-vector-e.md
  51   121    51    91  src/core/vector.pmt
  19    47    19    25  src/core/matrix.pmt
   4    21     4    19  include/igraph_vector_pmt.h
   3    12     3     8  include/igraph_matrix_pmt.h
```

Notes on remaining differences:
- `src/core/vector.pmt`: del reduced 121→91. Remaining diffs are other deprecated function removals (init_seq, qsort_ind, binsearch2, move_interval2), OOM macro changes, doc rewrites, index_int rename.
- `src/core/matrix.pmt`: del reduced 47→25. Remaining diffs are doc changes, error message punctuation, variable reordering.
- `include/igraph_vector_pmt.h`: del reduced 21→19. Remaining are other deprecated decl removals, index_int rename, copyright changes.
- `include/igraph_matrix_pmt.h`: del reduced 12→8. Remaining are copyright/license header changes.
