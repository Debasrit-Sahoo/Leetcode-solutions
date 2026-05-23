class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        for i in range(m):
            p = n
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] != '.': continue
                p = min(p, j - 1)
                while p >= 0 and boxGrid[i][p] != '*':
                    if boxGrid[i][p] == '#': boxGrid[i][j], boxGrid[i][p] = boxGrid[i][p], boxGrid[i][j]; break
                    p-=1

        boxGrid[:] = [list(row)[::-1] for row in zip(*boxGrid)]

        return boxGrid
