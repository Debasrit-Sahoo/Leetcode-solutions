def permute(nums):
        res = []
        n = len(nums)
        used = [False] * n
        def boo(s):
            if len(s) == n:
                res.append(s[:])
                return
            for x in range(n):
                if not used[x]:
                    used[x] = True
                    s.append(nums[x])
                    boo(s)
                    s.pop()
                    used[x] = False
        boo([])
        return res