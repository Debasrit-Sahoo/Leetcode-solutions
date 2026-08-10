class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        sqs = [i ** 2 for i in range(1, math.isqrt(n) + 1)]

        dp = [False] * (n + 1)
        dp[1] = True

        for i in range(2, n+1):
            dp[i] = any(not dp[i - sqs[j]] for j in range(bisect_left(sqs, i + 1)))

        return dp[n]