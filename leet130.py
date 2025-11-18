from collections import deque
def solve(board):
    r = len(board)
    c = len(board[0])
    def bfs(x,y):
        cands = [(x,y)]
        is_prot = False
        board[x][y] = "V"
        stack = deque([(x,y)])
        while stack:
            x, y = stack.popleft()
            if not is_prot and (x == 0 or x == r-1 or y == 0 or y == c-1):
                is_prot = True
            if x-1 >= 0:
                if board[x-1][y] == "O":
                    cands.append((x-1,y))
                    board[x-1][y] = "V"
                    stack.append((x-1,y))
            if x+1 < r:
                if board[x+1][y] == "O":
                    cands.append((x+1,y))
                    board[x+1][y] = "V"
                    stack.append((x+1,y))
            if y-1 >= 0:
                if board[x][y-1] == "O":
                    cands.append((x,y-1))
                    board[x][y-1] = "V"
                    stack.append((x,y-1))
            if y+1 < c:
                if board[x][y+1] == "O":
                    cands.append((x,y+1))
                    board[x][y+1] = "V"
                    stack.append((x,y+1))
        if not is_prot:
            for x,y in cands:
                board[x][y] = "X"
        else:
            for x,y in cands:
                board[x][y] = "O"
    for x in range(r):
        for y in range(c):
            if board[x][y] != "X":
                bfs(x,y)
    return board