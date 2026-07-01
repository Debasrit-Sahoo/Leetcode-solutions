class Solution:
    def minCost(self, houses: List[int], costs: List[List[int]], m: int, n: int, target: int) -> int:
        DEF_MAX = 1 << 31
        @lru_cache(None)
        def grass(idx, prev_col, nf):
            if nf > idx + 1: return DEF_MAX
            if idx == -1:
                return 0 if not nf else DEF_MAX

            if houses[idx]:
                if houses[idx] != prev_col:
                    if not nf: return DEF_MAX
                    nf -= 1
                return grass(idx - 1, houses[idx], nf)

            ret = DEF_MAX

            for colors, cost in enumerate(costs[idx]):
                col = colors + 1

                if col == prev_col:
                    t = cost + grass(idx - 1, col, nf)
                    if ret > t: ret = t
                elif nf:
                    t = cost + grass(idx - 1, col, nf - 1)
                    if ret > t: ret = t

            return ret

        if houses[-1]:
            a = grass(m-2, houses[-1], target - 1)

        else:
            a = DEF_MAX
            for colors, cost in enumerate(costs[-1]):
                col = colors + 1
                t = cost + grass(m - 2, col, target - 1)
                if t < a: a = t
            
        return a if a != DEF_MAX else -1

                    

