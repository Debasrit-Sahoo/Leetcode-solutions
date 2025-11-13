from functools import lru_cache
def numDistinct(s,t):
        @lru_cache(None)
        def rec(i,j):
            if len(t) == j:
                return 1
            if len(t) - j > len(s) - i:
                return 0
            if len(s) == i:
                return 0
            if s[i] == t[j]:
                return rec(i+1, j+1) + rec(i+1,j)
            else:
                return rec(i+1,j)
        return rec(0,0)