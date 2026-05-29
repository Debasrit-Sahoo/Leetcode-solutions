class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0]*32
        for x in nums:
            for i in range(32):
                bits[i] += (x >> i) & 1

        for i in range(32):
            bits[i] = '1' if bits[i] >= k else '0'

        return int("".join(bits[::-1]), 2)