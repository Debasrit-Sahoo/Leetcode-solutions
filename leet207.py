from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        m = defaultdict(list)
        for i in prerequisites:
            m[i[0]].append(i[1])
        f = set()
        def cycle(node,s):
            if node in s: return True
            if node in f: return False
            if node not in m: return False
            s.add(node)
            for i in m[node]:
                if cycle(i,s): return True
            s.remove(node)
            f.add(node)
            return False
        for i in range(numCourses):
            if cycle(i,set()):
                return False
        return True