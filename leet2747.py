class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        timestamps = defaultdict(list)
        for id, time in logs: timestamps[time].append(id)
        time = sorted(timestamps.keys())
        queries = sorted((q, i) for i, q in enumerate(queries))
        ans = [0] * len(queries)

        freq = [0] * (n + 1)
        active = 0
        ri = 0
        li = 0

        for qi, (right, og_idx) in enumerate(queries):
            while ri < len(time) and time[ri] <= right:
                for id in timestamps[time[ri]]:
                    if freq[id] == 0: active += 1
                    freq[id] += 1
                ri += 1

            while li < len(time) and time[li] < right - x:
                for id in timestamps[time[li]]:
                    if freq[id] == 1: active -= 1
                    freq[id] -= 1
                li += 1

            ans[og_idx] = n - active

        return ans