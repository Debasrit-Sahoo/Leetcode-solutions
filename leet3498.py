class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(i * (123 - ord(v)) for i, v in enumerate(s, start=1))