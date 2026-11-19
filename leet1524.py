class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        e = o = ans = 0
        for each in arr:
            if each & 1:
                o, e = 1 + e, o
            else:
                e += 1
            ans += o
        return ans % MOD
        