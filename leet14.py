def longestCommonPrefix(s):
    pref = s[0]
    for i in s:
        if i == "" or pref == "":
            return ""
        c = 0
        while True:
            if c >= len(i) or c >= len(pref) or pref[c] != i[c]:
                pref = pref[:c]
                break
            c += 1
    return pref