class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        r, c = len(grid), len(grid[0])
        m = r*c
        arr = [val for row in grid for val in row]
        arr.sort()
        mod = arr[0] % x
        if not all(a % x == mod for a in arr):
            return -1
        mid = arr[m//2]
        s = sum(abs(mid - a)//x for a in arr)
        return s

