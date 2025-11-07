from functools import lru_cache
from collections import Counter
def isInterleave(s1, s2 , s3):
        @lru_cache(None)
        def backtrack(p1, p2, p3, t):
            if p3 == len(s3):
                return True if p1 == len(s1) and p2 == len(s2) else False
            if t:
                while p1<len(s1) and p3 < len(s3) and s1[p1] == s3[p3]:
                    if (len(s1) - p1 + len(s2) - p2) == (len(s3) - p3):
                        if backtrack(p1 + 1, p2, p3 + 1, False):
                            return True
                    p1 += 1
                    p3 += 1
                return False
            else:
                while p2<len(s2) and p3 < len(s3) and s2[p2] == s3[p3]:
                    if (len(s1) - p1 + len(s2) - p2) == (len(s3) - p3):
                        if backtrack(p1, p2 + 1, p3 +1, True):
                            return True
                    p2 += 1
                    p3 += 1
                return False
        return backtrack(0,0,0,0) or backtrack(0,0,0,1)