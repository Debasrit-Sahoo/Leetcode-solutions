class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0

        for dx in range(r):
            for dy in range(c):
                if grid[dx][dy] == 0 or grid[dx][dy] == -1: continue

                csum = grid[dx][dy]
                stack = [(dx, dy)]
                grid[dx][dy] = -1

                while stack:
                    x, y = stack.pop()

                    if x + 1 < r and (grid[x + 1][y] != 0 and grid[x + 1][y] != -1): csum += grid[x + 1][y]; grid[x + 1][y] = -1; stack.append((x + 1, y))
                    if x - 1 >= 0 and (grid[x - 1][y] != 0 and grid[x - 1][y]  != -1): csum += grid[x - 1][y]; grid[x - 1][y] = -1; stack.append((x - 1, y))
                    if y + 1 < c and (grid[x][y + 1] != 0 and grid[x][y + 1] != -1): csum += grid[x][y + 1]; grid[x][y + 1] = -1; stack.append((x, y + 1))
                    if y - 1 >= 0 and (grid[x][y - 1] != 0 and grid[x][y - 1] != -1): csum += grid[x][y - 1]; grid[x][y - 1] = -1; stack.append((x, y - 1))

                if csum % k == 0:
                    ans += 1

        return ans