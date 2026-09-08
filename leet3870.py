class Solution:
    def countCommas(self, n: int) -> int:
        n -= 999
        return n if n > 0 else 0