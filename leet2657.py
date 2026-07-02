class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = 1 + len(a)
        s = [0]*n
        ans = 0
        for i in range(n-1):
            if s[a[i]]: ans += 1
            else: s[a[i]] = 1
            if s[b[i]]: ans += 1
            else: s[b[i]] = 1
            a[i] = ans
        return a