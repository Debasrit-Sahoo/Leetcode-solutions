class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        n = len(cuts)

        dp = [[0] * n for _ in range(n - 1)]

        for size in range(2, n):
            for left in range(n - size):
                right = left + size
                l, r = cuts[left], cuts[right]

                dp[left][right] = r - l + min((dp[left][k] + dp[k][right] for k in range(left + 1, right)), default = 0)

        return dp[0][-1]