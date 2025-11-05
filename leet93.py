def restoreIpAddresses(s):
        save = []
        def backtrack(l,p):
            print(l)
            if len(l) == 4 or p == len(s):
                if len(l) == 4 and p == len(s):
                    save.append(".".join(l))
                return
            if s[p] == "0":
                l.append("0")
                backtrack(l,p+1)
                l.pop()
            else: 
                l.append(s[p])
                backtrack(l,p+1)
                l.pop()
                if p+1 < len(s):
                    l.append(s[p:p+2])
                    backtrack(l,p+2)
                    l.pop()
                if p+2 < len(s) and int(s[p:p+3]) <= 255:
                    l.append(s[p:p+3])
                    backtrack(l,p+3)
                    l.pop()
        backtrack([], 0)
        return save