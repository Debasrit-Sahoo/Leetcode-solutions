class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = defaultdict(int)
        c = len(citations)
        for i in citations:
            if i >= c:
                count[c] += 1
            else:
                count[i] += 1
        m = 0
        for i in range(c, -1, -1):
            m += count[i]
            if m >= i:
                return i