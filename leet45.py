def jump(nums):
        target = len(nums) - 1
        m = float("inf")
        def dfs(p, jc,):
            nonlocal m
            if p == target and jc < m:
                m = jc
                return
            else:
                for i in range(1, nums[p]+1):
                    if p + i > target:
                        break
                    dfs(p + i, jc + 1)
        dfs(0, 0)
        return m