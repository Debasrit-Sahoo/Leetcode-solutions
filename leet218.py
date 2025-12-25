class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        changes = []
        for s,e,h in buildings:
            changes.append((s,-h))
            changes.append((e,h))
        changes.sort()

        heap = [0]
        exp = defaultdict(int)
        out = []
        height = 0

        for x, h in changes:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                exp[h] += 1
            while heap and exp[-heap[0]] > 0:
                exp[-heap[0]] -= 1
                heapq.heappop(heap)
            cur = -heap[0]
            if cur != height:
                out.append([x, cur])
                height = cur
        return out