class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        s = len(num)
        def dfs(l1, l2, idx, f):
            print(l1,l2)
            if idx == s and f: return True
            n = l1 + l2
            new = str(n)
            L = len(new)
            if idx + L <= s and num[idx:idx+L] == new:
                return dfs(l2, n, idx+L, True)
            return False
        
        for i in range(s):
            if num[0] == '0' and i > 0: break
            for j in range(i+1, s):
                if num[i+1] == '0' and j > i+1: continue
                l1 = int(num[0:i+1])
                l2 = int(num[i+1:j+1])
                if dfs(l1 ,l2, j+1, False): return True
        return False