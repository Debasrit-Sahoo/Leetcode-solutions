class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = y = z = 0
        n = len(grid)
        for i in grid:
            x += max(i)
        grid = list(zip(*grid))
        for i in grid:
            y += max(i)
        z = n*n
        for i in range(n):
            for j in range(n):
                if not grid[i][j]: z-=1

        return x + y + z