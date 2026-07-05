from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        board[0] = '0' + board[0][1:]
        MOD = 10**9 + 7

        dp = [[-1, 0] for i in range(n-1)]
        dp.append([0, 1])
        for i in range(n-2, -1, -1):
            if board[-1][i] == 'X': break
            dp[i] = (dp[i+1][0] + int(board[-1][i]), 1)

        edge_r_unreach = 0
        for x in range(n-2, -1, -1):
            diag = dp[-1]
            if board[x][-1] == 'X': edge_r_unreach = 1
            dp[-1] = [-1, 0] if edge_r_unreach else [dp[-1][0] + int(board[x][-1]), 1]
            for y in range(n-2, -1, -1):
                if board[x][y] == 'X': nxt = [-1, 0]
                else:
                    mx = max(dp[y][0], dp[y+1][0], diag[0])
                    nxt = [-1, 0] if mx == -1 else [mx + int(board[x][y]), ((dp[y][1] if dp[y][0] == mx else 0) + (dp[y+1][1] if dp[y+1][0] == mx else 0) + (diag[1] if diag[0] == mx else 0)) % MOD]
                dp[y], diag = nxt, dp[y]

        return dp[0] if dp[0][0] != -1 else [0, 0]

print(Solution().pathsWithMaxScore(["E11","XXX","11S"]))