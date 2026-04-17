# igraph_motifs_randesu_callback()

**Category**: Other network analysis

The `igraph_motifs_handler_t` callback type now takes a `const igraph_vector_int_t *vids` parameter. Previously this was not formally `const`, even though it was not allowed to modify `vids`. This affects uses of `igraph_motifs_randesu_callback()`.

---

**Original changelog wording:**

> The `igraph_motifs_handler_t` callback type now takes a `const igraph_vector_int_t *vids` parameter. Previously this was not formally `const`, even though it was not allowed to modify `vids`. This affects uses of `igraph_motifs_randesu_callback()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0820-motifs-randesu-callback.md
   8    17     7    16  include/igraph_motifs.h
  85    71    83    70  src/misc/motifs.c
   2     3     1     2  tests/unit/igraph_motifs_randesu.c
   8     5     6     3  examples/simple/igraph_motifs_randesu.c
```

Notes on remaining differences:
- `changelog/1-nfc/0820-motifs-randesu-callback.md`: Fully resolved (11→0 add).
- `include/igraph_motifs.h`: Reduced from 8/17 to 7/16. Remaining diffs are header reformatting (`__BEGIN_DECLS`, copyright, deprecated function removal, `const` removal on other functions).
- `src/misc/motifs.c`: Reduced from 85/71 to 83/70. Remaining diffs are reformatting (copyright, `father`→`parent` rename, function signature reformatting) from other entries.
- `tests/unit/igraph_motifs_randesu.c`: Reduced from 2/3 to 1/2. Remaining diff is copyright header change.
- `examples/simple/igraph_motifs_randesu.c`: Reduced from 8/5 to 6/3. Remaining diffs are copyright header, `igraph_setup()` addition, `igraph_integer_t`→`igraph_int_t` in loop variables.
