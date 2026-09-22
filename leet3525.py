class Solution:
    class Segtree:
        def __init__(self, n, k) -> None:
            self.tree = [None] * (n << 2)
            self.k = k

        def merge(self, l, r):
            par = l.copy()

            for ep in range(self.k):
                par[(l[-1] * ep) % self.k] += r[ep]

            par[-1] = (l[-1] * r[-1]) % self.k
            return par
        
        def build(self, i, l, r, arr):
            if l == r:
                self.tree[i] = [0] * self.k + [arr[l] % self.k]
                self.tree[i][arr[l] % self.k] = 1

            else:
                m = (l + r) >> 1

                self.build(i << 1, l, m, arr)
                self.build((i << 1) | 1, m + 1, r, arr)

                self.tree[i] = self.merge(self.tree[i << 1], self.tree[(i << 1) | 1])

        def update(self, i, l, r, pos, val):
            if l == r:
                self.tree[i] = [0] * self.k + [val % self.k]
                self.tree[i][val % self.k] = 1
                return

            m = (l + r) >> 1

            if pos <= m:
                self.update(i << 1, l, m, pos, val)
            else:
                self.update((i << 1) | 1, m + 1, r, pos, val)

            self.tree[i] = self.merge(self.tree[i << 1], self.tree[(i << 1) | 1])

        def query(self, i, l, r, ql, qr):
            if ql <= l and r <= qr:
                return self.tree[i]

            m = (l + r) >> 1

            if qr <= m:
                return self.query(i << 1, l, m, ql, qr)
            if ql > m:
                return self.query((i << 1) | 1, m + 1, r, ql, qr)
    
            left = self.query(i << 1, l, m, ql, qr)
            right = self.query((i << 1) | 1, m + 1, r, ql, qr)

            return self.merge(left, right)

    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = self.Segtree(n, k)
        seg.build(1, 0, n - 1, nums)
        ans = []

        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            node = seg.query(1, 0, n - 1, start, n - 1)
            ans.append(node[x])

        return ans