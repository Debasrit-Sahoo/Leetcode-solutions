class Solution:
    def canAliceWin(self, n: int) -> bool:
        t = 10
        ans = False
        while n >= t:
            ans ^= 1
            n -= t
            t -= 1
        return bool(ans)