class Solution:
    def integerReplacement(self, n: int) -> int:
        c = 0
        while (n != 1):
            if n&1:
                if n == 3:
                    n -= 1
                elif n % 4 == 3:
                    n += 1
                else:
                    n -= 1
            else:
                n = n>>1
            c += 1
        return c