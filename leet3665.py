class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        r, c = len(grid), len(grid[0])

        prev = [[0,0] for _ in range(c)]
        prev[0][0] = 1
        prev[0][1] = 1
        for cx in range(1, c):
            prev[cx][1] = 1
            if grid[0][cx]: break

        for rx in range(1, r):
            new = [[0,0] for _ in range(c)]
            if grid[rx - 1][0] == 0:
                new[0][0] = prev[0][0]

            for cx in range(1, c):
                new[cx][0] = (prev[cx][1] + (0 if grid[rx - 1][cx] else prev[cx][0])) % MOD
                new[cx][1] = (new[cx - 1][0] + (0 if grid[rx][cx - 1] else new[cx - 1][1])) % MOD

            prev = new

        return (prev[-1][0] + prev[-1][1]) % MOD