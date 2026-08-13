class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        mis, ext = [0] * (n + 1), [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            ext[i] = ext[i+1] + (1 if ext[i+1] < m and word1[i] == word2[m - 1 - ext[i+1]] else 0)

            mis[i] = (mis[i+1] + 1) if mis[i+1] < m and word1[i] == word2[m - 1 - mis[i+1]] else max(ext[i+1] + 1, mis[i+1])

        used = 0
        j = 0
        ans = []

        for i in range(n):
            rem = m - j - 1
            match = word1[i] == word2[j]
            if used:
                good = match and ext[i + 1] >= rem
            else:
                if match:
                    good = mis[i + 1] >= rem
                else:
                    good = ext[i + 1] >= rem

            if good:
                ans.append(i)
                j+=1
                if not match: used = 1

            if j == m: break

        return ans if j == m else []