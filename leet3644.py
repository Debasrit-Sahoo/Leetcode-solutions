class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = ~0
        for i in range(len(nums)):
            if i != nums[i]: ans &= nums[i]

        if ans == ~0: return 0
        return ans