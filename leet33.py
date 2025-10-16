def search(nums, target):
    def lowest(nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[hi] > nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
    pivot = lowest(nums)
    out = -1
    lo, hi = 0, len(nums) - 1
    while hi >= lo:
        mid = (lo + hi) // 2
        real = (mid + pivot) % len(nums)
        if nums[real] == target:
            out = real
            break
        if nums[real] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return out