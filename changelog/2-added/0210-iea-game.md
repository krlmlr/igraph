# igraph_iea_game()

`igraph_iea_game()` samples random multigraphs through independent edge assignment.

---

**Original changelog wording:**

> `igraph_iea_game()` samples random multigraphs through independent edge assignment.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0210-iea-game.md
 322   354   321   351  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/2-added/0210-iea-game.md`: Fully ported (9→0 additions remaining). The del-after stays 0 because next doesn't have the proof-of-work section.
- `interfaces/functions.yaml`: Small decrease (322→321 add, 354→351 del) from reformatting `igraph_iea_game` PARAMS from multi-line to single-line. Remaining diffs are from other unported entries.
