class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums)+1)
        c = 0
        for i in range(len(nums)):
            c += nums[i]; self.arr[i+1] = c

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]
