class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1: return 0
        rounds = minutesToTest//minutesToDie + 1
        i = 1
        while pow(rounds, i) < buckets: i+=1
        return i