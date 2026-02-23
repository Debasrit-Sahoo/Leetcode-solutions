class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4: return n-1
        p = n // 3
        r = n % 3
        if r == 1:
            return pow(3, p-1)*4
        p = pow(3, p)
        if r == 2:
            return p*2
        return p