class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            o = s.count('1')
            z = s.count('0')

            for i in range(m, z-1, -1):
                for j in range(n, o-1 ,-1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-z][j-o])

        return dp[-1][-1]