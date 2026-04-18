# igraph_density()

`igraph_density()` now takes an optional `weights` parameter.

---

**Original changelog wording:**

> `igraph_density()` now takes an optional `weights` parameter.

## Proof of work: `git diff --numstat HEAD..next` for modified files

```
BEFORE                AFTER
add  del  file        add  del  file
  9    0  changelog/2-added/0160-density.md            (matches next)
 22   44  include/igraph_structural.h        42   20  include/igraph_structural.h
 48   26  src/properties/basic_properties.c   8    8  src/properties/basic_properties.c
 84   25  tests/unit/igraph_density.c                  (matches next)
```

### Remaining differences explained

- `include/igraph_structural.h` (42+/20-): Copyright header style, `__BEGIN_DECLS` vs `IGRAPH_BEGIN_C_DECLS`, deprecated `igraph_are_connected` removal, `igraph_diversity` const qualifier change — all unrelated to density.
- `src/properties/basic_properties.c` (8+/8-): Mode line/copyright header style, `\experimental` tag on `igraph_mean_degree`, `igraph_incident`/`igraph_neighbors` API changes — all unrelated to density.
