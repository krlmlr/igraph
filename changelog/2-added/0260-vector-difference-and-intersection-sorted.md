# igraph_vector_difference_and_intersection_sorted()

`igraph_vector_difference_and_intersection_sorted()` calculates the intersection and the differences of two vectors simultaneously.

---

**Original changelog wording:**

> `igraph_vector_difference_and_intersection_sorted()` calculates the intersection and the differences of two vectors simultaneously.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0260-vector-difference-and-intersection-sorted.md
```

Notes on remaining differences:
- `changelog/2-added/0260-vector-difference-and-intersection-sorted.md`: Fully ported (9→0). The function was already ported in an earlier entry. This adds the dedicated changelog file.
