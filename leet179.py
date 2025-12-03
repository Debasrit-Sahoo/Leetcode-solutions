from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):#9534330
        def comparator(a, b):
            if a+b > b+a:
                return -1
            if a+b < b+a:
                return 1
            return 0
        map(str,nums)
        nums.sort(key=cmp_to_key(comparator))
        return "".join(nums)