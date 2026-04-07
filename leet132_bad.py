from collections import deque
from functools import lru_cache
def minCut(s):
    @lru_cache(None)
    def comp(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    l = len(s)
    d = 0
    if s == s[::-1]:
        return d
    stack = deque([0])
    while stack:
        sl = len(stack)
        d += 1
        for _ in range(sl):
            lo = stack.popleft()
            for i in range(lo,l):
                if comp(lo, i):
                    if comp(i+1, l-1):
                        return d
                    stack.append(i+1)
    return 0