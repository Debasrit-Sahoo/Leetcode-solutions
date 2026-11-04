class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        a, b, c, d = heapq.heappush_max, heapq.heappop_max, heapq.heappush, heapq.heappop
        mx = [nums[0], 1, [(nums[0],0)]]
        mn = [0, 0, []]
        n = len(nums)
        in_mx = [False] * n
        in_mx[0] = True
        def mxpush(idx):
            a(mx[2], (nums[idx], idx))
            mx[1] += 1
            mx[0] += nums[idx]
            in_mx[idx] = True
        def mxpop():
            ret = b(mx[2])
            mx[1] -= 1
            mx[0] -= ret[0]
            return ret[1]
        def mnpush(idx):
            c(mn[2], (nums[idx], idx))
            mn[1] += 1
            mn[0] += nums[idx]
            in_mx[idx] = False
        def mnpop():
            ret = d(mn[2])
            mn[1] -= 1
            mn[0] -= ret[0]
            return ret[1]
        
        lazydel = [False] * n
        costs = [0] * (n - x + 1)

        for i in range(1, x):
            if mx[2][0][0] <= nums[i]:
                mnpush(i)
            else:
                mxpush(i)
            if mx[1] < mn[1]:
                mxpush(mnpop())

            elif mn[1] + 1 < mx[1]:
                mnpush(mxpop())

        costs[0] = mn[0] - mx[0] + (mx[1] - mn[1]) * mx[2][0][0]

        for i in range(x, n):
            lazydel[i-x] = True
            if in_mx[i - x]:
                mx[0] -= nums[i - x]
                mx[1] -= 1
            else:
                mn[0] -= nums[i - x]
                mn[1] -= 1

            while mx[2] and lazydel[mx[2][0][1]]: b(mx[2])
            while mn[2] and lazydel[mn[2][0][1]]: d(mn[2])

            if not mx[1] or mx[2][0][0] <= nums[i]:
                mnpush(i)
            else:
                mxpush(i)

            if mx[1] < mn[1]:
                mxpush(mnpop())
            elif mn[1] + 1 < mx[1]:
                mnpush(mxpop())

            while mx[2] and lazydel[mx[2][0][1]]: b(mx[2])
            while mn[2] and lazydel[mn[2][0][1]]: d(mn[2])

            costs[i - x + 1] = mn[0] - mx[0] + (mx[1] - mn[1]) * mx[2][0][0]

        MAX = 1 << 50
        dp = deque([[0] + [MAX] * k for _ in range(x)])

        for i in range(x, n + 1):
            new = [0] + [MAX] * k
            for j in range(1, k + 1):
                new[j] = min(dp[-1][j], dp[0][j-1] + costs[i-x])
            dp.popleft()
            dp.append(new)

        return dp[-1][-1]