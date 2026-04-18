# igraph_edges()

`igraph_edges()` gained a new `igraph_bool_t bycol` argument that determines the order in which the edges are returned. `bycol = false` reproduces the existing behaviour, while `bycol = true` returns the edges suitable for a matrix stored in column-wise order.

---

**Original changelog wording:**

> `igraph_edges()` gained a new `igraph_bool_t bycol` argument that determines the order in which the edges are returned. `bycol = false` reproduces the existing behaviour, while `bycol = true` returns the edges suitable for a matrix stored in column-wise order.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0250-edges.md
  38    15     1     2  src/graph/type_common.c
  25    23    24    22  include/igraph_interface.h
 320   350   319   349  interfaces/functions.yaml
   3     3     2     2  src/connectivity/percolation.c
   4     4     3     3  src/misc/cocitation.c
  10     3     1     1  tests/unit/igraph_edges.c
   6     3     0     0  tests/unit/igraph_edges.out
```

Notes on remaining differences:
- `src/graph/type_common.c`: Large reduction (38→1 add, 15→2 del). Remaining diff is NFC (copyright header changes).
- `include/igraph_interface.h`: Small reduction. Remaining diffs are NFC and from other entries.
- `tests/unit/igraph_edges.c` and `.out`: Fully ported (test: 10→1, out: 6→0). Remaining 1/1 in test is NFC copyright change.
