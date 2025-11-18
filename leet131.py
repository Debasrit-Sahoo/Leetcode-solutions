def partition(s):
    final = []
    l = len(s)

    def dfs(lst,sp):
        if sp == l:
            final.append(lst[:])
            return
        for x in range(sp, l):
            c = s[sp:x+1] 
            if c == c [::-1]:
                lst.append(c)
                dfs(lst, x+1)
                lst.pop()
    dfs([],0)
    return final