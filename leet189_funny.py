class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        i = n - k
        for o in range(n):
            nums.append(nums[(i+o)%n])
        for i in range(n-1, -1, -1):
            nums[i] = nums.pop()