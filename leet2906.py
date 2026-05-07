class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        m = 12345
        mat = [[0]*c for _ in range(r)]
        p = 1
        for i in range(r):
            for j in range(c):
                mat[i][j] = p
                p = (p*grid[i][j]) % m
        
        p = 1
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                mat[i][j] = (mat[i][j] * p) % m
                p = (p * grid[i][j]) % m
        
        return mat