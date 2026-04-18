# igraph_neighbors(), igraph_vs_adj(), igraph_adjlist_init()

`igraph_neighbors()` and `igraph_vs_adj()` gained two extra arguments, `igraph_loops_t loops` and `igraph_bool_t multiple` to specify what to do with loop and multiple edges. This makes their interfaces consistent with `igraph_adjlist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` and `multiple = true` to reproduce the previous behavior.

---

**Original changelog wording:**

> `igraph_neighbors()` and `igraph_vs_adj()` gained two extra arguments, `igraph_loops_t loops` and `igraph_bool_t multiple` to specify what to do with loop and multiple edges. This makes their interfaces consistent with `igraph_adjlist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` and `multiple = true` to reproduce the previous behavior.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0320-neighbors.md
  24    22    16    18  include/igraph_interface.h
  16    21     5    17  include/igraph_iterators.h
  80    61    37    28  src/graph/type_indexededgelist.c
  56   102    17    89  src/graph/iterators.c
  54   134    49   104  src/graph/adjlist.c
   3    13     3     3  src/graph/internal.h
 311   350   306   347  interfaces/functions.yaml
  17    56    16    55  src/connectivity/components.c
  83    70    82    68  src/misc/motifs.c
  13    24    13    24  src/misc/matching.c
   7     6     4     3  examples/simple/igraph_neighbors.c
  20    21     7     7  tests/unit/adj.c
 155    12   155    12  tests/unit/igraph_neighbors.c
```

Notes on remaining differences:
- `src/graph/type_indexededgelist.c`: 80/61 -> 37/28, large reduction from merging `igraph_i_neighbors` into `igraph_neighbors` and `igraph_i_incident` into `igraph_incident`. Remaining diffs are NFC (copyright, doc wording, formatting from later entries).
- `src/graph/iterators.c`: 56/102 -> 17/89, significant reduction from updating `igraph_vs_adj` and `igraph_es_incident` with new parameters. Remaining diffs are NFC changes and `igraph_vs_nonadj` changes from later entries.
- `src/graph/adjlist.c`: 54/134 -> 49/104, reduction from updating adjlist callers. Remaining diffs are other NFC/refactoring changes.
- `src/graph/internal.h`: 3/13 -> 3/3, removed `igraph_i_neighbors` and `igraph_i_incident` declarations.
- `include/igraph_iterators.h`: 16/21 -> 5/17, significant reduction from adding struct fields and updating signatures.
- All callers across 41+ source files updated with appropriate `loops` and `multiple` parameters.
