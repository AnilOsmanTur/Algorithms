# definition of graph class
import numpy as np

class Graph:
    # vertex_n needed integer edges_w is list of (1, 2, 3) tree element first 2 is vertexes
    # and last one is weight
    def __init__(self, edges_w=None, directed=False):
        self.directed = directed
        self.vertex_n = 0

        if edges_w == None:
            self.edges = []
        else:
            self.edges = np.copy(edges_w)
            self.findVertex_n(edges_w)

        self.vertex_sets = np.zeros(self.vertex_n, dtype=int)
        if edges_w == None:
            self.vertexes = []
        else:
            self.vertexes = np.arange(self.vertex_n)
        # adjacent matrix
        if edges_w == None:
            self.adjMat = []
        else:
            self.adjMat = np.zeros((self.vertex_n, self.vertex_n), dtype=int)
            self.connect(edges_w)

    def findVertex_n(self,edges_w):
        n = 0
        vertex = []
        for edge in edges_w:
            if not edge[0] in vertex:
                vertex.append(edge[0])
                n += 1
            if not edge[1] in vertex:
                vertex.append(edge[1])
                n += 1

        self.vertex_n = n


    def connect(self, edges_w):
        for edge in edges_w:
            self.adjMat[edge[0],edge[1]] = edge[2]
            if not self.directed:
                self.adjMat[edge[1], edge[0]] = edge[2]

    def isConnected(self, node1, node2):
        if self.adjMat[node1,node2] != 0:
            return True
        else:
            return False

    def getEdges(self):
        return self.edges

    def getMat(self):
        return self.adjMat

    def make_set(self, v):
        self.vertex_sets[v] = v

    def union(self, v1, v2):
        ch = self.vertex_sets[v2]
        swap = self.vertex_sets[v1]
        for i in range(self.vertex_n):
            if self.vertex_sets[i] == ch:
                self.vertex_sets[i] = swap


    def find_set(self, v):
        return self.vertex_sets[v]

# tests
#edgesW = [(0,1,1),(1,2,3),(0,2,2),(3,1,3)]
#graph = Graph(edgesW)
#print graph.getMat()
#print graph.edges
