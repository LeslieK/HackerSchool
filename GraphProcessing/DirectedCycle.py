# detect a directed cycle in a connected digraph using DFS
#
# DG = Digraph(13)
# DG.addEdge(v, w)
# ...
# dc = DirectedCycle(DG)
# dc.cycle()
# returns: 2 0 5 4 2

class DC(object):
	"find first directed cycle in a digraph"
	def __init__(self, G):
		self._marked = [(False, -1) for _ in range(G.V())]
		self._edgeTo = [-1 for _ in range(G.V())]
		self._cycle = []
		for v in range(G.V()):
			if not self._marked[v][0]:
				self._dfs(G, v, 0)

	def _dfs(self, G, v, level):
		if not self._cycle:
			self._marked[v] = (True, level)
			for w in G.adj(v):
				if not self._marked[w][0]:
					self._edgeTo[w] = v
					self._dfs(G, w, level + 1)
				elif level < self._marked[w][1]:
					# reached w from level above
					# not a cycle
					pass
				else:
					# found cycle
					x = v
					while (x != w):
						self._cycle.append(x)
						x = self._edgeTo[x]
					self._cycle.append(w)
					self._cycle.append(v)
					print self._cycle
					return
		else:
			return

	def cycle(self):
		if not self._cycle:
			print "no cycle"
		else:
			for _ in range(len(self._cycle)):
				print self._cycle.pop()

	def hasCycle(self):
		if not self._cycle:
			return False
		else:
			return True




