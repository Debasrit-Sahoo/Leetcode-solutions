class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
        
            for i in range(1, n):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for r in range(n):
                mat[r].reverse()

            if target == mat: return True

        return False
                    