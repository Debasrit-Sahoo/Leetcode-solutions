class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        i = 0
        cnt = 0
        for each in nums:
            if each < target:
                i += 1
            elif each == target:
                cnt += 1

        return [i + j for j in range(cnt)]