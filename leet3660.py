class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pmax = [0]*n
        pmax[0] = nums[0]
        for i in range(1, n):
            pmax[i] = nums[i] if nums[i] > pmax[i-1] else pmax[i-1]

        smin = 1<<32
        for i in range(n-1, -1, -1):
            s = smin if nums[i] > smin else nums[i]
            if pmax[i] > smin:
                nums[i] = nums[i+1]
            else:
                nums[i] = pmax[i]
            smin = s

        return nums