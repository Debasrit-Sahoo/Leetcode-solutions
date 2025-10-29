from functools import lru_cache
def minDistance(word1, word2):
    @lru_cache(None)
    def dp(i,j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if word1[i] == word2[j]:
            return dp(i+1,j+1)
        return min((dp(i,j+1)+1),(dp(i+1,j)+1),(dp(i+1,j+1)+1))
    return dp(0,0)