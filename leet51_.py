def solveNQueens(n):
        combs= []
        def dfs(q, r, c, dl, dr):
            if r == n:
                combs.append(q[:])
            for c_ in range(n):
                if c_ not in c and r+c_ not in dl and r-c_ not in dr:
                    coords = (r, c_)
                    c.add(c_)
                    dl.add(r+c_)
                    dr.add(r-c_)
                    q.append(coords)
                    dfs(q, r+1, c, dl, dr)
                    q.pop()
                    dr.remove(r-c_)
                    dl.remove(r+c_)
                    c.remove(c_)
        dfs([], 0, set(), set(), set())
        boards = []
        for comb in combs:
            temp = [["."]*n for _ in range(n)]
            for c in comb:
                i,j = c
                temp[i][j] = "Q"
            for x in range(len(temp)):
                temp[x] = "".join(temp[x])
            boards.append(temp)
        return boards