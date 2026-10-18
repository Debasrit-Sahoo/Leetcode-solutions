class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        root = [nums[0], None, None]
        for i in range(1, len(nums)):
            each = nums[i]
            node = [each, None, None]

            cur = root
            while cur[0]:
                if cur[0] > each:
                    if not cur[1]: cur[1] = node; break
                    else: cur = cur[1]
                else:
                    if not cur[2]: cur[2] = node; break
                    else: cur = cur[2]

        def fx(root):
            if not root: return (0, 1)
            ls, lw = fx(root[1])
            rs, rw = fx(root[2])
            return (ls + rs + 1, (lw * rw) % MOD * math.comb(ls + rs, ls) % MOD)

        return (fx(root)[1] - 1) % MOD