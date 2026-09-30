class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []

        c1 = c2 = 0

        for char in seq:
            match char:
                case '(':
                    if c1 > c2:
                        c1 -= 1
                        ans.append(0)
                    else:
                        c2 -= 1
                        ans.append(1)
                case _:
                    if c1 < c2:
                        c1 += 1
                        ans.append(0)
                    else:
                        c2 += 1
                        ans.append(1)

        return ans