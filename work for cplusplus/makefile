.PHONY: clean directories

all: directories bin/c299

bin/gene_cluster: c299.cpp
	g++ -std=c++11 gene_cluster.cpp -o bin/c299

directories:
	mkdir -p bin

clean:
	rm -rf bin
