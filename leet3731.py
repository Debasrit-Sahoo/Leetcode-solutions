class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = mx = nums[0]
        b = 0
        for i in nums:
            b |= 1 << i
            if i > mx:
                mx = i
            elif i < mn:
                mn = i

        return [i for i in range(mn+1, mx) if not b & (1 << i)]