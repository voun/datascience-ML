import numpy as np
import argparse
import os

##define helper functions
def euclidean_distance(v1,v2):
    return float((sum((v1-v2)**2)**0.5))

def find_majority(v):
    sum = 0
    for (vector,label) in v:
        sum = (sum+1) if label == "+" else (sum-1)
    if sum == 0:
        return "tie"
    else:
        return "+" if sum > 0 else "-"

def evaluation(true_labels,predicted_labels):
    TP,FP,TN,FN = 0,0,0,0
    for name in predicted_labels:
        if predicted_labels[name] == "+":
            if true_labels[name] == "+":
                TP +=1
            else:
                FP +=1
        else:
            if true_labels[name] == "+":
                FN +=1
            else:
                TN +=1

    accuracy = 0 if (TP+TN == 0) else (TP+TN)/(TP+FP+TN+FN) 
    precision = 0 if TP == 0 else TP/(TP+FP)
    recall = 0 if TP == 0 else TP/(TP+FN)
    return (accuracy,precision,recall)

#main program
parser = argparse.ArgumentParser()
parser.add_argument("--traindir")
parser.add_argument("--testdir")
parser.add_argument("--outdir")
parser.add_argument("--mink",type=int)
parser.add_argument("--maxk",type=int)
args = parser.parse_args()


train_data_path = "{}/matrix_mirna_input.txt".format(args.traindir)
train_labels_path ="{}/phenotype.txt".format(args.traindir)

train_labels = np.loadtxt(train_labels_path,delimiter="\t",dtype="str")
train_data = np.loadtxt(train_data_path,delimiter="\t",dtype="str")
train_labels_and_data = []
for i in range(1,len(train_labels)): #Assume id same order in both files 
    label = train_labels[i,1]
    data = np.array([float(x) for x in train_data[i,1:]])
    train_labels_and_data.append((data,label))
    
test_data_path="{}/matrix_mirna_input.txt".format(args.testdir)
test_labels_path="{}/phenotype.txt".format(args.testdir)

test_data = np.loadtxt(test_data_path,delimiter="\t",dtype="str")
test_labels = np.loadtxt(test_labels_path,delimiter="\t",dtype="str")

true_labels={}
distances = {}
for i in range(1,len(test_data)):
    name = test_data[i,0]
    data = np.array([float(x) for x in test_data[i,1:]])
    true_labels[name] = test_labels[i,1]

    distance = []
    for (vector,label) in train_labels_and_data:
        distance.append((euclidean_distance(data,vector),label))
    distance.sort()
    distances[name] = distance

if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)

output_path = "{}/output_knn.txt".format(args.outdir)
with open(output_path,"w") as file:
    file.write("\t".join(["Value of k","Accuracy","Precision","Recall"])+"\n")
    for k in range(args.mink,args.maxk+1):
        predicted_labels = {}
        for name in distances:
            label = find_majority((distances[name])[0:k])
            if label == "tie":
                label = find_majority((distances[name])[0:k-1]) #now can't have ties
            predicted_labels[name] = label

        result = ["{0:.2f}".format(num) for num in evaluation(true_labels,predicted_labels)]
        result.insert(0,str(k)) 
        file.write("\t".join(result)+"\n")
