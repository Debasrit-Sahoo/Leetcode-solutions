def singleNumber(nums):
        nums.sort()
        for x in range(0, len(nums)-2, 3):
            if not nums[x] == nums[x+1] == nums[x+2]:
                if nums[x+1] == nums[x+2]:
                    return nums[x]
                if nums[x] == nums[x+1]:
                    return nums[x+2]
                return nums[x+1]
        return nums[-1]