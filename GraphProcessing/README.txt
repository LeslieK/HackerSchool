This folder contains programs I wrote to answer interview questions provided by the Algorithm II course (Princeton University), on Coursera. I took the course Spring 2013.

Undirected Graph Questions:

Diameter and center of a tree. Given a connected graph with no cycles
Diameter: design a linear-time algorithm to find the longest simple path in the graph.
Center: design a linear-time algorithm to find a vertex such that its maximum distance from any other vertex is minimized.
Solution: GraphCenter.py 				dependencies: BreadthFirstSearch.py, ConnectedComponent.py, Cycle.py, GraphLib.py
Solution: GraphDiameter.py 				dependencies: BreadthFirstSearch.py, ConnectedComponent.py, Cycle.py, GraphLib.py

Eulierian cycle. An Eulierian cycle in a graph is a cycle (not necessarily simple) that uses every edge in the graph exactly one.
Show that a graph has an Eulerian cycle if and only if it is both connected and every vertex has even degree.
Design a linear-time algorithm to determine whether a graph has an Eulerian cycle, and if so, find one.

Solution: EulerianCycle.py				dependencies: ConnectedComponent.py

Directed Graph Questions:

Find a Directed Cycle, if one exists. Use Depth First Search.
Solution: DirectedCycle.py				dependencies: none

Shortest directed cycle. Given a digraph G, design an efficient algorithm to find a directed cycle with the minimum number of edges (or report that the graph is acyclic). The running time of your algorithm should be at most proportional to V(E+V) and use space proportional to E+V, where V is the number of vertices and E is the number of edges.

Solution: ShortestDirectedCycle.py		dependencies: built-in modules

Hamiltonian path in a DAG. Given a directed acyclic graph, design a linear-time algorithm to determine whether it has a Hamiltonian path (a simple path that visits every vertex), and if so, find one.

Solution: Hamiltonian.py				dependencies: DepthFistOrder.py

Reachable vertex.
DAG: Design a linear-time algorithm to determine whether a DAG has a vertex that is reachable from every other vertex, and if so, find one.
Digraph: Design a linear-time algorithm to determine whether a digraph has a vertex that is reachable from every other vertex, and if so, find one.

Solution: Reachable.py					dependencies: DirectedCycle.py, DepthFirstOrder.py

KosarajuSharirSCC.py (dependency: DepthFirstOrder.py): This computers strongly connected components in a graph. I actually worked on this for about 10 hours before I continued to watch the Alogrithms class lecture on this topic and realized this was above my level!!! I just coded it up in python.

