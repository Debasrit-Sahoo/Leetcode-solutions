class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m = len(word1)+1
        n = len(word2)+1
        dp = [0]*m

        for w2 in word2:
            diag = dp[0]
            for j in range(1, m):
                dp[j], diag = diag + 1 if word1[j-1] == w2 else max(dp[j], dp[j-1]), dp[j]

        return (m + n - 2 ) - 2 * dp[-1]