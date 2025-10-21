def permuteUnique(nums):
        res = []
        nums.sort()
        l = len(nums) 
        seen = [False]*l
        def back(s):
            if len(s) == l:
                res.append(s[:])
                return
            for i in range(l):
                if i > 0 and nums[i] == nums[i-1] and seen[i-1]:
                    continue
                if not seen[i]:
                    seen[i] = True
                    s.append(nums[i])
                    back(s)
                    s.pop()
                    seen[i] = False
        back([])
        return res
    
