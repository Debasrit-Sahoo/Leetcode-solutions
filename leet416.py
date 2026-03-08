class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        s //= 2
        dp = [0]*(s+1)
        dp[0] = 1
        for n in nums:
            for i in range(s, n-1, -1):
                if dp[i - n]:
                    dp[i] = 1
            if dp[s]: return True
        return False