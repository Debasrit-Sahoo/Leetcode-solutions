class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def day(s):
            m, d = map(int, s.split('-'))
            return days[m - 1] + d

        return max(0, min(day(leaveAlice), day(leaveBob)) - max(day(arriveAlice), day(arriveBob)) + 1)