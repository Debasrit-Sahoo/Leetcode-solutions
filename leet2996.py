class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = prev = nums[0]
        ht = set([s])
        n = len(nums)
        for i in range(1, n):
            if prev + 1 == nums[i]:
                prev = nums[i]
                s += prev
            else:
                for j in range(i, n):
                    ht.add(nums[j])
                break
        
        while s in ht:
            s += 1
        
        return s