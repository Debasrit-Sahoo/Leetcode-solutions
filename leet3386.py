class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        k = 0
        d = 0
        p = 0
        for i in range(len(events)):
            x = events[i]
            if x[1] - p > d: d = x[1] - p; k = x[0]
            elif x[1] - p == d: k = k if k < x[0] else x[0]
            p = x[1]

        return k