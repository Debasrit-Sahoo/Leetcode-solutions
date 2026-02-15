class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf"); rest = cool = 0
        for p in prices:
            h = max(hold, rest - p)
            r = max(rest, cool)
            c = hold + p
            hold, rest, cool = h,r,c
        return max(rest, cool)