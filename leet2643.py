class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r = m = -1
        for i, v in enumerate(mat):
            x = v.count(1)
            if x > m: r = i; m = x

        return [r, m]