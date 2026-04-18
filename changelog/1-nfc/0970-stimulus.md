# Update Stimulus types and functions

Various updates to Stimulus types, resulting in signature changes. In addition to that, various updates to function definitions. When backporting this change, create one commit per change.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  25    30     0     0  interfaces/types.yaml
 123    83    95    55  interfaces/functions.yaml
   0     0     0     0  changelog/1-nfc/0970-stimulus.md
```

Shortstat:

```
Before:  812 files changed, 10603 insertions(+), 6266 deletions(-)
After:   811 files changed, 10550 insertions(+), 6208 deletions(-)
```

Notes on remaining differences:

- `interfaces/types.yaml` is now fully aligned with `next` (diff = 0/0).
- `interfaces/functions.yaml` still differs by 95/55 lines because this
  port only covers Stimulus type renames (callbacks, options, storage,
  `EDGE_CAPACITIES`, `MSTALGORITHM`, `INTEGER`/`EDGE`/`VERTEX` CTYPE,
  `LEIDEN_OBJECTIVE`, `LPA_VARIANT` relocation, removal of `LONGINT`
  and `ERDOS_RENYI_TYPE`). The remaining function-level changes
  (`FLAGS: no_rng` additions, extra `DEPS` entries, `cutoff=-1` →
  `cutoff=UNLIMITED`, parameter additions such as `weights` for
  assortativity, and the `circle` → `cycle` rename on `igraph_girth`)
  are deferred to subsequent commits per the "create one commit per
  change" directive above.
- The changelog file entry itself contributes 0 lines to the diff to
  `next` because this markdown file is identical to the copy on `next`
  (the proof-of-work section is scoped out of the `--numstat` call via
  `:!/changelog`).
