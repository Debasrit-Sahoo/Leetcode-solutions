class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        o = 0
        m = 0
        for c in moves:
            if c == '_': m+=1
            elif c == 'L': o-=1
            else: o+=1

        return abs(o) + m