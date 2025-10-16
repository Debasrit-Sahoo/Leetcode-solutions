def strStr(haystack, needle):
    i = 0
    j = 0
    while i < len(haystack):
        print(haystack[i], needle[j])
        print(i,j)
        if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
                return i - j + 1
        elif j and haystack[i] != needle[j]:
            i = i - (j-1)
            j = 0
            continue
        i += 1
    return -1