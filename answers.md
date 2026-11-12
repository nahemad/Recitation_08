# CMPS 2200 Recitation 08 Answers

**Name:** Nahema Dumonteil
**Name:**_________________________


Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?

Lets analyze the code. The outer while loop, would run at most n times because for n nodes, each node can be added to forntier at most once and can be popped at most once. The inner loop that checks for neighbors, for m edges each edge connects 2 nodes, so it can appear in 2 neighbor sets so the loop runs most 2m times total. Putting these together gives O(n+m). 

- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

The worst case of times we need to call reachable is 1. This is because the graph is undirected so it suffices to check if 1 arbitrary node can reach all other nodes to determine if its  connected or not. 

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

The work is going to also be O(n+m). This is because checking if
its nonempty, finiding the first node, and comparing the lengths all take constant time. So in the end calling reachable dominantes therefore O(n+m) is the work. 

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

An adjacency matrix for a graph with n nodes is an n*n matrix that has a 1 when 2 nodes are connected by an edge and a 0 when they are not. This layout changes the Work of "reachable" because we would have to check each row for each node to find the connecting nodes. This means we scan a row of n elements for n nodes so the Work becomes O(n^2) instead of O(n+m) as explained in question 2. 
