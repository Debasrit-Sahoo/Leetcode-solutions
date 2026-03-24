class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [-1]*(1<<n)
        end = (1<<n) - 1

        def backtrack(s):
            if s == end: return 1
            if dp[s] != -1: return dp[s]
            idx = s.bit_count() + 1
            tot = 0
            for i in range(1, n+1):
                if (s & (1 << (i-1))) or ((idx % i) and (i % idx)): continue
                ns = s | (1 << (i-1))
                tot+= backtrack(ns)
            dp[s] = tot
            return tot
        return backtrack(0)
