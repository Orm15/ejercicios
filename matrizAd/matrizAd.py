def readTXT(nameD):
    with open(nameD, 'r') as document:
        line = document.readlines()

    data = []
    for lines in line:
        fila = list(map(int, lines.strip().split()))
        data.append(fila)

    return data

rows = readTXT("input.txt")

def paint(rows,cont):
    if cont == len(rows) :
        return 
    else :
        print(rows[cont])
        paint(rows,cont + 1)

## paint(rows,0)

def createMat(rows):
    mat = [[]]  
    cont = -1
    nodA = 0
    nodR = 0
    for fil in rows:
        if cont == -1:
            numNod = fil[0]
            mat = [[0] * numNod for _ in range(numNod)]  
        else:
            if cont % 2 == 0:
                nodA = fil[0]
            else:
                for i in fil:
                    nodR = i
                    for j in range(1, numNod + 1):
                        if j == nodR:
                            mat[nodA - 1][j - 1] = 1

                nodA = nodA + 1
        cont = cont + 1
    return mat

print(createMat(rows))