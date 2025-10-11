def threeSumClosest(nums, target):
        nums.sort()
        w = 0
        closest = float("inf")
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                print(nums[i], nums[j], nums[k])
                s = nums[i] + nums[j] + nums[k] 
                if abs(target - s) < closest:
                    print(closest,s)
                    closest = abs(target - s)
                    w = s
                if s > target:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while k > j and nums[j] == nums[j-1]:
                        j += 1
        return w