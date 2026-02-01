class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        zero = p = 0
        l = len(nums)
        while p < l and zero < l:
            if nums[p] != 0:
                if p != zero: nums[p], nums[zero] = nums[zero], nums[p]
                zero += 1
            p += 1