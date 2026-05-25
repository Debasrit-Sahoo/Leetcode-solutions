class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        layers = min(r, c)//2
        for l in range(layers):
            tot = 2*(r+c-2*l) - 4
            if not tot: continue
            rots = k%tot
            if rots: 
                ext = grid[l][l:c][::-1]
                for x in range(l+1, r-1):
                    ext.append(grid[x][l])
                ext += grid[r-1][l:c]
                for x in range(r-2, l, -1):
                    ext.append(grid[x][c-1])
                print(ext)
                idx = 0
                rots = tot - rots
                rot = [0]*tot
                for i in range(tot):
                    rot[i] = ext[(i + rots) % tot]
                print(rot)
                for y in range(c-1, l-1, -1):
                    grid[l][y] = rot[idx]
                    idx += 1
                for x in range(l+1, r-1):
                    grid[x][l] = rot[idx]
                    idx += 1
                for y in range(l, c):
                    grid[r-1][y] = rot[idx]
                    idx += 1
                for x in range(r-2, l, -1):
                    grid[x][c-1] = rot[idx]
                    idx += 1
            r-=1
            c-=1
        return grid
