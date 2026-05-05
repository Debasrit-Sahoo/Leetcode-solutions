class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return 0
        n = len(grid)

        bfs_q = deque()
        patch = set()

        for x in range(n):
            for y in range(n):
                if grid[x][y]:
                    grid[x][y] = 1
                    patch.add((x,y))
                    if x+1 < n: bfs_q.append((x+1, y))
                    if x-1 >= 0: bfs_q.append((x-1, y))
                    if y+1 < n: bfs_q.append((x, y+1))
                    if y-1 >= 0: bfs_q.append((x, y-1))
        
        d = 0
        while (bfs_q):
            d += 1
            for _ in range(len(bfs_q)):
                x, y = bfs_q.popleft()
                if not grid[x][y]:
                    grid[x][y] = d
                    if x+1 < n: bfs_q.append((x+1, y))
                    if x-1 >= 0: bfs_q.append((x-1, y))
                    if y+1 < n: bfs_q.append((x, y+1))
                    if y-1 >= 0: bfs_q.append((x, y-1))

        for x, y in patch: grid[x][y] = 0

        def is_connected(min_safety_level):
            bfs_q.append((0,0))
            v = set()
            while bfs_q:
                x, y = bfs_q.popleft()
                if grid[x][y] < min_safety_level or (x,y) in v: continue
                if (x == y == n-1):bfs_q.clear(); return 1
                v.add((x, y))
                if x+1 < n: bfs_q.append((x+1, y))
                if x-1 >= 0: bfs_q.append((x-1, y))
                if y+1 < n: bfs_q.append((x, y+1))
                if y-1 >= 0: bfs_q.append((x, y-1))
            return 0
        
        l,h = 0, d
        mid  = 0

        while l <= h:
            mid = (l + h) // 2
            if is_connected(mid):
                l = mid + 1
            else:
                h = mid - 1
        
        return l-1