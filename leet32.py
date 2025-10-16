def longestValidParentheses(s):
    l, r = 0, 0
    max_len = 0
    for i in range(len(s)):
        if s[i] == "(":
            l += 1
        if s[i] == ")":
            r += 1
        if r == l:
            max_len = l*2 if l*2 > max_len else max_len
        if r > l:
            l, r = 0, 0
    l, r = 0, 0 
    for i in range(len(s)-1, -1, -1):
        if s[i] == "(":
            l += 1
        if s[i] == ")":
            r += 1
        if r == l:
            max_len = l*2 if l*2 > max_len else max_len
        if r < l:
            l, r = 0, 0
    return max_len