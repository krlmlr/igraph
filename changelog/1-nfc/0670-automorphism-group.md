# igraph_automorphism_group(), igraph_automorphism_group_bliss(), igraph_automorphism_group()

**Category**: Isomorphism functions and permutations

`igraph_automorphism_group()` has been renamed to `igraph_automorphism_group_bliss()` because it has a BLISS-specific interface. A new `igraph_automorphism_group()` function was added with a simplified interface that does not depend on BLISS.

---

**Original changelog wording:**

> `igraph_automorphism_group()` has been renamed to `igraph_automorphism_group_bliss()` because it has a BLISS-specific interface. A new `igraph_automorphism_group()` function was added with a simplified interface that does not depend on BLISS.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0670-automorphism-group.md
  22    57    21    60  include/igraph_isomorphism.h
  89    14    51    11  src/isomorphism/bliss.cc
   5     7     1     3  tests/unit/isomorphism_test.c
   4     4     2     2  fuzzing/bliss.cpp
   6    16     4    15  doc/isomorphism.xxml
 417   386   416   390  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0670-automorphism-group.md`: Dropped from 11/0 to 0/0 — fully ported (the file now exists on main-dev). The after shows 0/0 because the proof-of-work section we added doesn't exist on `next`.
- `include/igraph_isomorphism.h`: add decreased 22→21, del increased 57→60. The remaining diffs are unrelated changes (copyright header, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, removal of deprecated functions, `igraph_canonical_permutation` rename, `igraph_isoclass_subgraph` signature change, etc.) belonging to other changelog entries. The small del increase (3 lines) is because the new `igraph_automorphism_group()` declaration adds 4 lines that partially overlap with what `next` expects.
- `src/isomorphism/bliss.cc`: add decreased 89→51, del decreased 14→11. Large reduction because the `igraph_automorphism_group`/`igraph_automorphism_group_bliss` rename and wrapper were the major changes. Remaining diffs are `igraph_canonical_permutation` rename, `igraph_allow_interruption` change, copyright header changes.
- `tests/unit/isomorphism_test.c`: add decreased 5→1, del decreased 7→3. Remaining diffs are whitespace/comment changes unrelated to this entry.
- `fuzzing/bliss.cpp`: add decreased 4→2, del decreased 4→2. Remaining diffs are copyright header and `igraph_integer_t`→`igraph_int_t` changes.
- `doc/isomorphism.xxml`: add decreased 6→4, del decreased 16→15. Remaining diffs are removal of deprecated sections and `igraph_canonical_permutation` rename.
- `interfaces/functions.yaml`: add decreased 417→416, del increased 386→390. The small increase in del (4 lines) is because we added the new `igraph_automorphism_group` entry (4 lines) which `next` also has but with different type names (`VERTEX_COLORS` vs `VERTEX_COLOR`). Remaining large diff is due to many other function changes across the file.
