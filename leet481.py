class Solution:
    def magicalString(self, n: int) -> int:
        arr = [1, 2, 2]
        p = 2
        s = 0
        c = 1
        while (len(arr) < n):
            if not s: c += arr[p]
            for _ in range(arr[p]):
                arr.append(s + 1)
            p += 1
            s ^= 1
        if len(arr) > n and arr.pop() == 1: c-=1
        return c