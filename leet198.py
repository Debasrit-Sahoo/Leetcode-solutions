from functools import lru_cache
class Solution:
    def rob(self, nums):
        n = len(nums)
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            a = nums[i] + dfs(i+2)
            b = dfs(i+1)
            return max(a,b)
        return dfs(0)