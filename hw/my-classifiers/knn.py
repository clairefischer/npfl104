
import matplotlib 
import math
import csv
import random


def importcsv(file):
	lines = csv.reader(open(file, "rb"))
	data = list(lines)
	for i in range(len(data)):
		data[i]=[float(x) for x in data[i]]
	return data

def distance(data,predict):
    distance=[]
    for line in data:
        somme=0
        for i in range(len(predict)):
                somme=somme+(line[i]-predict[i])**2
        distance.append((line[-1],math.sqrt(somme)))
    return distance

def getclass(data):
    group=[]
    for line in data:
        group.append(line[-1])
    return set(group)

def knn(data,predict,k):
    dist=distance(data,predict)
    tri_dist=sorted(dist)    
    dist_best=tri_dist[:k]  #Take the k best ones
    occ=[]
    for grp in getclass(data):
            occ.append((grp,dist_best.count(grp)))
    resultat=sorted(occ)[0]
    return resultat 



