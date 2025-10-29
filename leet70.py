from functools import lru_cache
def climbStairs(n):
        @lru_cache(None)
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return dfs(i+1) + dfs(i+2)
        return dfs(0)