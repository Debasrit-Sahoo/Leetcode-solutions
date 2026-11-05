class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        ans = 0

        for a1 in arr1:
            idx = bisect_left(arr2, a1)
            ans += (idx == 0 or a1 - arr2[idx - 1] > d) and (idx == n or arr2[idx] - a1 > d)
        return ans