class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0

        if cost1 + cost2 >= costBoth:
            n = (need1 if need1 < need2 else need2)
            ans += costBoth * n
            need1 -= n
            need2 -= n

        if need1 and cost1 > costBoth:
            ans += costBoth * need1
            need2 -= need1
        elif need1:
            ans += cost1 * need1

        if need2 < 1: return ans

        ans += (costBoth if costBoth < cost2 else cost2) * need2 

        return ans