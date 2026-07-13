class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        n = 9
        ans = []

        for size in range(len(str(low)) - 1, n):
            for i in range(n - size):
                cand = int(s[i:i+size+1])
                if cand < low: continue
                if cand > high: break
                ans.append(cand)

        return ans
