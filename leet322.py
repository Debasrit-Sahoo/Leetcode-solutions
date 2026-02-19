class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = amount + 1
        dp = [float("inf")]*l
        dp[0] = 0
        for i in range(1,l):
            for c in coins:
                if i - c >= 0: dp[i] = min(dp[i-c] + 1, dp[i])
        return -1 if dp[-1] == float("inf") else dp[-1]