class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        idx = []
        num = [0]
        pf = [0]
        p10 = 1
        
        for i in range(len(s) - 1, -1, -1):
            v = s[i]
            if v != '0':
                v = int(v)
                pf.append(v + pf[-1])
                idx.append(i)
                num.append((v * p10 + num[-1]) % MOD)
                p10 = (p10 * 10) % MOD

        num.reverse(); idx.reverse(); pf.reverse()

        bl = bisect.bisect_left
        br = bisect.bisect_right

        k = len(idx)

        invPow10 = [1] * (k + 1)
        inv10 = pow(10, MOD - 2, MOD)
        for i in range(1, len(invPow10)):
            invPow10[i] = invPow10[i - 1] * inv10 % MOD

        for i, v in enumerate(queries):
            st, e = v
            L = bl(idx, st)
            R = br(idx, e)
            queries[i] = ((((num[L] - num[R]) * invPow10[k - R]) % MOD) * (pf[L] - pf[R])) % MOD

        return queries