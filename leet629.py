class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        m = 10**9+7

        dp = [0]*(k+1);dp[0]=1

        for i in range(1, n+1):
            new = [0]*(k+1)
            w = 0
            for j in range(0, k+1):
                w += dp[j]
                if j >= i:
                    w -= dp[j-i]
                
                new[j] = w % m

            dp = new

        return dp[-1]