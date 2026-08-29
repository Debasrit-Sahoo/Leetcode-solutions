class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        arr = sorted((x, i) for i, x in enumerate(nums))

        s = 0
        for e in range(1, n + 1):
            if e == n or arr[e][0] - arr[e-1][0]> limit:

                idxs = sorted(arr[i][1] for i in range(s, e))

                for i, idx in enumerate(idxs):
                    nums[idx] = arr[s + i][0]

                s =  e

        return nums