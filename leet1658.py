class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        cur = 0
        target = sum(nums) - x

        n = len(nums)
        i = 0
        ans = -1

        for j in range(n):
            cur += nums[j]
            while i <= j and cur > target:
                cur -= nums[i]
                i += 1

            if cur == target:
                ans = max(ans, j - i + 1)
        return n - ans if ans != -1 else -1