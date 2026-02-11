class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lr = rr = 0
        for i in s:
            if i == '(':lr += 1
            elif i == ')':
                if lr > 0: lr -= 1
                else: rr += 1
        seen = set()
        q = deque([(s, lr ,rr)])
        out = []
        while q:
            h = len(q)
            for _ in range(h):
                cur, l, r = q.popleft()
                if l == 0 and r == 0:
                    stk = f = 0
                    for i in cur:
                        if i == '(': stk += 1
                        elif i == ')': stk -= 1
                        if stk < 0: f = 1; break
                    if not f and stk == 0: out.append(cur)
                    continue
                for i in range(len(cur)):
                    if cur[i] == '(' and l > 0:
                        ns = cur[:i] + cur [i+1:]
                        if ns not in seen:
                            seen.add(ns)
                            q.append((ns, l-1, r))
                    elif cur[i] == ')' and r > 0:
                        ns = cur[:i] + cur [i+1:]
                        if ns not in seen:
                            seen.add(ns)
                            q.append((ns, l, r-1))
            if out: break
        return out