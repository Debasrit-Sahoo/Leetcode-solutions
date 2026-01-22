class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = 0
        for x in nums: n ^= x
        d = (n & -n)
        o = [0, 0]
        for x in nums: o[bool(x&d)] ^= x
        return o