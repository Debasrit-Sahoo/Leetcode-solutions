class Solution:
    def findRepeatedDnaSequences(self, s):
        sent = set()
        seen = set()
        for i in range(10, len(s)+1):
            c = s[i-10:i]
            if c in seen:
                sent.add(c)
            else:
                seen.add(c)
        return list(sent)