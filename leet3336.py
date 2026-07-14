class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        MAX = max(nums) + 1

        cur = [[0] * MAX for _ in range(MAX)]
        cur[0][0] = 1

        for x in nums:
            nxt = [[0] * MAX for _ in range(MAX)]
            for g1 in range(MAX):
                for g2 in range(MAX):
                    c = cur[g1][g2]
                    if not c: continue

                    nxt[g1][g2] = (c + nxt[g1][g2]) % MOD

                    g = gcd(g1, x)
                    nxt[g][g2] = (c + nxt[g][g2]) % MOD
                    g = gcd(g2, x)
                    nxt[g1][g] = (c + nxt[g1][g]) % MOD

            cur = nxt

        ans = 0

        for g in range(1, MAX):
                ans = (ans + cur[g][g]) % MOD

        return ans