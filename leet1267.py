class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = sum(sum(r) for r in grid)

        for rx in range(r):
            for rc in range(c):
                
                if grid[rx][rc]:

                    cnt = -1
                    for i in range(r):
                        if grid[i][rc]: cnt += 1

                    if cnt: break

                    cnt = -1
                    for i in range(c):
                        if grid[rx][i]: cnt += 1
                    if cnt: break

                    ans -= 1

        return ans