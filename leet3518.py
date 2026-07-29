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
        def count(rem):
            ans = 1
            slots = rem

            for f in cnt:
                if not f: continue

                ans *= math.comb(slots, f)

                if ans >= k: return k

                slots -= f

            return ans

        if count(rem) < k:
            return ""
        
        for _ in range(len(s) >> 1):
            for ch in range(26):
                if not cnt[ch]: continue

                cnt[ch] -= 1

                ways = count(rem - 1)

                if ways < k:
                    k -= ways
                    cnt[ch] += 1
                else:
                    p.append(chr(off + ch))
                    rem -= 1
                    break

        p = "".join(p)
        return p + mid + p[::-1]