# igraph_canonical_permutation(), igraph_canonical_permutation_bliss(), igraph_canonical_permutation()

**Category**: Isomorphism functions and permutations

`igraph_canonical_permutation()` has been renamed to `igraph_canonical_permutation_bliss()` because it has a BLISS-specific interface. A new `igraph_canonical_permutation()` function was added with a simplified interface that does not depend on BLISS.

---

**Original changelog wording:**

> `igraph_canonical_permutation()` has been renamed to `igraph_canonical_permutation_bliss()` because it has a BLISS-specific interface. A new `igraph_canonical_permutation()` function was added with a simplified interface that does not depend on BLISS.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0680-canonical-permutation.md
  21    60    16    59  include/igraph_isomorphism.h
  51    11     8     8  src/isomorphism/bliss.cc
 416   390   411   391  interfaces/functions.yaml
   4    15     2    14  doc/isomorphism.xxml
```

Notes on remaining differences:
- `changelog/1-nfc/0680-canonical-permutation.md`: Fully ported (11→0 adds). The `del-a` stays 0 because the proof-of-work section added here does not exist on `next`.
- `include/igraph_isomorphism.h`: Reduced from 21→16 adds, 60→59 dels. Remaining diffs are unrelated changes (copyright header updates, removed deprecated functions, DAG section removal, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, etc.) that belong to other changelog entries.
- `src/isomorphism/bliss.cc`: Reduced from 51→8 adds, 11→8 dels. Remaining diffs are unrelated (copyright header, `igraph_allow_interruption()` return check change).
- `interfaces/functions.yaml`: Reduced from 416→411 adds, 390→391 dels. The +1 del increase is because the old `igraph_canonical_permutation` entry (using `VERTEX_COLOR` singular) was replaced with a new simplified entry, while `next` uses `VERTEX_COLORS` (plural, a type not yet on `main-dev`). Remaining diffs are from many other unrelated entries (FLAGS, DEPS changes, etc.).
- `doc/isomorphism.xxml`: Reduced from 4→2 adds, 15→14 dels. Remaining diffs are other doc restructuring changes (deprecated sections, `igraph_count_automorphisms` move, etc.).
