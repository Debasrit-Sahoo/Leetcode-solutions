def setZeroes(matrix):
        c = set()
        for i in range(len(matrix)):
            seen = False
            for j in range(len(matrix[0])+1):
                if j == len(matrix[0]):
                    if seen:
                        matrix[i] = [0] * len(matrix[0])
                elif matrix[i][j] == 0:
                    for x in range(0, i):
                        matrix[x][j] = 0
                    c.add(j)
                    seen = True
                elif not seen and j in c:
                    matrix[i][j] = 0
        return matrix