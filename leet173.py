from functools import lru_cache
class Solution:
    def calculateMinimumHP(self, dungeon):
        h, w = len(dungeon), len(dungeon[0])
        @lru_cache(None)
        def dfs(x, y):
            if x + 1 == w and y + 1 == h:
                return max(1, 1 - dungeon[y][x])
            a = b = float("inf")
            if x+1 < w: a = dfs(x+1,y)
            if y+1 < h: b = dfs(x,y+1)
            return max(1, min(a,b) - dungeon[y][x])
        return dfs(0, 0)