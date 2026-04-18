# igraph_community_label_propagation()

`igraph_community_label_propagation()` gained the `igraph_lpa_variant_t lpa_variant` parameter to allow specification of label propagation algorithm (LPA) variants. A new fast label propagation variant was added. Set `lpa_variant=DOMINANCE` to select the algorithm used up to igraph 0.10.

---

**Original changelog wording:**

> `igraph_community_label_propagation()` gained the `igraph_lpa_variant_t lpa_variant` parameter to allow specification of label propagation algorithm (LPA) variants. A new fast label propagation variant was added. Set `lpa_variant=DOMINANCE` to select the algorithm used up to igraph 0.10.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0240-community-label-propagation.md
 505   197     1     1  src/community/label_propagation.c
  16    18    14    17  include/igraph_community.h
  85    48    70    48  include/igraph_constants.h
 321   351   320   350  interfaces/functions.yaml
  31    41    31    46  interfaces/types.yaml
  66    25     0     0  tests/unit/community_label_propagation.c
   5     5     2     2  tests/unit/community_label_propagation2.c
   1     1     0     0  tests/unit/community_label_propagation2.out
   2     4     1     3  tests/unit/community_label_propagation3.c
  12     4    11     3  tests/unit/community_indexing.c
  21     8    17     7  tests/unit/null_communities.c
   8     7     6     5  examples/simple/igraph_community_label_propagation.c
```

Notes on remaining differences:
- `src/community/label_propagation.c`: Massive reduction (505→1 add, 197→1 del). The remaining 1/1 is the `igraph_neighbors` call which uses 4 args on `main-dev` vs 6 args on `next` (from a different changelog entry).
- `include/igraph_community.h`: Small remaining diff (14/17) from unrelated NFC changes (copyright, `__BEGIN_DECLS`, `const` parameter).
- `include/igraph_constants.h`: Remaining diff (70/48) from unrelated NFC changes (`__END_DECLS` → `IGRAPH_END_C_DECLS`, etc.).
- `interfaces/types.yaml`: Increase (41→46 del) because the LPA_VARIANT type was added but `next` has other type renames (ARPACKFUNC→ARPACK_FUNC, LEVCFUNC→LEVC_FUNC) that introduce new deletions.
- Test/example files: Nearly all reduced to 0 or minimal remaining NFC diffs.
- `changelog/2-added/0240-community-label-propagation.md`: Fully ported. Del-after remains 0 because `next` doesn't have the proof-of-work section.
