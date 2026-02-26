class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        lp = [-1]*len(nums)
        arr = [1]*len(nums)
        out_i = 0; out_m = 1
        for i in range(1, len(nums)):
            idx, m = -1, 1
            for x in range(i):
                if nums[i]%nums[x]==0 and m<1+arr[x]:
                    m = 1+arr[x]; idx = x
            if out_m < m:
                out_m = m; out_i = i
            arr[i] = m; lp[i] = idx
        path = []
        while out_i != -1:
            path.append(nums[out_i])
            out_i = lp[out_i]
        path.reverse()
        return path