class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        d = [0]*10
        for i in range(len(guess)):
            if secret[i] == guess[i]: b += 1
            else: d[ord(secret[i]) - 48] += 1
        a = 0
        for i in range(len(guess)):
            t = ord(guess[i])-48
            if secret[i] != guess[i] and d[t] > 0:
                a += 1; d[t] -= 1
        return f"{b}A{a}B"