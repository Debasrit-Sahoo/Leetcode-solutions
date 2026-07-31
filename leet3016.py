class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        off = ord('a')
        for c in word:
            freq[ord(c) - off] += 1
        freq.sort(reverse=True)

        ans = 0

        for i in range(3):
            tmp = 0
            n = i << 3
            for j in range(8):
                tmp += freq[n + j]
            ans += tmp * (i + 1)

        return ans + ((freq[-1] + freq[-2]) << 2)