class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        e = intervals[0][1]
        ans = 1

        for i in range(1, len(intervals)):
            e1 = intervals[i][1]

            if e < e1: e = e1; ans += 1

        return ans