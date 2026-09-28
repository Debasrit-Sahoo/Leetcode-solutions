class Solution:
    def maxDepth(self, s: str) -> int:
        a = 0
        ans = 0
        for c in s:
            match c:
                case '(':
                    a += 1
                    if a > ans:
                        ans = a
                case ')':
                    a -= 1
        return ans