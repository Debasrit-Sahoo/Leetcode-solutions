class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(32):
            bs = 1 << i
            s1 = sum(1 for a in nums if a & bs)
            ans += s1 * (n - s1)
        return ans