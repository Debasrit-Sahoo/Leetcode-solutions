class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n
        run = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n-mid:
                run = max(run, n-mid)
                hi = mid
            else:
                lo = mid+1
        return n - lo