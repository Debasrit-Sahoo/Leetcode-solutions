class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = max(nums)
        return sum(x - a for a in nums)