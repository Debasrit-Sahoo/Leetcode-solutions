class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
            MOD = 1000000007
            r += 1

            size = r - l

            dsc_pf = [0] * (size)
            for i in range(1, size):
                dsc_pf[i] = dsc_pf[i-1] + size - i
            dsc_pf.reverse()
            dsc_pf.pop()
            for _ in range(2, n):
                for i in range(1, size-1):
                    dsc_pf[i] = (dsc_pf[i-1] + dsc_pf[i]) % MOD
                dsc_pf.reverse()
            return (dsc_pf[0] << 1) % MOD