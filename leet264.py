class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        ax = bx = cx = 0
        while len(l) < n:
            l.append(min(l[ax]*2, l[bx]*3, l[cx]*5))
            p = l[-1]
            if p == l[ax]*2: ax += 1
            if p == l[bx]*3: bx += 1
            if p == l[cx]*5: cx += 1
        return l[-1]