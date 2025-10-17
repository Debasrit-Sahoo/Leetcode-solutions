def isValidSudoku(board):
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                box_index = ((i//3)*3)+(j//3)
                if cur in rows[i] or cur in cols[j] or cur in boxes[box_index]:
                    return False
                rows[i].append(cur)
                cols[j].append(cur)
                boxes[box_index].append(cur)
        return True