class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        return min(nums[n] - nums[2], nums[n - 1] - nums[1], nums[n - 2] - nums[0])