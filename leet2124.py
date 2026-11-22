class Solution:
    def checkString(self, s: str) -> bool:
        a, b = s.rfind('a'), s.find('b')
        if a == -1 or b == -1: return True
        return a < b