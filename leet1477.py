class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ht = {0:-1}
        starts = []
        ends = []

        s = 0
        for i, v in enumerate(arr):
            s += v
            if s - target in ht:
                starts.append(ht[s-target])
                ends.append(i)

            ht[s] = i

        n = len(starts)
        if n < 2: return -1

        ans = mn = s = 1 << 31
        rmin = [0] * n

        for i in range(n):
            mn = min(mn, ends[i] - starts[i])
            rmin[i] = mn

        for i in range(n):
            j = bisect_right(ends, starts[i])
            if not j: continue
            ans = min(ans, rmin[j - 1] + ends[i] - starts[i])

        return ans if ans != s else -1