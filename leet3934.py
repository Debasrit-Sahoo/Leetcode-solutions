class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        base = 911
        MOD = 10**9 + 7

        n = len(nums)
        bps = [1] * n
        for i in range(1, n): bps[i] = (base * bps[i - 1]) % MOD

        def is_unique(size):
            #COLLISIONS ARE NOT HANDLED
            hmap = defaultdict(int)
            h = sum(nums[i]*bps[size - i - 1] for i in range(size)) % MOD
            hmap[h] = 1
            p = bps[size - 1]
            for i in range(size, n):
                h = ((h - nums[i - size] * p) * base + nums[i]) % MOD
                hmap[h] += 1

            return any(each == 1 for each in hmap.values())

        l, r = 1, n

        while l < r:
            mid = (l + r) // 2

            if is_unique(mid):
                r = mid
            else:
                l = mid + 1

        return l