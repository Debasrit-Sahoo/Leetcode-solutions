class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        f = []
        for c in coins:
            if all(c % x for x in f):
                f.append(c)

        coins = f
        n = len(coins)

        def cnt(lim):
            tot = 0

            for size in range(1, n + 1):
                for s in combinations(coins, size):
                    lcm = 1

                    for c in s:
                        lcm = lcm // gcd(lcm, c) * c

                    if size & 1:
                        tot += lim // lcm
                    else:
                        tot -= lim // lcm

            return tot

        lo, hi = 1, min(coins) * k

        while lo < hi:
            mid = (lo + hi) >> 1

            if cnt(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo