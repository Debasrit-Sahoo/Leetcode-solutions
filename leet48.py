def rotate(matrix):
    l = len(matrix)
    for i in range(l):
        for j in range(1 + i, l):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for r in matrix:
        r.reverse()