class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = [0] * (26)
        off = ord('a')
        need = 0
        for i, v in enumerate(s):
            idx = ord(v) - off
            last[idx] = i
            need |= 1 << idx
        
        stack = [chr(0)]

        for i, v in enumerate(s):
            if not ((need >> (ord(v) - off)) & 1): continue
            while stack and v < stack[-1] and i < last[ord(stack[-1]) - off]:
                need |= 1 << (ord(stack[-1]) - off)
                stack.pop()
            stack.append(v)
            need &= ~(1 << (ord(v) - off))

        return "".join(stack)[1:]