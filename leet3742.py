class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])

        if k >= r + c - 1:
            dp = [[-1]*c for _ in range(r)]
            dp[0][0] = grid[0][0]
            for i in range(1, c):dp[0][i] = grid[0][i] + dp[0][i-1]
            for i in range(1, r):dp[i][0] = grid[i][0] + dp[i-1][0]
            for i in range(1, r):
                for j in range(1, c):
                    dp[i][j] = grid[i][j] + (dp[i-1][j] if dp[i-1][j] > dp[i][j-1]else dp[i][j-1])
            return dp[-1][-1]

        dp = [[[-1]*(k+1) for _ in range(c)] for _ in range(r)]
        cost = score = 0
        for i in range(c):
            s = grid[0][i]
            cost += bool(s)
            score += s
            if cost > k: break
            dp[0][i][cost] = score
        cost = bool(grid[0][0])
        score = grid[0][0]
        for i in range(1, r):
            s = grid[i][0]
            cost += bool(s)
            score += s
            if cost > k: break
            dp[i][0][cost] = score

        for i in range(1,r):
            for j in range(1,c):
                grid_val = grid[i][j]
                grid_cost = bool(grid_val)
                for cost in range(k+1):
                    a = dp[i-1][j][cost] if dp[i-1][j][cost] > dp[i][j-1][cost] else dp[i][j-1][cost]
                    if a == -1: continue
                    cost+=grid_cost
                    if cost > k: break
                    dp[i][j][cost] = grid_val + a
            
        return max(dp[-1][-1])
