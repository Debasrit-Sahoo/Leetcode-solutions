class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        prev = [-1] * 26
        off = ord('a')

        for c in s:
            ndp = dp << 1
            idx = ord(c) - off
            if prev[idx] >= 0:
                ndp -= prev[idx]
            else:
                ndp += 1
            prev[idx] = dp
            dp = ndp % MOD

        return dp