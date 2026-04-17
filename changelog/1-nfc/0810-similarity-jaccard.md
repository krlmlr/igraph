# igraph_similarity_jaccard(), igraph_similarity_dice()

**Category**: Other network analysis

`igraph_similarity_jaccard()` and `igraph_similarity_dice()` now take two sets of vertices (`to` and `from` parameters) to create vertex pairs of, instead of one. Pass the same vertex set to both parameters to recover the previous behaviour.

---

**Original changelog wording:**

> `igraph_similarity_jaccard()` and `igraph_similarity_dice()` now take two sets of vertices (`to` and `from` parameters) to create vertex pairs of, instead of one. Pass the same vertex set to both parameters to recover the previous behaviour.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0810-similarity-jaccard.md
  33    29     4     4  src/misc/cocitation.c
  14    19    12    17  include/igraph_cocitation.h
   7     4     1     1  tests/unit/igraph_similarity.c
   2     0     0     0  tests/unit/igraph_similarity.out
   7     6     7     6  examples/simple/igraph_similarity.c
 375   362   371   358  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0810-similarity-jaccard.md`: Fully resolved (11→0 add, 0→0 del). The file now exists on main-dev.
- `src/misc/cocitation.c`: Reduced from 33/29 to 4/4. Remaining differences are unrelated changes (copyright header, `igraph_degree` call, `igraph_neighbors` call, `igraph_edges` call, convex hull removal) belonging to other changelog entries.
- `include/igraph_cocitation.h`: Reduced from 14/19 to 12/17. Remaining diffs are header reformatting (`__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, copyright, `const` removal on other functions) from other entries.
- `tests/unit/igraph_similarity.c`: Reduced from 7/4 to 1/1. Remaining diff is a copyright header change.
- `tests/unit/igraph_similarity.out`: Fully resolved (2→0).
- `examples/simple/igraph_similarity.c`: Unchanged at 7/6. The remaining diffs are unrelated (header reformatting, `igraph_integer_t` → `igraph_int_t`, `igraph_setup()` addition, `IGRAPH_NO_LOOPS` vs `0`) from other entries.
- `interfaces/functions.yaml`: Reduced from 375/362 to 371/358. The 4-line reduction matches the 2 entries changed (jaccard + dice, 2 lines each for PARAMS/DEPS).
