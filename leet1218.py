class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        out = 1
        get = dp.get
        d = difference
        for v in arr:
            dp[v] = n = 1 + get(v-d, 0)
            if n > out:
                out = n
        return out