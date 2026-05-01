class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        out = []
        if not dictionary or not queries: return out
        n = len(queries[0])
        for q in queries:
            for d in dictionary:
                m = 0
                for i in range(n):
                    if q[i] != d[i]:
                        m+=1
                        if m == 3: break
                if m == 3: continue
                out.append(q)
                break

        return out