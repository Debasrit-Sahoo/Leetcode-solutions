from collections import deque
def wordBreak(s, wordDict):
        f = set([])
        l = len(s)
        lo = float("inf")
        hi = float("-inf")
        for i in wordDict:
            x = len(i)
            if x < lo:
                lo = x
            if x > hi:
                hi = x
            f.add(i)
        stack = deque([0])
        seen = set()
        while stack:
            i = stack.popleft()
            if i in seen:
                continue
            seen.add(i)
            if i >= l:
                return True   
            for x in range(lo, hi+1):
                if s[i:i+x] in f:
                    stack.append(i+x)
        return False