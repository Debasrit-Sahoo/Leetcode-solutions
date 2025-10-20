def jump(nums):
    l = len(nums) - 1
    jumps = 0
    bound = 0
    m = 0
    for i in range(l+1):
        if i == l:
            return jumps
        m = max(m, i + nums[i])
        if i == bound:
            bound = m
            jumps += 1