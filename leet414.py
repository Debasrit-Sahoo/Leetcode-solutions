class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        a = b = c = s = -(1 << 31) - 1

        for each in nums:
            if each > a:
                c = b
                b = a
                a = each
            elif a != each and each > b:
                c = b
                b = each
            elif a != each and b != each and each > c:
                c = each

        return a if c == s else c