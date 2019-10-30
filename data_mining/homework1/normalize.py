import numpy as np

arr = np.loadtxt("output_distances.txt",delimiter="\t")

cols = []
for i in range(0,6):
	col = arr[:,i]
	minVal = min(col)
	maxVal = max(col)
	col = [ (x-minVal)/(maxVal-minVal) for x in col] ##normalizes the column
	cols.append(col)

cols = np.transpose(cols) 
np.savetxt("normalized_output.txt",cols,"%.2f")

	
