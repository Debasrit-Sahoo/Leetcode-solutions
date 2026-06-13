class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a = ord('a')
        z = ord('z')
        ans = []

        for w in words:
            s = 0
            for c in w:
                s += weights[ord(c) - a]
            
            ans.append(chr(z - s % 26))

        return "".join(ans)
            