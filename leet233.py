class Solution:
    def countDigitOne(self, n: int) -> int:
        co = 0
        p = 1
        while n >= p:
            l = n // (10*p)
            c = (n // p)%10
            r = n % p
            if c == 0:
                co += l*p
            elif c == 1:
                co += l*p + r + 1
            else:
                co += (l+1)*p
            p *= 10
        return co