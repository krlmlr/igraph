# igraph_setup()

`igraph_setup()` performs all initialization tasks that are recommended before using the igraph library. Right now this function only initializes igraph's internal random number generator with a practically random seed, but it may also perform other tasks in the future. It is recommended to call this function before using any other function from the library (although most of the functions will work fine now even if this function is not called).

---

**Original changelog wording:**

> `igraph_setup()` performs all initialization tasks that are recommended before using the igraph library. Right now this function only initializes igraph's internal random number generator with a practically random seed, but it may also perform other tasks in the future. It is recommended to call this function before using any other function from the library (although most of the functions will work fine now even if this function is not called).
