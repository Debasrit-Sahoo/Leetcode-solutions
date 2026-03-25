class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        dp = [[-1]*m for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j]: continue
                q.append((i, j))
                dp[i][j] = 0

        cost = 0
        while q:
                i, j = q.popleft()
                s = dp[i][j] + 1

                if 0<=i+1<n and dp[i+1][j] == -1: dp[i+1][j] = s;q.append((i+1, j))
                if 0<=i-1<n and dp[i-1][j] == -1: dp[i-1][j] = s;q.append((i-1, j))
                if 0<=j+1<m and dp[i][j+1] == -1: dp[i][j+1] = s;q.append((i, j+1))
                if 0<=j-1<m and dp[i][j-1] == -1: dp[i][j-1] = s;q.append((i, j-1))

        return dp