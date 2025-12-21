class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s1 = s + '$' + s[::-1]
        j = 0
        lps = [0]*len(s1)
        for i in range(1, len(s1)):
            while j > 0 and s1[i] != s1[j]:
                j = lps[j-1]
            if s1[i] == s1[j]:
                j += 1
            lps[i] = j
        return s[lps[-1]:][::-1] + s