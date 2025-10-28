def mySqrt(x):
        if x == 0:
            return 0
        gi = x
        while abs(gi - ((gi + x / gi)/ 2)) > 0.00001:
            gi = (gi + x / gi)/ 2
        return int(gi)