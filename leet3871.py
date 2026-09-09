class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        p = 1000
        commas = 1

        while p <= n:
            nxt = p * 1000
            end = min(n, nxt - 1)

            ans += (end - p + 1) * commas

            p = nxt
            commas += 1

        return ans