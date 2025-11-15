def maxProfit(prices):
        total = 0
        cur = 0
        lo, hi = float("inf"), float("-inf")
        for x in prices:
            if x < hi:
                total += cur
                cur = 0
                lo, hi = float("inf"), float("-inf")
            lo = min(lo,x)
            hi = max(hi,x)
            cur = max(cur, hi - lo)
        return total + cur