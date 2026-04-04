class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        h = -prices[0]
        r = 0

        for i in range(1, len(prices)):
            nh = max(h, r - prices[i])
            nr = max(h - fee + prices[i], r)
            h = nh
            r = nr

        return r