def subsets(nums):
        save = []
        def cascade(lst, p):
            save.append(lst[:])
            if len(lst) == len(nums):
                return
            for x in range(p, len(nums)):
                lst.append(nums[x])
                cascade(lst, x+1)
                lst.pop()
        cascade([],0)
        return save