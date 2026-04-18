# Assortativity

Add weight argument to `igraph_assortativity()` and `igraph_assortativity_nominal()` .

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  86    55    79    53  interfaces/functions.yaml
  14    19     4     8  include/igraph_mixing.h
 117    66     0     0  src/misc/mixing.c
  23    27     0     0  tests/unit/assortativity.c
  22    19     0     0  tests/unit/igraph_joint_degree_distribution.c
   1     1     0     0  tests/unit/igraph_joint_type_distribution.c
   4     1     0     0  examples/simple/igraph_assortativity_degree.c
   9     6     0     0  examples/simple/igraph_assortativity_nominal.c
   0     0     0     0  changelog/3-modified/0070-assortativity.md
```

Shortstat:

```
Before:  811 files changed, 10541 insertions(+), 6208 deletions(-)
After:   805 files changed, 10348 insertions(+), 6075 deletions(-)
```

Notes on remaining differences:

- `src/misc/mixing.c`, both assortativity examples and all three
  affected unit tests are now fully aligned with `next` (0/0).
- `include/igraph_mixing.h` keeps a 4/8 delta because the unrelated
  copyright-header refresh and the `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`
  rename are left to other changelog entries; only the assortativity
  signature change is pulled in here.
- `interfaces/functions.yaml` shrinks from 86/55 to 79/53: the 7/2
  reduction matches the two new `DEPS` lines and parameter rearrangement
  for the assortativity entries. The residual 79/53 belongs to
  still-unported sub-changes of `changelog/1-nfc/0970-stimulus.md`.
- `joint_type_distribution.c`, `joint_degree_distribution.c` and the
  assortativity tests/examples were taken wholesale from `next` because
  the few incidental edits they carry (e.g. `true` → `IGRAPH_LOOPS` for
  `igraph_strength`, usage of `igraph_vector_range`) are small and would
  otherwise have to be re-synchronised later — there is no conflicting
  not-yet-ported change that would break by including them now. Build
  + the full set of affected ctests (`assortativity`,
  `igraph_joint_degree_distribution`, `igraph_joint_type_distribution`,
  `example::igraph_assortativity_degree`,
  `example::igraph_assortativity_nominal`) all pass.
