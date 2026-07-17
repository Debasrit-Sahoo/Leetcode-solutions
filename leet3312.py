class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        mx1 = mx + 1
        freq = [0] * mx1
        pairs = [0] * mx1

        for each in nums:
            freq[each] += 1

        for div in range(1, mx1):
            cnt = 0
            for i in range(div, mx1, div):
                cnt += freq[i]
            pairs[div] = (cnt * (cnt - 1)) >> 1

        for div in range(mx, 0, -1):
            for i in range(div << 1, mx1, div):
                pairs[div] -= pairs[i]

        for i in range(1, mx1):
            pairs[i] += pairs[i-1]

        for i, v in enumerate(queries):
            queries[i] = bisect_right(pairs, v)
        
        return queries