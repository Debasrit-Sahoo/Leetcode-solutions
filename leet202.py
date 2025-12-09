class Solution:
    def isHappy(self, n) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = str(n)
            a = 0
            for i in n:
                a += int(i)**2
            n = a
        return True