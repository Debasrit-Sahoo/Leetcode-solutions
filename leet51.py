def solveNQueens(n):
    combs= []
    def dfs(q, invalid):
        print(q, invalid)
        if len(q) == n:
            combs.append(q[:])
            return
        for i in range(n):
            for j in range(n):
                if (i,j) in invalid:
                    continue
                changes = invalid.copy()
                for y in range(n):
                    if (i,y) not in invalid:
                        changes.add((i,y))
                    if (y,j) not in invalid:
                        changes.add((y,j))
                    y += 1
                    if i+y < n and j + y < n and ((i+y),(j+y)) not in invalid:
                        changes.add(((i+y),(j+y)))
                    if i+y < n and j - y >= 0 and ((i+y),(j-y)) not in invalid:
                        changes.add(((i+y),(j-y)))
                q.append((i,j))
                dfs(q, changes)
                q.pop()
    dfs([], set())
    return combs