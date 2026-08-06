class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, ((n+9)//10)*10 + 2):
            p = i if i < 10 else (i // 10) * (i % 10)
            if gcd(p, t) == t: return i