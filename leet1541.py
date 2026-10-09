class Solution:
    def minInsertions(self, s: str) -> int:
        cur = 0
        ans = 0
        for char in s:
            if char == '(':
                if cur < 0:
                    ans += (-cur >> 1) + (2 if cur & 1 else 0)
                    cur = 0
                elif cur & 1:
                    ans += 1
                    cur -= 1
                cur += 2
            else:
                cur -= 1
        if cur < 0: ans += (-cur >> 1) + (2 if cur & 1 else 0)
        else:
            if cur & 1:
                ans += 1
                cur -= 1
            ans += cur
        return ans