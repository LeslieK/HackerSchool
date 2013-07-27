# Topological sort is the reverse post order of running DFS on a DAG (Directed Acyclic Graph)

class DFOrder(object):
	def __init__(self, G):
		self._marked = [False for _ in range(G.V())]
		self._stack = []
		# run DFS on G; after a vertex is done, push it on a stack
		for v in range(G.V()):
			if not self._marked[v]:
				self._dfs(G, v)

	def _dfs(self, G, v):
		self._marked[v] = True
		for w in G.adj(v):
			if not self._marked[w]:
				self._dfs(G, w)
		# done with v
		self._stack.append(v)

	def reversePost(self):
		"return stack in reverse post order"
		return self._stack[::-1]




