class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def find_prev(arr, pref, x):
            lo, hi = 0, pref

            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid][1] < x:
                    lo = mid + 1
                else:
                    hi = mid

            return lo - 1

        for i, (left, right, weight, index) in enumerate(intervals, start=1):
            ext = dp[find_prev(intervals, i, left) + 1]
            prev = dp[i-1]

            for k in range(1, 5):
                take_indices = tuple(sorted(ext[k-1][1] + (index,)))
                take = (ext[k-1][0] + weight, take_indices)
                skip = prev[k]
                if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
                    dp[i][k] = take
                else:
                    dp[i][k] = skip 

        max_score = max(dp[n][k][0] for k in range(1, 5))
        ans = min(dp[n][k][1] for k in range(1, 5) if dp[n][k][0] == max_score)

        return ans