

download:
	python download.py
	python knn.py
	python perceptron.py
	python nb.py
default : download
all : download
download : download
nb : NB
perceptron : perceptron
knn : 
	knn
clean : 
	rm *.pyo download 
string_times : download.pyo
	python download.pyo  -pyo $@ 
%.pyo : %.py 
	python $<