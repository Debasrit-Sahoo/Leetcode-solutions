class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if not s: return 0

        nums = []
        st = s[0]
        cnt = 0
        for c in s:
            if st == c: cnt += 1
            else: nums.append(cnt * (-1 if st == '1' else 1)); cnt = 1; st = c
        nums.append(cnt * (-1 if st == '1' else 1))

        tot = -sum(i for i in nums if i < 0)
        ans = 0

        for i in range(1 + (nums[0] < 0), len(nums) - 1, 2):
            cand = nums[i-1] + nums[i+1]
            if cand > ans: ans = cand
        
        return ans + tot