class Solution:
    def maxProduct(self, nums):
        n = p = m = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if x < 0:
                n, p = p, n
            p = x if p*x < x else p*x
            n = x if n*x > x else n*x
            if m < p:
                m = p
        return m