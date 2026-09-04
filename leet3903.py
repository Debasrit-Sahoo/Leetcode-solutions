class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        rmin = [0] * len(nums)
        mn = rmax = 1 << 32
        rmax *= -1

        for i, v in enumerate(reversed(nums), start=1):
            if mn > v: mn = v
            rmin[-i] = mn

        for i, v in enumerate(nums):
            if v > rmax: rmax = v
            c = rmax - rmin[i]
            if c <= k: return i

        return -1