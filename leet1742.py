class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        arr = [0] * 46

        s = sum(map(int, str(lowLimit)))

        for i in range(lowLimit, highLimit + 1):
            arr[s] += 1

            x = i + 1

            while x % 10 == 0:
                s -= 9
                x //= 10

            s += 1

        return max(arr)