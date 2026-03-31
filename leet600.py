class Solution:
    def findIntegers(self, n: int) -> int:
        k = n.bit_length()
        f = [0]*(k+2)
        f[0] = 1; f[1] = 2
        for i in range(2, k+1): f[i] = f[i-1] + f[i-2]

        prev = 0
        ret = 0

        for i in range(k-1, -1, -1):
            if n & (1 << i):
                ret += f[i]
                if prev: return ret
                prev = 1
            else:
                prev = 0

        return ret + 1