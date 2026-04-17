# Several random graph generators, including the Erdős-Rényi generators, can no...

Several random graph generators, including the Erdős-Rényi generators, can now produce graphs with multi-edges.

---

**Original changelog wording:**

> Several random graph generators, including the Erdős-Rényi generators, can now produce graphs with multi-edges.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0030-several-random-graph-generators-including-the-erd.md
```

Notes on remaining differences:
- The multi-edge support for random graph generators (igraph_erdos_renyi_game_gnm, igraph_erdos_renyi_game_gnp, igraph_iea_game, gnm_multi helper) was already ported as part of earlier NFC changelog entries (1-nfc/0450, 0460). No additional code changes were needed for this entry.
- The changelog file itself reduces the diff by 9 additions (from 9 to 0) since the file now matches next.
