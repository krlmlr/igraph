# igraph_vector_copy() and 3 others

The deprecated `igraph_vector_copy()` and `igraph_matrix_copy()` were removed. Use `igraph_vector_init_copy()` and `igraph_matrix_init_copy()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_vector_copy()` and `igraph_matrix_copy()` were removed. Use `igraph_vector_init_copy()` and `igraph_matrix_init_copy()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0060-vector-copy.md
  51   134    51   121  src/core/vector.pmt
  19    59    19    47  src/core/matrix.pmt
   4    23     4    21  include/igraph_vector_pmt.h
   3    15     3    12  include/igraph_matrix_pmt.h
```

Notes on remaining differences:
- `src/core/vector.pmt`: Remaining 51 add / 121 del belong to other changelog entries (removal of `igraph_vector_e`, `igraph_vector_e_ptr`, `igraph_vector_init_seq`, `igraph_vector_qsort_ind`, `igraph_vector_binsearch2`, `igraph_vector_move_interval2`, plus OOM macro changes, doc rewrites, and `index_int` → `index_in_place` rename).
- `src/core/matrix.pmt`: Remaining 19 add / 47 del belong to other entries (removal of `igraph_matrix_e`, `igraph_matrix_e_ptr`, doc changes, error message punctuation fixes, variable reordering).
- `include/igraph_vector_pmt.h`: Remaining 4 add / 21 del belong to other entries (removal of `init_seq`, `e`, `e_ptr`, `binsearch2`, `qsort_ind`, `move_interval2` declarations, `index_int` rename, copyright header changes).
- `include/igraph_matrix_pmt.h`: Remaining 3 add / 12 del belong to other entries (removal of `e`, `e_ptr` declarations, copyright header changes).
- `changelog/4-deprecated/0060-vector-copy.md`: After goes to 0/0 because the file now matches `next` (aside from the proof-of-work section appended here, which increases the after-del count slightly in subsequent measurements).
