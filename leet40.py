from collections import Counter
def combinationSum2(candidates, target):
    candidates.sort()
    freq = list(Counter(candidates).items())
    combs = []
    def dfs(lst, s, i):
        if s == target:
            combs.append(lst[:])
            return
        if s > target or i < 0:
            return
        cur, cnt = freq[i]
        for x in range(cnt+1):
            if s + cur*x > target:
                break
            lst.extend([cur]*x)
            dfs(lst, s+ cur*x, i - 1)
            for _ in range(x):
                lst.pop()
    dfs([], 0, len(freq) - 1)
    return combs