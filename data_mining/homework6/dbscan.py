
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--eps",type=float)
parser.add_argument("--min_pts",type=int)
args = parser.parse_args()

class Node:

	def __init__(self,id,label,visited=False):
		self.id = id
		self.label = label #core,border,noise or unclassified
		self.visited=visited

	def get_visited(self):
		return self.visited
	def set_visited(self,visited):
		self.visited = visited
	def get_id(self):
		return self.id
	def get_label(self):
		return self.label
	def set_label(self,label):
		self.label = label

matrix = np.ones((18,18))*np.inf
matrix[0,1]=0.3
matrix[1,2]=0.2
matrix[1,0]=0.3
matrix[1,3]=0.2
matrix[1,4]=0.9
matrix[2,1]=0.2
matrix[2,3]=0.2
matrix[2,5]=0.5
matrix[3,1]=0.2
matrix[3,2]=0.2
matrix[3,6]=0.4
matrix[3,7]=0.4
matrix[4,1]=0.9
matrix[4,7]=0.4
matrix[4,8]=0.1
matrix[4,10]=0.3
matrix[4,9]=0.2
matrix[5,2]=0.5
matrix[5,6]=0.2
matrix[5,11]=0.4
matrix[6,3]=0.4
matrix[6,5]=0.2
matrix[6,11]=0.5
matrix[7,3]=0.4
matrix[7,12]=0.8
matrix[7,4]=0.4
matrix[8,4]=0.1
matrix[8,9]=0.2
matrix[9,8]=0.2
matrix[9,10]=0.2
matrix[9,4]=0.2
matrix[10,4]=0.3
matrix[10,9]=0.2
matrix[10,12]=0.5
matrix[11,6]=0.5
matrix[11,5]=0.4
matrix[11,15]=0.2
matrix[11,14]=0.2
matrix[12,7]=0.8
matrix[12,14]=0.2
matrix[12,16]=0.4
matrix[12,10]=0.5
matrix[13,9]=0.8
matrix[13,16]=0.4
matrix[14,11]=0.2
matrix[14,12]=0.2
matrix[14,15]=0.1
matrix[14,16]=0.3
matrix[14,17]=0.2
matrix[15,11]=0.2
matrix[15,14]=0.1
matrix[15,17]=0.2
matrix[16,12]=0.4
matrix[16,14]=0.3
matrix[16,17]=0.4
matrix[16,13]=0.3
matrix[17,15]=0.2
matrix[17,14]=0.2
matrix[17,16]=0.4

nodes = []
for i in range(0,18):
	node = Node(i,"unclassified")
	nodes.append(node)

def DBscan(eps,min_pts):
	clusterID = 1
	clusters = {}
	for node in nodes:
		if node.get_visited():
			continue
		cluster = []
		expandCluster(node,cluster,True,eps,min_pts)
		
		if node.get_label() != "noise":
			clusters[clusterID] = cluster
			clusterID +=1	
	return clusters

def expandCluster(node,cluster,first,eps,min_pts):

	node.set_visited(True)
	cluster.append(node)
	if not isCorePoint(node,eps,min_pts):
		if first:
			node.set_label("noise")
		else:
			node.set_label("border")
		return

	node.set_label("core")
	for i in range(0,18):

		if matrix[node.get_id(),i] <= eps:
			if nodes[i].get_label() == "noise":
				nodes[i].set_label("border")
				cluster.append(nodes[i])
			elif nodes[i].get_label() == "unclassified":
				expandCluster(nodes[i],cluster,False,eps,min_pts)

def isCorePoint(node,eps,min_pts):

	eps_neigh = 1
	for i in range(0,18):
		if matrix[node.get_id(),i] <= eps:
			eps_neigh +=1
	return True if eps_neigh >= min_pts else False
	
clusters = DBscan(args.eps,args.min_pts)
core_points=""
border_points=""
noise_points=""

for node in nodes:
	label = node.get_label()
	id = str(node.get_id()+1) + ", "
	if label == "noise":
		noise_points += id
	elif label == "border":
		border_points += id
	else:
		core_points += id

core_points = core_points[0:-2]
border_points = border_points[0:-2]
noise_points = noise_points[0:-2]
print("Core points: "+ core_points)
print("Border points : "+ border_points)
print("Noise points :"+ noise_points)

for cluster in clusters:
	s = "Cluster"+str(cluster)+":{"
	for node in clusters[cluster]:
		s+= str(node.get_id()+1) + ", "
	s = s[0:-2] + "}"
	print(s)



