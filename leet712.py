class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        s = 0
        for i in range(1, l2+1):
            s += ord(s2[i-1])
            dp[0][i] = s
        s = 0 
        for i in range(1, l1+1):
            s += ord(s1[i-1])
            dp[i][0] = s

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = dp[i-1][j-1] if s1[i-1] == s2[j-1] else min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        return dp[-1][-1]