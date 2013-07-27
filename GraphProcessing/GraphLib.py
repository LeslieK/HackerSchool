
from collections import Counter
import random

## build a Graph 
## V = number of vertices
## E = number of edges
class Graph(object):
	"""defines a undirected graph class"""
	def __init__(self, V, E=None):
		self._V = V
		self._adj = []
		for v in range(self._V):
			self._adj.append(Counter())
		if E:
			# builds a random graph with E edges
			for e in range(E):
				v = int(random.random() * V)
				w = int(random.random() * V)
				self.addEdge(v, w)
				print '{0} to {1}'.format(v, w)	

	def addEdge(self, v, w):
		"add edge v - w (parallel edges and self-loops allowed)"
		self._adj[v][w] += 1
		self._adj[w][v] += 1

	def adj(self, v):
		"return all vertices adjacent to v"
		return self._adj[v]

	def V(self):
		"number of vertices"
		return self._V

	def E(self):
		"number of edges (incl self-loops and parallel edges)"
		e = 0
		for v in range(self._V):
			e = sum(self._adj[v].values()) + e
		return e/2

	def _isSelfLoop(self, v, w):
		return v == w

	def showEdges(self):
		"shows 1 of each edge; if parallel edges, just shows 1 of them"
		edict = {}
		for v in range(self._V):
			for w in self.adj(v):
				if (w, v) not in edict:
					edict[tuple([v, w])] = True
					print '{0} to {1}'.format(v, w)

	def removeEdge(self, v, w):
		if w not in self.adj(v):
			print "no such edge"
		else:
			self._adj[v][w] -= 1
			self._adj[w][v] -= 1
			if not self._adj[v][w]:
				del(self._adj[v][w])
				del(self._adj[w][v])

class Digraph(object):
	"""defines a undirected graph class"""
	def __init__(self, V):
		self._V = V
		self._adj = []
		for v in range(self._V):
			self._adj.append(Counter())

	def addEdge(self, v, w):
		"add edge v - w (parallel edges and self-loops allowed)"
		self._adj[v][w] += 1

	def adj(self, v):
		"return all vertices adjacent to v"
		return self._adj[v]

	def V(self):
		"number of vertices"
		return self._V

	def E(self):
		"number of edges (incl self-loops and parallel edges)"
		e = 0
		for v in range(self._V):
			e = sum(self._adj[v].values()) + e
		return e

	def _isSelfLoop(self, v, w):
		return v == w

	def showEdges(self):
		"shows each directed edge"
		for v in range(self._V):
			for w in self.adj(v):
				print '{0} to {1}'.format(v, w)

	def removeEdge(self, v, w):
		if w not in self.adj(v):
			print "no such edge"
		else:
			self._adj[v][w] -= 1
			if not self._adj[v][w]:
				del(self._adj[v][w])

	def reverse(self):
		R = Digraph(self._V)
		for v in range(self._V):
			for w in self._adj[v]:
				R.addEdge(w, v)
		return R

			
