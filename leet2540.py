class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]: return -1
        n = len(nums2)
        for i in nums1:
            if i == nums2[j]: return i
            if i < nums2[j]: continue
            while i > nums2[j]:
                j+=1
                if j == n: return -1
                if i == nums2[j]: return i
        return -1
