class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        c = 0
        s = 0
        for i in nums:
            s += i
            c += d.get(s - k, 0)
            d[s] = d.get(s, 0) + 1

        return c