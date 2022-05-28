"""
Greedy Algorithm
The greedy method is one of the strategies like Divide and conquer used to solve the problems. This method is used for solving optimization problems. An optimization problem is a problem that demands either maximum or minimum results. Let's understand through some terms.

The Greedy method is the simplest and straightforward approach. It is not an algorithm, but it is a technique. The main function of this approach is that the decision is taken on the basis of the currently available information. Whatever the current information is present, the decision is made without worrying about the effect of the current decision in future.

This technique is basically used to determine the feasible solution that may or may not be optimal. The feasible solution is a subset that satisfies the given criteria. The optimal solution is the solution which is the best and the most favorable solution in the subset. In the case of feasible, if more than one solution satisfies the given criteria then those solutions will be considered as the feasible, whereas the optimal solution is the best solution among all the solutions.
"""
# Python program for Kruskal's algorithm to find Minimum Spanning Tree of a given connected, undirected and weighted graph
from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1
	def KruskalMST(self):
		result = []
		i, e = 0, 0
		self.graph = sorted(
			self.graph, 
			key=lambda item: item[2]
		)
		parent = []
		rank = []
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
		while e < self.V - 1:
			u, v, w = self.graph[i]
			i += 1
			x = self.find(parent, u)
			y = self.find(parent, v)
			if x != y:
				e += 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print(u, "--", v, "==", weight)
		print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
