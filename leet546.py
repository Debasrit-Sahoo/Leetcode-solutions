class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        b = boxes
        n = len(boxes)

        @lru_cache(None)
        def name(l, r, k):
            if (r < l): return 0

            i = 1
            colour = b[l]
            while l + i <= r and colour == b[l+i]: i+=1
            a = (i+k)**2 + name(l+i, r, 0)
            new_l = l + i
            rs = []
            for c in range(new_l, r+1):
                if b[c]==colour and b[c-1]!=colour:
                    x = name(new_l, c - 1, 0) + name(c, r, i+k)
                    if x > a: a = x
            return a
        return name(0, n-1, 0)