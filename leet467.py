class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        a = [0]*26
        p = ord(s[0]) - 1
        z = ord('z')
        ax = ord('a')
        l = 0
        for c in s:
            o = ord(c)
            if o - p == 1 or (o == ax and p == z):
                l += 1
            else:
                l = 1
            i = o - ax
            if a[i] < l: a[i] = l
            p = o

        return sum(a)