# igraph_count_automorphisms(), igraph_count_automorphisms_bliss(), igraph_count_automorphisms()

**Category**: Isomorphism functions and permutations

`igraph_count_automorphisms()` has been renamed to `igraph_count_automorphisms_bliss()` because it has a BLISS-specific interface. A new `igraph_count_automorphisms()` function was added with a simplified interface that does not depend on BLISS.

---

**Original changelog wording:**

> `igraph_count_automorphisms()` has been renamed to `igraph_count_automorphisms_bliss()` because it has a BLISS-specific interface. A new `igraph_count_automorphisms()` function was added with a simplified interface that does not depend on BLISS.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  23    58    22    57  include/igraph_isomorphism.h
 136    23    89    14  src/isomorphism/bliss.cc
   2     2     1     1  tests/unit/bliss_automorphisms.c
  13    17     5     7  tests/unit/isomorphism_test.c
 418   382   417   386  interfaces/functions.yaml
```

Notes on remaining differences:
- include/igraph_isomorphism.h: Remaining diff (22 add, 57 del) is from other changelog entries (copyright header changes, removal of deprecated functions like `igraph_isomorphic_function_vf2`, `igraph_subisomorphic_function_vf2`, `igraph_isomorphic_34`, DAG function removals, `igraph_automorphism_group`/`igraph_canonical_permutation` renames, LAD signature change, `igraph_isoclass_subgraph` signature change). Both add and del decreased by 1.
- src/isomorphism/bliss.cc: Remaining diff (89 add, 14 del) is from other entries (copyright changes, `igraph_canonical_permutation` rename, `igraph_automorphism_group` rename, interrupt check fix). Decreased significantly (136→89 add, 23→14 del) because the new `igraph_count_automorphisms` wrapper and `igraph_count_automorphisms_bliss` rename were ported.
- tests/unit/bliss_automorphisms.c: Remaining diff (1 add, 1 del) is from a copyright header change. Decreased from 2/2 to 1/1.
- tests/unit/isomorphism_test.c: Remaining diff (5 add, 7 del) is from other entries (`igraph_automorphism_group` → `igraph_automorphism_group_bliss` rename, whitespace changes). Decreased significantly (13→5 add, 17→7 del).
- interfaces/functions.yaml: Remaining diff (417 add, 386 del) is from many other entries. Add decreased by 1, del increased by 4 due to the new `igraph_count_automorphisms` entry being added on `main-dev` but not yet present as a separate entry on `next` (it's inline in the same position). The `VERTEX_COLOR` → `VERTEX_COLORS` type rename and other function renames account for the bulk of remaining diff.
