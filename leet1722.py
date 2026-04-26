class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in allowedSwaps: graph[a].append(b); graph[b].append(a)
        n = len(target)
        ans = 0
        vis = [0]*n
        h = Counter()
        for i in range(n):
            if vis[i]: continue
            elems = []
            q = [i]
            while q:
                x = q.pop()
                if vis[x]: continue
                vis[x] ^= 1
                elems.append(x)
                for j in graph[x]:
                    if not vis[j]: q.append(j)

            for j in elems:
                h[source[j]]+=1
                h[target[j]]-=1

            for each in h.values():
                if each > 0: ans+=each
            h.clear()
    
        return ans