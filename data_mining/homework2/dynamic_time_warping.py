import numpy as np

def constrained_dtw(t1,t2,w): 

	DTW = np.zeros(shape=(len(t2),len(t1)),dtype=float) 
	distances = np.zeros(shape=(len(t2),len(t1)),dtype=float)

	for i in range(len(t1)):
		for j in range(len(t2)):
			distances[j,i] = abs(t1[i]-t2[j])
			if(abs(j-i) > w):
				DTW[j,i] = float("inf")

	DTW[0,0] = distances[0,0]
	for i in range(1,min(len(t1),1+w)):
		DTW[0,i] = DTW[0,i-1]+distances[0,i]
	for j in range(1,min(len(t2),1+w)):
		DTW[j,0] = DTW[j-1,0]+distances[j,0]

	for i in range(1,len(t1)):
		for j in range(1,len(t2)):
			if(abs(i-j) <= w): ##maybe can do this better so that for each i choose j so that only loop through the important cells
				DTW[j,i] = distances[j,i]+min(DTW[j-1,i],DTW[j-1,i-1],DTW[j,i-1])
	return DTW[-1,-1]

def manhattan(t1,t2):
	return float(sum(abs(t1-t2)))











