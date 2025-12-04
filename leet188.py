class Solution:
    def maxProfit(self, k , prices):
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i+1]-prices[i], 0) for i in range(n-1))
        dp = [0]*n
        for _ in range(k):
            buy = -prices[0]
            pro = 0
            for i in range(1, n):
                buy = max(buy, dp[i] - prices[i])
                pro = max(pro, prices[i] + buy)
                dp[i] = pro
        return dp[-1]