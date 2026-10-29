class Solution:
    #god help me
    class Segtree:
        def __init__(self, base):
            self.n = len(base)
            self.t = [0] * self.n + base
            for i in range(self.n - 1, 0, -1):
                self.t[i] = self.t[i * 2] ^ self.t[i * 2 + 1]

        def update(self, i, val):
            i += self.n
            self.t[i] = val
            while i > 1:
                i //= 2
                self.t[i] = self.t[i * 2] ^ self.t[i * 2 + 1]

        def query(self, l, r):
            res = 0
            l += self.n
            r += self.n + 1
            while l < r:
                if l & 1:
                    res ^= self.t[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= self.t[r]

                l//=2
                r//=2
            return res

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        size = [1] * n
        heavy = [-1] * n
        parent = [-1] * n
        depth = [0] * n

        def weight(node, par):
            for child in adj[node]:
                if par == child: continue
                parent[child] = node
                depth[child] = depth[node] + 1
                weight(child, node)
                size[node] += size[child]
                if heavy[node] == -1 or size[child] > size[heavy[node]]:
                    heavy[node] = child

        weight(0, -1)

        head = [0] * n
        pos = [0] * n
        cnt = 0

        def enum(cur, par, start):
            nonlocal cnt
            head[cur] = start
            pos[cur] = cnt
            cnt += 1

            if heavy[cur] != -1:
                enum(heavy[cur], cur, start)
            for child in adj[cur]:
                if child == heavy[cur] or child == par: continue
                enum(child, cur, child)

        enum(0, -1, 0)

        off = ord('a')
        base = [0] * n
        for v in range(n):
            base[pos[v]] = 1 << (ord(s[v]) - off)
        seg = self.Segtree(base)

        def path_mask(a, b):
            res = 0
            while head[a] != head[b]:
                if depth[head[a]] < depth[head[b]]:
                    a, b = b, a
                res ^= seg.query(pos[head[a]], pos[a])
                a = parent[head[a]]
            if depth[a] > depth[b]:
                a, b = b, a
            res ^= seg.query(pos[a], pos[b])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0][0] == 'q':
                m = path_mask(int(parts[1]), int(parts[2]))
                ans.append(m & (m - 1) == 0)
            else:
                i, c = int(parts[1]), parts[2]
                seg.update(pos[i], 1 << (ord(c) - off))

        return ans