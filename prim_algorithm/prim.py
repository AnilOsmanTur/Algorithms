# Anil Osmna TUR
# 12290551
# Advance Algorithms:
# Prim algorithm for minimum spanning tree
# - it will take a graph object and a starting node

from graphClass import Graph
from minheap import Heap
import numpy as np


def mst_prim(graph, r):

    # initialization of key and parent matrix
    keys = np.empty(graph.vertex_n, dtype=int)
    keys.fill(999999)
    parents = np.empty(graph.vertex_n, dtype=int)
    parents.fill(-1)

    keys[r] = 0

    Q = Heap()
    Q.buildMinHeap(graph.vertexes, keys)

    while len(Q._heap) != 0:
        u = Q.pop()
        adjs = graph.adjs(u)
        for v in adjs:
            if Q.isInHeap(v) and graph.weight_between(u, v) < keys[v]:
                parents[v] = u
                keys[v] = graph.weight_between(u, v)
                Q.changeKey(v, keys[v])
    print( "keys:    ",keys)
    print( "parents: ",parents)

    return parents, keys



def mst_to_edges(parents, keys):
    edges = []

    for i in range(len(parents)):
        if parents[i] != -1:
            edges.append([parents[i], i, keys[i]])
    print( "found edges: ", edges)
    return edges

"""
dgesW = [[0,1,3], [0,3,6], [0,4,9], [1,5,5], [2,5,4], [2,3,2] ,[3,5,3], [3,4,1], [4,5,7]]
graphT = Graph(dgesW)
prim, keys = mst_prim(graphT, 0)
edges = mst_to_edges(prim, keys)
print prim
"""
