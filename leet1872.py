class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        dp = k = sum(stones)
        k -= stones[-1]
        for i in range(len(stones) - 2, 0, -1):
            if k > dp << 1: dp = k - dp
            k -= stones[i]

        return dp