def longestConsecutive(nums): #nums = [0,3,7,2,5,8,4,6,0,1]
        s = set(nums)
        om = 0
        for i in s:
            if i-1 in s:
                continue
            m = i
            while m in s:
                m += 1
            if m-i > om:
                om = m-i
        return om