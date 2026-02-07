class MedianFinder:

    def __init__(self):
        self.lo = []; heapq.heapify(self.lo)
        self.hi = []; heapq.heapify(self.hi)

    def addNum(self, num: int) -> None:
        if not self.lo and num <= -self.lo[0]:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        elif len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        return -self.lo[0]