class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t  = []
        for i, v in enumerate(index):
            t.insert(v, nums[i])

        return t