class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t = 1
        l = len(nums)
        arr = [0]*l
        for i in range(l):
            t *= nums[i]
            arr[i] = t
        t = 1
        for i in range(l-1, 0, -1):
            p = nums[i]
            nums[i] = t*arr[i-1]
            t *= p
        nums[0] = t
        return nums