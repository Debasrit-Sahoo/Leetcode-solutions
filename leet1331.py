class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr = [[v, i] for i, v in enumerate(arr)]
        arr.sort()

        new = [None] * len(arr)
        c = 0
        prev = None
        for val, idx in arr:
            c += prev != val
            new[idx] = c
            prev = val

        return new