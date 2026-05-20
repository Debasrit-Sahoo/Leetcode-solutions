class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new = []
        for each in nums:
            new.extend(map(int, list(str(each))))
        return new