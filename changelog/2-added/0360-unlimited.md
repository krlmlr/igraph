# IGRAPH_UNLIMITED

`IGRAPH_UNLIMITED`, defined to `-1`, is a convenience constant for use with various "size limit" parameters, such as number of cliques returned, maximum path length, number of results returned, etc. It indicates that no limit should be used.

---

**Original changelog wording:**

> `IGRAPH_UNLIMITED`, defined to `-1`, is a convenience constant for use with various "size limit" parameters, such as number of cliques returned, maximum path length, number of results returned, etc. It indicates that no limit should be used.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0360-unlimited.md
  70    64    66    64  include/igraph_constants.h
```

Notes on remaining differences:
- `include/igraph_constants.h`: Remaining 66 add / 64 del from other entries (igraph_loops_t refactoring, igraph_order_t, IGRAPH_UNDIRECTED/IGRAPH_DIRECTED additions, etc.)
- `changelog/2-added/0360-unlimited.md`: Now 0 add since file exists; proof-of-work section adds to del count
