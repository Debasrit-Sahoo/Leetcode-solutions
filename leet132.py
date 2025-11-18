def minCut(s):
        l = len(s)
        is_pal = [[False for _ in range(l)] for _ in range(l)]
        for x in range(l):
            is_pal[x][x] = True
            if x+1 < l and s[x] == s[x+1]:
                is_pal[x][x+1] = True 
        for length in range(3,l+1):
            for i in range(l-length+1):
                j = i + length - 1
                if s[i] == s[j] and is_pal[i+1][j-1]:
                    is_pal[i][j] = True
        m = [0]*l
        for i in range(l):
            if is_pal[0][i]:
                m[i] = 0
            else:
                m[i] = min(m[j] + 1 for j in range(i) if is_pal[j+1][i])
        return m[-1]