class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s = stoneValue
        s.append(0)
        s.append(0)
        a = b = c = 0
        for i in range(len(s) - 3, -1, -1):
            a, b, c = max(s[i] - a, s[i] + s[i+1] - b,  s[i] + s[i+1] + s[i+2] - c), a, b

        if a > 0:
            return "Alice"
        if not a:
            return "Tie"
        return "Bob"