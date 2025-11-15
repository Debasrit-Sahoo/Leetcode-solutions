def maxProfit(prices):
    s1 = s2 = 0
    b1 = b2 = float("-inf")
    for x in prices:
        if -x > b1:
            b1 = -x
        if b1 + x > s1:
            s1 = b1+x
        if s1 - x > b2:
            b2 = s1 - x
        if b2 + x > s2:
            s2 = b2 + x
    return s2