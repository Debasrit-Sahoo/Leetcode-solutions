class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        high += 1
        dp = [0]*high
        dp[0] = 1

        lim = 10**9 + 7

        for i in range(high):
            n = dp[i]
            if n > 0:
                if i + zero < high:
                    dp[i+zero] = (dp[i+zero] + n) % lim
                if i + one < high:
                    dp[i+one] = (dp[i+one] + n) % lim

        return sum(dp[low:])%lim