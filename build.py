#!/usr/bin/python3

import numpy as np

matrix = np.loadtxt('data/build', dtype=int)
print(matrix)
ostream = open('data/graph.dat', 'w')


def build_with_labels(matrix, f):
    size = matrix.shape[0]
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if matrix[i - 1][j - 1] != -1:
                f.write(f'{i} -> {j} [ label={matrix[i - 1][j - 1]} ];\n')


def build_without_labels(matrix, f):
    size = matrix.shape[0]
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if matrix[i - 1][j - 1]:
                f.write(f'{i} -> {j};\n')

ostream.write('digraph my_graph { \n')
# ostream.write('edge [dir=none];\n')


# build_without_labels(matrix, ostream)
build_with_labels(matrix, ostream)

ostream.write('}\n')



import os
# dot -Tpng data/graph.dat -o data/my_graph.png
# os.system('chmod +x data/my_graph.png && code ./data/my_graph.png && rm data/graph.dat')