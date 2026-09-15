class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        cnt = 0

        i = 0
        n = len(s) - k

        while i <= n:
            if s[i:i + k] == s[i:i + k][::-1]:
                i += k
                cnt += 1
            elif i <= n and s[i:i + k+1] == s[i:i + k+1][::-1]:
                i += k + 1
                cnt += 1
            else:
                i += 1

        return cnt