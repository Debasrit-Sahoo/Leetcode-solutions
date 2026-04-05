class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        t = s = 0
        for i in range(n):
            nt = count[nums[i]]*nums[i] + (s if abs(nums[i-1] - nums[i]) == 1 else max(t, s))
            ns = max(t,s)
            t, s = nt, ns
        return max(t,s)