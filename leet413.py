class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        t = 0
        r = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                r+=1
                t+=r
            else:
                r = 0
        return t