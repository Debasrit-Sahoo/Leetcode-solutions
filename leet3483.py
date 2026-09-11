class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        dig = [0] * 10
        for d in digits: dig[d] += 1
        ans = 0
        for i in range(0, 10, 2):
            if not dig[i]: continue
            dig[i] -= 1
            for j in range(1, 10):
                if not dig[j]: continue
                dig[j] -= 1
                ans += sum(1 for a in dig if a)
                dig[j] += 1
            dig[i] += 1

        return ans