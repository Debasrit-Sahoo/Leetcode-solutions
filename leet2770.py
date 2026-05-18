class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = max([1 + dp[j] for j in range(i) if dp[j] and abs(nums[j]-nums[i]) <= target], default=0)
        return dp[-1] - 1