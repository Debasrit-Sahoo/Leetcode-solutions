class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        u = d = 1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                u = d + 1
            elif nums[i-1] < nums[i]:
                d = u + 1
        return max(u,d)