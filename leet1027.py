class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        o = len(nums)
        dp = [{} for _ in range(o)]
        m = 0
        for i in range(o):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = n = dp[j].get(d, 1) + 1
                if m < n: m = n
        return m 