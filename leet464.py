class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        m = maxChoosableInteger
        if desiredTotal <= m: return True
        if m * (m + 1) // 2 < desiredTotal: return False
        bits = [1 << i for i in range(m + 1)]

        @lru_cache(None)
        def dfs(numset, remsum):
            for n in range(m):
                if (numset & bits[n]): continue
                v = n + 1
                if remsum <= v or not dfs(numset | bits[n], remsum - v): return True
            return False

        return dfs(0, desiredTotal)