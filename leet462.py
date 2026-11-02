class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) >> 1]
        return sum(abs(x - mid) for x in nums)