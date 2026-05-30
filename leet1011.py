class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            d = days - 1
            c = 0
            f = 1
            for w in weights:
                if c + w > mid: d -= 1; c = 0
                c += w
                if d < 0: f = 0; break
            if c > mid: d-=1
            if d >= 0 and f:
                hi = mid
            else:
                lo = mid + 1
        return lo