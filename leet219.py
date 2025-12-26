class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            window.add(n)
            if i-k > -1: window.remove(nums[i-k])
        return False