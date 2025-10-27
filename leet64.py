from functools import lru_cache
def minPathSum(grid):
        m = len(grid)
        n = len(grid[0])
        @lru_cache(None)
        def dfs(i,j):
            if i>=m or j>=n:
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            return min(dfs(i+1,j), dfs(i,j+1)) + grid[i][j]
        return dfs(0,0)