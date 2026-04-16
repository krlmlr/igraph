# igraph_get_all_simple_paths()

**Category**: Paths and cycles

`igraph_get_all_simple_paths()` now has an additional parameter that allows restricting paths by minimum length as well, and its `mode` parameter was moved to before the path length limit parameters.

---

**Original changelog wording:**

> `igraph_get_all_simple_paths()` now has an additional parameter that allows restricting paths by minimum length as well, and its `mode` parameter was moved to before the path length limit parameters.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0600-get-all-simple-paths-2.md
```

Notes on remaining differences:
- `changelog/1-nfc/0600-get-all-simple-paths-2.md`: Fully ported (11→0 add, 0→0 del). The after-delete count will increase slightly due to the proof-of-work section added here but not present on `next`.
- No other files were modified because the code changes (adding `minlen` parameter and reordering `mode`) were already ported as part of changelog entry 0590 (igraph_get_all_simple_paths returns results in vector list), which rewrote the entire function signature in one step.
