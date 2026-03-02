class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t and s: return False
        i = 0
        for c in t:
            if c == s[i]:
                i+=1
            if i == len(s):
                return True
        return False