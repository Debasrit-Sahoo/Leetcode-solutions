class Solution:
    def maximumGap(self, nums):
        if len(nums) <= 1:
            return 0
        nums.sort()
        i = 0
        l = float("-inf")
        p = nums[0]
        for i in range(1, len(nums)):
            c = nums[i]-p
            if l < c:
                l = c
            p = nums[i]
            i += 1
        return l