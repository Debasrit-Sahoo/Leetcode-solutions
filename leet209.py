class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums) + 1
        i = 0
        s = 0
        for j in range(l-1):
            s += nums[j]
            while s >= target:
                if j-i+1 < l:
                    l = j-i+1
                s -= nums[i]
                i += 1
        return 0 if l > len(nums) else l