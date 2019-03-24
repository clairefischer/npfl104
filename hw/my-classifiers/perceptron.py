import random
import csv


def importcsv(file):
	lines = csv.reader(open(file, "r"))
	data = list(lines)
	return data

def getclass(data): #Return a list with the class possible in the data
    group=[data[0][-1]]
    for line in data:
        if line[-1] not in group:
            group.append(line[-1])
    return group


def format(data):#Transform the data so the class or coded like a binary variable
    if getclass(data)==2:
        class1=getclass(data)[0]
        class2=getclass(data)[1]
        for line in data:
            if line[-1]==class1:
                line[-1]=0
            else:
                line[-1]=1
    return data

def activation(data,weight): #Activation function
    activ=weight[0]
    for i in range(len(data)-1):
        activ=activ+weight[i+1]*data[i]
    if activ>=0:
        return 1
    else:
        return 0

def updateweight(data,l,nb): #Update the weight with the number nb (number of times that we will go through the data)
    weight=[0]*len(data[0])
    n=0
    while n <=nb: #Choose how many times going through the data
        for line in data:
            error=line[-1]-activation(line,weight)
            weight[0]=weight[0]+l*error
            for i in range(len(line)):
                weight[i+1]=weight[i+1]+l*error*line[i]
        n+=1
    return weight

def accuracy(test,predict): #Test how well the classifier is predicting
    right=0
    for i in range(len(test)):
        if test[i][-1]==predict[i]:
            right+=1
    acc=right/float(len(test))*100
    return acc
    
def perceptron(filetrain,filetest,l,nb): #Classifier
    train=format(importcsv(filetrain))
    test=format(importcsv(filetest))
    weight=updateweight(train,l,nb)
    prediction=[]
    for i in test:
        prediction.append(activation(i,weight))
    acc=accuracy(filetest,prediction)
    return prediction,acc



