def generateMatrix(n):
        grid = [[0] * n for _ in range(n)]
        for x in range(1,n+1):
            grid[0][x-1] = x
        x = n + 1
        l = n
        n -= 1
        i, j = 0, n
        while x < l**2:
            for _ in range(n):
                i += 1
                grid[i][j] = x
                x += 1
            for _ in range(n):
                j -= 1
                grid[i][j] = x
                x += 1
            if n == 0:
                return grid
            n -= 1
            for _ in range(n):
                i -= 1
                grid[i][j] = x
                x += 1
            for _ in range(n):
                j += 1
                grid[i][j] = x
                x += 1
            n -= 1
        return grid