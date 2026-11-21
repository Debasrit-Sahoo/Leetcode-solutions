class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(s)
        graph = [[] for _ in range(n)]
        for num in range(1, n):
            graph[parent[num]].append(num)

        offset = ord('a')

        def dfs(node, chrstck):
            idx = ord(s[node]) - offset
            if chrstck[idx]:
                parent[node] = chrstck[idx][-1]

            chrstck[idx].append(node)

            for child in graph[node]:
                dfs(child, chrstck)

            chrstck[idx].pop()

        dfs(0, [[] for _ in range(26)])

        graph = [[] for _ in range(n)]
        for num in range(1, n):
            graph[parent[num]].append(num)

        def pso(node):
            acc = 1
            for x in graph[node]:
                acc += pso(x)
            parent[node] = acc
            return acc

        pso(0)

        return parent