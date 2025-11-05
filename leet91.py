from functools import lru_cache
def numDecodings(s):
        ex = set(["1","2"])
        e = set(["0","7","8","9"])
        @lru_cache(None)
        def backtrack(p):
            if p == len(s):
                return 1
            if s[p] == "0":
                return 0
            else:
                s1 = backtrack(p+1)
                s2 = backtrack(p+2) if p+1 < len(s) and (s[p] == "1" or (s[p] == "2" and s[p+1] < "7")) else 0
                return s1 + s2
        return backtrack(0)