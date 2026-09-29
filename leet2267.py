class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid[0]) - 1, len(grid) - 1

        if grid[-1][-1] == '(' or grid[0][0] == ')' or (m + n + 1) & 1: return False

        @cache
        def trav(s: int, r: int, c: int):
            s += 1 if grid[r][c] == '(' else -1

            if s < 0: return False
            if r == n and c == m and s == 0:
                return True

            if r + 1 <= n and trav(s, r + 1, c): return True
            if c + 1 <= m and trav(s, r, c + 1): return True

            return False

        return trav(0, 0, 0)