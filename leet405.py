class Solution:
    def toHex(self, num: int) -> str:
        if not num: return '0'
        num &= 0xFFFFFFFF
        res = []
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        while num > 0:
            res.append(digits[num%16])
            num //= 16

        return "".join(reversed(res))