###NEEDS REWORK
def longestPalindrome(s):
        out, l = "" , len(s)
        for i in range(l):
            temp, f, m, n = s[i], 1, 0, 0
            if (i - 1) >= 0 and (i+1) < l:
                left, right = s[i - 1], s[i + 1]
                if left != right:
                    if right == temp:
                        n = 1
                        temp = s[i:i+n+1]
            while (i-f-m) >= 0 and (i+f+n) < l:
                left, right = s[i-f-m], s[i+f+n]
                if left == right:
                    f += 1
                else:
                    break
            m, n = (i-f-m), (i+f+n)
            out = s[m+1:n] if n-m > len(out) else out
        return out