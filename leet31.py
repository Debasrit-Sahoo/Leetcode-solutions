def nextPermutation(nums):
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            temp = len(nums) - 1
            while temp > i:
                if nums[temp] > nums[i]:
                    target = nums[temp]
                    break
                else:
                    temp -= 1
            nums[temp],nums[i] = nums[i], nums[temp]
            nums[i+1:] = reversed(nums[i+1:])
            return nums
    return nums.reverse()