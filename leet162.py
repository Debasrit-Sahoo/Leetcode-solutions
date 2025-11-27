class Solution:
    def findPeakElement(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid+1] > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo