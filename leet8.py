def myAtoi(s):
        s = s.strip()
        if s == "":
            return 0
        bounds = [-2**31, 2**31 -1]
        sign = -1 if s[0] == "-" else 1
        if s[0] in ["-", "+"]:
            s = s[1:]
        for i in range(len(s)):
            print(i)
            if not s[i].isdigit():
                s = s[:i] if i >= 1 else 0
                break
        s = int(s) * sign if s != "" else 0
        return bounds[0] if s < bounds[0] else bounds[1] if s > bounds[1] else s
