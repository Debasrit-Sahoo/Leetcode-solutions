class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = 0
        while n >= 5:
            n //= 5
            a += n
        return a