class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        w = valueDiff + 1
        for i, n in enumerate(nums):
            buc = n // w if not n < 0 else ((n+1)) // w - 1
            if buc in buckets or (buc-1 in buckets and abs(buckets[buc-1]-n) <= valueDiff) or (buc+1 in buckets and abs(buckets[buc+1]-n) <= valueDiff):
                return True
            buckets[buc] = n
            if i >= indexDiff:
                k = nums[i-indexDiff]
                k =  k // w if not k < 0 else ((k+1)) // w - 1
                del buckets[k]
        return False