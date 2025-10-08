def convert(s,r):
        r -= 1
        d = [""] * (r+1)
        level = 0
        for v in s:
            d[level] = d[level] + v 
            if level == 0:
                check = 0
            if level == r:
                check = 1
            level = level + 1 if check == 0 else level - 1
        out = ""
        for i in d:
            out = out + i
        return out