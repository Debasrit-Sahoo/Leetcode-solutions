class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        a = []
        for m in asteroids:
            if mass < m: a.append(m)
            else: mass += m
        if not a: return True
        a.sort()
        for m in a:
            if mass < m: return False
            mass += m
        return True