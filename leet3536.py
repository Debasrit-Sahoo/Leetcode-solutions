class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = -1

        while n:
            d = n%10
            n //= 10

            if d > a:
                b = a
                a = d
            elif d > b:
                b = d

        return a * b