class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(r,c,k):
            if not (0 <= r < m and 0 <= c < n): return 1
            if not k: return 0
            k-=1
            return (dfs(r+1, c, k) + dfs(r-1, c, k) + dfs(r, c+1, k) + dfs(r, c-1, k)) % MOD 

        return dfs(startRow, startColumn, maxMove) % MOD