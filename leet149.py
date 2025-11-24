from math import gcd
def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n
    m = 1
    for i in range(n):
        slope = {}
        d = 0
        c = 0
        for j in range(n):
            if i == j:
                continue
            dx, dy = points[j][0] - points[i][0], points[j][-1] - points[i][-1]
            if dx == 0 and dy == 0:
                d += 1
                continue
            elif dx == 0:
                s = (1,0)
            elif dy == 0:
                s = (0,1,)
            else:
                a = gcd(dx,dy)
                dy //= a
                if dx < 0:
                    dx, dy = -dx, -dy
                s = (dx,dy)
            slope[s] = slope.get(s, 0) + 1
            if c < slope[s]:
                c = slope[s]
        lm = c + 1 + d
        if lm > m:
            m = lm
    return m