class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        p = 0
        q = deque([p]); visited = [False] * n; visited[p] = True
        while q:
            node = q.popleft()
            p = node
            for i in graph[node]:
                if not visited[i]: q.append(i); visited[i] = True
        q.append(p); visited = [False]*n; visited[p] = True; parents = [-1]*n; end = 0
        while q:
            node = q.popleft()
            end = node
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True; q.append(i); parents[i] = node
        p = []
        while end != -1:
            p.append(end)
            end = parents[end]

        l = len(p)
        if l % 2 == 1:
            return [p[l//2]]
        else:
            return [p[l//2], p[l//2 - 1]]