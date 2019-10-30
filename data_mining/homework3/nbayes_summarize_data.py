import numpy as np
import argparse
import os

benign_data = [{"total":0},{"total":0},{"total":0},{"total":0}] #clump thickness, uniformity, marginal adhesion,mitoses
malignant_data = [{"total":0},{"total":0},{"total":0},{"total":0}]
tot_benign,tot_malignant = 0,0


parser = argparse.ArgumentParser()
parser.add_argument("--traindir")
parser.add_argument("--outdir")
args = parser.parse_args()

train_data_path = "{}/tumor_info.txt".format(args.traindir)
train_data = np.loadtxt(train_data_path,delimiter="\t",dtype="str")

for row in train_data:
	data = None
	if row[-1] == "2":
		data = benign_data
		tot_benign +=1
	else:
		data = malignant_data
		tot_malignant +=1

	for i in range(0,4):
		num = row[i]
		if num == "":
			continue
		num = int(num)
		if not num in data[i]: 
			(data[i])[num] = 0
		(data[i])[num] += 1
		(data[i])["total"] +=1

output_path2 = "{}/output_summary_class_2.txt".format(args.outdir)
output_path4 = "{}/output_summary_class_4.txt".format(args.outdir)


if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)

with open(output_path2,"w") as file:
	file.write("\t".join(["Value","clump","uniformity","marginal","mitoses"])+"\n")
	for k in range(1,11):
		row = [str(k)]
		for i in range(0,4): 
			frequency = 0 if not k in benign_data[i] else (benign_data[i])[k]
			prob = frequency/(benign_data[i])["total"]
			row.append("{0:.2f}".format(prob))
		file.write("\t".join(row)+"\n")
	file.write("\n" + "P(benignant) = "+str(tot_benign/(tot_benign+tot_malignant)))	

with open(output_path4,"w") as file:
	file.write("\t".join(["Value","clump","uniformity","marginal","mitoses"])+"\n")
	for k in range(1,11):
		row = [str(k)]
		for i in range(0,4): 
			frequency = 0 if not k in malignant_data[i] else (malignant_data[i])[k]
			prob = frequency/(malignant_data[i])["total"]
			row.append("{0:.2f}".format(prob))
		file.write("\t".join(row)+"\n")
	file.write("\n" + "P(malignant) = "+str(tot_malignant/(tot_benign+tot_malignant)))	



