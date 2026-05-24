class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        d+=1
        n = len(arr)
        @lru_cache(None)
        def dfs(i):
            val = arr[i]
            mx = 0

            for left in range(i - 1, i - d, -1):
                if left < 0 or arr[left] >= val: break
                t = dfs(left)
                if mx < t: mx = t
            
            for right in range(i + 1, i + d):
                if right >= n or arr[right] >= val: break
                t = dfs(right)
                if mx < t: mx = t

            return mx + 1

        return max(dfs(x) for x in range(n))