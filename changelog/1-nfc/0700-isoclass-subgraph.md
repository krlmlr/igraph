# igraph_isoclass_subgraph(), igraph_vss_vector()

**Category**: Isomorphism functions and permutations

`igraph_isoclass_subgraph()` now takes a parameter of type `igraph_vs_t vids` instead of `igraph_vector_int_t vids`. Apply `igraph_vss_vector()` to the vector of vertex IDs to convert it to an `igraph_vs_t`.

---

**Original changelog wording:**

> `igraph_isoclass_subgraph()` now takes a parameter of type `igraph_vs_t vids` instead of `igraph_vector_int_t vids`. Apply `igraph_vss_vector()` to the vector of vertex IDs to convert it to an `igraph_vs_t`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0700-isoclass-subgraph.md
  15    58    13    57  include/igraph_isomorphism.h
  18    15     4     3  src/isomorphism/isoclasses.c
  21    22     1     2  tests/unit/isoclasses.c
   3     3     1     1  tests/unit/isoclasses2.c
 410   390   409   389  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0700-isoclass-subgraph.md`: Fully ported (0/0 after). The proof-of-work section below will add deletion lines since `next` doesn't have it.
- `include/igraph_isomorphism.h`: Remaining diff (13 add, 57 del) is from other changelog entries (removal of deprecated functions, header/copyright cleanup, reordering declarations).
- `src/isomorphism/isoclasses.c`: Remaining diff (4 add, 3 del) is from other entries (header/copyright cleanup, `igraph_neighbors` extra parameters change).
- `tests/unit/isoclasses.c`: Remaining diff (1 add, 2 del) is from header/copyright cleanup.
- `tests/unit/isoclasses2.c`: Remaining diff (1 add, 1 del) is from header/copyright cleanup.
- `interfaces/functions.yaml`: Remaining diff (409 add, 389 del) is from many other changelog entries' interface changes.
