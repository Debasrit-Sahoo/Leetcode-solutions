def removeElement(nums, val):
    i = len(nums) - 1
    while i >= 0 and nums[i] == val:
        i -= 1
    j = 0
    while j <= i:
        if nums[j] == val:
            nums[j] = nums[i]
            i -= 1
            while nums[i] == val:
                i -= 1
        j += 1
    return j