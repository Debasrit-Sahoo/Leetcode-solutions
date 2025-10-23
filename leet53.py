def maxSubArray(nums):
        om = float("-inf")
        im = 0
        for x in nums:
            im = x if im+x < x else im + x
            om = im if om < im else om
        return om