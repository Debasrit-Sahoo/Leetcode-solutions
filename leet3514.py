class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = set(nums)
        pairs = set()
        finals = set()
        for i in nums:
            for j in nums:
                pairs.add(i ^ j)

        for k in nums:
            for p in pairs:
                finals.add(k ^ p)

        return len(finals)