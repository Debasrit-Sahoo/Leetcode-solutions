class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        r, l = sum(nums), max(nums)
        cand = 0
        while l<r:
            cand = (l+r)//2
            cuts = 0
            asum = 0
            for v in nums:
                if asum + v > cand:
                    asum = 0
                    cuts+=1
                asum+=v
            if cuts+1 <= k:
                r = cand
            else:
                l = cand+1
        return l