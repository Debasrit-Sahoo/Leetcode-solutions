class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        if n == 2:
            return 0 if s[0] <= s[-1] else -1

        for i in range(1, n):
            if s[i-1] > s[i]:
                break
        else:
            return 0

        mx = 'a'
        mn = 'z'
        for i, char in enumerate(s):
            if char > mx:
                mx = char
            if char < mn:
                mn = char

        if mn == s[0] or mx == s[-1]:
            return 1
        if not mn in s[:n-1] and not mx in s[1:]:
            return 3
        return 2