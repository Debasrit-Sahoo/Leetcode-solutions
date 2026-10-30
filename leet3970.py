class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1: return 0
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        MAX = 1 << 31
        costs = [[MAX]* (k + 1) for _ in range(n)]
        costs[0][1] = 0
        heap = [(0, 0, 1)]

        pop = heapq.heappop
        push = heapq.heappush
        end = n - 1

        while heap:
            cost, node, streak = pop(heap)

            if node == end: return cost
            if cost != costs[node][streak]: continue

            for nxt, weight in graph[node]:
                ns = 1 + streak if labels[nxt] == labels[node] else 1
                if ns > k: continue
                nc = cost + weight
                if nc < costs[nxt][ns]:
                    costs[nxt][ns] = nc
                    push(heap, (nc, nxt, ns))
        return -1