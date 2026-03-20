class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        p1, p2 = 0, 1
        for _ in range(2, n+1):
            p1, p2 = p2, p1+p2
        return p2 