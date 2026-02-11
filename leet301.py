class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lr = rr = 0
        for i in s:
            if i == '(':lr += 1
            elif i == ')':
                if lr > 0: lr -= 1
                else: rr += 1
        done = set()
        q = deque([()])
        l = len(s)
        out = set()
        while q:
            xl = len(q)
            for _ in range(xl):
                skip = q.popleft()
                stack = []
                invalid = False
                for i, v in enumerate(s):
                    if i in skip: continue
                    if v == '(': stack.append(0)
                    if v == ')': 
                        if stack: stack.pop()
                        else: invalid = True; break
                if len(stack) != 0 or invalid:
                    for i in range(l):
                        if i not in skip:
                            n = skip + (i,)
                            if n not in done:
                                q.append(n); done.add(n)
                else:
                    j = []
                    for i in range(l):
                        if i in skip: continue
                        j.append(s[i])
                    out.add("".join(j))
            if out: break
        return list(out)