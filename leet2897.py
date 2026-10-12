class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = max(nums).bit_length()
        bits = [0] * n
        for num in nums:
            for sh in range(num.bit_length()):
                bits[sh] += num & 1
                num >>= 1
        ans = 0
        for _ in range(k):
            x = 0
            for sh in range(n):
                if bits[sh]:
                    x |= 1 << sh
                    bits[sh] -= 1
            ans += x ** 2
            ans %= MOD

        return ans