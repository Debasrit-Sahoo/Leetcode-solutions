class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        r_sums = [0]*rows
        c_sums = list(map(sum, zip(*grid)))
        for i in range(rows):
            r_sums[i] = sum(grid[i])
        p = 0
        for i in range(rows): r_sums[i], p = p, p + r_sums[i]

        for left in r_sums:
            if left<<1 == p: return True
        
        p = 0
        for i in range(cols): c_sums[i], p = p, p + c_sums[i]
        
        for top in c_sums:
            if top<<1 == p: return True
        
        return False