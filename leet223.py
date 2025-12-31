class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        xl = max(ax1, bx1)
        xr = min(ax2, bx2)
        yl = max(ay1, by1)
        yr = min(ay2, by2)
        r = abs(ax1- ax2)* abs(ay1-ay2)+abs(bx1-bx2)*abs(by1-by2)
        return r if not (xr > xl and yr > yl) else r - abs(xr-xl)*abs(yr-yl)