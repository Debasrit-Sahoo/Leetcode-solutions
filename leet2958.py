class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = ans = 0

        for r, x in enumerate(nums):
            freq[x] += 1

            while freq[x] > k:
                freq[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans