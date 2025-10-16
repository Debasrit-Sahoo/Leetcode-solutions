def divide(dividend, divisor):
    def helper(dividend, divisor):
        c = 0
        while divisor << 1 <= dividend:
            divisor = divisor << 1
            c += 1
        return divisor, c
    sign = 1
    if divisor < 0:
        sign = sign*(-1)
        divisor = abs(divisor)
    if dividend < 0:
        sign = sign*(-1)
        dividend = abs(dividend)
    if divisor == 1:
        return sign*dividend
    init = divisor
    q = 0
    while dividend >= init:
        divisor, c = helper(dividend, init)
        q += 1 << c
        dividend = dividend - divisor
    q = sign * q
    if q < -(2**31):
        return -(2**31)
    if q > (2**31 - 1):
        return (2**31 - 1)
    return q

