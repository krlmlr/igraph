# igraph_setup()

`igraph_setup()` performs all initialization tasks that are recommended before using the igraph library. Right now this function only initializes igraph's internal random number generator with a practically random seed, but it may also perform other tasks in the future. It is recommended to call this function before using any other function from the library (although most of the functions will work fine now even if this function is not called).

---

**Original changelog wording:**

> `igraph_setup()` performs all initialization tasks that are recommended before using the igraph library. Right now this function only initializes igraph's internal random number generator with a practically random seed, but it may also perform other tasks in the future. It is recommended to call this function before using any other function from the library (although most of the functions will work fine now even if this function is not called).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0370-setup.md
```

Notes on remaining differences:
- `igraph_setup()` was already fully ported to main-dev (header, implementation, test all present and identical to next)
- Only the changelog entry was missing
