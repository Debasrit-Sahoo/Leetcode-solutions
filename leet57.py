import bisect
def insert(intervals, newInterval):
        def merge(intervals):
            new = []
            lo, hi = float("inf"), float("-inf")
            p = -1
            for i in intervals:
                if lo <= i[0] and hi >= i[0]:
                    new[p][-1] = new[p][-1] if new[p][-1] > i[-1] else i[-1]
                    hi = new[p][-1]
                else:
                    new.append(i)
                    lo, hi = i[0], i[-1]
                    p += 1
            return new
        intervals.insert(bisect.bisect_left(intervals, newInterval), newInterval)
        return merge(intervals)