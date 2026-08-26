class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt = i = 0
        l = len(s) + 1
        best = ""
        for j, v in enumerate(s):
            if v == '1': cnt += 1

            while cnt > k or j - i + 1 > l:
                if s[i] == '1': cnt -= 1
                i += 1
            
            while cnt == k and s[i] == '0': i += 1

            if k == cnt: 
                c = s[i:j+1]
                if l > j - i + 1:
                    l = j - i + 1
                    best = c
                elif c < best:
                    best = c
        
        return best