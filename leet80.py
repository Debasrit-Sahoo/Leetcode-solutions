def removeDuplicates(nums):
        j = 0
        i = 0
        while i < len(nums):
            if j > 1 and nums[j-2] == nums[i]:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
        return j,nums