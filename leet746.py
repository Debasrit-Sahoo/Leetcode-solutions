class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p, q = cost[0], cost[1]
        for i in range(2, len(cost)):
            p, q = q, cost[i] + min(p, q)
        return min(p, q)