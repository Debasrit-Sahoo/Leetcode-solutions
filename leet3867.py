class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        for i, v in enumerate(nums):
            if v > mx:
                mx = v
            nums[i] = gcd(v, mx)

        nums.sort()
        return sum(gcd(nums[i], nums[-i-1]) for i in range(len(nums) >> 1))