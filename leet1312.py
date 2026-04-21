class Solution:
    def minInsertions(self, s: str) -> int:
        s = s
        if s == s[::-1]: return 0
        n = len(s) + 1

        dp = [0]*n
        
        for i in range(1, n):
            d = 0
            si = s[i-1]
            for j in range(1, n):
                t = dp[j]
                if si == s[-j]:
                    dp[j] = d + 1
                else:
                    if dp[j-1] > dp[j]:
                        dp[j] = dp[j-1]
                d = t
    
        return n - 1 - dp[-1]