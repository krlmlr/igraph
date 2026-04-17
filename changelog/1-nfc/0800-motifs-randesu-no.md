# igraph_motifs_randesu_no(), igraph_motifs_randesu_estimate()

**Category**: Other network analysis

`igraph_motifs_randesu_no()` and `igraph_motifs_randesu_estimate()` now take an `igraph_real_t` as their `result` argument to prevent overflows when igraph is compiled with 32-bit integers.

---

**Original changelog wording:**

> `igraph_motifs_randesu_no()` and `igraph_motifs_randesu_estimate()` now take an `igraph_real_t` as their `result` argument to prevent overflows when igraph is compiled with 32-bit integers.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
11     0      -      -      changelog/1-nfc/0800-motifs-randesu-no.md
10     19     8      17     include/igraph_motifs.h
94     75     85     71     src/misc/motifs.c
4      4      1      1      tests/unit/igraph_motifs_randesu_no.c
4      4      1      1      tests/unit/igraph_motifs_randesu_estimate.c
377    364    375    362    interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0800-motifs-randesu-no.md`: File no longer appears in diff (was 11 add / 0 del) — fully ported. The proof-of-work section is only on main-dev, not on next, so the file content differs slightly but git sees them as matching for the changelog-relevant content.
- `include/igraph_motifs.h`: Reduced from 10/19 to 8/17. Remaining diff is unrelated changes (copyright header update, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, `const` qualifier on `vids`, `igraph_adjacent_triangles` deprecation removal, `__END_DECLS` → `IGRAPH_END_C_DECLS`).
- `src/misc/motifs.c`: Reduced from 94/75 to 85/71. Remaining diff is unrelated changes (`father` → `parent` rename, `igraph_neighbors()` parameter additions, copyright header, formatting, `IGRAPH_CHECK()` wrapping).
- `tests/unit/igraph_motifs_randesu_no.c` and `igraph_motifs_randesu_estimate.c`: Reduced from 4/4 to 1/1. Remaining diff is copyright header change (`IGraph` → `igraph`).
- `interfaces/functions.yaml`: Reduced from 377/364 to 375/362. Remaining diff is other function signature changes in the same file.
