def simplifyPath(path):
        i = 0
        out = []
        last = []
        flag =  False
        for i in range(len(path)):
            print(path[i], out, last)
            if path[i] == "/":
                if flag:
                    flag = False
                if i+1 < len(path) and path[i+1] == "/":
                    continue
                else:
                    out.append("".join(last))
                    last.clear()
                    out.append("/")
            elif path[i] == "." and not flag:
                if i+1 < len(path) and path[i+1] == ".":
                    if i+2 < len(path) and path[i+2] == ".":
                        last.append(".")
                        flag = True
                        continue
                    else:
                        for _ in range(2):
                            if out:
                                out.pop()
                else:
                    if out:
                        out.pop()
            else:
                last.append(path[i])
        out.extend(last)
        if out[-1] == "/":
            out.pop()
        out = "".join(out).strip()
        if out.strip() == "":
            return "/"
        return out