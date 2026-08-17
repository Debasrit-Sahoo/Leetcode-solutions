class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        pf = [0] * (n + 1)
        for i, s in enumerate(stoneValue):
            pf[i + 1] = pf[i] + s

        @lru_cache(None)
        def dp(left, right):
            if right - left <= 1:
                return 0
            best = 0
            for k in range(left + 1, right):
                l = pf[k] - pf[left]
                r = pf[right] - pf[k]
                if l <= r:
                    best = max(best, l + dp(left, k))
                if r <= l:
                    best = max(best, r + dp(k, right))
            return best

        return dp(0, n)
