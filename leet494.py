class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        tot_sum = sum(nums)
        if tot_sum < target or -tot_sum > target or (tot_sum + target) & 1: return 0
        target += tot_sum
        target //= 2
             
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[-1]