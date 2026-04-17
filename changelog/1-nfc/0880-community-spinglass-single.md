# igraph_community_spinglass_single()

**Category**: Bug fixes

`igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output parameters, as these return not simply edge counts, but the sum of the weights of some edges. Thus these results are no longer incorrectly rounded.

---

**Original changelog wording:**

> `igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output parameters, as these return not simply edge counts, but the sum of the weights of some edges. Thus these results are no longer incorrectly rounded.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0880-community-spinglass-single.md
  40    21    38    19  include/igraph_community.h
  14    23     7    17  src/community/spinglass/clustertool.cpp
   3     4     1     2  src/community/spinglass/pottsmodel_2.cpp
   3     4     1     2  src/community/spinglass/pottsmodel_2.h
   2     5     1     3  tests/unit/spinglass.c
 371   358   370   357  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0880-community-spinglass-single.md`: Fully ported (11→0 add).
- `include/igraph_community.h`: Reduced from 40→38 add, 21→19 del. The 2-line reduction matches the two parameter type changes. Remaining diffs are from other entries (copyright, `__BEGIN_DECLS`, deprecated function removal, other parameter changes).
- `src/community/spinglass/clustertool.cpp`: Reduced from 14→7 add, 23→17 del. Ported parameter type and doc changes. Remaining diffs are copyright and other unrelated changes.
- `src/community/spinglass/pottsmodel_2.cpp` and `.h`: Reduced from 3→1 add, 4→2 del each. Remaining diffs are copyright header changes.
- `tests/unit/spinglass.c`: Reduced from 2→1 add, 5→3 del. Remaining diffs are copyright and variable cleanup from other entries.
- `interfaces/functions.yaml`: Reduced from 371→370 add, 358→357 del. The 1-line reduction corresponds to the PARAMS type change. Remaining diff is from all other unported entries.
