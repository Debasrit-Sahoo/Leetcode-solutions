def minimumTotal(triangle):
        dp = triangle[-1]
        for r in range(len(triangle)-2,-1,-1):
            for c,v in enumerate(triangle[r]):
                a, b = dp[c], dp[c+1]
                a = a if a < b else b
                dp[c] = v + a
        return dp[0]