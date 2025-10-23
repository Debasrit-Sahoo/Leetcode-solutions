def totalNQueens(n):
    combinations = []
    def lua(q,r, cols, dl, dr):
        if r == n:
            combinations.append(q)
            return
        for c in range(n):
            if c not in cols and r-c not in dl and r+c not in dr:
                cols.add(c)
                dl.add(r-c)
                dr.add(r+c)
                q.append((r,c))
                lua(q, r+1, cols, dl, dr)
                q.pop()
                dr.remove(r+c)
                dl.remove(r-c)
                cols.remove(c)
    lua([], 0, set(), set(), set())
    return len(combinations)