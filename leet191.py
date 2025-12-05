class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in bin(n)[2:]:
            if i == "1":
                c += 1
        return c