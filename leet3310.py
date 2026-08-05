class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            for a, b in invocations:
                graph[a].append(b)

            s = [0]*n

            def dfs(node):
                if s[node]: return
                s[node] = 1
                for each in graph[node]:
                    dfs(each)

            dfs(k)

            for a, b in invocations:
                if not s[a] and s[b]:
                    return [i for i in range(n)]
            
            return [i for i in range(n) if not s[i]]