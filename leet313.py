class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]*n
        n1 =len(primes)
        ptrs = [0]*n1
        for i in range(1, n):
            s = min(dp[ptrs[c]]*primes[c] for c in range(n1))
            dp[i] = s
            for c in range(n1):
                if dp[ptrs[c]]*primes[c] == s:
                    ptrs[c] += 1
        return dp[-1]