from __future__ import division, print_function
import numpy as np
import dynamic_time_warping as dtw
import argparse
import os
import math


DISTANCES = {"Manhattan": dtw.manhattan,
			"DTW, w = 0": lambda t1,t2 : dtw.constrained_dtw(t1,t2,0),
            "DTW, w = 10": lambda t1,t2 : dtw.constrained_dtw(t1,t2,10),
            "DTW, w = 25": lambda t1,t2 : dtw.constrained_dtw(t1,t2,25),
            "DTW, w = inf": lambda t1,t2 : dtw.constrained_dtw(t1,t2,float("inf"))}


def obtain_pairwise_distances(lst_vec1, lst_vec2, num_comparisons):

    avg_dist = np.zeros(len(DISTANCES),dtype=float)
    for index, metric in enumerate(DISTANCES):
        for i in range(len(lst_vec1)):
            for j in range(len(lst_vec2)):
            	v1 = lst_vec1[i]
            	v2 = lst_vec2[j]
            	avg_dist[index] += DISTANCES[metric](v1,v2)

    avg_dist = avg_dist/num_comparisons
    return avg_dist


parser = argparse.ArgumentParser()
parser.add_argument("--datadir")
parser.add_argument("--outdir")
args = parser.parse_args()

file_name = "{}/ECG200_TRAIN.txt".format(args.datadir)
my_dict = {"abnormal":[],"normal":[]}
groups = list(my_dict.keys())
data = np.loadtxt(file_name,delimiter=",")

for row in data:
    if row[0] == -1:
        my_dict["abnormal"].append(row[1:])
    else:
        my_dict["normal"].append(row[1:])

if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)

file_name = "{}/timeseries_output.txt".format(args.outdir)

with open(file_name,"w") as file:

    file.write("Pair of classes\t{}\n".format("\t".join(list(DISTANCES.keys()))))

    for i in range(0,len(groups)):
        for j in range(i,len(groups)):

            group1 = groups[i]
            group2 = groups[j]
            num_comparisons = len(my_dict[group1])*len(my_dict[group2])


            if group1 == group2:
                num_comparisons -= len(my_dict[group1])

            vec_dist = obtain_pairwise_distances(my_dict[group1],my_dict[group2],num_comparisons)
            str_dist = "\t".join(["{0:.2f}".format(x) for x in vec_dist])

            file.write("{}:{}\t{}\n".format(group1,group2,str_dist))








