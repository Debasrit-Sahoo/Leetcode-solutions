class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        co1 = co2 = 0
        for n in nums:
            if n == c1: co1 += 1
            elif n == c2: co2 += 1
            elif co1 == 0: c1, co1 = n, 1
            elif co2 == 0: c2, co2 = n, 1
            else:
                co1 -= 1
                co2 -= 1
        out = []
        co1 = co2 = 0
        for i in nums:
            if i == c1: co1 += 1
            if i == c2: co2 += 1
        if co1 > len(nums)//3: out.append(c1)
        if co2 > len(nums)//3: out.append(c2)
        return out