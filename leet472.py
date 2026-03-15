class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        lo = len(words[0])
        out = []

        word_set = set(words)

        for n in range(len(words) - 1, -1, -1):
            w = words[n]
            word_set.remove(w)
            hi = len(w) + 1

            dp = [False]*hi
            dp[0] = True

            for i in range(hi - 1):
                if dp[i]:
                    for le in range(lo, hi):
                        if i + le > hi - 1: break
                        if w[i:i+le] in word_set:
                            dp[i+le] = True

            word_set.add(w)
            if dp[-1]: out.append(w)

        return out