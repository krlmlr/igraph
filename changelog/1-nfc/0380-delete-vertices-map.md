# igraph_delete_vertices_map(), igraph_delete_vertices_idx(), igraph_induced_subgraph_map()

**Category**: Core graph manipulation

`igraph_delete_vertices_map()` (formerly called `igraph_delete_vertices_idx()`) and `igraph_induced_subgraph_map()` now use `-1` to represent unmapped vertices in the returned forward mapping vector and they do not offset vertex indices by 1 any more. Note that the inverse map always behaved this way, this change makes the two mappings consistent.

---

**Original changelog wording:**

> `igraph_delete_vertices_map()` (formerly called `igraph_delete_vertices_idx()`) and `igraph_induced_subgraph_map()` now use `-1` to represent unmapped vertices in the returned forward mapping vector and they do not offset vertex indices by 1 any more. Note that the inverse map always behaved this way, this change makes the two mappings consistent.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0380-delete-vertices-map.md
  30    22    20    18  include/igraph_interface.h
 206   130   177    93  src/graph/type_indexededgelist.c
  52    16    39    16  src/graph/type_common.c
  19    35    11    27  src/operators/subgraph.c
  15    52    12    52  src/connectivity/components.c
  21    21    18    18  src/flow/st-cuts.c
   1     1     0     0  tests/unit/igraph_induced_subgraph_map.out
```

Notes on remaining differences:

- `changelog/1-nfc/0380-delete-vertices-map.md`: 0 remaining (the del-a count will increase by the lines of this proof-of-work section, since `next` does not have it).
- `include/igraph_interface.h`: Remaining differences belong to other changelog entries (e.g., `igraph_neighbors` extended signature, `igraph_delete_vertices` const removal, and other function signature changes).
- `src/graph/type_indexededgelist.c`: Large remaining diff covers many future changelog entries including `igraph_neighbors` extended signature, comment style changes, and other refactoring.
- `src/graph/type_common.c`: Remaining 39 additions include the `igraph_neighbors` refactoring and other later changes.
- `src/operators/subgraph.c`: Remaining differences include the `igraph_incident` extended signature (5th `loops` parameter), `IGRAPH_I_ATTRIBUTE_DESTROY` removal, `igraph_subgraph_edges` deprecation removal, and other later entries.
- `src/connectivity/components.c`: The 52 remaining deletions on `next` correspond to a substantial refactoring of `igraph_decompose` and related functions not yet ported; we added only the two `igraph_vector_int_fill(&vids_old2new, -1)` calls required by the mapping convention change.
- `src/flow/st-cuts.c`: Small remaining differences are `igraph_neighbors` signature changes for later entries.
- `tests/unit/igraph_induced_subgraph_map.out`: Fully ported (0 remaining diff).
