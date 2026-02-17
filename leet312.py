class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums; nums.append(1); n=len(nums)
        dp = [[0]*n for _ in range(n)]
        for s in range(2,n):
            for i in range(n-s):
                j = s + i
                dp[i][j] = max(dp[i][k] +  dp[k][j] + (nums[i]*nums[k]*nums[j]) for k in range(i+1,j))
        return dp[0][-1]