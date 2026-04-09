class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0]*n
        nc7 = nc30 = -1
        d,w,m = costs[0], costs[1], costs[2]

        for i in range(n):
            day = days[i]

            while (nc7 < i) and (day - days[nc7 + 1] > 6): nc7 += 1
            while (nc30 < i) and (day - days[nc30 + 1] > 29): nc30 += 1

            dp[i] = min(dp[i-1] + d, dp[nc7] + w, dp[nc30] + m)
        return dp[-1]