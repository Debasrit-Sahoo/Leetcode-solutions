class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        m = r*c
        def e(x, y, edir):
            cn = 0
            while not (x == r-1 and y == c-1) and 0 <= x < r and 0 <= y < c and edir in street_valid_dirs[grid[x][y]] and cn < m:
                cn +=1
                s = grid[x][y]
                d = street_valid_dirs[s]
                d = d[0] if d[1] == edir else d[1]
                if d == 1: y-=1
                elif d == 2: y+=1
                elif d == 3: x-=1
                else: x+=1
                edir = flip[d]
            return True if (x == r-1 and y == c-1 and edir in street_valid_dirs[grid[x][y]]) else False    
        if r == c == 1: return True
        street_valid_dirs = [0, (1,2), (3,4), (1,4), (2,4), (1,3), (2,3)]
        flip = [0, 2, 1, 4, 3]
        s = grid[0][0]
        if s == 5: return False
        if s == 1 or s == 6: return e(0, 1, 1)
        if s == 2 or s == 3: return e(1, 0, 3)
        else:
            return e(0, 1, 1) or e(1, 0, 3)