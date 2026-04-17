# igraph_community_leiden_simple(), igraph_community_leiden()

`igraph_community_leiden_simple()` is a simplified interface to `igraph_community_leiden()` that allows selecting the objective function to maximize directly.

---

**Original changelog wording:**

> `igraph_community_leiden_simple()` is a simplified interface to `igraph_community_leiden()` that allows selecting the objective function to maximize directly.

## Proof of work: `git diff --numstat HEAD..next` for modified files

```
BEFORE                   AFTER
add  del  file           add  del  file
  9    0  changelog/...0180-community-leiden-simple.md   (matches next)
 35   18  include/igraph_community.h       21   4  include/igraph_community.h
231    0  src/community/leiden.c            7    0  src/community/leiden.c
 56    1  tests/unit/community_leiden.c     5    1  tests/unit/community_leiden.c
```

### Remaining differences explained

- `include/igraph_community.h` (21+/4-): Copyright header, __BEGIN_DECLS, other unrelated API changes (igraph_community_edge_betweenness lengths param, const qualifiers, IGRAPH_EXPERIMENTAL).
- `src/community/leiden.c` (7+/0-): Doc comment differences (abbreviated version used).
- `tests/unit/community_leiden.c` (5+/1-): igraph_vector_range replaced with manual init (function not available on main-dev).
