def exist(board,word):
        if len(word) > len(board) * len(board[0]):
            return False
        def sol(i, j, p):
            if p == len(word):
                return True
            need = word[p]
            temp , board[i][j] = board[i][j], "#"
            if i-1 >= 0 and need == board[i-1][j] and sol(i-1, j, p+1):
                    board[i][j] = temp
                    return True
            if i+1 < len(board) and need == board[i+1][j] and sol(i+1, j, p+1):
                    board[i][j] = temp
                    return True
            if j-1 >= 0 and need == board[i][j-1] and sol(i, j-1, p+1):
                    board[i][j] = temp
                    return True
            if j+1 < len(board[0]) and need == board[i][j+1] and sol(i, j+1, p+1):
                    board[i][j] = temp
                    return True
            board[i][j] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and sol(i, j, 1):
                    return True
        return False