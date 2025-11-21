from functools import lru_cache
def wordBreak(s, wordDict):
        lo, hi, l, f= float("inf"), float("-inf"), len(s), set()
        for x in wordDict:
            n = len(x)
            if lo > n:
                lo = n
            if hi < n:
                hi = n
            f.add(x)

        fin = []
        @lru_cache(None)
        def dfs(i):
            if i == l:
                return [[]]
            lst = []
            for x in range(lo,hi+1):
                slc = s[i:i+x]
                if slc in f:
                    for a in dfs(x+i):
                        if a:
                            lst.append(slc + " " + a)
                        else:
                            lst.append(slc)
            return lst
        return dfs(0)