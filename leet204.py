class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        arr = [True]*(n)
        arr[0] = arr[1] = False
        for i in range(2,int(n**0.5)+1):
            if arr[i]:
                for x in range(i*i, n ,i):
                    arr[x] = False
        return sum(arr)