def maxProfit(prices):
        lo = float("inf")
        prof = 0
        for x in prices:
            lo = lo if lo < x else x
            prof = prof if prof > x - lo else x - lo
        return prof