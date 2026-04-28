class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        o = obstacles
        n = len(o)
        dp = [0]*n
        b = bisect.bisect_right
        t = []
        for i in range(n):
            c = o[i]
            x = b(t, c)
            if len(t) == x:
                t.append(c)
            else:
                t[x] = c
            dp[i] = 1 + x
        return dp