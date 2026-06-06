class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        MAX = 10000001
        hi = MAX
        lo = 1

        d = dist
        final = dist.pop()

        while lo < hi:
            mid = (lo + hi) // 2
            if (sum((i + mid - 1) // mid for i in d) + final / mid) <= hour:
                hi = mid
            else:
                lo = mid + 1

        return lo if lo != MAX else -1