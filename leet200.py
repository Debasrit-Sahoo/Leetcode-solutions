from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mx, my = len(grid[0]), len(grid)
        def marker(x,y):
            if not 0 <= x < mx or not 0 <= y < my or grid[y][x] != "1":
                return
            grid[y][x] = "#"
            marker(x,y+1)
            marker(x,y-1)
            marker(x-1,y)
            marker(x+1,y)
        islands = 0
        for i in range(my):
            for j in range(mx):
                if grid[i][j] == "1":
                    islands += 1
                    marker(j,i)
        return islands