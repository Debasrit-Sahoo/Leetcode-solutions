class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return 0
        n = len(grid)
        q = deque([(x, y) for x in range(n) for y in range(n) if grid[x][y]])

        while q:
            x, y = q.popleft()
            c = grid[x][y] + 1
            if x + 1 < n and not grid[x+1][y]: grid[x+1][y] = c; q.append((x+1, y))
            if x - 1 >= 0 and not grid[x-1][y]: grid[x-1][y] = c; q.append((x-1, y))
            if y + 1 < n and not grid[x][y+1]: grid[x][y+1] = c; q.append((x, y+1))
            if y - 1 >= 0 and not grid[x][y-1]: grid[x][y-1] = c; q.append((x, y-1))

        h = [(-grid[0][0], 0, 0)]
        push = heapq.heappush 
        pop = heapq.heappop

        while h:
            v, x, y = pop(h)
            if x == y == n - 1: return -v - 1
            if x + 1 < n and grid[x+1][y] > 0: grid[x+1][y] *= -1; push(h, (max(v, grid[x+1][y]), x+1, y))
            if x - 1 >= 0 and grid[x-1][y] > 0: grid[x-1][y] *= -1; push(h, (max(v, grid[x-1][y]), x-1, y))
            if y + 1 < n and grid[x][y+1] > 0: grid[x][y+1] *= -1; push(h, (max(v, grid[x][y+1]), x, y+1))
            if y - 1 >= 0 and grid[x][y-1] > 0: grid[x][y-1] *= -1; push(h, (max(v, grid[x][y-1]), x, y-1))
