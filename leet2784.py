class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1: return False
        if nums.pop() != nums[-1]: return False
        prev = 0
        for i in nums:
            prev+=1
            if prev != i: return False
        return True