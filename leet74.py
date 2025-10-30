import bisect
def searchMatrix(matrix, target):
        lo, hi = 0, len(matrix) 
        while lo<hi:
            mid = (lo+hi)// 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid
        if lo-1 < 0:
            return False
        idx = bisect.bisect_left(matrix[lo-1], target)
        if idx < len(matrix[0]) and matrix[lo-1][idx] == target:
            return True
        return False