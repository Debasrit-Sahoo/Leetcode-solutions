import bisect
def searchRange(nums, target):
    lst = [bisect.bisect_left(nums,target),bisect.bisect_right(nums,target)]
    if lst[0] == lst[1]:
        return [-1,-1]
    lst[1] = lst[1] - 1
    return lst