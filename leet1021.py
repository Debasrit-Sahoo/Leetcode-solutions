class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        buf = []
        c = 0

        for char in s:
            if char == '(':
                if c:
                    buf.append(char)
                c += 1
            else:
                if c != 1:
                    buf.append(char)
                c -= 1

        return "".join(buf)