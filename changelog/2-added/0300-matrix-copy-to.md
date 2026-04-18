# igraph_matrix_copy_to()

`igraph_matrix_copy_to()` gained an `igraph_matrix_storage_t storage` parameter that specifies whether the data should be written in column-major or row-major format.

---

**Original changelog wording:**

> `igraph_matrix_copy_to()` gained an `igraph_matrix_storage_t storage` parameter that specifies whether the data should be written in column-major or row-major format.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0300-matrix-copy-to.md
  65    96    19    59  src/core/matrix.pmt
   4    16     3    15  include/igraph_matrix_pmt.h
```

Notes on remaining differences:
- `src/core/matrix.pmt`: Dropped from 65/96 to 19/59. Remaining diffs are NFC changes from other entries: copyright header updates, doc wording tweaks (\c -> \type), removal of deprecated `igraph_matrix_copy()`, `igraph_matrix_e()`, `igraph_matrix_e_ptr()`, error message punctuation, and minor reformatting.
- `include/igraph_matrix_pmt.h`: Dropped from 4/16 to 3/15. Remaining diffs are removal of deprecated function declarations and doc parameter description updates from other entries.
- `changelog/2-added/0300-matrix-copy-to.md`: Fully ported (9/0 -> 0/0).
