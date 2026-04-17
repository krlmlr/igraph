# igraph_community_leading_eigenvector()

**Category**: Community detection

The `history` parameter of `igraph_community_leading_eigenvector()` is now a pointer to an `igraph_vector_int_t` instead of an `igraph_vector_t`.

---

**Original changelog wording:**

> The `history` parameter of `igraph_community_leading_eigenvector()` is now a pointer to an `igraph_vector_int_t` instead of an `igraph_vector_t`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0640-community-leading-eigenvector.md
  45    25    44    24  include/igraph_community.h
  22    21     8     7  src/community/leading_eigenvector.c
 420   384   419   383  interfaces/functions.yaml
   4     5     1     2  tests/unit/levc-stress.c
```

Notes on remaining differences:
- `changelog/1-nfc/0640-community-leading-eigenvector.md`: Now 0/0 (fully ported). Before showed 11/0 because the file didn't exist yet on main-dev.
- `include/igraph_community.h`: Reduced by 1/1. Remaining differences are unrelated changes (copyright headers, other function signatures from later entries).
- `src/community/leading_eigenvector.c`: Reduced by 14/14. The history type change and all push_back calls are ported. Remaining differences are copyright header changes and other unrelated cleanups.
- `interfaces/functions.yaml`: Reduced by 1/1. Only the `VECTOR` → `VECTOR_INT` change for history was applied. Remaining differences are from other entries.
- `tests/unit/levc-stress.c`: Reduced by 3/3. Remaining differences are copyright header changes.
