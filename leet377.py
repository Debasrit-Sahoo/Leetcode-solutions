class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        target+=1
        dp = [0]*target
        dp[0] = 1
        for i in range(1, target):
            for j in nums:
                if j > i: break
                dp[i] += dp[i-j]
        return dp[-1]