class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for i in nums:
            x = bisect.bisect_left(tail, i)
            if len(tail) == x:
                tail.append(i)
            else:
                tail[x] = i
        return len(tail)