class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        xs, ys = zip(*coords)
        xs = list(xs)
        ys = list(ys)
        min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

        xb, yb = defaultdict(list), defaultdict(list)
        area = 0

        for i in range(len(xs)):
            x, y = xs[i], ys[i]
            xb[x].append(y)
            yb[y].append(x)

        for x, yl in xb.items():
            if len(yl) < 2: continue
            b = max(yl) - min(yl)
            h = max(abs(x - min_x), abs(x - max_x))
            area = max(area, b * h)

        for y, xl in yb.items():
            if len(xl) < 2: continue
            b = max(xl) - min(xl)
            h = max(abs(y - min_y), abs(y - max_y))
            area = max(area, b * h)

        return area if area > 0 else -1