class Solution:
    def check(self, nums: List[int]) -> bool:
        mis = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                mis += 1
            
        if not mis: return True
        if mis > 1: return False
        
        return nums[-1] <= nums[0]