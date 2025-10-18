def combinationSum(candidates, target):
    candidates.sort()
    combs = []
    def dfs(lst,s,i):
        if s == target:
            combs.append(lst[:])
            return
        if s > target or i < 0:
            return
        lst.append(candidates[i])
        dfs(lst, s + candidates[i], i)
        lst.pop()
        dfs(lst, s, i- 1)
    dfs([], 0, len(candidates) - 1)
    return combs