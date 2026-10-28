class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        prev = [None] * c

        prev[0] = {grid[0][0]}
        for cx in range(1, c): prev[cx] = set(x ^ grid[0][cx] for x in prev[cx - 1])

        for rx in range(1, r):
            new = [None] * c
            new[0] = set(x ^ grid[rx][0] for x in prev[0])

            for cx in range(1, c):
                g = grid[rx][cx]
                new[cx] = set(x ^ g for x in prev[cx])
                new[cx].update(x ^ g for x in new[cx - 1])

            prev = new

        return min(prev[-1])