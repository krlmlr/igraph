# igraph_vs_seq() and 4 others

The deprecated `igraph_vs_seq()`, `igraph_vss_seq()`, `igraph_es_seq()`, `igraph_ess_range()`, and `igraph_vector_init_seq()` were removed. Use the `range` alternatives instead of the old `seq` ones.

---

**Original changelog wording:**

> The deprecated `igraph_vs_seq()`, `igraph_vss_seq()`, `igraph_es_seq()`, `igraph_ess_range()`, and `igraph_vector_init_seq()` were removed. Use the `range` alternatives instead of the old `seq` ones.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
    9      0      -      -  changelog/4-deprecated/0340-vs-seq.md
    5     17      5     11  include/igraph_iterators.h
    4     11      4     10  include/igraph_vector_pmt.h
   51     60     51     28  src/core/vector.pmt
   12     89     12      2  src/graph/iterators.c
```

Notes on remaining differences:
- `changelog/4-deprecated/0340-vs-seq.md`: Before 9+/0-: file didn't exist on main-dev. After: `-` means the file now matches `next` (ignoring the proof-of-work section added here, which next doesn't have).
- `include/igraph_iterators.h`: Deletions decreased 17→11. The 6-line decrease corresponds to the 3 removed declaration lines (2 for vs_seq/vss_seq, 2 for es_seq/ess_seq, plus 2 blank lines). Remaining 5+/11- are from copyright header updates, `__BEGIN_DECLS`/`__END_DECLS` → `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS`, and removal of `IGRAPH_ES_UNUSED_WAS_MULTIPAIRS` — all belong to later entries.
- `include/igraph_vector_pmt.h`: Deletions decreased 11→10. The 1-line decrease is the removed `init_seq` declaration. Remaining 4+/10- are copyright header updates, `__BEGIN_DECLS`/`__END_DECLS`, blank line removal, and `index_int`→`index_in_place` rename — all later entries.
- `src/core/vector.pmt`: Deletions decreased 60→28. The 32-line decrease is the removed `igraph_vector_init_seq` function (doc comment + implementation). Remaining 51+/28- are from other entries (OOM macro changes, doc rewrites, `index_int`→`index_in_place`, typo fixes, `\experimental` removal, copyright header, etc.).
- `src/graph/iterators.c`: Deletions decreased 89→2. The 87-line decrease is the removal of 4 deprecated functions (`igraph_vs_seq`, `igraph_vss_seq`, `igraph_es_seq`, `igraph_ess_seq`) with their doc comments. Remaining 12+/2- are doc additions for `igraph_vs_adj` parameters and copyright header changes — later entries.
