from functools import lru_cache
def uniquePathsWithObstacles(obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obs = set()
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    obs.add((i,j))
        end = (m-1,n-1)
        @lru_cache(None)
        def dfs(i,j):
            if i>=m or j >=n:
                return 0
            if (i,j) in obs:
                return 0
            if (i,j) == end:
                return 1
            return dfs(i+1,j) + dfs(i, j+1)
        return dfs(0,0)