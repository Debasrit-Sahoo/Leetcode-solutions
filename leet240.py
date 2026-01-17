class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = len(matrix)
        i, j = 0, len(matrix[0])-1
        while i != s and j != -1:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j-= 1
            else: i+= 1
        return False