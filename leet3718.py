class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        x = [0] * n
        for each in nums:
            if not each % k and each // k < n: x[each // k] |= 1

        for i in range(1, n):
            if not x[i]: return i * k
        else:
            return n * k