class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        circular_dist = lambda a, b: min(abs(a - b), n - abs(a - b))

        idxs = [set() for _ in range(26)]
        offset = ord('a')
        for i,v in enumerate(ring):
            idxs[ord(v) - offset].add(i)

        inf = 10**9
        prev = [inf]*n
        prev[0] = 0

        for c in key:
            cur = [inf]*n
            for start in range(n):
                if prev[start] == inf: continue
                for end in idxs[ord(c) - offset]:
                    cur[end] = min(cur[end], prev[start] + circular_dist(start, end) + 1)
            
            prev = cur
        
        return min(prev)