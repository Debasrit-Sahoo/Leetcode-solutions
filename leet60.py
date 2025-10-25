import math
def getPermutation(n,k):
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        res = []
        while nums:
            block = math.factorial(n-1)
            n -= 1
            i = (k -1) // block
            res.append(nums.pop(i))
            k = k - (i * block)
        s = "".join(map(str, res))
        return s