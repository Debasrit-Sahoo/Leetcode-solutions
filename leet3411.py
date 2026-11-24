class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)

        for size in range(n, 1, -1):
            for l in range(n-size+1):
                s = nums[l:l+size]
                if math.prod(s) == math.lcm(*s) * math.gcd(*s): return size

        return 1