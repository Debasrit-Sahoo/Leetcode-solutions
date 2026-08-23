class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        l = r = ls = rs = 0

        for i in range(n >> 1):
            if num[i] == '?': l+=1
            else: ls += int(num[i])

        for i in range(n >> 1, n):
            if num[i] == '?': r+=1
            else: rs += int(num[i])

        if l == r: return ls != rs
        if (l - r) & 1: return True

        if l > r:
            return rs - ls != 9 * (l - r) >> 1

        return ls - rs != 9 * (r - l) >> 1