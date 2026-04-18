# igraph_get_stochastic_sparsemat(), igraph_get_stochastic_sparse()

The deprecated `igraph_get_stochastic_sparsemat()` was removed. Use `igraph_get_stochastic_sparse()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_get_stochastic_sparsemat()` was removed. Use `igraph_get_stochastic_sparse()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     15     5     10  include/igraph_conversion.h
  41     95    41     64  src/misc/conversion.c
```

Notes on remaining differences:
- `include/igraph_conversion.h`: del reduced 15→10 (5 lines: comment + declaration). Remaining diff (5 add, 10 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes).
- `src/misc/conversion.c`: del reduced 95→64 (31 lines: function + doc comment + blank line). Remaining diff (41 add, 64 del) is from other changelog entries (copyright/header changes, other deprecated function removals, code changes).
