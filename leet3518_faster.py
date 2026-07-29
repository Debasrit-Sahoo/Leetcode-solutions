import math
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        off = ord('a')

        for c in s:
            cnt[ord(c) - off]+=1

        mid = ""
        rem = 0

        for i, c in enumerate(cnt):
            if not mid and c & 1: mid = chr(off + i)
            cnt[i] >>= 1
            rem += cnt[i]

        p = []

        cur = 1
        slots = rem

        for f in cnt:
            if not f: continue

            cur *= math.comb(slots, f)
            slots -= f

            if cur < k: return ""

        for _ in range(len(s) >> 1):
            for ch in range(26):
                if not cnt[ch]: continue

                child = cur * cnt[ch] // rem

                if child < k: k-=child
                else:
                    p.append(chr(off + ch))
                    cnt[ch] -= 1
                    rem -= 1
                    cur = child
                    break

        p = "".join(p)
        return p + mid + p[::-1]