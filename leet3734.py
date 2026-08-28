class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        if len(s) == 1: return s if s > target else ""
        sf = [0] * 26
        off = ord('a')

        for each in s: sf[ord(each) - off] += 1
        c = 0
        mid = ""
        for i, each in enumerate(sf):
            if each & 1:
                sf[i] = each - 1
                c+=1
                mid = chr(i + off)
                if c == 2: return ""
        
        tf = [0] * 26
        n = (len(target) >> 1)
        t = target[:n]

        for each in t: tf[ord(each) - off] += 2

        delta = sum(max(0, tf[i] - sf[i]) for i in range(26)) // 2

        a = t + mid + t[::-1]
        if a > target and not delta:
            return a

        for p, c in enumerate(reversed(t)):
            idx = ord(c) - off
            if tf[idx] > sf[idx]:
                delta -= 1
            tf[idx] -= 2

            if not delta:
                for char_idx in range(ord(c) - off + 1, 26):
                    if sf[char_idx] > tf[char_idx]:
                        sf[char_idx] -= 2
                        left = t[:-p-1] + chr(char_idx + off) + "".join(chr(off + i) * ((sf[i] - tf[i])//2) for i in range(26) if sf[i] - tf[i])
                        return left + mid + left[::-1]
                
        return ""