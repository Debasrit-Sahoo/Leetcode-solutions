class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (k * ((max(nums) << 1) + k - 1)) // 2