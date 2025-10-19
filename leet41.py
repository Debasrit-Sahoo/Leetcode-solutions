def firstMissingPositive(nums):
        l = len(nums)
        for i in range(l):
            while True:
                cur = nums[i]
                if cur < 1 or cur > l:
                    break
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    break
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1