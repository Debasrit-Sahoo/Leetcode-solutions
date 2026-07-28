class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        off = ord('a')

        for c in s:
            cnt[ord(c) - off]+=1
        
        p = [chr(off + i) * (cnt[i] >> 1) for i in range(len(cnt))]
        p = "".join(p)

        m = ''
        if len(s) & 1: 
            for i, c in enumerate(cnt):
                if c & 1:
                    m = chr(off + i)
                    break
        return p + m + p[::-1]