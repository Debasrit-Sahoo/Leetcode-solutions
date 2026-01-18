class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens, s = [], []
        for i in expression:
            if i in "*-+":
                tokens.append("".join(s)); s.clear()
                tokens.append(i)
            else:
                s.append(i)
        tokens.append("".join(s))
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return [int(tokens[i])]
            res = []
            for x in range(i+1, j, 2):
                o = tokens[x]
                l = dfs(i, x-1)
                r = dfs(x+1, j)
                for a in l:
                    for b in r:
                        if o == '+': res.append(a+b)
                        elif o == '-': res.append(a-b)
                        else: res.append(a*b)
            return res
        return dfs(0, len(tokens)-1)