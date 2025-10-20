from functools import lru_cache
def isMatch(s, p):
    l = []
    for x in range(len(p)):
        if x + 1 < len(p) and p[x] == "*" and p[x+1] == "*":
            continue
        l.append(p[x])
    p = "".join(l)
    @lru_cache(None)
    def dfs(i,j):
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        if p[j] == "*":
            return dfs(i, j+1) or (i<len(s) and dfs(i+1, j))
        else:
            mat = i < len(s) and (s[i] == p[j] or p[j] == "?")
            return dfs(i+1, j+1) and mat
    return dfs(0,0)