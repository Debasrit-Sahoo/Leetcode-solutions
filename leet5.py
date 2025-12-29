class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s)) == 1: return s
        l = len(s)
        start, length = 0, 1
        dp = [[False]*(l+1) for _ in range(l)]
        for i in range(l):
            dp[i][i+1] = True
        for i in range(l-1):
            if s[i] == s[i+1]:
                start = i; length = 2 
                dp[i][i+2] = True
        for i in range(3, l+1):
            for j in range(l-i+1):
                if s[j] == s[j+i-1] and dp[j+1][j+i-1]:
                    start = j; length = i 
                    dp[j][j+i] = True
        return s[start:start+length]