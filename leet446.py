class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        r = 0
        dp = [{} for _ in range(l)]
        for i in range(l):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[i].get(d, 0)
                r += cnt
                dp[j][d] = dp[j].get(d, 0) + cnt
        return r