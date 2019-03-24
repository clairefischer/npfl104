

default : download nb perceptron knn

all : download nb perceptron knn 

download : download
	python download.py
NB : NB
	python NB.py
perceptron : perceptron
	python perceptron.py
knn : knn
	python knn.py
clean : 
	rm *.pyo download 
string_times : download.pyo
	python download.pyo  -pyo $@ 
%.pyo : %.py 
	python $<