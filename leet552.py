class Solution:
    def checkRecord(self, n: int) -> int:
        a0l0 = a0l1 = a0l2 = a1l0 = a1l1 = a1l2 = 0
        a0l0 = 1
        mod = 10**9 + 7

        for _ in range(n):
            t = (a0l0 + a0l1 + a0l2) % mod
            a0l0, a0l1, a0l2, a1l0, a1l1, a1l2 = t, a0l0 % mod, a0l1 % mod, (a1l0 + a1l1 + a1l2 + t)%mod, a1l0 % mod, a1l1 % mod
        
        return (a0l0 + a0l1 + a0l2 + a1l0 + a1l1 + a1l2) % mod
