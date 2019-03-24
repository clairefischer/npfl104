import csv
import random
import math


def importcsv(file):
	lines = csv.reader(open(file, "r"))
	data = list(lines)
	return data

def class_sep(data):
	sep={}
	for i in range(len(data)):
		item=data[i]
		if (item[-1] not in sep): #-1 because it is the group label
			sep[item[-1]]=[]
		sep[item[-1]].append(item)
	return sep

def mean(x):
	return sum(x)/len(x)
 
def dev(x):
    somme=0
    for i in x:
        somme=somme+(i-mean(x))**2
    return math.sqrt(somme/float(len(x)-1))

def info(data):
    j=0
    list_att=[]
    while j<len(data[0])-1:
        attribute=[]
        for i in range(len(data)):
            attribute.append(data[i][j])
        list_att.append(attribute)
        j+=1
    infos_=[(att,mean(att),dev(att)) for att in list_att]
    sep=class_sep(data)
    infos={}
    for class_,item in sep.items():
        for i in range(len(infos_)):
            if item==i[0]:
                infos[class_] = [i[1],i[2]]
    return infos


def prediction(infos, predi):
    predict=[]
    for i in range(len(predi)):
        proba={}
        for class_, classinfo in infos.items():
            proba[class_]=1
            for i in range(len(classinfo)):
                mean,dev=classinfo[i]
                proba[class_]=proba[class_]*(1/(math.sqrt(2*math.pi)*dev))*(math.exp(-((predi[i]-mean)**2/(2*dev**2))))
        bestclass=None
        bestproba=-100
        for class_,proba in proba.items():
            if bestclass is None or proba>bestproba:
                bestproba=proba
                bestclass=class_
        predict.append(bestclass)
    return predict

def accuracy(test,predict):
    right=0
    for i in range(len(test)):
        if test[i][-1]==predict[i]:
            right+=1
    acc=right/float(len(test))*100
    return acc

def nb(filetrain,filetest):
    traindata=importcsv(filetrain)
    predictdata=importcsv(filetest)
    predi= prediction(info(traindata),predictdata)
    acc=accuracy(predictdata,predi)
    return predi,acc
 
