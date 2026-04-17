# igraph_eigenvector_centrality(), igraph_centralization_eigenvector_centrality(), igraph_centralization_eigenvector_centrality_tmax()

**Category**: Centralities

`igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` no longer have a `scale` parameter. The result is now always scaled so that the largest centrality value is 1.

---

**Original changelog wording:**

> `igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` no longer have a `scale` parameter. The result is now always scaled so that the largest centrality value is 1.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0740-eigenvector-centrality-2.md
  57    71    40    50  include/igraph_centrality.h
 139    86    25     5  src/centrality/eigenvector.c
  20    47    13     9  src/centrality/centralization.c
   6    10     3     7  tests/unit/igraph_eigenvector_centrality.c
   1     2     1     1  tests/unit/centralization.c
   6     4     4     2  examples/simple/eigenvector_centrality.c
   5     4     5     3  examples/simple/centralization.c
 399   380   396   377  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0740-eigenvector-centrality-2.md`: 11→0 adds (file ported); now 0/0 since file matches `next` except for the proof-of-work section (which `next` doesn't have, accounting for deletions in `next`'s perspective).
- `include/igraph_centrality.h`: 57→40 adds, 71→50 dels. Remaining differences are unrelated NFC changes (copyright headers, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `const igraph_vs_t`→`igraph_vs_t`, pagerank signature changes, removal of deprecated `igraph_hub_score`/`igraph_authority_score`).
- `src/centrality/eigenvector.c`: Major reduction (139→25 adds, 86→5 dels). Remaining diffs are NFC (copyright, whitespace, `igraph_cycles.h` include).
- `src/centrality/centralization.c`: 20→13 adds, 47→9 dels. Remaining diffs are NFC (copyright, whitespace, doc comment changes for other functions).
- `tests/unit/igraph_eigenvector_centrality.c`: 6→3 adds, 10→7 dels. Remaining diffs are NFC (copyright, `#include <igraph.h>` vs `"igraph.h"`, brace style).
- `tests/unit/centralization.c`: Minimal remaining (1/1), just NFC copyright.
- `examples/simple/eigenvector_centrality.c`: 6→4 adds, 4→2 dels. Remaining diffs are NFC (copyright) and `igraph_setup()` call (later entry).
- `examples/simple/centralization.c`: 5→5 adds, 4→3 dels. Small increase in adds (1) is from removing `/*scale=*/ true,` which shifts a comment. Remaining diffs are NFC.
- `interfaces/functions.yaml`: 399→396 adds, 380→377 dels. Bulk of remaining diffs are unrelated (FLAGS, type renames, other function changes).
