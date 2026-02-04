class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        c, r = len(board), len(board[0])
        for y in range(c):
            for x in range(r):
                count = 0
                for i in range(y-1, y+2):
                    for j in range(x-1, x+2):
                        if (not((0 <= i < c) and (0 <= j < r))) or (i == y and j == x): continue
                        if board[i][j] % 2 == 1: count += 1
                if (board[y][x] == 1) and (count < 2 or count > 3): board[y][x] = 3
                elif board[y][x] == 0 and count == 3: board[y][x] = 2
        for y in range(c):
            for x in range(r):
                if board[y][x] == 3: board[y][x] = 0
                elif board[y][x] == 2: board[y][x] = 1