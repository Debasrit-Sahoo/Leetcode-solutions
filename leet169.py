class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        count = 0
        for i in nums:
            if count == 0:
                cur = i
            if cur == i:
                count += 1
            else:
                count -=1
        return cur