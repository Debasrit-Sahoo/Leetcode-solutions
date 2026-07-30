class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        t = n >> 3
        return (t + 1) * ((t << 2) + (n & 7))