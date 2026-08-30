class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return n
        MXV = -(1 << 31)
        MNV = 1 << 31
        MNI = MXI = -1

        for i, v in enumerate(nums):
            if v > MXV: MXV = v; MXI = i
            if v < MNV: MNV = v; MNI = i

        MNI, MXI = min(MNI, MXI), max(MNI, MXI)
        return min(1 + MXI, n - MNI, 1 + MNI + n - MXI)