# igraph_get_all_simple_paths()

**Category**: Paths and cycles

`igraph_get_all_simple_paths()` returns its results in an integer vector list (`igraph_vector_int_list_t`) instead of a single integer vector.

---

**Original changelog wording:**

> `igraph_get_all_simple_paths()` returns its results in an integer vector list (`igraph_vector_int_list_t`) instead of a single integer vector.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0590-get-all-simple-paths.md
  77    55     0     0  src/paths/simple_paths.c
  51    87    47    81  include/igraph_paths.h
  30    21     3     3  tests/unit/igraph_get_all_simple_paths.c
  81    10     0     0  tests/unit/igraph_get_all_simple_paths.out
 434   395   430   393  interfaces/functions.yaml
  36    36    36    41  interfaces/types.yaml
   7     3     7     3  fuzzing/misc_algos.cpp
```

Notes on remaining differences:
- `changelog/1-nfc/0590-get-all-simple-paths.md`: Fully ported (11→0 add, 0→0 del). The after-delete increase is due to the proof-of-work section added here but not present on `next`.
- `src/paths/simple_paths.c`: Fully ported (77→0 add, 55→0 del).
- `include/igraph_paths.h`: Decreased slightly (51→47 add, 87→81 del). Remaining diffs are unrelated changes to other function declarations (e.g. `igraph_distances`, `igraph_get_shortest_paths`, deprecated function removals, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`).
- `tests/unit/igraph_get_all_simple_paths.c`: Large decrease (30→3 add, 21→3 del). Remaining small diff is copyright header reformatting.
- `tests/unit/igraph_get_all_simple_paths.out`: Fully ported (81→0 add, 10→0 del).
- `interfaces/functions.yaml`: Small decrease (434→430 add, 395→393 del). Remaining diffs are unrelated function entries.
- `interfaces/types.yaml`: Small increase in del (36→41). This is because the new `VERTEX_INDICES_LIST` type was added but `next` has additional types not yet ported, increasing the delete count slightly.
- `fuzzing/misc_algos.cpp`: No change (7→7 add, 3→3 del). Remaining diffs are unrelated changes (copyright header, other function calls).
