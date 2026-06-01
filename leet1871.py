class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1': return False

        n = len(s)
        dp = [0]*n
        dp[0] = True
        lo, hi = maxJump, minJump
        c = 0

        for i in range(hi, n):
            c -= dp[i - lo - 1]
            c += dp[i - hi]
            if s[i] == '0' and c: dp[i] = 1

        return bool(dp[-1])