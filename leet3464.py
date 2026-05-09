class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        arr = [0]*n
        per = side<<2
        for i, a in enumerate(points):
            x, y = a
            if not y: arr[i] = x
            elif y == side: arr[i] = 3*side - x
            elif x == side: arr[i] = side + y
            else: arr[i] = per - y

        arr.sort()
        arr = arr + [x + per for x in arr]
        n2 = n<<1

        lo, hi = 0, side<<1
        nxt = [0]*n2
        while lo < hi:
            mid = (lo + hi + 1)//2
            x = 0
            f = 0
            for start in range(n2):
                x = x if start + 1 < x else start + 1
                while x < n2 and arr[x] - arr[start] < mid:
                    x+=1
                nxt[start] = x
            for start in range(n):
                cur = start
                for _ in range(k-1): 
                    cur = nxt[cur]
                    if cur >= start + n: break
                if cur < start + n and arr[start] + per - arr[cur] >= mid:
                    f = 1; break            
            
            if f: lo = mid
            else: hi = mid - 1

        return lo