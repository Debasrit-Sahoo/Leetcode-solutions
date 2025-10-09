def isMatch(s,p):
        c = {}
        def fun(i, j):
            print(i,j)
            if (i,j) in c:
                return c[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            m = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
            if (j+1 < len(p)) and (p[j+1] == "*"):
                c[(i,j)] = fun(i, j+2) or (m and fun(i+1,j))
                return c[(i,j)]
            if m:
                c[(i,j)] = fun(i+1, j+1)
                return c[(i,j)]
            c[(i,j)] = False
            return c[(i,j)]
        return fun(0,0)