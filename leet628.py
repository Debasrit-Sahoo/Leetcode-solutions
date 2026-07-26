class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        mx1 = mx2 = mx3 = -(1 << 31)
        mn1 = mn2 = 1 << 31

        for x in nums:
            if x > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = x
            elif x > mx2:
                mx3 = mx2
                mx2 = x
            elif x > mx3:
                mx3 = x

            if x < mn1:
                mn2 = mn1
                mn1 = x
            elif x < mn2:
                mn2 = x

        a = mx1 * mx2 * mx3
        b = mx1 * mn1 * mn2

        return a if a > b else b