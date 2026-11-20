class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        inc = ans = unc = 1
        for a, b in pairwise(nums):
            diff = b - a
            if diff == 2: inc, unc = 1, 1 + inc
            elif diff == 1: inc+=1; unc+=1
            elif diff == 0: inc = 1 + unc
            else: inc = unc = 1

            ans = max(ans, inc, unc)

        return ans