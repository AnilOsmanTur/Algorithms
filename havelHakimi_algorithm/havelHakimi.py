import numpy as np

def getKey(item):
    return item[0]

def havelHakimi(S):

    edges = []
    n = len(S)
    degrees = np.copy(S)

    for k in range(n):
        #step 1: check is it all the elements of the array zero or is there at least one -1?
        count_zero = 0
        for i in range(n):
            if (degrees[i][0] < 0): # there is a -1 so there isn't a graph
                return -1
            elif (degrees[i][0] > n):
                return -1
            elif (degrees[i][0] == 0): # count the zeros
                count_zero += 1


        if (count_zero == n):
            return edges

        #step 2: sort S in non-rising order
        degrees = sorted(degrees, key=getKey, reverse=True)

        #step 3: delete the first element of the array and decrease 1 for first k th element
        #and add edges between to the first element and the decreased elements
        t, edge = degrees.pop(0)
        n -= 1
        if t <= len(degrees):
            for i in range(t):
                degrees[i][0] -= 1
                edges.append((edge, degrees[i][1]))
        else:
            return -1


