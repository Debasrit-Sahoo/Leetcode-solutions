class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i] ** 2 for i in range(len(nums)) if not len(nums) % (i + 1))