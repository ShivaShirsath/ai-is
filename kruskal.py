"""
Greedy Algorithm

The greedy method is one of the strategies like Divide and conquer used to solve the problems. This method is used for solving optimization problems. An optimization problem is a problem that demands either maximum or minimum results. Let's understand through some terms.

The Greedy method is the simplest and straightforward approach. It is not an algorithm, but it is a technique. The main function of this approach is that the decision is taken on the basis of the currently available information. Whatever the current information is present, the decision is made without worrying about the effect of the current decision in future.

This technique is basically used to determine the feasible solution that may or may not be optimal. The feasible solution is a subset that satisfies the given criteria. The optimal solution is the solution which is the best and the most favorable solution in the subset. In the case of feasible, if more than one solution satisfies the given criteria then those solutions will be considered as the feasible, whereas the optimal solution is the best solution among all the solutions.

Kruskal's Algorithm

Spanning tree - A spanning tree is the subgraph of an undirected connected graph.
Minimum Spanning tree - Minimum spanning tree can be defined as the spanning tree in which the sum of the weights of the edge is minimum. The weight of the spanning tree is the sum of the weights given to the edges of the spanning tree.

Kruskal's Algorithm is used to find the minimum spanning tree for a connected weighted graph. The main target of the algorithm is to find the subset of edges by using which we can traverse every vertex of the graph. It follows the greedy approach that finds an optimum solution at every stage instead of focusing on a global optimum.

Algorithm

Step 1: Create a forest F in such a way that every vertex of the graph is a separate tree.  
Step 2: Create a set E that contains all the edges of the graph.  
Step 3: Repeat Steps 4 and 5 while E is NOT EMPTY and F is not spanning  
Step 4: Remove an edge from E with minimum weight  
Step 5: IF the edge obtained in Step 4 connects two different trees, then 
		add it to the forest F (for combining two trees into one tree).  
	ELSE
		Discard the edge  
Step 6: END

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
