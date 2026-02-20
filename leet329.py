class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        c, r = len(matrix), len(matrix[0])
        @lru_cache(None)
        def longest_sequence(i, j):
            cur = matrix[i][j]
            m = 0
            for offset in range(-1,2,2):
                ni,nj = i+offset, j
                if 0<=ni<c and 0<=nj<r and matrix[ni][nj] > cur:
                    m = max(m, longest_sequence(ni, nj))
            for offset in range(-1,2,2):
                ni,nj = i, j+offset
                if 0<=ni<c and 0<=nj<r and matrix[ni][nj] > cur:
                    m = max(m, longest_sequence(ni, nj))
            return 1 + m
        m = 0
        for i in range(c):
            for j in range(r):
                m = max(m , longest_sequence(i, j))
        return m