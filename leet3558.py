class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range((len(edges) + 2))]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            n = graph[node]
            graph[node] = []
            m = 0
            for i in n:
                if not graph[i]: continue
                a = dfs(i)
                if a > m: m = a
            return 1 + m

        return pow(2, dfs(1) - 2, 1000000007)