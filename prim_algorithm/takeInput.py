import re

def takeInstInput(S):
    edges = []
    input_s = S.split(" ")
    for edge in input_s:
        edge = list(map(int, re.findall(r'\d+', edge)))
        edges.append(edge)
    return edges


def takeFileInput(FileName):
    fileI = open(FileName, 'r')
    inputS = fileI.readline()
    edges = takeInstInput(inputS)
    return inputS, edges

# test
# file_n = "/home/anilosmantur/PycharmProjects/kruskal_adv_algorithms/input1.txt"
# S = "(0,3,5) (0,2,2) (0,1,1) (1,3,2) (2,3,3) (1,2,3)"
# print takeInstInput(S)

