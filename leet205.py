class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        x = 0
        for i in range(len(s)):
            a, b = ("a", s[i]), ("b", t[i])
            if (a in d) ^ (b in d):
                return False
            if a in d:
                if d[a] != d[b]:
                    return False
            else:
                d[a] = x
                d[b] = x
                x += 1
        return True