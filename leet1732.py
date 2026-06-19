class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = m = 0

        for g in gain:
            s+=g
            if s > m: m = s

        return m