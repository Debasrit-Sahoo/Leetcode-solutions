class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums) : return max(nums)
        if k == 1:
            for a, b in sorted((Counter(nums)).items(), reverse=True):
                if b == 1:
                    return a
            return -1
        s = nums[0]
        e = nums[-1]
        sf = ef = 0
        for each in nums: 
            if each == s: sf += 1
            elif each == e: ef += 1
        
        if sf == 1 and ef == 1:
            return max(s, e)
        if sf == 1:
            return s
        if ef == 1:
            return e
        return -1