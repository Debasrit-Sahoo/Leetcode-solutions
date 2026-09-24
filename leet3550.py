class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            if i == sum(map(int, str(v))):
                return i
        return -1
