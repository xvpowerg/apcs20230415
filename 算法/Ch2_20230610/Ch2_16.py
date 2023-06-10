def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end = " ")
        print()    
matrixA = [[0]*2 for row in range(3) ]
#print(matrixA)
for i in range(len(matrixA)):
    for j in range(len(matrixA[i])):
        matrixA[i][j] = 2 * (i+1) + (j+1)
printMatrix(matrixA)
