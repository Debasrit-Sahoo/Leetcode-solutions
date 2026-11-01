class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        r, c = len(grid), len(grid[0])
        quals = []
        q = deque([(0, grid[start[0]][start[1]], start[0], start[1])])
        grid[start[0]][start[1]] = 0

        while q:
            for _ in range(len(q)):
                t = q.popleft()

                if pricing[0] <= t[1] <= pricing[1]:
                    quals.append(t)

                cost, price, rx, cx = t

                if rx + 1 < r and grid[rx + 1][cx]: q.append((cost + 1, grid[rx + 1][cx], rx + 1, cx)); grid[rx + 1][cx] = 0
                if rx - 1 >= 0 and grid[rx - 1][cx]: q.append((cost + 1, grid[rx - 1][cx], rx - 1, cx)); grid[rx - 1][cx] = 0
                if cx + 1 < c and grid[rx][cx + 1]: q.append((cost + 1, grid[rx][cx + 1], rx, cx + 1)); grid[rx][cx + 1] = 0
                if cx - 1 >= 0 and grid[rx][cx - 1]: q.append((cost + 1, grid[rx][cx - 1], rx, cx - 1)); grid[rx][cx - 1] = 0
            if len(quals) >= k: break
        quals.sort()
        return [[quals[i][2], quals[i][3]] for i in range(min(k, len(quals)))]