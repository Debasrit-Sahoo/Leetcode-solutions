class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ns = sum(nums)
        c = 0
        l = len(nums)
        for i, v in enumerate(nums): c += i*v
        m = c
        for i in range(l-1, -1, -1):
            c += ns - nums[i]*l
            m = max(m, c)
        return m