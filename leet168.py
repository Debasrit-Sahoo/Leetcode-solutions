class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        while columnNumber > 0:
            columnNumber -= 1
            out.append(chr(columnNumber%26 + 65))
            columnNumber //= 26
        return "".join(out[::-1])