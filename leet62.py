from functools import lru_cache
def uniquePaths(m,n):
        end = (m-1,n-1)
        @lru_cache(None)
        def dfs(i,j):
            if i >= m or j >= n:
                return 0
            if (i,j) == end:
                return 1
            return dfs(i+1, j) + dfs(i,j+1)
        return dfs(0,0)