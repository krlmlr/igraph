# Leiden

Expose `igraph_community_leiden_simple()` .

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  95    55    86    55  interfaces/functions.yaml
   0     0     0     0  changelog/2-added/0410-leiden.md
```

Shortstat:

```
Before:  811 files changed, 10550 insertions(+), 6208 deletions(-)
After:   811 files changed, 10541 insertions(+), 6208 deletions(-)
```

Notes on remaining differences:

- `interfaces/functions.yaml` diff to `next` decreased from 95/55 to
  86/55 (the 9 inserted lines are the new `igraph_community_leiden_simple`
  Stimulus declaration that just landed on `main-dev`). The remaining
  86/55 delta belongs to the still-unported sub-changes of
  `changelog/1-nfc/0970-stimulus.md`.
- Source-level doc and comment additions on `src/community/leiden.c`,
  the `igraph_setup()` call in `examples/simple/igraph_community_leiden.c`,
  and the `igraph_vector_range` refactor in `tests/unit/community_leiden.c`
  on `next` are not part of "exposing" the function and belong to other
  changelog entries (documentation improvements, vector helpers, and
  the `igraph_setup()` init refactor respectively); they are left
  untouched here.
