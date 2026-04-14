class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = nums1, nums2
        l1, l2 = len(n1)+1, len(n2)+1
        if l1 < l2:
            l1, l2 = l2, l1
            n1, n2 = n2, n1

        dp = [0]*l1

        for i in range(1, l2):
            d = 0
            for j in range(1, l1):
                dp[j], d = 1 + d if n1[j-1] == n2[i-1] else max(dp[j-1], dp[j]), dp[j]

        return dp[-1]