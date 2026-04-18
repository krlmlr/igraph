# igraph_simple_cycles()

`igraph_simple_cycles()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

**Original changelog wording:**

> `igraph_simple_cycles()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0310-simple-cycles.md
```

Notes on remaining differences:
- Changelog-only port. The `max_results` parameter for `igraph_simple_cycles()` was already present on `main-dev` from a prior porting effort.
