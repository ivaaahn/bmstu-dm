#!/usr/bin/python3

import numpy as np
from math import inf


GREEN = "\x1b[32m"
RESET = "\x1b[0m"


matrix = np.loadtxt('data/bfs', dtype=int)
start = int(input(f'Enter index of start vertex, please [0, {len(matrix[0]) - 1}]: '))

def bfs_def(matrix, start):
    V = [v for v in range(len(matrix[0]))]  # All nodes
    M = [None for m in range(len(V))]  # Matrix of distances
    Q = []  # Queue

    M[start] = 0
    Q.append(start)

    while len(Q):
        print(f'Queue is {Q}')
        v_curr = Q.pop(0)
        for w in [i for i in range(len(matrix[v_curr])) if matrix[v_curr][i] > 0]:
            if M[w] is None:
                Q.append(w)
                M[w] = M[v_curr] + 1

    print(f'Result: {M}')


def bfs_weights(matrix, start):
    V = [v for v in range(len(matrix[0]))]   # All nodes
    M = [inf for v in range(len(V))]      # Matrix of distances
    Q = []                                   # Queue
    M[start] = 0
    Q.append(start)


    while len(Q):
        print(f'\tQueue: {Q}\t\t|\t\tResult: {M}')
        v_curr = Q.pop(0)
        for w in (i for i in range(len(matrix[v_curr])) if matrix[v_curr][i] > 0):
            delta = min(M[w], M[v_curr] + matrix[v_curr][w])
            if delta < M[w]:
                M[w] = delta
                if w not in Q:
                    Q.append(w) 

    print(f'\tQueue: {Q}\t\t|\t\tResult: {M}')
    

    print(GREEN)     
    print(f'Result: {M}')
    print(RESET)





bfs_weights(matrix, start)
# bfs_def(matrix, start)