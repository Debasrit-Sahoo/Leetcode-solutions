class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        ans = 1
        cnt = 0
        inc = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if inc == 1:
                    cnt += 1
                else:
                    cnt = 2
                    inc = 1
            elif nums[i] < nums[i - 1]:
                if inc == 0:
                    cnt += 1
                else:
                    cnt = 2
                    inc = 0
            else:
                inc = -1
                cnt = 1
            
            if ans < cnt: ans = cnt

        return ans