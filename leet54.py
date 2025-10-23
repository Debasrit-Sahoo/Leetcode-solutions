def spiralOrder(matrix):
        final = []
        for x in matrix[0]:
            final.append(x)
        c, r = len(matrix) - 1, len(matrix[0]) - 1
        if c == 0:
            return final
        if r == 0:
            x = []
            for i in matrix:
                x.append(i[0])
            return x
        t = len(matrix) * len(matrix[0])
        i, j = 0, r
        while len(final) < t:
            for _ in range(c):
                i += 1
                final.append(matrix[i][j])
            c -= 1
            for _ in range(r):
                j -= 1
                final.append(matrix[i][j])
            r -= 1
            if len(final) >= t:
                break
            for _ in range(c):
                i -= 1
                final.append(matrix[i][j])
            c -= 1
            for _ in range(r):
                j += 1
                final.append(matrix[i][j])
            r -= 1
        return final
