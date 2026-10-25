class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])

        ans = 0

        for nx in range(r):
            for ny in range(c):
                if grid[nx][ny] == 1 or grid[nx][ny] == 2: continue
                invalid = False
                q = [(nx, ny)]
                grid[nx][ny] = 2

                while q:
                    x, y = q.pop()
                    if x == 0 or x == r - 1 or y == 0 or y == c - 1: invalid = True

                    if x + 1 < r and grid[x + 1][y] == 0: q.append((x + 1, y)); grid[x + 1][y] = 2
                    if x - 1 >= 0 and grid[x - 1][y] == 0: q.append((x - 1, y)); grid[x - 1][y] = 2
                    if y + 1 < c and grid[x][y + 1] == 0: q.append((x, y + 1)); grid[x][y + 1] = 2
                    if y - 1 >= 0 and grid[x][y - 1] == 0: q.append((x, y - 1)); grid[x][y - 1] = 2

                if not invalid: ans += 1
        return ans