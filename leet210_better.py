from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        deps = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            deps[a] += 1
        queue = deque([i for i in range(numCourses) if deps[i] == 0])
        order = []

        while queue:
            cur = queue.popleft()
            order.append(cur)
            for n in graph[cur]:
                deps[n] -= 1
                if deps[n] == 0:
                    queue.append(n)
        
        if len(order) == numCourses:
            return order
        return []