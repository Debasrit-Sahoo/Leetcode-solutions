class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        ans = ['0']
        for a in str(n):
            if a == '0': continue
            x += int(a)
            ans.append(a)
        return int("".join(ans)) * x