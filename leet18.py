def fourSum(nums, target):
        nums.sort()
        length = len(nums)
        i = 0
        lst = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            new_target = target - nums[i]
            j = i + 1
            while j < length:
                if j > i + 1 and nums[j-1] == nums[j]:
                    j += 1 
                    continue
                newer_target = new_target - nums[j]
                k, l = j + 1, length - 1
                while k < l:
                    current = nums[k] + nums[l]
                    if current == newer_target:
                        lst.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif current > newer_target:
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    else:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                j += 1
        return lst