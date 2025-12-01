class Solution:
    def titleToNumber(self, columnTitle):
        c = 0
        for i in columnTitle:
            c *= 26
            c += ord(i) - 64
        return c