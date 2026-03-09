class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        l = 0
        p = float('-inf')
        for i,v in intervals:
            if i >= p:
                p = v
            else:
                l += 1
        return l