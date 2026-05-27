class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        state = [2, 2, 0, 1, 1, 0, 0, 1, 2, 0]
        dp = [-1]*(n+1) #0 == true, 1 == invalid, 2 == unchanged
        for i in range(min(10, n+1)):
            s = state[i]
            if s == 2: dp[i] = 2
            elif s == 0: dp[i] = 0; count+=1
            else: dp[i] = 1

        for u in range(10, n - (n % 10), 10):
            p = dp[u//10]
            if p == 1:
                for l in range(10):
                    dp[u+l] = 1
            elif p == 0:
                for l in range(10):
                    if state[l] != 1: dp[u+l] = 0; count += 1
                    else: dp[u+l] = 1
            else:
                for l in range(10):
                    s = state[l]
                    if s == 2: dp[u+l] = 2
                    elif s == 0: dp[u+l] = 0; count += 1
                    else: dp[u+l] = 1
        if n > 10:
            u = n // 10
            p = dp[u]
            if p == 0:
                for l in range(n%10 + 1):
                    if state[l] != 1: count += 1
            elif p == 2:
                for l in range(n%10 + 1):
                    if state[l] == 0: count+=1

        return count
