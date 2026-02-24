class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for i in envelopes:
            x = bisect.bisect_left(tails, i[1])
            if x == len(tails):
                tails.append(i[1])
            else:
                tails[x] = i[1]
        return len(tails)