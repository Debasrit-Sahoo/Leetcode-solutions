class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s = set(stones)
        end = stones[-1]
        @lru_cache(None)
        def dfs(stone, jump):
            if stone == end: return True
            if jump-1 > 0 and stone+(jump-1) in s:
                if dfs(stone+(jump-1), jump-1): return True
            if stone + jump <= end and stone+(jump) in s:
                if dfs(stone+(jump), jump): return True
            if stone + jump < end and stone+(jump+1) in s:
                if dfs(stone+(jump+1), jump+1): return True
            return False
        if 1 not in s: return False
        return dfs(1, 1)
