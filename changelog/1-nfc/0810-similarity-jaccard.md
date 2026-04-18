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
  14    19    12    17  include/igraph_cocitation.h
  33    29     4     4  src/misc/cocitation.c
   7     4     1     1  tests/unit/igraph_similarity.c
   2     0     0     0  tests/unit/igraph_similarity.out
   7     6     5     4  examples/simple/igraph_similarity.c
 375   362   371   358  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0810-similarity-jaccard.md`: Fully ported (11→0 add, 0→0 del). The file now exists on main-dev.
- `include/igraph_cocitation.h`: Remaining diff (12 add, 17 del) is from unrelated changes: copyright/license header updates, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, and `const` removal on other function parameters (cocitation, bibcoupling, inverse_log_weighted, jaccard_es, dice_es).
- `src/misc/cocitation.c`: Large reduction (33→4 add, 29→4 del). Remaining 4/4 are unrelated: `igraph_degree` `true`→`IGRAPH_LOOPS`, `igraph_neighbors` extra params, and `igraph_edges` extra param changes from other entries.
- `tests/unit/igraph_similarity.c`: Reduced from 7→1 add, 4→1 del. Remaining diff is unrelated copyright header change.
- `tests/unit/igraph_similarity.out`: Fully ported (2→0).
- `examples/simple/igraph_similarity.c`: Remaining diff (5 add, 4 del) is from unrelated changes: copyright/modeline cleanup, `igraph_integer_t`→`igraph_int_t`, and `igraph_setup()` addition.
- `interfaces/functions.yaml`: Small reduction (375→371 add, 362→358 del). The 4-line reduction corresponds to the two function entries changed. Remaining diff is from all other unported function entries.
