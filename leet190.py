class Solution:
    def reverseBits(self, n):
        return int(f"{n & 0xffffffff:032b}"[::-1],2)