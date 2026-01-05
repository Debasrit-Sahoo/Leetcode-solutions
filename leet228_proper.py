class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        i, j = 0, 1
        prev = nums[0]
        nums.append(nums[-1]+2)
        out = []
        while j < len(nums):
            if prev + 1 != nums[j]:
                out.append(f"{nums[i]}->{nums[j-1]}" if j-i != 1 else str(nums[i]))
                prev = nums[j]
                i = j
            else:
                prev += 1
            j += 1
        return out