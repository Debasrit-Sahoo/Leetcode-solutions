def subsetsWithDup(nums):
        nums.sort()
        save = []
        def backtrack(s,p):
            save.append(s[:])
            if len(s) == len(nums):
                return
            else:
                for x in range(p, len(nums)):
                    if x > p and nums[x] == nums[x-1]:
                        continue
                    s.append(nums[x])
                    backtrack(s,x+1)
                    s.pop()
        backtrack([], 0)
        return save