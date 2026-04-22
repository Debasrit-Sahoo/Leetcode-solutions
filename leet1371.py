class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        st = 0
        l = 0
        h = {0: -1}
        n = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        for i, c in enumerate(s):
            if c in n:
                st ^= (1 << n[c])
            if st in h:
                l = max(l, i - h[st])
            else:
                h[st] = i

        return l