import numpy as np
import scipy.io as sio
import shortest_path_kernel as spk
import argparse
import os

def obtain_pairwise_similarity(l1,l2,num_comparisons):

	avg_sim = 0.0
	for S1 in l1:
		for S2 in l2:
			avg_sim += spk.spkernel(S1,S2)
	return (avg_sim/num_comparisons)		
			

parser = argparse.ArgumentParser()
parser.add_argument("--datadir")
parser.add_argument("--outdir")
args = parser.parse_args()

mat = sio.loadmat("{}/MUTAG.mat".format(args.datadir))
label = np.reshape(mat["lmutag"], (len(mat["lmutag"], ))) 
data = np.reshape(mat["MUTAG"]["am"], (len(label), ))

my_dict={"mutagenic":[], "non-mutagenic":[]}
groups = list(my_dict.keys())
for index, graph in enumerate(data):
	if label[index] == 1:
		my_dict["mutagenic"].append(spk.floyd_warshall(graph))
	else:
		my_dict["non-mutagenic"].append(spk.floyd_warshall(graph))

if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)

file_name = "{}/graphs_output.txt".format(args.outdir)

with open(file_name,"w") as file:

    file.write("Pair of classes\t{}\n".format("SPKernel"))

    for i in range(0,len(groups)):
        for j in range(i,len(groups)):

            group1 = groups[i]
            group2 = groups[j]
            num_comparisons = len(my_dict[group1])*len(my_dict[group2])

            vec_sim = obtain_pairwise_similarity(my_dict[group1],my_dict[group2],num_comparisons)

            str_sim = "{0:.2f}".format(vec_sim)
            file.write("{}:{}\t{}\n".format(group1,group2,str_sim))





