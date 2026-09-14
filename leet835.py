class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        s = -(n-1)

        ans = 0

        for dx in range(s, n):
            for dy in range(s, n):

                tmp = sum(1 for x in range(n) for y in range(n) if 0 <= x+dx < n and 0 <= y+dy < n and img1[x][y] and img2[x+dx][y+dy])
                if tmp > ans: ans = tmp

        return ans