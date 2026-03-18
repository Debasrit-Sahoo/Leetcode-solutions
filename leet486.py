class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def d(l, r):
            if l == r: return nums[l]
            return max(
                nums[l] - d(l+1, r),
                nums[r] - d(l, r-1)
            )

        return d(0, len(nums) - 1) >= 0