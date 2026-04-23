class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        default = (-10**9, 10**9)

        @lru_cache(None)
        def dfs(r, c):
            if not ((0<=r<rows) and (0<=c<cols)): return default
            if (r == rows - 1) and (c == cols - 1):
                return (grid[-1][-1], grid[-1][-1])
            
            v1, v2 = dfs(r+1, c), dfs(r, c+1)
            mx, mn = max(v1[0], v2[0]), min(v1[1], v2[1])

            s = grid[r][c]

            return (s*mx, s*mn) if s >= 0 else (s*mn, s*mx)
        
        r = dfs(0,0)[0]

        return r % (10**9 + 7) if r >= 0 else -1
