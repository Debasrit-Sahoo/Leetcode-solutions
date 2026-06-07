class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0,0,k)])
        r, c = len(grid), len(grid[0])
        if r == c == 1: return 0
        if k >= r + c - 2: return r + c - 2
        rems = [[-1]*c for _ in range(r)]

        n = 0
        while q:
            for _ in range(len(q)):
                x, y, rem = q.popleft()
                if (x == r-1 and y == c-1): return n
                if grid[x][y]:
                    if not rem: continue
                    rem-=1
                if rems[x][y] >= rem: continue
                rems[x][y] = rem
                if x + 1 < r: q.append((x+1, y, rem))
                if x - 1 >= 0: q.append((x-1, y, rem))
                if y + 1 < c: q.append((x, y+1, rem))
                if y - 1 >= 0: q.append((x, y-1, rem))
            n+=1
        return -1