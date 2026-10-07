class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        t = sum(nums)
        n = len(nums)
        n2 = n >> 1
        w = sum(nums[:n2])
        ans = 0
        for k in range(n):
            ans += w << 1 > t
            w += nums[(n2 + k) % n] - nums[k]

        return ans