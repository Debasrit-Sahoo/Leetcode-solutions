class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = defaultdict(list)
        MAX = 0
        n = len(online) - 1
        for a, b, c in edges:
            if online[a] and online[b]:
                graph[a].append((b, c))
                if c > MAX: MAX = c

        DEF_INF = 10**30

        def check(mid):
            h = [(0, 0)]
            push = heapq.heappush
            pop = heapq.heappop
            dist = [DEF_INF] * (n + 1)
            dist[0] = 0

            while h:
                cost, u = pop(h)

                if cost > dist[u]: continue

                if u == n: return True

                for v, w in graph[u]:
                    if w < mid: continue
                    nc = cost + w
                    if nc > k: continue

                    if nc < dist[v]:
                        dist[v] = nc
                        push(h, (nc, v))

            return False
        
        if not check(0): return -1

        lo, hi = 0, MAX
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo