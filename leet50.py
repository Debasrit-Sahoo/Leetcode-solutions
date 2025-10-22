def myPow(x, n):
        if x == 1 or n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        res = x    
        extra = 1
        while n > 1:
            if n % 2 != 0:
                n -= 1
                extra *= res
            res *= res
            n = n >> 1
        return res*extra