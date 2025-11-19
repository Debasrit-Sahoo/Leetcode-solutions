def candy(ratings):
        tot = 1
        u = d = p = 0
        for i in range(1, len(ratings)):
            pre, nex = ratings[i-1], ratings[i]
            if pre < nex:
                u += 1
                d = 0
                p = u
                tot += u+1
            elif pre == nex:
                u = d = p = 0
                tot += 1
            else:
                d += 1
                u = 0
                tot += d
                if d > p:
                    tot += 1
        return tot