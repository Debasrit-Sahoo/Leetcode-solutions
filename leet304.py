class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.sum_arr = [[0]*(c+1) for _ in range(r+1)]
        for y in range(1, r+1):
            for x in range(1, c+1):
                self.sum_arr[y][x] = self.sum_arr[y-1][x] + self.sum_arr[y][x-1] - self.sum_arr[y-1][x-1] + matrix[y-1][x-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1; row2 += 1; col1 += 1; col2 += 1
        return self.sum_arr[row2][col2] - self.sum_arr[row2][col1 - 1] - self.sum_arr[row1 - 1][col2] + self.sum_arr[row1 - 1][col1 - 1]