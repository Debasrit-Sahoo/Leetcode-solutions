class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pf = [0] * (n + 1)
        for i in range(1, n + 1):
            pf[i] = pf[i-1] + piles[i-1]

        @lru_cache(None)
        def dp(i, m):
            if m << 1 >= n - i: return pf[n] - pf[i]
            return max(pf[i+j] - pf[i] - dp(i+j, m if m > j else j) for j in range(1, (m<<1 if m << 1 < n - i else n - i) + 1))

        return (pf[n] + dp(0, 1)) >> 1