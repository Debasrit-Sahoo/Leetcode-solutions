class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        out = []
        if (numerator < 0) ^ (denominator < 0):
            out.append("-")
        if numerator < 0:
            numerator *= -1
        if denominator < 0:
            denominator *= -1
        out.append(str(numerator//denominator))
        r = numerator % denominator
        if r == 0:
            return "".join(out)
        out.append(".")
        h = {}
        while r != 0:
            if r in h:
                out.insert(h[r], "(")
                out.append(")")
                break
            h[r] = len(out)
            r *= 10
            out.append(str(r//denominator))
            r %= denominator
        return "".join(out)