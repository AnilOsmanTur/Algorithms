def takeInstInput(S):
    degrees = []
    inputS = S.split(" ")
    inputS = [int(x) for x in inputS]
    for i in range(len(inputS)):
        degrees.append((inputS[i], i))
    return degrees

def takeFileInput(FileName):
    fileI = open(FileName, 'r')
    inputS = fileI.readline()
    degrees = takeInstInput(inputS)
    fileI.close()
    return inputS, degrees