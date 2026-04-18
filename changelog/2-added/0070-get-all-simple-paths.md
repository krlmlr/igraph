# igraph_get_all_simple_paths()

`igraph_get_all_simple_paths()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

**Original changelog wording:**

> `igraph_get_all_simple_paths()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0070-get-all-simple-paths.md
```

Notes on remaining differences:
- The `max_results` parameter was already ported in an earlier NFC entry. No additional code changes needed.
