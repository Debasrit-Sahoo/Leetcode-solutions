class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4: return False

        matchsticks.sort(reverse=True)
        l = len(matchsticks)
        t = s // 4
        if matchsticks[0] > t: return False
        sides = [0, 0, 0, 0]

        def d(i):
            if i == l: return True
            for s in range(4):
                side = sides[s]
                v = matchsticks[i]
                if not ((side + v > t) or (s > 0 and sides[s] == sides[s-1])):
                    sides[s] += v
                    if d(i+1): return True
                    sides[s] = side
                
                if side == 0:
                    break
            return False


        return d(0)


