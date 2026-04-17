# Various documentation improvements.

**Category**: Documentation, performance, and vendor updates

Various documentation improvements.

---

**Original changelog wording:**

> Various documentation improvements.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0940-various-documentation-improvements.md
```

Notes on remaining differences:
- `changelog/1-nfc/0940-...`: Fully ported (11→0 add).
- No code changes needed. The documentation improvements were already applied as part of the doc reorganization in the previous entry (0930). The doc/ directory is fully in sync with next.
