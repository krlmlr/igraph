# nanoflann was updated to version 1.9.0.

**Category**: Documentation, performance, and vendor updates

nanoflann was updated to version 1.9.0.

---

**Original changelog wording:**

> nanoflann was updated to version 1.9.0.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0920-nanoflann-was-updated-to-version-1-9-0.md
2813     0     0     0  vendor/nanoflann/nanoflann.hpp
```

Notes on remaining differences:
- `changelog/1-nfc/0920-...`: Fully ported (11→0 add).
- `vendor/nanoflann/nanoflann.hpp`: Fully ported (2813→0 add). The header-only library is now vendored on main-dev.
