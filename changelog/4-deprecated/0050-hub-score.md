# igraph_hub_score(), igraph_authority_score()

The deprecated `igraph_hub_score()` and `igraph_authority_score()` were removed.

---

**Original changelog wording:**

> The deprecated `igraph_hub_score()` and `igraph_authority_score()` were removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0050-hub-score.md
   3   109     3     6  src/centrality/hub_authority.c
  16    32    16    21  include/igraph_centrality.h
 304   335   304   321  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/centrality/hub_authority.c`: del decreased 109→6. Remaining 3/6 are copyright header NFC.
- `include/igraph_centrality.h`: del decreased 32→21. Remaining are from other entries (copyright, `__BEGIN_DECLS`/`__END_DECLS`, other changes).
- `interfaces/functions.yaml`: del decreased 335→321 (14 lines removed for the two entries).
- Changelog fully ported (0/0 after).
