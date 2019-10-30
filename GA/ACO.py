#SOLVING TSP USING ACO WITH NODES 
# x_i = 0.1 * ((9+11i^2) mod 200)
# y_i = 0.1 * ((7+1723i) mod 200)
# where i = 1,...,n

import numpy as np

n = 30 #number of nodes
N = n #number of ants
a = 1 #importance of pheromones
b = 2 #importance of short edge
phi = 0.5 #vaporization rate (how much ignore previous information)
ITER = 200 #number of iterations to perform

pheros = np.ones((n,n)) #start with 1 pheromones concentration
points = np.zeros((n,2))
dists = np.ones((n,n))

for i in range(1, n+1):
	points[i-1, 0] = 0.1*(9+11*i**2 % 200)
	points[i-1, 1] = 0.1*(7+1723*i % 200)
	

for i in range(n-1):
	for j in range(i+1,n):
		dist = np.sqrt((points[i,0]-points[j,0])**2 + (points[i,1]-points[j,1])**2)
		dists[i, j] = dist
		dists[j, i] = dist

current_node = 0
path_len = 0
visited = {0}
for i in range(n-1):
	unvisited = [1000 if node in visited else 1 for node in range(n)]
	node = np.argmin(unvisited*dists[current_node])
	visited.add(node)
	path_len += dists[current_node, node]
	current_node = node
path_len += dists[current_node, 0]

pheros = N*1/path_len * pheros

print(path_len)
	
#we start at node 0. Nodes are 0,1,...,n
for iteration in range(ITER):

	pheros_delta = np.zeros((n,n)) #remember tau(i,j) = (1-phi)*tau_(i,j) + delta tau_(i,j)
	for ant in range(N):			# where delta tau_(i,j) sum over how much pheromones each ant secreted at this edge
		path_len = 0
		current_node = 0
		edges = [] #tuples (i,j) if nodes
		visited = {0} #set of visited nodes
		for i in range(n-1):
			weights = np.array([0 if node in visited else pheros[current_node, node]**a * 1/dists[current_node, node]**b 
								for node in range(n)])
			weights = weights/np.sum(weights)			
			node = np.random.choice(n, 1, p = weights)[0]		
			edges = edges + [(current_node, node)]
			path_len += dists[current_node, node]
			visited.add(node)
			current_node = node

		path_len += dists[current_node, 0]
		edges = edges + [(current_node, 0)]
		for (node1, node2) in edges:
			pheros_delta[node1, node2] += 1/path_len #note not symmetric here. One edge may only be good in one direction!

	if iteration%300 == 0:
		print(iteration)

	pheros = (1-phi)*pheros + pheros_delta

##CONSTRUCT SHORTEST HAMILTON CYCLE BY FOLLOWING EDGES HIGHEST CONCENTRATION OF PHEROMONES
path_len = 0
current_node = 0
visited = {0}
for i in range(n-1):
	weights = np.array([0 if node in visited else pheros[current_node, node] for node in range(n)])
	weights = weights/np.sum(weights)
	node = np.random.choice(n, 1, p = weights)[0]
	path_len += dists[current_node, node]
	visited.add(node)
	current_node = node

path_len += dists[current_node, 0]
print(path_len)

























