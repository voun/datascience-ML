import numpy as np
from collections import Counter


def floyd_warshall(A):
	D = np.zeros(A.shape)
	for i in range(D.shape[0]):
		for j in range(D.shape[0]):
			if i != j:
				if A[i,j] == 0:
					D[i,j] = float("inf")
				else:
					D[i,j] = A[i,j]

	for k in range(D.shape[0]):
		for i in range(D.shape[0]):
			for j in range(D.shape[0]):
				if D[i,k]+D[k,j] < D[i,j]:
					D[i,j] = D[i,k]+D[k,j]

	return D

def to_single_list(A):
	list = []
	for index,row in enumerate(A):
		for num in row[index+1:]:
			list.append(num)
	return list


def spkernel(S1,S2):
	
	c1 = Counter(to_single_list(S1))
	c2 = Counter(to_single_list(S2))

	sum = 0
	for key in c1:
		sum += c1[key]*c2[key]
	return float(sum)








