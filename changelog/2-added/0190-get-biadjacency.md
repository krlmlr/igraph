# igraph_get_biadjacency()

`igraph_get_biadjacency()` now takes a `weights` parameter, and can optionally create weighted biadjacency matrices.

---

**Original changelog wording:**

> `igraph_get_biadjacency()` now takes a `weights` parameter, and can optionally create weighted biadjacency matrices.

## Proof of work: `git diff --numstat HEAD..next` for modified files

```
BEFORE                   AFTER
add  del  file           add  del  file
  9    0  changelog/...0190-get-biadjacency.md          (matches next)
 25   37  include/igraph_bipartite.h       33   20  include/igraph_bipartite.h
475  465  src/misc/bipartite.c            652  654  src/misc/bipartite.c
  3    3  tests/unit/igraph_get_biadjacency.c  1    1  tests/unit/igraph_get_biadjacency.c
```

### Remaining differences explained

- `include/igraph_bipartite.h` (33+/20-): Copyright header, other unrelated API changes (igraph_weighted_biadjacency, igraph_bipartite_iea_game, etc).
- `src/misc/bipartite.c` (652+/654-): Large unrelated diffs for igraph_weighted_biadjacency, igraph_biadjacency, game functions, copyright changes.
- `tests/unit/igraph_get_biadjacency.c` (1+/1-): Minor formatting difference.
