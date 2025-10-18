def solveSudoku(board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                box_index = ((i//3)*3)+(j//3)
                if cur in rows[i] or cur in cols[j] or cur in boxes[box_index]:
                    continue
                rows[i].add(cur)
                cols[j].add(cur)
                boxes[box_index].add(cur)
        def minfin():
            lowest = 10
            best = None
            for i in range(9):
                for j in range(9):
                    cur = board[i][j]
                    if cur != ".":
                        continue
                    box_index = (i // 3) * 3 + (j // 3)
                    candidates = {str(d) for d in range(1, 10)} - rows[i] - cols[j] - boxes[box_index]

                    if lowest > len(candidates):
                        lowest = len(candidates)
                        best = i, j, box_index, candidates
                    
                    if lowest == 1:
                        return best
            return best
        def dfs():
            cell = minfin()
            if not cell:
                return True
            i, j, box_index , possible = cell
            for p in possible:
                board[i][j] = p
                rows[i].add(p)
                cols[j].add(p)
                boxes[box_index].add(p)
                if dfs():
                    return True
                board[i][j] = "."
                rows[i].remove(p)
                cols[j].remove(p)
                boxes[box_index].remove(p)
            return False