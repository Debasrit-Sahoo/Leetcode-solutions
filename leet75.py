def sortColors(nums):
        i,j,k = 0, 0, len(nums) - 1
        x = 0
        while x<len(nums):
            if nums[x] == 2 and x < k:
                nums[x], nums[k] = nums[k], nums[x]
                k -= 1
            elif nums[x] == 1 and x > j:
                nums[x], nums[j] = nums[j], nums[x]
                j += 1
            elif nums[x] == 0 and x > i:
                nums[x], nums[i] = nums[i], nums[x]
                i += 1
                if j <= i:
                    j = i + 1
            else:
                x += 1
        return nums