class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        tot = r * c

        k %= tot
        if not k: return grid

        if k % c:
            g = gcd(tot, k)
            b = tot // g
            for i in range(g):
                x, y = divmod(i, c)
                prev = grid[x][y]
                idx = k + i
                for _ in range(b):
                    x, y = divmod(idx, c)
                    prev, grid[x][y] = grid[x][y], prev
                    idx = (idx + k) % tot
        else:
            k //= c
            g = gcd(r, k)
            b = r // g
            for i in range(g):
                prev = grid[i]
                idx = k + i
                for _ in range(b):
                    prev, grid[idx] = grid[idx], prev
                    idx = (idx + k) % r

        return grid