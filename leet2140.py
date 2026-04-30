class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            p, idx = questions[i]
            dp[i] = max(dp[i+1], p + (dp[i+idx+1] if i+idx+1 < n else 0))

        return dp[0]
