class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        num1 = num1 if num1 > 101 else 101
        num2+=1

        ans = 0

        for num in range(num1, num2):
            num = str(num)
            n = len(num)

            for i in range(1, n - 1):
                if (num[i-1] < num[i] and num[i+1] < num[i]) or (num[i-1] > num[i] and num[i+1] > num[i]):
                    ans += 1
            
        return ans