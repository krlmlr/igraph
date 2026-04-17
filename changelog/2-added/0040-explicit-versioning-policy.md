# Explicit versioning policy.

Explicit versioning policy.

---

**Original changelog wording:**

> Explicit versioning policy.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  58     0     0     0  VERSIONING.md
   9     0     0     0  changelog/2-added/0040-explicit-versioning-policy.md
```

Notes on remaining differences:
- Both files are new and now match next exactly (0 remaining adds). The diff to next decreased by 67 lines (58 + 9).
