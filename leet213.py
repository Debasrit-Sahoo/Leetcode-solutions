class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(i):
            if not i < n:
                return 0
            a = nums[i] + dfs(i+2)
            b = dfs(i+1)
            return max(a,b)
        a = dfs(1)
        if n == 1:
            return a
        nums.pop()
        n -= 1
        dfs.cache_clear()
        b = nums[0] + dfs(2)
        return max(a,b)