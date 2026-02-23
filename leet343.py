class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(3,n+1):
            m = 0
            for x in range(i):
                m = max(m, x*max(i-x, dp[i-x]))
            dp[i] = m
        return dp[-1]
