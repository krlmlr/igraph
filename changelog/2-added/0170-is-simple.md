# igraph_is_simple()

`igraph_is_simple()` gained an extra `igraph_bool_t` argument that decides whether edge directions should be considered. Directed graphs with a mutual edge pair are treated as non-simple if this argument is set to `IGRAPH_UNDIRECTED` (which treats the graph as if it was undirected).

---

**Original changelog wording:**

> `igraph_is_simple()` gained an extra `igraph_bool_t` argument that decides whether edge directions should be considered. Directed graphs with a mutual edge pair are treated as non-simple if this argument is set to `IGRAPH_UNDIRECTED` (which treats the graph as if it was undirected).

## Proof of work: `git diff --numstat HEAD..next` for modified files

```
BEFORE                   AFTER
add  del  file           add  del  file
  9    0  changelog/2-added/0170-is-simple.md           (matches next)
 37   15  src/properties/multiplicity.c       7   11  src/properties/multiplicity.c
 20   42  include/igraph_structural.h        41   19  include/igraph_structural.h
  5   24  src/cliques/glet.c                  4    3  src/cliques/glet.c
 23   33  src/community/fluid.c              24   23  src/community/fluid.c
  2   13  src/community/voronoi.c             1    1  src/community/voronoi.c
  6   15  src/misc/sir.c                      7    5  src/misc/sir.c
 11    2  tests/unit/prop_caching.c           2    0  tests/unit/prop_caching.c
```

### Remaining differences explained

- `src/properties/multiplicity.c` (7+/11-): igraph_neighbors API changes (extra params on next), copyright header style, igraph_has_multiple internals — unrelated to is_simple.
- `include/igraph_structural.h` (41+/19-): Copyright header, __BEGIN_DECLS, deprecated functions, other API signature changes — unrelated.
- `src/community/fluid.c` (24+/23-): Copyright header, igraph_neighbors API, other unrelated changes.
- `src/misc/sir.c` (7+/5-): Copyright header, unrelated changes.
- Other files with small remaining diffs: copyright headers, igraph_neighbors extra params, other unrelated API changes.
