def addBinary(a, b):
        x = -1
        o = []
        a, b = b if len(a) < len(b) else a, a if len(a) < len(b) else b
        c = 0
        while -x <= len(b):
            b1, b2 = int(a[x]), int(b[x])
            o.append(c ^ b1 ^ b2)
            c = ((b1 and b2) or (c and (b1 ^ b2)))
            x -= 1
        while -x <= len(a):
            s = int(a[x])
            o.append(s ^ c) 
            c = s and c
            x -= 1
        if c:
            o.append(c)
        return "".join(map(str,o[::-1]))