class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = 0
        cnt = 0
        q = deque()

        for node in range(n):
            if (seen >> node) & 1: continue

            seen |= 1 << node
            comp = len(graph[node])
            nodes = 0
            pure = 1

            q.append(node)
            while q:
                n = q.popleft()
                nodes += 1
                if pure:
                    if comp != len(graph[n]): pure = 0

                for each in graph[n]:
                    if (seen >> each) & 1: continue
                    q.append(each)
                    seen |= (1 << each)

            cnt += pure and comp == nodes - 1

        return cnt
