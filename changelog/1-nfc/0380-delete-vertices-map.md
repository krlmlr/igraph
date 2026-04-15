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
 223   134   195    99  src/graph/type_indexededgelist.c
  52    16    38    15  src/graph/type_common.c
  19    35     8    24  src/operators/subgraph.c
  32    24    25    23  include/igraph_interface.h
  21    21    18    18  src/flow/st-cuts.c
  15    52    17    56  src/connectivity/components.c
  23     1    22     0  doc/basicigraph.xxml
 472   444   471   443  interfaces/functions.yaml
   1     1     0     0  tests/unit/igraph_induced_subgraph_map.out
```

Notes on remaining differences:
- `changelog/1-nfc/0380-delete-vertices-map.md`: Now 0/0 — fully ported (the proof-of-work section is only on main-dev, so next has 0 add/0 del).
- `src/graph/type_indexededgelist.c`: Decreased from 223/134 to 195/99 — the rename and mapping logic changes are ported; remaining diffs are from other entries (memset init, IGRAPH_I_ATTRIBUTE_COPY refactoring, igraph_neighbors/igraph_degree/igraph_incident signature changes, etc.).
- `src/graph/type_common.c`: Decreased from 52/16 to 38/15 — the igraph_delete_vertices_map rename and deprecated alias are ported; remaining diffs are from other entries (igraph_edges bycol parameter, etc.).
- `src/operators/subgraph.c`: Decreased from 19/35 to 8/24 — the mapping logic changes are ported; remaining diffs are from other entries (igraph_incident parameter changes, IGRAPH_I_ATTRIBUTE_DESTROY removal, igraph_subgraph_edges removal, etc.).
- `include/igraph_interface.h`: Decreased from 32/24 to 25/23 — the function rename and deprecated alias are ported; remaining diffs are from other entries (header modernization, function signature changes).
- `src/flow/st-cuts.c`: Decreased from 21/21 to 18/18 — the three `- 1` offset removals are ported; remaining diffs are from other entries.
- `src/connectivity/components.c`: Increased from 15/52 to 17/56 — the vids_old2new initialization changes to -1 are necessary adaptations for this entry that differ slightly from the next branch (which may initialize differently); the increase is from the added `igraph_vector_int_fill` calls and comment adjustment.
- `doc/basicigraph.xxml`: Decreased from 23/1 to 22/0 — the doxrox-include rename is ported; remaining diffs are from other entries.
- `interfaces/functions.yaml`: Decreased from 472/444 to 471/443 — the function rename is ported; remaining diffs are from other entries.
- `tests/unit/igraph_induced_subgraph_map.out`: Now 0/0 — fully ported.
