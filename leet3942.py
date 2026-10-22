class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if not all(abs(nums[i - 1] - nums[i]) in (1, n - 1) for i in range(1, n)): return -1

        if nums[0] == 0 and nums[-1] == n - 1: return 0

        z = nums.index(n-1)
        return min(z + 1, n - z + 1)