def simplifyPath(path):
        path = path + "/"
        cur = []
        res = []
        for i in range(len(path)):
            if path[i] == "/":
                if i+1 < len(path) and path[i+1] == "/":
                    continue
                else:
                    cur = "".join(cur)
                    if cur == ".":
                        cur = []
                    elif cur == "..":
                        if res:
                            res.pop()
                        cur = []
                    else:
                        if cur != "":
                            res.append(cur)
                        cur = []
            elif path[i] != "/":
                cur.append(path[i])
        print(cur)
        return "/" + "/".join(res)