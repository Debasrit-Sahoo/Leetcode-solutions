class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        spec = []

        for each in special:
            s = 0 
            for i in range(n):
                if each[i] > needs[i]:
                    break
                s += each[i] * price[i]
            else:
                if s > each[-1]: spec.append(each)

        @lru_cache(None)
        def dfs(rem):
            if not rem: 
                return 0
            else:
                m = 0
                buf = [None]*n
                for i in range(n):
                    buf[i] = (rem >> (i << 2)) & 0xF
                    m += buf[i] * price[i]

                for offer in spec:
                    new_rem = 0

                    for i in range(n):
                        if offer[i] > buf[i]: break
                        new_rem |= (buf[i] - offer[i]) << (i << 2)

                    else:
                        x = dfs(new_rem) + offer[-1]
                        if x < m: m = x
            return m
        
        r = 0
        for i in range(n):
            r |= needs[i] << (i << 2)

        return dfs(r)