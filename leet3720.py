class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        sf = [0] * 26
        tf = [0] * 26
        off = ord("a")

        for each in s: sf[ord(each) - off] += 1
        for each in target: tf[ord(each) - off] += 1

        def can_make():
            for i, v in enumerate(tf):
                if v and sf[i] < v: return False
            return True

        for p, c in enumerate(reversed(target)):
            tf[ord(c) - off] -= 1
            if can_make():
                for char_idx in range(ord(c) - off + 1, 26):
                    if sf[char_idx] > tf[char_idx]:
                        sf[char_idx]-=1
                        res = [target[:-p-1], chr(char_idx + off)]
                        for i in range(26):
                            res.append(chr(i + off) * (sf[i] - tf[i]))
                        return "".join(res)
                    
        return ""