def isMatch(s,p):
        cache = {}
        def ugh(i, j):
            print(i,j)
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i,j)] = (match and ugh(i + 1, j)) or ugh (i, j + 2)
                return cache[(i,j)]
            if match:
                cache[(i,j)] = ugh(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return cache[(i,j)]
        return ugh(0,0)