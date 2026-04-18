# igraph_attribute_type_t

**Category**: Attribute handling

The deprecated `IGRAPH_ATTRIBUTE_DEFAULT` value of the `igraph_attribute_type_t` enum was removed.

---

**Original changelog wording:**

> The deprecated `IGRAPH_ATTRIBUTE_DEFAULT` value of the `igraph_attribute_type_t` enum was removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0350-attribute-type-t.md
 123   124   123   123  include/igraph_attributes.h
```

Notes on remaining differences:
- `changelog/1-nfc/0350-attribute-type-t.md`: Before had 11 added lines (file existed on next but not main-dev). After: 0/0 because the file now exists on main-dev. The after stats don't show it because the proof-of-work section we added is not on next, but the base content matches.
- `include/igraph_attributes.h`: Insertions stayed at 123, deletions decreased from 124 to 123 (the removed `IGRAPH_ATTRIBUTE_DEFAULT` line). Remaining 123/123 diff is from other changelog entries (doc reorganization, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, struct reordering, comment changes, etc.).
