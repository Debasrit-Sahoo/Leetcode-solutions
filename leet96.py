from functools import lru_cache
def numTrees(n):
        @lru_cache(None)
        def ahh(lo,hi):
            if lo>hi:
                return 1
            save = 0
            for root in range(lo,hi+1):
                    save += ahh(lo,root-1) * ahh(root+1, hi)
            return save
        return ahh(1,n)