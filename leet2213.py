class Solution:
    class Segtree:
        def __init__(self, n: int) -> None:
            self.tree = [[0, 0, 0, 0, 0] for _ in range(4 * n)]
            # best, [0], [-1], longest pref, longest suf

        def build(self, node, lo, hi, s):
            if lo == hi:
                c = s[lo]
                self.tree[node] = [1, c, c, 1, 1]
                return

            mid = (lo + hi) >> 1

            self.build(node << 1, lo, mid, s)
            self.build(node << 1 | 1, mid + 1, hi, s)

            self.merge(
                self.tree[node],
                self.tree[node << 1],
                self.tree[node << 1 | 1],
                mid - lo + 1,
                hi - mid
            )

        def update(self, node, lo, hi, pos, value):
            if lo == hi:
                self.tree[node] = value
                return

            mid = (lo + hi) >> 1

            node <<= 1

            if pos <= mid:
                self.update(node, lo, mid, pos, value)
            else:
                self.update(node + 1, mid + 1, hi, pos, value)

            self.merge(self.tree[node >> 1], self.tree[node], self.tree[node | 1], mid - lo + 1, hi - mid)

        def merge(self, parent, left, right, n1, n2):
            match = left[2] == right[1]
            parent[0] = max(left[0], right[0], left[4] + right[3] if match else 0)
            parent[1] = left[1]
            parent[2] = right[2]
            parent[3] = left[3] + (right[3] if match and left[3] == n1 else 0)
            parent[4] = right[4] + (left[4] if match and right[4] == n2 else 0)
            

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        seg = self.Segtree(n)

        seg.build(1, 0, n - 1, s)

        for j, (c, i) in enumerate(zip(queryCharacters, queryIndices)):
            seg.update(1, 0, n - 1, i, [1, c, c, 1, 1])
            queryIndices[j] = seg.tree[1][0]

        return queryIndices