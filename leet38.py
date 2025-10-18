def countAndSay(n):
    s = ['1']
    for _ in range(n-1):
        new = []
        cur = s[0]
        count = 0
        for x in s:
            if x == cur:
                count += 1
            else:
                new.append(str(count))
                new.append(cur)
                cur = x
                count = 1
        if count:
            new.append(str(count))
            new.append(cur)
        s = new
    return "".join(s)