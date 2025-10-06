def lenbs(s):
    dct = {}
    temp = 0
    max_len = 0
    for i,v  in enumerate(s):
        if v in dct and dct[v] >= temp:
            temp = dct[v] + 1
        dct[v] = i
        max_len = max(max_len, i - temp + 1)
    return max_len