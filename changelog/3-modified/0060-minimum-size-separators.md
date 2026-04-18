# igraph_minimum_size_separators()

`igraph_minimum_size_separators()` no longer returns any separating vertex sets for complete graphs. Prior to igraph 1.0, it would return all `n - 1` size vertex subsets where `n` is the vertex count.

---

**Original changelog wording:**

> `igraph_minimum_size_separators()` no longer returns any separating vertex sets for complete graphs. Prior to igraph 1.0, it would return all `n - 1` size vertex subsets where `n` is the vertex count.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/3-modified/0060-minimum-size-separators.md
  23    21    11     6  src/connectivity/separators.c
  24    20     1     1  tests/unit/igraph_minimum_size_separators.c
  49    24     0     0  tests/unit/igraph_minimum_size_separators.out
```

Notes on remaining differences:
- `src/connectivity/separators.c`: Remaining 11/6 are NFC changes from other entries (copyright header, `igraph_neighbors` call formatting, `igraph_vector_int_order1` → `igraph_i_vector_int_order` rename).
- `tests/unit/igraph_minimum_size_separators.c`: Remaining 1/1 is copyright header NFC change.
- Test output and changelog fully ported (0/0 after).
