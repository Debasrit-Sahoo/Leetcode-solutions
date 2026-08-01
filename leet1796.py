class Solution:
    def secondHighest(self, s: str) -> int:
        mx1 = mx2 = -1
        for c in s:
            if c.isdigit():
                c = int(c)

                if c > mx1:
                    mx2 = mx1
                    mx1 = c
                elif mx1 > c > mx2:
                    mx2 = c
        
        return mx2