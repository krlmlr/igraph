# igraph_vector_move_interval2()

The deprecated `igraph_vector_move_interval2()` was removed.

---

**Original changelog wording:**

> The deprecated `igraph_vector_move_interval2()` was removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0160-vector-move-interval2.md
  51    68    51    60  src/core/vector.pmt
   4    14     4    11  include/igraph_vector_pmt.h
```

Notes on remaining differences:
- `src/core/vector.pmt`: del reduced 68→60. Remaining are other deprecated removals (init_seq), OOM macro, doc changes, index_int rename.
- `include/igraph_vector_pmt.h`: del reduced 14→11. Remaining are init_seq removal, index_int rename, copyright changes.
