class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        factors = set()
        n = len(nums)

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)

        for i in range(1, n):
            if nums[i - 1] > nums[i]: break
        else:
            return sum(factors)

        print(factors)

        factors.discard(1)

        sorted_nums = sorted(nums)
        ans = 0

        for k in factors:
            for i in range(0, n, k):

                idx = 0
                for j in range(i+1, i + k):
                    if nums[j-1] > nums[j]:
                        idx = j
                        break
                else:
                    if nums[i + k - 1] > nums[i]:
                        idx = i

                if not all(nums[i + (j - i + idx) % k] == sorted_nums[j] for j in range(i, i + k)): break
            else:
                ans += k

        return ans