class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        arr = [10]*(n+1)
        c = cf = 9
        for i in range(2, n+1):
            c *= cf
            cf -= 1
            arr[i] = c + arr[i-1]
        return arr[-1]