class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        new = sorted(nums, key = lambda x: (sum(int(c) for c in str(x)), x))
        dest = {num : idx for idx, num in enumerate(new)}

        n = len(nums)
        cyc = 0
        seen = [False] * n
        for i in range(n):
            if seen[i]: continue

            k = i
            while not seen[k]:
                seen[k] = True
                k = dest[nums[k]]

            cyc += 1

        return n - cyc