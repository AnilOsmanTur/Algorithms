# Anil Osman TUR
# 12290551
#
# Kruskal algorithm for Minimum spanning tree
# step 1: sort the edges in ascending order
# step 2: if the edge won't create a cycle add edge to the spanning tree
# step 3: do the step 3 for all edges in the order


# to understand the cycle find set and make set functions will used
from graphClass import Graph

import numpy as np

def getKey(item):
    return item[2]

def mst_kruskal( graph ):
    A = [] # selected edges

    for v in graph.vertexes:
        graph.make_set(v)

    # sort edges in non-rising order
    sorted_edges = sorted(graph.edges, key=getKey)

    for edge in sorted_edges:
        if graph.find_set(edge[0]) != graph.find_set(edge[1]):
            A.append(edge)
            graph.union(edge[0], edge[1])
    return A


# test  #

#dgesW = [[0,1,3], [0,3,6], [0,4,9], [1,5,5], [2,5,4], [2,3,2] ,[3,5,3], [3,4,1], [4,5,7]]
#graph = Graph(edgesW)
#print "Graph :"
#print graph.getMat()
#print graph.edges
#tree = np.array(mst_kruskal(graph))
#print "tree :"
#print tree
#print graph.vertex_sets

#print "changes :"
#e_n = len(edgesW)
#t_n = len(tree)
#changes = []
#for i in range(e_n):
#    for j in range(t_n):
#        if np.array_equal(edgesW[i], tree[j]):
#           changes.append(i)
#print changes

#print "tree :"
#graphT = Graph(tree)
#print graphT.getMat()
#print graphT.edges