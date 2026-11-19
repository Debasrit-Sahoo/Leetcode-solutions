class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 1 << 31
        lsum = sum(nums[:l-1])
        
        for size in range(l, r + 1):
            lsum += nums[size - 1]
            cur = lsum
            if cur > 0: ans = min(ans, cur)
            for r in range(size, n):
                cur += nums[r] - nums[r - size]
                if cur < 1: continue
                ans = min(ans, cur)

        return ans if ans != 1 << 31 else -1