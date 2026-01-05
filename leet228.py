class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        out = []
        temp = [nums[0]]
        i = 0
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                temp.append(nums[i-1])
                out.append(temp[:])
                temp.clear()
                temp.append(nums[i])
        if temp:
            out.append(temp+[nums[i]] if nums[i]-1 == nums[i-1] else temp+temp)
        x = []
        for l, r in out:
            if l == r:
                x.append(str(l))
            else:
                x.append(f"{l}->{r}")
        return x