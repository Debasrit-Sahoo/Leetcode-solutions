class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l = a = 0

        for i, v in enumerate(s):
            freq[v] += 1

            while freq[v] > 2:
                freq[s[l]]-=1
                l += 1

            a = max(a, i - l + 1)

        return a