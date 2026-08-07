class Solution:
    class SegTree:
        def __init__(self, rle):
            self.rle = rle
            self.tree = [0] * (len(rle) << 1)
            self.build(1, 0, (len(rle) >> 1) - 1)

        def build(self, node, l, r):
            if l == r:
                idx = (l << 1) + 1
                self.tree[node] = self.rle[idx-1] + self.rle[idx+1]
                return
            mid = (l + r) >> 1
            self.build(node << 1, l, mid)
            self.build(node << 1 | 1, mid + 1, r)
            self.tree[node] = max(self.tree[node << 1], self.tree[node << 1 | 1])

        def query(self, node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return self.tree[node]
            mid = (l + r) >> 1
            return max(self.query(node << 1, l, mid, ql, qr), self.query(node << 1 | 1, mid + 1, r, ql, qr))

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        leading = 0
        while leading < len(s) and s[leading] == '1': leading += 1
        trailing = len(s) - 1
        while trailing >= leading and s[trailing] == '1': trailing -= 1

        rle = []
        mapping = [-1] * len(s)
        rle_start = []
        middle_ones = 0

        if leading <= trailing:
            st = s[leading]; cnt = 0; start = leading
            for i in range(leading, trailing + 1):
                if s[i] == st:
                    cnt += 1
                else:
                    rle.append(cnt); rle_start.append(start)
                    run = len(rle) - 1
                    for j in range(start, i): mapping[j] = run
                    if st == '1': middle_ones += cnt
                    st = s[i]; start = i; cnt = 1
            rle.append(cnt); rle_start.append(start)
            run = len(rle) - 1
            for j in range(start, trailing + 1): mapping[j] = run
            if st == '1': middle_ones += cnt

        total_ones = leading + middle_ones + (len(s) - 1 - trailing)
        n = len(rle)
        nseg = n >> 1

        if n < 3:
            return [total_ones] * len(queries)

        seg = self.SegTree(rle)

        def run_end(i):
            return rle_start[i] + rle[i] - 1

        def calc(l, r):
            if (mapping[l] == -1 and l > trailing) or (mapping[r] == -1 and r < leading):
                return 0

            ml = mapping[l]
            if ml == -1:
                map_l = 1
            elif ml & 1:
                map_l = ml + 2
            else:
                map_l = ml + 1

            mr = mapping[r]
            if mr == -1:
                map_r = n - 2
            elif mr & 1:
                map_r = mr - 2
            else:
                map_r = mr - 1

            if map_l > map_r or map_l >= n or map_r < 0:
                return 0

            def left_gain(i):
                zi = i - 1
                if rle_start[zi] >= l:
                    return rle[zi]
                return run_end(zi) - l + 1

            def right_gain(i):
                zi = i + 1
                if run_end(zi) <= r:
                    return rle[zi]
                return r - rle_start[zi] + 1
            best = 0
            if map_l == map_r:
                best = left_gain(map_l) + right_gain(map_l)
            else:
                best = max(best, left_gain(map_l) + rle[map_l + 1])
                best = max(best, rle[map_r - 1] + right_gain(map_r))
                if map_l + 2 <= map_r - 2:
                    best = max(best, seg.query(1, 0, nseg - 1, (map_l + 2) >> 1, (map_r - 2) >> 1))

            return best
        for qi, (l, r) in enumerate(queries):
            queries[qi] = calc(l, r) + total_ones
        return queries