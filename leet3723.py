class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        ans = ""
        for i in range(9, 0, -1):
            ans += str(i) * (s // i)
            s %= i

        rem = n - len(ans)
        if rem < 0: return ""

        return ans + '0'*rem