class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        a = 0
        b = costs[0] + 1
        if n == 1: return b
        c = costs[1] + min(a + 4, b + 1)
        if n == 2: return c

        for i in range(2, n):
            c, b, a = costs[i] + min(c + 1, b + 4, a + 9), c, b
        return c