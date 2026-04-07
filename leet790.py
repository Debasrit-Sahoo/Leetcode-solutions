class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        mod = 10**9 + 7

        p0 = 2; p1 = 1; p2 = 1

        for i in range(n-2):
            p0, p1, p2 = (p0*2 + p2)%mod, p0, p1

        return p0%mod 