from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < 1 or k < 1:
            return []
        combs = []
        def bt(i: int, l: List, sum: int) -> None:
            if len(l) > k:
                return
            if len(l) == k and sum == n:
                combs.append(l[:])
            for x in range(i+1, 10):
                if sum+x > n:
                    break
                l.append(x)
                bt(x, l, x + sum)
                l.pop()
        bt(0, [], 0)
        return combs